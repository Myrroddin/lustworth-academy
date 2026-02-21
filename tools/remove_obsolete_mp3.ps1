#
# remove_obsolete_mp3.ps1
# -----------------------
# Purpose:
#   Remove legacy .mp3 files only when a same-name .ogg exists in the same folder.
#
# Safety model:
#   - Never removes files without a confirmed .ogg counterpart.
#   - Supports WhatIf/Confirm via SupportsShouldProcess.
#
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    # Root folder containing audio assets to scan.
    [string]$AudioRoot = "game/audio"
)

# Fail fast if the target path is invalid.
if (-not (Test-Path -LiteralPath $AudioRoot)) {
    throw "Audio root not found: $AudioRoot"
}

# Enumerate all mp3 files recursively.
$mp3Files = Get-ChildItem -LiteralPath $AudioRoot -Recurse -File -Filter *.mp3
$removed = 0
$skippedNoOgg = 0

foreach ($mp3 in $mp3Files) {
    # Convert `x.mp3` to `x.ogg` in the same directory.
    $oggPath = [System.IO.Path]::ChangeExtension($mp3.FullName, ".ogg")

    # Remove only if the replacement file exists.
    if (Test-Path -LiteralPath $oggPath) {
        if ($PSCmdlet.ShouldProcess($mp3.FullName, "Remove obsolete .mp3 (found .ogg counterpart)")) {
            Remove-Item -LiteralPath $mp3.FullName -Force
            $removed++
        }
    }
    else {
        $skippedNoOgg++
    }
}

# Final summary for logs/CI output.
Write-Host "Scanned .mp3 files: $($mp3Files.Count)"
Write-Host "Removed .mp3 files: $removed"
Write-Host "Skipped (no .ogg counterpart): $skippedNoOgg"
