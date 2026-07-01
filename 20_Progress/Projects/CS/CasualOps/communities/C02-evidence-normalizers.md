# C02 — Evidence Normalizers

**Community 2** — 32 nodes, cohesion 0.12

The three evidence adapter functions and their API request models. Converts raw SIEM exports, CVE feeds, and incident reports into normalized `EvidenceRecord` dicts.

## Key Nodes

`normalize_cve_export()`, `normalize_incident_export()`, `normalize_sentinel_export()`, `NormalizeRequest`

## Source File

`src/evidence_adapters.py`

## Related Notes

- [[causal-engine/02-evidence|Evidence Compiler]] — what normalizers produce
- [[infrastructure/01-api|API]] — POST /normalize/* endpoints
