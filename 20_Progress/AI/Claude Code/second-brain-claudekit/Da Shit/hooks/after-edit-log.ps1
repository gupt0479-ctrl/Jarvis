#!/usr/bin/env pwsh
# after-edit-log.ps1
# PostToolUse hook — logs every file edit to 50_Claude/Sessions/_today-edits.md
# Claude Code passes tool context as environment variables.

param()

# Resolve vault root (two levels up from .claude/hooks/)
$vaultRoot = $PSScriptRoot | Split-Path -Parent | Split-Path -Parent
$sessionDir = Join-Path $vaultRoot "50_Claude" "Sessions"
$logFile    = Join-Path $sessionDir "_today-edits.md"

# Ensure sessions directory exists
if (-not (Test-Path $sessionDir)) {
    New-Item -ItemType Directory -Path $sessionDir -Force | Out-Null
}

# Archive yesterday's log if present
if (Test-Path $logFile) {
    $lastWrite = (Get-Item $logFile).LastWriteTime.Date
    if ($lastWrite -lt (Get-Date).Date) {
        $archiveName = Join-Path $sessionDir ($lastWrite.ToString("yyyy-MM-dd") + "-edits.md")
        Rename-Item -Path $logFile -NewName $archiveName -ErrorAction SilentlyContinue
    }
}

# Create header if file is new
if (-not (Test-Path $logFile)) {
    $header = "# Edit Log — $(Get-Date -Format 'yyyy-MM-dd')`n`n"
    Set-Content -Path $logFile -Value $header -Encoding UTF8
}

# Build and append the log entry
$time     = Get-Date -Format "HH:mm"
$tool     = if ($env:CLAUDE_TOOL_NAME)  { $env:CLAUDE_TOOL_NAME }  else { "unknown" }
$filePath = if ($env:CLAUDE_FILE_PATH)  { $env:CLAUDE_FILE_PATH }  else { "unknown" }

$entry = "- $time | $tool | $filePath"
Add-Content -Path $logFile -Value $entry -Encoding UTF8
