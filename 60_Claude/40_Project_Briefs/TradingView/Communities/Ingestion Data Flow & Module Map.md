---
type: community
cohesion: 0.16
members: 19
---

# Ingestion Data Flow & Module Map

**Cohesion:** 0.16 - loosely connected
**Members:** 19 nodes

## Members
- [[Evidence Card Action Labels (WATCHHOLDACCUMULATEREDUCEAVOIDINSUFFICIENT_DATA)]] - rationale - CLAUDE.md
- [[Evidence Card Cautious Action Labels]] - rationale - Docs/RESEARCH.md
- [[Ingestion Data Flow (provider - raw payload - normalization - quality - read API - evidence)]] - rationale - CLAUDE.md
- [[MVP Components Table]] - document - Docs/RESEARCH.md
- [[Repository Shape]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Research Desk Data Flow]] - rationale - Docs/RESEARCH.md
- [[System Architecture (Python source of truth)]] - rationale - Docs/RESEARCH.md
- [[Testing Strategy (pytest + hypothesis)]] - document - CLAUDE.md
- [[calendar.py_1]] - code - CLAUDE.md
- [[daily_ohlcv table]] - document - CLAUDE.md
- [[data_quality_reports table]] - document - CLAUDE.md
- [[ingestion_runs table]] - document - CLAUDE.md
- [[models.py_1]] - code - CLAUDE.md
- [[normalization.py_1]] - code - CLAUDE.md
- [[quality.py_1]] - code - CLAUDE.md
- [[raw_market_payloads table]] - document - CLAUDE.md
- [[read_api.py_1]] - code - CLAUDE.md
- [[research_data Module Map]] - document - CLAUDE.md
- [[storage.py_1]] - code - CLAUDE.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Ingestion_Data_Flow__Module_Map
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Project Guardrails (Non-Negotiable Rules)]]
- 2 edges to [[_COMMUNITY_V1 Universe Config (assets.toml)]]
- 2 edges to [[_COMMUNITY_Spec RequirementsPropertiesTasks Cross-Refs]]
- 2 edges to [[_COMMUNITY_NormalizerCalendar Properties & csv_fixture Entry]]
- 1 edge to [[_COMMUNITY_Data Ingestion Foundation Spec Overview]]
- 1 edge to [[_COMMUNITY_Provider Protocol & FabricationQuality Properties]]
- 1 edge to [[_COMMUNITY_Evidence Packet & Read API Properties]]
- 1 edge to [[_COMMUNITY_Quant Foundations & SECEDGAR Reference Docs]]
- 1 edge to [[_COMMUNITY_Provider Landscape & Backup Sources]]

## Top bridge nodes
- [[research_data Module Map]] - degree 9, connects to 2 communities
- [[Repository Shape]] - degree 8, connects to 2 communities
- [[quality.py_1]] - degree 7, connects to 2 communities
- [[storage.py_1]] - degree 6, connects to 1 community
- [[models.py_1]] - degree 5, connects to 1 community