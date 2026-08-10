#!/usr/bin/env bash
# PostToolUse — runs memory unit tests whenever a memory/ file is edited.
# Runs only unit tests (no integration). Never exits non-zero.
file="${CLAUDE_FILE_PATHS:-}"
if echo "$file" | grep -q "src/memory/\|tests/memory/"; then
  cd /home/anant_gupta/projects/hub/CausalOps
  /home/anant_gupta/projects/hub/CausalOps/.venv/bin/python -m pytest \
    tests/memory/test_extractor.py tests/memory/test_mcp_tools.py \
    -q --tb=short 2>&1 | tail -20 >&2
fi
exit 0
