# ingesting-clipping — Examples

Gold-standard frontmatter skeletons, one per source type. These show what a *good* finished note's header looks like — not how to produce it (that's SKILL.md + reference.md). `source_note` is the filename with extension, no path. `track` sets the flashcard deck (`track: trading` → `#cards/trading`). Verify every `notes:` wikilink exists before saving.

---

## PDF

```yaml
---
type: input
status: sprout
created: 2026-06-20
updated: 2026-06-20
tags:
  - summary
notes:
  - "[[Confirmed Existing Note]]"
source_url: 60_Claude/05_Clippings/PDFs/Quant Foundations.pdf
source_note: "[[Quant Foundations.pdf]]"
input_kind: pdf
track: trading
---
```

## Image

```yaml
---
type: input
status: sprout
created: 2026-06-20
updated: 2026-06-20
tags:
  - summary
notes:
  - "[[Confirmed Existing Note]]"
source_url: 60_Claude/05_Clippings/PDFs/Extracurriculars List.png
source_note: "[[Extracurriculars List.png]]"
input_kind: image
track: career
---
```

## Web URL

```yaml
---
type: input
status: sprout
created: 2026-06-20
updated: 2026-06-20
tags:
  - summary
notes:
  - "[[Confirmed Existing Note]]"
source_url: https://example.com/the-article
source_note: "[[the-article]]"
input_kind: web
track: ai
---
```

## GitHub repo

```yaml
---
type: input
status: sprout
created: 2026-06-20
updated: 2026-06-20
tags:
  - summary
  - github
notes:
  - "[[Confirmed Existing Note]]"
source_url: https://github.com/owner/repo
source_note: "[[Repo Landing Page Clip.md]]"
input_kind: github
track: ai
---
```
`source_note` points at the web clip that discovered the repo (if one exists) — the repo itself has no single filename to wikilink, so `source_url` carries the canonical reference. Omit `source_note` if the repo was found directly via `gh api`/search with no clip.

## Markdown clip

```yaml
---
type: input
status: sprout
created: 2026-06-20
updated: 2026-06-20
tags:
  - summary
notes:
  - "[[Confirmed Existing Note]]"
source_url: 60_Claude/05_Clippings/Web/Best MCPs.md
source_note: "[[Best MCPs.md]]"
input_kind: web
track: systems
---
```

## Video transcript

```yaml
---
type: input
status: sprout
created: 2026-06-20
updated: 2026-06-20
tags:
  - summary
notes:
  - "[[Confirmed Existing Note]]"
source_url: 60_Claude/05_Clippings/Videos/Talk Transcript.md
source_note: "[[Talk Transcript.md]]"
input_kind: video
track: general
---
```
