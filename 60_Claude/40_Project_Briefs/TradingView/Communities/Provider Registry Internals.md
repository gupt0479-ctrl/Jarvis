---
type: community
cohesion: 0.22
members: 9
---

# Provider Registry Internals

**Cohesion:** 0.22 - loosely connected
**Members:** 9 nodes

## Members
- [[.__init__()_4]] - code - src/research_data/providers/base.py
- [[Build a ProviderCapabilities model from a ProviderConfig.]] - rationale - src/research_data/providers/base.py
- [[Create a concrete provider instance based on the provider name.      This func]] - rationale - src/research_data/providers/base.py
- [[Initialize the provider registry.          Args             config Pre-load]] - rationale - src/research_data/providers/base.py
- [[Provider registry and base protocol for market data providers.  Defines the Pr]] - rationale - src/research_data/providers/base.py
- [[_build_capabilities()]] - code - src/research_data/providers/base.py
- [[_create_provider_instance()]] - code - src/research_data/providers/base.py
- [[base.py]] - code - src/research_data/providers/base.py
- [[default_provider_name()]] - code - src/research_data/providers/base.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Provider_Registry_Internals
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Provider Registry]]
- 2 edges to [[_COMMUNITY_App Config Loading]]
- 1 edge to [[_COMMUNITY_ProviderCapabilities Model]]
- 1 edge to [[_COMMUNITY_PriceProvider Protocol & MarketCalendarProtocol]]
- 1 edge to [[_COMMUNITY_CSV Fixture Provider]]

## Top bridge nodes
- [[_create_provider_instance()]] - degree 5, connects to 3 communities
- [[base.py]] - degree 6, connects to 2 communities
- [[.__init__()_4]] - degree 4, connects to 2 communities
- [[_build_capabilities()]] - degree 4, connects to 1 community