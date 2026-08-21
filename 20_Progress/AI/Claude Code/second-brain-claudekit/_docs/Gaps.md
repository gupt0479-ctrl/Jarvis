# Gaps — what's actually wrong in this repo right now

Mirrors Jarvis's own `10_Areas/AI/Setup/Gaps.md` convention on purpose — a plain, dated, no-spin list of what's currently wrong, thin, or missing, updated as items close rather than rewritten from scratch.

**Archived 2026-08-20 (fifth pass):** everything previously marked `[RESOLVED ...]` was moved to `_docs/Gaps-Archive.md`, per Anant's explicit choice via `AskUserQuestion` ("archive resolved sections now" over "keep everything in place as a permanent audit trail"). Nothing was deleted — the archive holds the full original text. This file now holds only what's still genuinely open or standing, so it stops growing indefinitely with settled history. Two real corrections were made in the process, not just a mechanical move: the "10+ days uncommitted work" finding was stale (the repo has been committed since 2026-08-20, `git log`/`git status` re-verified directly) and the "tested-skills vs tested-tools terminology drift" finding was stale (Jarvis's own `Tool Map.md` frontmatter now confirms it's been resolved since 2026-08-19) — both corrected and archived as resolved rather than carried forward as open when they no longer are.

---

## 🔴 TOP PRIORITY — real promotion throughput, still the core problem, now measurably moving

Originally flagged 2026-08-20: three-plus weeks of dense structural work went into this repo's own pipeline machinery while zero sandbox clones had reached a promoted state. **Update, 2026-08-20 (fourth and fifth passes):** this has started moving for real, not just been re-described:

- **gbrain: the embedding-provider decision that had blocked it since 2026-07-29 is made and executed.** OpenAI is wired and verified working (real doctor output, real semantic search hit). Promotion decision recorded: **cleared, global candidate** — `tested-tools/mcp-servers/gbrain/VERDICT.md`. This is the first tool in this repo's pipeline to reach a real, evidenced "cleared" verdict. **Still not actually promoted** — the global `~/.claude/` install is explicitly a separate session's job (per `_docs/Design.md`), so the underlying imbalance (zero tools installed into any real `.claude/`) is not yet fully closed, just one real step closer.
- **3 of the 6 dormant clones with a recorded next step were actually executed** (spec-kit, promptfoo, claude-context — see `tests/skills/spec-kit/`, `tests/cli-tools/promptfoo/`, `tests/mcp-servers/claude-context/` for full transcripts). None of the three has a promotion decision yet — real next-step execution, not a verdict.
- **Still open:** `hiring-agent`'s next step (a real internship-search pass) not attempted. `TradingAgents`/`OpenBB` remain out of scope for this repo (TradingView-side session, per Jarvis's own triage). Of the 21 originally-dormant clones, most are still either dropped (9, a real decision, not neglect) or genuinely untouched beyond the triage note. The structural imbalance this flag exists to track — pipeline machinery vastly outpacing real promotions — is real progress, not resolved.

## 🔴 STANDING GATE — no further net-new pipeline meta-infrastructure until a real tool is promoted

Added to `_docs/Design.md`'s minimal-footprint section 2026-08-20: no new top-level staging folder, new Standard, new convention doc, or new automated sync leg gets built in this repo until at least one real tool reaches a promoted state (installed into this repo's own `.claude/`, a real project's `.claude/`, or Jarvis's real `.claude/`). The actual work of testing, verdict-writing, and promoting a specific tool is exempt — it's the thing this gate exists to force forward. (`tested-tools/mcp-servers/` and `tests/cli-tools/` — both new type buckets added this round — fall under that exemption: real, tool-specific verdict/test-log homes, not new process scaffolding.)

## Review folder — still deliberately not built

`60_Claude/` has no equivalent of Jarvis's `60_Claude/30_Reviews/AI/` for reviewing this repo's own pipeline activity. Deliberately parked: it depends on the Jarvis-side review system having at least one real Weekly review written against it first (still zero data rows as of the last check). Revisit once that precondition is met — building against an unexercised upstream shape would repeat the exact "plan-and-never-run" failure mode this repo's pipeline exists to prevent.

