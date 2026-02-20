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

## Contributing

Pull requests that are limited to the scope described above (spelling/grammar
fixes, asset conversion, code optimisations) are welcome. Please do **not**
include any original game files in your contributions.

### Files to commit

**Do commit** files that are part of the patch itself:

| File type | Example paths | Purpose |
|-----------|---------------|---------|
| Ren'Py script patches | `game/*.rpy` | Spelling/grammar fixes, code clean-up |
| Patch / diff files | `*.patch`, `*.diff` | Portable change sets for manual application |
| Converted audio | `game/audio/**/*.ogg` | Replacement audio in the more efficient Ogg Vorbis format |
| Converted images | `game/images/**/*.webp`, `game/gui/**/*.webp` | Replacement images in the more efficient WebP format |
| Conversion / helper scripts | `scripts/` | Tools used to produce the converted assets |
| Documentation | `README.md`, `LICENSE`, `CONTRIBUTING.md` | Project documentation |

**Do not commit** anything that ships with the original game or is generated
at runtime:

- Original, unmodified game scripts (`.rpy`) — only commit files you have
  actually changed
- Original audio and image assets in their source formats (`.mp3`, `.ogg`,
  `.png`, `.jpg`, etc.) — the converted replacements go in instead
- Compiled Ren'Py bytecode (`*.rpyc`, `*.rpymc`)
- Compiled Ren'Py archives (`*.rpa`)
- The `renpy/` engine directory
- Save data and cache (`game/saves/`, `game/cache/`)
- Log files (`log.txt`, `errors.txt`, `traceback.txt`)
- OS and editor artefacts (`.DS_Store`, `Thumbs.db`, `.vscode/`, `.idea/`)

These exclusions are already listed in `.gitignore`, so Git will ignore them
automatically. If you are unsure whether a file belongs in the repository, run
`git status` — untracked files that are not greyed out (i.e. not ignored) are
candidates for committing.

## Acknowledgements

All credit for the original game, story, artwork, and music belongs to the
*Lustworth Academy* development team.