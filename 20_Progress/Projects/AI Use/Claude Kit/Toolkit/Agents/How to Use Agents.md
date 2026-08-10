---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - agents
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/What Agents]]"
  - "[[Research & Distillation]]"
  - "[[Vault Curation]]"
  - "[[Writing Quality]]"
  - "[[Learning & Mastery]]"
  - "[[Career Ops]]"
next:
---
# How to Use Agents
==An agent earns its own dispatch when a task needs a long, focused run with its own tool allowlist — not for a single quick edit a direct Read/Edit call already handles.==
# Claude Kit
Guidance for second-brain-claudekit's own three promoted agents, usable in any session working inside that repo specifically — none of these are wired into Jarvis's `.claude/`.
- **vault-curator** — invoke before a session ends if more than a handful of notes were touched; it reports link/dedup issues first, does not fix silently.
- **research-distiller** — invoke right after a raw capture lands in `00_Daily/`, before the idea cools, to turn it into a compact evergreen note.
- **weekly-reviewer** — invoke once, at the actual end of a week, not mid-week; it expects a full week of session logs to summarize.
# Particular Use
## Research & Distillation
Jarvis's `research-distiller` agent is the one to use — see [[Research & Distillation]] for the full use-case note and when to prefer it over the `/ingest-clipping` skill directly.
## Vault Curation
Jarvis's `vault-curator` agent, report-first by design — see [[Vault Curation]].
## Writing Quality
`anti-slop-editor` — rewrites per [[HUMAN_WRITING]], never touches frontmatter or links — see [[Writing Quality]].
## Learning & Mastery
`learning-agent` — spaced-repetition drills, only touches frontmatter with approval — see [[Learning & Mastery]].
## Career Ops
`career-operator` — internship, resume, and mentorship briefs — see [[Career Ops]].
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/What Agents]] for the underlying inventory this note gives usage guidance for.
