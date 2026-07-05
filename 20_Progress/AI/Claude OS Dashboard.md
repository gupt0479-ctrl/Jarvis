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
  - "[[20_Progress/AI/Cursor/MOC]]"
  - "[[20_Progress/AI/Kiro/MOC]]"
  - "[[20_Progress/AI/Codex/MOC]]"
next: "Setup.md/MOC.md/frontmatter pass complete on all 4 platforms (2026-07-05); still need Cursor DNA App + Trading View re-exported (empty dumps)"
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
| **Cursor** | Jarvis (rules ×5, current), CausalOps, Portfolio, SafeReach, OpsPilot | SafeReach: 7 lifecycle hooks + 8 skills (richest multi-agent handoff architecture seen); Jarvis mcp.json + all 5 rules byte-identical to live `.cursor/` | DNA App, Trading View folders empty |
| **Kiro** | Jarvis (current, 0 drift), Assisto, OpsPilot (dead — 2 broken symlinks only), Portfolio, Resq (48 files, largest single folder), SafeReach, The Plan, TradingView | Resq agent JSON + 7 hooks + 8 spec folders; SafeReach shares locked PRD/deployment-guide context with its Cursor dump; The Plan mirrors Jarvis's own specs (diverged, expected) | OpsPilot has no real config, only dangling symlinks to Codex's Assisto skills |
| **Codex** | Assisto (.agents + .codex), OpsPilot, Portfolio, Resq | Assisto .agents/ + config.toml; Portfolio 9 source-command-* skills; OpsPilot + Resq both carry the vendored `supabase`/`supabase-postgres-best-practices` skill packages | No usage signal recorded; light-touch pass only, no deep gap analysis |
=== end-column ===
## Open Actions
- [x] Re-export empty dumps: Claude Code {Portfolio, Trading View} — done 2026-07-05
- [x] Setup.md/MOC.md/frontmatter pass on Cursor, Kiro, Codex — done 2026-07-05
- [ ] Re-export empty dumps: Cursor {DNA App, Trading View}
- [ ] Adopt /emerge and /challenge (gap table in [[Claude OS]] — now confirmed by 3 sources)
- [ ] Trial the 8 High-relevance everything-claude-code skills; uninstall the Low bulk
- [ ] Populate jarvis-memory `chunks` → semantic search (North Star 5.4)
- [ ] Convert next most-used flat skill to directory shape (/ops or /context)
- [ ] Wire scheduled morning context assembly + evening close (Move 4)
=== end-multi-column
## Setup Coverage
All four platforms are fully mapped: every project folder has a `Setup.md` inventorying its files, rolled up in each platform's MOC. Cursor and Kiro got full-rigor treatment (live-vs-dump diffing where a live equivalent exists); Codex got a light-touch pass (frontmatter + Files list + Inventory table only, no gap analysis).
| Platform | Setup.md coverage | MOC.md |
| --- | --- | --- |
| **Claude Code** | 8 of 8 project folders | [[20_Progress/AI/Claude Code/MOC\|MOC]] |
| **Cursor** | 7 of 7 project folders | [[20_Progress/AI/Cursor/MOC\|MOC]] |
| **Kiro** | 8 of 8 project folders | [[20_Progress/AI/Kiro/MOC\|MOC]] |
| **Codex** | 5 of 5 project folders (light touch) | [[20_Progress/AI/Codex/MOC\|MOC]] |
## Recently Changed Setup Files
```dataview
TABLE file.folder AS Folder, file.mtime AS "Modified"
FROM "20_Progress/AI"
SORT file.mtime DESC
LIMIT 12
```
---
[[Claude OS]] · [[10_Areas/AI/Claude Code|Claude Code guide]] · [[10_Areas/AI/Cursor|Cursor guide]] · [[10_Areas/AI/Kiro|Kiro guide]] · [[10_Areas/AI/Codex|Codex guide]] · [[00_Dashboard]]
