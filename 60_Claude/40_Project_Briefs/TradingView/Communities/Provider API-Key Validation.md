---
type: community
cohesion: 0.14
members: 15
---

# Provider API-Key Validation

**Cohesion:** 0.14 - loosely connected
**Members:** 15 nodes

## Members
- [[.__post_init__()]] - code - src/research_data/config.py
- [[.test_missing_api_key_error_includes_env_var_name()]] - code - tests/test_provider_registry.py
- [[.test_missing_api_key_raises_config_error()]] - code - tests/test_provider_registry.py
- [[.test_provider_not_requiring_key_succeeds()]] - code - tests/test_provider_registry.py
- [[.test_validate_api_key_directly()]] - code - tests/test_provider_registry.py
- [[Configuration for a single data provider.]] - rationale - src/research_data/config.py
- [[Error message includes the expected environment variable name.]] - rationale - tests/test_provider_registry.py
- [[Generate valid ProviderConfig instances for normalization.]] - rationale - tests/test_property_no_fabrication.py
- [[Provider requiring API key raises ConfigError when env var is not set.]] - rationale - tests/test_provider_registry.py
- [[Provider that doesn't require API key doesn't raise on get_provider.]] - rationale - tests/test_provider_registry.py
- [[ProviderConfig]] - code - src/research_data/config.py
- [[Test that missing API key raises ConfigError before any network call.]] - rationale - tests/test_provider_registry.py
- [[TestMissingApiKey]] - code - tests/test_provider_registry.py
- [[provider_configs()]] - code - tests/test_property_no_fabrication.py
- [[validate_api_key raises ConfigError for missing env var.]] - rationale - tests/test_provider_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Provider_API-Key_Validation
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_Normalization Pipeline]]
- 6 edges to [[_COMMUNITY_Provider Registry]]
- 5 edges to [[_COMMUNITY_Data Quality Auditor]]
- 5 edges to [[_COMMUNITY_AssetUniverse Config & DuckDB Storage]]
- 3 edges to [[_COMMUNITY_Provider Config Loading & Validation]]
- 3 edges to [[_COMMUNITY_App Config Loading]]
- 2 edges to [[_COMMUNITY_Adjustment Policy Mapping Tests]]
- 2 edges to [[_COMMUNITY_Provider Registry Missing-Config Tests]]
- 2 edges to [[_COMMUNITY_PriceProvider Protocol & MarketCalendarProtocol]]
- 1 edge to [[_COMMUNITY_ProviderFetchResult Model]]
- 1 edge to [[_COMMUNITY_Provider Registry Config-Loading Tests]]
- 1 edge to [[_COMMUNITY_DuckDB Schema Init & Duplicate-PK Handling]]
- 1 edge to [[_COMMUNITY_Secret Redaction]]
- 1 edge to [[_COMMUNITY_CSV Fixture Provider]]

## Top bridge nodes
- [[ProviderConfig]] - degree 35, connects to 14 communities
- [[TestMissingApiKey]] - degree 9, connects to 3 communities
- [[.test_validate_api_key_directly()]] - degree 5, connects to 2 communities
- [[.test_missing_api_key_error_includes_env_var_name()]] - degree 4, connects to 2 communities
- [[.test_missing_api_key_raises_config_error()]] - degree 4, connects to 2 communities