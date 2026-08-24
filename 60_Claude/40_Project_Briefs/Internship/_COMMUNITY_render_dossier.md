---
type: community
members: 27
---

# render_dossier

**Members:** 27 nodes

## Members
- [[Confirms REQUIRED_FRONTMATTER_FIELDS actually enforces notes — adding     it to]] - rationale - tests/test_validate.py
- [[The mid-body loop explicitly allows a blank line after a callout — but not     w]] - rationale - tests/test_validate.py
- [[_ok_response()]] - code - tests/test_validate.py
- [[check_format_compliance()]] - code - vault_writer/validate.py
- [[listing()]] - code - tests/test_validate.py
- [[render_dossier()]] - code - vault_writer/writer.py
- [[required_fields runs before url_liveness — a missing field should reject     wit]] - rationale - tests/test_validate.py
- [[test_format_compliance_allows_blank_line_after_callout()]] - code - tests/test_validate.py
- [[test_format_compliance_passes_on_rendered_dossier()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_blank_line_after_frontmatter()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_dashes_in_body()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_duplicate_frontmatter_key()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_missing_frontmatter_field()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_missing_notes_field()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_missing_preference_tier_field()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_stray_blank_line_in_body()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_trailing_blank_line()]] - code - tests/test_validate.py
- [[test_format_compliance_rejects_trailing_blank_line_after_callout()]] - code - tests/test_validate.py
- [[test_render_dossier_frontmatter_contains_moc_link_and_company_tag()]] - code - tests/test_writer.py
- [[test_url_live_passes_on_2xx()]] - code - tests/test_validate.py
- [[test_url_live_passes_on_3xx()]] - code - tests/test_validate.py
- [[test_url_live_rejects_404()]] - code - tests/test_validate.py
- [[test_validate.py]] - code - tests/test_validate.py
- [[test_validate_happy_path()]] - code - tests/test_validate.py
- [[test_validate_rejects_duplicate_uid()]] - code - tests/test_validate.py
- [[test_validate_stops_at_first_failing_check()]] - code - tests/test_validate.py
- [[uid()]] - code - tests/test_validate.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/render_dossier
SORT file.name ASC
```

## Connections to other communities
- 21 edges to [[_COMMUNITY_normalize_josegael]]
- 13 edges to [[_COMMUNITY_build_frontmatter]]
- 2 edges to [[_COMMUNITY_test_writer.py]]
- 2 edges to [[_COMMUNITY_recheck.py]]
- 2 edges to [[_COMMUNITY_writer.py]]
- 2 edges to [[_COMMUNITY_filter.py]]
- 1 edge to [[_COMMUNITY_test_filter.py]]
- 1 edge to [[_COMMUNITY_fetch_posting_markdown]]

## Top bridge nodes
- [[render_dossier()]] - degree 32, connects to 5 communities
- [[test_validate.py]] - degree 36, connects to 4 communities
- [[check_format_compliance()]] - degree 18, connects to 3 communities
- [[test_validate_happy_path()]] - degree 4, connects to 1 community
- [[test_validate_stops_at_first_failing_check()]] - degree 4, connects to 1 community