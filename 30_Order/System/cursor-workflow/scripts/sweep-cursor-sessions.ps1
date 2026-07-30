# sweep-cursor-sessions.ps1
# Windows Task Scheduler entrypoint for Cursor session export.
# Cursor sessionEnd hooks for vscode-remote+wsl workspaces execute against the
# WSL user hooks.json, not the Windows one, so they cannot reliably open
# state.vscdb. This sweep is the Cowork-style eventually-consistent fallback.
#
# Manual:
#   powershell -File sweep-cursor-sessions.ps1 -Backfill
#   powershell -File sweep-cursor-sessions.ps1

param(
    [switch]$Backfill,
    [switch]$ArchiveOld
)

$ErrorActionPreference = "Continue"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Exporter = Join-Path $ScriptDir "export-cursor-sessions.py"
$LogDir = Join-Path (Split-Path -Parent $ScriptDir) "logs"
New-Item -ItemType Directory -Path $LogDir -Force | Out-Null
$LogFile = Join-Path $LogDir ("sweep-" + (Get-Date -Format "yyyy-MM-dd") + ".log")

function Write-Log([string]$Msg) {
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-ddTHH:mm:ss"), $Msg
    Add-Content -LiteralPath $LogFile -Value $line -Encoding UTF8
    Write-Output $line
}

if (-not (Test-Path -LiteralPath $Exporter)) {
    Write-Log "FATAL: exporter not found at $Exporter"
    exit 1
}

$py = Get-Command py -ErrorAction SilentlyContinue
if (-not $py) { $py = Get-Command python -ErrorAction SilentlyContinue }
if (-not $py) {
    Write-Log "FATAL: neither py nor python on PATH"
    exit 1
}

$argList = @($Exporter)
if ($Backfill) { $argList += "--backfill" } else { $argList += "--sweep" }
if ($ArchiveOld) { $argList += "--archive-old" }

Write-Log ("Running: " + $py.Source + " " + ($argList -join " "))
try {
    & $py.Source @argList 2>&1 | ForEach-Object {
        Write-Log ("$_")
    }
    $code = $LASTEXITCODE
} catch {
    Write-Log ("FATAL: " + $_.Exception.Message)
    exit 1
}
Write-Log ("Exit code: $code")
exit $code
