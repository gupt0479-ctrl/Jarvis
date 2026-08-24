---
type: community
members: 9
---

# normalize.py

**Members:** 9 nodes

## Members
- [[Map each source's raw shape to one internal Listing dataclass.]] - rationale - ingestion/normalize.py
- [[Real record, fetched 2026-07-25 Databricks 'Product Management Intern     (Summ]] - rationale - tests/test_filter.py
- [[_parse_iso_ts()]] - code - ingestion/normalize.py
- [[_strip_html()]] - code - ingestion/normalize.py
- [[normalize.py]] - code - ingestion/normalize.py
- [[normalize_ai_jobs()]] - code - ingestion/normalize.py
- [[normalize_greenhouse()]] - code - ingestion/normalize.py
- [[test_normalize_ai_jobs_maps_fields_and_matches_real_intern_record()]] - code - tests/test_filter.py
- [[test_normalize_greenhouse_strips_html_and_maps_fields()]] - code - tests/test_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/normalizepy
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_recheck.py]]
- 7 edges to [[_COMMUNITY_test_filter.py]]
- 6 edges to [[_COMMUNITY_matches]]
- 4 edges to [[_COMMUNITY_write_dossier]]
- 3 edges to [[_COMMUNITY_test_writer.py]]
- 2 edges to [[_COMMUNITY_test_write_dossier_creates_missing_dossiers_dir]]
- 1 edge to [[_COMMUNITY_normalize_josegael]]
- 1 edge to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 1 edge to [[_COMMUNITY_test_write_dossier_different_uid_same_role_company_gets_collision_suffix]]
- 1 edge to [[_COMMUNITY_render_dossier]]
- 1 edge to [[_COMMUNITY_build_frontmatter]]

## Top bridge nodes
- [[normalize.py]] - degree 25, connects to 11 communities
- [[normalize_greenhouse()]] - degree 8, connects to 3 communities
- [[normalize_ai_jobs()]] - degree 7, connects to 3 communities
- [[_parse_iso_ts()]] - degree 6, connects to 3 communities
- [[test_normalize_ai_jobs_maps_fields_and_matches_real_intern_record()]] - degree 4, connects to 2 communities