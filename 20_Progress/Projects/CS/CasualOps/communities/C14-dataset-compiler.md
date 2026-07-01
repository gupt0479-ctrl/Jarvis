# C14 — Dataset Compiler

**Community 14** — 21 nodes, cohesion 0.15

The evidence-to-dataframe compiler. The statistical boundary between LLM hypotheses and estimation. DO NOT MODIFY `src/dataset_compiler.py`.

## Key Nodes

`clean_variable()`, `_coerce_float()`, `compile_evidence_dataset()`, `DatasetCompilation`, `_normalize_records()`, `passes_estimation_gates()`, `_profile_warnings()`

## What This Code Does

`compile_evidence_dataset()` takes a graph_def dict and evidence records, filters out synthetic records, maps each record to numeric values for each causal variable, and returns a `DatasetCompilation` with dataframe, quality profile, and provenance.

`passes_estimation_gates()` checks minimum row counts, treatment/control balance, and missingness before allowing DoWhy to run.

`clean_variable()` is used throughout the codebase to normalize variable names (spaces → underscores, lowercase) for pandas and DoWhy GML compatibility.

`_coerce_float()` handles the boolean/string/numeric coercion for evidence field values.

## Source File

`src/dataset_compiler.py` — **DO NOT MODIFY**

## Related Notes

- [[causal-engine/02-evidence|Evidence Compiler]] — full description with all constants and the synthetic guard
- [[communities/C16-dowhy-estimator|C16]] — consumes DatasetCompilation output
- [[communities/C07-causal-discovery|C07]] — also receives the compiled dataframe
