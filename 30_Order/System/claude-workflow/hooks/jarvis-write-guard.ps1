param()

# PreToolUse write guard for the Jarvis vault.
# Enforces the Write Contract negative constraints from AGENTS.md:
#   - never create files at the vault root (only the four contract files may live there)
#   - never write into 50_Archive/, 60_Claude/05_Clippings/ (raw sources are read-only)
#   - never write notes into .obsidian/, .cursor/, .kiro/, .git/
# An allowlist of daily-operations paths (daily notes, plans, templates, skills,
# agents, dashboard, session log, Claude OS) is checked before any denial so the
# /startday-/closeday loop can never be blocked. Fails open (exit 0) on any
# parsing problem so it can never block legitimate work by accident.

$ErrorActionPreference = "Stop"

$raw = [Console]::In.ReadToEnd()
if ([string]::IsNullOrWhiteSpace($raw)) { exit 0 }

try { $payload = $raw | ConvertFrom-Json } catch { exit 0 }

$tool = [string]$payload.tool_name
if ($tool -notin @("Write", "Edit", "MultiEdit")) { exit 0 }

$filePath = [string]$payload.tool_input.file_path
if ([string]::IsNullOrWhiteSpace($filePath)) { exit 0 }

$root = "D:\Users\_Anant\10_Areas\Documents\Jarvis"
$norm = ($filePath -replace '/', '\')
$normLower = $norm.ToLowerInvariant()
$rootLower = $root.ToLowerInvariant()

# Only guard paths inside the vault. Anything outside is not our business.
if (-not $normLower.StartsWith($rootLower)) { exit 0 }

$rel = $norm.Substring($root.Length).TrimStart('\')
$relLower = $rel.ToLowerInvariant()

function Deny([string]$reason) {
    @{
        hookSpecificOutput = @{
            hookEventName            = "PreToolUse"
            permissionDecision       = "deny"
            permissionDecisionReason = $reason
        }
    } | ConvertTo-Json -Depth 5 -Compress
    exit 0
}

# --- Allowlist: daily-operations paths, checked before any denial ---
$allowPrefixes = @(
    "10_areas\life\enumerate\daily\",
    "10_areas\life\plans\",
    "30_order\templates\",
    ".claude\skills\",
    ".claude\agents\"
)
$allowExact = @(
    "00_dashboard.md",
    "60_claude\07_ai_information\session logs\log.md",
    "60_claude\07_ai_information\claude os.md",
    "60_claude\05_clippings\clippings board.md"
)
foreach ($prefix in $allowPrefixes) {
    if ($relLower.StartsWith($prefix)) { exit 0 }
}
if ($allowExact -contains $relLower) { exit 0 }

# --- Denials ---
if ($relLower.StartsWith("50_archive\")) {
    Deny "Write Contract: 50_Archive is never written. See AGENTS.md and the Vault Map."
}

if ($relLower.StartsWith(".obsidian\")) {
    Deny "Write Contract: .obsidian holds settings, never notes. See AGENTS.md."
}

if ($relLower.StartsWith("60_claude\05_clippings\")) {
    Deny "Write Contract: 60_Claude/05_Clippings is read-only after capture. Summaries go to 60_Claude/10_Source_Summaries/. See AGENTS.md."
}

foreach ($toolDir in @(".cursor\", ".kiro\", ".git\")) {
    if ($relLower.StartsWith($toolDir)) {
        Deny "Write Contract: $toolDir holds tooling config, never notes. See AGENTS.md."
    }
}

# Root-level path (no backslash in the relative path) => sits directly at vault root.
if ($rel -notmatch '\\') {
    $allowedRoot = @("00_dashboard.md", "agents.md", "claude.md", "human_writing.md")
    if ($allowedRoot -notcontains $relLower) {
        Deny "Write Contract golden rule #1: never create files at the vault root. If unsure where this belongs, write it to 60_Claude/00_Inbox/. See AGENTS.md."
    }
}

exit 0
