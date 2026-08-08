---
type: evergreen
status: sprout
created: 2026-08-08
updated: 2026-08-08
tags:
  - system
  - standards
notes:
  - "[[Brief Template]]"
  - "[[Transcript to Brief]]"
  - "[[HUMAN_WRITING]]"
---
# Brief Standard
==A brief compresses a transcript into what was decided and what actually mattered — it is not a second transcript, and it is not a task list.==
This is the content standard for `type: input` notes produced from any transcript — meeting, call, YouTube video, or written exchange — regardless of which folder they live in. The template gives the empty shape; this doc gives the content, and [[Transcript to Brief]] gives the steps that produce it.
## Maps To
- Template: [[Brief Template]]
## Used By Workflow
- [[Transcript to Brief]] — the `/transcript-to-brief` skill reads this Standard before writing the brief body.
## Per-Heading Standard
### Frontmatter
`type: input`, `status: sprout`, `input_kind: transcript`, `created`/`updated`, `tags:` includes `brief`, `source_note:` the raw transcript this brief was built from (filename with extension, no folder path), `related_progress:` the projects or notes this transcript touches, `next:` the single next thing this brief needs — usually the `/note-to-actions` pass that has not run yet.
> [!WARNING]
> `source_note` pointing at a transcript that does not exist, or written as a full path instead of a bare filename.
### Source Lines
`**Source:**`, `**Transcript:**`, `**Date of conversation:**` immediately after the title, no blank line after the frontmatter close.
*Density:* three lines, metadata only.
### What This Was
One to three sentences: what kind of transcript this is and who was involved. Enough that the brief is interpretable without opening the transcript.
> [!WARNING]
> Restating the title, or a vague "this was a conversation about various topics."
### What Was Decided
Every concrete decision or resolution, one bullet each, bolding a short label before the sentence. If a thread never actually resolved, it does not belong here — it belongs in Open Questions.
*Density:* one bullet per real decision. Zero bullets is a valid, honest result if nothing was decided.
> [!WARNING]
> Inventing a resolution for a thread the transcript left open. Force-resolving ambiguity is worse than naming it as unresolved.
### Key Threads
`###` subheadings, one per substantive topic, ordered by what matters most, not the order it was said. Each thread compresses what was discussed, bolds key names on first mention, and links to the vault notes it touches.
*Density:* the bulk of the note. Skip threads that were only mentioned in passing — that is what the "what mattered most" question during `/transcript-to-brief` is for.
> [!WARNING]
> A thread section for every topic touched, including 10-second tangents. That produces a second transcript, not a brief.
### Open Questions
`- [ ]` Tasks format. Unresolved threads, passages too garbled or ambiguously attributed to confidently write up, and anything the transcript assumed as known context that is not yet in the vault.
*Density:* the genuine gaps — typically two to six.
> [!WARNING]
> Guessing at a garbled or ambiguously-attributed passage instead of flagging it here.
### Follow-Up Actions
`- [ ]` format, short. The high-level next steps only — the full link-dense breakdown belongs in the linked action note that `/note-to-actions` produces from this brief, not here.
*Density:* enough to point at what needs following up, not a duplicate of the action note.
> [!WARNING]
> Writing the full action breakdown here instead of in its own note — see [[Action Standard]].
### Related Notes
Verified wikilinks only — Grep before adding.
*Density:* link every project, person, and concept the transcript actually touched.
## Done Conditions
- Reopening the raw transcript would not surface a decision or thread this brief missed.
- Key Threads covers what mattered, not everything that was said.
- Open Questions names every garbled or ambiguous passage instead of guessing.
- No duplicate frontmatter keys; every `notes:`/`related_progress:` link verified; no `---` in the body; zero blank lines except after a callout.
## Gold Standard Example
- [[Project Briefings - 2026-07-13]] — a real post-meeting brief: an honest framing line about unreliable speaker labels, numbered substantive threads instead of a blow-by-blow transcript recap, and clear treatment of what was and was not actually resolved.
