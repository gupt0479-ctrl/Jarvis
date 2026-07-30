# Hook: After-Edit Log

**Trigger:** `PostToolUse` — fires after Claude edits, creates, or writes a file.

**Purpose:** Keep a lightweight audit trail of what Claude changed so `/resume` and `/compress` have a clean source of truth.

## What It Does

After any file write/edit tool call:
1. Appends a single line to `50_Claude/Sessions/_today-edits.md` (created fresh each day).
2. Format: `HH:MM | {{tool}} | {{file_path}} | {{one-line description if available}}`
3. At session start, if `_today-edits.md` is more than 24 hours old, archive it to `50_Claude/Sessions/{{date}}-edits.md`.

## PowerShell Implementation

```powershell
# .claude/hooks/after-edit-log.ps1
# Called by Claude Code PostToolUse hook.
# Parameters passed as environment variables by Claude Code:
#   $env:CLAUDE_TOOL_NAME  — name of the tool used
#   $env:CLAUDE_FILE_PATH  — file path affected

param()

$vaultRoot = $PSScriptRoot | Split-Path -Parent | Split-Path -Parent
$sessionDir = Join-Path $vaultRoot "50_Claude\Sessions"
$logFile = Join-Path $sessionDir "_today-edits.md"

# Ensure sessions directory exists
if (-not (Test-Path $sessionDir)) {
    New-Item -ItemType Directory -Path $sessionDir -Force | Out-Null
}

# Archive old log if it's from a previous day
if (Test-Path $logFile) {
    $lastWrite = (Get-Item $logFile).LastWriteTime.Date
    if ($lastWrite -lt (Get-Date).Date) {
        $archiveName = $lastWrite.ToString("yyyy-MM-dd") + "-edits.md"
        Rename-Item -Path $logFile -NewName (Join-Path $sessionDir $archiveName)
    }
}

# Create header if file is new
if (-not (Test-Path $logFile)) {
    $header = "# Edit Log — $(Get-Date -Format 'yyyy-MM-dd')`n`n"
    Set-Content -Path $logFile -Value $header -Encoding UTF8
}

# Append the log entry
$time = Get-Date -Format "HH:mm"
$tool = if ($env:CLAUDE_TOOL_NAME) { $env:CLAUDE_TOOL_NAME } else { "unknown" }
$filePath = if ($env:CLAUDE_FILE_PATH) { $env:CLAUDE_FILE_PATH } else { "unknown" }

$entry = "- $time | $tool | $filePath"
Add-Content -Path $logFile -Value $entry -Encoding UTF8
```

## Claude Code Hook Configuration

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -ExecutionPolicy Bypass -File .claude/hooks/after-edit-log.ps1"
          }
        ]
      }
    ]
  }
}
```

## Notes

- This log is lightweight and non-blocking. It does not slow down Claude's work.
- The log is consumed by `/compress` to auto-populate the "What Happened" section.
- Do not commit `_today-edits.md` to version control — add it to `.gitignore`.
