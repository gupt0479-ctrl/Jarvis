$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$VaultRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..")
$Cli = Join-Path $ScriptDir "jarvis_ops.py"

$Python = Get-Command python -ErrorAction SilentlyContinue
if (-not $Python) {
    $Python = Get-Command py -ErrorAction SilentlyContinue
}

if (-not $Python) {
    Write-Error "Python was not found on PATH."
    exit 1
}

if ($Python.Name -eq "py.exe" -or $Python.Name -eq "py") {
    & $Python.Source -3 $Cli --root $VaultRoot @args
} else {
    & $Python.Source $Cli --root $VaultRoot @args
}

exit $LASTEXITCODE
