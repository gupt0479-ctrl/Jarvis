---
description: Promote a mature idea from inbox or daily notes into a permanent evergreen note
---

Identify a note ready to graduate from raw/draft to a permanent evergreen note and execute the promotion.

## Steps

1. If no note is specified, suggest the top 3 candidates from `00_Daily/` and `00-Inbox/` based on:
   - Appears in multiple notes (high cross-reference count)
   - Has been tagged `#idea` or `#develop` more than once
   - Has an explicit `status: developing` frontmatter field
2. For the chosen note, assess readiness:
   - Does it have one clear core claim?
   - Is it self-contained (understandable without context)?
   - Does it link to at least 2 other permanent notes?
3. If not ready, list what's needed and stop.
4. If ready, apply the graduation process:
   - Choose the best permanent home: `30_Knowledge/` (concept), `10_Areas/` (area insight), `20_Projects/` (project learning).
   - Apply the appropriate template from `50_Claude/Templates/`.
   - Write a clean, polished version preserving the original voice.
   - Add frontmatter: `type: evergreen`, `status: mature`, `graduated: {{date}}`.
   - Add `[[wikilinks]]` to at least 2 related notes.
   - Update the source note with a link to the new evergreen: `→ Graduated to [[evergreen-slug]]`.
5. Confirm the new note path and any backlinks added.
