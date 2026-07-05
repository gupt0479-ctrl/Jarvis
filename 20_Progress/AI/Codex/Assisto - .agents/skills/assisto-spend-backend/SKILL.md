---
name: assisto-spend-backend
description: Use when working on Assisto-Spend Supabase, migrations, auth, workflow, audit, storage, OCR, seed data, reports, server reads, server writes, or backend implementation.
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Codex/Assisto - .agents/Setup]]"
---

# Assisto-Spend Backend

Backend work is gated by source-of-truth recovery. The remote Supabase DB is useful evidence after review and local migration recovery; it is not production authority.

## Read First

- `AGENTS.md`
- `PRD.md`
- `.agent/codex-context.md`
- `.agent/mcp-checklist.md`
- `docs/assisto-spend/02-real-repo-architecture.md`
- `docs/assisto-spend/03-data-model.md`
- `docs/assisto-spend/11-implementation-phases.md`
- Relevant `docs/assisto-spend/agent-build/*`

## Required Checks

- Confirm current git state and protected paths.
- Inspect env names only; never values.
- Report Supabase project/ref/schema/migration/auth/storage state before DB work.
- Stop if local migrations are absent while remote migrations exist and the task needs schema or backend writes.
- Stop if storage/RLS details are needed but unavailable.

## Backend Rules

- No direct status mutation.
- Server actions/services must validate input, resolve actor, apply guards, execute workflow/policy, write audit, and return structured results.
- Service-role helpers must be server-only.
- Browser reads require audited RLS policy semantics.
- Upload/signing requires audited private bucket and policies.
- Seeds must be deterministic and separated from production data.

## Output

Report files changed, validation, Supabase/migration notes, security/audit notes, stop conditions, and next phase.
