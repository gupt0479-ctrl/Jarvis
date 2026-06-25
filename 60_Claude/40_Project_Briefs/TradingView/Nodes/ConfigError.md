---
source_file: "src/research_data/config.py"
type: "code"
community: "App Config Loading"
location: "L35"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/App_Config_Loading
---

# ConfigError

## Connections
- [[._validate_provider_name()]] - `calls` [INFERRED]
- [[Exception]] - `inherits` [EXTRACTED]
- [[PriceProvider]] - `uses` [INFERRED]
- [[ProviderRegistry]] - `uses` [INFERRED]
- [[Raised when configuration loading or validation fails.]] - `rationale_for` [EXTRACTED]
- [[TestConfigFileNotFound]] - `uses` [INFERRED]
- [[TestInvalidTomlSyntax]] - `uses` [INFERRED]
- [[TestMissingApiKey]] - `uses` [INFERRED]
- [[TestMissingRequiredFields]] - `uses` [INFERRED]
- [[TestProperty10ProviderRegistryRejectsInvalidConfig]] - `uses` [INFERRED]
- [[TestUnknownProviderRejected]] - `uses` [INFERRED]
- [[TestValidConfigLoads]] - `uses` [INFERRED]
- [[_create_provider_instance()]] - `calls` [INFERRED]
- [[_find_config_dir()]] - `calls` [EXTRACTED]
- [[_load_toml_file()]] - `calls` [EXTRACTED]
- [[config.py]] - `contains` [EXTRACTED]
- [[load_providers_config()]] - `calls` [EXTRACTED]
- [[validate_api_key()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/App_Config_Loading