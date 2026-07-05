---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Kiro/Assisto/Setup]]"
---
# Implementation Plan: Assisto-Spend Backend

## Overview

This plan covers the full backend gate (Phases 0-8) and core backend service implementation for Assisto-Spend. Tasks are sequenced with explicit dependencies. No UI implementation is included — this is backend-only. Phase 0 is complete (freeze snapshot exists). Phase 1 is blocked on Supabase CLI availability.

## Tasks

- [x] 1. Snapshot remote Supabase state via MCP read-only inspection
  - **Requirements:** REQ-1
  - **Result:** `docs/assisto-spend/backend/00-supabase-freeze-snapshot.md` exists

- [ ] 2. Install or verify Supabase CLI in development environment
  - **Requirements:** REQ-1
  - **Blocker:** CLI not found in WSL during previous inspection
  - **Acceptance:** `supabase --version` returns valid version

- [ ] 3. List remote migrations via CLI and document versions
  - **Requirements:** REQ-1
  - **Acceptance:** migration versions and names documented locally

- [ ] 4. Pull or reconstruct remote schema as local baseline migration
  - **Requirements:** REQ-1
  - **Decision required:** pull existing vs reviewed rewrite (user approval needed)
  - **Acceptance:** local `supabase/migrations/` contains baseline file(s)

- [ ] 5. Verify baseline reproduces schema on fresh database
  - **Requirements:** REQ-1
  - **Acceptance:** `supabase db reset` succeeds and schema matches remote

- [ ] 6. Review each table against canonical data model
  - **Requirements:** REQ-2
  - **Reference:** `docs/assisto-spend/03-data-model.md`
  - **Acceptance:** keep/redesign/remove matrix documented

- [ ] 7. Align enum values with canonical state machines
  - **Requirements:** REQ-2
  - **Reference:** `docs/assisto-spend/04-workflow-state-machines.md`
  - **Acceptance:** enum alignment document with gaps identified

- [ ] 8. Identify missing constraints and idempotency rules
  - **Requirements:** REQ-2
  - **Acceptance:** corrective constraint list documented

- [ ] 9. Triage FK/index advisor warnings and plan report indexes
  - **Requirements:** REQ-2, REQ-11
  - **Acceptance:** index plan document exists

- [ ] 10. Audit RLS policies (names, conditions, roles)
  - **Requirements:** REQ-4
  - **Acceptance:** RLS audit document with keep/redesign decisions

- [ ] 11. Audit storage bucket (name, privacy, policies, MIME)
  - **Requirements:** REQ-8
  - **Acceptance:** storage audit document exists

- [ ] 12. Write corrective migration plan (forward-fix only)
  - **Requirements:** REQ-2
  - **Acceptance:** ordered migration list with SQL sketches

- [ ] 13. Document auth-user mapping contract
  - **Requirements:** REQ-3
  - **Acceptance:** auth mapping spec with active/inactive/demo behavior

- [ ] 14. Implement demo actor resolver
  - **Requirements:** REQ-3
  - **Output:** `src/lib/spend/auth/resolve-actor.ts`
  - **Acceptance:** server-only function resolves actor from request context

- [ ] 15. Define server guard API signatures
  - **Requirements:** REQ-4
  - **Output:** `src/lib/spend/permissions/guards.ts`
  - **Acceptance:** typed guard functions for all operation types

- [ ] 16. Implement permission rules
  - **Requirements:** REQ-4
  - **Output:** `src/lib/spend/permissions/rules.ts`
  - **Acceptance:** rules cover all documented roles and operations

- [ ] 17. Decide RLS strategy (deny-all service-role vs scoped policies)
  - **Requirements:** REQ-4
  - **Acceptance:** documented decision with migration plan if needed

- [ ] 18. Define state machines for PR, TR, TE, PO, Task
  - **Requirements:** REQ-5
  - **Output:** `src/lib/spend/workflow/state-machines.ts`
  - **Acceptance:** transition tables with valid from-to, required fields, side effects

- [ ] 19. Implement transition engine with CAS
  - **Requirements:** REQ-5
  - **Output:** `src/lib/spend/workflow/transition-engine.ts`
  - **Acceptance:** validates, transitions atomically, returns STALE_STATUS on conflict

