# Registers a Windows Scheduled Task that sweeps Cursor sessions every 15 minutes.
# Runs fully hidden (no console popup) via a VBS launcher with WindowStyle 0.
# Idempotent: removes any existing task with the same name first.

$TaskName = "Jarvis-Cursor-Session-Export"
$ScriptDir = $PSScriptRoot
$SilentLauncher = Join-Path $ScriptDir "sweep-cursor-sessions-silent.vbs"
$SweepScript = Join-Path $ScriptDir "sweep-cursor-sessions.ps1"

if (-not (Test-Path -LiteralPath $SweepScript)) {
    Write-Error "Missing $SweepScript"
    exit 1
}
if (-not (Test-Path -LiteralPath $SilentLauncher)) {
    Write-Error "Missing $SilentLauncher"
    exit 1
}

Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue

# wscript + VBS WindowStyle 0 is more reliable than powershell -WindowStyle Hidden
# alone, which can still flash a console briefly under Interactive logon.
$action = New-ScheduledTaskAction `
    -Execute "wscript.exe" `
    -Argument "//B `"$SilentLauncher`""

# Daily trigger that repeats every 15 minutes for 24 hours — re-arms each day.
$trigger = New-ScheduledTaskTrigger -Daily -At "00:05"
$trigger.Repetition = (New-ScheduledTaskTrigger -Once -At "00:05" `
    -RepetitionInterval (New-TimeSpan -Minutes 15) `
    -RepetitionDuration (New-TimeSpan -Hours 23 -Minutes 55)).Repetition

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -MultipleInstances IgnoreNew `
    -Hidden

$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal `
    -Description "Sweep Cursor composerHeaders + agent-transcripts into Jarvis AI Conversations (hidden; no console popup)." |
    Out-Null

Write-Output "Registered scheduled task: $TaskName (every 15 min, daily re-arm, hidden)"
Get-ScheduledTask -TaskName $TaskName | Format-List TaskName, State
(Get-ScheduledTask -TaskName $TaskName).Actions | Format-List Execute, Arguments
(Get-ScheduledTask -TaskName $TaskName).Settings | Format-List Hidden
