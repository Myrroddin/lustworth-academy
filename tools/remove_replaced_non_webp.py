#!/usr/bin/env python3
"""Remove non-webp images replaced by same-directory .webp files.

Design goals:
- Keep behavior predictable and conservative.
- Avoid deleting likely launcher/build icon assets.
- Never infer destinations across folders; only same-directory replacements.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import fnmatch


DEFAULT_EXTS = {".png", ".jpg", ".jpeg"}
DEFAULT_PRESERVE_PATTERNS = [
    # Common icon patterns to keep by default.
    "*/window_icon.png",
    "*/icon.png",
    "*/icon_*.png",
    "*/icons/*.png",
]


def is_preserved(path: Path, patterns: list[str]) -> bool:
    """Return True when a file path matches a protection pattern."""
    normalized = path.as_posix().lower()
    return any(fnmatch.fnmatch(normalized, pattern.lower()) for pattern in patterns)


def main() -> int:
    """CLI entrypoint for conservative legacy image cleanup."""
    parser = argparse.ArgumentParser(
        description="Remove non-webp image files only when a same-name .webp exists in the same directory."
    )
    parser.add_argument("--root", default="game", help="Root directory to scan (default: game)")
    parser.add_argument("--dry-run", action="store_true", help="Preview actions without deleting files")
    parser.add_argument(
        "--extensions",
        default="png,jpg,jpeg",
        help="Comma-separated non-webp extensions to evaluate (default: png,jpg,jpeg)",
    )
    parser.add_argument(
        "--preserve-pattern",
        action="append",
        default=[],
        help="Additional glob pattern(s) to preserve from deletion",
    )
    args = parser.parse_args()

    # Validate scan root.
    root = Path(args.root)
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Scan root not found: {root}")

    # Parse extension list from CLI.
    exts = {f".{ext.strip().lower().lstrip('.')}" for ext in args.extensions.split(",") if ext.strip()}
    if not exts:
        exts = set(DEFAULT_EXTS)

    # Merge default + caller-supplied safety patterns.
    preserve_patterns = DEFAULT_PRESERVE_PATTERNS + args.preserve_pattern

    scanned = 0
    preserved = 0
    removable: list[Path] = []

    for path in root.rglob("*"):
        # Only process selected legacy image file types.
        if not path.is_file():
            continue
        if path.suffix.lower() not in exts:
            continue

        scanned += 1
        rel = path.relative_to(root)

        if is_preserved(rel, preserve_patterns):
            preserved += 1
            continue

        # Safe rule: remove only when replacement is in the same folder.
        webp = path.with_suffix(".webp")
        if webp.exists():
            removable.append(path)

    removed = 0
    for path in removable:
        # Dry-run prints proposed actions without deleting.
        if args.dry_run:
            print(f"DRY-RUN: would remove {path.as_posix()}")
        else:
            path.unlink()
            removed += 1

    print(f"Scanned non-webp candidates: {scanned}")
    print(f"Preserved by icon/safety patterns: {preserved}")
    print(f"Matched same-dir .webp replacements: {len(removable)}")
    print(f"Removed files: {removed}")
    if args.dry_run:
        print("Mode: dry-run")
    else:
        print("Mode: apply")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
