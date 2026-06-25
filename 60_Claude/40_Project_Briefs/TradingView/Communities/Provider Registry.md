---
type: community
cohesion: 0.13
members: 22
---

# Provider Registry

**Cohesion:** 0.13 - loosely connected
**Members:** 22 nodes

## Members
- [[._validate_provider_name()]] - code - src/research_data/providers/base.py
- [[.get_capabilities()]] - code - src/research_data/providers/base.py
- [[.get_provider()]] - code - src/research_data/providers/base.py
- [[.get_provider_config()]] - code - src/research_data/providers/base.py
- [[.list_providers()]] - code - src/research_data/providers/base.py
- [[.test_unknown_provider_get_capabilities()]] - code - tests/test_provider_registry.py
- [[.test_unknown_provider_get_config()]] - code - tests/test_provider_registry.py
- [[.test_unknown_provider_lists_available_providers()]] - code - tests/test_provider_registry.py
- [[.test_unknown_provider_raises_config_error()]] - code - tests/test_provider_registry.py
- [[Error for unknown provider lists all registered provider names.]] - rationale - tests/test_provider_registry.py
- [[ProviderRegistry]] - code - src/research_data/providers/base.py
- [[Registry that loads provider configuration and returns concrete provider instanc]] - rationale - src/research_data/providers/base.py
- [[Requesting an unknown provider raises ConfigError.]] - rationale - tests/test_provider_registry.py
- [[Return a concrete provider instance by name.          Validates that the requi]] - rationale - src/research_data/providers/base.py
- [[Return a sorted list of all registered provider names.]] - rationale - src/research_data/providers/base.py
- [[Return the capabilities for a named provider.          Exposes provider capabi]] - rationale - src/research_data/providers/base.py
- [[Return the configuration for a named provider.          Args             nam]] - rationale - src/research_data/providers/base.py
- [[Test that unknown provider names are rejected with helpful error messages.]] - rationale - tests/test_provider_registry.py
- [[TestUnknownProviderRejected]] - code - tests/test_provider_registry.py
- [[Validate that a provider name is registered.          Raises             Con]] - rationale - src/research_data/providers/base.py
- [[get_capabilities also rejects unknown provider names.]] - rationale - tests/test_provider_registry.py
- [[get_provider_config also rejects unknown provider names.]] - rationale - tests/test_provider_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Provider_Registry
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Provider API-Key Validation]]
- 5 edges to [[_COMMUNITY_App Config Loading]]
- 4 edges to [[_COMMUNITY_Provider Registry Config-Loading Tests]]
- 4 edges to [[_COMMUNITY_Data Quality Auditor]]
- 3 edges to [[_COMMUNITY_Provider Registry Missing-Config Tests]]
- 3 edges to [[_COMMUNITY_Provider Registry Internals]]
- 2 edges to [[_COMMUNITY_Provider Config Loading & Validation]]
- 1 edge to [[_COMMUNITY_ProviderCapabilities Model]]
- 1 edge to [[_COMMUNITY_ProviderFetchResult Model]]
- 1 edge to [[_COMMUNITY_CSV Fixture Provider]]

## Top bridge nodes
- [[ProviderRegistry]] - degree 31, connects to 9 communities
- [[TestUnknownProviderRejected]] - degree 9, connects to 3 communities
- [[.get_provider()]] - degree 5, connects to 2 communities
- [[._validate_provider_name()]] - degree 7, connects to 1 community
- [[.test_unknown_provider_get_capabilities()]] - degree 4, connects to 1 community