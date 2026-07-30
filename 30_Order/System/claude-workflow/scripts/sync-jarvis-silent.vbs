' Silent launcher for SecondBrainClaudekit-JarvisSync.
' WindowStyle 0 = hidden — prevents the every-15-min wsl.exe console popup.
' Does NOT change sync behavior; only hides the window. Sync-Log.md still gets entries.
Option Explicit
Dim sh
Set sh = CreateObject("WScript.Shell")
' Same command the scheduled task previously ran directly:
'   wsl.exe -d Ubuntu -- bash -lc ".../sync-jarvis.sh"
sh.Run "wsl.exe -d Ubuntu -- bash -lc ""/home/anant_gupta/projects/ai/claude/second-brain-claudekit/50_Claude/scripts/sync-jarvis.sh""", 0, False
