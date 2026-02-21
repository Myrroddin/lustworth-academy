#!/usr/bin/env python3
"""Repair missing legacy image refs by swapping to available .webp equivalents.

This script is intentionally narrow:
- It only changes refs that currently point to missing png/jpg files.
- It changes them only when a matching webp path exists.
- It preserves known launcher/icon exceptions.
"""

from __future__ import annotations

from pathlib import Path
import re

REPO = Path(__file__).resolve().parents[1]
GAME = REPO / "game"
SCRIPT_EXTS = {".rpy", ".rpym", ".py"}
REF_RE = re.compile(r"([\"'])(?P<path>[^\"']+?\.(?:png|jpe?g))\1", re.IGNORECASE)
EXT_RE = re.compile(r"\.(?:png|jpe?g)$", re.IGNORECASE)
PRESERVE = {"gui/window_icon.png"}


def glob_from_template(path: str) -> str:
    """Convert templated Ren'Py path patterns into filesystem glob patterns."""
    text = path
    text = text.replace("%s", "*")
    text = re.sub(r"\[[^\]]+\]", "*", text)
    text = re.sub(r"\{[^\}]+\}", "*", text)
    return text


def exists_for_ref(path: str, root: Path) -> bool:
    """Check whether a literal or templated asset reference resolves on disk."""
    if any(tok in path for tok in ("%s", "[", "{", "*", "?")):
        pattern = glob_from_template(path)
        return any(root.glob(pattern))
    return (root / path).exists()


def main() -> int:
    """CLI entrypoint for repairing missing png/jpg refs to webp."""
    scripts = [p for p in GAME.rglob("*") if p.is_file() and p.suffix.lower() in SCRIPT_EXTS]

    files_changed = 0
    refs_updated = 0

    for script in scripts:
        original = script.read_text(encoding="utf-8")

        def repl(m: re.Match[str]) -> str:
            # Replacement callback for each quoted png/jpg reference.
            nonlocal refs_updated
            quote = m.group(1)
            rel = m.group("path")

            if rel.lower() in {p.lower() for p in PRESERVE}:
                return m.group(0)

            # Keep reference untouched if the legacy file still exists.
            legacy_exists = exists_for_ref(rel, GAME) or exists_for_ref(rel, REPO)
            if legacy_exists:
                return m.group(0)

            # Only switch to webp when the target exists.
            webp_rel = EXT_RE.sub(".webp", rel)
            webp_exists = exists_for_ref(webp_rel, GAME) or exists_for_ref(webp_rel, REPO)
            if not webp_exists:
                return m.group(0)

            refs_updated += 1
            return f"{quote}{webp_rel}{quote}"

        updated = REF_RE.sub(repl, original)
        if updated != original:
            script.write_text(updated, encoding="utf-8")
            files_changed += 1

    print(f"Script files scanned: {len(scripts)}")
    print(f"Script files updated: {files_changed}")
    print(f"Legacy refs switched to webp: {refs_updated}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
