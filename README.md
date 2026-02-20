# Lustworth Academy — Unofficial Patch

An unofficial fan patch for the visual novel *Lustworth Academy*. This repository
contains only the changes (patches, corrected scripts, and converted assets) made
on top of the original game. It does **not** redistribute the original game or any
of its copyrighted assets.

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

### Optional cleanup: remove obsolete `.mp3` files

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

### Generate current patch files

This repo supports two local Git shortcuts for generating patch files:

```bash
# Full cumulative patch (first commit -> HEAD)
git makepatch

# Patch of your new work (origin/main -> HEAD)
git makepatch-main
```

Output files:

- `all-changes-current.patch` (full cumulative patch)
- `all-changes-from-main.patch` (changes since `origin/main`)

Recommended release flow:

1. Run cleanup dry-run and apply cleanup if needed.
2. Commit your latest changes.
3. Run `git makepatch-main` for a developer-facing patch.
4. Optionally run `git makepatch` to archive a full cumulative patch.

## Contributing

Pull requests that are limited to the scope described above (spelling/grammar
fixes, asset conversion, code optimisations) are welcome. Please do **not**
include any original game files in your contributions.

## Acknowledgements

All credit for the original game, story, artwork, and music belongs to the
*Lustworth Academy* development team.