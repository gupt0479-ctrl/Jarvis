---
type: community
cohesion: 0.06
members: 72
---

# Normalization Pipeline

**Cohesion:** 0.06 - loosely connected
**Members:** 72 nodes

## Members
- [[.test_adjusted_close_none_when_not_supplied()]] - code - tests/test_normalization.py
- [[.test_adjusted_close_preserved_when_different_from_close()]] - code - tests/test_normalization.py
- [[.test_adjusted_close_same_as_close_preserved()]] - code - tests/test_normalization.py
- [[.test_both_defaults_applied_together()]] - code - tests/test_normalization.py
- [[.test_close_not_overwritten_by_adjusted_close()]] - code - tests/test_normalization.py
- [[.test_data_as_of_defaults_to_trading_date()]] - code - tests/test_normalization.py
- [[.test_date_passes_through()]] - code - tests/test_normalization.py
- [[.test_datetime_converted_to_date()]] - code - tests/test_normalization.py
- [[.test_dividend_cash_defaults_to_zero()]] - code - tests/test_normalization.py
- [[.test_exchange_none_accepted()]] - code - tests/test_normalization.py
- [[.test_explicit_values_preserved()]] - code - tests/test_normalization.py
- [[.test_mix_of_valid_and_invalid_records()]] - code - tests/test_normalization.py
- [[.test_multiple_valid_records_all_normalized()]] - code - tests/test_normalization.py
- [[.test_negative_price_record_rejected()]] - code - tests/test_normalization.py
- [[.test_price_adjustment_set_from_provider_config()]] - code - tests/test_normalization.py
- [[.test_provenance_fields_populated_from_fetch_result()]] - code - tests/test_normalization.py
- [[.test_rejected_count_matches_number_of_failures()]] - code - tests/test_normalization.py
- [[.test_single_valid_record_normalized()]] - code - tests/test_normalization.py
- [[.test_split_factor_defaults_to_one()]] - code - tests/test_normalization.py
- [[.to_trading_date()_1]] - code - src/research_data/normalization.py
- [[A record with negative price should be rejected during normalization.]] - rationale - tests/test_normalization.py
- [[A single valid record should be normalized with provenance fields populated.]] - rationale - tests/test_normalization.py
- [[Both split_factor and dividend_cash should default when both are None.]] - rationale - tests/test_normalization.py
- [[Create a ProviderConfig with sensible defaults.]] - rationale - tests/test_normalization.py
- [[Create a ProviderFetchResult wrapping the given records.]] - rationale - tests/test_normalization.py
- [[Create a valid OHLCVRecord with optional overrides.]] - rationale - tests/test_normalization.py
- [[Default calendar that passes dates through unchanged.      Used when no market]] - rationale - src/research_data/normalization.py
- [[Even when adjusted_close equals close, both should be stored.]] - rationale - tests/test_normalization.py
- [[Generate ProviderFetchResult instances with records= (empty list).      This]] - rationale - tests/test_property_no_fabrication.py
- [[Multiple valid records should all be normalized.]] - rationale - tests/test_normalization.py
- [[NormalizationResult]] - code - src/research_data/normalization.py
- [[Normalize a ProviderFetchResult into canonical OHLCVRecord rows.      Takes a]] - rationale - src/research_data/normalization.py
- [[Normalize a single record by re-constructing it with corrected fields.      Th]] - rationale - src/research_data/normalization.py
- [[Normalizer converts provider-specific payloads into canonical OHLCVRecord rows.]] - rationale - src/research_data/normalization.py
- [[PassthroughCalendar]] - code - src/research_data/normalization.py
- [[Property-based tests for no data fabrication on empty provider response (Propert]] - rationale - tests/test_property_no_fabrication.py
- [[Provenance fields should come from the fetch result, not the original record.]] - rationale - tests/test_normalization.py
- [[Result of normalizing a provider fetch result.      Attributes         valid]] - rationale - src/research_data/normalization.py
- [[Return the date as-is (no timezone conversion).]] - rationale - src/research_data/normalization.py
- [[Test that adjusted_close is preserved separately from close.]] - rationale - tests/test_normalization.py
- [[Test that normalize_fetch_result converts valid records with correct provenance.]] - rationale - tests/test_normalization.py
- [[Test that normalizer sets default values for split_factor and dividend_cash.]] - rationale - tests/test_normalization.py
- [[Test that records failing validation are skipped with rejected_count incremented]] - rationale - tests/test_normalization.py
- [[Test the PassthroughCalendar default implementation.]] - rationale - tests/test_normalization.py
- [[TestNormalizeFetchResultValid]] - code - tests/test_normalization.py
- [[TestNormalizerAdjustedClose]] - code - tests/test_normalization.py
- [[TestNormalizerDefaults]] - code - tests/test_normalization.py
- [[TestNormalizerSkipsInvalidRecords]] - code - tests/test_normalization.py
- [[TestPassthroughCalendar]] - code - tests/test_normalization.py
- [[The close field should never be overwritten by adjusted_close.]] - rationale - tests/test_normalization.py
- [[Unit tests for the normalization module (Task 6.5).  Covers - normalize_fetc]] - rationale - tests/test_normalization.py
- [[Valid records should pass while invalid ones are rejected.]] - rationale - tests/test_normalization.py
- [[When data_as_of is the trading_date, it should be preserved.]] - rationale - tests/test_normalization.py
- [[When dividend_cash is None, normalizer should set it to 0.0.]] - rationale - tests/test_normalization.py
- [[When provider doesn't supply adjusted_close, it should remain None.]] - rationale - tests/test_normalization.py
- [[When split_factor and dividend_cash are explicitly set, they should be preserved]] - rationale - tests/test_normalization.py
- [[When split_factor is None, normalizer should set it to 1.0.]] - rationale - tests/test_normalization.py
- [[_make_fetch_result()]] - code - tests/test_normalization.py
- [[_make_provider_config()]] - code - tests/test_normalization.py
- [[_make_valid_record()]] - code - tests/test_normalization.py
- [[_normalize_record()]] - code - src/research_data/normalization.py
- [[adjusted_close should be stored separately even when different from close.]] - rationale - tests/test_normalization.py
- [[empty_provider_fetch_results()]] - code - tests/test_property_no_fabrication.py
- [[normalization.py]] - code - src/research_data/normalization.py
- [[normalize_fetch_result()]] - code - src/research_data/normalization.py
- [[price_adjustment should be derived from provider's adjustment_policy.]] - rationale - tests/test_normalization.py
- [[rejected_count should equal the number of failed records.]] - rationale - tests/test_normalization.py
- [[test_empty_response_implies_missing_quality_status()]] - code - tests/test_property_no_fabrication.py
- [[test_empty_response_produces_zero_normalized_records()]] - code - tests/test_property_no_fabrication.py
- [[test_empty_response_rejected_count_is_zero()]] - code - tests/test_property_no_fabrication.py
- [[test_normalization.py]] - code - tests/test_normalization.py
- [[test_property_no_fabrication.py]] - code - tests/test_property_no_fabrication.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Normalization_Pipeline
SORT file.name ASC
```

## Connections to other communities
- 10 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 10 edges to [[_COMMUNITY_OHLCVRecord Model & Validation Tests]]
- 9 edges to [[_COMMUNITY_Provider API-Key Validation]]
- 8 edges to [[_COMMUNITY_Adjustment Policy Mapping Tests]]
- 7 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 5 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 1 edge to [[_COMMUNITY_PriceProvider Protocol & MarketCalendarProtocol]]

## Top bridge nodes
- [[PassthroughCalendar]] - degree 18, connects to 5 communities
- [[NormalizationResult]] - degree 14, connects to 5 communities
- [[TestNormalizeFetchResultValid]] - degree 14, connects to 5 communities
- [[TestNormalizerAdjustedClose]] - degree 13, connects to 5 communities
- [[TestNormalizerDefaults]] - degree 13, connects to 5 communities