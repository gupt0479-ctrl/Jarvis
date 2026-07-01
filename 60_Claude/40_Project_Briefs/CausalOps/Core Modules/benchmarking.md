---
tags: [causalops, benchmarking, metrics, tiers, scoring]
aliases: [benchmarking.py]
---

# benchmarking.py — Deterministic Tier Metrics

`src/benchmarking.py` emits deterministic quality metrics for each tier of the agent pipeline. These metrics are included in the run artifact as `agent_tier_metrics` and give reproducible signals about what each tier produced.

## Tiers Scored

| Tier | What's Measured |
|------|-----------------|
| `orchestrator` | Decomposition quality — number of parent configs, persona diversity |
| `parent` | Child task quality — objectives produced per parent, specificity |
| `child` | Memo completeness — evidence_needs, risks, assumptions populated |
| `evaluator` | Output shape — ranked_strategies length, recommendation presence |
| `causal_graph` | Graph validity — nodes, edges, treatment/outcome defined |
| `estimator` | Readiness — gates passed, ATE presence, refutation status |

## score_agent_tiers() — Main Entry Point

```python
def score_agent_tiers(
    state: dict[str, Any],
    summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
```

Returns:
```json
{
  "orchestrator": { "score": 0.85, "signals": {...} },
  "parent":       { "score": 0.72, "signals": {...} },
  "child":        { "score": 0.68, "signals": {...} },
  "evaluator":    { "score": 0.90, "signals": {...} },
  "causal_graph": { "score": 0.80, "signals": {...} },
  "estimator":    { "score": 0.75, "signals": {...} },
  "overall_score": 0.78
}
```

## Key Properties

- **Deterministic:** Same inputs always produce the same scores. Uses only observable signals from GraphState, not LLM judgments.
- **Structural:** Scores reflect presence/absence and counts of expected outputs, not semantic quality.
- **Per-tier:** Each tier's score is independent. A failed causal estimation doesn't affect the orchestrator or memo scores.

## Usage in Artifact

`engine.py` calls `score_agent_tiers(final_state, summary=bus_summary)` and embeds the result in the run artifact for frontend display and monitoring.

## Related Notes

- [[engine]] — Calls score_agent_tiers and includes result in artifact
- [[agents]] — Orchestrator, parent, child produce outputs that are scored
- [[evaluator]] — Scored on output shape
- [[causal]] — Scored on graph validity and estimate readiness
