---
type: community
members: 23
---

# writer.py

**Members:** 23 nodes

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
TABLE source_file, type FROM #community/writerpy
SORT file.name ASC
```

## Connections to other communities
- 15 edges to [[_COMMUNITY_build_frontmatter]]
- 5 edges to [[_COMMUNITY_render_dossier]]
- 3 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 2 edges to [[_COMMUNITY_commit_and_push_with_retry_1]]
- 1 edge to [[_COMMUNITY_write_dossier]]
- 1 edge to [[_COMMUNITY_recheck.py]]

## Top bridge nodes
- [[writer.py]] - degree 22, connects to 6 communities
- [[build_frontmatter()]] - degree 11, connects to 3 communities
- [[dump_frontmatter()]] - degree 5, connects to 2 communities
- [[test_render_dossier_shows_real_rendered_frontmatter_with_preference_match()]] - degree 4, connects to 2 communities
- [[company_slug()]] - degree 8, connects to 1 community