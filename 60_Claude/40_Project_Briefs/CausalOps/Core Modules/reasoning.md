---
tags: [causalops, reasoning, anomaly, recommendations, statistics]
aliases: [reasoning.py]
---

# reasoning.py — Deterministic Reasoning Layer

`src/reasoning.py` runs after DoWhy estimation and produces three outputs: **anomaly detection**, **zone pressure summary**, and **ranked recommendations**. Like the discovery layer, it is pure statistics — no LLM.

## What It Produces

### 1. Anomalies (Causal Surprise)
An asset whose adverse outcome was improbable given its treatment group is flagged.

```
Threshold: CAUSALOPS_ANOMALY_THRESHOLD (default: 0.15)
```

For each evidence record where the outcome is adverse and the outcome probability (given treatment group average) deviates by more than the threshold, the record is flagged as an anomaly.

Each anomaly is then **explained** by walking the validated DAG:
- Active secondary causes of the outcome (non-refuted edges) account for the surprise
- Anomalies with no explaining cause are marked **unexplained** — the highest-severity signal

### 2. Zone Summary
Anomaly and outcome concentration per network zone (asset location), so the spatial axis of the 5D KG carries operational meaning.

### 3. Recommendations (Ranked)
Evidence-cited actions ranked by priority:
1. **Investigate unexplained anomalies** — the model cannot account for them
2. **Apply treatment** to highest-risk assets — ranked by active secondary risk drivers, only if estimated effect is statistically significant
3. **Mitigate confirmed secondary causes** from the validated DAG

## reasoning_node (LangGraph-compatible)

```python
def reasoning_node(state: dict[str, Any]) -> dict[str, Any]:
    # Reads: evidence_records, causal_payload (validated graph), causal_estimate_report
    # Writes: {"reasoning_report": report}
```

The reasoning report is stored in `RunRecord.reasoning_report` and exposed at `GET /run/{run_id}/reasoning`.

## Key Constants

```python
ANOMALY_THRESHOLD = float(os.getenv("CAUSALOPS_ANOMALY_THRESHOLD", "0.15"))
MAX_LISTED_TARGETS = int(os.getenv("CAUSALOPS_REASONING_MAX_TARGETS", "10"))
```

## Integration with 5D KG

Anomalies found here are ingested into the 5D graph as nodes/edges when the graph is built (either via Kafka stream or backfill). This allows the KG to capture which assets were flagged and why.

## Related Notes

- [[causal]] — Provides the validated causal graph consumed here
- [[estimators]] — Provides the estimate report used to determine significance
- [[dataset_compiler]] — Provides the compiled evidence records
- [[graph_5d]] — Where anomalies are ingested as KG events
- [[Coordinator Execution Model]] — `_run_reasoner` phase calls reasoning_node
