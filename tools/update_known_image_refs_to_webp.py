#!/usr/bin/env python3
"""Update script image refs from png/jpg to webp when conversion is known.

Unlike the missing-ref fixer, this updater does not require legacy files to be
missing first. It updates any legacy reference that has a resolvable webp
counterpart, while preserving explicit icon exceptions.
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
    """Convert templated Ren'Py path expressions to filesystem globs."""
    text = path
    text = text.replace("%s", "*")
    text = re.sub(r"\[[^\]]+\]", "*", text)
    text = re.sub(r"\{[^\}]+\}", "*", text)
    return text


def exists_for_ref(path: str, root: Path) -> bool:
    """Resolve literal or templated asset references against disk."""
    if any(tok in path for tok in ("%s", "[", "{", "*", "?")):
        pattern = glob_from_template(path)
        return any(root.glob(pattern))
    return (root / path).exists()


def main() -> int:
    """CLI entrypoint for safe, known webp substitutions."""
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

            # Convert only when the webp counterpart is known to exist.
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
