---
type: evergreen
status: sprout
created: 2026-06-01
updated: 2026-06-01
tags:
  - system
  - standards
notes:
  - "[[30_Order/Templates/Metadata/For Evergreen|For Evergreen]]"
  - "[[Summary to Distilled]]"
  - "[[Vault Rules — Complete AI Ruleset]]"
  - "[[HUMAN_WRITING]]"
---
# Evergreen Standard
==An evergreen note distills a reusable mechanism that outlives any single source — it exists because a concept recurred across sources or contexts, not because one source was worth keeping.==
This is the content standard for `evergreen` notes in `60_Claude/20_Distilled_Notes/` (including `Synthesis/` cross-concept comparisons). The difference from a source summary: a summary is fixed to one source and never extended; an evergreen is owned knowledge that grows as new evidence and contrasts arrive. The difference from a concept note: a concept note is course-facing and exam-scoped; an evergreen is a transferable mechanism that connects work across the vault.
## Maps To
- Template: [[30_Order/Templates/Metadata/For Evergreen|For Evergreen]]
## Used By Workflow
- [[Summary to Distilled]] — the create-the-note step reads this Standard first. Search `20_Distilled_Notes/` for an existing note on the concept and extend it before creating a sibling.
## Per-Heading Standard
### Frontmatter
`type: evergreen`, `status: sprout` (raise to `tree` only after the concept is reused and trusted), `tags: [evergreen]`, `notes:` linking the source summaries and concept neighbors it came from, `next:` if a concrete next move exists. Synthesis notes add `tracks:` for the domains they bridge.
> [!WARNING]
> Promoting straight to `status: tree` on first write, or leaving `notes:` empty so the note is invisible to backlinks and the graph.
### Core Claim
The single most important thing the note establishes, in one sentence. This is the `==highlight==` anchor.
*Density:* one sentence wrapped in `==...==`.
> [!WARNING]
> A topic label ("This note is about observability") instead of a claim. The synthesis note's claim: both observability and evaluation answer "why did this system produce this output," with identical reasoning under different vocabulary.
### Mechanism
How it works. Bold named concepts on first use; use `$...$` for notation and explain it. This is where the reusable understanding lives.
*Density:* the bulk of the note — enough that a reader learns the mechanism without opening the sources. Use a table when mapping two domains (the synthesis note maps backend concept → AI/ML analog row by row).
> [!WARNING]
> Restating what one source said rather than explaining the mechanism in your own words. BOOM § subsystems explains *why* Redis sits alongside Kafka (fast internal handoff vs public stream), not just that both exist.
### Why This Matters Here
The connection to active work in Jarvis — a named project, course, or decision. No generic importance; name the use.
*Density:* two to four sentences naming the real application.
> [!WARNING]
> "This is an important concept." The synthesis note names the transfer drill: if you built observability for BOOM, you already know how to build evaluation for an ML pipeline.
### Failure Modes
Where the mechanism breaks, or the nearby idea it is confused with. Anchor with a `> [!WARNING]` where a real trap exists.
*Density:* the genuine breakages and confusions.
> [!WARNING]
> Skipping this because the note "feels finished." The synthesis note locates the hard cases at boundaries (API/auth/Kafka/workers in BOOM; retrieval/prompt/inference/parsing in AI).
### Evidence
Verified wikilinks to the sources and vault notes that support the note. Grep each before writing.
*Density:* link the source summaries it distills and the projects that prove it.
> [!WARNING]
> Citing sources that do not exist as vault notes, or no evidence at all on a `tree`-bound note.
### Related
Wikilinks to nearby concepts. Link real relationships, not every keyword.
*Density:* the genuine neighbors — three to seven.
> [!WARNING]
> Reflexively linking every term mentioned. BOOM § Related links its actual sibling notes (Alerts and Data Flow, Observability and Tracing), not every Rust keyword.
## Done Conditions
- The note teaches the mechanism without the reader opening the sources.
- One highlight (Core Claim); a real mechanism, a named use, a failure mode, and a contrast where one exists.
- `Evidence` and `Related` link verified vault notes; gaps are stated, not hidden.
- `status: tree` only after the concept has been reused.
- Passes all 16 points of [[Vault Rules — Complete AI Ruleset]] Part 12.
## Gold Standard Example
- [[Observability in Backend vs Evaluation in AI]] — a synthesis evergreen: one parallel claim, a domain-mapping table for the mechanism, a named transfer drill, and boundary-located failure modes.
- [[BOOM]] — a mechanism-rich evergreen: every subsystem explained by *why* it exists, a Mermaid system diagram, and a dense Related section. Use it as the depth bar for the Mechanism section.
