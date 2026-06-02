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
# Promotion

Move a matured concept out of the AI workshop into the durable layers. This is the step that keeps `60_Claude` a workshop and not a second, permanent knowledge base.

**Use when:** a `20_Distilled_Notes` concept is `status: tree`, trusted, and you have reused it at least once.

**Moves:** `60_Claude/20_Distilled_Notes/` → `10_Areas/` (identity-level truth) **or** `40_Resources/` (lookup reference)

## Which target

- **`10_Areas/`** if the note is canonical truth about a domain — something you would state about your Career, Trading thesis, Life principles, or studies. Patch it into the domain hub by heading; do not scatter new top-level files.
- **`40_Resources/`** if the note is reference you look up to do the work — a guide, a concept explainer, a cheat sheet, a curated link set. Add it as a single backlinked entry.

## The 40_Resources guardrail

`40_Resources` is a curated hub, not a dumping ground. Promote **one note at a time, with a backlink to the domain it serves**, and only when it is genuinely reference. Never flush a batch of AI distillations into it. When in doubt, leave it in `20_Distilled_Notes` and flag it for review rather than promoting on your own judgment.

## Steps

1. Confirm the note is `status: tree` and actually reused (linked from a project, a brief, or another concept).
2. Pick the target by the test above.
3. Move or merge: for `10_Areas`, patch the domain hub by heading; for `40_Resources`, place the note and add a backlink to its `10_Areas` domain.
4. Leave a pointer behind. The `20_Distilled_Notes` origin can keep the provenance/source links; the durable copy is now canonical.
5. Update links so nothing points at a stale location.

## Done when

- The durable note lives in the right layer and backlinks to its domain.
- No bulk dump landed in `40_Resources`.
- Links resolve; the origin points forward to the promoted note.
- The session log records the promotion.
