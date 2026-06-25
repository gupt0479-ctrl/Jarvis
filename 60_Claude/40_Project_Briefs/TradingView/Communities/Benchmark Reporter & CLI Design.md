---
type: community
cohesion: 0.36
members: 8
---

# Benchmark Reporter & CLI Design

**Cohesion:** 0.36 - loosely connected
**Members:** 8 nodes

## Members
- [[Benchmark Reporter Component]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[CLI Interface (init-db, ingest-prices, audit-prices, benchmark)]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Design Acceptance Criteria]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 14 No Execution Language in System Output]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 20 Benchmark Reporter Refuses Insufficient Data]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Requirement 11 Benchmark Reporter]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Requirement 9 CLI Interface]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Task 10 Benchmark Reporter]] - document - .kiro/specs/data-ingestion-foundation/tasks.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Benchmark_Reporter__CLI_Design
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_Ingestion Architecture Diagram & Components]]
- 1 edge to [[_COMMUNITY_AI-Ready Evidence Contract & Schemas]]
- 1 edge to [[_COMMUNITY_Project Guardrails (Non-Negotiable Rules)]]
- 1 edge to [[_COMMUNITY_Spec RequirementsPropertiesTasks Cross-Refs]]
- 1 edge to [[_COMMUNITY_Evidence Packet & Read API Properties]]
- 1 edge to [[_COMMUNITY_Provider Landscape & Backup Sources]]

## Top bridge nodes
- [[Task 10 Benchmark Reporter]] - degree 5, connects to 2 communities
- [[Property 14 No Execution Language in System Output]] - degree 5, connects to 1 community
- [[Benchmark Reporter Component]] - degree 3, connects to 1 community
- [[CLI Interface (init-db, ingest-prices, audit-prices, benchmark)]] - degree 3, connects to 1 community
- [[Requirement 9 CLI Interface]] - degree 3, connects to 1 community