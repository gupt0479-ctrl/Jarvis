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

function ConvertTo-JsonStringArray {
    # ConvertTo-Json unwraps a single-element array into a bare scalar
    # ("abc" instead of ["abc"]), which then fails to round-trip as an array
    # on the next read. Build the JSON by hand instead - simple, and correct
    # regardless of element count.
    param([string[]]$Items)
    $escaped = @($Items) | ForEach-Object { '"' + ($_ -replace '\\','\\' -replace '"','\"') + '"' }
    return "[" + ($escaped -join ",") + "]"
}

function Read-JsonStringArray {
    # @(Get-Content -Raw | ConvertFrom-Json) silently collapses a 2+ element
    # JSON array into a single space-joined string when the whole pipeline is
    # wrapped in one @(...) - verified reproducible in this PowerShell version.
    # Parsing into a variable first, then wrapping that variable, is the
    # combination that actually preserves each element. Do not "simplify"
    # this back to the one-line form.
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path)) { return @() }
    try {
        $raw = Get-Content -LiteralPath $Path -Raw
        $parsed = $raw | ConvertFrom-Json
        return @($parsed)
    } catch {
        return @()
    }
}

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

if ($eventName -eq "SessionEnd") {
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
    try {
        $exportScript = "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\claude-workflow\scripts\export-claude-session.ps1"
        $indexPath = "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\claude-workflow\exported-claude-sessions.json"

        if ($isJarvis -and $sessionId -and $transcriptPath -and (Test-Path -LiteralPath $transcriptPath)) {
            $exported = Read-JsonStringArray -Path $indexPath

            if ($exported -notcontains $sessionId) {
                $outDir = "D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\05_Clippings\AI Conversations\Windows\Claude Code"
                & $exportScript -TranscriptPath $transcriptPath -OutputDir $outDir `
                    -SessionId $sessionId -Project "Jarvis" -Cwd $cwd | Out-Null

                $exported = @($exported) + $sessionId
                (ConvertTo-JsonStringArray $exported) | Set-Content -LiteralPath $indexPath -Encoding UTF8
            }
        }
    } catch {
        # fail open - a bad transcript must never block Claude Code from exiting
    }

    # Cowork sweep: Cowork/Agent-Mode sessions run in fully isolated .claude
    # sandboxes under %APPDATA%\Claude\local-agent-mode-sessions and never fire
    # this hook themselves, so they can't be captured live. Piggyback on every
    # normal session end instead - "eventually consistent" within one real
    # Claude Code use, not instant, but fully automatic.
    try {
        $coworkRoot = Join-Path $env:APPDATA "Claude\local-agent-mode-sessions"
        if (Test-Path -LiteralPath $coworkRoot) {
            $coworkIndexPath = "D:\Users\_Anant\10_Areas\Documents\Jarvis\30_Order\System\claude-workflow\exported-cowork-sessions.json"
            $coworkExported = Read-JsonStringArray -Path $coworkIndexPath

            $coworkOutDir = "D:\Users\_Anant\10_Areas\Documents\Jarvis\60_Claude\05_Clippings\AI Conversations\Windows\Cowork"
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

            $newlyExported = New-Object System.Collections.Generic.List[string]
            foreach ($fullPath in $candidatePaths) {
                if ($coworkExported -notcontains $fullPath) {
                    try {
                        $baseName = [System.IO.Path]::GetFileNameWithoutExtension($fullPath)
                        & $exportScript -TranscriptPath $fullPath -OutputDir $coworkOutDir `
                            -SessionId $baseName -Project "Cowork" | Out-Null
                        $newlyExported.Add($fullPath)
                    } catch {
                        # skip this one transcript, keep sweeping the rest
                    }
                }
            }

            if ($newlyExported.Count -gt 0) {
                $coworkExported = @($coworkExported) + @($newlyExported)
                (ConvertTo-JsonStringArray $coworkExported) | Set-Content -LiteralPath $coworkIndexPath -Encoding UTF8
            }
        }
    } catch {
        # fail open
    }
}

exit 0

