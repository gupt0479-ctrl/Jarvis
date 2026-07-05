---
name: assisto-spend-security
description: Use when working on Assisto-Spend authorization, RLS, service role, storage, signed URLs, CSV exports, audit, secrets, private evidence, AI/OCR safety, or financial workflow controls.
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Codex/Assisto - .agents/Setup]]"
---

# Assisto-Spend Security

Security is product behavior, not polish. Fail closed when authority, evidence, or privacy is unclear.

## Read First

- `AGENTS.md`
- `.agent/mcp-checklist.md`
- `docs/assisto-spend/05-permissions-and-security.md`
- `docs/assisto-spend/04-workflow-state-machines.md`
- `docs/assisto-spend/09-reports-and-csv.md`
- `docs/assisto-spend/06-ai-ocr-risk.md`

## Hard Rules

- UI hiding is never authorization.
- No client-supplied role, actor id, requester id, or approver id is authoritative.
- No self-approval by default.
- Service role is server-only and never `NEXT_PUBLIC_*`.
- Workflow status changes go through transition engine plus audit.
- Private storage only; signed URLs require permission checks and short lifetimes.
- CSV exports use allow-lists and exclude sensitive fields.
- AI/OCR is advisory only and never changes financial authority.

## Sensitive Data

Never expose secrets, service-role values, storage keys, signed URLs, private receipt URLs, receipt contents, raw OCR payloads, or hidden finance notes in UI, logs, audit streams, CSV, final responses, or docs.

## Stop

Stop if RLS/storage policy details, auth mapping, service-role boundaries, audit behavior, or transition rules are required but not verified.
