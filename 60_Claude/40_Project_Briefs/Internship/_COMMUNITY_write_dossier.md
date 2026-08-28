---
type: community
members: 91
---

# write_dossier

**Members:** 91 nodes

## Members
- [[ApplyGuy's own literal placeholder on real entries with no season data     (782]] - rationale - tests/test_filter.py
- [[Bare, year-less Spring stays ambiguous (could be excluded Spring 2026     or w]] - rationale - tests/test_filter.py
- [[Does Not Offer Sponsorship' means no H-1B, not no OPT — same rule as     everywh]] - rationale - tests/test_filter.py
- [[Fetch raw listings from each source. Used both by the scheduled pipeline and (wi]] - rationale - ingestion/sources.py
- [[Guards against silent test evaporation pytest.mark.parametrize collects     zer]] - rationale - tests/test_filter.py
- [[Listing]] - code - ingestion/normalize.py
- [[Map each source's raw shape to one internal Listing dataclass.]] - rationale - ingestion/normalize.py
- [[Permissive like locations no degrees data passes; non-empty data must     inclu]] - rationale - core/filter.py
- [[Real case Belvedere Trading's live 'Quantitative Trading Intern -     Summer 20]] - rationale - tests/test_filter.py
- [[Real case Ellipsis Labs' live 'Software Engineer - 2027 Interns' posting     ne]] - rationale - tests/test_filter.py
- [[Real case Marshall Wace's live 'Technology Intern - 2027' postings state     th]] - rationale - tests/test_filter.py
- [[Real record, fetched 2026-07-25 Databricks 'Product Management Intern     (Summ]] - rationale - tests/test_filter.py
- [[Regression for the _has_wrong_cycle_season bug a year-qualified season     (Sp]] - rationale - tests/test_filter.py
- [[The bare-city fallback added for 'London' alone must be an exact     whole-strin]] - rationale - tests/test_filter.py
- [[_load()]] - code - tests/test_filter.py
- [[_matches_josegael()]] - code - core/filter.py
- [[_parse_iso_ts()]] - code - ingestion/normalize.py
- [[_strip_html()]] - code - ingestion/normalize.py
- [[degrees_eligible()]] - code - core/filter.py
- [[fetch_ai_jobs()]] - code - ingestion/sources.py
- [[fetch_applyguy()]] - code - ingestion/sources.py
- [[fetch_ashby()]] - code - ingestion/sources.py
- [[fetch_greenhouse()]] - code - ingestion/sources.py
- [[fetch_josegael()]] - code - ingestion/sources.py
- [[fetch_lever()]] - code - ingestion/sources.py
- [[fetch_simplify()]] - code - ingestion/sources.py
- [[fetch_vanshb03()]] - code - ingestion/sources.py
- [[fetch_zshah101()]] - code - ingestion/sources.py
- [[location_eligible()]] - code - core/filter.py
- [[matches()]] - code - core/filter.py
- [[normalize.py]] - code - ingestion/normalize.py
- [[normalize_ai_jobs()]] - code - ingestion/normalize.py
- [[normalize_applyguy()]] - code - ingestion/normalize.py
- [[normalize_ashby()]] - code - ingestion/normalize.py
- [[normalize_greenhouse()]] - code - ingestion/normalize.py
- [[normalize_josegael()]] - code - ingestion/normalize.py
- [[normalize_lever()]] - code - ingestion/normalize.py
- [[normalize_vanshb03()]] - code - ingestion/normalize.py
- [[normalize_zshah101()]] - code - ingestion/normalize.py
- [[recheck.py]] - code - recheck.py
- [[sources.py]] - code - ingestion/sources.py
- [[test_active_false_rejects_any_source()]] - code - tests/test_filter.py
- [[test_applyguy_not_specified_season_maps_to_no_term_data()]] - code - tests/test_filter.py
- [[test_applyguy_prefers_listing_url_over_tracking_url()]] - code - tests/test_filter.py
- [[test_applyguy_should_match()]] - code - tests/test_filter.py
- [[test_applyguy_should_reject()]] - code - tests/test_filter.py
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
- [[test_lever_bare_year_with_no_season_word_passes_permissively()]] - code - tests/test_filter.py
- [[test_lever_matches_literal_term_in_description()]] - code - tests/test_filter.py
- [[test_lever_rejects_explicit_wrong_year()]] - code - tests/test_filter.py
- [[test_location_affirmatively_foreign_is_rejected()]] - code - tests/test_filter.py
- [[test_location_new_london_ct_is_not_caught_by_bare_london_fallback()]] - code - tests/test_filter.py
- [[test_location_no_data_is_unrestricted()]] - code - tests/test_filter.py
- [[test_location_one_us_entry_among_foreign_is_enough()]] - code - tests/test_filter.py
- [[test_location_us_or_ambiguous_is_eligible()]] - code - tests/test_filter.py
- [[test_matches_rejects_foreign_only_listing_end_to_end()]] - code - tests/test_filter.py
- [[test_normalize_ai_jobs_maps_fields_and_matches_real_intern_record()]] - code - tests/test_filter.py
- [[test_normalize_ashby_maps_fields()]] - code - tests/test_filter.py
- [[test_normalize_greenhouse_strips_html_and_maps_fields()]] - code - tests/test_filter.py
- [[test_normalize_lever_falls_back_to_hosted_url_when_no_apply_url()]] - code - tests/test_filter.py
- [[test_normalize_lever_maps_fields_and_prefers_apply_url()]] - code - tests/test_filter.py
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
- [[url is applyguy.ai's own utm-tagged redirect page; listingUrl is the     real em]] - rationale - tests/test_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/write_dossier
SORT file.name ASC
```

## Connections to other communities
- 20 edges to [[_COMMUNITY_test_freehire.py]]
- 18 edges to [[_COMMUNITY_recheck.py]]
- 13 edges to [[_COMMUNITY_normalize_simplify]]
- 10 edges to [[_COMMUNITY_commit_and_push_with_retry]]
- 8 edges to [[_COMMUNITY_test_write_dossier_creates_missing_dossiers_dir]]
- 5 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 4 edges to [[_COMMUNITY_test_debate_losses.py]]
- 4 edges to [[_COMMUNITY_build_frontmatter]]
- 3 edges to [[_COMMUNITY_validate.py]]
- 2 edges to [[_COMMUNITY_interndock.py]]
- 2 edges to [[_COMMUNITY_test_writer.py]]
- 2 edges to [[_COMMUNITY__fake_http_get_only_interndock]]
- 1 edge to [[_COMMUNITY_vault_root]]
- 1 edge to [[_COMMUNITY_test_write_dossier_different_uid_same_role_company_gets_collision_suffix]]
- 1 edge to [[_COMMUNITY_render_dossier]]

## Top bridge nodes
- [[normalize.py]] - degree 28, connects to 11 communities
- [[Listing]] - degree 34, connects to 8 communities
- [[recheck.py]] - degree 25, connects to 4 communities
- [[test_filter.py]] - degree 66, connects to 3 communities
- [[sources.py]] - degree 23, connects to 3 communities