param(
    [switch]$DryRun
)

$scriptPath = $MyInvocation.MyCommand.Path
$toolsDir = Split-Path -Parent $scriptPath
$repoRoot = Split-Path -Parent $toolsDir
$audioRoot = Join-Path $repoRoot "game\audio"

if (-not (Test-Path -LiteralPath $audioRoot -PathType Container)) {
    Write-Error "Audio folder not found: $audioRoot"
    exit 1
}

$mp3Files = @(
    Get-ChildItem -LiteralPath $audioRoot -Recurse -File -Filter *.mp3 |
        Sort-Object FullName
)

if ($mp3Files.Count -eq 0) {
    Write-Output "No MP3 files found under game/audio"
    exit 0
}

$failures = @()

foreach ($file in $mp3Files) {
    $relativePath = $file.FullName.Substring($repoRoot.Length).TrimStart([char]'\\', [char]'/')
    $relativePath = $relativePath.Replace([char]'\\', [char]'/')

    if ($DryRun) {
        Write-Output "Would delete: $relativePath"
        continue
    }

    Write-Output "Deleting: $relativePath"

    try {
        Remove-Item -LiteralPath $file.FullName -Force -ErrorAction Stop
    }
    catch {
        $failures += [pscustomobject]@{
            Path = $relativePath
            Error = $_.Exception.Message
        }
    }
}

Write-Output "Scanned: game/audio"
Write-Output "Found MP3 files: $($mp3Files.Count)"

if ($DryRun) {
    Write-Output "Dry run only. No files were deleted."
    exit 0
}

if ($failures.Count -gt 0) {
    Write-Error "Failed deletions: $($failures.Count)"

    foreach ($failure in $failures) {
        Write-Error "$($failure.Path): $($failure.Error)"
    }

    exit 1
}

Write-Output "Deleted all MP3 files successfully."
