---
type: index
status: active
created: 2026-07-05
updated: 2026-07-05
tags:
  - cursor
  - moc
  - index
notes:
  - "[[20_Progress/AI/Claude OS Dashboard]]"
  - "[[20_Progress/AI/Cursor/CausalOps/Setup]]"
  - "[[20_Progress/AI/Cursor/DNA App/Setup]]"
  - "[[20_Progress/AI/Cursor/Jarvis/Setup]]"
  - "[[20_Progress/AI/Cursor/OpsPilot/Setup]]"
  - "[[20_Progress/AI/Cursor/Portfolio/Setup]]"
  - "[[20_Progress/AI/Cursor/SafeReach/Setup]]"
  - "[[20_Progress/AI/Cursor/Trading View/Setup]]"
next: "Re-export DNA App and Trading View .cursor/ config if either project resumes"
---
# Cursor — Content Map
Every project folder under `20_Progress/AI/Cursor/` now has a `Setup.md` that inventories its files and tags each markdown note with a `setup_status`. This MOC is the one place to see all of them at once and find what needs work, without opening every folder.
`.cursor_windows/` and `.cursor_wsl/` are excluded from this map on purpose — they're raw mirrors of `~/.cursor` (13,690 and 3,951 files respectively: extensions, cache, daemon state), not hand-authored project configs. They're noted here for completeness, not tracked.
## Projects
| Project | Status | Last Updated | Setup |
|---|---|---|---|
| Jarvis | stale | 2026-07-05 | [[20_Progress/AI/Cursor/Jarvis/Setup\|Setup]] |
| CausalOps | static | 2026-07-05 | [[20_Progress/AI/Cursor/CausalOps/Setup\|Setup]] |
| OpsPilot | static | 2026-07-05 | [[20_Progress/AI/Cursor/OpsPilot/Setup\|Setup]] |
| Portfolio | static | 2026-07-05 | [[20_Progress/AI/Cursor/Portfolio/Setup\|Setup]] |
| SafeReach | static | 2026-07-05 | [[20_Progress/AI/Cursor/SafeReach/Setup\|Setup]] |
| DNA App | dead | 2026-07-05 | [[20_Progress/AI/Cursor/DNA App/Setup\|Setup]] |
| Trading View | dead | 2026-07-05 | [[20_Progress/AI/Cursor/Trading View/Setup\|Setup]] |
| .cursor_windows | unmanaged mirror | — | not tracked (raw `~/.cursor` backup, ~13,690 files) |
| .cursor_wsl | unmanaged mirror | — | not tracked (raw `~/.cursor` backup, ~3,951 files) |
## Needs Work
```dataview
TABLE setup_status, updated, file.folder AS Project
FROM "20_Progress/AI/Cursor"
WHERE setup_status AND setup_status != "current"
SORT setup_status ASC, file.folder ASC
```
## All Tracked Files
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Cursor"
WHERE setup_status
SORT file.folder ASC, file.name ASC
```
## Links
[[20_Progress/AI/Claude OS Dashboard]] · [[20_Progress/AI/Claude Code/MOC]]
