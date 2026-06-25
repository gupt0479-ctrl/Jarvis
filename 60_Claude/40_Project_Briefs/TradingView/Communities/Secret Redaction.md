---
type: community
cohesion: 0.13
members: 22
---

# Secret Redaction

**Cohesion:** 0.13 - loosely connected
**Members:** 22 nodes

## Members
- [[.test_case_insensitive_matching()]] - code - tests/test_storage.py
- [[.test_empty_dict()]] - code - tests/test_storage.py
- [[.test_no_secrets_unchanged()]] - code - tests/test_storage.py
- [[.test_redacts_api_key_field()]] - code - tests/test_storage.py
- [[.test_redacts_authorization_field()]] - code - tests/test_storage.py
- [[.test_redacts_password_field()]] - code - tests/test_storage.py
- [[.test_redacts_secret_field()]] - code - tests/test_storage.py
- [[.test_redacts_token_field()]] - code - tests/test_storage.py
- [[.test_returns_new_dict()]] - code - tests/test_storage.py
- [[Dict with no secret fields should be returned unchanged.]] - rationale - tests/test_storage.py
- [[Empty dict should return empty dict.]] - rationale - tests/test_storage.py
- [[Fields containing 'authorization' should be redacted.]] - rationale - tests/test_storage.py
- [[Fields containing 'key' should be redacted.]] - rationale - tests/test_storage.py
- [[Fields containing 'password' should be redacted.]] - rationale - tests/test_storage.py
- [[Fields containing 'secret' should be redacted.]] - rationale - tests/test_storage.py
- [[Fields containing 'token' should be redacted.]] - rationale - tests/test_storage.py
- [[Redact secret values from request metadata.      Matches field names containin]] - rationale - src/research_data/storage.py
- [[Redaction should be case-insensitive.]] - rationale - tests/test_storage.py
- [[Test that redact_secrets properly redacts secret field values. Requirements 3.5,]] - rationale - tests/test_storage.py
- [[TestRedactSecrets]] - code - tests/test_storage.py
- [[redact_secrets should return a new dict, not modify the original.]] - rationale - tests/test_storage.py
- [[redact_secrets()]] - code - src/research_data/storage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Secret_Redaction
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_AssetUniverse Config & DuckDB Storage]]
- 1 edge to [[_COMMUNITY_App Config Loading]]
- 1 edge to [[_COMMUNITY_Provider API-Key Validation]]
- 1 edge to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 1 edge to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 1 edge to [[_COMMUNITY_ProviderFetchResult Model]]
- 1 edge to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 1 edge to [[_COMMUNITY_Data Quality Auditor]]

## Top bridge nodes
- [[TestRedactSecrets]] - degree 19, connects to 7 communities
- [[redact_secrets()]] - degree 12, connects to 2 communities