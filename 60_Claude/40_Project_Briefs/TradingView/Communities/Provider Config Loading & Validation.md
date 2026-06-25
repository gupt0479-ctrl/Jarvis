---
type: community
cohesion: 0.12
members: 20
---

# Provider Config Loading & Validation

**Cohesion:** 0.12 - loosely connected
**Members:** 20 nodes

## Members
- [[.test_invalid_toml_raises_config_error()]] - code - tests/test_provider_registry.py
- [[.test_invalid_toml_with_bad_value()]] - code - tests/test_provider_registry.py
- [[.test_invalid_toml_with_unclosed_bracket()]] - code - tests/test_provider_registry.py
- [[.test_missing_fields_error_identifies_provider_name()]] - code - tests/test_provider_registry.py
- [[.test_missing_multiple_fields()]] - code - tests/test_provider_registry.py
- [[.test_missing_single_field()]] - code - tests/test_provider_registry.py
- [[A provider missing multiple required fields lists all missing fields.]] - rationale - tests/test_provider_registry.py
- [[A provider missing one required field produces an error naming that field.]] - rationale - tests/test_provider_registry.py
- [[Error message identifies the provider name with missing fields.]] - rationale - tests/test_provider_registry.py
- [[Invalid TOML syntax raises ConfigError mentioning parse failure.]] - rationale - tests/test_provider_registry.py
- [[Load and validate providers.toml configuration.      Returns a tuple of (provi]] - rationale - src/research_data/config.py
- [[TOML with invalid value type raises ConfigError.]] - rationale - tests/test_provider_registry.py
- [[Test that invalid TOML syntax produces clear parse error messages.]] - rationale - tests/test_provider_registry.py
- [[Test that missing required fields in provider config produce clear errors.]] - rationale - tests/test_provider_registry.py
- [[TestInvalidTomlSyntax]] - code - tests/test_provider_registry.py
- [[TestMissingRequiredFields]] - code - tests/test_provider_registry.py
- [[Unclosed bracket in TOML raises ConfigError.]] - rationale - tests/test_provider_registry.py
- [[Validate a single provider entry, returning list of missing fields.]] - rationale - src/research_data/config.py
- [[_validate_provider_entry()]] - code - src/research_data/config.py
- [[load_providers_config()]] - code - src/research_data/config.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Provider_Config_Loading__Validation
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_App Config Loading]]
- 7 edges to [[_COMMUNITY_Data Quality Auditor]]
- 3 edges to [[_COMMUNITY_Provider Registry Missing-Config Tests]]
- 3 edges to [[_COMMUNITY_Provider API-Key Validation]]
- 2 edges to [[_COMMUNITY_Provider Registry]]

## Top bridge nodes
- [[load_providers_config()]] - degree 15, connects to 4 communities
- [[TestInvalidTomlSyntax]] - degree 8, connects to 4 communities
- [[TestMissingRequiredFields]] - degree 8, connects to 4 communities
- [[.test_invalid_toml_raises_config_error()]] - degree 4, connects to 1 community
- [[.test_invalid_toml_with_bad_value()]] - degree 4, connects to 1 community