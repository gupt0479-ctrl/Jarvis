param()

$ErrorActionPreference = "Stop"

$rawInput = [Console]::In.ReadToEnd()
if ([string]::IsNullOrWhiteSpace($rawInput)) {
    exit 0
}

try {
    $hookInput = $rawInput | ConvertFrom-Json
} catch {
    exit 0
}

$eventName = [string]$hookInput.hook_event_name
$cwd = [string]$hookInput.cwd
$jarvisRoot = "D:\Users\_Anant\10_Areas\Documents\Jarvis"

function Test-IsInsideJarvis {
    param([string]$Path)

    if ([string]::IsNullOrWhiteSpace($Path)) {
        return $false
    }

    $normalizedPath = $Path.TrimEnd('\', '/').ToLowerInvariant()
    $normalizedRoot = $jarvisRoot.TrimEnd('\', '/').ToLowerInvariant()
    return ($normalizedPath -eq $normalizedRoot -or $normalizedPath.StartsWith($normalizedRoot + "\"))
}

if ($eventName -eq "SessionStart" -and (Test-IsInsideJarvis -Path $cwd)) {
    $context = @"
Jarvis context-pack policy:
- Read first: 60_Claude/07_AI_Information/Vault Map.md (orientation), then AGENTS.md (Write Contract), 40_Resources/Obsidian/Jarvis Vault Architecture.md (where notes go), and 30_Order/ (Templates + Workflows) before writing anything.
- For current state: 60_Claude/07_AI_Information/AI_CONTEXT.md, 00_Dashboard.md, and the recent tail of 60_Claude/07_AI_Information/Session Logs/log.md.
- Follow the matching 30_Order/Workflows/ procedure for the task; never invent a folder. If unsure where a note goes, write it to 60_Claude/00_Inbox/.
- Read task-specific project or course notes only after the task is clear. Do not scan the whole vault unless Anant explicitly asks.
- Use Sonnet for normal work, reserve Opus for hard planning or stuck debugging.
- Desktop is read-first planning/review; Claude Code is the implementation surface; mobile is capture only.
"@

    @{
        hookSpecificOutput = @{
            hookEventName = "SessionStart"
            additionalContext = $context
        }
    } | ConvertTo-Json -Depth 5 -Compress

    exit 0
}

if ($eventName -eq "SessionEnd") {
    try {
        $claudeDir = Join-Path $env:USERPROFILE ".claude"
        if (-not (Test-Path -LiteralPath $claudeDir)) {
            New-Item -ItemType Directory -Path $claudeDir -Force | Out-Null
        }

        $activityPath = Join-Path $claudeDir "jarvis-session-activity.jsonl"
        $entry = [ordered]@{
            timestamp = (Get-Date).ToString("o")
            event = $eventName
            session_id = [string]$hookInput.session_id
            cwd = $cwd
            reason = [string]$hookInput.reason
            transcript_path = [string]$hookInput.transcript_path
            in_jarvis = (Test-IsInsideJarvis -Path $cwd)
        }

        ($entry | ConvertTo-Json -Compress) | Add-Content -LiteralPath $activityPath -Encoding UTF8
    } catch {
        exit 0
    }
}

exit 0

