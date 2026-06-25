---
source_file: "src/research_data/config.py"
type: "code"
community: "Provider Config Loading & Validation"
location: "L187"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Provider_Config_Loading__Validation
---

# load_providers_config()

## Connections
- [[.test_invalid_toml_raises_config_error()]] - `calls` [INFERRED]
- [[.test_invalid_toml_with_bad_value()]] - `calls` [INFERRED]
- [[.test_invalid_toml_with_unclosed_bracket()]] - `calls` [INFERRED]
- [[.test_missing_fields_error_identifies_provider_name()]] - `calls` [INFERRED]
- [[.test_missing_multiple_fields()]] - `calls` [INFERRED]
- [[.test_missing_providers_toml()]] - `calls` [INFERRED]
- [[.test_missing_single_field()]] - `calls` [INFERRED]
- [[ConfigError]] - `calls` [EXTRACTED]
- [[Load and validate providers.toml configuration.      Returns a tuple of (provi]] - `rationale_for` [EXTRACTED]
- [[ProviderConfig]] - `calls` [EXTRACTED]
- [[_load_toml_file()]] - `calls` [EXTRACTED]
- [[_validate_provider_entry()]] - `calls` [EXTRACTED]
- [[config.py]] - `contains` [EXTRACTED]
- [[load_config()]] - `calls` [EXTRACTED]
- [[test_missing_required_fields_raises_config_error()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Provider_Config_Loading__Validation