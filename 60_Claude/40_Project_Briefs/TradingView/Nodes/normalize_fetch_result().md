---
source_file: "src/research_data/normalization.py"
type: "code"
community: "Normalization Pipeline"
location: "L115"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Normalization_Pipeline
---

# normalize_fetch_result()

## Connections
- [[.test_adjusted_close_none_when_not_supplied()]] - `calls` [INFERRED]
- [[.test_adjusted_close_preserved_when_different_from_close()]] - `calls` [INFERRED]
- [[.test_adjusted_close_same_as_close_preserved()]] - `calls` [INFERRED]
- [[.test_both_defaults_applied_together()]] - `calls` [INFERRED]
- [[.test_close_not_overwritten_by_adjusted_close()]] - `calls` [INFERRED]
- [[.test_data_as_of_defaults_to_trading_date()]] - `calls` [INFERRED]
- [[.test_dividend_cash_defaults_to_zero()]] - `calls` [INFERRED]
- [[.test_explicit_values_preserved()]] - `calls` [INFERRED]
- [[.test_mix_of_valid_and_invalid_records()]] - `calls` [INFERRED]
- [[.test_multiple_valid_records_all_normalized()]] - `calls` [INFERRED]
- [[.test_negative_price_record_rejected()]] - `calls` [INFERRED]
- [[.test_price_adjustment_set_from_provider_config()]] - `calls` [INFERRED]
- [[.test_provenance_fields_populated_from_fetch_result()]] - `calls` [INFERRED]
- [[.test_rejected_count_matches_number_of_failures()]] - `calls` [INFERRED]
- [[.test_single_valid_record_normalized()]] - `calls` [INFERRED]
- [[.test_split_factor_defaults_to_one()]] - `calls` [INFERRED]
- [[NormalizationResult]] - `calls` [EXTRACTED]
- [[Normalize a ProviderFetchResult into canonical OHLCVRecord rows.      Takes a]] - `rationale_for` [EXTRACTED]
- [[PassthroughCalendar]] - `calls` [EXTRACTED]
- [[_normalize_record()]] - `calls` [EXTRACTED]
- [[map_adjustment_policy()]] - `calls` [EXTRACTED]
- [[normalization.py]] - `contains` [EXTRACTED]
- [[test_empty_response_implies_missing_quality_status()]] - `calls` [INFERRED]
- [[test_empty_response_produces_zero_normalized_records()]] - `calls` [INFERRED]
- [[test_empty_response_rejected_count_is_zero()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Normalization_Pipeline