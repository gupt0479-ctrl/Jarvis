---
type: community
members: 4
---

# stage1_reject

**Members:** 4 nodes

## Members
- [[Page markdown via Firecrawl (JS-rendered — ATS pages are SPAs).     Raises reque]] - rationale - ingestion/posting_page.py
- [[fetch_posting_markdown()]] - code - ingestion/posting_page.py
- [[test_fetch_posting_markdown_calls_firecrawl()]] - code - tests/test_posting_page.py
- [[test_fetch_posting_markdown_strips_ashby_application_suffix_before_calling_firecrawl()]] - code - tests/test_posting_page.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/stage1_reject
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_plan_removals]]
- 2 edges to [[_COMMUNITY_interndock.py]]
- 1 edge to [[_COMMUNITY_vault_root_1]]
- 1 edge to [[_COMMUNITY_recheck.py]]

## Top bridge nodes
- [[fetch_posting_markdown()]] - degree 9, connects to 4 communities
- [[test_fetch_posting_markdown_calls_firecrawl()]] - degree 2, connects to 1 community
- [[test_fetch_posting_markdown_strips_ashby_application_suffix_before_calling_firecrawl()]] - degree 2, connects to 1 community