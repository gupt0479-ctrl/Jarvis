---
type: community
members: 49
---

# writer.py

**Members:** 49 nodes

## Members
- [[A posting with no stated section names at all must not have section     boundari]] - rationale - tests/test_posting_page.py
- [[Discovery-time posting-page fetch one Firecrawl call per NEW match serves both]] - rationale - ingestion/posting_page.py
- [[Drops a paragraph line that repeats verbatim later in the same fetch,     keepin]] - rationale - ingestion/posting_page.py
- [[OPT signals and content extraction — every eligibility string below marked 'real]] - rationale - tests/test_posting_page.py
- [[Page markdown via Firecrawl (JS-rendered — ATS pages are SPAs).     Raises reque]] - rationale - ingestion/posting_page.py
- [[Real CTGT posting (jobs.ashbyhq.com), fetched 2026-07-26 — confirms the     full]] - rationale - tests/test_posting_page.py
- [[Real Optiver 'Quantitative Research Intern, PhD (Summer 2027)'     (Greenhouse j]] - rationale - tests/test_posting_page.py
- [[Real bug, confirmed 2026-07-26 on both Google dossiers sourced via     Freehire]] - rationale - tests/test_posting_page.py
- [[Real bug, confirmed live 2026-07-26 the same CTGT posting returned     4015 cha]] - rationale - tests/test_posting_page.py
- [[Real bug the Conagra Brands 'Demand Science Rotational Analyst'     fixture has]] - rationale - tests/test_posting_page.py
- [[Real fetched content, verbatim from three separate live Zipline     dossiers ('A]] - rationale - tests/test_posting_page.py
- [[Real listing.url shape stored on every AIJobs-sourced Zipline dossier     ('Aero]] - rationale - tests/test_posting_page.py
- [[Real shape from the AppianConagra fixtures a fully-bolded standalone     line]] - rationale - tests/test_posting_page.py
- [[Real the Manhattan Associates 'A.I. Developer Co-Op' fixture ends     with a 'R]] - rationale - tests/test_posting_page.py
- [[The URL to actually fetch for posting content — rewrites known     board-index-o]] - rationale - ingestion/posting_page.py
- [[The matched PhD-exclusivity phrase, or None if the posting shows no     explicit]] - rationale - ingestion/posting_page.py
- [[The matched exclusion phrase, or None if the posting shows no explicit     negat]] - rationale - ingestion/posting_page.py
- [[The posting's substantive text from the first real heading up to the     applic]] - rationale - ingestion/posting_page.py
- [[_content_fetch_url()]] - code - ingestion/posting_page.py
- [[_dedupe_paragraphs()]] - code - ingestion/posting_page.py
- [[_strip_trailing_social_chrome()]] - code - ingestion/posting_page.py
- [[extract_content()]] - code - ingestion/posting_page.py
- [[fetch_posting_markdown()]] - code - ingestion/posting_page.py
- [[opt_exclusion()]] - code - ingestion/posting_page.py
- [[phd_only_exclusion()]] - code - ingestion/posting_page.py
- [[posting_page.py]] - code - ingestion/posting_page.py
- [[test_content_fetch_url_leaves_ashby_non_application_urls_alone()]] - code - tests/test_posting_page.py
- [[test_content_fetch_url_leaves_non_ashby_urls_alone()]] - code - tests/test_posting_page.py
- [[test_content_fetch_url_leaves_zipline_path_urls_alone()]] - code - tests/test_posting_page.py
- [[test_content_fetch_url_leaves_zipline_urls_without_job_id_alone()]] - code - tests/test_posting_page.py
- [[test_content_fetch_url_rewrites_real_zipline_query_url_to_path_form()]] - code - tests/test_posting_page.py
- [[test_content_fetch_url_strips_ashby_application_suffix()]] - code - tests/test_posting_page.py
- [[test_explicit_negative_signals_exclude()]] - code - tests/test_posting_page.py
- [[test_extract_content_dedupes_repeated_paragraph_real_conagra_case()]] - code - tests/test_posting_page.py
- [[test_extract_content_from_real_ashby_page()]] - code - tests/test_posting_page.py
- [[test_extract_content_from_real_page()]] - code - tests/test_posting_page.py
- [[test_extract_content_renders_real_section_names_as_headings()]] - code - tests/test_posting_page.py
- [[test_extract_content_skips_google_careers_listing_shell()]] - code - tests/test_posting_page.py
- [[test_extract_content_splits_ats_chrome_run_ons_real_conagra_case()]] - code - tests/test_posting_page.py
- [[test_extract_content_strips_read_more_and_follow_us_chrome_real_manhattan_case()]] - code - tests/test_posting_page.py
- [[test_extract_content_treats_real_zipline_board_index_as_unconfirmed()]] - code - tests/test_posting_page.py
- [[test_extract_content_with_no_internal_structure_stays_one_block()]] - code - tests/test_posting_page.py
- [[test_fetch_posting_markdown_calls_firecrawl()]] - code - tests/test_posting_page.py
- [[test_fetch_posting_markdown_strips_ashby_application_suffix_before_calling_firecrawl()]] - code - tests/test_posting_page.py
- [[test_non_signals_stay_eligible()]] - code - tests/test_posting_page.py
- [[test_phd_only_exclusion_does_not_reject_bachelors_masters_eligible_real_text()]] - code - tests/test_posting_page.py
- [[test_phd_only_exclusion_rejects_explicit_equivalent_phrasing()]] - code - tests/test_posting_page.py
- [[test_phd_only_exclusion_rejects_real_optiver_text()]] - code - tests/test_posting_page.py
- [[test_posting_page.py]] - code - tests/test_posting_page.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/writerpy
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_recheck.py]]

## Top bridge nodes
- [[extract_content()]] - degree 16, connects to 1 community
- [[posting_page.py]] - degree 10, connects to 1 community
- [[phd_only_exclusion()]] - degree 8, connects to 1 community
- [[opt_exclusion()]] - degree 7, connects to 1 community
- [[fetch_posting_markdown()]] - degree 7, connects to 1 community