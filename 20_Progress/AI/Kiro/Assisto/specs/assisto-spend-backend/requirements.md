---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Kiro/Assisto/Setup]]"
---
# Requirements Document

## Introduction

Assisto-Spend is an enterprise spend workflow module (PR/TR/TE) built inside the real Assisto Next.js App Router application. The backend must be correct, secure, and auditable before any UI implementation begins.

The remote Supabase project has a prototype-derived schema (28 tables, 4 migrations) that is NOT production-approved. Local migration source-of-truth is missing. This spec covers the full backend gate and core backend services.

### References

- `docs/assisto-spend/00-real-repo-build-plan.md`
- `docs/assisto-spend/01-product-scope.md`
- `docs/assisto-spend/03-data-model.md`
- `docs/assisto-spend/11-implementation-phases.md`
- `docs/assisto-spend/agent-build/02-supabase-data-storage-contract.md`
- `docs/assisto-spend/agent-build/03-security-permissions-audit-contract.md`
- `docs/assisto-spend/agent-build/04-pr-tr-te-workflow-contract.md`

## Glossary

| Term | Definition |
|------|-----------|
| PR | Procurement Request — employee request for goods/services |
| TR | Travel Request — employee request for travel approval |
| TE | Travel Expense — post-travel expense report with receipts |
| PO | Purchase Order — created from approved PR lines |
| RLS | Row Level Security — Supabase/Postgres access control |
| CAS | Compare-and-Set — optimistic concurrency control pattern |
| Spend Trace | Full audit timeline assembled for any request |

## Requirements

### REQ-1: Migration Source-of-Truth Recovery
The local repository must contain version-controlled migrations that reproduce the approved database schema. Remote schema is inspection-only until recovered into local migrations.

**Acceptance Criteria:**
- Local `supabase/migrations/` contains reviewed migration files
- Migrations reproduce the approved schema when applied to a fresh database
- No destructive edits to already-applied remote migrations
- Migration drift between local and remote is documented and resolved

### REQ-2: Schema Review and Corrective Migration Plan
Every remote table, enum, constraint, index, trigger, and RLS policy must be reviewed against canonical docs before production use.

**Acceptance Criteria:**
- Table-by-table review documented (keep/redesign/remove)
- Enum values aligned with canonical state machines
- Missing constraints identified (no-self-approval, approved-line-only PO, required comments)
- FK/index advisor warnings triaged
- Corrective migration list exists before any new schema work

### REQ-3: Auth-User Mapping
A documented contract maps `auth.users.id` to `public.users.auth_user_id` with support for active/inactive users and demo actors.

**Acceptance Criteria:**
- Auth mapping contract is documented and testable
- Demo actor resolution is server-side and clearly labeled MVP/demo
- Inactive user behavior is defined
- No client-side role is treated as authoritative

### REQ-4: RLS + Server Guard Strategy
Every read and write path has server-side permission enforcement. RLS policies are audited before any browser reads.

**Acceptance Criteria:**
- Server guard APIs defined for read, write, transition, upload, signed URL, export, and admin
- No self-approval enforced at server level
- Proxy/delegate actions record requester and submitter separately
- RLS policy semantics documented for each table before client access
- Denied actions return structured error without data leakage

### REQ-5: Workflow Transition Engine
All PR/TR/TE/PO/task status changes pass through a centralized transition engine. No direct status mutation.

**Acceptance Criteria:**
- Transition engine validates: current status, target status, actor permission, required comments, blocker flags
- Invalid transitions fail closed with no partial state change
- Compare-and-set / idempotent transitions return `STALE_STATUS` on concurrent changes
- Side-effectful actions use idempotency keys or unique constraints
- Every material transition writes an audit event

### REQ-6: Append-Only Audit + Spend Trace
Every material action produces an immutable audit event. Spend Trace assembles the full history of any request.

**Acceptance Criteria:**
- Audit events are append-only (DB-enforced, no UPDATE/DELETE on audit table)
- Event taxonomy covers: creation, submission, approval, rejection, clarification, cancellation, exception, PO creation, task changes, receipt upload, OCR extraction, finance decision, CSV export, policy changes, admin changes
- Each event includes: actor, action, entity, before/after, timestamp, source, reason/comment, policy snapshot ref
- Spend Trace can render the full sequence behind any current state
- Corrections are new events, never edits

### REQ-7: PR/TR/TE Backend Flows
Server-side business logic for all three core workflows is complete and enforces all rules.

**Acceptance Criteria:**
- PR: create, submit, header approve, line approve/reject, partial approval, PO from approved lines only
- TR: create, submit, approve, travel-admin task handoff, manual tasks only (no booking automation)
- TE: create, submit, receipt upload, mock OCR, value separation, duplicate detection, finance review, exception approval with reason, reimbursement state only
- Policy snapshot stored at submission
- Rejected/cancelled items remain visible
- All flows enforce server guards and write audit

### REQ-8: Storage + Signed URL Flow
Private storage for receipts and documents with server-mediated access.

**Acceptance Criteria:**
- Storage bucket is private (audited and documented)
- Uploads cross server boundary with MIME/size/checksum validation
- Attachment metadata stored separately from object storage
- Signed URLs generated only after permission check, short-lived
- No storage keys, object paths, or permanent URLs in UI or CSV
- Upload actor and audit reference recorded

### REQ-9: Mock OCR Persistence
Mock OCR runs on uploaded receipts with strict value separation.

**Acceptance Criteria:**
- Mock OCR produces extraction records with field-level confidence
- Employee-entered, OCR-extracted, and finance-approved values remain separate
- OCR never overwrites employee or finance values
- Duplicate candidates are suggestions only (never auto-reject)
- Raw OCR payload retention/redaction policy documented

### REQ-10: Finance Queue
Finance reviewers can approve, reject, clarify, or approve-with-exception.

**Acceptance Criteria:**
- Finance queue shows pending items scoped to reviewer permissions
- Exception approval requires documented reason
- Finance cannot approve while required OCR fields remain unreviewed (unless explicit exception path)
- All finance decisions write audit events

### REQ-11: Reports and CSV Export
Required reports with safe CSV export using strict allow-lists.

**Acceptance Criteria:**
- 13+ required reports implemented with correct data sources
- CSV export uses per-report, per-role allow-list
- Excluded fields: storage keys, permanent URLs, service keys, raw OCR payloads, hidden finance notes
- Export events are audited
- Report indexes planned for performance

### REQ-12: Seed/Demo Data Separation
Deterministic demo data is version-controlled and isolated from production.

**Acceptance Criteria:**
- Seed data is deterministic and reproducible from version-controlled files
- Demo data marked with `seed_key`, `is_demo`, or isolated project
- Seed covers: PR/TR/TE scenarios, finance, admin, audit, exception, duplicate candidates
- No real employee/receipt/vendor private data in seeds
- Demo data removable without affecting production rows

### REQ-13: QA / Backend Definition of Done
Backend is verified against all security, workflow, audit, and data integrity contracts.

**Acceptance Criteria:**
- Migration drift resolved
- Auth mapping tested for active/inactive users
- Server guard contract covers all paths
- Transition engine tests: invalid transitions, stale status, no self-approval, missing comment, blocker flags
- Audit append-only verified in DB
- Private storage policies verified
- Seed data deterministic and labeled
- Report/CSV tests prove excluded fields never appear
- `npm run build` passes
- Landing page regression clean
