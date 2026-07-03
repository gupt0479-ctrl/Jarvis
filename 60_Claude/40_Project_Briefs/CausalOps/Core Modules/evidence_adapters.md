---
type: project
status: sprout
created: 2026-07-01
tags: [causalops, evidence, normalization, siem, cve, adapters]
aliases: [evidence_adapters.py]
---

# evidence_adapters.py — External Evidence Normalizers

`src/evidence_adapters.py` converts records from SIEM exports, CVE feeds, and incident report systems into normalized `EvidenceRecord` objects. These adapters are **export-based** — they accept records from query exports without requiring live tenant credentials.

## Three Normalizers

### normalize_sentinel_records()
Normalizes Microsoft Sentinel or SIEM-like export rows.

**Field extraction priority:**
```python
SENTINEL_ASSET_KEYS  = ("Computer", "DeviceName", "HostName", "AssetId", "ResourceId")
SENTINEL_USER_KEYS   = ("Account", "UserPrincipalName", "InitiatingProcessAccountName")
SENTINEL_EVENT_KEYS  = ("AlertName", "Activity", "EventID", "OperationName", "Type")
SENTINEL_TIME_KEYS   = ("TimeGenerated", "Timestamp", "EventTime", "CreatedTime")
SENTINEL_TECHNIQUE_KEYS = ("TechniqueId", "TechniqueID", "MITRETechnique", "Tactic")
```

Sets `source_type: "siem"`.

**Key behavior:** All remaining fields not consumed by the fixed keys are passed through as `extracted_fields` via `_field_aliases()`. This allows arbitrary SIEM fields (`Patch_Applied`, `Lateral_Movement`, `Asset_Criticality`) to survive into the compiler.

### normalize_cve_records()
Normalizes NVD/CVE-style feed records.

**Extracted fields:**
- `cve_id` — from `cve_id`, `cveId`, `CVE`, or `id`
- `severity` — from `baseScore`, `cvssScore`, `score`
- `raw_text` — English description from `descriptions[0].value`
- `event_type` — `"cve_published"` plus optional vendor/product from `configurations`

Sets `source_type: "cve"`.

### normalize_incident_reports()
Normalizes incident report export rows.

**Extracted fields:**
- `asset_id` — from `asset_id`, `host`, `device`, `computer`
- `observed_at` — from `created_at`, `timestamp`, `date`, `incident_date`
- `technique_id` — from `technique_id` or parsed from `summary` text
- `severity` — from numeric value or text mapping (critical=1.0, high=0.8, medium=0.5, low=0.2)

Sets `source_type: "incident_report"`.

## Usage Pattern

All three return iterators of `dict[str, Any]` (the `EvidenceRecord.model_dump()` output). This means they can be piped directly into `/estimate` as `evidence_records`.

```python
# API endpoint:
@app.post("/normalize/sentinel")
def normalize_sentinel_export(request: NormalizeRequest):
    return {
        "evidence_records": list(
            normalize_sentinel_records(request.records, source_name=request.source_name)
        )
    }
```

## Demo Without Live Credentials

The `/normalize/*` endpoints accept exported records (CSV exports, JSON query results, etc.) without requiring API keys or live connections. The workflow is:
1. Export data from your SIEM/CVE system
2. `POST /normalize/sentinel` (or `/cve`, `/incidents`) to get `evidence_records`
3. `POST /estimate` with the graph and evidence_records
4. Get causal estimate report

## Related Notes

- [[schema]] — EvidenceRecord model that normalizers produce
- [[dataset_compiler]] — Consumes normalized EvidenceRecord dicts
- [[api]] — The `/normalize/*` endpoints that expose these normalizers
- [[demo_fixtures]] — Alternative path: pre-built SIEM-style evidence for smoke testing
