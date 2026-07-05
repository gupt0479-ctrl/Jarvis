---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Kiro/Assisto/Setup]]"
---
# Design: Assisto-Spend Backend

## Overview

This design covers the full backend architecture for Assisto-Spend: database recovery, auth mapping, server guards, workflow engine, audit system, storage, OCR, reports, and seed data. The backend must be correct and secure before any UI work begins.

## Architecture

The backend follows a layered architecture within Next.js App Router conventions. Server Actions handle business mutations, Route Handlers manage uploads/exports/callbacks, and server-only library modules enforce all authorization, workflow, and audit logic.

```
┌─────────────────────────────────────────────────────────┐
│  Client Components (render only, no auth decisions)      │
└──────────────────────────┬──────────────────────────────┘
                           │ invoke
┌──────────────────────────▼──────────────────────────────┐
│  Server Actions / Route Handlers                         │
│  (validate → resolve actor → guard → execute → audit)   │
└──────────────────────────┬──────────────────────────────┘
                           │ call
┌──────────────────────────▼──────────────────────────────┐
│  src/lib/spend/ (server-only business logic)             │
└──────────────────────────┬──────────────────────────────┘
                           │ query/mutate
┌──────────────────────────▼──────────────────────────────┐
│  Supabase (Postgres + Storage + Auth)                    │
└─────────────────────────────────────────────────────────┘
```

### Server Boundary Rules
- **Server Actions**: business mutations (create, submit, approve, reject, transition)
- **Route Handlers**: uploads, signed URLs, CSV export, future callbacks
- **Server Components**: scoped read models after actor resolution
- **Client Components**: render only; never authorize financial actions

### Operation Chain (Every Mutation)
1. Validate input (Zod schema)
2. Resolve actor (server-side)
3. Load scoped target
4. Apply server guard (permission check)
5. Execute workflow/policy service
6. Write data
7. Write audit event
8. Return structured result

## Components and Interfaces

### Auth Module (`src/lib/spend/auth/`)
- `resolve-actor.ts` — resolves current actor from request context (demo: header/cookie lookup; future: auth.users mapping)
- `types.ts` — `Actor`, `Role`, `AuthContext` types

### Permissions Module (`src/lib/spend/permissions/`)
- `guards.ts` — `canRead`, `canWrite`, `canTransition`, `canUpload`, `canSign`, `canExport`, `canAdmin`
- `rules.ts` — permission rule definitions per role and operation
- Guards receive: resolved actor + target entity + operation context
- No self-approval: guard rejects if actor === target approver

### Workflow Module (`src/lib/spend/workflow/`)
- `state-machines.ts` — finite state machine definitions for PR, TR, TE, PO, Task
- `transition-engine.ts` — CAS-based executor: `transition(entity, targetStatus, actor, context)`
- `types.ts` — `TransitionResult`, `StaleStatusError`, `TransitionContext`
- Returns `STALE_STATUS` on concurrent modification
- Required fields validated per transition

### Audit Module (`src/lib/spend/audit/`)
- `write-event.ts` — append immutable audit event
- `event-types.ts` — event taxonomy enum
- `spend-trace.ts` — assemble full timeline for any entity
- DB-level INSERT-only constraint on audit_events table

### Policy Module (`src/lib/spend/policy/`)
- `evaluate.ts` — evaluate rules against request at submission
- `snapshot.ts` — create immutable policy snapshot
- `simulator.ts` — dry-run evaluation without mutation

### Storage Module (`src/lib/spend/storage/`)
- `upload.ts` — server-mediated upload with validation
- `sign-url.ts` — permission-checked short-lived signed URL
- `validate.ts` — MIME type, size, checksum validation

### Data Module (`src/lib/spend/data/`)
- `client.ts` — service-role Supabase client (server-only import)
- `types.ts` — generated DB types (after schema settled)

### Validation Module (`src/lib/spend/validation/`)
- `schemas.ts` — Zod schemas for all inputs

### CSV Module (`src/lib/spend/csv/`)
- `allow-lists.ts` — per-report, per-role field allow-lists
- `serialize.ts` — safe CSV generation with audit

### Reports Module (`src/lib/spend/reports/`)
- `queries.ts` — typed query functions for 13+ reports
- `types.ts` — report result types

