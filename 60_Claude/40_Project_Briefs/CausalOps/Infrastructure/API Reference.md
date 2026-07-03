---
type: project
status: sprout
created: 2026-07-01
tags:
  - brief
  - causalops
---
﻿---
tags: [causalops, api, endpoints, curl, reference]
---

# API Reference

Base URL: `http://localhost:8000`

## Health & Info

```bash
GET /health
# → {"status": "ok"}

GET /
# → {"message": "Welcome to the CausalOps API", "docs_url": "/docs", ...}
```

## Full Agentic Run

### Async (recommended for UI)
```bash
# 1. Generate a run_id client-side
run_id="run-$(date +%Y%m%d-%H%M%S)-$(head -c4 /dev/urandom | xxd -p)"

# 2. Open SSE stream first
curl -N "http://localhost:8000/run/${run_id}/events"

# 3. In another terminal, POST the run
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d "{\"task_description\": \"Suspicious lateral movement detected across 3 hosts in the finance VLAN after a phishing email campaign.\", \"run_id\": \"${run_id}\"}"
# → {"run_id": "...", "status": "queued"}

# 4. Poll for completion
curl "http://localhost:8000/run/${run_id}"
# → {"run_id": "...", "status": "completed", "artifact": {...}}
```

### Synchronous (scripts/tests)
```bash
curl -X POST http://localhost:8000/run/sync \
  -H "Content-Type: application/json" \
  -d '{"task_description": "..."}'
```

## Deterministic Estimation (no LLM tokens)

```bash
# Demo (pre-built fixture):
curl http://localhost:8000/demo/estimate

# Your own evidence + graph:
curl -X POST http://localhost:8000/estimate \
  -H "Content-Type: application/json" \
  -d '{
    "graph": {
      "nodes": [
        {"id": "Patch_Applied", "label": "Patch Applied", "description": "Asset patched"},
        {"id": "Lateral_Movement", "label": "Lateral Movement", "description": "Lateral movement observed"},
        {"id": "Asset_Criticality", "label": "Asset Criticality", "description": "High-value tier"}
      ],
      "edges": [
        {"source": "Asset_Criticality", "target": "Patch_Applied", "relationship": "Critical assets prioritized"},
        {"source": "Asset_Criticality", "target": "Lateral_Movement", "relationship": "Critical assets attract movement"},
        {"source": "Patch_Applied", "target": "Lateral_Movement", "relationship": "Patching reduces exploitability"}
      ],
      "treatment_variable": "Patch_Applied",
      "outcome_variable": "Lateral_Movement",
      "candidate_confounders": ["Asset_Criticality"]
    },
    "evidence_records": [
      {
        "source_type": "siem",
        "source_name": "sentinel-kql-export",
        "observed_at": "2026-05-12T10:00:00Z",
        "asset_id": "host-001",
        "raw_ref": "row-001",
        "extracted_fields": {"Patch_Applied": 1, "Lateral_Movement": 0, "Asset_Criticality": 1}
      }
    ]
  }'
```

## Evidence Normalizers

```bash
# Normalize Sentinel/SIEM rows:
curl -X POST http://localhost:8000/normalize/sentinel \
  -H "Content-Type: application/json" \
  -d '{"source_name": "sentinel-prod-kql", "records": [
    {"TimeGenerated": "2026-05-12T10:00:00Z", "Computer": "host-001",
     "AlertName": "Lateral movement detected", "Patch_Applied": 1,
     "Lateral_Movement": 0, "Asset_Criticality": 1}
  ]}'

# Normalize CVE records:
curl -X POST http://localhost:8000/normalize/cve \
  -H "Content-Type: application/json" \
  -d '{"records": [
    {"id": "CVE-2026-0001", "published": "2026-05-01", "baseScore": 9.1,
     "descriptions": [{"lang": "en", "value": "Vulnerable service"}]}
  ]}'

# Normalize incident reports:
curl -X POST http://localhost:8000/normalize/incidents \
  -H "Content-Type: application/json" \
  -d '{"records": [
    {"incident_id": "INC-42", "created_at": "2026-05-12", "asset_id": "host-001",
     "severity": "high", "summary": "Credential misuse followed by lateral movement."}
  ]}'
```

## 5D Knowledge Graph

```bash
# Get KG for a run:
curl "http://localhost:8000/run/${run_id}/graph/5d"

# Manually ingest nodes/edges:
curl -X POST "http://localhost:8000/run/${run_id}/graph/5d/ingest" \
  -H "Content-Type: application/json" \
  -d '{"nodes": [{"id": "host-001", "node_type": "asset", "label": "Finance Server"}], "edges": []}'

# Get reasoning report:
curl "http://localhost:8000/run/${run_id}/reasoning"
```

## Response: Causal Estimate Report

```json
{
  "causal_estimate_report": {
    "data_mode": "empirical",
    "method": "backdoor.linear_regression",  // or "withheld:data_quality_gates"
    "treatment": "Patch_Applied",
    "outcome": "Lateral_Movement",
    "adjustment_set": ["Asset_Criticality"],
    "n_rows": 150,
    "ate": -0.34,
    "standard_error": 0.08,
    "p_value": 0.002,
    "ci_low": -0.49,
    "ci_high": -0.19,
    "refutation_passed": true,
    "warnings": []
  }
}
```

## Related Notes

- [[api]] — Implementation details and request model definitions
- [[evidence_adapters]] — Normalizer logic
- [[estimators]] — What the estimate endpoints call
- [[Docker Setup]] — How to start the stack
