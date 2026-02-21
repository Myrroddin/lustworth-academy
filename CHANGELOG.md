# Changelog

## [1.00] - 2026-02-20

### Added
- GitHub Actions release workflow: `.github/workflows/release.yml`
- Manual release trigger with inputs for `version`, `include_tools_patch`, and `prerelease`
- Automatic release trigger on pushed version tags (for example `v1.00`)
- Automated release assets:
  - `lustworth-academy-v<version>-game.patch`
  - `lustworth-academy-v<version>-game-tools.patch` (optional)
  - `lustworth-academy-v<version>-SHA256SUMS.txt`

### Changed
- README updated to show patch version **1.00** near the top
- README maintainer workflow updated to use GitHub Releases automation
- Release patch scope clarified:
  - Default artifact: `game/` only
  - Optional artifact: `game/` + `tools/`
- Explicit exclusion policy documented for release patches: `renpy/`, `lib/`, `README.md`, `LICENSE`, and other non-patch files
- README now documents maintainer helper scripts and recommended run order
- Automatic tag releases now default to including the tools patch

### Fixed
- Removed duplicate PowerShell attribute declaration in `tools/remove_obsolete_mp3.ps1`