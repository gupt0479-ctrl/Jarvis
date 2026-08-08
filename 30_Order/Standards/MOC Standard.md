---
type: evergreen
status: sprout
created: 2026-08-07
updated: 2026-08-08
tags:
  - system
  - standards
notes:
  - "[[MOC Template]]"
  - "[[HUMAN_WRITING]]"
---
# MOC Standard
==A MOC earns its name by explaining a folder in prose — a note that is only a dataview query is an index, not a map.==
This is the content standard for `type: index` notes (MOCs) anywhere in the vault. A MOC's frontmatter takes the same shape as an evergreen note (`status`, `tags`, `notes`, `next`) — `type: index` is what actually marks it as a map rather than a claim. The template gives the empty shape; this doc gives the content.
## Maps To
- Template: [[MOC Template]]
## Used By Workflow
- No linear capture→summarize→distill workflow applies — a MOC is maintained inline. Whoever creates or substantially changes a note inside a MOC-governed folder updates that folder's MOC prose in the same session, not later. The vault-curator agent's periodic sweeps are the backstop for anything missed.
## Per-Heading Standard
### Frontmatter
`type: index`, `status:` follows the evergreen maturity model (`seed | sprout | tree`), `created`/`updated`, `tags:` includes `moc`, `notes:` lists the folder's real key notes, `next:` the single next thing this cluster needs.
> [!WARNING]
> A MOC with `notes: []` left empty forever. If the folder has notes worth mapping, `notes:` should list them.
### Purpose
One to three sentences: what this folder or cluster is for and who reads it first. States the reason the cluster exists, not a definition of what a MOC is.
*Density:* short. If it takes more than three sentences, the folder may need to be split rather than the Purpose padded.
> [!WARNING]
> "This is the MOC for X" — restating the heading instead of saying why X exists.
### Map
The actual content. Short-linked prose explaining the key notes in the folder and how they relate — not a bullet list of bare links, sentences that carry information. This is what makes a MOC different from a dataview query.
*Density:* this is the bulk of the note. Every note worth surfacing gets a sentence, not just a link.
> [!WARNING]
> A bullet list of bare `[[Note]]` links with no surrounding sentence. That is an index, not a map.
### Status
Optional. A short table or a few lines of current live state, if the folder tracks ongoing work. Omit entirely for reference-only folders.
> [!WARNING]
> A stale status table nobody has touched in months. Either update it in the same session as the folder's other changes, or delete the section.
### Dataview
Live queries only, at the very bottom, never above the Map's prose. If a query would only repeat what the Map already says, do not add it.
> [!WARNING]
> A MOC that is a dataview block above the fold with the rest of the file left empty — the exact failure this Standard exists to fix.
### Links
Anything relevant that did not fit naturally into the Map's prose. Keep it short — most links belong woven into the Map, not listed separately.
## Done Conditions
- The Map section is prose with inline links, not a bare list.
- Dataview blocks sit below the prose, never above it.
- `notes:` frontmatter lists the folder's real key notes, all verified to exist.
- The MOC was updated in the same session as whatever note change in its folder triggered the update.
- No duplicate frontmatter keys; no `---` in the body; zero blank lines except after a callout.
## Gold Standard Example
- [[20_Progress/AI/Claude Code/MOC]] — a real Purpose→Map→Status→Dataview→Links shape: a purpose paragraph, prose sections explaining sub-areas with inline links, a status table, dataview blocks, and a closing Links section.