- [ ] 20. Define audit event taxonomy
  - **Requirements:** REQ-6
  - **Output:** `src/lib/spend/audit/event-types.ts`
  - **Acceptance:** enum covers all material actions

- [ ] 21. Implement audit writer
  - **Requirements:** REQ-6
  - **Output:** `src/lib/spend/audit/write-event.ts`
  - **Acceptance:** server-only function inserts immutable events

- [ ] 22. Implement Spend Trace assembler
  - **Requirements:** REQ-6
  - **Output:** `src/lib/spend/audit/spend-trace.ts`
  - **Acceptance:** assembles full timeline for any entity

- [ ] 23. Add DB-level append-only enforcement migration
  - **Requirements:** REQ-6
  - **Acceptance:** trigger/policy prevents UPDATE/DELETE on audit_events

- [ ] 24. Implement upload Route Handler
  - **Requirements:** REQ-8
  - **Output:** `src/app/api/spend/upload/route.ts`
  - **Acceptance:** validates MIME/size/checksum, stores privately, records metadata

- [ ] 25. Implement signed URL Server Action
  - **Requirements:** REQ-8
  - **Acceptance:** permission-checked, short-lived URL returned

- [ ] 26. Implement mock OCR provider
  - **Requirements:** REQ-9
  - **Output:** `src/lib/spend/ocr/mock-provider.ts`
  - **Acceptance:** deterministic extractions for test receipts

- [ ] 27. Implement OCR persistence with value separation
  - **Requirements:** REQ-9
  - **Acceptance:** three value tracks maintained, OCR never overwrites

- [ ] 28. Create deterministic seed manifest
  - **Requirements:** REQ-12
  - **Output:** `supabase/seed.sql` or seed script
  - **Acceptance:** covers all demo scenarios, reproducible

- [ ] 29. Implement demo data marking and isolation
  - **Requirements:** REQ-12
  - **Acceptance:** demo data identifiable and removable

- [ ] 30. Define report query functions
  - **Requirements:** REQ-11
  - **Output:** `src/lib/spend/reports/queries.ts`
  - **Acceptance:** 13+ reports with correct data sources

- [ ] 31. Define CSV allow-lists
  - **Requirements:** REQ-11
  - **Output:** `src/lib/spend/csv/allow-lists.ts`
  - **Acceptance:** per-report, per-role field restrictions

- [ ] 32. Implement CSV serializer with export audit
  - **Requirements:** REQ-11
  - **Acceptance:** excluded fields never appear, export audited

- [ ] 33. Create index migration for report/queue performance
  - **Requirements:** REQ-11
  - **Acceptance:** planned indexes added via forward migration

- [ ] 34. PR backend flow integration
  - **Requirements:** REQ-7
  - **Acceptance:** full PR lifecycle via Server Actions

- [ ] 35. TR backend flow integration
  - **Requirements:** REQ-7
  - **Acceptance:** full TR lifecycle via Server Actions

- [ ] 36. TE backend flow integration
  - **Requirements:** REQ-7
  - **Acceptance:** full TE lifecycle via Server Actions

- [ ] 37. Backend QA verification
  - **Requirements:** REQ-13
  - **Acceptance:** build passes, guards enforced, audit immutable, landing clean

## Task Dependency Graph

```json
{
  "waves": [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6, 10, 11, 20],
    [7, 8, 9, 13, 26],
    [12, 14, 15, 17, 18],
    [16, 19, 21, 23, 24, 28],
    [22, 25, 27, 29, 30, 33],
    [31, 34, 35, 36],
    [32],
    [37]
  ]
}
```

## Notes

- Phase 0 is complete. Phase 1 is blocked on Supabase CLI availability in WSL.
- No Supabase mutations without explicit user approval (enforced by `supabase-safety-check` hook).
- All tasks that produce code require `npm run build` to pass.
- Protected files (landing page, existing components, package.json) are never touched.
- Dependency phase (TypeScript config, Zod, Supabase client packages) must be approved before code tasks (14+) begin.
- Tasks 2-5 require user decision on pull vs rewrite strategy.
