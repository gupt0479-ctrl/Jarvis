# Graph Report - /home/anant_gupta/projects/hub/tradingview  (2026-06-25)

## Corpus Check
- Corpus is ~27,519 words - fits in a single context window. You may not need a graph.

## Summary
- 981 nodes · 1929 edges · 95 communities (49 shown, 46 thin omitted)
- Extraction: 63% EXTRACTED · 37% INFERRED · 0% AMBIGUOUS · INFERRED: 715 edges (avg confidence: 0.63)
- Token cost: 0 input · 145,907 output

## Community Hubs (Navigation)
- [[_COMMUNITY_OHLCVRecord Model & Validation Tests|OHLCVRecord Model & Validation Tests]]
- [[_COMMUNITY_Normalization Pipeline|Normalization Pipeline]]
- [[_COMMUNITY_AssetUniverse Config & DuckDB Storage|Asset/Universe Config & DuckDB Storage]]
- [[_COMMUNITY_Data Quality Auditor|Data Quality Auditor]]
- [[_COMMUNITY_Quant Foundations & SECEDGAR Reference Docs|Quant Foundations & SEC/EDGAR Reference Docs]]
- [[_COMMUNITY_DuckDB Schema Init & Duplicate-PK Handling|DuckDB Schema Init & Duplicate-PK Handling]]
- [[_COMMUNITY_Adjustment Policy Mapping Tests|Adjustment Policy Mapping Tests]]
- [[_COMMUNITY_Secret Redaction|Secret Redaction]]
- [[_COMMUNITY_Provider Registry|Provider Registry]]
- [[_COMMUNITY_Market Calendar Core|Market Calendar Core]]
- [[_COMMUNITY_Provider Config Loading & Validation|Provider Config Loading & Validation]]
- [[_COMMUNITY_Ingestion Data Flow & Module Map|Ingestion Data Flow & Module Map]]
- [[_COMMUNITY_QualityStatus  PriceAdjustment Enums|QualityStatus / PriceAdjustment Enums]]
- [[_COMMUNITY_Evidence Packet Models|Evidence Packet Models]]
- [[_COMMUNITY_App Config Loading|App Config Loading]]
- [[_COMMUNITY_Provider Landscape & Backup Sources|Provider Landscape & Backup Sources]]
- [[_COMMUNITY_Provider API-Key Validation|Provider API-Key Validation]]
- [[_COMMUNITY_AI-Ready Evidence Contract & Schemas|AI-Ready Evidence Contract & Schemas]]
- [[_COMMUNITY_Latest Expected Session (1600 ET) Logic|Latest Expected Session (16:00 ET) Logic]]
- [[_COMMUNITY_Calendar Holiday Exclusion Tests|Calendar Holiday Exclusion Tests]]
- [[_COMMUNITY_Missing Sessions Detection Tests|Missing Sessions Detection Tests]]
- [[_COMMUNITY_Is-Trading-Day Tests|Is-Trading-Day Tests]]
- [[_COMMUNITY_Data Ingestion Foundation Spec Overview|Data Ingestion Foundation Spec Overview]]
- [[_COMMUNITY_Spec RequirementsPropertiesTasks Cross-Refs|Spec Requirements/Properties/Tasks Cross-Refs]]
- [[_COMMUNITY_InsufficientDataError|InsufficientDataError]]
- [[_COMMUNITY_PriceAdjustment Enum & HighLow Validators|PriceAdjustment Enum & High/Low Validators]]
- [[_COMMUNITY_Calendar Unsupported-Range Error Handling|Calendar Unsupported-Range Error Handling]]
- [[_COMMUNITY_Trading Session Weekend Exclusion Tests|Trading Session Weekend Exclusion Tests]]
- [[_COMMUNITY_CSV Fixture Provider|CSV Fixture Provider]]
- [[_COMMUNITY_Provider Protocol & FabricationQuality Properties|Provider Protocol & Fabrication/Quality Properties]]
- [[_COMMUNITY_MarketCalendar & CalendarError|MarketCalendar & CalendarError]]
- [[_COMMUNITY_Project Guardrails (Non-Negotiable Rules)|Project Guardrails (Non-Negotiable Rules)]]
- [[_COMMUNITY_DataEvidencePacket Construction Tests|DataEvidencePacket Construction Tests]]
- [[_COMMUNITY_ProviderFetchResult Model|ProviderFetchResult Model]]
- [[_COMMUNITY_DataQualityReport Model|DataQualityReport Model]]
- [[_COMMUNITY_Provider Registry Config-Loading Tests|Provider Registry Config-Loading Tests]]
- [[_COMMUNITY_Ingestion Architecture Diagram & Components|Ingestion Architecture Diagram & Components]]
- [[_COMMUNITY_NormalizerCalendar Properties & csv_fixture Entry|Normalizer/Calendar Properties & csv_fixture Entry]]
- [[_COMMUNITY_ProviderCapabilities Model|ProviderCapabilities Model]]
- [[_COMMUNITY_PriceReadAPI|PriceReadAPI]]
- [[_COMMUNITY_PriceProvider Protocol & MarketCalendarProtocol|PriceProvider Protocol & MarketCalendarProtocol]]
- [[_COMMUNITY_Provider Registry Internals|Provider Registry Internals]]
- [[_COMMUNITY_Provider Registry Missing-Config Tests|Provider Registry Missing-Config Tests]]
- [[_COMMUNITY_Benchmark Reporter & CLI Design|Benchmark Reporter & CLI Design]]
- [[_COMMUNITY_Evidence Packet & Read API Properties|Evidence Packet & Read API Properties]]
- [[_COMMUNITY_2026 Research Baseline (FinGPTFinRobotFINRASEC)|2026 Research Baseline (FinGPT/FinRobot/FINRA/SEC)]]
- [[_COMMUNITY_Model Enum Validation Smoke Tests|Model Enum Validation Smoke Tests]]
- [[_COMMUNITY_V1 Universe Config (assets.toml)|V1 Universe Config (assets.toml)]]
- [[_COMMUNITY_Requirement 5.2 High Relationship Tests|Requirement 5.2: High Relationship Tests]]
- [[_COMMUNITY_Raw Payload Hash Validation Tests|Raw Payload Hash Validation Tests]]
- [[_COMMUNITY_Market Calendar Unit Test Setup|Market Calendar Unit Test Setup]]
- [[_COMMUNITY_research_data Package Init|research_data Package Init]]
- [[_COMMUNITY_providers Package Init|providers Package Init]]
- [[_COMMUNITY_Property Empty Response - Zero Records|Property: Empty Response -> Zero Records]]
- [[_COMMUNITY_Property Empty Response - Zero Rejected|Property: Empty Response -> Zero Rejected]]
- [[_COMMUNITY_Property Empty Response - MISSING Status|Property: Empty Response -> MISSING Status]]
- [[_COMMUNITY_Adjustment Policy CaseWhitespace Normalization|Adjustment Policy: Case/Whitespace Normalization]]
- [[_COMMUNITY_Adjustment Policy Unknown String - UNKNOWN|Adjustment Policy: Unknown String -> UNKNOWN]]
- [[_COMMUNITY_Adjustment Policy Empty String - UNKNOWN|Adjustment Policy: Empty String -> UNKNOWN]]
- [[_COMMUNITY_Raw Payload Hash Round-Trip Check|Raw Payload Hash Round-Trip Check]]
- [[_COMMUNITY_OHLCVRecord DuckDB Round-Trip Check|OHLCVRecord DuckDB Round-Trip Check]]
- [[_COMMUNITY_Duplicate PK Upsert Behavior|Duplicate PK Upsert Behavior]]
- [[_COMMUNITY_Req 5.1 Open Must Be Positive|Req 5.1: Open Must Be Positive]]
- [[_COMMUNITY_Req 5.1 High Must Be Positive|Req 5.1: High Must Be Positive]]
- [[_COMMUNITY_Req 5.1 Low Must Be Positive|Req 5.1: Low Must Be Positive]]
- [[_COMMUNITY_Req 5.1 Close Must Be Positive|Req 5.1: Close Must Be Positive]]
- [[_COMMUNITY_Req 5.2 High = Open|Req 5.2: High >= Open]]
- [[_COMMUNITY_Req 5.2 High = Close|Req 5.2: High >= Close]]
- [[_COMMUNITY_Req 5.3 Low = Open|Req 5.3: Low <= Open]]
- [[_COMMUNITY_Req 5.3 Low = Close|Req 5.3: Low <= Close]]
- [[_COMMUNITY_Req 5.4 Volume Non-Negative|Req 5.4: Volume Non-Negative]]
- [[_COMMUNITY_Req 5.5 Adjusted Close Must Be Positive|Req 5.5: Adjusted Close Must Be Positive]]
- [[_COMMUNITY_Req 5.6 Trading Date Not Future|Req 5.6: Trading Date Not Future]]
- [[_COMMUNITY_Req 5.6 Data-As-Of Not Future|Req 5.6: Data-As-Of Not Future]]
- [[_COMMUNITY_Req 5.7 Symbol Format (Uppercase, =10 chars)|Req 5.7: Symbol Format (Uppercase, <=10 chars)]]
- [[_COMMUNITY_Req 5.8 Raw Payload Hash Non-Empty|Req 5.8: Raw Payload Hash Non-Empty]]
- [[_COMMUNITY_Req 6.2 No Weekend Sessions|Req 6.2: No Weekend Sessions]]
- [[_COMMUNITY_Req 6.4 Sessions Within Requested Range|Req 6.4: Sessions Within Requested Range]]
- [[_COMMUNITY_Req 6.2 Exchange Holidays Excluded|Req 6.2: Exchange Holidays Excluded]]
- [[_COMMUNITY_Req 6.2 NASDAQ Weekend Exclusion|Req 6.2: NASDAQ Weekend Exclusion]]
- [[_COMMUNITY_Sessions Returned Chronologically|Sessions Returned Chronologically]]
- [[_COMMUNITY_Secret Redaction Field-Preservation Check|Secret Redaction Field-Preservation Check]]
- [[_COMMUNITY_Provider Config Missing-Fields Error Check|Provider Config Missing-Fields Error Check]]
- [[_COMMUNITY_Symbol Format Validation Rule|Symbol Format Validation Rule]]
- [[_COMMUNITY_OHLC Positivity Validation Rule|OHLC Positivity Validation Rule]]
- [[_COMMUNITY_Volume Non-Negativity Rule|Volume Non-Negativity Rule]]
- [[_COMMUNITY_Adjusted Close Positivity Rule|Adjusted Close Positivity Rule]]
- [[_COMMUNITY_Raw Payload Hash Non-Empty Rule|Raw Payload Hash Non-Empty Rule]]
- [[_COMMUNITY_OHLC Relationship Validation Rule|OHLC Relationship Validation Rule]]
- [[_COMMUNITY_Date-Not-In-Future Validation Rule|Date-Not-In-Future Validation Rule]]
- [[_COMMUNITY_Default Provider Name Lookup|Default Provider Name Lookup]]
- [[_COMMUNITY_ingestion_runs Table Schema|ingestion_runs Table Schema]]
- [[_COMMUNITY_Design Doc Performance Section|Design Doc: Performance Section]]
- [[_COMMUNITY_DuckDB Python API Reference|DuckDB Python API Reference]]

