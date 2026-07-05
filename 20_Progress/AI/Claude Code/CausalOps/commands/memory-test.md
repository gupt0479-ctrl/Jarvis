---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Claude Code/CausalOps/Setup]]"
---

Run the memory layer unit tests only. Execute:
python -m pytest tests/memory/test_extractor.py tests/memory/test_mcp_tools.py -v --tb=short
These tests require no credentials. If tests/memory/ doesn't exist, say so clearly.
Report: passed/failed counts. Show full tracebacks on failure. Do not auto-fix.
