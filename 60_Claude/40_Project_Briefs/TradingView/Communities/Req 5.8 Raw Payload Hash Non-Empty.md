---
type: community
cohesion: 1.00
members: 1
---

# Req 5.8: Raw Payload Hash Non-Empty

**Cohesion:** 1.00 - tightly connected
**Members:** 1 nodes

## Members
- [[Requirement 5.8 (partial) raw_payload_hash must be non-empty.]] - rationale - tests/test_property_ohlcv_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Req_58_Raw_Payload_Hash_Non-Empty
SORT file.name ASC
```
