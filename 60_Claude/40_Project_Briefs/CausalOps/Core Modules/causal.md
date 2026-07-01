---
tags: [causalops, causal, dag, dowhy, hypothesis]
aliases: [causal.py]
---

# causal.py — Causal Synthesis & DoWhy Engine

`src/causal.py` contains two LangGraph nodes that are the heart of the causal pipeline:
1. `causal_synthesis_node` — LLM-powered DAG design (hypothesis only, no data)
2. `dowhy_engine_node` — deterministic evidence compilation + estimation

## causal_synthesis_node

**Responsibility:** Ask the LLM to design a measurable causal DAG and evidence measurement plan.

**LLM prompt role:** "You are a Causal Hypothesis Architect for cyber operations. Construct a causal DAG, define exactly ONE treatment_variable and ONE outcome_variable, list candidate_confounders, and produce a measurement_plan. Do NOT generate dataset rows. For every important edge, include confirming evidence and falsifying evidence."

**Key constraint on the LLM:** The chain is wired to output `CausalPayload` — a Pydantic model that has no rows, no numeric data, only graph structure and measurement instructions.

**Demo path:** If `is_demo_evidence(evidence_records)` is True (no caller evidence provided), the node uses `demo_causal_payload()` from `demo_fixtures.py` instead of calling the LLM.

**Returns:**
```python
{"causal_payload": payload_dict, "causal_refutation_passed": False}
```

## dowhy_engine_node

**Responsibility:** Compile evidence, validate the DAG against data, run DoWhy, publish results.

**Steps inside this node:**
1. `compile_evidence_dataset(graph_def, evidence_records)` → DatasetCompilation
2. `discover_and_validate(df, graph_def["edges"])` → DiscoveryResult (PC algorithm)
3. `apply_discovery(graph_def, discovery)` → validated_graph (refuted edges removed)
4. `estimation_edges(validated_graph)` → edges with only confirmed/compatible/reversed (not discovered)
5. `estimate_causal_effect(estimation_graph, df, profile)` → CausalEstimateReport
6. If refuted edges found, logs them and proceeds with validated graph
7. Re-publishes causal_payload with validated graph so 5D KG updates edge statuses

**Returns:**
```python
{
    "causal_payload": validated_payload,        # graph with refuted edges removed
    "causal_discovery_report": discovery_dict,
    "dowhy_results": legacy_results,            # legacy format for backward compat
    "causal_estimate_report": report_dict,
    "causal_dataset_profile": compilation.profile.model_dump(),
    "causal_refutation_passed": report.refutation_passed,
    "causal_refutation_attempts": attempts,
}
```

## Graph Sanitization (_sanitize_graph)

Before any estimation, the graph definition is normalized:
- Variable names: `clean_variable()` → strip spaces, replace with `_`, lowercase
- Missing nodes auto-injected as placeholders for any referenced ID
- `treatment_variable` and `outcome_variable` coerced to clean format

This prevents DoWhy failures from whitespace or casing inconsistencies in LLM output.

## Demo Evidence Detection

```python
if is_demo_evidence(evidence_records):
    # Use bundled fixture, skip LLM call
    payload_dict = demo_causal_payload()
```

A run is using demo evidence when: no evidence records provided OR all records have `source_type: "synthetic"`.

## Refutation Loop Integration

The `conditional_refutation_check` in `graph.py` checks `causal_refutation_passed`. If False and attempts < limit, the loop returns to `causal_synthesis` for another try. The coordinator's `_run_causal_loop` uses the same logic.

## Related Notes

- [[causal_discovery]] — PC-algorithm validation called inside dowhy_engine_node
- [[dataset_compiler]] — Compiles evidence records into the dataframe
- [[estimators]] — Runs DoWhy and statsmodels
- [[demo_fixtures]] — Demo causal payload and evidence
- [[schema]] — CausalPayload, CausalGraphDef models
