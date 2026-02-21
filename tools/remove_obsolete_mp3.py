#!/usr/bin/env python3
"""Remove legacy .mp3 files when same-name .ogg files exist.

This script is cross-platform and intentionally conservative:
- It only touches .mp3 files under the selected root.
- A file is removable only if `<name>.ogg` exists in the same directory.
- `--dry-run` prints planned deletions without changing files.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    """CLI entrypoint for safe mp3 cleanup."""
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

    # Validate input root early.
    audio_root = Path(args.audio_root)
    if not audio_root.exists() or not audio_root.is_dir():
        raise SystemExit(f"Audio root not found: {audio_root}")

    # Collect candidate mp3 files.
    mp3_files = sorted(audio_root.rglob("*.mp3"))
    removable: list[Path] = []
    skipped_no_ogg = 0

    for mp3_file in mp3_files:
        # Same-directory replacement convention.
        ogg_file = mp3_file.with_suffix(".ogg")
        if ogg_file.exists():
            removable.append(mp3_file)
        else:
            skipped_no_ogg += 1

    # Apply deletes (or print planned actions for dry-run).
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
