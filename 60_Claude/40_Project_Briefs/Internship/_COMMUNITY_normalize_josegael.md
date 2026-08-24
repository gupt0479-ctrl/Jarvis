---
type: community
members: 16
---

# normalize_josegael

**Members:** 16 nodes

## Members
- [[Bare, year-less Spring stays ambiguous (could be excluded Spring 2026     or w]] - rationale - tests/test_filter.py
- [[Guards against silent test evaporation pytest.mark.parametrize collects     zer]] - rationale - tests/test_filter.py
- [[Regression for the _has_wrong_cycle_season bug a year-qualified season     (Sp]] - rationale - tests/test_filter.py
- [[_load()]] - code - tests/test_filter.py
- [[normalize_josegael()]] - code - ingestion/normalize.py
- [[test_active_false_rejects_any_source()]] - code - tests/test_filter.py
- [[test_fixture_has_both_match_and_reject_cases()]] - code - tests/test_filter.py
- [[test_josegael_bare_spring_still_rejects()]] - code - tests/test_filter.py
- [[test_josegael_matches_year_qualified_spring_2027()]] - code - tests/test_filter.py
- [[test_josegael_season_rejects_wrong_cycles_real_entries()]] - code - tests/test_filter.py
- [[test_josegael_should_match()]] - code - tests/test_filter.py
- [[test_josegael_should_reject()]] - code - tests/test_filter.py
- [[test_josegael_whitespace_only_season_does_not_crash()]] - code - tests/test_filter.py
- [[test_josegael_yearless_summer_passes_real_mlh_entry()]] - code - tests/test_filter.py
- [[test_matches_rejects_foreign_only_listing_end_to_end()]] - code - tests/test_filter.py
- [[test_simplify_matches_spring_2027_only()]] - code - tests/test_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/normalize_josegael
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_test_filter.py]]
- 11 edges to [[_COMMUNITY_matches]]
- 7 edges to [[_COMMUNITY_test_writer.py]]
- 2 edges to [[_COMMUNITY_filter.py]]
- 2 edges to [[_COMMUNITY_recheck.py]]
- 2 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 1 edge to [[_COMMUNITY_normalize.py]]

## Top bridge nodes
- [[normalize_josegael()]] - degree 18, connects to 6 communities
- [[test_active_false_rejects_any_source()]] - degree 4, connects to 3 communities
- [[test_matches_rejects_foreign_only_listing_end_to_end()]] - degree 4, connects to 3 communities
- [[test_simplify_matches_spring_2027_only()]] - degree 4, connects to 3 communities
- [[_load()]] - degree 14, connects to 2 communities