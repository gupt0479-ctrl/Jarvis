param()

# PreToolUse write guard for the Jarvis vault.
# Enforces the Write Contract negative constraints from AGENTS.md:
#   - never create files at the vault root (only the four contract files may live there)
#   - never write into 50_Archive/
#   - never write notes into .obsidian/
# Allows everything else. Fails open (exit 0) on any parsing problem so it can
# never block legitimate work by accident.

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

if ($relLower.StartsWith("50_archive\")) {
    Deny "Write Contract: 50_Archive is never written. See AGENTS.md and the Vault Map."
}

if ($relLower.StartsWith(".obsidian\")) {
    Deny "Write Contract: .obsidian holds settings, never notes. See AGENTS.md."
}

# Root-level path (no backslash in the relative path) => sits directly at vault root.
if ($rel -notmatch '\\') {
    $allowedRoot = @("00_dashboard.md", "agents.md", "claude.md", "human_writing.md")
    if ($allowedRoot -notcontains $relLower) {
        Deny "Write Contract golden rule #1: never create files at the vault root. If unsure where this belongs, write it to 60_Claude/00_Inbox/. See AGENTS.md."
    }
}

exit 0
