---
type: community
members: 24
---

# fetch_and_filter

**Members:** 24 nodes

## Members
- [[.increase_indent()]] - code - vault_writer/writer.py
- [[Dumps None as a blank scalar (matching the plan's `field` empty style     inste]] - rationale - vault_writer/writer.py
- [[Real rendered frontmatter (not just the dict) — confirms preference_tier     act]] - rationale - tests/test_writer.py
- [[Renders the fixed dossier template and writes it into a vault checkout.  Renderi]] - rationale - vault_writer/writer.py
- [[Same slugification as dossier_filename() lowercase, spaces to     hyphens, ille]] - rationale - vault_writer/writer.py
- [[Shared YAML rendering (None as blank scalar, indented list items) so     every d]] - rationale - vault_writer/writer.py
- [[Two dossiers for the same company (varying casingwhitespace) must     produce t]] - rationale - tests/test_writer.py
- [[_FrontmatterDumper]] - code - vault_writer/writer.py
- [[_iso_date()]] - code - vault_writer/writer.py
- [[_represent_none()]] - code - vault_writer/writer.py
- [[_yaml_list()]] - code - vault_writer/writer.py
- [[build_frontmatter()]] - code - vault_writer/writer.py
- [[company_slug()]] - code - vault_writer/writer.py
- [[dump_frontmatter()]] - code - vault_writer/writer.py
- [[listing's real company is 'Palantir' (testsfixturessimplifyjobs.json)     — no]] - rationale - tests/test_writer.py
- [[save_dossier_uids()]] - code - vault_writer/writer.py
- [[test_build_frontmatter_includes_moc_link_and_company_tag()]] - code - tests/test_writer.py
- [[test_build_frontmatter_preference_tier_matches_real_preferred_company()]] - code - tests/test_writer.py
- [[test_build_frontmatter_preference_tier_null_when_no_preferred_companies_given()]] - code - tests/test_writer.py
- [[test_company_slug_matches_real_standard_examples()]] - code - tests/test_writer.py
- [[test_company_slug_normalizes_case_and_whitespace_for_same_company_clustering()]] - code - tests/test_writer.py
- [[test_render_dossier_shows_real_rendered_frontmatter_with_preference_match()]] - code - tests/test_writer.py
- [[uid and category are deliberately not rendered — uid stays available     interna]] - rationale - vault_writer/writer.py
- [[writer.py]] - code - vault_writer/writer.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/fetch_and_filter
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_update_debate_losses]]
- 5 edges to [[_COMMUNITY_run_pipeline.py]]
- 5 edges to [[_COMMUNITY_dedup_new]]
- 3 edges to [[_COMMUNITY_test_cross_source_key_punctuation_insensitive_marmon_case]]

## Top bridge nodes
- [[writer.py]] - degree 20, connects to 4 communities
- [[build_frontmatter()]] - degree 11, connects to 3 communities
- [[test_render_dossier_shows_real_rendered_frontmatter_with_preference_match()]] - degree 4, connects to 2 communities
- [[save_dossier_uids()]] - degree 3, connects to 2 communities
- [[company_slug()]] - degree 8, connects to 1 community