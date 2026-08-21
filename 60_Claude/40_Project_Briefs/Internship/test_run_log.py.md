---
source_file: "tests/test_run_log.py"
type: "code"
community: "recheck.py"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/recheckpy
---

# test_run_log.py

## Connections
- [[_ts()]] - `contains` [EXTRACTED]
- [[append_run_log()]] - `imports` [EXTRACTED]
- [[append_weekly_rollup()]] - `imports` [EXTRACTED]
- [[format_weekly_rollup()]] - `imports` [EXTRACTED]
- [[load_recent_runs()]] - `imports` [EXTRACTED]
- [[run_log.py]] - `imports_from` [EXTRACTED]
- [[should_run_weekly_rollup()]] - `imports` [EXTRACTED]
- [[test_append_run_log_writes_one_json_line_per_call()]] - `contains` [EXTRACTED]
- [[test_append_weekly_rollup_appends_without_rewriting()]] - `contains` [EXTRACTED]
- [[test_append_weekly_rollup_creates_file_with_header()]] - `contains` [EXTRACTED]
- [[test_appended_run_log_note_has_no_blank_lines_or_stray_dashes()]] - `contains` [EXTRACTED]
- [[test_format_weekly_rollup_aggregates_written_and_rejections()]] - `contains` [EXTRACTED]
- [[test_format_weekly_rollup_handles_zero_activity()]] - `contains` [EXTRACTED]
- [[test_load_recent_runs_filters_by_timestamp()]] - `contains` [EXTRACTED]
- [[test_load_recent_runs_on_missing_file_returns_empty()]] - `contains` [EXTRACTED]
- [[test_should_run_weekly_rollup_only_fires_sunday_2300_utc()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/recheckpy