## Minor, low-priority open items

- No script mechanically verifies the `instructions/`/`tests/`/`tested-tools/_future/` scope — not blocking anything today, still nobody's asked for it.
- `60_Claude/Templates/weekly-summary.md`'s shape has no relationship to Jarvis's own real AI-tools review template. Two different subjects (engineering-session rollups vs. usage/sync-health reviews) — not wrong, just a real gap if this repo ever wants its own citation-disciplined pipeline review.
- **`tests/` needs a real refinement pass.** Flagged explicitly 2026-08-20 (sixth pass) as out of scope for that session (which was sync-mechanism-only) and deferred to a future session, not attempted.
- **The "third hop" is still an open question, not answered.** Whether/how content ever flows from a Jarvis mirror (or this repo's `agents/`/`commands/`/`hooks/`/`skills/`/`instructions/` staging folders) into a real project's actual live `.claude/` is deliberately unwired — every live-sync leg built so far stops at "repo ← real project's current state" or "Jarvis mirror ↔ real project's current state," never "repo/Jarvis → a project's live config."

---

## 2026-08-20 (sixth pass) — sync mechanism fixed for real, across all 10 manifest entries

Scope was explicitly the sync mechanism for content already decided ready — not promoting anything new, and not touching the "third hop" (Jarvis mirror → a real project's live `.claude/`, still an open question, added to the minor-items list above). Confirmed the 10-entry list directly against `sync-manifest.json` first (`second-brain-claudekit`, `.claude_windows`, `CausalOps`, `Jarvis`, `Portfolio`, `Trading View`, `Resq`, `OpsPilot`, `The Plan`, `.claude_wsl`) rather than trusting an earlier summary of it.

**Manifest fixed for real:** `.claude/settings.json` confirmed removed from all 10 (only 5 ever had it); `README.md` added to all 10 `paths` lists at each entry's real location; `second-brain-claudekit` gained `README.md` + `_docs` so Jarvis finally sees this repo's own governing docs; `.claude_windows`/`.claude_wsl` paths re-verified against real home-directory contents — `.claude_wsl` was already accurate, `.claude_windows` is genuinely thin (no `agents/`, no `hooks/`, empty `commands/`, no `CLAUDE.md`) and nothing real was found missing from its list, so the manifest wasn't the problem there, the underlying content just doesn't exist yet.

**All five live-sync folders built for real, for all 10 entries.** `sync-all.sh` gained a new one-way mirror block for `agents/`, `commands/`, `hooks/`, `skills/` (deriving the category from each entry's existing `paths`, same model already proven for `instructions/`, no new field to maintain in parallel). A category folder is only created where real, non-empty content exists — Resq and OpsPilot correctly have none of the four, matching their real `.claude/`. `instructions/second-brain-claudekit/`'s prior "one fact, one home" self-exclusion is reversed per direct instruction: every entry gets consistent treatment now.

**Real bug found and fixed while building, not just designed around:** the first run of the `instructions/` copy for Resq and OpsPilot silently lost each project's nested `.claude/README.md` — both projects also have a distinct root `README.md`, and the original basename-only destination naming let the second `cp` overwrite the first without warning. Caught by checking the resulting file's byte count against both real sources before trusting the copy, not assumed correct. Fixed: a nested path's destination gets a `claude-` prefix when it collides with another path's basename in the same entry's list. Re-ran and confirmed both files now present with correct, distinct content. Full account: `_docs/Sync.md`'s 2026-08-20 part-2 amendment.

Everything copied into `agents/`, `commands/`, `hooks/`, `skills/`, `instructions/` this pass was grepped for secret-shaped content (API keys, tokens, private keys, credential/`.env`-shaped filenames) before any git operation — clean.

## 2026-08-20 (fifth pass) — new findings this round

**`60_Claude/Sessions/_today-edits.md`'s edit-log hook is firing but its content is 100% unusable, by construction, not intermittently.** `.claude/hooks/after-edit-log.ps1` reads `$env:CLAUDE_TOOL_NAME` and `$env:CLAUDE_FILE_PATH` — but Claude Code's actual `PostToolUse` hook contract passes tool context as a JSON payload on **stdin**, not environment variables. These two env vars are never set, so the script's fallback branch (`"unknown"`) fires on literally every invocation. Confirmed by reading the file: 51 rows for 2026-08-20, every single one reading `- HH:mm | unknown | unknown`. The hook's *timing* data is real (rows span 10:55 through 14:37 with no multi-hour gap, so no session today appears to have gone completely silent), but its *content* has never once recorded a real tool name or file path — this is a total, 100%-reproducible bug that will keep producing empty rows for every future session too until the script is changed to read stdin instead. **Not fixed this pass** — this was a verify-and-report task, not a fix task; the fix (read and parse the stdin JSON payload per Claude Code's real hook contract) is straightforward and known, left for a session that's actually scoped to touch this hook.

A raw row-count comparison against `git show --stat` on today's 8 commits (181 files touched, before this round's own uncommitted work) is not a clean test of *coverage* even once the content bug is fixed — `Write|Edit|MultiEdit` is the hook's only trigger, and a real fraction of those 181 files were plausibly touched via `git mv`, build/install tooling, or Bash-authored heredocs rather than the Write/Edit tool, none of which would ever fire this hook regardless of health. So: the hook is wired correctly (`.claude/settings.json`'s `PostToolUse` matcher is intact, `2>/dev/null; exit 0` crash-guard present) and fires reliably across sessions, but has recorded zero usable content all day, and no stronger completeness claim than that can honestly be made from this file alone.

**`tests/` backfilled for the three round-4 dormant-clone executions.** Real test logs written for spec-kit, promptfoo, and claude-context (`tests/skills/spec-kit/2026-08-20-test-log.md`, `tests/cli-tools/promptfoo/2026-08-20-test-log.md`, `tests/mcp-servers/claude-context/2026-08-20-test-log.md`) — these tools were genuinely run for real last round (already reported), just not logged under `tests/` at the time, unlike `tested-tools/commands/cpr-compress-preserve-resume/`'s matching test log. `promptfoo` and `claude-context` needed new `tests/` type buckets (`cli-tools/`, and a second occupant of `mcp-servers/`) since neither fits the existing `agents/commands/hooks/skills` taxonomy — same reasoning as `tested-tools/mcp-servers/gbrain/`.

**`_docs/Gaps.md` and `_docs/Repo-Map.md` archived.** Both had grown into permanent, ever-lengthening scrolls of dated sections with resolved items left in place. Asked Anant directly (`AskUserQuestion`): archive now, or keep everything in place. **Answer: archive now.** `_docs/Gaps-Archive.md` and `_docs/Repo-Map-Archive.md` created holding everything previously resolved, verbatim; both live files trimmed to what's still open or standing, with a pointer at the top of each.

## Cross-references

- `_docs/Gaps-Archive.md` — everything resolved as of the fourth pass and earlier, moved here verbatim 2026-08-20.
- `_docs/Repo-Map.md` / `_docs/Repo-Map-Archive.md` — folder-by-folder ground truth (live) and its own resolved-history archive, both updated 2026-08-20.
- `_docs/Jarvis.md` — the Toolkit "How to Use X"/"What X" pattern, the real review-system build state, and the real conversation-capture state.
- `_docs/Sync.md` — the `instructions_paths` live-sync design, the 2026-08-20 part-2 extension to `agents/`/`commands/`/`hooks/`/`skills/`, and the collision bug found and fixed in the same pass.
- `60_Claude/Standards/README.md` — index of the six Standards and their paired templates.
- `_docs/Design.md` — the named-gap justification for `Standards/`/`write-contract.md`/templates, and the standing "no net-new pipeline meta-infrastructure until a real promotion" gate.
- `_docs/Architecture.md` — the `claudeMdExcludes` gap/fix history and the sandbox auto-load risk.
- `60_Claude/vault-rules/write-contract.md` — golden rules and the failure-visible-check discipline.
- `tested-tools/mcp-servers/gbrain/VERDICT.md`, `tests/skills/spec-kit/`, `tests/cli-tools/promptfoo/`, `tests/mcp-servers/claude-context/` — this round's real, evidenced tool-pipeline work.
