# C30 — Estimate Endpoint

**Community 30** — 4 nodes, cohesion 0.50

The deterministic estimation endpoint handler and its request model.

## Key Nodes

`estimate_from_evidence()`, `EstimateRequest`, `Request body for deterministic evidence-backed estimation.`, `Compile caller evidence and return a causal estimate report.`

## What This Code Does

`estimate_from_evidence()` handles `POST /estimate`. Calls `compile_evidence_dataset()` + `estimate_causal_effect()` directly, no LLM. Returns `causal_estimate_report`, `causal_dataset_profile`, and `provenance`.

## Source File

`src/api.py`

## Related Notes

- [[infrastructure/01-api|API Reference]] — POST /estimate
