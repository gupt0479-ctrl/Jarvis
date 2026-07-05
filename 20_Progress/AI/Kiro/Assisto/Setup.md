---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - kiro
  - setup
  - assisto
notes:
  - "[[20_Progress/AI/Kiro/MOC]]"
next: "none — external project dump, backend gate blocked on Supabase CLI availability per its own tasks.md"
---
# Assisto — Kiro Setup
A copy of the Kiro workspace for Assisto-Spend, an enterprise spend workflow module (PR/TR/TE) being built inside the real Assisto Next.js app. This is reference material, not part of this vault's own tooling — nothing here reads or writes vault notes. Compare against [[20_Progress/AI/Codex/Assisto - .agents/Setup|Assisto's Codex dump]], which covers the same project's backend-phase-0 freeze from a different tool.
## Files
### Specs (assisto-spend-backend)
- [[20_Progress/AI/Kiro/Assisto/specs/assisto-spend-backend/design|specs/assisto-spend-backend/design]] — layered Next.js backend architecture (Server Actions → guards → workflow engine → audit)
- [[20_Progress/AI/Kiro/Assisto/specs/assisto-spend-backend/requirements|specs/assisto-spend-backend/requirements]] — backend-gate requirements; remote Supabase schema is prototype-derived and not production-approved
- [[20_Progress/AI/Kiro/Assisto/specs/assisto-spend-backend/tasks|specs/assisto-spend-backend/tasks]] — Phases 0-8 task list; Phase 0 done, Phase 1 blocked on Supabase CLI
### Steering
- [[20_Progress/AI/Kiro/Assisto/steering/project-rules|steering/project-rules]] — repo layout, git remotes/branch conventions
- [[20_Progress/AI/Kiro/Assisto/steering/assisto-spend-product|steering/assisto-spend-product]] — product scope: PR/TR/TE flows, Control Tower, Admin, Reports
- [[20_Progress/AI/Kiro/Assisto/steering/assisto-spend-backend|steering/assisto-spend-backend]] — the 10-point backend-first gate
- [[20_Progress/AI/Kiro/Assisto/steering/assisto-spend-security|steering/assisto-spend-security]] — authorization non-negotiables (server-side checks, no self-approval, fail-closed transitions)
- [[20_Progress/AI/Kiro/Assisto/steering/assisto-spend-supabase|steering/assisto-spend-supabase]] — current remote Supabase state (28 tables, migration drift, CLI unavailable)
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Kiro/Assisto"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `settings/mcp.json` — Kiro MCP server config for this project.
- `hooks/backend-preflight.kiro.hook` — pre-work hook enforcing the backend-first gate.
- `hooks/final-report-checklist.kiro.hook` — completion checklist hook.
- `hooks/supabase-safety-check.kiro.hook` — guards against unsafe Supabase operations.
## Status & Gaps
External project dump, no live equivalent in this vault to diff against — every file marked `static`. All 5 steering docs use Kiro's native `inclusion: auto` frontmatter key (tool-native, left untouched); the 3 spec files (design/requirements/tasks) had no frontmatter at all and got a fresh minimal block. Per its own tasks.md, this project's backend work is currently blocked on Supabase CLI availability in WSL — not a gap in this dump, just the project's real state at capture time.
## Links
[[20_Progress/AI/Kiro/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
