---
type: input
input_kind: ai-conversation-summary
status: sprout
created: 2026-07-05
source_app: cursor
source_note: "[[60_Claude/05_Clippings/AI Conversations/Windows/Cursor/07-05 Cursor - Cursor AI conversation pipeline.md]]"
project: Jarvis
decision_count: 5
action_count: 2
tags:
  - input
  - ai-conversation-summary
notes: []
---

# Conversation Summary — Cursor AI conversation pipeline

## What Was Decided
- Cursor conversations live in one Windows SQLite file (`globalStorage/state.vscdb`, `cursorDiskKV` table) even for WSL workspaces — one export pipeline, not two.
- Output routes by workspace URI: `file://` → `Windows/Cursor/`, `vscode-remote://` → `WSL/Cursor/`.
- Tier 0 is on-demand `_raw_composer/` JSON dumps only; no junction to the commingled DB.
- Automation is manual via `/export-cursor-session`; no Cursor hook without explicit consent.
- Tool-only bubbles export as generic `*Tool activity (details omitted)*`; prose-only filter is intentional.

## What Changed
- Built `30_Order/System/cursor-workflow/` (export, list, dump, redact scripts + index).
- Created global skills on Windows and WSL for `/export-cursor-session`.
- First production exports landed in the vault (this run).

## Important Context
- `composer.composerHeaders` index (183) is incomplete vs 224 `composerData:*` rows; scripts read `cursorDiskKV` directly.
- Agent-transcripts JSONL under `~/.cursor/projects/` is a partial fallback (~13% coverage), not the primary source.
- Redaction lives in standalone `redact_secrets.py`, duplicated from the inline PowerShell in the Claude export script.

## Source Claims (Quoted From Transcript)
- "Never create a standing/global config… or a filesystem junction… without stopping to ask explicitly first."
- "`60_Claude/05_Clippings/` is append-only — new files only, never edit a previously-written raw capture in place."

## Inferred Claims (Distiller Interpretation)
- Long agentic composers will look much shorter in exports than raw turn counts; that is expected behavior, not a regression.

## Open Questions
- Whether to add a Cursor SessionEnd hook later (Claude Code got one separately; Cursor deliberately deferred).
- Whether WSL `/mnt/c` SQLite reads need a Windows-side fallback when Cursor holds a cross-OS file lock.

## Follow-Up Actions
- [ ] Run `/export-cursor-session` periodically for Jarvis composers worth keeping
- [ ] Consider promoting pipeline docs into `30_Order/Workflows/` once a few more exports validate the shape

## Related Notes
- [[60_Claude/05_Clippings/AI Conversations/README]]
- [[Conversation Capture]]

## Should Be Promoted?
- decision: partial — promote the "one SQLite store, route by URI" fact into cursor-workflow README (done); defer hook/junction decisions until explicitly requested.
