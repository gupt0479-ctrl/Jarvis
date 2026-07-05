param(
    [Parameter(Mandatory = $true)]
    [string]$TranscriptPath,

    # Exactly one of OutputPath / OutputDir must be given. OutputPath is exact
    # (used by attended callers, e.g. the skill, that already picked a title).
    # OutputDir is for unattended callers (the SessionEnd hook) - the script
    # derives "MM-DD Claude Code - {slug}.md" itself from the first human
    # message and handles name collisions.
    [string]$OutputPath = "",
    [string]$OutputDir = "",

    [string]$SessionId = "",
    [string]$Project = "",
    [string]$Cwd = "",
    [string]$Title = ""
)

if (-not $OutputPath -and -not $OutputDir) {
    Write-Error "Pass either -OutputPath or -OutputDir."
    exit 1
}

$ErrorActionPreference = "Stop"

# Cowork transcripts nest under paths well past Windows' 260-char MAX_PATH
# (observed up to ~440 chars) - Test-Path/Get-Content silently fail to find
# them without the \\?\ long-path prefix. Apply it whenever needed so this
# script works regardless of whether the caller remembered to.
if ($TranscriptPath.Length -ge 250 -and -not $TranscriptPath.StartsWith('\\?\')) {
    $TranscriptPath = "\\?\$TranscriptPath"
}

if (-not (Test-Path -LiteralPath $TranscriptPath)) {
    Write-Error "Transcript not found: $TranscriptPath"
    exit 1
}

$lines = Get-Content -LiteralPath $TranscriptPath -Encoding UTF8

$turns = New-Object System.Collections.Generic.List[object]
$currentRole = $null
$currentTextParts = New-Object System.Collections.Generic.List[string]
$currentTools = New-Object System.Collections.Generic.List[string]
$firstTimestamp = $null
$lastTimestamp = $null

function Flush-Turn {
    if ($script:currentRole -and ($script:currentTextParts.Count -gt 0 -or $script:currentTools.Count -gt 0)) {
        $turns.Add([pscustomobject]@{
            role  = $script:currentRole
            text  = ($script:currentTextParts -join "`n`n")
            tools = @($script:currentTools | Select-Object -Unique)
        })
    }
    $script:currentTextParts = New-Object System.Collections.Generic.List[string]
    $script:currentTools = New-Object System.Collections.Generic.List[string]
}

foreach ($line in $lines) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    try { $o = $line | ConvertFrom-Json } catch { continue }

    if ($o.timestamp) {
        if (-not $firstTimestamp) { $firstTimestamp = $o.timestamp }
        $lastTimestamp = $o.timestamp
    }

    if ($o.type -eq 'user' -and $o.message) {
        $content = $o.message.content
        if ($content -is [string]) {
            if ($content.Trim() -eq '') { continue }
            Flush-Turn
            $currentRole = 'user'
            $currentTextParts.Add($content)
            Flush-Turn
            $currentRole = $null
        }
        # array content on a 'user' entry is a tool_result being fed back, not human-authored - skip
    }
    elseif ($o.type -eq 'assistant' -and $o.message) {
        if ($currentRole -ne 'assistant') {
            Flush-Turn
            $currentRole = 'assistant'
        }
        foreach ($block in @($o.message.content)) {
            if ($block.type -eq 'text' -and $block.text -and $block.text.Trim() -ne '') {
                $currentTextParts.Add($block.text)
            }
            elseif ($block.type -eq 'tool_use' -and $block.name) {
                $currentTools.Add($block.name)
            }
        }
    }
}
Flush-Turn

if ($turns.Count -eq 0) {
    Write-Output "No human-readable turns found in transcript (tool-only or empty session) - nothing written."
    exit 0
}

# Deliberate safety choice: only 'text' content blocks are ever emitted below.
# tool_use.input and tool_result.content (where commands, file contents, and
# secrets can appear) are never written to the exported note. Text blocks still
# pass through Redact-Secrets, since a user can paste a literal key/token into
# a chat message, which tool-stripping alone would not catch.
function Redact-Secrets {
    param([string]$Text)
    if (-not $Text) { return $Text }

    # Known key-shaped prefixes (Anthropic, OpenAI, GitHub, Slack, AWS, generic bearer)
    $Text = $Text -replace '(sk-ant-[A-Za-z0-9_-]{10,})', '[REDACTED]'
    $Text = $Text -replace '(sk-[A-Za-z0-9]{20,})', '[REDACTED]'
    $Text = $Text -replace '(ghp_[A-Za-z0-9]{20,})', '[REDACTED]'
    $Text = $Text -replace '(xox[baprs]-[A-Za-z0-9-]{10,})', '[REDACTED]'
    $Text = $Text -replace '(AKIA[0-9A-Z]{12,})', '[REDACTED]'
    $Text = $Text -replace '(?i)(Bearer\s+)[A-Za-z0-9\-_.]{15,}', '$1[REDACTED]'

    # SetEnvironmentVariable("NAME", "value", ...) - redact the value argument
    $Text = $Text -replace '(?i)(SetEnvironmentVariable\(\s*"[^"]+"\s*,\s*")[^"]{8,}(")', '$1[REDACTED]$2'

    # Generic fallback: a bare alphanumeric token 24+ chars with both letters and
    # digits is almost never meaningful prose - treat it as a likely secret/key.
    $Text = $Text -replace '\b(?=[A-Za-z0-9_-]*[0-9])(?=[A-Za-z0-9_-]*[A-Za-z])[A-Za-z0-9_-]{24,}\b', '[REDACTED]'

    return $Text
}

