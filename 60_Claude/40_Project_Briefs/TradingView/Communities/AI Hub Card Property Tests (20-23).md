---
type: community
members: 12
---

# AI Hub Card Property Tests (20-23)

**Members:** 12 nodes

## Members
- [[Property 20+ — AI hub card allowlist and fail-closed runner (Phase 3).  Extends]] - rationale - tests/test_property_ai_hub_cards.py
- [[Property 20 floats match iff equal after FLOAT_DISPLAY_DECIMALS rounding.]] - rationale - tests/test_property_ai_hub_cards.py
- [[Property 21 MISSINGCONTRADICTORY → INSUFFICIENT_DATA, zero LLM calls.]] - rationale - tests/test_property_ai_hub_cards.py
- [[Property 23 a card quoting any packet float at display precision (4dp)     alwa]] - rationale - tests/test_property_ai_hub_cards.py
- [[QualityStatus_3]] - code
- [[ScorePacket_5]] - code
- [[_packet()_1]] - code - tests/test_property_ai_hub_cards.py
- [[test_int_bucket_exact()]] - code - tests/test_property_ai_hub_cards.py
- [[test_property_20_float_allowlist_rounding_boundary()]] - code - tests/test_property_ai_hub_cards.py
- [[test_property_21_missing_blocks_llm_zero_invocations()]] - code - tests/test_property_ai_hub_cards.py
- [[test_property_23_runner_accepts_display_precision_quotes()]] - code - tests/test_property_ai_hub_cards.py
- [[test_property_ai_hub_cards.py]] - code - tests/test_property_ai_hub_cards.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AI_Hub_Card_Property_Tests_20-23
SORT file.name ASC
```

## Connections to other communities
- 4 edges to [[_COMMUNITY_Analyst Assembly & LLM Seam Tests]]
- 3 edges to [[_COMMUNITY_Agents Runner & Critic Bundle]]
- 3 edges to [[_COMMUNITY_EvidenceCardCriticReview Validators]]
- 2 edges to [[_COMMUNITY_Numeric Allowlist (B3)]]
- 1 edge to [[_COMMUNITY_Analyst Prompt & Vault Writer]]

## Top bridge nodes
- [[test_property_23_runner_accepts_display_precision_quotes()]] - degree 8, connects to 4 communities
- [[test_property_21_missing_blocks_llm_zero_invocations()]] - degree 7, connects to 2 communities
- [[test_property_ai_hub_cards.py]] - degree 7, connects to 1 community
- [[_packet()_1]] - degree 7, connects to 1 community
- [[test_property_20_float_allowlist_rounding_boundary()]] - degree 4, connects to 1 community
