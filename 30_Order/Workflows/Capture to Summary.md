---
type: evergreen
status: tree
created: 2026-05-31
updated: 2026-05-31
tags:
  - system
  - workflow
notes:
  - "[[00_Workflows Index]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
---
# Capture to Summary

Turn a raw source into a source-grounded summary you can actually use. This is the first compression step: raw stays raw, the summary carries the claims.

**Use when:** you have a clipping, web page, video, PDF, or import worth keeping but too noisy to act on.

**Moves:** `60_Claude/05_Clippings/` (raw, untouched) → `60_Claude/10_Source_Summaries/`

**Template:** `30_Order/Templates/Capability/Clipping Distill Template.md`

## Steps

1. Confirm the raw source is in `05_Clippings/` (under `Web/`, `Videos/`, or `AI Conversations/`). If it is pasted text with no home, drop it there first. **Never edit the raw file.**
2. Create the summary in `10_Source_Summaries/` (use the matching `Web Ingestion/`, `Video Ingestion/`, or `Github Ingestion/` subfolder). Read `30_Order/Standards/Source Summary Standard.md` before writing.
3. Extract, in this order: source pointer (URL/path), key claims, what is actually useful to Jarvis, what to ignore, and any entities or concepts worth their own note later.
4. Label each claim's strength. If the source is weak, partial, or one person's opinion, say so.
5. Wikilink the raw clipping and any existing concept or project notes the source touches.
6. Add a one-line promotion recommendation: does any claim deserve a distilled note, or is this reference-only?

## Frontmatter to set

```yaml
type: input
status: sprout
source_url: <link or path>
source_status: externally-sourced   # or mixed / uncertain
track: <ai|systems|algorithms|career|trading>   # if it fits one
```

## Done when

- The summary cites its source and separates claims from your inference.
- The raw clipping is unchanged.
- Useful claims are flagged for promotion; noise is named as noise.
- One line is appended to the session log.
