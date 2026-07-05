---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - claude-code
  - setup
  - causalops
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: "none — reference dump from the CausalOps repo, not synced to this vault"
---
# CausalOps — Claude Code Setup
A copy of the Claude Code config from the separate CausalOps project (a causal-pipeline/coordinator system with a HiveMind memory layer). This is reference material, not part of the Jarvis vault's own tooling — nothing here reads or writes vault notes.
## Files
### Agents
- [[20_Progress/AI/Claude Code/CausalOps/agents/causal-safeguard-reviewer|causal-safeguard-reviewer]] — read-only reviewer of the causal pipeline's statistical integrity
- [[20_Progress/AI/Claude Code/CausalOps/agents/coordinator-expert|coordinator-expert]] — specialist for the Phase 2b coordinator execution model (RunRecord serialization, `execute_run()`, SQLite locks, Kafka barrier timeouts)
- [[20_Progress/AI/Claude Code/CausalOps/agents/memory-layer-specialist|memory-layer-specialist]] — specialist for the HiveMind memory layer (`src/memory/`)
### Commands
- [[20_Progress/AI/Claude Code/CausalOps/commands/lint|lint]] — runs ruff + pyright on memory/coordinator code
- [[20_Progress/AI/Claude Code/CausalOps/commands/memory-test|memory-test]]
- [[20_Progress/AI/Claude Code/CausalOps/commands/smoke|smoke]]
- [[20_Progress/AI/Claude Code/CausalOps/commands/unit-test|unit-test]]
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Claude Code/CausalOps"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `hooks/guard-sacred-files.sh` — pre-edit hook blocking changes to protected files.
- `hooks/lint-on-edit.sh` — runs lint automatically after an edit.
- `hooks/test-memory-on-edit.sh` — runs memory-layer tests automatically after an edit.
- `scheduled_tasks.lock` — CausalOps scheduled-task lock file.
- `settings.local.json` — local Claude Code permission overrides for this project.
## Status & Gaps
This is an external project's config, imported wholesale — there is no live equivalent in this vault to diff against, so every file is marked `static` rather than current/stale. Nothing here needs updating unless the source CausalOps repo changes and this dump is deliberately re-exported.
## Links
[[20_Progress/AI/Claude Code/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
