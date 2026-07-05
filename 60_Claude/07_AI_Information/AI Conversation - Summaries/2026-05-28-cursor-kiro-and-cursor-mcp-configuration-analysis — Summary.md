---
type: input
input_kind: ai-conversation-summary
status: sprout
created: 2026-05-28
source_app: cursor
source_note: "[[60_Claude/05_Clippings/AI Conversations/Windows/Cursor/05-28 Cursor - Kiro and cursor MCP configuration analysis.md]]"
project: Jarvis
decision_count: 4
action_count: 3
tags:
  - input
  - ai-conversation-summary
notes: []
---

# Conversation Summary — Kiro and cursor MCP configuration analysis

## What Was Decided
- Cursor does **not** read `~/.mcp.json`; it reads `~/.cursor/mcp.json` and project `.cursor/mcp.json` plus marketplace plugin MCPs.
- Claude Code's global `~/.mcp.json` strategy is sound — the gap was only missing Cursor-native config files.
- Cursor should mirror Claude's two-layer MCP setup: global `~/.cursor/mcp.json` + project `Jarvis/.cursor/mcp.json`.
- Subscription split: Claude Code in VS Code for daily coding; Cursor Pro for agentic refactors, vault MCP work, deployment plugins.

## What Changed
- Populated `C:\Users\Anant Gupta\.cursor\mcp.json` with jarvis/the-plan HTTP + filesystem servers (mirroring Claude global).
- Created `Jarvis/.cursor/mcp.json` with obsidian, context7, playwright, openaiDeveloperDocs (mirroring project `.mcp.json`).
- Left Claude and Kiro configs untouched in this session.

## Important Context
- Active Cursor session had only plugin MCPs (Supabase, Vercel, Sanity) until reload — empty global Cursor MCP was the root cause, not bad Obsidian ports.
- Plugin MCP does not appear in `mcp.json`; that is expected, not a config bug.
- Kiro's malformed global config (obsidian nested inside github) is a Kiro-only issue.

## Source Claims (Quoted From Transcript)
- "Cursor does **not** read `~/.mcp.json` — your global Claude setup was correct, but Cursor needed its own file."
- "Your global MCP design is sound. The only Cursor mistake was not copying it into `~/.cursor/mcp.json`."

## Inferred Claims (Distiller Interpretation)
- Later MCP work (stdio bridges for SSE 409 fix) superseded the HTTP entries written here for WSL sessions — treat this export as the config audit, not the final transport choice.

## Open Questions
- Whether to consolidate Obsidian connection to one style (HTTP vs stdio) across all tools.
- Whether The Plan needs `.cursor/rules/` mirroring Jarvis (offered but not done in this thread).

## Follow-Up Actions
- [ ] Reload MCP after any `mcp.json` edit (requires new session)
- [ ] Move hardcoded tokens to env-var interpolation when touching configs again

## Related Notes
- [[60_Claude/07_AI_Information/AI Conversation - Summaries/2026-07-05-cursor-mcp-failure-resolution-plan — Summary]]

## Should Be Promoted?
- decision: yes — add a one-line pointer in vault MCP docs that Cursor requires `.cursor/mcp.json`, not `.mcp.json`.
