#!/usr/bin/env bash
# PreToolUse guard — blocks any edit to dataset_compiler.py or estimators.py.
# Exit 2 blocks the tool call; the message goes to Claude.
file="${CLAUDE_FILE_PATHS:-}"
if echo "$file" | grep -qE "(dataset_compiler|estimators)\.py"; then
  echo "BLOCKED: dataset_compiler.py and estimators.py are statistical safeguards." >&2
  echo "They must never be modified. This is enforced by project hook." >&2
  exit 2
fi
exit 0
