---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-10
tags:
  - portfolio
  - claude-setup
  - hooks
notes:
  - "[[00 - Claude Code Build Kit — Index]]"
  - "[[04 - Eval Harness — promptfoo]]"
---
# Commands and Hooks
This note owns the slash commands and the `settings.json` hooks for the build. The principle: cheap deterministic gates run automatically and often; expensive LLM evals run on demand and at deploy, never on every edit.
## New command: /eval
Add `.claude/commands/eval.md` so any session can run the suite without re-explaining it:
```markdown
---
description: Run the promptfoo eval suite (grounding, tools, refusal, injection, fail-safe, persona warmth) and report pass/fail.
---
Delegate to the eval-runner subagent. Run `promptfoo eval` against the suite in the repo.
Report a table of case → pass/fail → the premortem failure it guards. If anything fails, stop and surface it; do not proceed to deploy.
```
Optional `/ship-check` that chains `/typecheck` → `pnpm build` → `/eval` → `security-reviewer` for a one-command pre-deploy gate.
## Hooks: what runs when
Keep the cheap gates automatic; keep the costly ones manual. In `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "pnpm biome check --write \"$CLAUDE_FILE_PATHS\"" }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "pnpm typecheck" }
        ]
      }
    ]
  }
}
```
- **PostToolUse (Biome on edit)** — formats/lints the moment a file changes. Cheap, keep it. (Already in your kit.)
- **Stop (typecheck)** — at the end of a turn, fail loudly if types broke. Cheap, deterministic, fast.
- **No AI evals in the Stop hook.** promptfoo costs model tokens and seconds per run; firing it on every Stop burns quota and slows the loop. Run it through `/eval` when a phase is done and as a CI gate (see [[04 - Eval Harness — promptfoo]]). This is the deliberate answer to "don't rely on Vitest / better hooks": the *gate* is promptfoo-in-CI, the *fast local check* is typecheck+Biome.
## Why this split is the token-smart choice
Edit-time and Stop-time hooks must be near-free or they tax every single turn — so they stay deterministic (Biome, tsc). The LLM eval is the real quality gate but it is expensive, so it fires at the two moments that justify the cost: when you finish a phase (`/eval`) and when you try to deploy (CI). This keeps Sonnet 4.8's per-turn context and your free-tier model quota from being eaten by background grading.
## Existing commands, reused
`typecheck`, `build-fix`, `deploy`, `review`, `sanity-push`, `e2e`, `performance`, `add-project` stay as-is. The build leans on `typecheck` (every phase), `sanity-push` (Phase 2 slug/content fix), `deploy` (Phase 8), and `e2e` (Phase 7 Orby navigation smoke test).
