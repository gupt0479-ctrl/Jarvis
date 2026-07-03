---
type: project
status: sprout
created: 2026-07-01
tags:
  - brief
  - causalops
---
﻿---
tags: [causalops, causal-discovery, pc-algorithm, statistics, dag]
aliases: [causal_discovery.py]
---

# causal_discovery.py — Constraint-Based Causal Structure Discovery

`src/causal_discovery.py` makes the causal DAG **emerge from the data** rather than being trusted as hypothesized. It runs a PC-style discovery pass over the compiled evidence dataframe and validates every LLM-proposed edge.

## Why This Exists

The LLM proposes a DAG. But LLM-proposed edges may not reflect statistical independence structure in the actual evidence. This module prevents the estimator from running on a DAG that the data does not support.

## Algorithm: PC-Style Skeleton + Orientation

### Phase 1: Skeleton Discovery
For each pair of variables:
1. Test marginal dependence (chi-square or G-test)
2. Test conditional dependence given every single variable (conditioning sets of size ≤ 1)
3. An edge survives only if variables are **dependent** both marginally AND given every conditioning variable

### Phase 2: Collider Orientation
For every triple X, Z, Y where X-Z and Y-Z are adjacent but X-Y are not:
- If Z did **not** separate X and Y → orient as X → Z ← Y (v-structure/collider)

### Phase 3: Validation
Each hypothesized edge gets a verdict:

| Verdict | Meaning |
|---------|---------|
| `confirmed` | Skeleton and orientation both agree with hypothesis |
| `compatible` | Dependence supported, data cannot orient, hypothesis direction adopted |
| `reversed` | Data orients the edge opposite to hypothesis direction |
| `refuted` | Variables are statistically independent — edge dropped |
| `discovered` | Dependence exists in data but edge was not in the hypothesis |

## Key Constants

```python
DEFAULT_ALPHA = 0.1              # p-value threshold (env: CAUSALOPS_DISCOVERY_ALPHA)
MIN_ROWS_FOR_DISCOVERY = 30      # skip discovery if fewer rows (env: CAUSALOPS_DISCOVERY_MIN_ROWS)
```

If fewer than 30 rows, all edges are marked `compatible` (insufficient data to test).

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

## Integration with causal.py

```python
# In dowhy_engine_node:
discovery = discover_and_validate(compilation.dataframe, graph_def.get("edges", []))
validated_graph = apply_discovery(graph_def, discovery)
estimation_edges_list = estimation_edges(validated_graph)
```

- `apply_discovery`: removes refuted edges from graph, reverses reversed edges
- `estimation_edges`: returns only confirmed/compatible/reversed edges (not discovered) for DoWhy

## What Happens to Refuted Edges

Refuted edges are removed from the graph before DoWhy runs. They are logged and included in `causal_discovery_report` and in `report.warnings`. The validated (pruned) graph is re-published as `CAUSAL_PAYLOAD` so the 5D KG consumer can update edge statuses.

```python
# dowhy_engine_node logs refuted edges:
if refuted:
    logger.info(
        "Causal discovery refuted %d hypothesized edge(s): %s",
        len(refuted),
        ", ".join(f"{v.source}->{v.target}" for v in refuted),
    )
```

## Determinism Guarantee

Everything in this module is pure statistics over evidence records. No LLM involvement. The verdicts cannot be steered by the model that authored the hypothesis.

## Related Notes

- [[causal]] — Calls discovery from within dowhy_engine_node
- [[dataset_compiler]] — Provides the dataframe that discovery tests run on
- [[estimators]] — Receives the validated graph for DoWhy identification
- [[Design Philosophy]] — Why DAG validation from data is a core safeguard
