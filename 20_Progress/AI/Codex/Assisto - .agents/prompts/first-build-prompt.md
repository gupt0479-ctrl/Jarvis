---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Codex/Assisto - .agents/Setup]]"
---
# First Build Prompt

```md
Perform backend Phase 0 only for Assisto-Spend. Read `AGENTS.md`, `PRD.md`, `.agent/**`, and `docs/assisto-spend/**`. Inspect current repo stack, git state, `.env` names without printing values, `supabase/config.toml`, linked project metadata, remote Supabase schema/migrations/RLS/storage/auth through MCP, and dirty worktree scope. Do not implement `/spend`, do not add dependencies, do not edit landing/app files, do not create migrations, and do not mutate Supabase. Return the backend freeze snapshot and the exact migration source-of-truth recovery decision needed next.
```
