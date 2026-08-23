---
type: community
members: 53
---

# build_frontmatter

**Members:** 53 nodes

## Members
- [[.increase_indent()]] - code - vault_writer/writer.py
- [[Copy of the committed throwaway_vault skeleton in a scratch dir per test,     so]] - rationale - tests/test_writer.py
- [[Dumps None as a blank scalar (matching the plan's `field` empty style     inste]] - rationale - vault_writer/writer.py
- [[Fix 2, Prompt 5 review (2026-07-30) two dossiers with the identical     filenam]] - rationale - tests/test_writer.py
- [[Moves a closed-posting dossier into Viewed instead of deleting it     (Internsh]] - rationale - vault_writer/writer.py
- [[Real rendered frontmatter (not just the dict) — confirms preference_tier     act]] - rationale - tests/test_writer.py
- [[Renders the fixed dossier template and writes it into a vault checkout.  Renderi]] - rationale - vault_writer/writer.py
- [[Same role+company but a genuinely different uid must not overwrite —     only a]] - rationale - tests/test_writer.py
- [[Same slugification as dossier_filename() lowercase, spaces to     hyphens, ille]] - rationale - vault_writer/writer.py
- [[Shared YAML rendering (None as blank scalar, indented list items) so     every d]] - rationale - vault_writer/writer.py
- [[Two dossiers for the same company (varying casingwhitespace) must     produce t]] - rationale - tests/test_writer.py
- [[Writes an already-rendered, already-validated dossier into its     priority-buck]] - rationale - vault_writer/writer.py
- [[Role - Company.md', Windows-unsafe chars stripped (the vault lives     on a]] - rationale - vault_writer/writer.py
- [[_FrontmatterDumper]] - code - vault_writer/writer.py
- [[_iso_date()]] - code - vault_writer/writer.py
- [[_represent_none()]] - code - vault_writer/writer.py
- [[_yaml_list()]] - code - vault_writer/writer.py
- [[build_frontmatter()]] - code - vault_writer/writer.py
- [[company_slug()]] - code - vault_writer/writer.py
- [[dossier_filename()]] - code - vault_writer/writer.py
- [[dump_frontmatter()]] - code - vault_writer/writer.py
- [[listing's real company is 'Palantir' (testsfixturessimplifyjobs.json)     — no]] - rationale - tests/test_writer.py
- [[listing()_1]] - code - tests/test_writer.py
- [[load_dossier_uids()]] - code - vault_writer/writer.py
- [[move_dossier_to_viewed()]] - code - vault_writer/writer.py
- [[save_dossier_uids()]] - code - vault_writer/writer.py
- [[state_dir()]] - code - tests/test_writer.py
- [[test_build_frontmatter_includes_moc_link_and_company_tag()]] - code - tests/test_writer.py
- [[test_build_frontmatter_preference_tier_matches_real_preferred_company()]] - code - tests/test_writer.py
- [[test_build_frontmatter_preference_tier_null_when_no_preferred_companies_given()]] - code - tests/test_writer.py
- [[test_company_slug_matches_real_standard_examples()]] - code - tests/test_writer.py
- [[test_company_slug_normalizes_case_and_whitespace_for_same_company_clustering()]] - code - tests/test_writer.py
- [[test_dossier_filename_collision_appends_number()]] - code - tests/test_writer.py
- [[test_dossier_filename_collision_increments_past_multiple()]] - code - tests/test_writer.py
- [[test_dossier_filename_sanitizes_illegal_chars()]] - code - tests/test_writer.py
- [[test_move_dossier_to_viewed_does_not_overwrite_filename_collision()]] - code - tests/test_writer.py
- [[test_move_dossier_to_viewed_moves_file_and_updates_frontmatter()]] - code - tests/test_writer.py
- [[test_move_dossier_to_viewed_updates_uid_manifest()]] - code - tests/test_writer.py
- [[test_render_dossier_frontmatter_contains_moc_link_and_company_tag()]] - code - tests/test_writer.py
- [[test_render_dossier_shows_real_rendered_frontmatter_with_preference_match()]] - code - tests/test_writer.py
- [[test_write_dossier_creates_missing_dossiers_dir()]] - code - tests/test_writer.py
- [[test_write_dossier_different_uid_same_role_company_gets_collision_suffix()]] - code - tests/test_writer.py
- [[test_write_dossier_is_idempotent_on_uid()]] - code - tests/test_writer.py
- [[test_write_dossier_records_uid_manifest()]] - code - tests/test_writer.py
- [[test_write_dossier_routes_into_bucket_subfolder()]] - code - tests/test_writer.py
- [[test_write_dossier_without_state_dir_records_no_manifest()]] - code - tests/test_writer.py
- [[test_write_dossier_writes_expected_file()]] - code - tests/test_writer.py
- [[test_writer.py]] - code - tests/test_writer.py
- [[uid and category are deliberately not rendered — uid stays available     interna]] - rationale - vault_writer/writer.py
- [[vault_root with no pre-existing Dossiers folder at all still works.]] - rationale - tests/test_writer.py
- [[vault_root()]] - code - tests/test_writer.py
- [[write_dossier()]] - code - vault_writer/writer.py
- [[writer.py]] - code - vault_writer/writer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/build_frontmatter
SORT file.name ASC
```

## Connections to other communities
- 17 edges to [[_COMMUNITY_render_dossier]]
- 9 edges to [[_COMMUNITY_recheck.py]]
- 4 edges to [[_COMMUNITY_revalidate.py]]
- 3 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 2 edges to [[_COMMUNITY_test_writer.py]]
- 1 edge to [[_COMMUNITY_write_dossier]]

## Top bridge nodes
- [[writer.py]] - degree 22, connects to 4 communities
- [[test_writer.py]] - degree 33, connects to 3 communities
- [[write_dossier()]] - degree 18, connects to 2 communities
- [[move_dossier_to_viewed()]] - degree 13, connects to 2 communities
- [[build_frontmatter()]] - degree 11, connects to 2 communities