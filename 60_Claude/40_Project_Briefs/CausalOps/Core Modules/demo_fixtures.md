---
type: project
status: sprout
created: 2026-07-01
tags: [causalops, demo, fixtures, smoke-test, siem]
aliases: [demo_fixtures.py]
---

# demo_fixtures.py — Deterministic Smoke-Test Evidence

`src/demo_fixtures.py` provides a pre-built SIEM-style evidence set and causal graph that exercises the full compiler/estimator pipeline without requiring real tenant data or LLM tokens.

## Demo Scenario

**Patching reduces observed lateral movement.**
- Treatment: `Patch_Applied`
- Outcome: `Lateral_Movement`
- Confounder: `Asset_Criticality`

## Key Functions

### patch_lateral_movement_evidence()
Returns a list of `EvidenceRecord` dicts with `source_type: "siem"`. Each record has `extracted_fields` containing numeric values for `Patch_Applied`, `Lateral_Movement`, and `Asset_Criticality`.

The fixture contains enough records to pass the 50-row minimum gate.

### patch_lateral_movement_graph()
Returns a `CausalGraphDef`-compatible dict with:
- 3 nodes: Patch_Applied, Lateral_Movement, Asset_Criticality
- 3 edges: Asset_Criticality→Patch_Applied, Asset_Criticality→Lateral_Movement, Patch_Applied→Lateral_Movement
- treatment_variable: "Patch_Applied"
- outcome_variable: "Lateral_Movement"

### demo_causal_payload()
Returns a `CausalPayload`-compatible dict for the patching scenario. Used by `causal_synthesis_node` when no caller evidence is present.

### is_demo_evidence(evidence_records)
Returns True when evidence_records is None, empty, or all records have `source_type: "synthetic"`.

```python
def is_demo_evidence(evidence_records):
    if not evidence_records:
        return True
    return all(r.get("source_type") == "synthetic" for r in evidence_records)
```

### resolve_run_evidence(evidence_records)
Returns `(resolved_evidence, used_demo_fixture: bool)`. If no caller evidence is provided, falls back to demo evidence.

## Used By

- `GET /demo/estimate` — the API's public smoke-test endpoint
- `causal.py` — `causal_synthesis_node` uses `demo_causal_payload()` when no evidence
- `engine.py` — `resolve_run_evidence()` and `is_demo_evidence()` for artifact flagging
- Tests — `tests/test_demo_fixtures.py` verifies fixture integrity

## Demo Warning in Reports

When demo evidence is used, the estimate report includes:
```
"DEMO_FIXTURE: No caller evidence was supplied. ATE is estimated from the bundled patch-vs-lateral-movement SIEM fixture, not from your scenario telemetry."
```

## Related Notes

- [[evidence_adapters]] — Production path for normalizing real evidence
- [[dataset_compiler]] — Receives the demo evidence records
- [[api]] — GET /demo/estimate exposes this
