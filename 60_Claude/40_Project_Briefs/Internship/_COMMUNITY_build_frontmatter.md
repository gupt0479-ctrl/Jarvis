---
type: community
members: 30
---

# build_frontmatter

**Members:** 30 nodes

## Members
- [[Fix 2, Prompt 5 review (2026-07-30) two dossiers with the identical     filenam]] - rationale - tests/test_writer.py
- [[Moves a closed-posting dossier into Viewed instead of deleting it     (Internsh]] - rationale - vault_writer/writer.py
- [[Renders the fixed dossier template and writes it into a vault checkout.  Renderi]] - rationale - vault_writer/writer.py
- [[Same role+company but a genuinely different uid must not overwrite —     only a]] - rationale - tests/test_writer.py
- [[Writes an already-rendered, already-validated dossier into its     priority-buck]] - rationale - vault_writer/writer.py
- [[Role - Company.md', Windows-unsafe chars stripped (the vault lives     on a]] - rationale - vault_writer/writer.py
- [[_represent_none()]] - code - vault_writer/writer.py
- [[dossier_filename()]] - code - vault_writer/writer.py
- [[listing()_1]] - code - tests/test_writer.py
- [[load_dossier_uids()]] - code - vault_writer/writer.py
- [[move_dossier_to_viewed()]] - code - vault_writer/writer.py
- [[save_dossier_uids()]] - code - vault_writer/writer.py
- [[state_dir()]] - code - tests/test_writer.py
- [[test_dossier_filename_collision_appends_number()]] - code - tests/test_writer.py
- [[test_dossier_filename_collision_increments_past_multiple()]] - code - tests/test_writer.py
- [[test_dossier_filename_sanitizes_illegal_chars()]] - code - tests/test_writer.py
- [[test_move_dossier_to_viewed_does_not_overwrite_filename_collision()]] - code - tests/test_writer.py
- [[test_move_dossier_to_viewed_moves_file_and_updates_frontmatter()]] - code - tests/test_writer.py
- [[test_move_dossier_to_viewed_updates_uid_manifest()]] - code - tests/test_writer.py
- [[test_write_dossier_creates_missing_dossiers_dir()]] - code - tests/test_writer.py
- [[test_write_dossier_different_uid_same_role_company_gets_collision_suffix()]] - code - tests/test_writer.py
- [[test_write_dossier_is_idempotent_on_uid()]] - code - tests/test_writer.py
- [[test_write_dossier_records_uid_manifest()]] - code - tests/test_writer.py
- [[test_write_dossier_routes_into_bucket_subfolder()]] - code - tests/test_writer.py
- [[test_write_dossier_without_state_dir_records_no_manifest()]] - code - tests/test_writer.py
- [[test_write_dossier_writes_expected_file()]] - code - tests/test_writer.py
- [[test_writer.py]] - code - tests/test_writer.py
- [[vault_root with no pre-existing Dossiers folder at all still works.]] - rationale - tests/test_writer.py
- [[write_dossier()]] - code - vault_writer/writer.py
- [[writer.py]] - code - vault_writer/writer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/build_frontmatter
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_render_dossier]]
- 12 edges to [[_COMMUNITY_build_frontmatter_1]]
- 6 edges to [[_COMMUNITY_recheck.py]]
- 4 edges to [[_COMMUNITY_write_dossier]]
- 4 edges to [[_COMMUNITY_commit_and_push_with_retry]]
- 3 edges to [[_COMMUNITY_dump_frontmatter]]
- 2 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 2 edges to [[_COMMUNITY_normalize_simplify]]
- 1 edge to [[_COMMUNITY_writer.py]]
- 1 edge to [[_COMMUNITY_vault_root_1]]

## Top bridge nodes
- [[writer.py]] - degree 22, connects to 7 communities
- [[test_writer.py]] - degree 33, connects to 5 communities
- [[move_dossier_to_viewed()]] - degree 13, connects to 4 communities
- [[load_dossier_uids()]] - degree 9, connects to 3 communities
- [[write_dossier()]] - degree 18, connects to 2 communities