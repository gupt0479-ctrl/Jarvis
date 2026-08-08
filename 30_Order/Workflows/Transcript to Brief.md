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
  - "[[Brief Standard]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
---
# Transcript to Brief

Turn any raw transcript — a meeting, a call, a YouTube video, a written exchange — into a brief that carries the decisions and threads, not the noise. This is the general-purpose entry point the `/transcript-to-brief` skill follows; it is not scoped to mentorship meetings even though the Mentorship Program folder is its first real use.

**Use when:** a transcript has been pasted into the vault and is worth turning into something usable, whether or not you were an active participant in it.

**Moves:** transcript note (wherever it was pasted) → brief note, saved to a sibling `Briefs/`-style folder if one exists next to the transcript's folder, otherwise saved alongside the transcript.

**Template:** [[Brief Template]]

## Steps

1. Confirm the raw transcript exists as its own note, using [[For Transcript]] if it was not already saved with proper frontmatter. **Never edit the raw transcript** — treat it the same as a `05_Clippings/` capture even outside that folder.
2. Read [[Brief Standard]] before writing the brief body.
3. Read the transcript once, fully, before asking anything.
4. Ask, only where the transcript actually requires it:
	- Disambiguation for garbled passages or unclear speaker attribution that would change what gets written.
	- Which threads actually mattered enough to become a `### Key Threads` section, versus a passing mention.
	- Any external context the transcript assumes as known (a project, a person, an acronym) that is not yet in the vault.
5. Write the brief using [[Brief Template]]'s shape: source lines, What This Was, What Was Decided, Key Threads, Open Questions, Follow-Up Actions, Related Notes.
6. Check for a sibling folder next to the transcript's folder whose name suggests brief output (`Briefs/`, `Summaries/`, `Debriefs/`). Save there if one exists; otherwise save in the same folder as the transcript.
7. Wikilink every project, person, and concept the transcript actually touched. Verify each link exists before adding it to frontmatter.
8. Set `next:` on the brief — usually a pointer at the `/note-to-actions` pass that turns Follow-Up Actions into a full linked action note.

## Frontmatter to set

```yaml
type: input
status: sprout
input_kind: transcript
source_note: "[[Transcript Filename.md]]"
next: Run /note-to-actions against this brief
```

## Done when

- The raw transcript is untouched and saved with `type: input`, `status: seed` frontmatter.
- The brief exists, saved next to the transcript or in its sibling Briefs-style folder.
- Every ambiguous or garbled passage was either resolved by asking, or named in Open Questions — never silently guessed.
- The brief links to every real project, person, and concept it touches.
- The session log records the import.
