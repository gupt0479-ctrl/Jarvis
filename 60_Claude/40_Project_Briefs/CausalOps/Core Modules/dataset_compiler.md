---
tags: [causalops, evidence, compiler, dataframe, statistics, DO-NOT-TOUCH]
aliases: [dataset_compiler.py]
---

# dataset_compiler.py — Evidence → Dataframe Compiler

> ⚠️ **DO NOT MODIFY.** This file is the statistical safeguard. Changing it without deep understanding of the evidence boundary can break the LLM-evidence separation.

`src/dataset_compiler.py` is the critical boundary between LLM-authored hypotheses and statistical estimation. It accepts a graph definition plus normalized evidence records, and produces a numeric dataframe, row-level provenance, and quality gates.

## Statistical Gates

```python
MIN_COMPLETE_ROWS = 50           # minimum observation rows for estimation
RECOMMENDED_COMPLETE_ROWS = 200  # recommended for stable estimates
MIN_TREATMENT_GROUP_ROWS = 10    # minimum rows in both treated and control groups
```

If these gates fail, `passes_estimation_gates()` returns `(False, warnings)` and the estimator withholds ATE.

## DatasetCompilation (Output)

```python
@dataclass
class DatasetCompilation:
    dataframe: pd.DataFrame            # numeric rows, one per evidence observation
    profile: CausalDatasetProfile      # quality metrics and metadata
    provenance: list[dict[str, Any]]   # row-level source traceability
```

Each provenance row records: `asset_id`, `observed_at`, `source_type`, `source_name`, `raw_ref`, and which variables were found vs missing.

## compile_evidence_dataset() — Main Entry Point

```python
def compile_evidence_dataset(
    graph_def: dict[str, Any],
    evidence_records: list[dict[str, Any]],
) -> DatasetCompilation:
```

Steps:
1. Extract `treatment`, `outcome`, `candidate_confounders` from graph_def
2. Filter out `source_type: "synthetic"` records
3. For each record, look up numeric values for each variable via `_variable_lookup()`
4. Build a row if at least treatment OR outcome has a value
5. Coerce all values to float via `_coerce_float()`
6. Build pandas DataFrame (one row per evidence record that had data)
7. Apply missingness rules: drop rows with missing treatment or outcome
8. Build `CausalDatasetProfile` with counts, missingness ratios, warnings
9. Return `DatasetCompilation`

## Variable Lookup Priority (_variable_lookup)

For each variable, searches `extracted_fields` dict keys using:
1. Exact match on variable name
2. Case-insensitive match
3. Normalized match (spaces → underscores, lowercase)
4. `raw_text` float parsing as fallback

## Synthetic Record Guard

```python
# Records with source_type == "synthetic" are SKIPPED:
if record.source_type == "synthetic":
    continue
```

This is the primary safeguard. LLM-generated synthetic records cannot pass through the compiler to reach the estimator.

## clean_variable() — Used Everywhere

```python
def clean_variable(value: str) -> str:
    return value.strip().replace(" ", "_").replace("-", "_")
```

Used in both compiler and `causal.py._sanitize_graph()` to normalize variable names for pandas column compatibility and DoWhy's GML parser.

## _coerce_float() — Type Normalization

Handles boolean, numeric, and string evidence values:
```python
"true"/"yes"/"present"/"detected"/"treated" → 1.0
"false"/"no"/"absent"/"clean"/"control"     → 0.0
numeric strings → float(value)
None or ""   → None (missing)
```

## passes_estimation_gates()

Checks:
- `n_rows >= MIN_COMPLETE_ROWS`
- `treated_count >= MIN_TREATMENT_GROUP_ROWS`
- `control_count >= MIN_TREATMENT_GROUP_ROWS`
- Treatment column has variation (not all-0 or all-1)
- Outcome column has variation
- Missingness per column below threshold

Returns `(bool, list[str])` — gate pass/fail and warning messages.

## Related Notes

- [[estimators]] — Consumes the DatasetCompilation output
- [[causal]] — Calls compile_evidence_dataset from dowhy_engine_node
- [[causal_discovery]] — Also receives the compiled dataframe for independence testing
- [[schema]] — EvidenceRecord and CausalDatasetProfile models
- [[evidence_adapters]] — Normalizes external records before they reach the compiler
- [[demo_fixtures]] — Provides the smoke-test evidence that bypasses real data needs
