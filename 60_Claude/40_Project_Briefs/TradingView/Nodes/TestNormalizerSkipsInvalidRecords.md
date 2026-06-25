---
source_file: "tests/test_normalization.py"
type: "code"
community: "Normalization Pipeline"
location: "L247"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Normalization_Pipeline
---

# TestNormalizerSkipsInvalidRecords

## Connections
- [[.test_mix_of_valid_and_invalid_records()]] - `method` [EXTRACTED]
- [[.test_negative_price_record_rejected()]] - `method` [EXTRACTED]
- [[.test_rejected_count_matches_number_of_failures()]] - `method` [EXTRACTED]
- [[NormalizationResult]] - `uses` [INFERRED]
- [[OHLCVRecord]] - `uses` [INFERRED]
- [[PassthroughCalendar]] - `uses` [INFERRED]
- [[PriceAdjustment]] - `uses` [INFERRED]
- [[ProviderConfig]] - `uses` [INFERRED]
- [[ProviderFetchResult]] - `uses` [INFERRED]
- [[QualityStatus]] - `uses` [INFERRED]
- [[Test that records failing validation are skipped with rejected_count incremented]] - `rationale_for` [EXTRACTED]
- [[test_normalization.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Normalization_Pipeline