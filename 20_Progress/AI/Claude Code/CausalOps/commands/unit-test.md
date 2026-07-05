---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Claude Code/CausalOps/Setup]]"
---

Run all unit tests (no integration, no Kafka). Execute from the repo root:
python -m pytest tests/ -m "not integration and not kafka" -q --tb=short
Report: total passed, total failed. If failures exist, show the full traceback
for each failure. Do not fix failures automatically — report them and stop.
