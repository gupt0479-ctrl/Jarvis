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
- Read first: 60_Claude/07_AI_Information/Jarvis OS — North Star.md (strategy spine), then AGENTS.md (write contract + routing), then 40_Resources/Obsidian/Jarvis Vault Architecture.md (folder placement).
- Before writing any note: read 30_Order/ (Templates + Workflows for the note type).
- For current state: 60_Claude/07_AI_Information/AI_CONTEXT.md, 00_Dashboard.md, then tail of 60_Claude/07_AI_Information/Session Logs/log.md.
- If unsure where a note goes: write it to 60_Claude/00_Inbox/. Never invent a folder.
- Load task-specific notes only after the task is clear. Do not dump the vault.
- Skill directories live at .claude/skills/<gerund-name>/SKILL.md — load SKILL.md first, reference.md only if needed.
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

if ($eventName -eq "SessionEnd" -or $eventName -eq "Stop") {
    # Stop fires after every turn (far more reliable than SessionEnd, which
    # depends on a clean process exit that doesn't always happen). Running
    # the same export path on both events means a session is never lost to
    # an ungraceful exit - the last Stop-triggered export already has it,
    # and export-claude-session.ps1's marker-staleness check (2026-08-11)
    # makes re-running safe: it updates the same note in place as the
    # session grows rather than creating a duplicate or skipping it.
    $isJarvis = Test-IsInsideJarvis -Path $cwd
    $transcriptPath = [string]$hookInput.transcript_path
    $sessionId = [string]$hookInput.session_id

    try {
        $claudeDir = Join-Path $env:USERPROFILE ".claude"
        if (-not (Test-Path -LiteralPath $claudeDir)) {
            New-Item -ItemType Directory -Path $claudeDir -Force | Out-Null
        }

        $activityPath = Join-Path $claudeDir "jarvis-session-activity.jsonl"
        $entry = [ordered]@{
            timestamp = (Get-Date).ToString("o")
            event = $eventName
            session_id = $sessionId
            cwd = $cwd
            reason = [string]$hookInput.reason
            transcript_path = $transcriptPath
            in_jarvis = $isJarvis
        }

        ($entry | ConvertTo-Json -Compress) | Add-Content -LiteralPath $activityPath -Encoding UTF8
    } catch {
        # fail open - never block session shutdown on the activity log
    }

    # Tier 1 (mechanical, ~0 tokens): auto-export this session's transcript to
    # the raw archive the moment it ends, so capture is live rather than
    # depending on a manual /export-ai-session pass. Distillation (tier 2)
    # stays manual - a hook can't invoke an LLM to synthesize a summary.
    #
    # Unconditional (no $isJarvis gate) - every Windows Claude Code project
    # (Home, Jarvis, The Plan, and anything new) gets exported and routed to
    # its own per-project folder by export-claude-session.ps1 itself, keyed
    # off the session's real cwd. Dedup is now a per-session marker file
    # inside that project folder (checked by the export script itself), not
    # a shared exported-claude-sessions.json index - so no index file to
    # read/write here at all.
    try {
        $exportScript = "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\claude-workflow\scripts\export-claude-session.ps1"

        if ($sessionId -and $transcriptPath -and (Test-Path -LiteralPath $transcriptPath)) {
            & $exportScript -TranscriptPath $transcriptPath -SessionId $sessionId -Cwd $cwd -SourceApp "ClaudeCode" | Out-Null
        }
    } catch {
        # fail open - a bad transcript must never block Claude Code from exiting
    }

    # Cowork sweep: Cowork/Agent-Mode sessions run in fully isolated .claude
    # sandboxes under %APPDATA%\Claude\local-agent-mode-sessions and never fire
    # this hook themselves, so they can't be captured live. Piggyback on every
    # normal session end instead - "eventually consistent" within one real
    # Claude Code use, not instant, but fully automatic.
    #
    # SessionEnd only, not Stop - Stop fires after every turn, and a full
    # enumeration of the Cowork sandbox tree that often has no bearing on
    # this session's own turns is unnecessary overhead per turn. Cowork
    # sessions aren't affected by how many turns this session takes.
    #
    # No shared cowork index file either - every candidate transcript found
    # this sweep is handed to export-claude-session.ps1, which checks its own
    # per-session marker (keyed on the transcript's own basename, grouped by
    # month) and returns instantly for anything already exported.
    if ($eventName -eq "SessionEnd") {
    try {
        $coworkRoot = Join-Path $env:APPDATA "Claude\local-agent-mode-sessions"
        if (Test-Path -LiteralPath $coworkRoot) {
            $exportScript = "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\claude-workflow\scripts\export-claude-session.ps1"

            # Only top-level session transcripts (parent dir ends "-outputs") -
            # never .credentials.json/.claude.json siblings, never nested
            # subagents/*.jsonl or tool-results/*.json fragments.
            # Cowork transcripts nest past the 260-char MAX_PATH (observed up
            # to ~440 chars) - Get-ChildItem -Recurse silently skips these, so
            # use .NET long-path enumeration with the \\?\ prefix instead.
            $longCoworkRoot = if ($coworkRoot.StartsWith('\\?\')) { $coworkRoot } else { "\\?\$coworkRoot" }
            $candidatePaths = [System.IO.Directory]::EnumerateFiles($longCoworkRoot, "*.jsonl", [System.IO.SearchOption]::AllDirectories) |
                Where-Object { (Split-Path $_ -Parent) -like "*-outputs" }

            foreach ($fullPath in $candidatePaths) {
                try {
                    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($fullPath)
                    & $exportScript -TranscriptPath $fullPath -SessionId $baseName -SourceApp "Cowork" | Out-Null
                } catch {
                    # skip this one transcript, keep sweeping the rest
                }
            }
        }
    } catch {
        # fail open
    }
    }
}

exit 0

