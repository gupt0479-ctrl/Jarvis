---
source_file: "src/research_data/providers/base.py"
type: "code"
community: "Provider Registry"
location: "L57"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Provider_Registry
---

# ProviderRegistry

## Connections
- [[.__init__()_4]] - `method` [EXTRACTED]
- [[._validate_provider_name()]] - `method` [EXTRACTED]
- [[.get_capabilities()]] - `method` [EXTRACTED]
- [[.get_provider()]] - `method` [EXTRACTED]
- [[.get_provider_config()]] - `method` [EXTRACTED]
- [[.list_providers()]] - `method` [EXTRACTED]
- [[.test_missing_api_key_error_includes_env_var_name()]] - `calls` [INFERRED]
- [[.test_missing_api_key_raises_config_error()]] - `calls` [INFERRED]
- [[.test_missing_config_dir_for_registry()]] - `calls` [INFERRED]
- [[.test_provider_capabilities_exposed()]] - `calls` [INFERRED]
- [[.test_provider_config_accessible()]] - `calls` [INFERRED]
- [[.test_provider_not_requiring_key_succeeds()]] - `calls` [INFERRED]
- [[.test_provider_registry_from_config_dir()]] - `calls` [INFERRED]
- [[.test_unknown_provider_get_capabilities()]] - `calls` [INFERRED]
- [[.test_unknown_provider_get_config()]] - `calls` [INFERRED]
- [[.test_unknown_provider_lists_available_providers()]] - `calls` [INFERRED]
- [[.test_unknown_provider_raises_config_error()]] - `calls` [INFERRED]
- [[AppConfig]] - `uses` [INFERRED]
- [[CSVFixtureProvider]] - `uses` [INFERRED]
- [[ConfigError]] - `uses` [INFERRED]
- [[ProviderCapabilities]] - `uses` [INFERRED]
- [[ProviderConfig]] - `uses` [INFERRED]
- [[ProviderFetchResult]] - `uses` [INFERRED]
- [[Registry that loads provider configuration and returns concrete provider instanc]] - `rationale_for` [EXTRACTED]
- [[TestConfigFileNotFound]] - `uses` [INFERRED]
- [[TestInvalidTomlSyntax]] - `uses` [INFERRED]
- [[TestMissingApiKey]] - `uses` [INFERRED]
- [[TestMissingRequiredFields]] - `uses` [INFERRED]
- [[TestUnknownProviderRejected]] - `uses` [INFERRED]
- [[TestValidConfigLoads]] - `uses` [INFERRED]
- [[base.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Provider_Registry