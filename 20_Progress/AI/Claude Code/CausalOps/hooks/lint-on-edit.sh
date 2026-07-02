#!/usr/bin/env bash
# PostToolUse — runs ruff on any edited Python file and prints errors.
# Never exits non-zero (PostToolUse hooks can't block, only inform).
file="${CLAUDE_FILE_PATHS:-}"
if echo "$file" | grep -q "\.py$"; then
  cd /home/anant_gupta/projects/hub/CausalOps
  result=$(/home/anant_gupta/projects/hub/CausalOps/.venv/bin/python -m ruff check "$file" 2>&1)
  if [ -n "$result" ]; then
    echo "=== ruff $file ===" >&2
    echo "$result" >&2
  fi
fi
exit 0
