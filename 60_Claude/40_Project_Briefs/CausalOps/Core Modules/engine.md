---
tags: [causalops, engine, orchestration, artifact]
aliases: [engine.py]
---

# engine.py — Run Orchestration & Artifact Persistence

`src/engine.py` is the backend boundary used by the HTTP API and legacy Streamlit demo. It runs the Phase 2 coordinator workflow, composes a frontend-friendly artifact, emits deterministic tier metrics, and persists the full run record.

## run_CausalOps() — Main Entry Point

```python
async def run_CausalOps(
    task_description: str,
    evidence_records: list[dict[str, Any]] | None = None,
    run_id: str | None = None,
) -> dict[str, Any]:
```

### Execution Flow

1. Generate `run_id` if not provided: `"run-20260601-143022-a1b2c3d4"`
2. `resolve_run_evidence(evidence_records)` → fallback to demo fixture if none provided
3. Bind run context (for Kafka correlation_id)
4. Set asyncio event loop for Kafka producer
5. Call `execute_run(...)` from `coordinator/runner.py`
6. Load bus summary from `RunRecord` or in-process summary
7. Compose frontend artifact
8. Persist as `data/{run_id}.json`
9. Publish `completed` run event
10. Return artifact dict

### Frontend Artifact Shape

```json
{
  "run_id": "run-20260601-143022-a1b2c3d4",
  "strategies": [...],               // strategy cards for UI display
  "ranked_strategies": [...],        // raw evaluator output
  "final_recommendation": "...",
  "causal_graph": {...},             // validated DAG
  "impact": {
    "ate": -0.34,                    // null if withheld
    "confidence": "high",            // "high" | "medium" | "low" | "insufficient_data"
    "p_value": 0.002,
    "ci_low": -0.49,
    "ci_high": -0.19,
    "n_rows": 150,
    "method": "backdoor.linear_regression",
    "demo_fixture": false
  },
  "causal_estimate_report": {...},
  "causal_dataset_profile": {...},
  "agent_tier_metrics": {...},
  "agent_evolution_report": {...},
  "policy_optimization_report": {...},
  "bus_summary": {...}
}
```

## Strategy Card Composition (_strategy_card)

Each memo is converted into a UI-friendly card:
```json
{
  "title": "Network Forensics Analyst",    // truncated to 80 chars
  "summary": "Trace lateral movement...",
  "risk_score": 0.47,                      // derived from risks count + confidence
  "cost_score": 0.63,                      // stable hash-based pseudo-score
  "speed_score": 0.71                      // stable hash-based pseudo-score
}
```

`cost_score` and `speed_score` are deterministic from `sha256(salt + text)` — they don't change across runs for the same memo content.

## Impact Confidence Mapping

```python
def _impact_confidence(report):
    if ate is None:               return "insufficient_data"
    if refuted and p ≤ 0.05:     return "high"
    if p ≤ 0.1:                   return "medium"
    return "low"
```

## Artifact Persistence

```python
artifact_path = DATA_DIR / f"{run_id}.json"
with artifact_path.open("w") as handle:
    json.dump(artifact, handle, indent=2)
```

`DATA_DIR` defaults to `./data/` (configurable via `CAUSALOPS_DATA_DIR`). Artifacts are plain JSON — the frontend fetches them at `GET /run/{run_id}`.

## load_run_artifact()

```python
def load_run_artifact(run_id: str) -> dict[str, Any] | None:
    artifact_path = DATA_DIR / f"{run_id}.json"
    ...
```

Used by `GET /run/{run_id}` to serve the completed artifact.

## new_run_id()

```python
def new_run_id() -> str:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"run-{stamp}-{uuid.uuid4().hex[:8]}"
```

## Related Notes

- [[api]] — Calls run_CausalOps() from POST /run and /run/sync
- [[Coordinator Execution Model]] — What execute_run() does internally
- [[benchmarking]] — score_agent_tiers() called here to build agent_tier_metrics
- [[demo_fixtures]] — resolve_run_evidence() and is_demo_evidence() from here
