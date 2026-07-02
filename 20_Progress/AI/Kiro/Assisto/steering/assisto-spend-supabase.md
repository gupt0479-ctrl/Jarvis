---
inclusion: auto
---

# Assisto-Spend Supabase & MCP Rules

## Current Supabase State

- Project: `Assisto` (ref: `tmhsadkglxbhbffsnokh`)
- Region: `ap-northeast-1`, Postgres 17, active healthy
- Remote schema: 28 public RLS-enabled tables (PR/TR/TE/PO/audit/OCR/master-data)
- Remote migrations: 4 applied
- Local `supabase/migrations/`: ABSENT — migration source-of-truth drift exists
- Generated types: absent
- App helpers: absent (no client/server Supabase code in app)
- Auth: `auth.users` empty; `public.users` has 7 demo users
- Storage: enabled remotely; bucket name/policies unaudited
- Supabase CLI: not available in WSL (blocks Phase 1)

## Backend Verdict

Remote DB is usable after review and local migration recovery. It is NOT production-ready. Treat as candidate baseline with domain evidence, not approved architecture.

## MCP Usage Rules

1. **Read-only inspection first** — always
2. **Never print or persist** secrets, env values, service-role keys, storage keys, signed URLs, receipt contents, or raw OCR payloads
3. **No schema or data mutations** without explicit user prompt for that exact action
4. **No migrations** until database phase is active and migration recovery is approved
5. **No destructive migrations** without explicit approval
6. **No browser Supabase reads** until RLS policy semantics are audited
7. **No upload/signed URL work** until bucket name/privacy/policies are audited

## Before Any DB Work, Report

- Project id/ref/name
- Region/status
- Local config presence
- Local migrations/types presence
- Remote migration count
- Schema/table inventory state
- RLS/storage/auth state if relevant

## Migration Rules

- All schema changes must be version-controlled
- Never edit already-applied shared migrations
- Use forward corrective migrations only
- Resolve local/remote drift before new schema work
- Remote schema pull is inspection only, not blind source of truth
- Dry-run locally before shared push (once CLI available)

## GitHub MCP Rules

- Repository: `gupta-builds/assisto-website`
- Read-only inspection first
- No branches, commits, pushes, PRs, labels, or comments without explicit user scope
- No force-push or history rewrite

## Canonical Docs

- `docs/assisto-spend/agent-build/02-supabase-data-storage-contract.md`
- `docs/assisto-spend/backend/00-supabase-freeze-snapshot.md`
- `.agent/mcp-checklist.md`
