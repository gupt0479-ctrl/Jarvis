# C16 — DoWhy + Statsmodels Estimator

**Community 16** — 19 nodes, cohesion 0.17

DoWhy causal identification + linear regression estimation. DO NOT MODIFY `src/estimators.py`.

## Key Nodes

`_build_gml()`, `estimate_causal_effect()`, `_linear_regression_stats()`, `Estimate causal effects from compiled evidence datasets.`, `Build a GML DAG string compatible with NetworkX and DoWhy.`, `Compute OLS diagnostics for the treatment coefficient.`

## What This Code Does

`_build_gml()` converts a graph_def dict to a GML string that DoWhy's `CausalModel` accepts. Only includes nodes present as dataframe columns.

`estimate_causal_effect()` runs the full estimation pipeline: gate check → GML construction → DoWhy identification → backdoor.linear_regression → statsmodels OLS diagnostics → refuters.

`_linear_regression_stats()` runs a separate `statsmodels.OLS` to produce `p_value`, `standard_error`, `ci_low`, `ci_high` for the treatment coefficient. This is separate from DoWhy's point estimate.

## Source File

`src/estimators.py` — **DO NOT MODIFY**

## Related Notes

- [[causal-engine/03-estimation|Estimation]] — full algorithm with all steps
- [[communities/C14-dataset-compiler|C14]] — provides the dataframe and profile
- [[communities/C29-refutation-logic|C29]] — refutation loop termination logic
