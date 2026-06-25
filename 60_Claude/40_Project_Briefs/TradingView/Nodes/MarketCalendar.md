---
source_file: "src/research_data/calendar.py"
type: "code"
community: "Market Calendar Core"
location: "L50"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Market_Calendar_Core
---

# MarketCalendar

## Connections
- [[.__init__()_1]] - `calls` [INFERRED]
- [[.__init__()_3]] - `method` [EXTRACTED]
- [[._get_calendar()]] - `method` [EXTRACTED]
- [[._validate_date_range()]] - `method` [EXTRACTED]
- [[.get_latest_expected_session()]] - `method` [EXTRACTED]
- [[.get_missing_sessions()]] - `method` [EXTRACTED]
- [[.get_trading_sessions()]] - `method` [EXTRACTED]
- [[.is_trading_day()]] - `method` [EXTRACTED]
- [[DataQualityAuditor]] - `uses` [INFERRED]
- [[Determines expected trading sessions for US equity exchanges.      Supports NY]] - `rationale_for` [EXTRACTED]
- [[TestCalendarErrorUnsupportedRange]] - `uses` [INFERRED]
- [[TestGetMissingSessions]] - `uses` [INFERRED]
- [[TestIsTradingDay]] - `uses` [INFERRED]
- [[TestLatestExpectedSession]] - `uses` [INFERRED]
- [[TestProperty6MarketCalendarExcludesNonTradingDays]] - `uses` [INFERRED]
- [[TestTradingSessionsExcludesHolidays]] - `uses` [INFERRED]
- [[TestTradingSessionsExcludesWeekends]] - `uses` [INFERRED]
- [[calendar()]] - `calls` [INFERRED]
- [[calendar.py]] - `contains` [EXTRACTED]
- [[test_all_sessions_within_requested_range()]] - `calls` [INFERRED]
- [[test_known_holidays_excluded()]] - `calls` [INFERRED]
- [[test_nasdaq_no_weekends()]] - `calls` [INFERRED]
- [[test_no_weekends_in_trading_sessions()]] - `calls` [INFERRED]
- [[test_sessions_are_sorted()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Market_Calendar_Core