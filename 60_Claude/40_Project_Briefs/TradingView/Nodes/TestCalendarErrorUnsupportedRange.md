---
source_file: "tests/test_calendar.py"
type: "code"
community: "Calendar Unsupported-Range Error Handling"
location: "L250"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Calendar_Unsupported-Range_Error_Handling
---

# TestCalendarErrorUnsupportedRange

## Connections
- [[.test_far_future_date_raises_error()]] - `method` [EXTRACTED]
- [[.test_is_trading_day_unsupported_range()]] - `method` [EXTRACTED]
- [[.test_start_after_end_returns_empty()]] - `method` [EXTRACTED]
- [[.test_unsupported_exchange_raises_error()]] - `method` [EXTRACTED]
- [[.test_very_old_date_raises_error()]] - `method` [EXTRACTED]
- [[CalendarError]] - `uses` [INFERRED]
- [[MarketCalendar]] - `uses` [INFERRED]
- [[Test that CalendarError is raised for unsupported date ranges.]] - `rationale_for` [EXTRACTED]
- [[test_calendar.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Calendar_Unsupported-Range_Error_Handling