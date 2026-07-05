---
type: dashboard
status: sprout
created: 2026-07-03
updated: 2026-07-05
tags:
  - claude-os
  - ai-infrastructure
  - dashboard
cssclasses:
  - dashboard
notes:
  - "[[Claude OS]]"
  - "[[10_Areas/AI/Claude Code|Claude Code]]"
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: "Claude Code Portfolio + Trading View re-exported 2026-07-05; still need Cursor DNA App + Trading View re-exported, then run the same Setup.md/MOC.md/frontmatter pass on Cursor, Kiro, Codex"
---
# Claude OS — Operational Registry
*Last verified: `$= moment().format("YYYY-MM-DD")`*
Operational view over the AI-tool setups in `20_Progress/AI/`. Strategy and per-item detail live in [[Claude OS]]; this note answers "what exists, what's live, what's dead" at a glance.
## Health Panel
```dataviewjs
const checks = [
  {name: 'jarvis-memory MCP',      status: '✅', detail: '8,158 notes indexed'},
  {name: 'Semantic search',         status: '❌', detail: 'chunks/embeddings unpopulated'},
  {name: 'Write guard',             status: '✅', detail: 'allowlist + 14 test payloads verified'},
  {name: 'Homepage plugin',         status: '✅', detail: 'opens Jarvis OS Dashboard canvas on startup'},
  {name: 'Skills on dir standard',  status: '⚠️', detail: '3 of 14'},
  {name: 'Agents with frontmatter', status: '✅', detail: '5 of 5'},
  {name: 'Scheduled loop (Move 4)', status: '❌', detail: 'still manual /startday + /closeday'},
];
const container = dv.el('div', '', {cls: 'stat-grid'});
container.innerHTML = checks.map(c => `
  <div class="stat-tile">
    <div class="stat-label">${c.name}</div>
    <div class="stat-value" style="font-size:1.2rem">${c.status}</div>
    <div class="stat-delta neutral" style="font-size:0.65rem">${c.detail}</div>
  </div>
`).join('');
```
=== start-multi-column: ClaudeOS
```column-settings
Number of Columns: 2
Largest Column: left
Border: off
Shadow: off
```
## Platform Inventory
| Platform | Projects | Live components | Dead/empty |
| --- | --- | --- | --- |
| **Claude Code** | Jarvis, CausalOps, Resq, OpsPilot, Portfolio, Trading View, .claude_windows, .claude_wsl | 14 Jarvis commands, 5 agents, 2 hooks, 5 MCP servers; CausalOps 3 agents + 4 commands + 3 hooks; Portfolio 7 agents + 10 commands; Trading View 2 agents + 2 skills | Github ReadMe (settings only) |
| **Cursor** | Jarvis (rules ×5), CausalOps, Portfolio, SafeReach, OpsPilot | SafeReach: 7 lifecycle hooks + 8 skills (reference architecture) | DNA App, Trading View folders empty |
| **Kiro** | Assisto, Resq, Portfolio, SafeReach, TradingView, OpsPilot, Jarvis (stub) | Resq agent JSON + 4 hook sets; Assisto 5 steering + 3 hooks + spec | Jarvis .kiro has no agent |
| **Codex** | Assisto, Portfolio, OpsPilot, Resq | Assisto .agents/ + config.toml; Portfolio 9 source-command-* skills | No usage signal recorded |
=== end-column ===
## Open Actions
- [x] Re-export empty dumps: Claude Code {Portfolio, Trading View} — done 2026-07-05
- [ ] Re-export empty dumps: Cursor {DNA App, Trading View}
- [ ] Adopt /emerge and /challenge (gap table in [[Claude OS]] — now confirmed by 3 sources)
- [ ] Trial the 8 High-relevance everything-claude-code skills; uninstall the Low bulk
- [ ] Populate jarvis-memory `chunks` → semantic search (North Star 5.4)
- [ ] Convert next most-used flat skill to directory shape (/ops or /context)
- [ ] Wire scheduled morning context assembly + evening close (Move 4)
=== end-multi-column
## Setup Coverage
`Claude Code/` is fully mapped: every project folder has a `Setup.md` inventorying its files, rolled up in [[20_Progress/AI/Claude Code/MOC]]. Cursor, Kiro, and Codex don't have this yet — pending follow-up round.
| Platform | Setup.md coverage | MOC.md |
| --- | --- | --- |
| **Claude Code** | 8 of 8 project folders | [[20_Progress/AI/Claude Code/MOC\|MOC]] |
| **Cursor** | none yet | pending |
| **Kiro** | none yet | pending |
| **Codex** | none yet | pending |
## Recently Changed Setup Files
```dataview
TABLE file.folder AS Folder, file.mtime AS "Modified"
FROM "20_Progress/AI"
SORT file.mtime DESC
LIMIT 12
```
---
[[Claude OS]] · [[10_Areas/AI/Claude Code|Claude Code guide]] · [[10_Areas/AI/Cursor|Cursor guide]] · [[10_Areas/AI/Kiro|Kiro guide]] · [[10_Areas/AI/Codex|Codex guide]] · [[00_Dashboard]]
