---
type: community
cohesion: 0.20
members: 12
---

# Provider Protocol & Fabrication/Quality Properties

**Cohesion:** 0.20 - loosely connected
**Members:** 12 nodes

## Members
- [[Error Handling Table]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[PriceProvider Protocol]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 11 No Data Fabrication on Empty Provider Response]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 17 Rejected Records Counted in Quality Report]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 5 Quality Status Classification Correctness]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[ProviderCapabilities Model]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[ProviderFetchResult Model]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Requirement 13 Error Handling]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Requirement 2 Price Provider Interface]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Requirement 7 Data Quality Auditing]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Task 7 Data Quality Auditor]] - document - .kiro/specs/data-ingestion-foundation/tasks.md
- [[Task 8 Checkpoint - Ensure All Tests Pass]] - document - .kiro/specs/data-ingestion-foundation/tasks.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Provider_Protocol__Fabrication/Quality_Properties
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Ingestion Architecture Diagram & Components]]
- 2 edges to [[_COMMUNITY_NormalizerCalendar Properties & csv_fixture Entry]]
- 1 edge to [[_COMMUNITY_Ingestion Data Flow & Module Map]]
- 1 edge to [[_COMMUNITY_Project Guardrails (Non-Negotiable Rules)]]
- 1 edge to [[_COMMUNITY_Spec RequirementsPropertiesTasks Cross-Refs]]
- 1 edge to [[_COMMUNITY_Provider Landscape & Backup Sources]]
- 1 edge to [[_COMMUNITY_Evidence Packet & Read API Properties]]

## Top bridge nodes
- [[Requirement 7 Data Quality Auditing]] - degree 5, connects to 2 communities
- [[Property 11 No Data Fabrication on Empty Provider Response]] - degree 4, connects to 2 communities
- [[Task 7 Data Quality Auditor]] - degree 5, connects to 1 community
- [[Requirement 2 Price Provider Interface]] - degree 4, connects to 1 community
- [[Property 17 Rejected Records Counted in Quality Report]] - degree 3, connects to 1 community