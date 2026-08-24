---
type: community
members: 16
---

# test_posting_page.py

**Members:** 16 nodes

## Members
- [[OPT signals and content extraction — every eligibility string below marked 'real]] - rationale - tests/test_posting_page.py
- [[Real bug, confirmed live 2026-07-26 the same CTGT posting returned     4015 cha]] - rationale - tests/test_posting_page.py
- [[Real listing.url shape stored on every AIJobs-sourced Zipline dossier     ('Aero]] - rationale - tests/test_posting_page.py
- [[The URL to actually fetch for posting content — rewrites known     board-index-o]] - rationale - ingestion/posting_page.py
- [[The matched exclusion phrase, or None if the posting shows no explicit     negat]] - rationale - ingestion/posting_page.py
- [[_content_fetch_url()]] - code - ingestion/posting_page.py
- [[opt_exclusion()]] - code - ingestion/posting_page.py
- [[test_content_fetch_url_leaves_ashby_non_application_urls_alone()]] - code - tests/test_posting_page.py
- [[test_content_fetch_url_leaves_non_ashby_urls_alone()]] - code - tests/test_posting_page.py
- [[test_content_fetch_url_leaves_zipline_path_urls_alone()]] - code - tests/test_posting_page.py
- [[test_content_fetch_url_leaves_zipline_urls_without_job_id_alone()]] - code - tests/test_posting_page.py
- [[test_content_fetch_url_rewrites_real_zipline_query_url_to_path_form()]] - code - tests/test_posting_page.py
- [[test_content_fetch_url_strips_ashby_application_suffix()]] - code - tests/test_posting_page.py
- [[test_explicit_negative_signals_exclude()]] - code - tests/test_posting_page.py
- [[test_non_signals_stay_eligible()]] - code - tests/test_posting_page.py
- [[test_posting_page.py]] - code - tests/test_posting_page.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_posting_pagepy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_writer.py]]
- 4 edges to [[_COMMUNITY_fetch_posting_markdown]]
- 4 edges to [[_COMMUNITY_phd_only_exclusion]]
- 3 edges to [[_COMMUNITY_posting_page.py]]
- 1 edge to [[_COMMUNITY_recheck.py]]
- 1 edge to [[_COMMUNITY_render_dossier]]

## Top bridge nodes
- [[test_posting_page.py]] - degree 29, connects to 4 communities
- [[opt_exclusion()]] - degree 7, connects to 3 communities
- [[_content_fetch_url()]] - degree 10, connects to 2 communities