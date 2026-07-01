# Causal Discovery

`src/causal_discovery.py` makes the causal DAG emerge from the data rather than being trusted as hypothesized. It runs a PC-style discovery pass over the compiled evidence dataframe and validates every LLM-proposed edge. No LLM involvement — pure statistics.

## Why This Exists

The LLM proposes edges. But LLM-proposed edges may not reflect statistical independence in actual evidence. This module prevents the estimator from running on a DAG that the data doesn't support. The verdicts cannot be steered by the model that authored the hypothesis.

## Algorithm: PC-Style Skeleton + Orientation

### Phase 1 — Skeleton Discovery
For each variable pair:
1. Test marginal dependence (chi-square or G-test)
2. Test conditional dependence given every single variable (conditioning sets of size ≤ 1)
3. An edge survives only if variables are **dependent** both marginally AND given every conditioning variable

### Phase 2 — Collider Orientation
For every triple X, Z, Y where X-Z and Y-Z are adjacent but X-Y are not:
- If Z did **not** separate X and Y → orient as X → Z ← Y (v-structure/collider)

### Phase 3 — Validation
Each hypothesized edge gets a verdict:

| Verdict | Meaning |
|---------|---------|
| `confirmed` | Skeleton and orientation both agree with hypothesis |
| `compatible` | Dependence supported, data cannot orient — hypothesis direction adopted |
| `reversed` | Data orients the edge opposite to the hypothesis direction |
| `refuted` | Variables are statistically independent — edge dropped |
| `discovered` | Dependence exists in data but edge was not in the hypothesis |

## Key Constants

```python
DEFAULT_ALPHA = 0.1              # p-value threshold (env: HIVEMIND_DISCOVERY_ALPHA)
MIN_ROWS_FOR_DISCOVERY = 30      # skip discovery if fewer rows (env: HIVEMIND_DISCOVERY_MIN_ROWS)
```

If fewer than 30 rows: all edges marked `compatible` (insufficient data to test). Discovery doesn't run.

## EdgeVerdict Dataclass

```python
@dataclass
class EdgeVerdict:
    source: str
    target: str
    status: str          # confirmed | compatible | reversed | refuted | discovered
    p_value: float | None
    strength: float | None  # Cramér's V of marginal association
```

## Integration with causal.py (dowhy_engine_node)

```python
discovery = discover_and_validate(compilation.dataframe, graph_def.get("edges", []))
validated_graph = apply_discovery(graph_def, discovery)
estimation_edges_list = estimation_edges(validated_graph)
```

- `apply_discovery`: removes refuted edges, reverses reversed edges
- `estimation_edges`: returns only confirmed/compatible/reversed (not `discovered`) for DoWhy — discovered edges are noted but not used for estimation without hypothesis backing

## What Happens to Refuted Edges

Refuted edges are logged and included in `causal_discovery_report` and `report.warnings`. The validated (pruned) graph is re-published as `CAUSAL_PAYLOAD` so the 5D KG consumer updates edge statuses.

```python
logger.info(
    "Causal discovery refuted %d hypothesized edge(s): %s",
    len(refuted),
    ", ".join(f"{v.source}->{v.target}" for v in refuted),
)
```

## Related Notes

- [[causal-engine/00-overview|Causal Engine Overview]] — why this safeguard exists
- [[causal-engine/02-evidence|Evidence Compiler]] — provides the dataframe tested here
- [[causal-engine/03-estimation|Estimation]] — receives the validated graph
