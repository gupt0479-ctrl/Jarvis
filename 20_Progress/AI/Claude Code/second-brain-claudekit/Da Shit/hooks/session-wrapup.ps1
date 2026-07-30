#!/usr/bin/env pwsh
# session-wrapup.ps1
# Stop hook — reminds you to run /compress if no session log was written today.

param()

$vaultRoot  = $PSScriptRoot | Split-Path -Parent | Split-Path -Parent
$sessionDir = Join-Path $vaultRoot "50_Claude" "Sessions"
$today      = Get-Date -Format "yyyy-MM-dd"
$logFile    = Join-Path $sessionDir "$today-session.md"

# Session already logged — nothing to do
if (Test-Path $logFile) {
    exit 0
}

# Only remind if something was actually done this session
$editLog  = Join-Path $sessionDir "_today-edits.md"
$hasEdits = (Test-Path $editLog) -and (
    (Get-Content $editLog -ErrorAction SilentlyContinue |
        Where-Object { $_ -match "^\- \d" }).Count -gt 0
)

if ($hasEdits) {
    Write-Host ""
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    Write-Host "  Session wrapup: no log found for today."
    Write-Host "  Run /compress to save a session log."
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    Write-Host ""
}
