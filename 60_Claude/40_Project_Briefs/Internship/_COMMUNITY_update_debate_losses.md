---
type: community
members: 21
---

# update_debate_losses

**Members:** 21 nodes

## Members
- [[Copy of the committed throwaway_vault skeleton in a scratch dir per test,     so]] - rationale - tests/test_writer.py
- [[Same role+company but a genuinely different uid must not overwrite —     only a]] - rationale - tests/test_writer.py
- [[Writes an already-rendered, already-validated dossier into its     priority-buck]] - rationale - vault_writer/writer.py
- [[Role - Company.md', Windows-unsafe chars stripped (the vault lives     on a]] - rationale - vault_writer/writer.py
- [[dossier_filename()]] - code - vault_writer/writer.py
- [[listing()_1]] - code - tests/test_writer.py
- [[state_dir()]] - code - tests/test_writer.py
- [[test_dossier_filename_collision_appends_number()]] - code - tests/test_writer.py
- [[test_dossier_filename_collision_increments_past_multiple()]] - code - tests/test_writer.py
- [[test_dossier_filename_sanitizes_illegal_chars()]] - code - tests/test_writer.py
- [[test_render_dossier_frontmatter_contains_moc_link_and_company_tag()]] - code - tests/test_writer.py
- [[test_write_dossier_creates_missing_dossiers_dir()]] - code - tests/test_writer.py
- [[test_write_dossier_different_uid_same_role_company_gets_collision_suffix()]] - code - tests/test_writer.py
- [[test_write_dossier_is_idempotent_on_uid()]] - code - tests/test_writer.py
- [[test_write_dossier_routes_into_bucket_subfolder()]] - code - tests/test_writer.py
- [[test_write_dossier_without_state_dir_records_no_manifest()]] - code - tests/test_writer.py
- [[test_write_dossier_writes_expected_file()]] - code - tests/test_writer.py
- [[test_writer.py]] - code - tests/test_writer.py
- [[vault_root with no pre-existing Dossiers folder at all still works.]] - rationale - tests/test_writer.py
- [[vault_root()]] - code - tests/test_writer.py
- [[write_dossier()]] - code - vault_writer/writer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/update_debate_losses
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_fetch_and_filter]]
- 8 edges to [[_COMMUNITY_dedup_new]]
- 6 edges to [[_COMMUNITY_run_pipeline.py]]
- 2 edges to [[_COMMUNITY__run_once_kwargs]]
- 1 edge to [[_COMMUNITY_test_run_pipeline.py]]
- 1 edge to [[_COMMUNITY_validate_and_write]]

## Top bridge nodes
- [[test_writer.py]] - degree 29, connects to 5 communities
- [[write_dossier()]] - degree 16, connects to 3 communities
- [[dossier_filename()]] - degree 8, connects to 1 community
- [[test_write_dossier_writes_expected_file()]] - degree 4, connects to 1 community
- [[test_write_dossier_different_uid_same_role_company_gets_collision_suffix()]] - degree 4, connects to 1 community