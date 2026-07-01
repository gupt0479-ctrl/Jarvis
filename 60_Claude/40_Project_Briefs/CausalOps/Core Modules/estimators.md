---
tags: [causalops, estimators, dowhy, statsmodels, ate, DO-NOT-TOUCH]
aliases: [estimators.py]
---

# estimators.py — DoWhy + Statsmodels Estimator

> ⚠️ **DO NOT MODIFY.** This file is the core statistical safeguard. The backdoor identification, GML graph construction, refuter suite, and statsmodels coefficient report must not be altered without careful review.

`src/estimators.py` runs causal identification and effect estimation after quality gates pass. It uses DoWhy for causal identification and estimation, and statsmodels for explicit coefficient diagnostics that executives and reviewers ask for.

## estimate_causal_effect() — Main Entry Point

```python
def estimate_causal_effect(
    graph_def: dict[str, Any],
    df: pd.DataFrame,
    profile: CausalDatasetProfile,
) -> CausalEstimateReport:
```

### Step 1: Gate Check
```python
gates_passed, gate_warnings = passes_estimation_gates(profile, df)
if not gates_passed:
    return CausalEstimateReport(
        method="withheld:data_quality_gates",
        ate=None, p_value=None, ...
    )
```

If gates fail, returns immediately with `ate=None`. The API/UI shows "insufficient data".

### Step 2: GML Graph Construction
The DoWhy `CausalModel` requires a GML string representing the DAG. `_build_gml()` converts the graph_def into:
```
graph [
  directed 1
  node [id "Patch_Applied" label "Patch_Applied"]
  node [id "Lateral_Movement" label "Lateral_Movement"]
  edge [source "Patch_Applied" target "Lateral_Movement"]
  ...
]
```
Only nodes present in the dataframe columns are included.

### Step 3: DoWhy Estimation
```python
model = dowhy.CausalModel(data=df, treatment=treatment, outcome=outcome, graph=gml_string)
identified_estimand = model.identify_effect(proceed_when_unidentifiable=False)
estimate = model.estimate_effect(
    identified_estimand,
    method_name="backdoor.linear_regression",
)
```
Uses linear regression backdoor adjustment. If identification fails (unidentifiable), returns `withheld:dowhy_identification_or_estimation_failed`.

### Step 4: Statsmodels Diagnostics
```python
stats = _linear_regression_stats(df, treatment, outcome, adjustment_set)
```
Runs `statsmodels.OLS` to get: `standard_error`, `p_value`, `ci_low`, `ci_high` for the treatment coefficient. This is separate from DoWhy's estimate value and gives reviewers familiar statistical diagnostics.

### Step 5: Refuters
```python
refuters = _run_refuters(model, identified_estimand, estimate, ate)
```
Runs DoWhy's built-in refuters:
- **Placebo treatment refuter** — replaces treatment with random noise; ATE should become ~0
- **Data subset refuter** — estimate on 80% subset; should be similar to full-data ATE

`refutation_passed = all(r.passed for r in refuters)`

## CausalEstimateReport Output

```python
CausalEstimateReport(
    data_mode="empirical",
    method="backdoor.linear_regression",
    treatment="Patch_Applied",
    outcome="Lateral_Movement",
    adjustment_set=["Asset_Criticality"],
    n_rows=150,
    ate=-0.34,
    standard_error=0.08,
    p_value=0.002,
    ci_low=-0.49,
    ci_high=-0.19,
    refutation_passed=True,
    refuters=[
        RefuterReport(name="placebo_treatment", passed=True, details="..."),
        RefuterReport(name="data_subset", passed=True, details="..."),
    ],
    warnings=[],
    dataset_profile=...,
)
```

## Confidence Mapping (in engine.py)

```python
def _impact_confidence(report):
    if report.ate is None:          return "insufficient_data"
    if refuted and p_value <= 0.05: return "high"
    if p_value <= 0.1:              return "medium"
    return "low"
```

## Related Notes

- [[dataset_compiler]] — Provides the dataframe and CausalDatasetProfile
- [[causal]] — Calls this from dowhy_engine_node
- [[schema]] — CausalEstimateReport, RefuterReport models
- [[Design Philosophy]] — Why ATE withholding is correct behavior
- [[api]] — `/estimate` and `/demo/estimate` endpoints that invoke this directly
