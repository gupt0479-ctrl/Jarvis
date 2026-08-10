---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - skills
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/How to Use Skills]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/Github Skills]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/What Commands]]"
next:
---
# What Skills
==Skills carry the logic a command triggers — Jarvis has around 19 skills under .claude/skills/, second-brain-claudekit has zero, since Claude Code's directory-skill format postdates most of that repo's own build.==
## Promoted in claudekit
None. `skills/` at the repo's top level (the staging area for drafts) is empty, confirmed by direct listing. Nothing has reached the skill-authoring stage of the pipeline yet — every promoted artifact in that repo so far is an agent, command, or hook.
## Live in Jarvis
Verified against `.claude/skills/` at the vault root. Three follow the full directory-skill standard (`SKILL.md` + `reference.md`, per [[Jarvis OS — North Star]] Part 5.1): `closeday`, `ingesting-clipping`, `startday`. The rest are flat prose files, still real and in daily use, just not yet converted:
`challenge`, `connect-notes`, `context`, `distill-note`, `excalidraw-diagram`, `ideas`, `lint-claude-layer`, `llm-council`, `mcp-hub` (skill only, no matching command — a reference lookup rather than an invoked action), `note-to-actions`, `ops`, `ops-reference` (a reference doc for `/ops`, not an independently invocable skill), `remove-ai-slop`, `strategy`, `tag-month`, `trace-topic`, `transcript-to-brief`, `weekly-review`.
Every flat file above has a matching command in `.claude/commands/` except `mcp-hub` and `ops-reference` — see [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/What Commands|What Commands]] for the trigger side of this same inventory.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/How to Use Skills]] for when to use each. [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/Github Skills]] for external skill repos evaluated but not yet promoted anywhere.
