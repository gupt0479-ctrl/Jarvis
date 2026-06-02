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
# Summary to Distilled

Turn one or more source summaries into a reusable concept note: knowledge *you* understand, not a record of what a source said. This is where understanding is built.

**Use when:** a concept shows up across summaries, or one summary contains an idea worth owning permanently.

**Moves:** `60_Claude/10_Source_Summaries/` → `60_Claude/20_Distilled_Notes/` (cross-concept comparisons go in `20_Distilled_Notes/Synthesis/`)

**Template:** `30_Order/Templates/Capability/Synthesis Template.md` (or `Deep Dive Template.md` for a single deep concept)

## Steps

1. Search `20_Distilled_Notes/` for an existing note on the concept. If one exists, extend it instead of creating a sibling.
2. Read `30_Order/Standards/Evergreen Standard.md` before writing. Write the concept in your own words. Hit at least: a one-line definition, why it matters, the mechanism (how it works), one concrete example from your vault (BOOM, a course, a project), and one contrast with a nearby idea people confuse it with.
3. Record the failure mode or misconception — the thing that is easy to get wrong.
4. Cite the source summaries it came from; wikilink them and any related concepts.
5. State what is still unclear. A distilled note is allowed to be honest about its gaps.

## Frontmatter to set

```yaml
type: evergreen
status: sprout        # sprout until reused and trusted, then tree
track: <ai|systems|algorithms|career|trading>
source_status: vault-grounded   # or mixed
enrichment_status: in-progress
```

## Done when

- The note teaches the concept without the reader opening the sources.
- It has a definition, a mechanism, a real example, and a contrast.
- Gaps are stated, not hidden.
- It links to its source summaries and its concept neighbors.
- When the concept is stable and you have reused it, raise `status` to `tree` and consider [[Promotion]].
