# C15 — Engine / Impact Functions

**Community 15** — 21 nodes, cohesion 0.12

The engine.py boundary functions: impact reporting, strategy card composition, and run artifact persistence.

## Key Nodes

`clear_run_context()`, `_impact_ate()`, `_impact_confidence()`, `_memo_text()`, `Convert a raw decision memo into a compact UI strategy card.`, `Return ATE for the UI, or None when estimation was withheld.`

## What This Code Does

`_impact_confidence()` maps the `CausalEstimateReport` to a UI confidence label: `"high"` (p ≤ 0.05, refuted), `"medium"` (p ≤ 0.1), `"low"` (anything else), `"insufficient_data"` (ate is None).

`_strategy_card()` converts a `DecisionMemo` into a UI card with `title`, `summary`, `risk_score`, `cost_score` (sha256 hash-based pseudo-score), `speed_score`.

`clear_run_context()` cleans up the bus context after a run completes.

## Source File

`src/engine.py`

## Related Notes

- [[causal-engine/03-estimation|Estimation]] — produces the CausalEstimateReport mapped here
- [[pipeline/00-overview|Pipeline Overview]] — artifact shape
