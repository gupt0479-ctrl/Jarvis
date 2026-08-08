---
type: evergreen
status: sprout
created: 2026-08-08
updated: 2026-08-08
tags:
  - system
  - standards
notes:
  - "[[Action Template]]"
  - "[[Brief to Action]]"
  - "[[HUMAN_WRITING]]"
---
# Action Standard
==An action note is a linked map of what still needs doing, not a second brief and not a checklist — every statement earns its place by carrying a link.==
This is the content standard for `type: action` notes produced from any brief or note with real interlinks, regardless of folder. The template gives the empty shape; this doc gives the content, and [[Brief to Action]] gives the steps that produce it.
## Maps To
- Template: [[Action Template]]
## Used By Workflow
- [[Brief to Action]] — the `/note-to-actions` skill reads this Standard before writing the action note body.
## Per-Heading Standard
### Frontmatter
`type: action`, `status: active`, `created`/`updated`, `tags:` includes `action`, `source_note:` the brief or note this was derived from, `related_progress:` the projects it touches, `next:` the single next statement to close out.
> [!WARNING]
> `type: project` used instead — action notes are their own type precisely because they are not prose progress notes.
### Opening Line
One line naming the source note this was derived from and the format rule: statements only, no checkboxes, no prose paragraphs, and a statement with no link was not actually mapped back to its source.
### Thread Sections
One `##` heading per thread, matching the source brief's Key Threads in the same order. Under each, one short declarative statement per required step. Every statement carries at least one wikilink — to the project, concept, person, or date it concerns.
*Density:* terse. A statement is one sentence, not a paragraph. If a step needs a paragraph to explain, the explanation belongs in the source brief, not here.
> [!WARNING]
> A statement with zero links — "Follow up on the resume review" instead of "Follow up on the [[Portfolio]] resume review Ahnaf offered in [[Mentor Meeting Playbook]]." A sentence with no link has not actually been mapped back to anything.
### Open Threads
Statements naming what the Q&A pass could not resolve into a concrete next step — named as open, not silently dropped and not guessed at.
> [!WARNING]
> Silently omitting a thread from the source brief instead of naming it here as unresolved.
## Done Conditions
- Nearly every sentence carries at least one wikilink; a sentence with none is the exception, not the norm.
- No checkboxes, no prose paragraphs — statements only.
- Every thread from the source brief is represented, either as resolved statements or as a named open thread — nothing silently dropped.
- Missing link targets were raised as a question during the skill run, not auto-created as stub notes.
- No duplicate frontmatter keys; no `---` in the body; zero blank lines except after a callout.
## Gold Standard Example
- No vault example exists yet — `20_Progress/Mentorship Program/Meetings/Action/` will hold the first real instance once a fall meeting brief runs through `/note-to-actions`.
