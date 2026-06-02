---
type: evergreen
status: sprout
created: 2026-06-01
updated: 2026-06-01
tags:
  - system
  - standards
notes:
  - "[[30_Order/Templates/Metadata/For Progress|For Progress]]"
  - "[[Brief to Progress]]"
  - "[[Vault Rules — Complete AI Ruleset]]"
  - "[[HUMAN_WRITING]]"
---
# Project Standard
==A project note tracks current state and the single next move so the dashboard can surface it — a project note without a live `next:` is invisible to the system.==
This is the content standard for `project` notes in `20_Progress/`. The brief in `40_Project_Briefs/` is the thinking; the project note is the doing. Its job is continuity: at any milestone, the note tells you what is true now, what to do next, and what already happened. Update it by appending to the log — never by rewriting history.
## Maps To
- Template: [[30_Order/Templates/Metadata/For Progress|For Progress]]
## Used By Workflow
- [[Brief to Progress]] — the create-the-note step reads this Standard first. Write the brief in `40_Project_Briefs/` before the project note exists.
## Per-Heading Standard
### Frontmatter
`type: project`, `status:` one of `active | paused | complete | archived`, `created`/`updated`, `deadline:` if one exists, `tags:`, and `next:` — the single next move, mirrored in the `## Next Action` section. Set `related_progress:` / `notes:` to the brief and supporting concepts.
> [!WARNING]
> An `active` project with an empty `next:` — it drops out of the "projects missing a next action" dashboard. Jarvis carries `next: Build Week 1 registry hardening...` mirrored in its body.
### Goal
One sentence: what done looks like.
*Density:* a single outcome sentence; this is the `==highlight==` anchor if the note uses one.
> [!WARNING]
> A feature list instead of an outcome. State the finish line, not the work.
### Current State
What is true right now. Bold the key blocker or milestone.
*Density:* the honest present — what works, what is mocked, what is blocked. A complete project (OpsPilot) breaks this into Completed / Partially completed / Not implemented / Real vs mocked.
> [!WARNING]
> Aspirational state ("the pipeline is robust") when the truth is partial. OpsPilot explicitly labels what was **real** vs **mocked/deferred** — that honesty is the standard.
### Next Action
The single next step, mirroring the `next:` frontmatter field so dashboards surface it.
*Density:* one concrete action. Multi-step plans go under Log or Open Questions, not here.
> [!WARNING]
> A vague direction ("keep building") or a list of five next steps. One move.
### Open Questions
`- [ ]` Tasks format, never prose. Add `📅`/priority where a real date exists.
*Density:* the genuine unknowns blocking or shaping the work.
> [!WARNING]
> Prose paragraphs of musing. Use checkboxes so they are trackable.
### Log
Dated entries appended over time, newest at the bottom: `- **YYYY-MM-DD:** what changed`. Do not rewrite past entries.
*Density:* one entry per meaningful work session or milestone.
> [!WARNING]
> Editing or deleting old log lines to make the history look clean. The log is append-only by design.
## Done Conditions
- The note exists in `20_Progress/` under the right project home with a live `next:` mirrored in `## Next Action`.
- Current State is honest about what is real vs mocked vs blocked.
- It links back to its brief and the concepts/resources it depends on.
- The dashboard shows it as active with a next action.
- Open Questions are `- [ ]` tasks; the Log is append-only.
- Passes the applicable points of [[Vault Rules — Complete AI Ruleset]] Part 12 (flashcards do not apply to project notes).
## Gold Standard Example
- [[Jarvis]] — an active project note: one-line north star, control surfaces, build tracks, and a concrete `next:` mirrored in the body.
- [[Opspilot|OpsPilot]] — a complete project retrospective: Current State split into Completed / Partial / Not implemented / Real vs mocked, plus What Went Well/Wrong, lessons, and portfolio assets. Use it as the depth bar for a finished project.
