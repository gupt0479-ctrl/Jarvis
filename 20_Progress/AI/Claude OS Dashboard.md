---
type: dashboard
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - claude-os
  - ai-infrastructure
  - dashboard
notes:
  - "[[Claude OS]]"
  - "[[10_Areas/AI/Claude Code|Claude Code]]"
next: "Re-export the empty dumps (Claude Code Portfolio + TradingView, Cursor DNA App + Trading View)"
---
# Claude OS Dashboard
Operational view over the AI-tool setups in `20_Progress/AI/`. Strategy and per-item detail live in [[Claude OS]]; this note answers "what exists, what's live, what's dead" at a glance.
## Inventory (verified 2026-07-03)
| Platform | Projects with setups | Live components | Dead/empty dumps |
| --- | --- | --- | --- |
| Claude Code | Jarvis, CausalOps, Resq, OpsPilot, Windows Home, WSL Home | 14 Jarvis commands, 5 agents, 2 hooks, 5 MCP servers; CausalOps 3 agents + 4 commands + 3 hooks | Portfolio, TradingView folders empty |
| Cursor | Jarvis (.cursor/rules ×5), CausalOps, Portfolio, SafeReach, OpsPilot | SafeReach: 7 lifecycle hooks + 8 skills (the reference architecture) | DNA App, Trading View folders empty |
| Kiro | Assisto, Resq, Portfolio, SafeReach, TradingView, OpsPilot, Jarvis (.kiro stub) | Resq agent JSON + 4 hook sets; Assisto 5 steering + 3 hooks + spec | Jarvis .kiro has no agent |
| Codex | Assisto, Portfolio, OpsPilot, Resq | Assisto .agents/ + config.toml; Portfolio 9 source-command-* skills | No usage signal recorded anywhere |
## Health checks
| Check | Status |
| --- | --- |
| jarvis-memory MCP | ✅ running; 8,124 notes indexed; status/search/reindex all respond |
| jarvis-memory semantic search | ❌ chunks/embeddings unpopulated |
| Write guard hook | ✅ allowlist + denials verified with 14 test payloads (2026-07-03) |
| Homepage plugin | ✅ opens [[00_Dashboard]] on startup via lazy-plugins |
| Skills on directory standard | 3 of 14 (startday, closeday, ingesting-clipping) |
| Agents with full frontmatter | 5 of 5 |
| Scheduled automation (morning/evening loop) | ❌ not wired — North Star Move 4 |
## Recently changed setup files
```dataview
TABLE file.folder AS Folder, file.mtime AS "Modified"
FROM "20_Progress/AI"
SORT file.mtime DESC
LIMIT 12
```
## Open actions
- [ ] Re-export empty dumps: Claude Code {Portfolio, TradingView}, Cursor {DNA App, Trading View}
- [ ] Adopt /emerge and /challenge from second-brain-claudekit (gap table in [[Claude OS]])
- [ ] Trial the 8 High-relevance everything-claude-code skills; uninstall the Low bulk
- [ ] Populate jarvis-memory `chunks` → semantic search (North Star 5.4)
- [ ] Convert next most-used flat skill to directory shape (/ingest usage says /ops or /context)
- [ ] Wire scheduled morning context assembly + evening close
