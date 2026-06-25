---
type: community
cohesion: 0.15
members: 15
---

# AI-Ready Evidence Contract & Schemas

**Cohesion:** 0.15 - loosely connected
**Members:** 15 nodes

## Members
- [[AI-Ready Evidence Contract]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[DataEvidencePacket Model]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Evidence Card JSON Shape]] - document - Docs/RESEARCH.md
- [[EvidenceRef Model]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[LangGraph Durable Execution Docs]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[OHLCVRecord Model]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[OHLCVRecord Validation Rules]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[OpenAI Agents SDK Guardrails Docs]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[OpenAI Structured Outputs Docs]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[PriceAdjustment Enum]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[PriceReadAPI Class Design]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Pydantic AI Agents Docs]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[QualityStatus Enum]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[daily_ohlcv Table Schema]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[data_quality_reports Schema]] - document - .kiro/specs/data-ingestion-foundation/design.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AI-Ready_Evidence_Contract__Schemas
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Spec RequirementsPropertiesTasks Cross-Refs]]
- 2 edges to [[_COMMUNITY_Quant Foundations & SECEDGAR Reference Docs]]
- 2 edges to [[_COMMUNITY_Ingestion Architecture Diagram & Components]]
- 2 edges to [[_COMMUNITY_Evidence Packet & Read API Properties]]
- 1 edge to [[_COMMUNITY_Benchmark Reporter & CLI Design]]

## Top bridge nodes
- [[daily_ohlcv Table Schema]] - degree 4, connects to 2 communities
- [[PriceReadAPI Class Design]] - degree 4, connects to 2 communities
- [[data_quality_reports Schema]] - degree 3, connects to 2 communities
- [[DataEvidencePacket Model]] - degree 7, connects to 1 community
- [[OHLCVRecord Model]] - degree 5, connects to 1 community