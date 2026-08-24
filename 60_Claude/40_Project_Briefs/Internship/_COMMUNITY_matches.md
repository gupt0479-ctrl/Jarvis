---
type: community
members: 21
---

# matches

**Members:** 21 nodes

## Members
- [[Listing]] - code - ingestion/normalize.py
- [[Real case Belvedere Trading's live 'Quantitative Trading Intern -     Summer 20]] - rationale - tests/test_filter.py
- [[Real case Ellipsis Labs' live 'Software Engineer - 2027 Interns' posting     ne]] - rationale - tests/test_filter.py
- [[Real case Marshall Wace's live 'Technology Intern - 2027' postings state     th]] - rationale - tests/test_filter.py
- [[matches()]] - code - core/filter.py
- [[normalize_zshah101()]] - code - ingestion/normalize.py
- [[test_ashby_bare_year_real_ellipsis_labs_case_passes()]] - code - tests/test_filter.py
- [[test_ashby_matches_literal_term_in_description()]] - code - tests/test_filter.py
- [[test_ashby_matches_spring_2027_literal_term()]] - code - tests/test_filter.py
- [[test_greenhouse_bare_wrong_year_with_no_right_year_rejects()]] - code - tests/test_filter.py
- [[test_greenhouse_bare_year_with_no_season_word_passes_permissively()]] - code - tests/test_filter.py
- [[test_greenhouse_matches_literal_term_in_title()]] - code - tests/test_filter.py
- [[test_greenhouse_matches_spring_2027_literal_term()]] - code - tests/test_filter.py
- [[test_greenhouse_rejects_explicit_wrong_year_in_content()]] - code - tests/test_filter.py
- [[test_lever_bare_year_with_no_season_word_passes_permissively()]] - code - tests/test_filter.py
- [[test_lever_matches_literal_term_in_description()]] - code - tests/test_filter.py
- [[test_lever_rejects_explicit_wrong_year()]] - code - tests/test_filter.py
- [[test_zshah101_citizens_only_real_anduril_entry()]] - code - tests/test_filter.py
- [[test_zshah101_matches_spring_2027()]] - code - tests/test_filter.py
- [[test_zshah101_should_match()]] - code - tests/test_filter.py
- [[test_zshah101_should_reject()]] - code - tests/test_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/matches
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_test_filter.py]]
- 11 edges to [[_COMMUNITY_normalize_josegael]]
- 6 edges to [[_COMMUNITY_normalize.py]]
- 5 edges to [[_COMMUNITY_filter.py]]
- 5 edges to [[_COMMUNITY_recheck.py]]
- 4 edges to [[_COMMUNITY_write_dossier]]
- 4 edges to [[_COMMUNITY_test_writer.py]]
- 4 edges to [[_COMMUNITY_test_write_dossier_creates_missing_dossiers_dir]]
- 2 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]

## Top bridge nodes
- [[Listing]] - degree 29, connects to 8 communities
- [[matches()]] - degree 43, connects to 6 communities
- [[normalize_zshah101()]] - degree 12, connects to 4 communities
- [[test_zshah101_citizens_only_real_anduril_entry()]] - degree 4, connects to 2 communities
- [[test_zshah101_matches_spring_2027()]] - degree 4, connects to 2 communities