---
type: community
cohesion: 0.10
members: 29
---

# Adjustment Policy Mapping Tests

**Cohesion:** 0.10 - loosely connected
**Members:** 29 nodes

## Members
- [[.test_adjusted_policy()]] - code - tests/test_normalization.py
- [[.test_case_insensitive()]] - code - tests/test_normalization.py
- [[.test_empty_string()]] - code - tests/test_normalization.py
- [[.test_fully_adjusted_policy()]] - code - tests/test_normalization.py
- [[.test_none_like_string()]] - code - tests/test_normalization.py
- [[.test_numeric_string()]] - code - tests/test_normalization.py
- [[.test_partial_match()]] - code - tests/test_normalization.py
- [[.test_random_string()]] - code - tests/test_normalization.py
- [[.test_raw_policy()]] - code - tests/test_normalization.py
- [[.test_split_adjusted_policy()]] - code - tests/test_normalization.py
- [[.test_split_dividend_adjusted_policy()]] - code - tests/test_normalization.py
- [[.test_split_policy()]] - code - tests/test_normalization.py
- [[.test_unadjusted_policy()]] - code - tests/test_normalization.py
- [[.test_whitespace_stripped()]] - code - tests/test_normalization.py
- [[Leadingtrailing whitespace should be stripped.]] - rationale - tests/test_normalization.py
- [[Map a provider's adjustment_policy string to a PriceAdjustment enum value.]] - rationale - src/research_data/normalization.py
- [[Policy mapping should be case-insensitive.]] - rationale - tests/test_normalization.py
- [[Property 18 Normalizer Price Adjustment Mapping.      Use Hypothesis to gener]] - rationale - tests/test_property_adjustment_mapping.py
- [[Property-based tests for normalizer price adjustment mapping (Property 18).  P]] - rationale - tests/test_property_adjustment_mapping.py
- [[Test that map_adjustment_policy maps recognized policies correctly.]] - rationale - tests/test_normalization.py
- [[Test that map_adjustment_policy returns UNKNOWN for unrecognized values.]] - rationale - tests/test_normalization.py
- [[TestMapAdjustmentPolicyKnown]] - code - tests/test_normalization.py
- [[TestMapAdjustmentPolicyUnknown]] - code - tests/test_normalization.py
- [[TestProperty18NormalizerPriceAdjustmentMapping]] - code - tests/test_property_adjustment_mapping.py
- [[map_adjustment_policy()]] - code - src/research_data/normalization.py
- [[test_empty_string_maps_to_unknown()]] - code - tests/test_property_adjustment_mapping.py
- [[test_known_policies_map_correctly_regardless_of_case()]] - code - tests/test_property_adjustment_mapping.py
- [[test_property_adjustment_mapping.py]] - code - tests/test_property_adjustment_mapping.py
- [[test_unknown_policies_map_to_unknown()]] - code - tests/test_property_adjustment_mapping.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Adjustment_Policy_Mapping_Tests
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Normalization Pipeline]]
- 3 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 2 edges to [[_COMMUNITY_Provider API-Key Validation]]
- 2 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 2 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 2 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]

## Top bridge nodes
- [[TestMapAdjustmentPolicyKnown]] - degree 18, connects to 6 communities
- [[TestMapAdjustmentPolicyUnknown]] - degree 14, connects to 6 communities
- [[map_adjustment_policy()]] - degree 20, connects to 1 community
- [[TestProperty18NormalizerPriceAdjustmentMapping]] - degree 3, connects to 1 community