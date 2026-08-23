---
type: community
members: 27
---

# test_freehire.py

**Members:** 27 nodes

## Members
- [[Checks freehire's own company mapping before ever guessing a token     ourselves]] - rationale - ingestion/freehire.py
- [[Map each source's raw shape to one internal Listing dataclass.]] - rationale - ingestion/normalize.py
- [[Real and correct Nuro's actual freehire record never states a year in     title]] - rationale - tests/test_freehire.py
- [[The literal miss this whole investigation started from — confirmed     reachable]] - rationale - tests/test_freehire.py
- [[_by_case()]] - code - tests/test_freehire.py
- [[_load()_1]] - code - tests/test_freehire.py
- [[_parse_iso_ts()]] - code - ingestion/normalize.py
- [[_search_response()]] - code - tests/test_freehire.py
- [[_strip_html()]] - code - ingestion/normalize.py
- [[fetch_freehire()]] - code - ingestion/freehire.py
- [[freehire (github.comstrelov1freehire) — a real, live, no-auth public API aggre]] - rationale - ingestion/freehire.py
- [[freehire — real ground-truth records only (see fixturesfreehire.json) Google's]] - rationale - tests/test_freehire.py
- [[freehire.py]] - code - ingestion/freehire.py
- [[lookup_company_on_freehire()]] - code - ingestion/freehire.py
- [[normalize.py]] - code - ingestion/normalize.py
- [[normalize_freehire()]] - code - ingestion/normalize.py
- [[normalize_greenhouse()]] - code - ingestion/normalize.py
- [[test_fetch_freehire_filters_to_structured_intern_seniority()]] - code - tests/test_freehire.py
- [[test_fetch_freehire_skips_a_dead_company_without_crashing()]] - code - tests/test_freehire.py
- [[test_freehire.py]] - code - tests/test_freehire.py
- [[test_google_ground_truth_posting_matches()]] - code - tests/test_freehire.py
- [[test_lookup_company_on_freehire_found()]] - code - tests/test_freehire.py
- [[test_lookup_company_on_freehire_not_found_returns_empty_dict()]] - code - tests/test_freehire.py
- [[test_lookup_company_on_freehire_slugifies_the_company_name()]] - code - tests/test_freehire.py
- [[test_normalize_freehire_strips_tracking_param_and_splits_locations()]] - code - tests/test_freehire.py
- [[test_normalize_greenhouse_strips_html_and_maps_fields()]] - code - tests/test_filter.py
- [[test_nuro_ground_truth_posting_rejects_no_year_anywhere()]] - code - tests/test_freehire.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_freehirepy
SORT file.name ASC
```

## Connections to other communities
- 16 edges to [[_COMMUNITY_write_dossier]]
- 8 edges to [[_COMMUNITY_recheck.py]]
- 2 edges to [[_COMMUNITY_test_write_dossier_creates_missing_dossiers_dir]]
- 1 edge to [[_COMMUNITY_normalize_simplify]]
- 1 edge to [[_COMMUNITY_test_debate_losses.py]]
- 1 edge to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 1 edge to [[_COMMUNITY_test_write_dossier_different_uid_same_role_company_gets_collision_suffix]]
- 1 edge to [[_COMMUNITY_test_writer.py]]
- 1 edge to [[_COMMUNITY_render_dossier]]
- 1 edge to [[_COMMUNITY_build_frontmatter]]

## Top bridge nodes
- [[normalize.py]] - degree 24, connects to 10 communities
- [[test_freehire.py]] - degree 20, connects to 2 communities
- [[normalize_greenhouse()]] - degree 8, connects to 2 communities
- [[_parse_iso_ts()]] - degree 6, connects to 2 communities
- [[normalize_freehire()]] - degree 9, connects to 1 community