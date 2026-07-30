# Hook: Session Wrapup Reminder

**Trigger:** `Stop` — fires when the Claude Code session is ending.

**Purpose:** Ensure every meaningful session leaves a log artifact. Eliminates the "I forgot to document this session" problem.

## What It Does

At session end:
1. Check if a session log was written today (`50_Claude/Sessions/YYYY-MM-DD-session.md` exists).
2. If **yes**: confirm it exists and exit silently.
3. If **no**: display a reminder to run `/compress` before closing.

## PowerShell Implementation

```powershell
# .claude/hooks/session-wrapup.ps1
# Called by Claude Code Stop hook.

param()

$vaultRoot  = $PSScriptRoot | Split-Path -Parent | Split-Path -Parent
$sessionDir = Join-Path $vaultRoot "50_Claude\Sessions"
$today      = Get-Date -Format "yyyy-MM-dd"
$logFile    = Join-Path $sessionDir "$today-session.md"

if (Test-Path $logFile) {
    # Session already logged — nothing to do
    exit 0
}

# Check if today's edit log has any entries (was anything done?)
$editLog = Join-Path $sessionDir "_today-edits.md"
$hasEdits = (Test-Path $editLog) -and ((Get-Content $editLog | Where-Object { $_ -match "^\- \d" }).Count -gt 0)

if ($hasEdits) {
    Write-Host ""
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    Write-Host "  Session wrapup: no log found for today."
    Write-Host "  Run /compress to save a session log."
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    Write-Host ""
}
```

## Claude Code Hook Configuration

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "powershell -ExecutionPolicy Bypass -File .claude/hooks/session-wrapup.ps1"
          }
        ]
      }
    ]
  }
}
```

## Notes

- This hook is **non-blocking** — it only prints a reminder, it does not prevent session end.
- If you want auto-compress (no prompt), replace the `Write-Host` block with a call to run `/compress` directly. Start with the reminder version — it is less intrusive.
- Works on both Windows (PowerShell 5+) and WSL (pwsh).