## Data Models

### Core Database Tables (28 tables, RLS-enabled)

| Table Group | Tables | Purpose |
|-------------|--------|---------|
| Master Data | users, departments, projects, cost_centers, vendors, categories, budgets | Organization and classification |
| Request Workflow | spend_requests, request_lines, approval_steps, policy_flags, budget_checks | PR/TR/TE lifecycle |
| Procurement | purchase_orders, purchase_order_lines | PO from approved PR lines |
| Travel | travel_segments, travel_service_tasks | TR route and admin tasks |
| Expenses/OCR | expense_reports, expense_lines, attachments, receipt_extractions, receipt_extraction_fields, duplicate_candidates | TE evidence and review |
| Policy/Admin | approval_policies, policy_rules, request_number_sequences | Configurable rules |
| Collaboration | comments, notifications | User communication |
| Audit | audit_events | Append-only history |

### Key Type Definitions

```typescript
type RequestType = 'procurement' | 'travel' | 'expense';
type RequestStatus = 'draft' | 'submitted' | 'under_review' | 'approved' | 'partially_approved' | 'rejected' | 'cancelled';
type LineStatus = 'pending' | 'approved' | 'rejected' | 'cancelled';
type ApprovalDecision = 'approved' | 'rejected' | 'clarification_requested';
type FinanceDecision = 'approved' | 'rejected' | 'clarification_requested' | 'approved_with_exception';
type TaskStatus = 'pending' | 'in_progress' | 'completed' | 'waived';
type OCRFieldReviewState = 'pending' | 'accepted' | 'corrected' | 'rejected' | 'not_detected';
```

### Money Handling
- Fixed precision decimal in database
- Explicit ISO currency code
- Server calculates authoritative totals
- Client totals are previews only

## Correctness Properties

### Property 1: No Direct Status Mutation
All status changes go through the transition engine. Direct UPDATE on status columns is forbidden at the application layer.
**Validates: Requirements REQ-5**

### Property 2: Append-Only Audit
DB-level trigger/policy prevents UPDATE and DELETE on audit_events table. Corrections are new events.
**Validates: Requirements REQ-6**

### Property 3: No Self-Approval
Server guard rejects any approval where actor.id === target.approver_id.
**Validates: Requirements REQ-4**

### Property 4: Idempotent Transitions
CAS pattern prevents double-apply. Concurrent modifications return STALE_STATUS.
**Validates: Requirements REQ-5**

### Property 5: Policy Immutability
Snapshots frozen at submission time. Admin policy changes affect only new submissions.
**Validates: Requirements REQ-7**

### Property 6: Value Separation
Employee-entered, OCR-extracted, and finance-approved values never overwrite each other.
**Validates: Requirements REQ-9**

### Property 7: Private Storage
No public URLs generated. No storage keys in API responses. Signed URLs are short-lived and permission-checked.
**Validates: Requirements REQ-8**

## Error Handling

| Error Type | Handling |
|-----------|----------|
| Validation failure | Return structured Zod error, no side effects |
| Permission denied | Return `DENIED` with reason, no data leakage |
| Stale status (CAS) | Return `STALE_STATUS`, client must refresh and retry |
| Invalid transition | Fail closed, no partial state change, log attempt |
| Missing required field | Block transition, return specific missing field |
| Upload validation failure | Reject before storage write |
| Concurrent PO creation | Unique constraint prevents duplicate line inclusion |

## Testing Strategy

### Unit Tests
- Transition engine: valid/invalid transitions, required comments, blocker flags
- Permission guards: role-based access, self-approval rejection, proxy tracking
- Policy evaluation: threshold matching, route generation
- CSV serializer: allow-list enforcement, excluded field verification

### Integration Tests
- Full PR lifecycle: create → submit → approve → PO
- Full TR lifecycle: create → submit → approve → tasks
- Full TE lifecycle: create → upload → OCR → finance → reimburse
- Audit trail completeness for each flow

### Safety Tests
- Audit append-only: verify UPDATE/DELETE blocked on audit_events
- Storage privacy: verify no public URLs generated
- Secret isolation: verify service-role not importable from client modules
- Landing regression: verify `/` renders unchanged
