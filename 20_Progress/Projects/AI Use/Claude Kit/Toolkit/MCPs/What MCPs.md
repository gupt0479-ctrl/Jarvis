---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - mcp
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/How to Use MCPs]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
next: Re-check this note if gbrain's embedding-provider decision gets made and it moves toward promotion
---
# What MCPs
==No MCP has cleared second-brain-claudekit's own pipeline yet — GBrain is the only real candidate, and it is still at sandbox stage.==
## Promoted in claudekit
None. GBrain (`sandbox/gbrain/`) cleared the "ran for real" bar — `bun install`, `bun run src/cli.ts init --pglite --no-embedding`, `doctor` reported 80/100 overall health — but is blocked on one named, unresolved decision: which embedding provider (Voyage, ZeroEntropy, or OpenAI) to pay for or accept the free tier of. See [[20_Progress/Projects/AI Use/Claude Kit/Tool Map|Tool Map]]'s GBrain row for the full state. `second-brain-claudekit/_docs/Current-Setup.md` lists MCP servers connected in a live session (`github`, `jarvis`, `jarvis-fs`, `the-plan`, `the-plan-fs`, `graphify`, `pencil`) — these are session-level connections, not artifacts that cleared the qualification pipeline, and are not "promoted" in the pipeline sense this note tracks.
## Live in Jarvis
Verified against `.mcp.json` at the vault root — six servers, committed configuration, not a session snapshot:
- **obsidian** (`uvx mcp-obsidian`) — vault read/write through the Obsidian Local REST API, patch-by-heading, periodic notes. Requires the Local REST API plugin running.
- **filesystem** (`@modelcontextprotocol/server-filesystem`) — direct file access scoped to the vault root.
- **git** (`mcp-server-git`) — git operations on the vault repo.
- **fetch** (`mcp-server-fetch`) — web fetch.
- **jarvis-memory** (`30_Order/System/jarvis-memory/server.py`) — custom SQLite registry (`jarvis_status`, `jarvis_search`, `jarvis_reindex`) — the seed of a semantic index, still keyword-only.
- **excalidraw** (`30_Order/System/excalidraw-mcp`) — drives the live diagram canvas.
`10_Areas/AI/Claude Code.md`'s MCP table lists only five (missing `excalidraw`) — stale against the current `.mcp.json`.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/MCPs/How to Use MCPs]] for when to reach for which server. [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]] for GBrain's real blocker.
