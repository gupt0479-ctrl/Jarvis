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
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/How to Use Agents]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Claude Code]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
next: Re-check this note the same session anything is promoted from second-brain-claudekit's sandbox into either agents folder
---
# What Agents
==Nothing has been promoted from second-brain-claudekit's sandbox into any agents folder yet — every agent below is either the repo's original scaffold or Jarvis's own hand-built five.==
## Promoted in claudekit
second-brain-claudekit's own `.claude/agents/` holds three, unchanged since the repo's initial scaffold (`d35f0b7`, 2026-04-03) — none came through the sandbox → tested-tools → promoted pipeline; they predate that pipeline entirely.
- **vault-curator** — keeps that repo's own PARA notes linked, clean, deduplicated.
- **research-distiller** — turns rough captures into compact evergreen notes inside that repo.
- **weekly-reviewer** — runs its end-of-week review and writes the weekly summary.
A separate top-level `agents/` folder in the repo (`connector.md`, `researcher.md`, `reviewer.md`, `writer.md`) is a staging area for drafts, not promoted content — see [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/How to Use Agents|How to Use Agents]] before treating anything there as ready to use.
## Live in Jarvis
Verified against `.claude/agents/` at the vault root, not the 2026-07-05 snapshot in `20_Progress/AI/Claude Code/Jarvis/`, which [[20_Progress/AI/Claude Code/MOC]] already flags stale. Five agents, all Jarvis-native — none sourced from claudekit's sandbox:
- **research-distiller** — deep source ingestion; the only agent with Bash + WebFetch access.
- **anti-slop-editor** — rewrites AI-sounding prose per [[HUMAN_WRITING]].
- **vault-curator** — link, duplicate, and frontmatter health, report-first.
- **learning-agent** — spaced-repetition drills over Capability Engine fields.
- **career-operator** — internship, resume, and mentorship briefs.
Jarvis's `research-distiller` and `vault-curator` share a name with claudekit's promoted pair above but are independently built — same job description, no shared code, confirmed by reading both files directly.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Agents/How to Use Agents]] for when to reach for each. [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]] for what is still in sandbox and could eventually add an agent here.
