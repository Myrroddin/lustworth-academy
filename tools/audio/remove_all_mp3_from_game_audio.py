#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve()
DEFAULT_GAME_ROOT = SCRIPT_PATH.parents[2] / "game"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Delete every .mp3 file under game/audio recursively.",
    )
    parser.add_argument(
        "--game-root",
        type=Path,
        help="Path to the game directory to clean. Defaults to the repository game directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List matching files without deleting them.",
    )
    return parser.parse_args()


def resolve_game_root(game_root: Path | None) -> Path:
    if game_root is None:
        return DEFAULT_GAME_ROOT.resolve()

    return game_root.expanduser().resolve()


def get_display_root(game_root: Path) -> Path:
    if game_root.name.lower() == "game":
        return game_root.parent

    return game_root


def format_path(path: Path, display_root: Path) -> str:
    try:
        return path.relative_to(display_root).as_posix()
    except ValueError:
        return path.as_posix()


def find_mp3_files(audio_root: Path) -> list[Path]:
    return sorted(
        path
        for path in audio_root.rglob("*")
        if path.is_file() and path.suffix.lower() == ".mp3"
    )


def remove_mp3_files(
    mp3_files: list[Path],
    dry_run: bool,
    display_root: Path,
) -> list[tuple[Path, OSError]]:
    failures: list[tuple[Path, OSError]] = []
    action = "Would delete" if dry_run else "Deleting"

    for path in mp3_files:
        relative_path = format_path(path, display_root)
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
    game_root = resolve_game_root(args.game_root)
    audio_root = game_root / "audio"
    display_root = get_display_root(game_root)

    if not audio_root.is_dir():
        print(f"Audio folder not found: {audio_root}", file=sys.stderr)
        return 1

    mp3_files = find_mp3_files(audio_root)

    if not mp3_files:
        print(f"No MP3 files found under {format_path(audio_root, display_root)}")
        return 0

    failures = remove_mp3_files(mp3_files, args.dry_run, display_root)

    print(f"Scanned: {format_path(audio_root, display_root)}")
    print(f"Found MP3 files: {len(mp3_files)}")

    if args.dry_run:
        print("Dry run only. No files were deleted.")
        return 0

    if failures:
        print(f"Failed deletions: {len(failures)}", file=sys.stderr)
        for path, exc in failures:
            print(f"{format_path(path, display_root)}: {exc}", file=sys.stderr)
        return 1

    print("Deleted all MP3 files successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())