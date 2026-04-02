#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]
AUDIO_ROOT = REPO_ROOT / "game" / "audio"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Delete every .mp3 file under game/audio recursively.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List matching files without deleting them.",
    )
    return parser.parse_args()


def find_mp3_files(audio_root: Path) -> list[Path]:
    return sorted(
        path
        for path in audio_root.rglob("*")
        if path.is_file() and path.suffix.lower() == ".mp3"
    )


def remove_mp3_files(mp3_files: list[Path], dry_run: bool) -> list[tuple[Path, OSError]]:
    failures: list[tuple[Path, OSError]] = []
    action = "Would delete" if dry_run else "Deleting"

    for path in mp3_files:
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

    if not AUDIO_ROOT.is_dir():
        print(f"Audio folder not found: {AUDIO_ROOT}", file=sys.stderr)
        return 1

    mp3_files = find_mp3_files(AUDIO_ROOT)

    if not mp3_files:
        print(f"No MP3 files found under {AUDIO_ROOT.relative_to(REPO_ROOT).as_posix()}")
        return 0

    failures = remove_mp3_files(mp3_files, args.dry_run)

    print(f"Scanned: {AUDIO_ROOT.relative_to(REPO_ROOT).as_posix()}")
    print(f"Found MP3 files: {len(mp3_files)}")

    if args.dry_run:
        print("Dry run only. No files were deleted.")
        return 0

    if failures:
        print(f"Failed deletions: {len(failures)}", file=sys.stderr)
        for path, exc in failures:
            print(f"{path.relative_to(REPO_ROOT).as_posix()}: {exc}", file=sys.stderr)
        return 1

    print("Deleted all MP3 files successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())