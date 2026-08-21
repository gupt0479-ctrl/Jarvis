---
type: community
members: 38
---

# Feed Schema-Drift Checks

**Members:** 38 nodes

## Members
- [[Exception]] - code
- [[Fixtures carry a test-only _case label; real upstream entries don't.]] - rationale - tests/test_schema_drift.py
- [[Runs every check in order; raises SchemaDriftError from whichever     fails firs]] - rationale - core/schema_drift.py
- [[Schema-drift check. Runs before the scheduled pipeline touches feeds for real f]] - rationale - core/schema_drift.py
- [[SchemaDriftError]] - code - core/schema_drift.py
- [[The one source shaped as a dict, not a list — a schema check that     assumed li]] - rationale - tests/test_schema_drift.py
- [[_check_json_source()]] - code - core/schema_drift.py
- [[_json_response()]] - code - tests/test_schema_drift.py
- [[_strip_case_keys()_1]] - code - tests/test_schema_drift.py
- [[_text_response()]] - code - tests/test_schema_drift.py
- [[category is read via .get() so a rename wouldn't crash the normalizer —     it w]] - rationale - tests/test_schema_drift.py
- [[check_all()]] - code - core/schema_drift.py
- [[check_josegael_schema()]] - code - core/schema_drift.py
- [[check_simplify_schema()]] - code - core/schema_drift.py
- [[check_vanshb03_schema()]] - code - core/schema_drift.py
- [[check_zshah101_schema()]] - code - core/schema_drift.py
- [[josegael_raw()]] - code - tests/test_schema_drift.py
- [[schema_drift.py]] - code - core/schema_drift.py
- [[simplify_raw()]] - code - tests/test_schema_drift.py
- [[test_check_all_passes_when_all_sources_are_healthy()]] - code - tests/test_schema_drift.py
- [[test_check_all_raises_on_first_failing_source()]] - code - tests/test_schema_drift.py
- [[test_josegael_schema_detects_dropped_permissive_field()]] - code - tests/test_schema_drift.py
- [[test_josegael_schema_detects_renamed_key()]] - code - tests/test_schema_drift.py
- [[test_josegael_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py
- [[test_schema_drift.py]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_detects_dropped_optional_field()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_detects_dropped_permissive_field()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_detects_empty_list()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_detects_renamed_key()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_detects_wrong_shape()]] - code - tests/test_schema_drift.py
- [[test_simplify_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py
- [[test_vanshb03_schema_detects_dropped_sponsorship_field()]] - code - tests/test_schema_drift.py
- [[test_vanshb03_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py
- [[test_zshah101_schema_detects_dropped_is_open_field()]] - code - tests/test_schema_drift.py
- [[test_zshah101_schema_detects_wrong_shape()]] - code - tests/test_schema_drift.py
- [[test_zshah101_schema_passes_on_real_shape()]] - code - tests/test_schema_drift.py
- [[vanshb03_raw()]] - code - tests/test_schema_drift.py
- [[zshah101_raw()]] - code - tests/test_schema_drift.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Feed_Schema-Drift_Checks
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Run Log & Weekly Rollup]]
- 3 edges to [[_COMMUNITY_Fetch, Dedup & Identity]]

## Top bridge nodes
- [[schema_drift.py]] - degree 12, connects to 2 communities
- [[SchemaDriftError]] - degree 7, connects to 2 communities
- [[check_all()]] - degree 11, connects to 1 community
- [[Exception]] - degree 2, connects to 1 community