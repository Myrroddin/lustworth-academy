param(
    [switch]$DryRun,
    [string]$GameRoot
)

$scriptPath = $MyInvocation.MyCommand.Path
$scriptDir = Split-Path -Parent $scriptPath
$pythonScript = Join-Path $scriptDir "remove_all_mp3_from_game_audio.py"

if (-not (Test-Path -LiteralPath $pythonScript -PathType Leaf)) {
    Write-Error "Python cleanup script not found: $pythonScript"
    exit 1
}

$pythonExe = $null
$pythonArgs = @()

if (Get-Command py -ErrorAction SilentlyContinue) {
    $pythonExe = "py"
    $pythonArgs = @("-3")
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $pythonExe = "python"
}
elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
    $pythonExe = "python3"
}

if (-not $pythonExe) {
    Write-Error "Python 3 was not found in PATH. Install Python 3 to run this tool."
    exit 1
}

$invokeArgs = @()
$invokeArgs += $pythonArgs
$invokeArgs += $pythonScript

if ($DryRun) {
    $invokeArgs += "--dry-run"
}

if ($GameRoot) {
    $resolvedGameRoot = (Resolve-Path -LiteralPath $GameRoot -ErrorAction Stop).Path
    $invokeArgs += "--game-root"
    $invokeArgs += $resolvedGameRoot
}

& $pythonExe @invokeArgs
exit $LASTEXITCODE