## God Nodes (most connected - your core abstractions)
1. `OHLCVRecord` - 132 edges
2. `ProviderFetchResult` - 58 edges
3. `PriceAdjustment` - 54 edges
4. `QualityStatus` - 51 edges
5. `_valid_record_kwargs()` - 40 edges
6. `ProviderConfig` - 35 edges
7. `ProviderCapabilities` - 34 edges
8. `InsufficientDataError` - 33 edges
9. `DataQualityReport` - 32 edges
10. `ProviderRegistry` - 31 edges

## Surprising Connections (you probably didn't know these)
- `FinRobot (specialized financial agents)` --semantically_similar_to--> `Multi-Agent Research Design`  [INFERRED] [semantically similar]
  .kiro/specs/data-ingestion-foundation/design.md → Docs/RESEARCH.md
- `Evidence Card JSON Shape` --semantically_similar_to--> `DataEvidencePacket Model`  [INFERRED] [semantically similar]
  Docs/RESEARCH.md → .kiro/specs/data-ingestion-foundation/design.md
- `Risk Manager Agent` --semantically_similar_to--> `data_quality_reports Schema`  [INFERRED] [semantically similar]
  Docs/RESEARCH.md → .kiro/specs/data-ingestion-foundation/design.md
- `Research Desk Data Flow` --semantically_similar_to--> `Ingestion Data Flow (provider -> raw payload -> normalization -> quality -> read API -> evidence)`  [INFERRED] [semantically similar]
  Docs/RESEARCH.md → CLAUDE.md
