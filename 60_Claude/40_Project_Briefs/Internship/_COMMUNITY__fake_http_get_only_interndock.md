---
type: community
members: 23
---

# _fake_http_get_only_interndock

**Members:** 23 nodes

## Members
- [[Layer 4 — the five-check write gate. Fail any check - item is rejected and neve]] - rationale - vault_writer/validate.py
- [[Like SafeLoader, but raises on duplicate mapping keys instead of     silently ke]] - rationale - vault_writer/validate.py
- [[Renders + validates each new listing; writes the ones that pass into     the Jar]] - rationale - run_pipeline.py
- [[Runs all checks in the plan's order, fail-closed on the first failure.     Short]] - rationale - vault_writer/validate.py
- [[Same program via two sources = two different uids but one normalized     company]] - rationale - vault_writer/validate.py
- [[ValidationResult]] - code - vault_writer/validate.py
- [[_DupeKeyLoader]] - code - vault_writer/validate.py
- [[_construct_mapping_no_dupes()]] - code - vault_writer/validate.py
- [[build_matched_reason()]] - code - run_pipeline.py
- [[check_cross_source_duplicate()]] - code - vault_writer/validate.py
- [[check_not_duplicate()]] - code - vault_writer/validate.py
- [[check_required_fields()]] - code - vault_writer/validate.py
- [[check_url_live()]] - code - vault_writer/validate.py
- [[cross_source_key()]] - code - core/identity.py
- [[test_not_duplicate_passes_when_uid_unseen()]] - code - tests/test_validate.py
- [[test_not_duplicate_rejects_seen_uid()]] - code - tests/test_validate.py
- [[test_required_fields_pass()]] - code - tests/test_validate.py
- [[test_required_fields_rejects_missing_company()]] - code - tests/test_validate.py
- [[test_required_fields_rejects_missing_uid()]] - code - tests/test_validate.py
- [[test_url_live_rejects_on_request_exception()]] - code - tests/test_validate.py
- [[validate()]] - code - vault_writer/validate.py
- [[validate.py]] - code - vault_writer/validate.py
- [[validate_and_write()]] - code - run_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_fake_http_get_only_interndock
SORT file.name ASC
```

## Connections to other communities
- 23 edges to [[_COMMUNITY_render_dossier]]
- 11 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 6 edges to [[_COMMUNITY_recheck.py]]
- 2 edges to [[_COMMUNITY_test_write_dossier_creates_missing_dossiers_dir]]
- 2 edges to [[_COMMUNITY_test_writer.py]]
- 1 edge to [[_COMMUNITY_test_write_dossier_different_uid_same_role_company_gets_collision_suffix]]
- 1 edge to [[_COMMUNITY_plan_removals]]
- 1 edge to [[_COMMUNITY_dump_frontmatter]]
- 1 edge to [[_COMMUNITY_writer.py]]
- 1 edge to [[_COMMUNITY_commit_and_push_with_retry_1]]
- 1 edge to [[_COMMUNITY_build_frontmatter]]

## Top bridge nodes
- [[validate_and_write()]] - degree 16, connects to 9 communities
- [[cross_source_key()]] - degree 16, connects to 3 communities
- [[validate.py]] - degree 14, connects to 3 communities
- [[validate()]] - degree 14, connects to 2 communities
- [[check_url_live()]] - degree 8, connects to 1 community