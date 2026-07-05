---
type: index
status: active
created: 2026-07-05
updated: 2026-07-05
tags:
  - kiro
  - moc
  - index
notes:
  - "[[20_Progress/AI/Claude OS Dashboard]]"
  - "[[20_Progress/AI/Kiro/Assisto/Setup]]"
  - "[[20_Progress/AI/Kiro/Jarvis/Setup]]"
  - "[[20_Progress/AI/Kiro/OpsPilot/Setup]]"
  - "[[20_Progress/AI/Kiro/Portfolio/Setup]]"
  - "[[20_Progress/AI/Kiro/Resq/Setup]]"
  - "[[20_Progress/AI/Kiro/SafeReach/Setup]]"
  - "[[20_Progress/AI/Kiro/The Plan/Setup]]"
  - "[[20_Progress/AI/Kiro/TradingView/Setup]]"
next: "none — all seven real Kiro project folders mapped; OpsPilot's two files are broken symlinks, nothing more to capture there"
---
# Kiro — Content Map
Every project folder under `20_Progress/AI/Kiro/` now has a `Setup.md` that inventories its files and tags each markdown note with a `setup_status`. This MOC is the one place to see all of them at once and find what needs work, without opening every folder.
`.kiro_wsl/` is excluded from this map on purpose — it's a raw mirror of `~/.kiro` (5,182 files: extensions, cache, daemon state), not a hand-authored project config. It's noted here for completeness, not tracked.
## Projects
| Project | Status | Last Updated | Setup |
|---|---|---|---|
| Jarvis | current | 2026-07-05 | [[20_Progress/AI/Kiro/Jarvis/Setup\|Setup]] |
| Assisto | static | 2026-07-05 | [[20_Progress/AI/Kiro/Assisto/Setup\|Setup]] |
| OpsPilot | dead | 2026-07-05 | [[20_Progress/AI/Kiro/OpsPilot/Setup\|Setup]] |
| Portfolio | static | 2026-07-05 | [[20_Progress/AI/Kiro/Portfolio/Setup\|Setup]] |
| Resq | static | 2026-07-05 | [[20_Progress/AI/Kiro/Resq/Setup\|Setup]] |
| SafeReach | static | 2026-07-05 | [[20_Progress/AI/Kiro/SafeReach/Setup\|Setup]] |
| The Plan | static | 2026-07-05 | [[20_Progress/AI/Kiro/The Plan/Setup\|Setup]] |
| TradingView | static | 2026-07-05 | [[20_Progress/AI/Kiro/TradingView/Setup\|Setup]] |
| .kiro_wsl | unmanaged mirror | — | not tracked (raw `~/.kiro` backup, ~5,182 files) |
## Needs Work
```dataview
TABLE setup_status, updated, file.folder AS Project
FROM "20_Progress/AI/Kiro"
WHERE setup_status AND setup_status != "current"
SORT setup_status ASC, file.folder ASC
```
## All Tracked Files
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Kiro"
WHERE setup_status
SORT file.folder ASC, file.name ASC
```
## Links
[[20_Progress/AI/Claude OS Dashboard]] · [[20_Progress/AI/Claude Code/MOC]] · [[20_Progress/AI/Cursor/MOC]]
