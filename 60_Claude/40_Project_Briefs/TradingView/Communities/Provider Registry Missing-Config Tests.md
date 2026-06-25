---
type: community
cohesion: 0.25
members: 8
---

# Provider Registry Missing-Config Tests

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[.test_missing_config_dir_for_registry()]] - code - tests/test_provider_registry.py
- [[.test_missing_providers_toml()]] - code - tests/test_provider_registry.py
- [[Missing providers.toml raises ConfigError with the expected path.]] - rationale - tests/test_provider_registry.py
- [[ProviderRegistry raises ConfigError when config dir doesn't have providers.toml.]] - rationale - tests/test_provider_registry.py
- [[Test that missing config files produce clear error messages.]] - rationale - tests/test_provider_registry.py
- [[TestConfigFileNotFound]] - code - tests/test_provider_registry.py
- [[Unit tests for the Provider Registry and configuration loading.  Tests cover]] - rationale - tests/test_provider_registry.py
- [[test_provider_registry.py]] - code - tests/test_provider_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Provider_Registry_Missing-Config_Tests
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Provider Config Loading & Validation]]
- 3 edges to [[_COMMUNITY_Provider Registry]]
- 2 edges to [[_COMMUNITY_Provider API-Key Validation]]
- 1 edge to [[_COMMUNITY_Provider Registry Config-Loading Tests]]
- 1 edge to [[_COMMUNITY_App Config Loading]]
- 1 edge to [[_COMMUNITY_Data Quality Auditor]]

## Top bridge nodes
- [[test_provider_registry.py]] - degree 7, connects to 4 communities
- [[TestConfigFileNotFound]] - degree 7, connects to 3 communities
- [[.test_missing_providers_toml()]] - degree 4, connects to 2 communities
- [[.test_missing_config_dir_for_registry()]] - degree 3, connects to 1 community