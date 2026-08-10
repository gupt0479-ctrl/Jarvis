---
name: note-to-actions
description: Turns any note — a brief, or any note with real content — into a link-dense map of concrete next steps, by asking what each thread actually requires rather than inferring it.
---
# note-to-actions

**Usage:** `/note-to-actions` (points at the note in the current file, or asks which one) or `/note-to-actions "path/to/Note.md"`

General-purpose skill. It is not a second brief — it does not re-summarize. It reads a note that already exists, understands what each thread in it actually requires, and asks until every thread either becomes a linked statement or is named as an open thread.

---

## Instructions

When this skill is invoked:

Before drafting, read:

- `30_Order/Standards/Action Standard.md`
- `30_Order/Workflows/Brief to Action.md`
- `30_Order/Templates/Capability/Action Template.md`
- `HUMAN_WRITING.md`

### 1. Locate the Source Note

If a path was given, use it. Otherwise ask which note to process, or use the active file. The source is usually a brief from `/transcript-to-brief`, but can be any note with enough real content and existing interlinks to extract steps from.

### 2. Understand the Source Fully First

Read the whole source note, including everything it already links to (`related_progress:`, inline wikilinks) that's needed to understand each thread. Do not start writing statements from a partial read.

### 3. Ask What Each Thread Actually Requires

For each thread or topic in the source (a brief's `## Key Threads`, or a general note's own section structure), ask what the concrete next step actually is. This is the core of the skill — do not infer a next step the source doesn't support.

Ask concretely, one thread at a time if the threads are independent: "For [thread], what's the actual next move — and on what, by when, with whom?" Propose a candidate statement if one is obvious from context, but confirm it rather than assuming.

### 4. Ask Before Linking to Missing Notes

If a step needs to reference a person, concept, or project with no existing vault note (search first — Grep or MCP search), ask the user: link it anyway pointing at a note to create, skip the link, or note the gap. Never silently create a stub note.

### 5. Write the Action Note

Follow `Action Template.md`'s exact shape and `Action Standard.md`'s per-heading content rules:

- Opening line naming the source and the format rule.
- One `##` per thread, matching the source's thread order exactly.
- Under each: plain declarative statements, one per required step, no checkboxes, no prose paragraphs. Every statement carries at least one wikilink.
- `## Open Threads` for anything the Q&A pass could not resolve — name it, don't drop it.

### 6. Choose the Save Location

Check for a sibling folder next to the source's folder whose name suggests action output (`Action/`, `Next Steps/`). Save there if one exists. Otherwise save in the same folder as the source.

### 7. Set Frontmatter and Close Out

Set `type: action`, `status: active`, `source_note:` pointing at the source (filename with extension, no path), `related_progress:`, and `next:` — the single statement to close out first.

Link the action note back into the source note's `## Follow-Up Actions` (or equivalent) section if the source is a brief.

Append a one-line entry to `60_Claude/07_AI_Information/Session Logs/log.md`.

---

## Style Guidelines

- Statements only. A sentence with no link has not actually been mapped back to anything — rewrite it or ask a question until it can carry one.
- Terse. One sentence per step. Explanation belongs in the source note, not here.
- Nothing silently dropped — every thread either resolves into statements or is named under Open Threads.
- Follow [[HUMAN_WRITING]]: no filler, no generic framing, concrete over polished.
