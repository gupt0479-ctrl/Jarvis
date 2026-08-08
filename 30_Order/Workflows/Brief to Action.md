---
type: evergreen
status: tree
created: 2026-08-08
updated: 2026-08-08
tags:
  - system
  - workflow
notes:
  - "[[00_Workflows Index]]"
  - "[[Action Standard]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
---
# Brief to Action

Turn any note with real content into a linked map of what still needs doing. This is the general-purpose entry point the `/note-to-actions` skill follows — it works against a meeting brief, but also against any note dense enough to need its Follow-Up Actions broken into concrete, linked steps.

**Use when:** a brief or note exists, its topics are understood, and what's missing is the concrete next step for each one.

**Moves:** source note (a brief, or any note with interlinks) → action note, saved to a sibling `Action/`-style folder if one exists next to the source's folder, otherwise saved alongside the source.

**Template:** [[Action Template]]

## Steps

1. Read the source note fully — its Key Threads (if it's a brief) or its own section structure (if it's a general note) — before asking anything.
2. Read [[Action Standard]] before writing the action note body.
3. For each thread or topic in the source, ask what the concrete next step actually is. Do not infer a next step the source doesn't support — ask.
4. For each entity a step needs to reference (a person, a concept, a project) that has no existing vault note, ask whether to link it as-is, skip the link, or note it as a gap — never silently create a stub note.
5. Write the action note using [[Action Template]]'s shape: one `##` per thread, matching the source's thread order, each holding link-dense declarative statements — no checkboxes, no prose paragraphs.
6. Name anything the Q&A pass could not resolve under `## Open Threads` instead of dropping it.
7. Check for a sibling folder next to the source's folder whose name suggests action output (`Action/`, `Next Steps/`). Save there if one exists; otherwise save in the same folder as the source.
8. Link the action note back to its source in `source_note:`, and link the source's Follow-Up Actions section forward to this note.

## Frontmatter to set

```yaml
type: action
status: active
source_note: "[[Source Brief or Note]]"
next: <the single next statement to close out>
```

## Done when

- Every thread in the source is represented in the action note, either as statements or as a named open thread.
- Nearly every sentence carries a wikilink; any that don't are the rare exception.
- No checkboxes and no prose paragraphs snuck into the action note.
- Missing link targets were asked about, not auto-created as stubs.
- The session log records the pass.
