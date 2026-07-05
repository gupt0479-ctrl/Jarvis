---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Codex/Assisto - .agents/Setup]]"
---
# Codex And Kiro Work Plan

This file defines the working split for Assisto-Spend while two agents are active.

## Ownership Split

| Area | Owner | Reviewer | Notes |
|---|---|---|---|
| Supabase remote access and mutation | Kiro | Codex | Codex reviews evidence; no remote mutation unless explicitly reassigned. |
| Migration recovery and baseline | Kiro | Codex | Codex checks safety, versioning, and drift resolution. |
| Schema review and corrective plan | Kiro | Codex | Codex verifies against `docs/assisto-spend/**`. |
| RLS policy implementation | Kiro | Codex | Codex verifies no browser-read claims before policy tests. |
| Server guard implementation | Kiro | Codex | Codex checks no UI-only auth, no self-approval, proxy tracking. |
| Auth/user mapping | Kiro | Codex | Codex checks demo actors cannot be mistaken for production auth. |
| Workflow engine | Kiro | Codex | Codex verifies transition-only status changes, CAS/idempotency, required reasons. |
| Audit and Spend Trace backend | Kiro | Codex | Codex verifies append-only enforcement and event coverage. |
| Storage and signed URL backend | Kiro | Codex | Codex verifies private bucket, policy audit, permission checks. |
| OCR backend and duplicate detection | Kiro | Codex | Codex verifies advisory-only behavior and value separation. |
| Reports backend and CSV data sources | Kiro | Codex | Codex verifies role scopes and allow-lists. |
| UI routes and components | Codex | Kiro for backend contracts | Codex starts only after read contracts and permission behavior are stable. |
| Frontend tests and UX state checks | Codex | Kiro for backend fixtures | Include denied/loading/empty/error states. |
| Integration QA and demo validation | Codex | Kiro for backend evidence | Codex is the final quality gate. |
| Docs/spec consistency | Codex | Kiro | Codex keeps specs aligned and flags conflicts. |

## Codex Phases

1. Verify Kiro backend Phase 0/1 output.
2. Maintain docs/spec alignment.
3. Prepare UI architecture only after backend contracts stabilize.
4. Implement `/spend` shell and UI pages only after backend read contracts exist.
5. Build tests, QA checks, and demo validation.
6. Run final integration review before any merge or release claim.

## Codex Review Checklist For Kiro Output

- [ ] No secrets, env values, storage keys, signed URLs, receipt contents, or raw OCR payloads exposed.
- [ ] No destructive DB mutation or unapproved remote mutation.
- [ ] Migrations are versioned and source-of-truth drift is resolved or explicitly blocked.
- [ ] Schema matches canonical docs or conflicts are reported.
- [ ] RLS/server guard boundary is clear.
- [ ] No UI-only authorization.
- [ ] No self-approval path.
- [ ] Transition engine enforces material status changes.
- [ ] Audit is append-only and event coverage is complete.
- [ ] Storage is private.
- [ ] Signed URLs are permission-checked and short-lived.
- [ ] CSV uses role/report allow-lists.
- [ ] AI/OCR remains advisory only.
- [ ] Demo data is deterministic and separated from production.
- [ ] Validation commands and evidence are reported.

## Codex Stop Conditions

Stop and report if Kiro output:

- Treats the remote schema as production-approved without review.
- Starts backend implementation before migration recovery/source-of-truth is resolved.
- Claims RLS/storage/audit guarantees without catalog evidence or tests.
- Implements client-authoritative roles or UI-only authorization.
- Copies Lovable/TanStack code into the Next.js app.
- Changes protected landing/app files outside scope.
