---
source_file: "tests/test_models.py"
type: "code"
community: "OHLCVRecord Model & Validation Tests"
location: "L251"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/OHLCVRecord_Model__Validation_Tests
---

# TestValidationSymbol

## Connections
- [[.test_empty_symbol_rejected()]] - `method` [EXTRACTED]
- [[.test_lowercase_symbol_rejected()]] - `method` [EXTRACTED]
- [[.test_mixed_case_symbol_rejected()]] - `method` [EXTRACTED]
- [[.test_single_char_symbol_accepted()]] - `method` [EXTRACTED]
- [[.test_symbol_too_long_rejected()]] - `method` [EXTRACTED]
- [[.test_symbol_with_digits_rejected()]] - `method` [EXTRACTED]
- [[.test_symbol_with_special_chars_rejected()]] - `method` [EXTRACTED]
- [[.test_ten_char_symbol_accepted()]] - `method` [EXTRACTED]
- [[DataEvidencePacket]] - `uses` [INFERRED]
- [[DataQualityReport]] - `uses` [INFERRED]
- [[EvidenceRef]] - `uses` [INFERRED]
- [[InsufficientDataError]] - `uses` [INFERRED]
- [[OHLCVRecord]] - `uses` [INFERRED]
- [[PriceAdjustment]] - `uses` [INFERRED]
- [[ProviderCapabilities]] - `uses` [INFERRED]
- [[ProviderFetchResult]] - `uses` [INFERRED]
- [[QualityStatus]] - `uses` [INFERRED]
- [[Requirement 5.7 symbol must be uppercase ASCII, max 10 chars.]] - `rationale_for` [EXTRACTED]
- [[test_models.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/OHLCVRecord_Model__Validation_Tests