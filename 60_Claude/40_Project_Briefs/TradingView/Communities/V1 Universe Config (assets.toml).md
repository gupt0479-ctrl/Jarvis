---
type: community
cohesion: 0.50
members: 5
---

# V1 Universe Config (assets.toml)

**Cohesion:** 0.50 - moderately connected
**Members:** 5 nodes

## Members
- [[Design Goals]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[V1 Universe (VOO,VTI,SPY,QQQ,AAPL,MSFT,NVDA,AMZN,GOOGL,META)]] - document - Docs/RESEARCH.md
- [[assets Table Schema]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[config.py_1]] - code - CLAUDE.md
- [[configassets.toml (V1 Universe Config)]] - document - config/assets.toml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/V1_Universe_Config_assetstoml
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Ingestion Data Flow & Module Map]]
- 1 edge to [[_COMMUNITY_Provider Landscape & Backup Sources]]
- 1 edge to [[_COMMUNITY_Quant Foundations & SECEDGAR Reference Docs]]
- 1 edge to [[_COMMUNITY_Data Ingestion Foundation Spec Overview]]
- 1 edge to [[_COMMUNITY_Spec RequirementsPropertiesTasks Cross-Refs]]

## Top bridge nodes
- [[configassets.toml (V1 Universe Config)]] - degree 6, connects to 2 communities
- [[config.py_1]] - degree 3, connects to 2 communities
- [[Design Goals]] - degree 3, connects to 1 community
- [[V1 Universe (VOO,VTI,SPY,QQQ,AAPL,MSFT,NVDA,AMZN,GOOGL,META)]] - degree 3, connects to 1 community