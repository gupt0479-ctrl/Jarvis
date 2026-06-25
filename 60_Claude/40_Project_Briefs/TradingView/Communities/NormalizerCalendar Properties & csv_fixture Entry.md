---
type: community
cohesion: 0.27
members: 10
---

# Normalizer/Calendar Properties & csv_fixture Entry

**Cohesion:** 0.27 - loosely connected
**Members:** 10 nodes

## Members
- [[Design Testing Strategy]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 18 Normalizer Price Adjustment Mapping]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 2 OHLCV Round-Trip Integrity]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 6 Market Calendar Excludes Non-Trading Days]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Requirement 15 Testing Without Network Access]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Requirement 4 Normalization]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Requirement 6 Market Calendar]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[Task 5 CSV Fixture Provider and Raw Payload Writer]] - document - .kiro/specs/data-ingestion-foundation/tasks.md
- [[Task 6 Normalizer and Market Calendar]] - document - .kiro/specs/data-ingestion-foundation/tasks.md
- [[csv_fixture provider entry]] - document - config/providers.toml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Normalizer/Calendar_Properties__csv_fixture_Entry
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Ingestion Architecture Diagram & Components]]
- 2 edges to [[_COMMUNITY_Ingestion Data Flow & Module Map]]
- 2 edges to [[_COMMUNITY_Spec RequirementsPropertiesTasks Cross-Refs]]
- 2 edges to [[_COMMUNITY_Provider Protocol & FabricationQuality Properties]]
- 1 edge to [[_COMMUNITY_Evidence Packet & Read API Properties]]
- 1 edge to [[_COMMUNITY_Project Guardrails (Non-Negotiable Rules)]]
- 1 edge to [[_COMMUNITY_Provider Landscape & Backup Sources]]

## Top bridge nodes
- [[Task 5 CSV Fixture Provider and Raw Payload Writer]] - degree 7, connects to 4 communities
- [[Requirement 4 Normalization]] - degree 5, connects to 2 communities
- [[Requirement 6 Market Calendar]] - degree 4, connects to 2 communities
- [[Property 2 OHLCV Round-Trip Integrity]] - degree 3, connects to 2 communities
- [[Task 6 Normalizer and Market Calendar]] - degree 6, connects to 1 community