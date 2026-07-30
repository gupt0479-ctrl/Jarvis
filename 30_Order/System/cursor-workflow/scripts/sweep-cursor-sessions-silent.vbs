' Silent launcher for Jarvis-Cursor-Session-Export.
' WindowStyle 0 = hidden — prevents the every-15-min PowerShell popup.
' Output goes to cursor-workflow/logs/ via sweep-cursor-sessions.ps1.
Option Explicit
Dim sh, scriptDir, ps1
Set sh = CreateObject("WScript.Shell")
scriptDir = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
ps1 = scriptDir & "\sweep-cursor-sessions.ps1"
sh.Run "powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File """ & ps1 & """", 0, False
