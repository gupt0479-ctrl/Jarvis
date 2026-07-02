---
name: assisto-spend-docs
description: Use when editing Assisto-Spend docs, planning files, PRD, AGENTS.md, .agent context, prompts, hooks, or agent instructions.
---

# Assisto-Spend Docs

Keep docs compact, current, and source-linked. Do not duplicate canonical detail when a link is enough.

## Source Order

1. Current repo code/config for verified architecture.
2. `docs/assisto-spend/` for product/build truth.
3. `docs/assisto-spend/agent-build/` for compact contracts.
4. `.agent/` for operational memory.
5. Lovable/spend-control and archived docs as reference only.

## Rules

- Preserve the backend verdict: remote DB is usable after review and local migration recovery, not production-ready.
- Keep Supabase state accurate: local config exists, remote schema/migrations exist, local migrations/types/helpers are absent unless reverified.
- Do not edit product code, package files, migrations, assets, or landing files during docs-only work.
- Avoid stale claims that Supabase is absent or fully ready.
- Include stop conditions and final-response expectations in agent-facing docs.

## Validation

Run `git diff --check` on changed markdown/TOML files. Confirm changed paths are docs/setup only.
