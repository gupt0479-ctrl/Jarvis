---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - kiro
  - setup
  - resq
notes:
  - "[[20_Progress/AI/Kiro/MOC]]"
next: "none — external hackathon project dump, largest single folder across all three platforms"
---
# Resq — Kiro Setup
A copy of the Kiro workspace for Resq, an autonomous SMB survival agent (collections, financing scout, vendor/insurance optimization) built for a fintech hackathon — formerly called OpsPilot before a project split (`specs/project-separation/`). At 48 files this is the largest single project folder across Cursor/Kiro/Codex. Reference material only.
## Files
### Skills
- [[20_Progress/AI/Kiro/Resq/skills/smb-survival-agent/SKILL|skills/smb-survival-agent/SKILL]] — mission, core pillars, priority order, operating rules, first-files-to-inspect map
### Steering
- [[20_Progress/AI/Kiro/Resq/steering/project-context|steering/project-context]] — auto-included project context mirror
- [[20_Progress/AI/Kiro/Resq/steering/api-patterns|steering/api-patterns]] — scoped to `**/app/api/**`
- [[20_Progress/AI/Kiro/Resq/steering/supabase-patterns|steering/supabase-patterns]] — scoped to `**/supabase/**,**/db/**,**/services/**`
- [[20_Progress/AI/Kiro/Resq/steering/tinyfish-patterns|steering/tinyfish-patterns]] — scoped to `**/tinyfish/**`
- [[20_Progress/AI/Kiro/Resq/steering/change-gate|steering/change-gate]] — manual-inclusion change-control steering
- [[20_Progress/AI/Kiro/Resq/steering/hackathon-ops|steering/hackathon-ops]] — manual-inclusion hackathon operations mirror
### Specs
- [[20_Progress/AI/Kiro/Resq/specs/improve-decision-reasoning/design|specs/improve-decision-reasoning/design]], [[20_Progress/AI/Kiro/Resq/specs/improve-decision-reasoning/requirements|requirements]], [[20_Progress/AI/Kiro/Resq/specs/improve-decision-reasoning/tasks|tasks]]
- [[20_Progress/AI/Kiro/Resq/specs/loading-screen-catchphrases/design|specs/loading-screen-catchphrases/design]], [[20_Progress/AI/Kiro/Resq/specs/loading-screen-catchphrases/requirements|requirements]], [[20_Progress/AI/Kiro/Resq/specs/loading-screen-catchphrases/tasks|tasks]] — historical, written during the OpsPilot → Resq transition
- [[20_Progress/AI/Kiro/Resq/specs/project-separation/design|specs/project-separation/design]], [[20_Progress/AI/Kiro/Resq/specs/project-separation/requirements|requirements]], [[20_Progress/AI/Kiro/Resq/specs/project-separation/tasks|tasks]] — the OpsPilot ↔ Resq split itself
- [[20_Progress/AI/Kiro/Resq/specs/rescue-demo-polish/design|specs/rescue-demo-polish/design]], [[20_Progress/AI/Kiro/Resq/specs/rescue-demo-polish/requirements|requirements]], [[20_Progress/AI/Kiro/Resq/specs/rescue-demo-polish/tasks|tasks]]
- [[20_Progress/AI/Kiro/Resq/specs/resq-cash-breakpoint-agent/design|specs/resq-cash-breakpoint-agent/design]], [[20_Progress/AI/Kiro/Resq/specs/resq-cash-breakpoint-agent/requirements|requirements]], [[20_Progress/AI/Kiro/Resq/specs/resq-cash-breakpoint-agent/tasks|tasks]]
- [[20_Progress/AI/Kiro/Resq/specs/tinyfish-financing-stability/bugfix|specs/tinyfish-financing-stability/bugfix]], [[20_Progress/AI/Kiro/Resq/specs/tinyfish-financing-stability/design|design]], [[20_Progress/AI/Kiro/Resq/specs/tinyfish-financing-stability/tasks|tasks]]
- [[20_Progress/AI/Kiro/Resq/specs/tinyfish-portal-login/design|specs/tinyfish-portal-login/design]], [[20_Progress/AI/Kiro/Resq/specs/tinyfish-portal-login/requirements|requirements]], [[20_Progress/AI/Kiro/Resq/specs/tinyfish-portal-login/tasks|tasks]] — historical, OpsPilot → Resq transition
- [[20_Progress/AI/Kiro/Resq/specs/tinyfish-sse-async-harness/design|specs/tinyfish-sse-async-harness/design]], [[20_Progress/AI/Kiro/Resq/specs/tinyfish-sse-async-harness/requirements|requirements]], [[20_Progress/AI/Kiro/Resq/specs/tinyfish-sse-async-harness/tasks|tasks]] — requirements doc is historical, OpsPilot → Resq transition
### Docs
- [[20_Progress/AI/Kiro/Resq/hooks/README|hooks/README]] — describes the shared Kiro hook set below
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Kiro/Resq"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `agents/resq.json` — Kiro agent definition for the Resq product agent.
- `settings/mcp.json` — Kiro MCP server config for this project.
- `hooks/canon-gate.sh`, `hooks/demo-safety.sh`, `hooks/secret-hygiene.sh` — shell-based lifecycle hooks.
- `hooks/finance-guard.json`, `hooks/secret-hygiene.json`, `hooks/verify-build.json` — hook registration configs.
- `skills/supabase`, `skills/supabase-postgres-best-practices` — broken symlink placeholders (same as [[20_Progress/AI/Kiro/OpsPilot/Setup|Kiro/OpsPilot]]), pointing at `../../.agents/skills/...`. Not real files.
- 6 `.config.kiro` files under `specs/*/` (improve-decision-reasoning, loading-screen-catchphrases, project-separation, resq-cash-breakpoint-agent, tinyfish-portal-login, tinyfish-sse-async-harness) — Kiro spec metadata, not markdown.
## Status & Gaps
External project dump, no live equivalent in this vault to diff against — every real file marked `static`. `skills/smb-survival-agent/SKILL.md` had a pre-existing `description:` value with an unquoted colon (`Build and operate the Resq product: an autonomous...`), which is invalid YAML and would have made the whole frontmatter block — including the new `setup_status` field — unparseable by Dataview. Quoted the value to fix it; no wording changed. Several spec docs across `loading-screen-catchphrases`, `tinyfish-portal-login`, and `tinyfish-sse-async-harness` open with an identical "Historical Note" flagging that they predate the OpsPilot → Resq rename — this is the project's own annotation, not a defect in the dump. The `skills/supabase*` entries are the same broken-symlink artifacts documented in [[20_Progress/AI/Kiro/OpsPilot/Setup|Kiro/OpsPilot's Setup]]; both point at Codex's Assisto `.agents/skills/` content.
## Links
[[20_Progress/AI/Kiro/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
