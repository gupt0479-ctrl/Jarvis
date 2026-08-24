---
type: community
members: 39
---

# test_write_dossier_creates_missing_dossiers_dir

**Members:** 39 nodes

## Members
- [[Layer 2.5b — priority-bucket classification for listings that already passed cor]] - rationale - core/classify.py
- [[No numeric label ('Priority 123') — the folder location already     encodes th]] - rationale - core/classify.py
- [[Real committed fixture Poshmark 'Cloud Platform Engineer Intern,     Growth' (t]] - rationale - tests/test_classify.py
- [[Real committed fixture plain 'Software Engineer Intern', category     Software]] - rationale - tests/test_classify.py
- [[Real false positive Mosaic Company 'Operations & Automation     Engineering Co-]] - rationale - tests/test_classify.py
- [[Returns (bucket_name, signal) — signal is the specific real phrase     that drov]] - rationale - core/classify.py
- [[Same bucket for both candidates — stage 2 is explicitly a no-op here     per spe]] - rationale - tests/test_debate.py
- [[Scoped per-bucket per the tunable budget dict — each bucket fills only     from]] - rationale - run_pipeline.py
- [[Standard cmp semantics negative if a should rank first, positive if     b shoul]] - rationale - core/debate.py
- [[Task L — the deterministic pairwise 'debate' comparator. Each stage is tested in]] - rationale - tests/test_debate.py
- [[Two non-preferred candidates (stage 1 ties), different buckets, one     bucket's]] - rationale - tests/test_debate.py
- [[Two preferred companies with different dates — stage 1 ties (both     'high'), r]] - rationale - tests/test_debate.py
- [[_candidate()]] - code - tests/test_debate.py
- [[_prioritize_and_cap()]] - code - run_pipeline.py
- [[bucket_urgency=None (the default) skips stage 2 entirely, falling     straight t]] - rationale - tests/test_debate.py
- [[classification_callout()]] - code - core/classify.py
- [[classify()]] - code - core/classify.py
- [[classify.py]] - code - core/classify.py
- [[compute_bucket_urgency()]] - code - core/debate.py
- [[coreclassify.py — real examples throughout, same fixtures as test_relevance.py]] - rationale - tests/test_classify.py
- [[debate_compare()]] - code - core/debate.py
- [[test_classification_callout_format_has_no_numeric_label()]] - code - tests/test_classify.py
- [[test_classification_callout_other_bucket_has_no_signal_but_still_no_number()]] - code - tests/test_classify.py
- [[test_classify.py]] - code - tests/test_classify.py
- [[test_classify_ai_ml_from_real_bosch_content()]] - code - tests/test_classify.py
- [[test_classify_ai_ml_from_real_magna_content()]] - code - tests/test_classify.py
- [[test_classify_does_not_match_bare_threat_real_mosaic_safety_disclaimer()]] - code - tests/test_classify.py
- [[test_classify_fullstack_from_real_vanshb03_fixture()]] - code - tests/test_classify.py
- [[test_classify_other_from_real_zshah101_fixture()]] - code - tests/test_classify.py
- [[test_classify_still_matches_genuine_threat_intelligence_content()]] - code - tests/test_classify.py
- [[test_debate.py]] - code - tests/test_debate.py
- [[test_debate_compare_missing_date_posted_sorts_last()]] - code - tests/test_debate.py
- [[test_debate_compare_prefers_bucket_at_risk_of_going_unfilled()]] - code - tests/test_debate.py
- [[test_debate_compare_prefers_preferred_company_with_identical_dates()]] - code - tests/test_debate.py
- [[test_debate_compare_recency_is_final_tiebreak()]] - code - tests/test_debate.py
- [[test_debate_compare_skips_bucket_fill_need_for_same_bucket_pair()]] - code - tests/test_debate.py
- [[test_debate_compare_ties_between_two_preferred_companies_falls_through()]] - code - tests/test_debate.py
- [[test_debate_compare_without_bucket_urgency_skips_stage_2()]] - code - tests/test_debate.py
- [[{bucket max(0, budgetbucket - candidate_countbucket)} for every     bucket]] - rationale - core/debate.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_write_dossier_creates_missing_dossiers_dir
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_test_filter.py]]
- 8 edges to [[_COMMUNITY_recheck.py]]
- 7 edges to [[_COMMUNITY_test_render_dossier_shows_real_rendered_frontmatter_with_preference_match]]
- 2 edges to [[_COMMUNITY_writer.py]]

## Top bridge nodes
- [[test_debate.py]] - degree 16, connects to 3 communities
- [[classify()]] - degree 15, connects to 3 communities
- [[debate_compare()]] - degree 14, connects to 2 communities
- [[classification_callout()]] - degree 7, connects to 2 communities
- [[compute_bucket_urgency()]] - degree 7, connects to 2 communities