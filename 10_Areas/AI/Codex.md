---
type: evergreen
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - ai
  - tool-guide
  - codex
notes:
  - "[[Claude OS]]"
  - "[[10_Areas/AI/Claude Code|Claude Code]]"
next: "Verify which Codex skills are actually invoked in real sessions — the source-command-* migration exists on disk but nothing records whether it's used"
---
# Codex
Codex (OpenAI's CLI agent) is the fourth and thinnest surface. Its role in practice: a second-opinion agent on repos that already have a Claude Code or Kiro canon, and a carrier for migrated slash-commands on Portfolio. It has no Jarvis vault integration and shouldn't get one — the vault loop is Claude Code's job, and splitting it across model vendors would fork the context layer.
Setups are snapshotted in `20_Progress/AI/Codex/` (Assisto, OpsPilot, Portfolio, Resq).
## How each project uses it
| Project | Setup | Mechanism |
| --- | --- | --- |
| Assisto | `.agents/` dir + `.codex/config.toml` | The richest Codex setup: `codex-context.md`, a codex-kiro work plan (explicit division of labor with Kiro), backend-phase-0-freeze, mcp-checklist, prompts/, skills/, hooks/. `config.toml` declares one repo-local MCP (`mcp_servers.supabase` → `https://mcp.supabase.com/mcp`) and deliberately stores no credentials, tokens, model overrides, or sandbox overrides. |
| Portfolio | `skills/source-command-*` (9) | Claude Code slash-commands migrated to Codex skills: add-project, build-fix, deploy, e2e, eval, review, sanity-push, ship-check, typecheck. Each reproduces the original command template — `source-command-deploy` runs the full gate in order (`pnpm typegen` → `pnpm typecheck` → …) and stops on any failure before the Vercel push. Same gates, either agent. |
| OpsPilot | `skills/supabase`, `skills/supabase-postgres-best-practices` | Vendor best-practice skills only. |
| Resq | `skills/supabase` | Same pattern. |
## The two patterns worth keeping
1. **Repo-local, credential-free config.** Assisto's `config.toml` opens with the rule: no bearer tokens, no model overrides, no global MCPs in the repo. GitHub access goes through the installed GitHub app, "keep GitHub writes explicitly user-scoped." This is the opposite of the Jarvis `.kiro/mcp.json` incident (exposed key, removed in `b8604279`) — Codex got it right first.
2. **Command migration, not command duplication.** The Portfolio `source-command-*` skills are ports of existing Claude commands, named to say so. When the underlying gate changes (say, a new typecheck step), the naming makes the sync target obvious. Contrast with the Cursor/Kiro steering files that silently restate vault rules.
## When to use Codex vs the others
- A deploy/check gate on Portfolio when Claude Code is mid-task on something else → Codex runs the same migrated gate.
- Cross-checking an architectural decision with a different model family → Codex, reading the same `.agents/` or `.claude/` canon.
- Anything vault-related, multi-file agentic work, or where skills/hooks/MCP depth matters → [[10_Areas/AI/Claude Code|Claude Code]]. Codex's setup here is skills-only; it has no hook layer on any project.
## Gaps
1. No usage signal. The skills exist on disk but no session log or history in the dumps shows Codex actually being driven. Before investing further, verify it's used at all — dead setups cost sync effort.
2. No hook layer anywhere — Codex sessions run unguarded on repos where Kiro and Cursor enforce canon gates. If Codex keeps write access on Assisto/Resq, it needs at least the secret-hygiene equivalent.
3. The codex-kiro work plan (`.agents/codex-kiro-work-plan.md`) is the only division-of-labor doc; Portfolio has the migrated commands but no note saying when to prefer Codex over Claude Code for the same gate.
