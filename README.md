# Lustworth Academy — Unofficial Patch

Patch version: **v1.03**

An unofficial fan patch for the visual novel *Lustworth Academy*. This repository
contains only the changes (patches, corrected scripts, and converted assets) made
on top of the original game. It does **not** redistribute the original game or any
of its copyrighted assets.

## Table of contents

- [Compatible game versions](#compatible-game-versions)
- [Why WebP and OGG formats?](#why-webp-and-ogg-formats)
- [What this patch does](#what-this-patch-does)
- [Legal notice](#legal-notice)
- [How to apply the patch](#how-to-apply-the-patch)
- [Generate current patch file (maintainer workflow)](#generate-current-patch-file-maintainer-workflow)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Compatible game versions

This patch is intended for *Lustworth Academy* v0.5.5 Extended Edition.
Do not apply it to earlier or later editions.
If you do, you may need to fix bugs manually.

## Why WebP and OGG formats?

For details on why Lustworth Academy uses WebP for images and OGG for audio (instead of ASIF or MP3), see the [format rationale](format_rationale.md).

## What this patch does

- Updates `.rpy` script files to use `.ogg` audio files instead of `.mp3` files
- Updates `.rpy` script files to use `.webp` image files instead of older image formats
- Corrects English spelling and grammar throughout the scripts
- Includes miscellaneous code clean-up and optimisations
- Updates game script files to make future translation work easier

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

### Before you start

1. Install *Lustworth Academy* from its official source.
2. Open the latest GitHub Release for this repository.
3. Go to the main game folder.

You are in the correct folder if you can see `game/` there.

### Choose which patch file to download

- `lustworth-academy-v<version>-game.patch`
  Use this if you only want the patch.
- `lustworth-academy-v<version>-game-tools.patch`
  Use this if you also want the helper tools in `tools/`.

Important:

1. `game-tools.patch` already includes the normal game patch changes.
2. Do **not** apply both patch files.
3. Pick **one** patch file only.

### Apply the patch file

Run one of these commands from the game folder.

If you chose the normal patch:

```bash
git apply --binary /path/to/lustworth-academy-v<version>-game.patch
```

If you chose the tools patch:

```bash
git apply --binary /path/to/lustworth-academy-v<version>-game-tools.patch
```

After that:

1. Start the game.
2. Make sure the game opens normally.
3. If you used `game.patch`, you are done.
4. If you used `game-tools.patch`, you may also use the optional cleanup tools below.

### Optional cleanup tools

Use the cleanup tools only if you already applied
`lustworth-academy-v<version>-game-tools.patch`.

That tools patch adds the files in `tools/audio/` and `tools/images/`.

Before you run any cleanup tool:

1. Open a terminal in the same game folder where you ran `git apply`.
2. Pick **one** file only for the task you want to run.
3. Do **not** run every file in the folder. Files for the same task do the same job.
4. Run the dry run first.
5. If the dry run looks correct, run the real command.

### Optional: remove `.mp3` files from `game/audio/`

This step removes `.mp3` files from `game/audio/` and all subfolders.

#### Windows Audio Tool

Use this file:
`tools/audio/remove_all_mp3_from_game_audio_windows.ps1`

Dry run:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\audio\remove_all_mp3_from_game_audio_windows.ps1 -DryRun
```

Real run:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\audio\remove_all_mp3_from_game_audio_windows.ps1
```

#### macOS Audio Tool

Use this file:
`tools/audio/remove_all_mp3_from_game_audio_macos.command`

Dry run:

```bash
bash ./tools/audio/remove_all_mp3_from_game_audio_macos.command --dry-run
```

Real run:

```bash
bash ./tools/audio/remove_all_mp3_from_game_audio_macos.command
```

#### Linux Audio Tool

Use this file:
`tools/audio/remove_all_mp3_from_game_audio_linux.sh`

Dry run:

```bash
bash ./tools/audio/remove_all_mp3_from_game_audio_linux.sh --dry-run
```

Real run:

```bash
bash ./tools/audio/remove_all_mp3_from_game_audio_linux.sh
```

#### One Audio Tool That Works on Every OS

If Python is already installed, you can use this file instead:
`tools/audio/remove_all_mp3_from_game_audio.py`

Dry run:

```bash
python ./tools/audio/remove_all_mp3_from_game_audio.py --dry-run
```

Real run:

```bash
python ./tools/audio/remove_all_mp3_from_game_audio.py
```

### Optional: remove matching `.png` files from `game/`

This step scans `game/` and its subfolders only.

It removes a `.png` file only when all of these are true:

1. A `.webp` file with the same file name exists in the same folder.
2. The `.png` and `.webp` files have the same image dimensions.

This tool does **not** scan `lib/`, because `lib/` is outside `game/`.

#### Windows Image Tool

Use this file:
`tools/images/remove_png_with_matching_webp_from_game_images_windows.ps1`

Dry run:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\images\remove_png_with_matching_webp_from_game_images_windows.ps1 -DryRun
```

Real run:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\images\remove_png_with_matching_webp_from_game_images_windows.ps1
```

#### macOS Image Tool

Use this file:
`tools/images/remove_png_with_matching_webp_from_game_images_macos.command`

Dry run:

```bash
bash ./tools/images/remove_png_with_matching_webp_from_game_images_macos.command --dry-run
```

Real run:

```bash
bash ./tools/images/remove_png_with_matching_webp_from_game_images_macos.command
```

#### Linux Image Tool

Use this file:
`tools/images/remove_png_with_matching_webp_from_game_images_linux.sh`

Dry run:

```bash
bash ./tools/images/remove_png_with_matching_webp_from_game_images_linux.sh --dry-run
```

Real run:

```bash
bash ./tools/images/remove_png_with_matching_webp_from_game_images_linux.sh
```

#### One Image Tool That Works on Every OS

If Python is already installed, you can use this file instead:
`tools/images/remove_png_with_matching_webp_from_game_images.py`

Dry run:

```bash
python ./tools/images/remove_png_with_matching_webp_from_game_images.py --dry-run
```

Real run:

```bash
python ./tools/images/remove_png_with_matching_webp_from_game_images.py
```

### What the tools patch adds right now

At the moment, the tools patch adds:

- audio cleanup tools in `tools/audio/`
- image cleanup tools in `tools/images/`

## Generate current patch file (maintainer workflow)

This section is only for maintainers.

Use the GitHub Actions workflow in `.github/workflows/release.yml` to build the
release patch files.

The workflow can create two release files:

- `lustworth-academy-v<version>-game.patch`
  This is the normal patch.
- `lustworth-academy-v<version>-game-tools.patch`
  This is the normal patch plus the files in `tools/`.

Important:

1. `game-tools.patch` includes the normal patch too.
2. End users should download only one patch file.

You can trigger the workflow in two ways:

1. Manually from GitHub Actions.
2. Automatically by pushing a tag such as `v1.01`.

Recommended maintainer release flow:

1. Commit your latest changes.
2. Run the **Release Patch Artifacts** workflow with the version number you want.
3. Wait for the workflow to finish.
4. Open the GitHub Release.
5. Check that the patch files were created correctly.
6. Share the release assets.

These release patches intentionally exclude `renpy/`, `lib/`, `README.md`,
`LICENSE`, and other non-patch files.

## Contributing

Pull requests that are limited to the scope described above (spelling/grammar
fixes, asset conversion, code optimisations) are welcome. Please do **not**
include any original game files in your contributions.

## Acknowledgements

All credit for the original game, story, artwork, and music belongs to the
*Lustworth Academy* development team.
