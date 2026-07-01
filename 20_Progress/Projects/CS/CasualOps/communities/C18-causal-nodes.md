# C18 — Causal Synthesis + DoWhy Engine Nodes

**Community 18** — 18 nodes, cohesion 0.17

The two LangGraph nodes that form the core of the causal pipeline: `causal_synthesis_node` (LLM) and `dowhy_engine_node` (deterministic).

## Key Nodes

`causal_synthesis_node()`, `dowhy_engine_node()`, `_ensure_nodes()`, `_format_memo()`, `_memo_value()`, `LangGraph nodes for causal hypothesis generation and estimation.`

## What This Code Does

`causal_synthesis_node()`: calls LLM with structured output to `CausalPayload`. Uses demo fixture if no real evidence. Returns `{"causal_payload": ..., "causal_refutation_passed": False}`.

`dowhy_engine_node()`: calls `compile_evidence_dataset` → `discover_and_validate` → `apply_discovery` → `estimate_causal_effect`. Returns updated payload with validated graph + full estimate report.

`_format_memo()` / `_memo_value()` serialize ranked strategies for prompt injection into the causal architect.

`_ensure_nodes()` sanitizes the graph_def to inject placeholder nodes for any referenced-but-undefined node IDs.

## Source File

`src/causal.py`

## Related Notes

- [[causal-engine/00-overview|Causal Engine Overview]] — full pipeline description
- [[communities/C14-dataset-compiler|C14]] — compile_evidence_dataset
- [[communities/C07-causal-discovery|C07]] — discover_and_validate
- [[communities/C16-dowhy-estimator|C16]] — estimate_causal_effect
