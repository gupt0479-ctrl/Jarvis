---
type: community
members: 74
---

# Layer 1 Eligibility Filter

**Members:** 74 nodes

## Members
- [[Bare, year-less Spring stays ambiguous (could be excluded Spring 2026     or w]] - rationale - tests/test_filter.py
- [[Does Not Offer Sponsorship' means no H-1B, not no OPT — same rule as     everywh]] - rationale - tests/test_filter.py
- [[Guards against silent test evaporation pytest.mark.parametrize collects     zer]] - rationale - tests/test_filter.py
- [[Layer 2 — pure field matching against each feed's own schema. No LLM, determinis]] - rationale - core/filter.py
- [[Listing]] - code - ingestion/normalize.py
- [[Map each source's raw shape to one internal Listing dataclass.]] - rationale - ingestion/normalize.py
- [[Permissive like locations no degrees data passes; non-empty data must     inclu]] - rationale - core/filter.py
- [[Real case Ellipsis Labs' live 'Software Engineer - 2027 Interns' posting     ne]] - rationale - tests/test_filter.py
- [[Real case Marshall Wace's live 'Technology Intern - 2027' postings state     th]] - rationale - tests/test_filter.py
- [[Real record, fetched 2026-07-25 Databricks 'Product Management Intern     (Summ]] - rationale - tests/test_filter.py
- [[Regression for the _has_wrong_cycle_season bug a year-qualified season     (Sp]] - rationale - tests/test_filter.py
- [[_entry_is_us_or_remote()]] - code - core/filter.py
- [[_has_wrong_cycle_season()]] - code - core/filter.py
- [[_load()]] - code - tests/test_filter.py
- [[_matches_free_text_source()]] - code - core/filter.py
- [[_matches_josegael()]] - code - core/filter.py
- [[_matches_simplify()]] - code - core/filter.py
- [[_matches_vanshb03()]] - code - core/filter.py
- [[_matches_zshah101()]] - code - core/filter.py
- [[_norm()]] - code - core/filter.py
- [[_parse_iso_ts()]] - code - ingestion/normalize.py
- [[_strip_html()]] - code - ingestion/normalize.py
- [[_target_years()]] - code - core/filter.py
- [[_text_has_any()]] - code - core/filter.py
- [[degrees_eligible()]] - code - core/filter.py
- [[filter.py]] - code - core/filter.py
- [[location_eligible()]] - code - core/filter.py
- [[matches()]] - code - core/filter.py
- [[normalize.py]] - code - ingestion/normalize.py
- [[normalize_ai_jobs()]] - code - ingestion/normalize.py
- [[normalize_ashby()]] - code - ingestion/normalize.py
- [[normalize_greenhouse()]] - code - ingestion/normalize.py
- [[normalize_josegael()]] - code - ingestion/normalize.py
- [[normalize_vanshb03()]] - code - ingestion/normalize.py
- [[normalize_zshah101()]] - code - ingestion/normalize.py
- [[test_active_false_rejects_any_source()]] - code - tests/test_filter.py
- [[test_ashby_bare_year_real_ellipsis_labs_case_passes()]] - code - tests/test_filter.py
- [[test_ashby_matches_literal_term_in_description()]] - code - tests/test_filter.py
- [[test_ashby_matches_spring_2027_literal_term()]] - code - tests/test_filter.py
- [[test_degrees_eligible()]] - code - tests/test_filter.py
- [[test_filter.py]] - code - tests/test_filter.py
- [[test_fixture_has_both_match_and_reject_cases()]] - code - tests/test_filter.py
- [[test_greenhouse_bare_wrong_year_with_no_right_year_rejects()]] - code - tests/test_filter.py
- [[test_greenhouse_bare_year_with_no_season_word_passes_permissively()]] - code - tests/test_filter.py
- [[test_greenhouse_matches_literal_term_in_title()]] - code - tests/test_filter.py
- [[test_greenhouse_matches_spring_2027_literal_term()]] - code - tests/test_filter.py
- [[test_greenhouse_rejects_explicit_wrong_year_in_content()]] - code - tests/test_filter.py
- [[test_josegael_bare_spring_still_rejects()]] - code - tests/test_filter.py
- [[test_josegael_matches_year_qualified_spring_2027()]] - code - tests/test_filter.py
- [[test_josegael_season_rejects_wrong_cycles_real_entries()]] - code - tests/test_filter.py
- [[test_josegael_should_match()]] - code - tests/test_filter.py
- [[test_josegael_should_reject()]] - code - tests/test_filter.py
- [[test_josegael_whitespace_only_season_does_not_crash()]] - code - tests/test_filter.py
- [[test_josegael_yearless_summer_passes_real_mlh_entry()]] - code - tests/test_filter.py
- [[test_location_affirmatively_foreign_is_rejected()]] - code - tests/test_filter.py
- [[test_location_no_data_is_unrestricted()]] - code - tests/test_filter.py
- [[test_location_one_us_entry_among_foreign_is_enough()]] - code - tests/test_filter.py
- [[test_location_us_or_ambiguous_is_eligible()]] - code - tests/test_filter.py
- [[test_matches_rejects_foreign_only_listing_end_to_end()]] - code - tests/test_filter.py
- [[test_normalize_ai_jobs_maps_fields_and_matches_real_intern_record()]] - code - tests/test_filter.py
- [[test_normalize_ashby_maps_fields()]] - code - tests/test_filter.py
- [[test_normalize_greenhouse_strips_html_and_maps_fields()]] - code - tests/test_filter.py
- [[test_simplify_matches_spring_2027_only()]] - code - tests/test_filter.py
- [[test_simplify_should_match()]] - code - tests/test_filter.py
- [[test_simplify_should_reject()]] - code - tests/test_filter.py
- [[test_terms_weight_present_and_correct()]] - code - tests/test_filter.py
- [[test_vanshb03_bare_spring_still_rejects()]] - code - tests/test_filter.py
- [[test_vanshb03_no_sponsorship_is_not_an_exclusion()]] - code - tests/test_filter.py
- [[test_vanshb03_should_match()]] - code - tests/test_filter.py
- [[test_vanshb03_should_reject()]] - code - tests/test_filter.py
- [[test_zshah101_citizens_only_real_anduril_entry()]] - code - tests/test_filter.py
- [[test_zshah101_matches_spring_2027()]] - code - tests/test_filter.py
- [[test_zshah101_should_match()]] - code - tests/test_filter.py
- [[test_zshah101_should_reject()]] - code - tests/test_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Layer_1_Eligibility_Filter
SORT file.name ASC
```

## Connections to other communities
- 18 edges to [[_COMMUNITY_Run Log & Weekly Rollup]]
- 10 edges to [[_COMMUNITY_normalize_simplify]]
- 9 edges to [[_COMMUNITY_Priority-Bucket Classification]]
- 9 edges to [[_COMMUNITY_Freehire Ingestion Source]]
- 6 edges to [[_COMMUNITY_Cross-Source Identity Keys]]
- 4 edges to [[_COMMUNITY_Fetch, Dedup & Identity]]
- 3 edges to [[_COMMUNITY_test_debate_losses.py]]
- 1 edge to [[_COMMUNITY_CSSoftware Relevance Gate]]
- 1 edge to [[_COMMUNITY_Write-Gate Validation Tests]]
- 1 edge to [[_COMMUNITY_Dossier Writer (Vault Output)]]

## Top bridge nodes
- [[normalize.py]] - degree 24, connects to 10 communities
- [[Listing]] - degree 24, connects to 5 communities
- [[filter.py]] - degree 21, connects to 5 communities
- [[normalize_josegael()]] - degree 18, connects to 4 communities
- [[test_filter.py]] - degree 54, connects to 2 communities