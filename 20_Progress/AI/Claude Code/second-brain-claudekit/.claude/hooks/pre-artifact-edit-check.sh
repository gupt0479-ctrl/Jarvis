#!/usr/bin/env bash
# PreToolUse hook (Write|Edit|MultiEdit). Reads hook stdin JSON, checks whether
# tool_input.file_path touches an agent/command/hook/skill staging path, and if
# so asks for confirmation with a reminder to consult the live Anthropic docs
# index first (60_Claude/vault-rules/anthropic-docs-reference.md).
input="$(cat)"
file_path="$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null)"

if printf '%s' "$file_path" | grep -qE '(^|/)(agents|commands|hooks|skills)/'; then
  printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Authoring/editing an agent, skill, command, or hook file. Per 60_Claude/vault-rules/anthropic-docs-reference.md: fetch https://platform.claude.com/llms.txt (and the 1-3 relevant pages) first, then confirm to proceed."}}'
fi
exit 0
