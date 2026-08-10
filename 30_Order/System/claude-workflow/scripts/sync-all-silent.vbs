' Silent launcher for ClaudeKit-Sync-All.
' WindowStyle 0 = hidden -- prevents the every-15-min wsl.exe console popup.
' Correction (2026-08-10): register-sync-task.ps1 originally called wsl.exe
' directly, relying on ScheduledTaskSettingsSet -Hidden to suppress the
' window. That setting hides the task from the Task Scheduler *library* UI,
' not the console window a directly-invoked console executable opens in an
' interactive session -- confirmed for real: the popup kept happening, and
' the window being closed mid-run is the likely cause of LastTaskResult
' 3221225786 (STATUS_CONTROL_C_EXIT) observed 2026-08-10.
' Unlike the retired sync-jarvis-silent.vbs, this launcher WAITS for the
' inner command (waitOnReturn = True) and exits with its real return code,
' so Task Scheduler's LastTaskResult still reflects whether sync-all.sh
' actually succeeded -- closing the exact fire-and-forget gap that let the
' 50_Claude path bug go undetected for over a week (see _docs/Repo-Map.md).
Option Explicit
Dim sh, exitCode
Set sh = CreateObject("WScript.Shell")
exitCode = sh.Run("wsl.exe -e bash -lc ""~/projects/ai/claude/second-brain-claudekit/60_Claude/scripts/sync-all.sh""", 0, True)
WScript.Quit(exitCode)
