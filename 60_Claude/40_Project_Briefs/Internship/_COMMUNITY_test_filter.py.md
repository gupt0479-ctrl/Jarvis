---
type: community
members: 23
---

# test_filter.py

**Members:** 23 nodes

## Members
- [[Does Not Offer Sponsorship' means no H-1B, not no OPT — same rule as     everywh]] - rationale - tests/test_filter.py
- [[Permissive like locations no degrees data passes; non-empty data must     inclu]] - rationale - core/filter.py
- [[The bare-city fallback added for 'London' alone must be an exact     whole-strin]] - rationale - tests/test_filter.py
- [[degrees_eligible()]] - code - core/filter.py
- [[location_eligible()]] - code - core/filter.py
- [[normalize_lever()]] - code - ingestion/normalize.py
- [[normalize_vanshb03()]] - code - ingestion/normalize.py
- [[test_degrees_eligible()]] - code - tests/test_filter.py
- [[test_filter.py]] - code - tests/test_filter.py
- [[test_location_affirmatively_foreign_is_rejected()]] - code - tests/test_filter.py
- [[test_location_new_london_ct_is_not_caught_by_bare_london_fallback()]] - code - tests/test_filter.py
- [[test_location_no_data_is_unrestricted()]] - code - tests/test_filter.py
- [[test_location_one_us_entry_among_foreign_is_enough()]] - code - tests/test_filter.py
- [[test_location_us_or_ambiguous_is_eligible()]] - code - tests/test_filter.py
- [[test_normalize_lever_falls_back_to_hosted_url_when_no_apply_url()]] - code - tests/test_filter.py
- [[test_normalize_lever_maps_fields_and_prefers_apply_url()]] - code - tests/test_filter.py
- [[test_simplify_should_match()]] - code - tests/test_filter.py
- [[test_simplify_should_reject()]] - code - tests/test_filter.py
- [[test_terms_weight_present_and_correct()]] - code - tests/test_filter.py
- [[test_vanshb03_bare_spring_still_rejects()]] - code - tests/test_filter.py
- [[test_vanshb03_no_sponsorship_is_not_an_exclusion()]] - code - tests/test_filter.py
- [[test_vanshb03_should_match()]] - code - tests/test_filter.py
- [[test_vanshb03_should_reject()]] - code - tests/test_filter.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_filterpy
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_matches]]
- 15 edges to [[_COMMUNITY_normalize_josegael]]
- 7 edges to [[_COMMUNITY_recheck.py]]
- 7 edges to [[_COMMUNITY_normalize.py]]
- 5 edges to [[_COMMUNITY_filter.py]]
- 3 edges to [[_COMMUNITY_test_writer.py]]
- 2 edges to [[_COMMUNITY_revalidate.py]]
- 2 edges to [[_COMMUNITY_test_write_dossier_creates_missing_dossiers_dir]]

## Top bridge nodes
- [[test_filter.py]] - degree 61, connects to 6 communities
- [[normalize_vanshb03()]] - degree 11, connects to 4 communities
- [[location_eligible()]] - degree 11, connects to 3 communities
- [[normalize_lever()]] - degree 7, connects to 3 communities
- [[degrees_eligible()]] - degree 5, connects to 2 communities