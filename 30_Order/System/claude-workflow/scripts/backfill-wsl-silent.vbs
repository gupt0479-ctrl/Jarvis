' Silent launcher for ConversationCapture-Backfill-WSL.
' Same corrected hidden + synchronous + honest-exit-code pattern as
' sync-all-silent.vbs (2026-08-11). Safety-net catch-up for WSL Claude Code
' sessions the SessionEnd/Stop hooks missed - not the primary mechanism.
Option Explicit
Dim sh, exitCode
Set sh = CreateObject("WScript.Shell")
exitCode = sh.Run("wsl.exe -e bash -lc ""pwsh -ExecutionPolicy Bypass -File ~/.claude/hooks/wsl-session-export.ps1 -BackfillAll""", 0, True)
' Records this run's honest exit code to the Capture Health dashboard note
' (added 2026-08-19 - reliability gap fix, see the CoreCLR crash-in-pwsh
' investigation). Runs after the real work so it can never mask exitCode
' below; ignore its own exit status.
sh.Run "powershell -NoProfile -ExecutionPolicy Bypass -File ""D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\claude-workflow\scripts\update-capture-health.ps1"" -TaskLabel WSL -ExitCode " & exitCode, 0, True
WScript.Quit(exitCode)
