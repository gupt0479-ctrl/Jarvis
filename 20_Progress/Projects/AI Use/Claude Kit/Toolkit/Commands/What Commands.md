---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-19
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
second-brain-claudekit's `.claude/commands/`, 11 files, all from the original scaffold: `context`, `today`, `trace`, `graduate`, `closeday`, `emerge`, `ghost`, `challenge`, `ideas`, `drift`, `schedule`. **As of 2026-08-19, the top-level `commands/` folder is empty** and no longer the repo's global command set — verified by direct listing, not carried over. Its 11 files split two ways, both resolved for real: `preserve.md`/`compress.md`/`resume.md` went through a real qualification pass against the external `EliaAlberti/cpr-compress-preserve-resume` repo (cloned into `sandbox/`, installed into a scratch project, exercised for real) and landed — **verdict: blend** — in `tested-tools/commands/cpr-compress-preserve-resume/`, with the old hand-authored trio archived to `.claude/_archive/superseded-commands/`, not deleted; the other 8 (`capture`, `brainstorm`, `connect`, `research`, `review`, `summarize`, `inbox-process`, `journal`) were confirmed zero-provenance (same scaffold commit as the agents/hooks batch) and relocated to `tested-tools/commands/native-scaffold/`. `commands/` is now per-destination-project staging (`commands/<ProjectName>/`, created only when real content lands), not a global-command drop point — see [[20_Progress/Projects/AI Use/Claude Kit/Tool Map|Tool Map]]'s cpr-compress-preserve-resume and native-scaffold rows for the full evidence.
## Live in Jarvis
Verified against `.claude/commands/` at the vault root — 19 files: `challenge`, `closeday`, `connect-notes`, `context`, `distill-note`, `excalidraw-diagram`, `ideas`, `ingest-clipping`, `lint-claude-layer`, `llm-council`, `note-to-actions`, `ops`, `remove-ai-slop`, `startday`, `strategy`, `tag-month`, `trace-topic`, `transcript-to-brief`, `weekly-review`. Four names collide with claudekit's promoted set above (`context`, `closeday`, `challenge`, `ideas`) — independently built, confirmed by reading both files; no code is shared between them.
`10_Areas/AI/Claude Code.md`'s command table (14 rows, dated 2026-07-03) is stale against this list — it is missing `challenge`, `excalidraw-diagram`, `ideas`, `llm-council`, `note-to-actions`, `strategy`, and `transcript-to-brief` (all built later, 2026-07-29 per [[20_Progress/Projects/AI Use/Builds & Resources/Claude Council (LLM Council Skill Install)|Claude Council]] and [[20_Progress/Projects/AI Use/Builds & Resources/Maverick Skills Mode-to-Repo Mapping|Maverick Skills Mode-to-Repo Mapping]]), and still lists `organize-csci2033`, which is no longer present in the live `commands/` folder.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Commands/How to Use Commands]] for when to type which one. [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Skills/What Skills]] for the logic each command triggers.
