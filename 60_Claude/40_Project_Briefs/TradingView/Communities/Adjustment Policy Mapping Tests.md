---
type: community
members: 32
---

# Adjustment Policy Mapping Tests

**Members:** 32 nodes

## Members
- [[.test_adjusted_policy()]] - code - tests/test_normalization.py
- [[.test_case_insensitive()]] - code - tests/test_normalization.py
- [[.test_empty_string()]] - code - tests/test_normalization.py
- [[.test_empty_string_maps_to_unknown()]] - code - tests/test_property_adjustment_mapping.py
- [[.test_fully_adjusted_policy()]] - code - tests/test_normalization.py
- [[.test_known_policies_map_correctly_regardless_of_case()]] - code - tests/test_property_adjustment_mapping.py
- [[.test_none_like_string()]] - code - tests/test_normalization.py
- [[.test_numeric_string()]] - code - tests/test_normalization.py
- [[.test_partial_match()]] - code - tests/test_normalization.py
- [[.test_random_string()]] - code - tests/test_normalization.py
- [[.test_raw_policy()]] - code - tests/test_normalization.py
- [[.test_split_adjusted_policy()]] - code - tests/test_normalization.py
- [[.test_split_dividend_adjusted_policy()]] - code - tests/test_normalization.py
- [[.test_split_policy()]] - code - tests/test_normalization.py
- [[.test_unadjusted_policy()]] - code - tests/test_normalization.py
- [[.test_unknown_policies_map_to_unknown()]] - code - tests/test_property_adjustment_mapping.py
- [[.test_whitespace_stripped()]] - code - tests/test_normalization.py
- [[An empty string maps to PriceAdjustment.UNKNOWN.]] - rationale - tests/test_property_adjustment_mapping.py
- [[For any known policy string with arbitrary casing and whitespace,         map_a]] - rationale - tests/test_property_adjustment_mapping.py
- [[For any string that doesn't match a known policy (after lowercasing         and]] - rationale - tests/test_property_adjustment_mapping.py
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
- [[test_property_adjustment_mapping.py]] - code - tests/test_property_adjustment_mapping.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Adjustment_Policy_Mapping_Tests
SORT file.name ASC
```

## Connections to other communities
- 5 edges to [[_COMMUNITY_OHLCV Normalization Tests]]
- 4 edges to [[_COMMUNITY_Provider-to-Canonical Normalizer]]
- 2 edges to [[_COMMUNITY_App Config Loading]]
- 1 edge to [[_COMMUNITY_Core Models & Quality Auditor Modules]]
- 1 edge to [[_COMMUNITY_PriceReadAPI Row Conversion Tests]]

## Top bridge nodes
- [[map_adjustment_policy()]] - degree 21, connects to 3 communities
- [[TestMapAdjustmentPolicyKnown]] - degree 14, connects to 3 communities
- [[TestMapAdjustmentPolicyUnknown]] - degree 10, connects to 3 communities
- [[test_property_adjustment_mapping.py]] - degree 4, connects to 2 communities
