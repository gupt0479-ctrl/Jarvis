---
type: community
members: 18
---

# test_interndock.py

**Members:** 18 nodes

## Members
- [[Firecrawl-fetches one candidate URL and parses it. Returns  both on     fetch]] - rationale - ingestion/interndock.py
- [[InternDock (interndock.com) — periodic drop guide posts, not a JSON feed.  Che]] - rationale - ingestion/interndock.py
- [[Real case, confirmed live 2026-08-24 'summer-2027-internship-programs-open-now']] - rationale - tests/test_interndock.py
- [[Real verbatim content (WebFetch, 2026-08-24) — the first 15 entries of     inter]] - rationale - tests/test_interndock.py
- [[Real, live guide URLs from the sitemap whose slug loosely looks     drop-shaped.]] - rationale - ingestion/interndock.py
- [[Real, live-verified InternDock fixtures (2026-08-24, Task 3) — no live network c]] - rationale - tests/test_interndock.py
- [[{title, url, company, location}, ... from a fetched drop page's     markdown.]] - rationale - ingestion/interndock.py
- [[fetch_interndock_drop()]] - code - ingestion/interndock.py
- [[fetch_interndock_drop_candidates()]] - code - ingestion/interndock.py
- [[interndock.py]] - code - ingestion/interndock.py
- [[parse_interndock_postings()]] - code - ingestion/interndock.py
- [[test_fetch_interndock_drop_candidates_loosely_filters_sitemap()]] - code - tests/test_interndock.py
- [[test_fetch_interndock_drop_fails_open_on_firecrawl_error()]] - code - tests/test_interndock.py
- [[test_fetch_interndock_drop_returns_empty_when_below_threshold()]] - code - tests/test_interndock.py
- [[test_fetch_interndock_drop_returns_postings_above_threshold()]] - code - tests/test_interndock.py
- [[test_interndock.py]] - code - tests/test_interndock.py
- [[test_parse_interndock_postings_ignores_non_matching_lines()]] - code - tests/test_interndock.py
- [[test_parse_interndock_postings_real_fixture()]] - code - tests/test_interndock.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_interndockpy
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_fetch_posting_markdown]]
- 1 edge to [[_COMMUNITY_posting_page.py]]

## Top bridge nodes
- [[interndock.py]] - degree 7, connects to 2 communities
- [[fetch_interndock_drop()]] - degree 8, connects to 1 community