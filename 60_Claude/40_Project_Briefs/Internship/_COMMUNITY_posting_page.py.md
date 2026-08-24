---
type: community
members: 5
---

# posting_page.py

**Members:** 5 nodes

## Members
- [[Discovery-time posting-page fetch one Firecrawl call per NEW match serves both]] - rationale - ingestion/posting_page.py
- [[Drops a paragraph line that repeats verbatim later in the same fetch,     keepin]] - rationale - ingestion/posting_page.py
- [[_dedupe_paragraphs()]] - code - ingestion/posting_page.py
- [[_strip_trailing_social_chrome()]] - code - ingestion/posting_page.py
- [[posting_page.py]] - code - ingestion/posting_page.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/posting_pagepy
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_test_posting_page.py]]
- 3 edges to [[_COMMUNITY_writer.py]]
- 1 edge to [[_COMMUNITY_test_interndock.py]]
- 1 edge to [[_COMMUNITY_fetch_posting_markdown]]
- 1 edge to [[_COMMUNITY_phd_only_exclusion]]
- 1 edge to [[_COMMUNITY_recheck.py]]

## Top bridge nodes
- [[posting_page.py]] - degree 11, connects to 6 communities
- [[_dedupe_paragraphs()]] - degree 3, connects to 1 community
- [[_strip_trailing_social_chrome()]] - degree 2, connects to 1 community