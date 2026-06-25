---
source_file: "src/research_data/calendar.py"
type: "code"
community: "MarketCalendar & CalendarError"
location: "L20"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/MarketCalendar__CalendarError
---

# CalendarError

## Connections
- [[._get_calendar()]] - `calls` [EXTRACTED]
- [[._validate_date_range()]] - `calls` [EXTRACTED]
- [[.is_trading_day()]] - `calls` [EXTRACTED]
- [[Exception]] - `inherits` [EXTRACTED]
- [[Raised when a calendar operation fails due to unsupported date range or invalid]] - `rationale_for` [EXTRACTED]
- [[TestCalendarErrorUnsupportedRange]] - `uses` [INFERRED]
- [[TestGetMissingSessions]] - `uses` [INFERRED]
- [[TestIsTradingDay]] - `uses` [INFERRED]
- [[TestLatestExpectedSession]] - `uses` [INFERRED]
- [[TestProperty6MarketCalendarExcludesNonTradingDays]] - `uses` [INFERRED]
- [[TestTradingSessionsExcludesHolidays]] - `uses` [INFERRED]
- [[TestTradingSessionsExcludesWeekends]] - `uses` [INFERRED]
- [[calendar.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/MarketCalendar__CalendarError