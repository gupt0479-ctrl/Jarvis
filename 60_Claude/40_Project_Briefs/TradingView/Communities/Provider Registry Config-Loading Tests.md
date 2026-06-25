---
type: community
cohesion: 0.20
members: 10
---

# Provider Registry Config-Loading Tests

**Cohesion:** 0.20 - loosely connected
**Members:** 10 nodes

## Members
- [[.test_load_config_from_project_root()]] - code - tests/test_provider_registry.py
- [[.test_provider_capabilities_exposed()]] - code - tests/test_provider_registry.py
- [[.test_provider_config_accessible()]] - code - tests/test_provider_registry.py
- [[.test_provider_registry_from_config_dir()]] - code - tests/test_provider_registry.py
- [[ProviderRegistry exposes capabilities for registered providers.]] - rationale - tests/test_provider_registry.py
- [[ProviderRegistry initializes successfully with valid config.]] - rationale - tests/test_provider_registry.py
- [[ProviderRegistry returns provider config for known providers.]] - rationale - tests/test_provider_registry.py
- [[Test that the actual configproviders.toml loads without errors.]] - rationale - tests/test_provider_registry.py
- [[TestValidConfigLoads]] - code - tests/test_provider_registry.py
- [[Valid config loads successfully using the actual config directory.]] - rationale - tests/test_provider_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Provider_Registry_Config-Loading_Tests
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Provider Registry]]
- 2 edges to [[_COMMUNITY_App Config Loading]]
- 1 edge to [[_COMMUNITY_Provider Registry Missing-Config Tests]]
- 1 edge to [[_COMMUNITY_Provider API-Key Validation]]

## Top bridge nodes
- [[TestValidConfigLoads]] - degree 9, connects to 4 communities
- [[.test_load_config_from_project_root()]] - degree 3, connects to 1 community
- [[.test_provider_capabilities_exposed()]] - degree 3, connects to 1 community
- [[.test_provider_config_accessible()]] - degree 3, connects to 1 community
- [[.test_provider_registry_from_config_dir()]] - degree 3, connects to 1 community