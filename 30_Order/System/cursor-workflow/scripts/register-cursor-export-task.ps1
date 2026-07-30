# Registers a Windows Scheduled Task that sweeps Cursor sessions every 15 minutes.
# Requires an elevated or user-interactive PowerShell session on Windows.
# Idempotent: removes any existing task with the same name first.

$TaskName = "Jarvis-Cursor-Session-Export"
$Script = Join-Path $PSScriptRoot "sweep-cursor-sessions.ps1"

if (-not (Test-Path -LiteralPath $Script)) {
    Write-Error "Missing $Script"
    exit 1
}

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue

$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$Script`""

$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).Date -RepetitionInterval (New-TimeSpan -Minutes 15) -RepetitionDuration ([TimeSpan]::MaxValue)

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -MultipleInstances IgnoreNew

$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal `
    -Description "Sweep Cursor composerHeaders + agent-transcripts into Jarvis AI Conversations (WSL/Windows per-project)." |
    Out-Null

Write-Output "Registered scheduled task: $TaskName (every 15 min)"
Get-ScheduledTask -TaskName $TaskName | Format-List TaskName, State