- `Evidence Card Cautious Action Labels` --semantically_similar_to--> `Evidence Card Action Labels (WATCH|HOLD|ACCUMULATE|REDUCE|AVOID|INSUFFICIENT_DATA)`  [INFERRED] [semantically similar]
  Docs/RESEARCH.md → CLAUDE.md

## Hyperedges (group relationships)
- **Ingestion Pipeline Component Chain (Provider Registry through Data Quality Auditor)** — design_provider_registry_component, design_provider_fetchers_component, design_raw_payload_writer_component, design_normalizer_component, design_market_calendar_component, design_data_quality_auditor_component [EXTRACTED 1.00]
- **research_data Module Map (models, config, storage, normalization, calendar, quality, read_api)** — claudemd_models_py, claudemd_config_py, claudemd_storage_py, claudemd_normalization_py, claudemd_calendar_py, claudemd_quality_py, claudemd_read_api_py [EXTRACTED 1.00]
- **Multi-Agent Research Design Roles** — research_technical_analyst_agent, research_fundamentals_analyst_agent, research_sentiment_news_analyst_agent, research_bull_case_analyst_agent, research_bear_case_analyst_agent, research_risk_manager_agent, research_portfolio_allocation_reviewer_agent, research_student_tutor_agent [EXTRACTED 1.00]

