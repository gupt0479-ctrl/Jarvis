---
type: community
cohesion: 0.15
members: 16
---

# Provider Landscape & Backup Sources

**Cohesion:** 0.15 - loosely connected
**Members:** 16 nodes

## Members
- [[Alpha Vantage Documentation]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Alpha Vantage Support Page]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Backup Providers Table]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[FMP Quickstart Docs]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[OpenBB Docs]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Polygon Basic as V1 Default Provider]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Polygon Stocks Pricing Page]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[Provider Selection Rules]] - rationale - .kiro/specs/data-ingestion-foundation/design.md
- [[Task 11 Polygon Provider]] - document - .kiro/specs/data-ingestion-foundation/tasks.md
- [[Tiingo EOD Ingestion Guide]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[alpha_vantage provider entry]] - document - config/providers.toml
- [[configproviders.toml (Provider Registry Config)]] - document - config/providers.toml
- [[fmp provider entry]] - document - config/providers.toml
- [[polygon provider entry]] - document - config/providers.toml
- [[providers Table Schema]] - document - .kiro/specs/data-ingestion-foundation/design.md
- [[tiingo provider entry]] - document - config/providers.toml

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Provider_Landscape__Backup_Sources
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Spec RequirementsPropertiesTasks Cross-Refs]]
- 1 edge to [[_COMMUNITY_V1 Universe Config (assets.toml)]]
- 1 edge to [[_COMMUNITY_Data Ingestion Foundation Spec Overview]]
- 1 edge to [[_COMMUNITY_Quant Foundations & SECEDGAR Reference Docs]]
- 1 edge to [[_COMMUNITY_Ingestion Data Flow & Module Map]]
- 1 edge to [[_COMMUNITY_Provider Protocol & FabricationQuality Properties]]
- 1 edge to [[_COMMUNITY_Benchmark Reporter & CLI Design]]
- 1 edge to [[_COMMUNITY_Project Guardrails (Non-Negotiable Rules)]]
- 1 edge to [[_COMMUNITY_NormalizerCalendar Properties & csv_fixture Entry]]

## Top bridge nodes
- [[configproviders.toml (Provider Registry Config)]] - degree 12, connects to 5 communities
- [[Task 11 Polygon Provider]] - degree 4, connects to 3 communities
- [[Backup Providers Table]] - degree 11, connects to 2 communities