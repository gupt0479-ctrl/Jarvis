---
source_file: "tests/test_normalization.py"
type: "code"
community: "Normalization Pipeline"
location: "L105"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Normalization_Pipeline
---

# TestNormalizeFetchResultValid

## Connections
- [[.test_data_as_of_defaults_to_trading_date()]] - `method` [EXTRACTED]
- [[.test_multiple_valid_records_all_normalized()]] - `method` [EXTRACTED]
- [[.test_price_adjustment_set_from_provider_config()]] - `method` [EXTRACTED]
- [[.test_provenance_fields_populated_from_fetch_result()]] - `method` [EXTRACTED]
- [[.test_single_valid_record_normalized()]] - `method` [EXTRACTED]
- [[NormalizationResult]] - `uses` [INFERRED]
- [[OHLCVRecord]] - `uses` [INFERRED]
- [[PassthroughCalendar]] - `uses` [INFERRED]
- [[PriceAdjustment]] - `uses` [INFERRED]
- [[ProviderConfig]] - `uses` [INFERRED]
- [[ProviderFetchResult]] - `uses` [INFERRED]
- [[QualityStatus]] - `uses` [INFERRED]
- [[Test that normalize_fetch_result converts valid records with correct provenance.]] - `rationale_for` [EXTRACTED]
- [[test_normalization.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Normalization_Pipeline