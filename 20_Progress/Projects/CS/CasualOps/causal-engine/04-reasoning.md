# Reasoning Layer

`src/reasoning.py` runs after DoWhy estimation. Pure deterministic statistics — no LLM. Produces anomaly detection, zone pressure summary, and ranked recommendations.

## What It Produces

### 1. Anomalies (Causal Surprise)

An asset is flagged when its adverse outcome is improbable given its treatment group:

```python
ANOMALY_THRESHOLD = float(os.getenv("HIVEMIND_ANOMALY_THRESHOLD", "0.15"))
# Default: 0.15 deviation from treatment-group mean
```

For each evidence record where outcome is adverse and deviates beyond the threshold, the record is flagged. Each anomaly is then **explained** by walking the validated DAG — active secondary causes of the outcome account for the surprise. Anomalies with no explaining cause are marked **unexplained** — the highest-severity signal.

### 2. Zone Summary

Anomaly and outcome concentration per network zone (asset location). Feeds the spatial dimension of the 5D KG with operational meaning.

### 3. Recommendations (Ranked)

Evidence-cited actions ranked by priority:
1. **Investigate unexplained anomalies** — the model cannot account for them
2. **Apply treatment** to highest-risk assets — ranked by active secondary risk drivers, only when estimated effect is statistically significant
3. **Mitigate confirmed secondary causes** from the validated DAG

## reasoning_node Interface

```python
def reasoning_node(state: dict[str, Any]) -> dict[str, Any]:
    # Reads:  evidence_records, causal_payload (validated graph), causal_estimate_report
    # Writes: {"reasoning_report": report}
```

## Key Constants

```python
ANOMALY_THRESHOLD = float(os.getenv("HIVEMIND_ANOMALY_THRESHOLD", "0.15"))
MAX_LISTED_TARGETS = int(os.getenv("HIVEMIND_REASONING_MAX_TARGETS", "10"))
```

## 5D KG Integration

Anomalies ingested into the 5D graph as nodes/edges (either via Kafka stream consumer or coordinator backfill). This lets the KG track which assets were flagged, why, and when — across runs.

## Unexplained Anomalies

The most actionable signal. If an asset has a bad outcome and none of the validated causal edges can explain it, the reasoning layer flags it as unexplained. No causal story accounts for this asset's outcome — something is missing from the model.

## Related Notes

- [[causal-engine/03-estimation|Estimation]] — provides the estimate used for significance gating
- [[causal-engine/01-discovery|Discovery]] — provides the validated causal graph traversed here
- [[causal-engine/02-evidence|Evidence]] — provides the compiled records analyzed per-asset
- [[pipeline/02-coordinator|Coordinator]] — `_run_reasoner` phase
