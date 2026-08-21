# How to — staged artifacts (agents, commands, hooks, skills, instructions)

Reflects the state after this repo's 2026-08-19 Phase 1 resolution (`_docs/Repo-Map.md` — read that first for the history of what changed and why). The full conventions live in `60_Claude/vault-rules/pipeline-conventions.md`; this doc is the "what do I actually do" companion.

## The six staging surfaces, and what each one means

| Folder | What lands here | Who decides it belongs there |
|---|---|---|
| `sandbox/<repo-name>/` | A real `git clone`, nothing else yet | Anyone starting to evaluate a new external tool |
| `tested-tools/<type>/<use-case>/<repo-name>/` | Something individually run and judged against `_docs/Promotion-Criteria.md` | The person who actually ran it |
| `tests/<type>/<repo-name>/` | The runnable script or dated log proving the above actually happened | Same session as the test itself |
| `instructions/<ProjectName>/<file>` | A `CLAUDE.md`/`AGENTS.md`/`PRD.md` of a **real project Anant works on** (per `sync-manifest.json`'s `"kind": "project"` entries), live-synced one-way — **never** a `sandbox/` candidate | Nobody manually — `sync-all.sh`'s `instructions_paths` logic |
| `agents/<ProjectName>/`, `commands/<ProjectName>/`, `hooks/<ProjectName>/` | Real, in-progress artifacts for a specific destination project | Whoever is actively building for that project |
| `skills/` | Source-repo staging (unchanged role) | Same as before 2026-08-19 |

## What changed 2026-08-19

Before this date, `agents/`, `commands/`, `hooks/` (top-level, repo root) were a generic "draft, then distribute" area with no destination attached — a leftover from this repo's very first scaffold commit (`d35f0b7`, 2026-04-03), written before the qualification pipeline existed. Two real findings changed that:

1. **`commands/compress.md`, `preserve.md`, `resume.md`** (added `726f6de`) named a real external repo (`cpr-compress-preserve-resume`) that had never actually been run. It was: cloned into `sandbox/`, installed into a scratch project, and its step logic exercised for real (`tests/commands/cpr-compress-preserve-resume/2026-08-19-test-log.md`). Verdict: **blend**, not adopt-or-reject — see `tested-tools/commands/cpr-compress-preserve-resume/VERDICT.md`. The hand-authored originals are archived at `.claude/_archive/superseded-commands/`, not deleted.
2. **Every other file in `agents/`, `commands/`, `hooks/`** (15 files, all from `d35f0b7`) had zero external provenance — confirmed by cross-referencing every distinctive phrase against all 30 `sandbox/` clones and everything already in `tested-tools/`. Anant's decision: relocate to `tested-tools/<type>/native-scaffold/`, honestly labeled as never-tested, home-grown content — not archived, not left in place implying pipeline-tested status they never had.

With both groups resolved, the three top-level folders (`agents/`, `commands/`, `hooks/`) were repurposed as per-destination-project staging (table above) — this is genuinely new scope, not a rename of the old role. A fourth sibling, `docs/<ProjectName>/`, was added at the same time and briefly documented here too — that turned out to be a naming error for `_docs/` (this repo's one, singular docs folder) and was removed 2026-08-20, not part of the real convention (`_docs/Repo-Map.md`'s standing rule).

`instructions/<ProjectName>/` went through a similar correction the same day, on a different mistake: it was first built to hold `CLAUDE.md`/`AGENTS.md` copied from `sandbox/` *evaluation candidates* — content that already lived, unmodified, in its source repo, adding no value as a second copy. Cleared and rebuilt to hold the real instruction files of real projects Anant works on instead, live-synced one-way from each project's actual source (`instructions/README.md`, `_docs/Sync.md`'s 2026-08-19 amendment).

## How to actually use this, concretely

**Starting work for a specific project** (say, CausalOps needs a new command): write it at `commands/CausalOps/<name>.md`. Don't pre-create `commands/CausalOps/` before there's real content — an empty project folder implies staged work that doesn't exist.

**Evaluating a new external tool**: `sandbox/<repo>/` first, always — see `tests-and-promotion.md` for what happens next.

**Finding a real project's own instruction file while working in this repo**: check `instructions/<ProjectName>/` — it's kept current automatically by `sync-all.sh`, never hand-edited. **This is not for `sandbox/` candidates** — there's no "copy a pattern in" step; a pattern worth reviewing from a `sandbox/` repo stays read where it already lives, in `sandbox/<repo>/` itself.

**Promoting something out of staging**: follow `60_Claude/Qualification-Checklist.md`'s "Before moving `tested-tools/... → a rigid folder`" section — global vs. project-scoped decided and justified, Jarvis's build standard met if the destination is Jarvis's real `.claude/`, a dated decision recorded in Jarvis per `_docs/Jarvis.md`.
