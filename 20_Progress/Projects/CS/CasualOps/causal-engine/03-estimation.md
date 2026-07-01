# Causal Estimation

`src/estimators.py` runs DoWhy identification + linear regression estimation after quality gates pass. **DO NOT MODIFY** — the backdoor identification, GML construction, refuter suite, and OLS diagnostics must not be altered without deep review.

## estimate_causal_effect() — Main Entry Point

```python
def estimate_causal_effect(
    graph_def: dict[str, Any],
    df: pd.DataFrame,
    profile: CausalDatasetProfile,
) -> CausalEstimateReport:
```

## Step 1 — Gate Check

```python
gates_passed, gate_warnings = passes_estimation_gates(profile, df)
if not gates_passed:
    return CausalEstimateReport(
        method="withheld:data_quality_gates",
        ate=None, p_value=None, ...
    )
```

If gates fail, returns immediately with `ate=None`. The API/UI shows "insufficient data." This is not a bug.

## Step 2 — GML Graph Construction

DoWhy's `CausalModel` requires a GML string. `_build_gml()` converts graph_def into:
```
graph [
  directed 1
  node [id "Patch_Applied" label "Patch_Applied"]
  node [id "Lateral_Movement" label "Lateral_Movement"]
  edge [source "Patch_Applied" target "Lateral_Movement"]
]
```
Only nodes present in the dataframe columns are included. `clean_variable()` normalizes all variable names (spaces → underscores, lowercase) before this step.

## Step 3 — DoWhy Estimation

```python
model = dowhy.CausalModel(data=df, treatment=treatment, outcome=outcome, graph=gml_string)
identified_estimand = model.identify_effect(proceed_when_unidentifiable=False)
estimate = model.estimate_effect(
    identified_estimand,
    method_name="backdoor.linear_regression",
)
```

Uses backdoor adjustment with linear regression. If identification fails → `withheld:dowhy_identification_or_estimation_failed`.

## Step 4 — Statsmodels OLS Diagnostics

```python
stats = _linear_regression_stats(df, treatment, outcome, adjustment_set)
```

Runs `statsmodels.OLS` separately to get the treatment coefficient's `standard_error`, `p_value`, `ci_low`, `ci_high`. DoWhy gives the ATE estimate; statsmodels gives the inferential statistics reviewers ask for.

## Step 5 — Refuters

```python
refuters = _run_refuters(model, identified_estimand, estimate, ate)
```

Two refuters run:
- **Placebo treatment**: replaces treatment with random noise — ATE should become ~0
- **Data subset**: estimates on 80% subset — should be similar to full-data ATE

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

## Impact Confidence (in engine.py)

```python
def _impact_confidence(report):
    if ate is None:               return "insufficient_data"
    if refuted and p <= 0.05:     return "high"
    if p <= 0.1:                  return "medium"
    return "low"
```

## Refutation Loop

If `refutation_passed=False`, the coordinator's `_run_causal_loop` retries `causal_synthesis_node` to produce a revised DAG, then re-estimates. Stops when refuters pass or ATE is withheld. See [[pipeline/02-coordinator|Coordinator]].

## Related Notes

- [[causal-engine/02-evidence|Evidence Compiler]] — provides the dataframe
- [[causal-engine/01-discovery|Discovery]] — validates the DAG before this runs
- [[causal-engine/00-overview|Causal Engine Overview]] — ATE withholding is correct behavior
- [[infrastructure/01-api|API]] — `/estimate` and `/demo/estimate` call this directly