## Communities (95 total, 46 thin omitted)

### Community 0 - "OHLCVRecord Model & Validation Tests"
Cohesion: 0.05
Nodes (40): OHLCVRecord, Canonical normalized daily price record with full provenance fields.      Vali, Comprehensive unit tests for research_data models (Task 1.4).  Covers: - Vali, All prices equal is valid (flat day)., Requirement 5.1: open, high, low, close must be > 0., Requirement 5.5: adjusted_close, if present, must be > 0., Requirement 5.6: trading_date and data_as_of cannot be in the future., Requirement 5.7: symbol must be uppercase ASCII, max 10 chars. (+32 more)

### Community 1 - "Normalization Pipeline"
Cohesion: 0.06
Nodes (49): NormalizationResult, normalize_fetch_result(), _normalize_record(), PassthroughCalendar, Normalizer: converts provider-specific payloads into canonical OHLCVRecord rows., Normalize a ProviderFetchResult into canonical OHLCVRecord rows.      Takes a, Normalize a single record by re-constructing it with corrected fields.      Th, Default calendar that passes dates through unchanged.      Used when no market (+41 more)

### Community 2 - "Asset/Universe Config & DuckDB Storage"
Cohesion: 0.05
Nodes (49): AssetConfig, Configuration for a single asset in the universe., Configuration for the asset universe., UniverseConfig, batch_insert_ohlcv(), _detect_payload_format(), DuckDB storage layer for the research data system.  Provides schema initializa, Insert OHLCV records in batches with upsert semantics.      Inserts up to batc (+41 more)

### Community 3 - "Data Quality Auditor"
Cohesion: 0.05
Nodes (43): DataQualityAuditor, Data Quality Auditor for the research data system.  Evaluates symbol-level and, Compare OHLCV fields between two providers for the same symbol/date., Detect records with impossible OHLC relationships.          Checks for:, Check if the latest bar is older than the latest expected session.          Ar, Detect duplicate trading_dates in the records.          Returns:, Evaluates symbol-level data quality and generates quality reports.      Uses M, Detect non-monotonic (out-of-order) trading_dates.          Checks that dates (+35 more)

### Community 4 - "Quant Foundations & SEC/EDGAR Reference Docs"
Cohesion: 0.06
Nodes (43): SEC Accessing EDGAR Data, SEC EDGAR APIs (design source), Quant Foundations: roadmap for quant trading/research interview prep, Project: Market Microstructure Simulator, Project: Monte Carlo Pricing Engine, Project: Optimal Stopping Simulation, Probability Fundamentals (quant interview prep), Disciplined Quant Problem-Solving Method (+35 more)

### Community 5 - "DuckDB Schema Init & Duplicate-PK Handling"
Cohesion: 0.06
Nodes (30): init_db(), Create all required tables and indexes using CREATE TABLE IF NOT EXISTS., ohlcv_prices(), Property-based tests for duplicate primary key handling (Property 12).  Proper, Property 12: Duplicate Primary Key Rejection.      When two records share the, Generate valid OHLC prices satisfying high >= open/close >= low., Generate a valid OHLCVRecord with optional fixed PK fields., test_upsert_overwrites_duplicate_pk() (+22 more)

### Community 6 - "Adjustment Policy Mapping Tests"
Cohesion: 0.1
Nodes (14): map_adjustment_policy(), Map a provider's adjustment_policy string to a PriceAdjustment enum value., Test that map_adjustment_policy maps recognized policies correctly., Policy mapping should be case-insensitive., Leading/trailing whitespace should be stripped., Test that map_adjustment_policy returns UNKNOWN for unrecognized values., TestMapAdjustmentPolicyKnown, TestMapAdjustmentPolicyUnknown (+6 more)

### Community 7 - "Secret Redaction"
Cohesion: 0.13
Nodes (13): Redact secret values from request metadata.      Matches field names containin, redact_secrets(), Test that redact_secrets properly redacts secret field values. Requirements 3.5,, Fields containing 'key' should be redacted., Fields containing 'token' should be redacted., Fields containing 'secret' should be redacted., Fields containing 'password' should be redacted., Fields containing 'authorization' should be redacted. (+5 more)

### Community 8 - "Provider Registry"
Cohesion: 0.13
Nodes (13): ProviderRegistry, Return a sorted list of all registered provider names., Return the configuration for a named provider.          Args:             nam, Return a concrete provider instance by name.          Validates that the requi, Return the capabilities for a named provider.          Exposes provider capabi, Validate that a provider name is registered.          Raises:             Con, Registry that loads provider configuration and returns concrete provider instanc, Test that unknown provider names are rejected with helpful error messages. (+5 more)

