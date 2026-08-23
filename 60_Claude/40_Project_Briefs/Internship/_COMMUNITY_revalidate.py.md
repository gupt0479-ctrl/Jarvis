---
type: community
members: 25
---

# revalidate.py

**Members:** 25 nodes

## Members
- [[Frontmatter dicts of every dossier file actually present in the vault     checko]] - rationale - vault_writer/writer.py
- [[Real dossier Optiver 'FPGA Internship (2027 Start)' — Netherlands,     a _NON_U]] - rationale - tests/test_revalidate.py
- [[Real dossier Optiver 'Software Engineer Intern' style content —     genuine tec]] - rationale - tests/test_revalidate.py
- [[Real dossier UHY 'Data Operations Intern' — Excel-only audit     support, no si]] - rationale - tests/test_revalidate.py
- [[Real dossier Vertiv 'Product Management Intern' — matches     stage1_reject's e]] - rationale - tests/test_revalidate.py
- [[The dossier's own already-fetched content (verbatim, as originally     written)]] - rationale - revalidate.py
- [[The first rule this dossier would now fail under current code, or     None if it]] - rationale - revalidate.py
- [[{path, company, title, reason} for every live dossier that would     now fail]] - rationale - revalidate.py
- [[check_dossier()]] - code - revalidate.py
- [[extract_posting_content()]] - code - revalidate.py
- [[file_github_issue()]] - code - run_pipeline.py
- [[find_regressions()]] - code - revalidate.py
- [[main()_2]] - code - recheck.py
- [[main()_3]] - code - revalidate.py
- [[revalidate.py]] - code - revalidate.py
- [[revalidate.py — re-checks live dossiers against current core code using their o]] - rationale - tests/test_revalidate.py
- [[scan_dossiers()]] - code - vault_writer/writer.py
- [[test_check_dossier_flags_real_non_us_location()]] - code - tests/test_revalidate.py
- [[test_check_dossier_flags_real_stage1_reject_title()]] - code - tests/test_revalidate.py
- [[test_check_dossier_flags_real_stage2_non_technical_content()]] - code - tests/test_revalidate.py
- [[test_check_dossier_passes_real_genuine_posting()]] - code - tests/test_revalidate.py
- [[test_extract_posting_content_from_enriched_dossier()]] - code - tests/test_revalidate.py
- [[test_extract_posting_content_from_thin_dossier()]] - code - tests/test_revalidate.py
- [[test_find_regressions_scans_real_vault_layout()]] - code - tests/test_revalidate.py
- [[test_revalidate.py]] - code - tests/test_revalidate.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/revalidatepy
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_recheck.py]]
- 5 edges to [[_COMMUNITY_test_write_dossier_different_uid_same_role_company_gets_collision_suffix]]
- 4 edges to [[_COMMUNITY_build_frontmatter]]
- 3 edges to [[_COMMUNITY_write_dossier]]
- 1 edge to [[_COMMUNITY_commit_and_push_with_retry]]
- 1 edge to [[_COMMUNITY_plan_removals]]
- 1 edge to [[_COMMUNITY_render_dossier]]

## Top bridge nodes
- [[revalidate.py]] - degree 14, connects to 4 communities
- [[main()_2]] - degree 8, connects to 4 communities
- [[scan_dossiers()]] - degree 9, connects to 3 communities
- [[check_dossier()]] - degree 11, connects to 2 communities
- [[find_regressions()]] - degree 9, connects to 1 community