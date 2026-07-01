# C07 — Causal Discovery (PC Algorithm)

**Community 7** — 23 nodes, cohesion 0.14

PC-style constraint-based causal structure discovery. Validates every LLM-proposed edge against the actual compiled evidence using statistical independence tests.

## Key Nodes

`apply_discovery()`, `_binarize()`, `_conditional_test()`, `discover_and_validate()`, `DiscoveryReport`, `EdgeVerdict`, `estimation_edges()`, `_g_statistic()`

## What This Code Does

1. For each pair of variables: test marginal independence (chi-square / G-test) and conditional independence given each other variable
2. Collider orientation: X → Z ← Y v-structures detected via d-separation
3. Each hypothesized edge gets a verdict: confirmed / compatible / reversed / refuted / discovered
4. `apply_discovery()` drops refuted edges and reverses reversed ones
5. `estimation_edges()` filters to confirmed+compatible+reversed for DoWhy (not discovered)

`_binarize()` converts continuous variables into binary for chi-square testing.

## Source File

`src/causal_discovery.py`

## Related Notes

- [[causal-engine/01-discovery|Discovery]] — full algorithm description
- [[causal-engine/03-estimation|Estimation]] — receives the validated graph
