---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Codex/Assisto - .agents/Setup]]"
---
# Preflight Checklist

Run before future Assisto-Spend edits.

- [ ] Read `AGENTS.md`, `PRD.md`, `.agent/README.md`, `.agent/codex-context.md`, and `.agent/mcp-checklist.md`.
- [ ] Read `.agent/codex-kiro-work-plan.md` for ownership before touching backend, UI, tests, or docs.
- [ ] Read relevant `docs/assisto-spend/**` files for the active phase.
- [ ] Check `git status --short --branch`.
- [ ] Identify unrelated dirty-worktree changes and leave them alone.
- [ ] Confirm whether the task is docs/setup, backend, UI, DB/migration, or release work.
- [ ] Confirm whether the work belongs to Codex or Kiro; if backend-heavy, Codex reviews unless explicitly reassigned.
- [ ] Confirm protected paths are out of scope unless explicitly requested.
- [ ] List env file names and variable names only if env context is needed; never values.
- [ ] For Supabase work, report project/ref/schema/migration/auth/storage state before changes.
- [ ] Confirm backend-first gate status before any data-dependent implementation.
- [ ] Stop if migration drift, RLS/storage policy gaps, auth mapping gaps, or service-role ambiguity block the task.
- [ ] Choose validation commands before editing.
