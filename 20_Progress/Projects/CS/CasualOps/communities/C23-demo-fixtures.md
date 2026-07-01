# C23 — Demo Fixtures

**Community 23** — 12 nodes, cohesion 0.23

Deterministic evidence fixtures for smoke testing without real credentials.

## Key Nodes

`demo_estimate()`, `demo_causal_payload()`, `patch_lateral_movement_evidence()`, `patch_lateral_movement_graph()`

## What This Code Does

Provides a bundled SIEM-style scenario: `Patch_Applied` → `Lateral_Movement`, confounder `Asset_Criticality`. Used by `GET /demo/estimate` and as the fallback when `is_demo_evidence(evidence_records)` is True.

`demo_causal_payload()` returns a pre-built `CausalPayload` dict — skips the causal_synthesis_node LLM call entirely.

## Source File

`src/demo_fixtures.py`

## Related Notes

- [[causal-engine/00-overview|Causal Engine Overview]] — demo evidence detection
- [[infrastructure/01-api|API]] — /demo/estimate endpoint
