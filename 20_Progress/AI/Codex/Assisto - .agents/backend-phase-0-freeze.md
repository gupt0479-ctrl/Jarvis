# Backend Phase 0 Freeze Checklist

Goal: preserve and understand current remote backend truth through read-only inspection. Do not implement product code.

## Scope

Allowed:

- Read repo files and active docs.
- List env file names and variable names only.
- Inspect `supabase/config.toml`.
- Inspect Supabase project metadata through MCP/app tools.
- Read schema, migrations, RLS/storage/auth/advisor state.
- Inspect git status and changed-file scope.

Forbidden:

- Product code changes.
- Package or dependency changes.
- Supabase schema or data mutation.
- Migration creation or application.
- Storage upload, deletion, policy mutation, or signed URL generation.
- Landing page edits.
- Printing env values or secrets.

## Required Read-Only Outputs

Return:

- Files inspected.
- Current git state and unrelated dirty-worktree notes.
- Supabase project id/ref/name/region/status.
- Local Supabase config and migration/type/helper presence.
- Remote migration list/count.
- Public schema inventory and table groups.
- Row-count summary for business/demo tables.
- Auth state: `auth.users` count and app-user mapping gaps.
- Storage state: bucket name if safely visible, public/private status, policy visibility, object count.
- RLS state: enabled tables and policy audit gaps.
- Advisor findings summary.
- Security risks and stop conditions.
- Migration source-of-truth recovery decision needed next.

## Decision To Produce

End Phase 0 with one of:

- `recover-reviewed-baseline`: pull/export current remote schema into local reviewed baseline.
- `clean-reviewed-rebuild`: rebuild in a non-production branch/project from reviewed docs and discard remote prototype drift after backup.
- `blocked`: access, policy visibility, backup, or ownership gaps prevent a safe decision.

Do not choose by guessing. State what evidence supports the recommendation and what approval is needed.
