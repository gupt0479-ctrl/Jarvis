---
inclusion: auto
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Kiro/Assisto/Setup]]"
---

# Assisto-Spend Security & Audit Rules

## Authorization Non-Negotiables

- UI hiding is NOT authorization — server-side permission checks on every read and write
- No self-approval by default
- Proxy/delegate actions must record both requester and submitter/actor
- Client role is cosmetic only; server resolves authority
- Service-role key NEVER reaches client code
- Denied actions return explicit denied state without leaking private data

## Workflow Authority

- No direct financial status mutation from UI or ad-hoc DB writes
- ALL status changes go through the transition engine
- Invalid transitions fail closed (no partial status change)
- Compare-and-set / idempotent transitions; return `STALE_STATUS` on concurrent changes
- Required comments validated before transition (rejection, clarification, exception, waiver, cancellation)

## Audit Requirements

- Append-only audit events for every material action
- Event fields: actor, action, target entity, previous state, next state, timestamp, source, reason/comment, policy snapshot reference
- Corrections are new events (never edit existing)
- Spend Trace assembled from audit events + approvals + flags + attachments + OCR + PO lines + tasks

## Storage & Privacy

- Receipts and documents use private storage ONLY
- Signed URLs generated only after server-side permission check
- Signed URLs are short-lived, never permanent
- Storage keys, object paths, permanent URLs never in UI, logs, audit streams, or CSV
- MIME type and size validated before upload acceptance
- Checksum stored for uploaded files

## AI/OCR Boundaries

- AI/OCR is advisory only
- Never approves, rejects, changes totals, creates POs, creates payments, deletes receipts, hides uncertainty, or reassigns approvers
- Employee-entered, OCR-extracted, and finance-approved values stay separate
- Duplicate candidates are suggestions requiring human review
- Raw OCR payloads: retention/redaction must be approved before storage

## CSV Export

- Strict allow-list per report and role
- Excludes: storage keys, permanent receipt URLs, service keys, private OCR payloads, hidden finance notes (unless explicitly allowed)
- Export events are audited

## Canonical Docs

- `docs/assisto-spend/agent-build/03-security-permissions-audit-contract.md`
- `docs/assisto-spend/05-permissions-and-security.md`
