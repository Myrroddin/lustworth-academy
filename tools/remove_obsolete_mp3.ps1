[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$AudioRoot = "game/audio"
)

if (-not (Test-Path -LiteralPath $AudioRoot)) {
    throw "Audio root not found: $AudioRoot"
}

$mp3Files = Get-ChildItem -LiteralPath $AudioRoot -Recurse -File -Filter *.mp3
$removed = 0
$skippedNoOgg = 0

foreach ($mp3 in $mp3Files) {
    $oggPath = [System.IO.Path]::ChangeExtension($mp3.FullName, ".ogg")

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

Write-Host "Scanned .mp3 files: $($mp3Files.Count)"
Write-Host "Removed .mp3 files: $removed"
Write-Host "Skipped (no .ogg counterpart): $skippedNoOgg"
