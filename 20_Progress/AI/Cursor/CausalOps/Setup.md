---
type: project
status: static
created: 2026-07-05
updated: 2026-07-05
tags:
  - cursor
  - setup
  - causalops
notes:
  - "[[20_Progress/AI/Cursor/MOC]]"
next: "none — reference dump from the CausalOps repo, not synced to this vault"
---
# CausalOps — Cursor Setup
A copy of the Cursor config from the separate CausalOps project (a causal-pipeline/coordinator system with a HiveMind memory layer) — the same project as [[20_Progress/AI/Claude Code/CausalOps/Setup|CausalOps' Claude Code dump]], captured for its Cursor-specific layer. This is reference material, not part of the Jarvis vault's own tooling — nothing here reads or writes vault notes.
## Files
### Docs
- [[20_Progress/AI/Cursor/CausalOps/README|README]] — layout guide for `.cursor/` in the HiveMind repo (rules/skills/hooks/agents) plus the global MCP server table
### Skills
- [[20_Progress/AI/Cursor/CausalOps/skills/hivemind-project/SKILL|skills/hivemind-project/SKILL]] — architecture anchors and guardrails for editing the HiveMind repo
- [[20_Progress/AI/Cursor/CausalOps/skills/persistent-semantic-memory/SKILL|skills/persistent-semantic-memory/SKILL]] — design checklist for HiveMind's memory/retrieval layer
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Cursor/CausalOps"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `hooks.json` — Cursor hook registration for this project.
- `hooks/preflight.sh` — session preflight/guardrail script.
- `rules/hivemind-core.mdc` — always-on Cursor rule for the HiveMind repo.
## Status & Gaps
This is an external project's config, imported wholesale — there is no live equivalent in this vault to diff against, so every file is marked `static` rather than current/stale. Nothing here needs updating unless the source CausalOps repo changes and this dump is deliberately re-exported.
## Links
[[20_Progress/AI/Cursor/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
