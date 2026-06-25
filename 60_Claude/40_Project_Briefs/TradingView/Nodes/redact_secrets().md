---
source_file: "src/research_data/storage.py"
type: "code"
community: "Secret Redaction"
location: "L405"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Secret_Redaction
---

# redact_secrets()

## Connections
- [[.test_case_insensitive_matching()]] - `calls` [INFERRED]
- [[.test_empty_dict()]] - `calls` [INFERRED]
- [[.test_no_secrets_unchanged()]] - `calls` [INFERRED]
- [[.test_redacts_api_key_field()]] - `calls` [INFERRED]
- [[.test_redacts_authorization_field()]] - `calls` [INFERRED]
- [[.test_redacts_password_field()]] - `calls` [INFERRED]
- [[.test_redacts_secret_field()]] - `calls` [INFERRED]
- [[.test_redacts_token_field()]] - `calls` [INFERRED]
- [[.test_returns_new_dict()]] - `calls` [INFERRED]
- [[Redact secret values from request metadata.      Matches field names containin]] - `rationale_for` [EXTRACTED]
- [[storage.py]] - `contains` [EXTRACTED]
- [[write_raw_payload()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Secret_Redaction