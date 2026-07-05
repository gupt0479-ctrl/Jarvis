---
type: project
status: draft
created: 2026-07-05
updated: 2026-07-05
tags:
  - claude-code
  - setup
  - the-plan
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: "none — reference dump; agents/skills use prose-only shape instead of YAML frontmatter, would need a rewrite to match the Jarvis convention if ever adopted here"
---
# The Plan — Claude Code Setup
A copy of the Claude Code config for a project called "The Plan." Unlike every other folder in `Claude Code/`, its agents and skills carry **no YAML frontmatter at all** — each file opens with a `# name` heading and plain bold-text fields (`**Type:** Subagent`, `**Description:** ...`) instead of the `name:`/`description:` keys used everywhere else (Jarvis, CausalOps). Reference material only.
## Files
### Agents
- [[20_Progress/AI/Claude Code/The Plan/agents/career-operator|career-operator]]
- [[20_Progress/AI/Claude Code/The Plan/agents/research-distiller|research-distiller]]
- [[20_Progress/AI/Claude Code/The Plan/agents/vault-curator|vault-curator]]
### Skills
- [[20_Progress/AI/Claude Code/The Plan/skills/closeday|closeday]]
- [[20_Progress/AI/Claude Code/The Plan/skills/connect-notes|connect-notes]]
- [[20_Progress/AI/Claude Code/The Plan/skills/context|context]]
- [[20_Progress/AI/Claude Code/The Plan/skills/distill-note|distill-note]]
- [[20_Progress/AI/Claude Code/The Plan/skills/ingest-clipping|ingest-clipping]]
- [[20_Progress/AI/Claude Code/The Plan/skills/lint-claude-layer|lint-claude-layer]]
- [[20_Progress/AI/Claude Code/The Plan/skills/organize-csci2033|organize-csci2033]]
- [[20_Progress/AI/Claude Code/The Plan/skills/today|today]]
- [[20_Progress/AI/Claude Code/The Plan/skills/trace-topic|trace-topic]]
- [[20_Progress/AI/Claude Code/The Plan/skills/weekly-review|weekly-review]]
## Inventory
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Claude Code/The Plan"
WHERE setup_status
SORT setup_status ASC, file.name ASC
```
## Non-Markdown Files
- `settings.json` — Claude Code project settings for this dump.
- `settings.local.json` — local permission overrides for this dump.
## Status & Gaps
Every file marked `draft` because the frontmatter/prose shape here predates the `name:`/`description:` convention used in Jarvis and CausalOps — these were never brought up to that standard. `skills/today.md` has no equivalent skill name anywhere else in this vault's dumps (the other three platforms call the same idea `startday`); worth a note if this project is ever actively maintained again.
## Links
[[20_Progress/AI/Claude Code/MOC]] · [[20_Progress/AI/Claude OS Dashboard]]
