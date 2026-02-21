# Lustworth Academy — Unofficial Patch

Patch version: **1.00**

An unofficial fan patch for the visual novel *Lustworth Academy*. This repository
contains only the changes (patches, corrected scripts, and converted assets) made
on top of the original game. It does **not** redistribute the original game or any
of its copyrighted assets.

## Compatible game versions

This patch is intended for *Lustworth Academy* v0.5.4b Extended Edition.
Do not apply it to earlier or later editions.
If you do, you may need to fix bugs manually.

## What this patch does

- Converts audio files to the more efficient `.ogg` format
- Converts image files to the more efficient `.webp` format
- Corrects English spelling and grammar throughout the scripts
- Includes miscellaneous code clean-up and optimisations

## Legal notice

*Lustworth Academy* is the intellectual property of its original developer(s).
The original game ships several components (tooling, libraries, etc.) under the
[MIT License](https://opensource.org/licenses/MIT); please refer to the game's
own "About" screen and bundled licence files for the full details.

The patch code and asset-conversion scripts contained in **this** repository are
released under the MIT License (see [`LICENSE`](LICENSE)). They do not include
any original game content; you must own a legitimate copy of *Lustworth Academy*
to use this patch.

## How to apply the patch

1. Install *Lustworth Academy* from its official source.
2. Clone or download this repository.
3. Run the provided patch script (or apply the `.patch` / `.diff` files manually)
   against your local game installation.
4. Remove obsolete `.mp3` files that were replaced by `.ogg` files.
5. Remove obsolete non-webp image files that were replaced by `.webp` files.

### Step 4 (optional): remove obsolete `.mp3` files

After applying the audio-conversion patch, you can safely remove `.mp3` files that
have `.ogg` counterparts:

```bash
# Cross-platform (Windows/Linux/macOS) dry-run
python ./tools/remove_obsolete_mp3.py --dry-run

# Cross-platform apply cleanup
python ./tools/remove_obsolete_mp3.py
```

On Windows, you can also use PowerShell:

```powershell
# Dry-run (shows what would be removed)
powershell -ExecutionPolicy Bypass -File .\tools\remove_obsolete_mp3.ps1 -WhatIf

# Apply cleanup
powershell -ExecutionPolicy Bypass -File .\tools\remove_obsolete_mp3.ps1
```

The script only removes `.mp3` files when a same-name `.ogg` file exists in the
same directory.

### Step 5 (optional): remove replaced non-webp image files

After converting images, you can remove non-webp files that have a same-name
`.webp` in the same directory.

This cleanup is conservative:

- Only checks same-directory replacements (`name.png` -> `name.webp`)
- Preserves common icon patterns (for launcher/build safety)
- Skips uncertain cases automatically

```bash
# Dry-run
python ./tools/remove_replaced_non_webp.py --dry-run

# Apply cleanup
python ./tools/remove_replaced_non_webp.py
```

## Generate current patch file (maintainer workflow)

Use the GitHub Actions workflow in `.github/workflows/release.yml` to generate
release patch artifacts.

Default release artifact scope:

- `game/` only (developer-facing apply patch)

Optional release artifact scope:

- `game/` + `tools/` (for maintainers who also want helper scripts)

These release patches intentionally exclude `renpy/`, `lib/`, `README.md`,
`LICENSE`, and other non-patch files.

Recommended release flow:

1. Run cleanup dry-run and apply cleanup if needed.
2. Commit your latest changes.
3. Run the **Release Patch Artifacts** workflow with your version (for example `1.00`).
4. Share the generated release assets from GitHub Releases.

## Contributing

Pull requests that are limited to the scope described above (spelling/grammar
fixes, asset conversion, code optimisations) are welcome. Please do **not**
include any original game files in your contributions.

## Acknowledgements

All credit for the original game, story, artwork, and music belongs to the
*Lustworth Academy* development team.