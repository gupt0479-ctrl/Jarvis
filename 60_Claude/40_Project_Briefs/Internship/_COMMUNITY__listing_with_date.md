---
type: community
members: 9
---

# _listing_with_date

**Members:** 9 nodes

## Members
- [[A bucket with 0 eligible candidates this run must not let another     bucket's i]] - rationale - tests/test_run_pipeline.py
- [[Task L integration two 'Other'-bucket candidates, non-preferred one     posted]] - rationale - tests/test_run_pipeline.py
- [[_listing_with_date()]] - code - tests/test_run_pipeline.py
- [[preferred_companies=None (the default) must reproduce the exact     pre-Task-L r]] - rationale - tests/test_run_pipeline.py
- [[test_prioritize_and_cap_keeps_most_recent_first()]] - code - tests/test_run_pipeline.py
- [[test_prioritize_and_cap_missing_date_posted_sorts_last()]] - code - tests/test_run_pipeline.py
- [[test_prioritize_and_cap_orders_preferred_company_first_within_bucket()]] - code - tests/test_run_pipeline.py
- [[test_prioritize_and_cap_scopes_budget_per_bucket()]] - code - tests/test_run_pipeline.py
- [[test_prioritize_and_cap_without_preferred_companies_keeps_recency_only_order()]] - code - tests/test_run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_listing_with_date
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_test_writer.py]]
- 3 edges to [[_COMMUNITY_normalize_simplify]]

## Top bridge nodes
- [[_listing_with_date()]] - degree 9, connects to 2 communities
- [[test_prioritize_and_cap_orders_preferred_company_first_within_bucket()]] - degree 3, connects to 1 community
- [[test_prioritize_and_cap_without_preferred_companies_keeps_recency_only_order()]] - degree 3, connects to 1 community
- [[test_prioritize_and_cap_scopes_budget_per_bucket()]] - degree 3, connects to 1 community
- [[test_prioritize_and_cap_keeps_most_recent_first()]] - degree 2, connects to 1 community