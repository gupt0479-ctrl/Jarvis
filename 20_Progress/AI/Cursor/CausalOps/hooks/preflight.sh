#!/usr/bin/env bash
# HiveMind session preflight: remind agents of project entry points.
set -euo pipefail

branch="$(git -C "${CURSOR_PROJECT_DIR:-.}" rev-parse --abbrev-ref HEAD 2>/dev/null || echo unknown)"
status="$(git -C "${CURSOR_PROJECT_DIR:-.}" status --short 2>/dev/null | wc -l | tr -d ' ')"

cat <<EOF
{
  "additional_context": "HiveMind session preflight: branch=${branch}, changed_files=${status}. Read AGENTS.md and Docs/PROJECT_CONTEXT.md before editing. Preserve the evidence boundary — LLM narrative must not become estimator data."
}
EOF
