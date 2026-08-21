---
type: community
members: 18
---

# Source Normalization

**Members:** 18 nodes

## Members
- [[Covers the fetch-normalize wiring in ingestionsources.py. requests.get is mock]] - rationale - tests/test_sources.py
- [[One company's board 404ingrenaming must not halt discovery for the     other se]] - rationale - tests/test_sources.py
- [[_ai_jobs_response()]] - code - tests/test_sources.py
- [[_ashby_response()]] - code - tests/test_sources.py
- [[_gh_response()]] - code - tests/test_sources.py
- [[test_fetch_ai_jobs_filters_to_intern_level_and_normalizes()]] - code - tests/test_sources.py
- [[test_fetch_ai_jobs_propagates_no_crash_on_failure()]] - code - tests/test_sources.py
- [[test_fetch_ashby_filters_to_structured_intern_employment_type()]] - code - tests/test_sources.py
- [[test_fetch_ashby_skips_a_dead_company_board_without_crashing()]] - code - tests/test_sources.py
- [[test_fetch_greenhouse_polls_every_seeded_company_and_filters_to_intern_titles()]] - code - tests/test_sources.py
- [[test_fetch_greenhouse_skips_a_dead_company_board_without_crashing()]] - code - tests/test_sources.py
- [[test_fetch_josegael_calls_correct_url_and_normalizes()]] - code - tests/test_sources.py
- [[test_fetch_simplify_calls_correct_url_and_normalizes()]] - code - tests/test_sources.py
- [[test_fetch_simplify_propagates_http_errors()]] - code - tests/test_sources.py
- [[test_fetch_vanshb03_calls_correct_url_and_normalizes()]] - code - tests/test_sources.py
- [[test_fetch_zshah101_handles_dict_shape_and_normalizes()]] - code - tests/test_sources.py
- [[test_sources.py]] - code - tests/test_sources.py
- [[zshah101's datajobs.json is a dict keyed by id, not a list — the only     sourc]] - rationale - tests/test_sources.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Source_Normalization
SORT file.name ASC
```