### Community 9 - "Market Calendar Core"
Cohesion: 0.13
Nodes (16): MarketCalendar, Return expected trading sessions in the given date range.          Args:, Return trading sessions in the range that are not in actual_dates.          Ar, Determines expected trading sessions for US equity exchanges.      Supports NY, Initialize calendar instances for supported exchanges., Validate that the requested date range is within the calendar's bounds., date_ranges(), Property-based tests for Market Calendar (Property 6).  Property 6: Market Cal (+8 more)

### Community 10 - "Provider Config Loading & Validation"
Cohesion: 0.12
Nodes (14): load_providers_config(), Validate a single provider entry, returning list of missing fields., Load and validate providers.toml configuration.      Returns a tuple of (provi, _validate_provider_entry(), A provider missing multiple required fields lists all missing fields., Error message identifies the provider name with missing fields., Test that invalid TOML syntax produces clear parse error messages., Invalid TOML syntax raises ConfigError mentioning parse failure. (+6 more)

### Community 11 - "Ingestion Data Flow & Module Map"
Cohesion: 0.16
Nodes (19): calendar.py, daily_ohlcv table, Ingestion Data Flow (provider -> raw payload -> normalization -> quality -> read API -> evidence), data_quality_reports table, Evidence Card Action Labels (WATCH|HOLD|ACCUMULATE|REDUCE|AVOID|INSUFFICIENT_DATA), ingestion_runs table, models.py, research_data Module Map (+11 more)

### Community 12 - "QualityStatus / PriceAdjustment Enums"
Cohesion: 0.13
Nodes (8): QualityStatus, Classification of data quality for a symbol or record., Test enum serialization (to string) and deserialization (from string)., Enum .value gives the serialized string form., QualityStatus inherits from str, so it can be compared to its value., Enum .value gives the serialized string form., PriceAdjustment inherits from str, so it can be compared to its value., TestEnumSerialization

### Community 13 - "Evidence Packet Models"
Cohesion: 0.17
Nodes (10): BaseModel, DataEvidencePacket, EvidenceRef, Reference to a specific row in a data table for provenance tracking., Structured evidence packet with full provenance for downstream AI consumption., Requirement 5.3: low must be <= open, close., Requirement 5.4: volume must be >= 0., TestValidationLowRelationships (+2 more)

### Community 14 - "App Config Loading"
Cohesion: 0.18
Nodes (15): AppConfig, ConfigError, _find_config_dir(), load_assets_config(), load_config(), _load_toml_file(), Configuration loading and validation for research_data.  Loads and validates T, Load and parse a TOML file, raising ConfigError on failure. (+7 more)

### Community 15 - "Provider Landscape & Backup Sources"
Cohesion: 0.15
Nodes (16): Alpha Vantage Documentation, Alpha Vantage Support Page, Backup Providers Table, FMP Quickstart Docs, OpenBB Docs, Polygon Basic as V1 Default Provider, Polygon Stocks Pricing Page, Provider Selection Rules (+8 more)

### Community 16 - "Provider API-Key Validation"
Cohesion: 0.14
Nodes (10): ProviderConfig, Configuration for a single data provider., provider_configs(), Generate valid ProviderConfig instances for normalization., Test that missing API key raises ConfigError before any network call., Provider requiring API key raises ConfigError when env var is not set., Error message includes the expected environment variable name., Provider that doesn't require API key doesn't raise on get_provider. (+2 more)

### Community 17 - "AI-Ready Evidence Contract & Schemas"
Cohesion: 0.15
Nodes (15): AI-Ready Evidence Contract, daily_ohlcv Table Schema, DataEvidencePacket Model, data_quality_reports Schema, EvidenceRef Model, LangGraph Durable Execution Docs, OHLCVRecord Validation Rules, OHLCVRecord Model (+7 more)

### Community 18 - "Latest Expected Session (16:00 ET) Logic"
Cohesion: 0.14
Nodes (8): Test get_latest_expected_session logic around 16:00 ET., After 16:00 ET on a trading day, latest expected session is today., Before 16:00 ET on a trading day, latest expected session is previous trading da, On a weekend, latest expected session is the previous Friday., On a holiday, latest expected session is the previous trading day., When no exchange specified, should default to NYSE., At exactly 16:00 ET on a trading day, today is the latest expected session., TestLatestExpectedSession

### Community 19 - "Calendar Holiday Exclusion Tests"
Cohesion: 0.14
Nodes (8): MLK Day (2024-01-15) should not be a trading session., Independence Day (2024-07-04) should not be a trading session., Thanksgiving (2024-11-28) should not be a trading session., A week with a holiday should have fewer than 5 sessions., Test that get_trading_sessions excludes known exchange holidays., New Year's Day (2024-01-01) should not be a trading session., Christmas Day (2024-12-25) should not be a trading session., TestTradingSessionsExcludesHolidays

### Community 20 - "Missing Sessions Detection Tests"
Cohesion: 0.14
Nodes (8): Test that get_missing_sessions correctly identifies gaps in data., When all expected sessions are present, missing should be empty., When no actual dates provided, all expected sessions are missing., When some sessions are missing, they should be identified., Extra dates in actual_dates that aren't expected sessions are ignored., Holidays should not appear in missing sessions., Calendar should support at least 5 years of historical sessions., TestGetMissingSessions

### Community 21 - "Is-Trading-Day Tests"
Cohesion: 0.14
Nodes (8): Test is_trading_day correctly identifies non-trading days., Saturday should not be a trading day., Sunday should not be a trading day., A regular Monday should be a trading day., A regular Friday should be a trading day., A known holiday should not be a trading day., NASDAQ also doesn't trade on weekends., TestIsTradingDay

### Community 22 - "Data Ingestion Foundation Spec Overview"
Cohesion: 0.19
Nodes (14): Design Document: Data Ingestion Foundation, Implementation Tasks for Codex/Cursor, Provider-Agnostic Architecture, yfinance as Disposable Dev Fallback Only, kiro-status Skill, Data Ingestion Foundation, No LLM Calls in Ingestion Path, research_data Package (+6 more)

### Community 23 - "Spec Requirements/Properties/Tasks Cross-Refs"
Cohesion: 0.22
Nodes (13): Property 10: Provider Registry Rejects Invalid Configuration, Property 12: Duplicate Primary Key Rejection, Property 19: Ingestion Idempotence for Identical Payloads, Property 1: OHLCV Validation Rejects Invalid Records, Property 4: Raw Before Normalized Ordering Invariant, Requirement 1: Provider Registry and Configuration, Requirement 5: Data Validation, Requirement 8: Storage Schema (+5 more)

### Community 24 - "InsufficientDataError"
Cohesion: 0.23
Nodes (5): InsufficientDataError, Raised when a symbol has fewer rows than required for the requested operation., Test InsufficientDataError exception class., TestInsufficientDataError, TestInsufficientDataError

### Community 25 - "PriceAdjustment Enum & High/Low Validators"
Cohesion: 0.18
Nodes (4): Enum, PriceAdjustment, Pydantic models, enumerations, and validation rules for the research data system, Type of price adjustment applied to OHLCV data.

### Community 26 - "Calendar Unsupported-Range Error Handling"
Cohesion: 0.17
Nodes (7): Test that CalendarError is raised for unsupported date ranges., A date before the calendar's supported range should raise CalendarError., A date far in the future beyond calendar range should raise CalendarError., An unsupported exchange should raise CalendarError., is_trading_day should raise CalendarError for dates outside supported range., When start > end, should return empty list (not an error)., TestCalendarErrorUnsupportedRange

### Community 27 - "Trading Session Weekend Exclusion Tests"
Cohesion: 0.17
Nodes (7): Test that get_trading_sessions never returns Saturday or Sunday., A normal week (Mon-Fri) should return 5 sessions, no weekends., Two full weeks should return 10 sessions., A range covering only Saturday and Sunday should return no sessions., A single Saturday should return no sessions., A single Sunday should return no sessions., TestTradingSessionsExcludesWeekends

### Community 28 - "CSV Fixture Provider"
Cohesion: 0.2
Nodes (8): CSVFixtureProvider, _parse_adjustment_policy(), CSV fixture provider for deterministic testing without network access.  Loads, Parse a single CSV row into an OHLCVRecord.          This method intentionally, Map a provider config adjustment_policy string to PriceAdjustment enum., Provider that loads deterministic sample data from local CSV fixtures.      Co, Initialize the CSV fixture provider.          Args:             config: Provi, Fetch daily OHLCV data for a symbol from local CSV fixtures.          Args:

### Community 29 - "Provider Protocol & Fabrication/Quality Properties"
Cohesion: 0.2
Nodes (12): Error Handling Table, PriceProvider Protocol, Property 11: No Data Fabrication on Empty Provider Response, Property 17: Rejected Records Counted in Quality Report, Property 5: Quality Status Classification Correctness, ProviderCapabilities Model, ProviderFetchResult Model, Requirement 13: Error Handling (+4 more)

### Community 30 - "MarketCalendar & CalendarError"
Cohesion: 0.2
Nodes (7): Exception, CalendarError, Market calendar for determining expected trading sessions.  Uses the exchange_, Return the latest expected trading session as of now.          Logic:, Check if a given date is a trading day for the exchange.          Args:, Raised when a calendar operation fails due to unsupported date range or invalid, Get or create a calendar instance for the given exchange.          Args:

### Community 31 - "Project Guardrails (Non-Negotiable Rules)"
Cohesion: 0.36
Nodes (11): Non-Negotiable Guardrails, Guardrails to Preserve, Design Non-Goals, Property 13: No Secrets in Stored Metadata, guardrail-auditor Agent, guardrail-check Skill, Requirement 14: Security and Privacy, Requirement 16: Scope Boundaries (+3 more)

### Community 32 - "DataEvidencePacket Construction Tests"
Cohesion: 0.31
Nodes (4): Test DataEvidencePacket construction and JSON serialization., Serialize to JSON and deserialize back, verify equivalence., confidence_cap must be between 0.0 and 1.0., TestDataEvidencePacket

### Community 33 - "ProviderFetchResult Model"
Cohesion: 0.27
Nodes (7): ProviderFetchResult, Result of a provider fetch operation including raw payload and parsed records., Test ProviderFetchResult model construction and defaults., TestProviderFetchResult, TestProviderFetchResult, Property 11: No Data Fabrication on Empty Provider Response.      For any prov, TestProperty11NoDataFabrication

### Community 34 - "DataQualityReport Model"
Cohesion: 0.29
Nodes (6): DataQualityReport, Per-symbol quality report generated after an ingestion run., Test DataQualityReport model construction., confidence_cap must be between 0.0 and 1.0., TestDataQualityReport, TestDataQualityReport

### Community 35 - "Provider Registry Config-Loading Tests"
Cohesion: 0.2
Nodes (6): Test that the actual config/providers.toml loads without errors., Valid config loads successfully using the actual config directory., ProviderRegistry initializes successfully with valid config., ProviderRegistry exposes capabilities for registered providers., ProviderRegistry returns provider config for known providers., TestValidConfigLoads

### Community 36 - "Ingestion Architecture Diagram & Components"
Cohesion: 0.33
Nodes (10): Ingestion Architecture Diagram (mermaid), Data Quality Auditor Component, Market Calendar Component, Normalizer Component, Property 3: Raw Payload Hash Consistency, Provider Fetchers Component, Provider Registry Component, raw_market_payloads Table Schema (+2 more)

### Community 37 - "Normalizer/Calendar Properties & csv_fixture Entry"
Cohesion: 0.27
Nodes (10): Property 18: Normalizer Price Adjustment Mapping, Property 2: OHLCV Round-Trip Integrity, Property 6: Market Calendar Excludes Non-Trading Days, Design Testing Strategy, csv_fixture provider entry, Requirement 15: Testing Without Network Access, Requirement 4: Normalization, Requirement 6: Market Calendar (+2 more)

### Community 38 - "ProviderCapabilities Model"
Cohesion: 0.33
Nodes (5): ProviderCapabilities, Describes the capabilities and constraints of a data provider., Test ProviderCapabilities model construction and defaults., TestProviderCapabilities, TestProviderCapabilities

### Community 39 - "PriceReadAPI"
Cohesion: 0.25
Nodes (5): PriceReadAPI, Read API for downstream module consumption.  Provides typed access to time-ord, Convert a DuckDB row tuple to an OHLCVRecord instance., Downstream-facing interface for reading time-ordered price frames.      Return, Return time-ordered OHLCV rows with provenance and quality metadata.

### Community 40 - "PriceProvider Protocol & MarketCalendarProtocol"
Cohesion: 0.22
Nodes (7): Protocol, PriceProvider, Protocol that all data providers must implement.      Each provider exposes it, Fetch daily OHLCV data for a symbol within a date range.          Args:, MarketCalendarProtocol, Protocol for market calendar implementations.      Used to derive trading_date, Convert a date/datetime to the trading date in the exchange timezone.

### Community 41 - "Provider Registry Internals"
Cohesion: 0.22
Nodes (6): _build_capabilities(), _create_provider_instance(), Provider registry and base protocol for market data providers.  Defines the Pr, Build a ProviderCapabilities model from a ProviderConfig., Create a concrete provider instance based on the provider name.      This func, Initialize the provider registry.          Args:             config: Pre-load

### Community 42 - "Provider Registry Missing-Config Tests"
Cohesion: 0.25
Nodes (5): Unit tests for the Provider Registry and configuration loading.  Tests cover:, Test that missing config files produce clear error messages., Missing providers.toml raises ConfigError with the expected path., ProviderRegistry raises ConfigError when config dir doesn't have providers.toml., TestConfigFileNotFound

### Community 43 - "Benchmark Reporter & CLI Design"
Cohesion: 0.36
Nodes (8): Design Acceptance Criteria, Benchmark Reporter Component, CLI Interface (init-db, ingest-prices, audit-prices, benchmark), Property 14: No Execution Language in System Output, Property 20: Benchmark Reporter Refuses Insufficient Data, Requirement 11: Benchmark Reporter, Requirement 9: CLI Interface, Task 10: Benchmark Reporter

### Community 44 - "Evidence Packet & Read API Properties"
Cohesion: 0.43
Nodes (8): Property 15: Evidence Packet Completeness and Confidence Cap, Property 16: Evidence Packet Serialization Round-Trip, Property 7: Read API Ordering Guarantee, Property 8: Read API Usability Filter, Property 9: Read API Source and Adjustment Filtering, Requirement 10: Read API, Requirement 12: Evidence Packet Contract, Task 9: Read API and Evidence Packets

### Community 45 - "2026 Research Baseline (FinGPT/FinRobot/FINRA/SEC)"
Cohesion: 0.29
Nodes (7): Research Update: 2026 Baseline, FinGPT (curated financial data pipelines), FINRA AI Investment Fraud Alert, FINRA Auto-Trading Risk Alert, FinRobot (specialized financial agents), SEC AI-Washing Enforcement Release, Security and Privacy Section

### Community 47 - "V1 Universe Config (assets.toml)"
Cohesion: 0.5
Nodes (5): config/assets.toml (V1 Universe Config), config.py, assets Table Schema, Design Goals, V1 Universe (VOO,VTI,SPY,QQQ,AAPL,MSFT,NVDA,AMZN,GOOGL,META)

### Community 50 - "Market Calendar Unit Test Setup"
Cohesion: 0.5
Nodes (3): calendar(), Unit tests for the market calendar module (Task 6.5).  Covers: - get_trading_, Create a MarketCalendar instance for tests.

## Knowledge Gaps
- **383 isolated node(s):** `Property-based tests for no data fabrication on empty provider response (Propert`, `Generate ProviderFetchResult instances with records=[] (empty list).      This`, `Generate valid ProviderConfig instances for normalization.`, `Property 11: No Data Fabrication on Empty Provider Response.      For any prov`, `For any empty provider response, normalization SHALL produce zero valid records.` (+378 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **46 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `OHLCVRecord` connect `OHLCVRecord Model & Validation Tests` to `Normalization Pipeline`, `Asset/Universe Config & DuckDB Storage`, `Data Quality Auditor`, `DuckDB Schema Init & Duplicate-PK Handling`, `Adjustment Policy Mapping Tests`, `Secret Redaction`, `QualityStatus / PriceAdjustment Enums`, `Evidence Packet Models`, `InsufficientDataError`, `PriceAdjustment Enum & High/Low Validators`, `CSV Fixture Provider`, `DataEvidencePacket Construction Tests`, `ProviderFetchResult Model`, `DataQualityReport Model`, `ProviderCapabilities Model`, `PriceReadAPI`, `PriceProvider Protocol & MarketCalendarProtocol`, `Model Enum Validation Smoke Tests`, `Requirement 5.2: High Relationship Tests`, `Raw Payload Hash Validation Tests`?**
  _High betweenness centrality (0.185) - this node is a cross-community bridge._
- **Why does `DataQualityAuditor` connect `Data Quality Auditor` to `OHLCVRecord Model & Validation Tests`, `DataQualityReport Model`, `Market Calendar Core`, `QualityStatus / PriceAdjustment Enums`, `PriceAdjustment Enum & High/Low Validators`?**
  _High betweenness centrality (0.141) - this node is a cross-community bridge._
- **Why does `MarketCalendar` connect `Market Calendar Core` to `Data Quality Auditor`, `Latest Expected Session (16:00 ET) Logic`, `Calendar Holiday Exclusion Tests`, `Missing Sessions Detection Tests`, `Is-Trading-Day Tests`, `Market Calendar Unit Test Setup`, `Calendar Unsupported-Range Error Handling`, `Trading Session Weekend Exclusion Tests`, `MarketCalendar & CalendarError`?**
  _High betweenness centrality (0.131) - this node is a cross-community bridge._
- **Are the 129 inferred relationships involving `OHLCVRecord` (e.g. with `TestNormalizeFetchResultValid` and `TestMapAdjustmentPolicyKnown`) actually correct?**
  _`OHLCVRecord` has 129 INFERRED edges - model-reasoned connections that need verification._
- **Are the 55 inferred relationships involving `ProviderFetchResult` (e.g. with `TestProperty11NoDataFabrication` and `TestNormalizeFetchResultValid`) actually correct?**
  _`ProviderFetchResult` has 55 INFERRED edges - model-reasoned connections that need verification._
- **Are the 50 inferred relationships involving `PriceAdjustment` (e.g. with `TestProperty18NormalizerPriceAdjustmentMapping` and `TestNormalizeFetchResultValid`) actually correct?**
  _`PriceAdjustment` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Are the 47 inferred relationships involving `QualityStatus` (e.g. with `TestProperty11NoDataFabrication` and `TestNormalizeFetchResultValid`) actually correct?**
  _`QualityStatus` has 47 INFERRED edges - model-reasoned connections that need verification._