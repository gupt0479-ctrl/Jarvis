---
type: input
input_kind: ai-conversation-summary
status: sprout
created: 2026-07-05
source_app: cursor
source_note: "[[60_Claude/05_Clippings/AI Conversations/WSL/Cursor/07-05 Cursor - MCP failure resolution plan.md]]"
project: CausalOps
decision_count: 3
action_count: 2
tags:
  - input
  - ai-conversation-summary
notes: []
---

# Conversation Summary — MCP failure resolution plan

## What Was Decided
- Root cause of jarvis/the-plan MCP failures on WSL: Streamable HTTP SSE session conflict (HTTP 409) after ~15 min idle, not wrong ports or API keys.
- Fix: switch `jarvis` and `the-plan` from HTTP/SSE to stdio bridges via `obsidian-mcp-server@3.2.9`.
- Fixed `The Plan/.mcp.json` port typo (was 27123, should be 27124).

## What Changed
- Updated `~/.cursor/mcp.json` (WSL home) to stdio transport for both Obsidian vaults.
- Verified both REST backends respond and stdio processes start cleanly.
- User must reload MCP in Cursor for changes to take effect.

## Important Context
- Workspace: CausalOps on WSL (`vscode-remote://wsl+ubuntu/.../CausalOps`).
- `jarvis-fs` / `the-plan-fs` stdio filesystem MCPs were already stable alternatives to HTTP.
- Background shell verification tasks aborted; config change still applied on disk.

## Source Claims (Quoted From Transcript)
- "409 here means: only one SSE stream per MCP session — a previous one is still registered."
- "Stdio avoids SSE session management entirely — no more 409 reconnect loops."

## Inferred Claims (Distiller Interpretation)
- WSL2 + long-lived localhost SSE to Windows Obsidian is fragile; stdio bridge is the durable fix for this setup.

## Open Questions
- Whether Windows-side `~/.cursor/mcp.json` should match the WSL stdio config when working from both OS contexts.

## Follow-Up Actions
- [ ] Reload MCP (toggle off/on or Developer: Reload Window) after config edits
- [ ] Confirm tool names shift to `obsidian_list_notes` / `obsidian_get_note` post-reload

## Related Notes
- [[60_Claude/07_AI_Information/AI Conversation - Summaries/2026-05-28-cursor-kiro-and-cursor-mcp-configuration-analysis — Summary]]

## Should Be Promoted?
- decision: partial — document stdio-over-HTTP for Obsidian MCP in a durable system note if 409 recurs on other machines.
