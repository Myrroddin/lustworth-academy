# Lustworth Academy — Unofficial Patch

Repository patch version: **v1.03**

An unofficial fan patch for the visual novel *Lustworth Academy*. This repository
contains only the changes (patches, corrected scripts, and converted assets) made
on top of the original game. It does **not** redistribute the original game or any
of its copyrighted assets.

When you download release files, use the version number shown on the latest
GitHub Release page.

## Table of contents

- [Compatible game versions](#compatible-game-versions)
- [Why WebP and OGG formats?](#why-webp-and-ogg-formats)
- [What this patch does](#what-this-patch-does)
- [Legal notice](#legal-notice)
- [How to apply the patch](#how-to-apply-the-patch)
- [Create a release](#create-a-release)
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

These release assets are intended for the original game developer, or anyone
maintaining a game tree that already includes the previous patch release.
They are not packaged as a first-time end-user installer for a clean official
game copy.

### Before you start

1. Install Git on your computer.
2. Open the latest GitHub Release for this repository.
3. Make sure your game tree already matches the previous patch release.
4. Go to the main game folder.

You are in the correct folder if you can see `game/` there.

### Choose which release files to download

- `lustworth-academy-v<version>-game.patch`
  This is the incremental patch for the tracked files under `game/`.
- `lustworth-academy-v<version>-tools.zip`
  This is a zip of the tracked helper scripts in `tools/`.
- `lustworth-academy-v<version>-SHA256SUMS.txt`
  This contains SHA256 checksums for the release assets.

Most release consumers only need `game.patch`.
`tools.zip` is only needed when you also want the helper scripts.

### Apply the patch file

`game.patch` updates a tree from the previous patch tag to the tagged release
version. If your current tree does not already match the previous release,
bring it up to that version first.

Run this command from the game folder.

Replace `/path/to/...` with the real path to the patch file you downloaded.

```bash
git apply --binary "/path/to/lustworth-academy-v<version>-game.patch"
```

After that:

1. Start the game.
2. Make sure the game opens normally.
3. If you only wanted the patch, you are done.
4. If you also downloaded `tools.zip`, extract it and use the optional cleanup tools below.

### Optional cleanup tools

`tools.zip` contains the cleanup tools in `tools/audio/` and `tools/images/`.

Extract that zip anywhere you want.
The examples below assume the zip contents are available under `tools/`, and that you pass the target game folder with `--game-root` or `-GameRoot`.

Before you run any cleanup tool:

1. Open a terminal where the extracted `tools/` folder is available.
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
powershell -ExecutionPolicy Bypass -File .\tools\audio\remove_all_mp3_from_game_audio_windows.ps1 -GameRoot "C:\path\to\game" -DryRun
```

Real run:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\audio\remove_all_mp3_from_game_audio_windows.ps1 -GameRoot "C:\path\to\game"
```

#### macOS Audio Tool

Use this file:
`tools/audio/remove_all_mp3_from_game_audio_macos.command`

Dry run:

```bash
bash ./tools/audio/remove_all_mp3_from_game_audio_macos.command --game-root "/path/to/game" --dry-run
```

Real run:

```bash
bash ./tools/audio/remove_all_mp3_from_game_audio_macos.command --game-root "/path/to/game"
```

#### Linux Audio Tool

Use this file:
`tools/audio/remove_all_mp3_from_game_audio_linux.sh`

Dry run:

```bash
bash ./tools/audio/remove_all_mp3_from_game_audio_linux.sh --game-root "/path/to/game" --dry-run
```

Real run:

```bash
bash ./tools/audio/remove_all_mp3_from_game_audio_linux.sh --game-root "/path/to/game"
```

#### One Audio Tool That Works on Every OS

If Python is already installed, you can use this file instead:
`tools/audio/remove_all_mp3_from_game_audio.py`

Dry run:

```bash
python ./tools/audio/remove_all_mp3_from_game_audio.py --game-root "/path/to/game" --dry-run
```

Real run:

```bash
python ./tools/audio/remove_all_mp3_from_game_audio.py --game-root "/path/to/game"
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
powershell -ExecutionPolicy Bypass -File .\tools\images\remove_png_with_matching_webp_from_game_images_windows.ps1 -GameRoot "C:\path\to\game" -DryRun
```

Real run:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\images\remove_png_with_matching_webp_from_game_images_windows.ps1 -GameRoot "C:\path\to\game"
```

#### macOS Image Tool

Use this file:
`tools/images/remove_png_with_matching_webp_from_game_images_macos.command`

Dry run:

```bash
bash ./tools/images/remove_png_with_matching_webp_from_game_images_macos.command --game-root "/path/to/game" --dry-run
```

Real run:

```bash
bash ./tools/images/remove_png_with_matching_webp_from_game_images_macos.command --game-root "/path/to/game"
```

#### Linux Image Tool

Use this file:
`tools/images/remove_png_with_matching_webp_from_game_images_linux.sh`

Dry run:

```bash
bash ./tools/images/remove_png_with_matching_webp_from_game_images_linux.sh --game-root "/path/to/game" --dry-run
```

Real run:

```bash
bash ./tools/images/remove_png_with_matching_webp_from_game_images_linux.sh --game-root "/path/to/game"
```

#### One Image Tool That Works on Every OS

If Python is already installed, you can use this file instead:
`tools/images/remove_png_with_matching_webp_from_game_images.py`

Dry run:

```bash
python ./tools/images/remove_png_with_matching_webp_from_game_images.py --game-root "/path/to/game" --dry-run
```

Real run:

```bash
python ./tools/images/remove_png_with_matching_webp_from_game_images.py --game-root "/path/to/game"
```

### What `tools.zip` adds right now

At the moment, `tools.zip` adds:

- audio cleanup tools in `tools/audio/`
- image cleanup tools in `tools/images/`

## Create a release

The GitHub Actions workflow in `.github/workflows/release.yml` builds the
release assets automatically when you push a tag like `v1.03`.

Normal release flow:

1. Commit your latest changes.
2. In VS Code Source Control, create and push a tag such as `v1.03`.
3. Wait for the **Create GitHub Release** workflow to finish.
4. Open the GitHub Release page.
5. Download or share `lustworth-academy-v<version>-game.patch`, `lustworth-academy-v<version>-tools.zip`, and `lustworth-academy-v<version>-SHA256SUMS.txt`.

If needed, you can also run the workflow manually from GitHub Actions.

These release patches intentionally exclude `renpy/`, `lib/`, `README.md`,
`LICENSE`, and other non-patch files.

## Contributing

Pull requests that are limited to the scope described above (spelling/grammar
fixes, asset conversion, code optimisations) are welcome. Please do **not**
include any original game files in your contributions.

## Acknowledgements

All credit for the original game, story, artwork, and music belongs to the
*Lustworth Academy* development team.
