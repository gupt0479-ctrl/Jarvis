---
type: evergreen
status: tree
created: 2025-07-18
updated: 2025-07-18
tags:
  - index
  - capability
  - synthesis
---
# Synthesis Index
This folder holds synthesis notes — notes that bridge concepts across two or more tracks to surface non-obvious connections, transfer patterns, or combined insights.
## Cross-Track Requirement
A valid synthesis note must:
- Link at least two concepts in the `concepts` frontmatter field
- Reference at least two distinct tracks in the `tracks` frontmatter field
If a note links concepts from only one track, it's a regular connection, not a synthesis. Synthesis requires cross-domain transfer.
## What Good Synthesis Looks Like
Good synthesis reveals something you couldn't see from either concept alone:
- Rust ownership vs OCaml immutability — both enforce correctness at compile time, but through different mechanisms. Comparing them clarifies what "compile-time safety" actually means.
- Kafka pipelines vs agent tool orchestration — both handle fan-out and backpressure. The structural parallel helps reason about agent reliability using distributed systems intuition.
- Observability in backend systems vs evaluation in AI systems — both answer "is this thing working?" but with different signal types. The comparison sharpens what "monitoring" means in each domain.
Bad synthesis is just noting that two things are vaguely similar without explaining what the comparison reveals.
## Dashboards
- [[Capability Dashboard]] — surfaces synthesis notes by track
- Field OS boards — each track's Field OS shows synthesis notes touching that track
