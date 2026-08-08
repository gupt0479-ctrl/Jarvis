---
name: transcript-to-brief
description: Turns any transcript — meeting, call, YouTube video, written exchange — into a structured brief by asking targeted questions, not by summarizing blind.
---
# transcript-to-brief

**Usage:** `/transcript-to-brief` (points at the transcript in the current note, or asks which one) or `/transcript-to-brief "path/to/Transcript.md"`

General-purpose skill. It works on any transcript anywhere in the vault, not just Mentorship Program meetings — a mentorship transcript is just the first real use.

---

## Instructions

When this skill is invoked:

Before drafting, read:

- `30_Order/Standards/Brief Standard.md`
- `30_Order/Workflows/Transcript to Brief.md`
- `30_Order/Templates/Capability/Brief Template.md`
- `HUMAN_WRITING.md`

### 1. Locate the Transcript

If a path was given, use it. Otherwise ask which note holds the transcript, or use the active file if it's clearly a transcript (raw pasted conversation, `type: input`).

If the transcript is pasted as loose text with no note yet, save it first using `30_Order/Templates/Frontmatter/For Transcript.md` — `type: input`, `status: seed`, `input_kind: transcript`. Never edit the raw text once saved.

### 2. Read Fully Before Asking Anything

Read the entire transcript once, start to finish, before asking a single question. Do not ask mid-read.

### 3. Ask Only What the Transcript Actually Requires

Ask about, in this order, and only where a real gap exists — do not ask questions the transcript already answers:

1. **Disambiguation** — garbled passages or unclear/unreliable speaker attribution that would change what gets written. Quote the exact confusing fragment when asking.
2. **What mattered most** — which threads deserve a full `### Key Threads` subsection versus a passing mention. Propose your own read first ("It looks like X and Y were the real substance, Z was a tangent — is that right?") rather than asking open-ended.
3. **External context** — anything the conversation assumes as known (a project, a person, an acronym, a prior decision) that isn't yet in the vault. Search the vault first; only ask if it's genuinely missing.

Ask one question at a time if the answers might change each other. Batch unrelated questions.

### 4. Search Before Linking

For every project, person, or concept the transcript touches, search the vault (MCP search or Grep) before adding a wikilink. Only wikilink notes confirmed to exist.

### 5. Write the Brief

Follow `Brief Template.md`'s exact shape and `Brief Standard.md`'s per-heading content rules:

- Source lines (`**Source:**`, `**Transcript:**`, `**Date of conversation:**`)
- `## What This Was`
- `## What Was Decided` — only real resolutions, bulleted
- `## Key Threads` — `###` per thread that actually mattered
- `## Open Questions` — every unresolved or disambiguation-needed item, `- [ ]` format
- `## Follow-Up Actions` — high-level only, `- [ ]` format
- `## Related Notes` — verified wikilinks

### 6. Choose the Save Location

Check for a sibling folder next to the transcript's folder whose name suggests brief output (`Briefs/`, `Summaries/`, `Debriefs/`). Save there if one exists. Otherwise save in the same folder as the transcript.

### 7. Set Frontmatter and Close Out

Set `type: input`, `status: sprout`, `input_kind: transcript`, `source_note:` pointing at the transcript (filename with extension, no path), `related_progress:`, and `next:` pointing at running `/note-to-actions` against this brief.

Append a one-line entry to `60_Claude/07_AI_Information/Session Logs/log.md`.

Tell the user: where the brief was saved, what Open Questions remain, and that `/note-to-actions` is the next step if the brief has real follow-up work.

---

## Style Guidelines

- The brief is not a second transcript. If Key Threads is as long as the source, something wasn't compressed.
- Never invent a resolution for a thread the transcript left open — that goes in Open Questions.
- Follow [[HUMAN_WRITING]]: no filler, no generic framing, concrete over polished.
