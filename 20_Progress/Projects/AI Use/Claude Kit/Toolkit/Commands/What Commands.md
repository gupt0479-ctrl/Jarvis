---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - commands
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/How to Use Commands]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills]]"
next:
---
# What Commands
==A command is the trigger; the skill behind it is the logic — this note inventories triggers, [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills|What Skills]] inventories what actually runs.==
## Promoted in claudekit
second-brain-claudekit's `.claude/commands/`, 11 files, all from the original scaffold: `context`, `today`, `trace`, `graduate`, `closeday`, `emerge`, `ghost`, `challenge`, `ideas`, `drift`, `schedule`. A separate top-level `commands/` folder in the repo (11 different files: `preserve`, `compress`, `resume`, `capture`, `brainstorm`, `connect`, `research`, `review`, `summarize`, `inbox-process`, `journal`) is the repo's *global* command set, meant to be copied to `~/.claude/commands/` — not yet copied anywhere, still repo-local.
## Live in Jarvis
Verified against `.claude/commands/` at the vault root — 19 files: `challenge`, `closeday`, `connect-notes`, `context`, `distill-note`, `excalidraw-diagram`, `ideas`, `ingest-clipping`, `lint-claude-layer`, `llm-council`, `note-to-actions`, `ops`, `remove-ai-slop`, `startday`, `strategy`, `tag-month`, `trace-topic`, `transcript-to-brief`, `weekly-review`. Four names collide with claudekit's promoted set above (`context`, `closeday`, `challenge`, `ideas`) — independently built, confirmed by reading both files; no code is shared between them.
`10_Areas/AI/Claude Code.md`'s command table (14 rows, dated 2026-07-03) is stale against this list — it is missing `challenge`, `excalidraw-diagram`, `ideas`, `llm-council`, `note-to-actions`, `strategy`, and `transcript-to-brief` (all built later, 2026-07-29 per [[20_Progress/Projects/AI Use/Builds & Resources/Claude Council (LLM Council Skill Install)|Claude Council]] and [[20_Progress/Projects/AI Use/Builds & Resources/Maverick Skills Mode-to-Repo Mapping|Maverick Skills Mode-to-Repo Mapping]]), and still lists `organize-csci2033`, which is no longer present in the live `commands/` folder.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/How to Use Commands]] for when to type which one. [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills]] for the logic each command triggers.
