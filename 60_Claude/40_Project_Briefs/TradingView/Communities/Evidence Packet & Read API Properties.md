---
type: community
cohesion: 0.43
members: 8
---

# Evidence Packet & Read API Properties

**Cohesion:** 0.43 - moderately connected
**Members:** 8 nodes

## Members
- [[Property 15 Evidence Packet Completeness and Confidence Cap]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 16 Evidence Packet Serialization Round-Trip]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 7 Read API Ordering Guarantee]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 8 Read API Usability Filter]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 9 Read API Source and Adjustment Filtering]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Requirement 10 Read API]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Requirement 12 Evidence Packet Contract]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Task 9 Read API and Evidence Packets]] - document - .kiro/specs/data-ingestion-foundation/tasks.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Evidence_Packet__Read_API_Properties
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_AI-Ready Evidence Contract & Schemas]]
- 1 edge to [[_COMMUNITY_Ingestion Data Flow & Module Map]]
- 1 edge to [[_COMMUNITY_NormalizerCalendar Properties & csv_fixture Entry]]
- 1 edge to [[_COMMUNITY_Provider Protocol & FabricationQuality Properties]]
- 1 edge to [[_COMMUNITY_Benchmark Reporter & CLI Design]]

## Top bridge nodes
- [[Requirement 10 Read API]] - degree 7, connects to 3 communities
- [[Task 9 Read API and Evidence Packets]] - degree 9, connects to 2 communities
- [[Requirement 12 Evidence Packet Contract]] - degree 4, connects to 1 community