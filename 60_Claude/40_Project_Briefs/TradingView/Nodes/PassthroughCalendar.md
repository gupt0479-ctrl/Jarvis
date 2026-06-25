---
source_file: "src/research_data/normalization.py"
type: "code"
community: "Normalization Pipeline"
location: "L41"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Normalization_Pipeline
---

# PassthroughCalendar

## Connections
- [[.test_date_passes_through()]] - `calls` [INFERRED]
- [[.test_datetime_converted_to_date()]] - `calls` [INFERRED]
- [[.test_exchange_none_accepted()]] - `calls` [INFERRED]
- [[.to_trading_date()_1]] - `method` [EXTRACTED]
- [[Default calendar that passes dates through unchanged.      Used when no market]] - `rationale_for` [EXTRACTED]
- [[OHLCVRecord]] - `uses` [INFERRED]
- [[PriceAdjustment]] - `uses` [INFERRED]
- [[ProviderConfig]] - `uses` [INFERRED]
- [[ProviderFetchResult]] - `uses` [INFERRED]
- [[TestMapAdjustmentPolicyKnown]] - `uses` [INFERRED]
- [[TestMapAdjustmentPolicyUnknown]] - `uses` [INFERRED]
- [[TestNormalizeFetchResultValid]] - `uses` [INFERRED]
- [[TestNormalizerAdjustedClose]] - `uses` [INFERRED]
- [[TestNormalizerDefaults]] - `uses` [INFERRED]
- [[TestNormalizerSkipsInvalidRecords]] - `uses` [INFERRED]
- [[TestPassthroughCalendar]] - `uses` [INFERRED]
- [[normalization.py]] - `contains` [EXTRACTED]
- [[normalize_fetch_result()]] - `calls` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Normalization_Pipeline