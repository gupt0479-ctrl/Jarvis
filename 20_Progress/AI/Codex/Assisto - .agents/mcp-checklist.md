---
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Codex/Assisto - .agents/Setup]]"
---
# MCP Checklist

Use MCP/app tools conservatively. Inspect first, mutate only with explicit user scope.

## Detected State

- Supabase app/plugin tools are available in this Codex session.
- Supabase project for Assisto: `tmhsadkglxbhbffsnokh`.
- GitHub app/plugin tools are available for `gupta-builds/assisto-website`.
- Kiro has a `supabase` URL MCP configured.
- Codex CLI global MCPs observed during planning: `obsidianVault` and `pencil`; they are unrelated to Assisto-Spend backend work.
- `.codex/config.toml` contains only the safe Supabase MCP URL and no credentials.

## Supabase Rules

Before DB work, report:

- Project id/ref/name
- Region/status
- Local config presence
- Local migrations/types presence
- Remote migration count
- Schema/table inventory state
- RLS/storage/auth state if relevant

Rules:

- Read-only inspection first.
- Never print secrets, env values, service-role keys, storage keys, signed URLs, receipt contents, or raw OCR payloads.
- Do not run schema or data mutations without an explicit user prompt for that exact action.
- Do not use `execute_sql` for mutation unless explicitly scoped.
- Do not create migrations until the database phase is active and migration source-of-truth recovery is approved.
- Do not apply destructive migrations without explicit approval.
- Do not rely on browser Supabase reads until RLS policy semantics are audited.
- Do not implement upload or signed URL behavior until bucket name/privacy/policies are audited.

## GitHub Rules

Before GitHub work, report:

- Repository
- Branch
- Whether the task is read-only or write-scoped

Rules:

- Prefer read-only repo/PR/issue inspection first.
- Do not create branches, commits, pushes, PRs, labels, reactions, or comments without explicit user scope.
- Do not force-push or rewrite shared history.
- Keep connector/app state and local git state aligned.

## Stop Conditions

Stop if:

- A tool would expose a secret or private payload.
- A requested mutation is broader than the user asked for.
- Supabase project access is unavailable for required backend work.
- GitHub repository identity is ambiguous.
- Remote schema would be treated as production truth without the backend gate.