$sb = New-Object System.Text.StringBuilder

$createdDate = if ($firstTimestamp) { ([datetime]$firstTimestamp) } else { (Get-Date) }
$created = $createdDate.ToString("yyyy-MM-dd")
$startedAt = if ($firstTimestamp) { ([datetime]$firstTimestamp).ToString("yyyy-MM-ddTHH:mm:ss") } else { "" }
$endedAt = if ($lastTimestamp) { ([datetime]$lastTimestamp).ToString("yyyy-MM-ddTHH:mm:ss") } else { "" }
$projectLabel = if ($Project) { $Project } else { "Unknown" }

function New-SlugFromText {
    param([string]$Text)
    if (-not $Text) { return "" }
    # First line/sentence only, strip filename-illegal chars, collapse whitespace, cap length.
    $firstLine = ($Text -split "`n")[0]
    $firstLine = ($firstLine -split '(?<=[.!?])\s')[0]
    $clean = $firstLine -replace '[<>:"/\\|?*`]', ''
    $clean = $clean -replace '\s+', ' '
    $clean = $clean.Trim()
    if ($clean.Length -gt 60) {
        $truncated = $clean.Substring(0, 60)
        $lastSpace = $truncated.LastIndexOf(' ')
        if ($lastSpace -gt 20) { $truncated = $truncated.Substring(0, $lastSpace) }
        $clean = $truncated.Trim()
    }
    return $clean
}

$firstUserTurn = $turns | Where-Object { $_.role -eq 'user' } | Select-Object -First 1
$autoSlug = if ($firstUserTurn) { New-SlugFromText $firstUserTurn.text } else { "" }
if (-not $autoSlug) { $autoSlug = "Session $($createdDate.ToString('HHmmss'))" }

$titleLabel = if ($Title) { $Title } else { $autoSlug }

if (-not $OutputPath) {
    $mmdd = $createdDate.ToString("MM-dd")
    $appLabel = if ($Project -eq "Cowork") { "Cowork" } else { "Claude Code" }
    $baseName = "$mmdd $appLabel - $autoSlug"
    $candidate = Join-Path $OutputDir "$baseName.md"
    $n = 2
    while (Test-Path -LiteralPath $candidate) {
        $candidate = Join-Path $OutputDir "$baseName-$n.md"
        $n++
    }
    $OutputPath = $candidate
}

# Schema per 60_Claude/05_Clippings/AI Conversations/README.md - do not
# rename these keys without updating that README too.
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("type: input")
[void]$sb.AppendLine("input_kind: ai-conversation")
[void]$sb.AppendLine("source_app: claude-code")
[void]$sb.AppendLine("title: `"$titleLabel`"")
[void]$sb.AppendLine("started_at: $startedAt")
[void]$sb.AppendLine("ended_at: $endedAt")
[void]$sb.AppendLine("project: $projectLabel")
[void]$sb.AppendLine("status: raw")
[void]$sb.AppendLine("session_id: $SessionId")
if ($Cwd) { [void]$sb.AppendLine("cwd: '$Cwd'") }
[void]$sb.AppendLine("tags:")
[void]$sb.AppendLine("  - input")
[void]$sb.AppendLine("  - ai-conversation")
[void]$sb.AppendLine("  - claude-code")
[void]$sb.AppendLine("---")
[void]$sb.AppendLine("")
[void]$sb.AppendLine("# $titleLabel")
[void]$sb.AppendLine("")

foreach ($turn in $turns) {
    if ($turn.role -eq 'user') {
        [void]$sb.AppendLine("## You")
        [void]$sb.AppendLine("")
        [void]$sb.AppendLine((Redact-Secrets $turn.text))
        [void]$sb.AppendLine("")
    }
    else {
        [void]$sb.AppendLine("## Claude")
        [void]$sb.AppendLine("")
        if ($turn.text) {
            [void]$sb.AppendLine((Redact-Secrets $turn.text))
            [void]$sb.AppendLine("")
        }
        if ($turn.tools.Count -gt 0) {
            [void]$sb.AppendLine("*Tools used: $($turn.tools -join ', ')*")
            [void]$sb.AppendLine("")
        }
    }
}

$outDir = Split-Path -Path $OutputPath -Parent
if (-not (Test-Path -LiteralPath $outDir)) {
    New-Item -ItemType Directory -Path $outDir -Force | Out-Null
}

Set-Content -LiteralPath $OutputPath -Value $sb.ToString() -Encoding UTF8
Write-Output "Wrote $OutputPath ($($turns.Count) turns)"
Write-Output "WROTE_PATH:$OutputPath"
