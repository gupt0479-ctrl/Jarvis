---
inclusion: auto
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Kiro/Assisto/Setup]]"
---

# Assisto-Spend Backend Architecture

## Backend-First Gate

No product code until the backend gate passes. The gate requires:

1. Freeze/read-only snapshot of remote Supabase state (Phase 0 — done)
2. Migration source-of-truth recovery (Phase 1 — blocked on Supabase CLI)
3. Schema review and corrective migration plan
4. Auth-user mapping (`auth.users.id` → `public.users.auth_user_id`)
5. RLS + server guard strategy
6. Workflow transition engine contract
7. Append-only audit + Spend Trace contract
8. Storage/OCR backend flow
9. Seed/demo data separation
10. Reports/CSV/index plan

## Server Boundary

- **Server Actions**: business mutations (create, submit, approve, reject, transition)
- **Route Handlers**: uploads, signed URLs, CSV export, future callbacks
- **Server Components**: scoped read models after actor resolution
- **Client Components**: render only; never authorize financial actions

## Operation Chain (Every Mutation)

1. Validate input
2. Resolve actor (server-side)
3. Load scoped target
4. Apply server guard (permission check)
5. Execute workflow/policy service
6. Write data
7. Write audit event
8. Return structured result

## Module Layout

```
src/lib/spend/
  audit/       — append-only event service
  auth/        — actor resolution, demo switcher
  csv/         — allow-list export
  data/        — typed DB access
  permissions/ — server guards
  policy/      — threshold evaluation, snapshots
  reports/     — report queries
  storage/     — upload, signed URL, attachment metadata
  validation/  — input schemas (Zod)
  workflow/    — transition engine, state machines
```

## Implementation Phases

20 feature phases preceded by 8 backend-first gate phases. See:
- `docs/assisto-spend/11-implementation-phases.md`
- `docs/assisto-spend/agent-build/04-pr-tr-te-workflow-contract.md`

## Stop Conditions

Stop and report if:
- Local migrations absent while remote exist and task requires schema work
- Supabase project access unavailable for backend work
- Remote schema treated as production-approved without review
- RLS/storage policy details unavailable for browser reads or uploads
- Migration would be destructive or edit applied shared migration
- Permission rule, workflow transition, or audit event is undocumented
