---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - kiro
  - setup
  - portfolio
notes:
  - "[[20_Progress/AI/Kiro/MOC]]"
next: "none — external project dump, not synced to this vault"
---
# Portfolio — Kiro Setup
A copy of the Kiro steering docs for the same Next.js + Sanity + Three.js portfolio site covered by [[20_Progress/AI/Claude Code/Portfolio/Setup|Portfolio's Claude Code dump]] and [[20_Progress/AI/Cursor/Portfolio/Setup|Cursor dump]]. Reference material only.
## Files
### Steering
- [[20_Progress/AI/Kiro/Portfolio/steering/portfolio-v1|steering/portfolio-v1]] — stack reference: Next.js 16 App Router, Tailwind v4 CSS-first, shadcn/Radix, Framer Motion
- [[20_Progress/AI/Kiro/Portfolio/steering/orby-system|steering/orby-system]] — architecture and constraints for Orby, the portfolio's 3D scroll companion + AI chatbot
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Kiro/Portfolio"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `settings/mcp.json` — Kiro MCP server config for this project.
## Status & Gaps
External project dump, no live equivalent in this vault to diff against — marked `static`. `orby-system.md` uses Kiro's `fileMatch` inclusion mode scoped to specific source paths (not `auto`/`always` like most other steering docs in this vault's dumps) — worth noting since it's the only file-scoped steering doc seen across Cursor/Kiro/Codex.
## Links
[[20_Progress/AI/Kiro/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
