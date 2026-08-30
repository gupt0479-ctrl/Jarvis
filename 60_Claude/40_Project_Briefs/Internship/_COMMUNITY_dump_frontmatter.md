---
type: community
members: 6
---

# dump_frontmatter

**Members:** 6 nodes

## Members
- [[Real Optiver 'Quantitative Research Intern, PhD (Summer 2027)'     (Greenhouse j]] - rationale - tests/test_posting_page.py
- [[The matched PhD-exclusivity phrase, or None if the posting shows no     explicit]] - rationale - ingestion/posting_page.py
- [[phd_only_exclusion()]] - code - ingestion/posting_page.py
- [[test_phd_only_exclusion_does_not_reject_bachelors_masters_eligible_real_text()]] - code - tests/test_posting_page.py
- [[test_phd_only_exclusion_rejects_explicit_equivalent_phrasing()]] - code - tests/test_posting_page.py
- [[test_phd_only_exclusion_rejects_real_optiver_text()]] - code - tests/test_posting_page.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/dump_frontmatter
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_plan_removals]]
- 1 edge to [[_COMMUNITY_vault_root_1]]
- 1 edge to [[_COMMUNITY_recheck.py]]
- 1 edge to [[_COMMUNITY__fake_http_get_only_interndock]]

## Top bridge nodes
- [[phd_only_exclusion()]] - degree 8, connects to 4 communities
- [[test_phd_only_exclusion_rejects_real_optiver_text()]] - degree 3, connects to 1 community
- [[test_phd_only_exclusion_does_not_reject_bachelors_masters_eligible_real_text()]] - degree 2, connects to 1 community
- [[test_phd_only_exclusion_rejects_explicit_equivalent_phrasing()]] - degree 2, connects to 1 community