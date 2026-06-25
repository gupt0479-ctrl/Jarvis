---
type: community
cohesion: 0.05
members: 92
---

# OHLCVRecord Model & Validation Tests

**Cohesion:** 0.05 - loosely connected
**Members:** 92 nodes

## Members
- [[.test_empty_symbol_rejected()]] - code - tests/test_models.py
- [[.test_enum_in_model_json_deserialization()]] - code - tests/test_models.py
- [[.test_etf_asset_type()]] - code - tests/test_models.py
- [[.test_full_record_all_fields()]] - code - tests/test_models.py
- [[.test_future_data_as_of_rejected()]] - code - tests/test_models.py
- [[.test_future_trading_date_rejected()]] - code - tests/test_models.py
- [[.test_high_equals_open_close_low()]] - code - tests/test_models.py
- [[.test_lowercase_symbol_rejected()]] - code - tests/test_models.py
- [[.test_minimal_record_optional_fields_none()]] - code - tests/test_models.py
- [[.test_mixed_case_symbol_rejected()]] - code - tests/test_models.py
- [[.test_negative_adjusted_close_rejected()]] - code - tests/test_models.py
- [[.test_negative_close_rejected()]] - code - tests/test_models.py
- [[.test_negative_high_rejected()]] - code - tests/test_models.py
- [[.test_negative_low_rejected()]] - code - tests/test_models.py
- [[.test_negative_open_rejected()]] - code - tests/test_models.py
- [[.test_none_adjusted_close_accepted()]] - code - tests/test_models.py
- [[.test_reject_empty_raw_payload_hash()]] - code - tests/test_models_validation.py
- [[.test_reject_empty_symbol()]] - code - tests/test_models_validation.py
- [[.test_reject_future_data_as_of()]] - code - tests/test_models_validation.py
- [[.test_reject_future_trading_date()]] - code - tests/test_models_validation.py
- [[.test_reject_high_less_than_close()]] - code - tests/test_models_validation.py
- [[.test_reject_high_less_than_open()]] - code - tests/test_models_validation.py
- [[.test_reject_low_greater_than_close()]] - code - tests/test_models_validation.py
- [[.test_reject_low_greater_than_open()]] - code - tests/test_models_validation.py
- [[.test_reject_lowercase_symbol()]] - code - tests/test_models_validation.py
- [[.test_reject_mixed_case_symbol()]] - code - tests/test_models_validation.py
- [[.test_reject_negative_adjusted_close()]] - code - tests/test_models_validation.py
- [[.test_reject_negative_open()]] - code - tests/test_models_validation.py
- [[.test_reject_negative_volume()]] - code - tests/test_models_validation.py
- [[.test_reject_non_positive_adjusted_close()]] - code - tests/test_models_validation.py
- [[.test_reject_non_positive_close()]] - code - tests/test_models_validation.py
- [[.test_reject_non_positive_open()]] - code - tests/test_models_validation.py
- [[.test_reject_symbol_too_long()]] - code - tests/test_models_validation.py
- [[.test_reject_symbol_with_numbers()]] - code - tests/test_models_validation.py
- [[.test_reject_whitespace_raw_payload_hash()]] - code - tests/test_models_validation.py
- [[.test_single_char_symbol_accepted()]] - code - tests/test_models.py
- [[.test_symbol_too_long_rejected()]] - code - tests/test_models.py
- [[.test_symbol_with_digits_rejected()]] - code - tests/test_models.py
- [[.test_symbol_with_special_chars_rejected()]] - code - tests/test_models.py
- [[.test_ten_char_symbol_accepted()]] - code - tests/test_models.py
- [[.test_today_trading_date_accepted()]] - code - tests/test_models.py
- [[.test_valid_record_construction()]] - code - tests/test_models_validation.py
- [[.test_valid_record_with_adjusted_close()]] - code - tests/test_models_validation.py
- [[.test_valid_record_with_zero_volume()]] - code - tests/test_models_validation.py
- [[.test_zero_adjusted_close_rejected()]] - code - tests/test_models.py
- [[.test_zero_close_rejected()]] - code - tests/test_models.py
- [[.test_zero_high_rejected()]] - code - tests/test_models.py
- [[.test_zero_low_rejected()]] - code - tests/test_models.py
- [[.test_zero_open_rejected()]] - code - tests/test_models.py
- [[.test_zero_volume_accepted()]] - code - tests/test_models.py
- [[All prices equal is valid (flat day).]] - rationale - tests/test_models.py
- [[Canonical normalized daily price record with full provenance fields.      Vali]] - rationale - src/research_data/models.py
- [[Comprehensive unit tests for research_data models (Task 1.4).  Covers - Vali]] - rationale - tests/test_models.py
- [[OHLCVRecord]] - code - src/research_data/models.py
- [[Property 1 OHLCV Validation Rejects Invalid Records.      Validates Requir]] - rationale - tests/test_property_ohlcv_validation.py
- [[Property-based tests for OHLCV validation (Property 1).  Property 1 OHLCV Val]] - rationale - tests/test_property_ohlcv_validation.py
- [[Pydantic should accept string values for enum fields.]] - rationale - tests/test_models.py
- [[Requirement 5.1 open, high, low, close must be  0.]] - rationale - tests/test_models.py
- [[Requirement 5.5 adjusted_close, if present, must be  0.]] - rationale - tests/test_models.py
- [[Requirement 5.6 trading_date and data_as_of cannot be in the future.]] - rationale - tests/test_models.py
- [[Requirement 5.7 symbol must be uppercase ASCII, max 10 chars.]] - rationale - tests/test_models.py
- [[Return a valid OHLCVRecord dict with optional overrides.]] - rationale - tests/test_models_validation.py
- [[Return a valid record dict with overrides applied.]] - rationale - tests/test_property_ohlcv_validation.py
- [[Return kwargs for a valid OHLCVRecord with optional overrides.]] - rationale - tests/test_models.py
- [[Test that valid OHLCVRecord construction succeeds with all fields.]] - rationale - tests/test_models.py
- [[TestOHLCVRecordValid]] - code - tests/test_models_validation.py
- [[TestOHLCVRecordValidConstruction]] - code - tests/test_models.py
- [[TestOHLCVRecordValidation]] - code - tests/test_models_validation.py
- [[TestProperty1OHLCVValidationRejectsInvalid]] - code - tests/test_property_ohlcv_validation.py
- [[TestValidationAdjustedClose]] - code - tests/test_models.py
- [[TestValidationFutureDates]] - code - tests/test_models.py
- [[TestValidationNonPositivePrices]] - code - tests/test_models.py
- [[TestValidationSymbol]] - code - tests/test_models.py
- [[_make_record()]] - code - tests/test_property_ohlcv_validation.py
- [[_valid_record()]] - code - tests/test_models_validation.py
- [[_valid_record_kwargs()]] - code - tests/test_models.py
- [[test_models.py]] - code - tests/test_models.py
- [[test_property_ohlcv_validation.py]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_empty_raw_payload_hash()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_future_data_as_of()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_future_trading_date()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_high_less_than_close()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_high_less_than_open()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_invalid_symbols()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_low_greater_than_close()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_low_greater_than_open()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_negative_volume()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_non_positive_adjusted_close()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_non_positive_close()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_non_positive_high()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_non_positive_low()]] - code - tests/test_property_ohlcv_validation.py
- [[test_rejects_non_positive_open()]] - code - tests/test_property_ohlcv_validation.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/OHLCVRecord_Model__Validation_Tests
SORT file.name ASC
```

## Connections to other communities
- 28 edges to [[_COMMUNITY_Evidence Packet Models]]
- 13 edges to [[_COMMUNITY_QualityStatus  PriceAdjustment Enums]]
- 12 edges to [[_COMMUNITY_ProviderFetchResult Model]]
- 10 edges to [[_COMMUNITY_Normalization Pipeline]]
- 10 edges to [[_COMMUNITY_ProviderCapabilities Model]]
- 10 edges to [[_COMMUNITY_DataQualityReport Model]]
- 10 edges to [[_COMMUNITY_InsufficientDataError]]
- 9 edges to [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators]]
- 6 edges to [[_COMMUNITY_DuckDB Schema Init & Duplicate-PK Handling]]
- 6 edges to [[_COMMUNITY_Requirement 5.2 High Relationship Tests]]
- 6 edges to [[_COMMUNITY_Raw Payload Hash Validation Tests]]
- 5 edges to [[_COMMUNITY_AssetUniverse Config & DuckDB Storage]]
- 4 edges to [[_COMMUNITY_Model Enum Validation Smoke Tests]]
- 2 edges to [[_COMMUNITY_Adjustment Policy Mapping Tests]]
- 2 edges to [[_COMMUNITY_DataEvidencePacket Construction Tests]]
- 2 edges to [[_COMMUNITY_Data Quality Auditor]]
- 2 edges to [[_COMMUNITY_PriceReadAPI]]
- 2 edges to [[_COMMUNITY_CSV Fixture Provider]]
- 1 edge to [[_COMMUNITY_Secret Redaction]]
- 1 edge to [[_COMMUNITY_PriceProvider Protocol & MarketCalendarProtocol]]

## Top bridge nodes
- [[OHLCVRecord]] - degree 132, connects to 20 communities
- [[test_models.py]] - degree 17, connects to 9 communities
- [[TestOHLCVRecordValidation]] - degree 29, connects to 8 communities
- [[TestOHLCVRecordValid]] - degree 13, connects to 8 communities
- [[TestValidationNonPositivePrices]] - degree 19, connects to 7 communities