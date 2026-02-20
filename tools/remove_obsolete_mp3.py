#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Remove obsolete .mp3 files when a same-name .ogg exists in the same directory."
    )
    parser.add_argument(
        "--audio-root",
        default="game/audio",
        help="Audio root directory to scan (default: game/audio)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be removed without deleting files.",
    )
    args = parser.parse_args()

    audio_root = Path(args.audio_root)
    if not audio_root.exists() or not audio_root.is_dir():
        raise SystemExit(f"Audio root not found: {audio_root}")

    mp3_files = sorted(audio_root.rglob("*.mp3"))
    removable: list[Path] = []
    skipped_no_ogg = 0

    for mp3_file in mp3_files:
        ogg_file = mp3_file.with_suffix(".ogg")
        if ogg_file.exists():
            removable.append(mp3_file)
        else:
            skipped_no_ogg += 1

    removed = 0
    for mp3_file in removable:
        if args.dry_run:
            print(f"DRY-RUN: would remove {mp3_file.as_posix()}")
        else:
            mp3_file.unlink()
            removed += 1

    print(f"Scanned .mp3 files: {len(mp3_files)}")
    print(f"Matched .ogg counterpart: {len(removable)}")
    print(f"Removed .mp3 files: {removed}")
    print(f"Skipped (no .ogg counterpart): {skipped_no_ogg}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
