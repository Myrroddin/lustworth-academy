#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[2]
GAME_ROOT = REPO_ROOT / "game"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Delete .png files under game only when a same-name .webp file "
            "exists in the same folder and both images have the same dimensions."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List matching files without deleting them.",
    )
    return parser.parse_args()


def read_png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)

    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("Not a valid PNG file")

    if header[12:16] != b"IHDR":
        raise ValueError("PNG is missing IHDR header")

    width = int.from_bytes(header[16:20], "big")
    height = int.from_bytes(header[20:24], "big")
    return width, height


def read_webp_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(12)

        if len(header) < 12 or header[:4] != b"RIFF" or header[8:12] != b"WEBP":
            raise ValueError("Not a valid WebP file")

        while True:
            chunk_header = handle.read(8)

            if len(chunk_header) == 0:
                break

            if len(chunk_header) < 8:
                raise ValueError("Invalid WebP chunk header")

            chunk_type = chunk_header[:4]
            chunk_size = int.from_bytes(chunk_header[4:8], "little")
            chunk_data = handle.read(chunk_size)

            if len(chunk_data) < chunk_size:
                raise ValueError("Invalid WebP chunk data")

            if chunk_type == b"VP8X":
                if chunk_size < 10:
                    raise ValueError("Invalid VP8X chunk")

                width = 1 + int.from_bytes(chunk_data[4:7], "little")
                height = 1 + int.from_bytes(chunk_data[7:10], "little")
                return width, height

            if chunk_type == b"VP8 ":
                if chunk_size < 10 or chunk_data[3:6] != b"\x9d\x01\x2a":
                    raise ValueError("Invalid VP8 chunk")

                width = int.from_bytes(chunk_data[6:8], "little") & 0x3FFF
                height = int.from_bytes(chunk_data[8:10], "little") & 0x3FFF
                return width, height

            if chunk_type == b"VP8L":
                if chunk_size < 5 or chunk_data[0] != 0x2F:
                    raise ValueError("Invalid VP8L chunk")

                byte_0, byte_1, byte_2, byte_3 = chunk_data[1:5]
                width = 1 + (((byte_1 & 0x3F) << 8) | byte_0)
                height = 1 + (((byte_3 & 0x0F) << 10) | (byte_2 << 2) | ((byte_1 & 0xC0) >> 6))
                return width, height

            if chunk_size % 2 == 1:
                handle.seek(1, 1)

    raise ValueError("Could not determine WebP dimensions")


def find_removable_png_files(
    image_root: Path,
) -> tuple[list[Path], list[Path], list[tuple[Path, tuple[int, int], Path, tuple[int, int]]], list[tuple[Path, Exception]]]:
    removable: list[Path] = []
    missing_webp: list[Path] = []
    mismatched: list[tuple[Path, tuple[int, int], Path, tuple[int, int]]] = []
    errors: list[tuple[Path, Exception]] = []

    for png_path in sorted(image_root.rglob("*.png")):
        if not png_path.is_file():
            continue

        webp_path = png_path.with_suffix(".webp")

        if not webp_path.exists():
            missing_webp.append(png_path)
            continue

        try:
            png_size = read_png_size(png_path)
            webp_size = read_webp_size(webp_path)
        except Exception as exc:
            errors.append((png_path, exc))
            continue

        if png_size == webp_size:
            removable.append(png_path)
        else:
            mismatched.append((png_path, png_size, webp_path, webp_size))

    return removable, missing_webp, mismatched, errors


def remove_png_files(png_files: list[Path], dry_run: bool) -> list[tuple[Path, OSError]]:
    failures: list[tuple[Path, OSError]] = []
    action = "Would delete" if dry_run else "Deleting"

    for path in png_files:
        relative_path = path.relative_to(REPO_ROOT).as_posix()
        print(f"{action}: {relative_path}")

        if dry_run:
            continue

        try:
            path.unlink()
        except OSError as exc:
            failures.append((path, exc))

    return failures


def main() -> int:
    args = parse_args()

    if not GAME_ROOT.is_dir():
        print(f"Game folder not found: {GAME_ROOT}", file=sys.stderr)
        return 1

    removable, missing_webp, mismatched, errors = find_removable_png_files(GAME_ROOT)

    if errors:
        print(f"Failed image reads: {len(errors)}", file=sys.stderr)
        for path, exc in errors:
            print(f"{path.relative_to(REPO_ROOT).as_posix()}: {exc}", file=sys.stderr)
        return 1

    failures = remove_png_files(removable, args.dry_run)

    print(f"Scanned: {GAME_ROOT.relative_to(REPO_ROOT).as_posix()}")
    print(f"Found matching PNG files: {len(removable)}")
    print(f"Skipped without WebP: {len(missing_webp)}")
    print(f"Skipped dimension mismatch: {len(mismatched)}")

    if not removable:
        print("No matching PNG files found under game")
        return 0

    if args.dry_run:
        print("Dry run only. No files were deleted.")
        return 0

    if failures:
        print(f"Failed deletions: {len(failures)}", file=sys.stderr)
        for path, exc in failures:
            print(f"{path.relative_to(REPO_ROOT).as_posix()}: {exc}", file=sys.stderr)
        return 1

    print("Deleted all matching PNG files successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
