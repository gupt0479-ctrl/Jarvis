---
type: evergreen
status: tree
created: 2026-05-31
updated: 2026-05-31
tags:
  - system
  - workflow
  - enrichment
notes:
  - "[[00_Workflows Index]]"
  - "[[40_Resources/Obsidian/Jarvis Enrichment Engine]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
---
# Enrichment

Strengthen an existing note without flattening it. The three-month target is 100+ enriched notes, where opening a major note feels like opening a private textbook page: clear, concrete, linked, testable, source-grounded. Enrichment adds depth; it does not rewrite the human voice underneath.

**Use when:** a note has thin content, no examples, no source anchors, or no drills — and it matters enough to deepen.

**Applies in place:** wherever the note already lives (`10_Areas/`, `20_Progress/`, `40_Resources/`, `60_Claude/20_Distilled_Notes/`). Enrichment does not move a note.

**Template:** `30_Order/Templates/Capability/Jarvis Enrichment Template.md`. Full method: [[40_Resources/Obsidian/Jarvis Enrichment Engine]].

## The rule that protects your notes

Preserve the existing note. Append under a `## Jarvis Enrichment` or `## Addendum — Jarvis Enrichment YYYY-MM-DD` heading. Leave the original structure and wording visible. Never silently overwrite a human note with generic AI prose.

## Levels

- **Light** — definition, links, a few questions.
- **Standard** — definition, mechanism, example, contrast, misconceptions, source anchors, drills.
- **Deep** — formal model, implementation, worked examples, synthesis, evidence, an output artifact.

## Steps

1. Profile the note: what type and track is it, what headings are present, what is missing (examples? contrasts? source anchors? drills?).
2. Pick a level by how much the note matters and how thin it is.
3. Retrieve related notes and sources to pull from — enrichment is grounded, not invented.
4. Draft the enrichment, then run a critic pass against [[HUMAN_WRITING]]: mechanism over vibes, real examples, honest uncertainty.
5. Append it under the enrichment heading. Add drills (`#cards`) only for concepts already understood.
6. Update metadata so dashboards can track it.

## Frontmatter to update

```yaml
enrichment_status: enriched   # was candidate / in-progress
enrichment_level: standard    # light | standard | deep
source_status: vault-grounded # or mixed
updated: YYYY-MM-DD
```

## Done when

- The original content is intact; new depth is appended, not overwritten.
- The enrichment has mechanism, a concrete example, and source anchors.
- `enrichment_status` and `enrichment_level` are set.
- The session log records the note and level.
