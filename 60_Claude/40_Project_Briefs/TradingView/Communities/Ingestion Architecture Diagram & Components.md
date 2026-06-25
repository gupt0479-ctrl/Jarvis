---
type: community
cohesion: 0.33
members: 10
---

# Ingestion Architecture Diagram & Components

**Cohesion:** 0.33 - loosely connected
**Members:** 10 nodes

## Members
- [[Data Quality Auditor Component]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Ingestion Architecture Diagram (mermaid)]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Market Calendar Component]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Normalizer Component]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Property 3 Raw Payload Hash Consistency]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Provider Fetchers Component]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Provider Registry Component]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Raw Payload Writer Component]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Requirement 3 Raw Payload Preservation]] - document - .kiro/specs/data-ingestion-foundation/requirements.md
- [[raw_market_payloads Table Schema]] - document - .kiro/specs/data-ingestion-foundation/design.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Ingestion_Architecture_Diagram__Components
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_NormalizerCalendar Properties & csv_fixture Entry]]
- 2 edges to [[_COMMUNITY_Provider Protocol & FabricationQuality Properties]]
- 2 edges to [[_COMMUNITY_Spec RequirementsPropertiesTasks Cross-Refs]]
- 2 edges to [[_COMMUNITY_AI-Ready Evidence Contract & Schemas]]
- 1 edge to [[_COMMUNITY_Data Ingestion Foundation Spec Overview]]
- 1 edge to [[_COMMUNITY_Benchmark Reporter & CLI Design]]
- 1 edge to [[_COMMUNITY_Project Guardrails (Non-Negotiable Rules)]]

## Top bridge nodes
- [[Provider Registry Component]] - degree 5, connects to 3 communities
- [[Data Quality Auditor Component]] - degree 5, connects to 2 communities
- [[Requirement 3 Raw Payload Preservation]] - degree 5, connects to 2 communities
- [[Ingestion Architecture Diagram (mermaid)]] - degree 7, connects to 1 community
- [[Market Calendar Component]] - degree 4, connects to 1 community