# Repo Map Archive — resolved history, moved out of the live `_docs/Repo-Map.md`

Archived 2026-08-20 (fifth pass), per Anant's explicit choice (`AskUserQuestion`: "archive resolved sections now"). Everything below is fully resolved, closed, or purely historical — moved here verbatim so the live `_docs/Repo-Map.md` stays a current ground-truth reference plus genuinely open items, not an ever-growing scroll of settled incidents and closed checklists. If any fact below turns out to have drifted again, fix it here in place rather than re-litigating it in the live file.

---

## Incident: the `50_Claude/` recreation bug (found and fixed 2026-08-08)

**Symptom:** partway through this session, `/home/.../second-brain-claudekit/50_Claude/Sessions/_today-edits.md` reappeared on disk — a folder that should not have existed post-rename.

**Root cause:** `.claude/hooks/after-edit-log.ps1` and `.claude/hooks/session-wrapup.ps1` (plus their `.md` companion docs) hardcoded the path `50_Claude/Sessions/...`. They were never updated when the vault renamed `50_Claude/` → `60_Claude/`. `.claude/settings.json` wires `after-edit-log.ps1` to fire on every `PostToolUse` (`Write|Edit|MultiEdit`). Earlier in this same session, `.claude/` (including `settings.json`) was restored from git after being found deleted — the moment that restore re-armed the hook, the very next `Write` tool call fired it, and it recreated `50_Claude/Sessions/_today-edits.md` from scratch (confirmed: the file had exactly one entry, timestamped seconds after the restore).

**Fix applied:**
1. `.claude/hooks/after-edit-log.ps1` and `session-wrapup.ps1` (and their `.md` docs) now point at `60_Claude/Sessions/`.
2. The stray, bug-recreated `50_Claude/` was deleted.
3. `60_Claude/scripts/register-jarvis-sync-task.ps1` had the **same class of bug** in its `$RepoLauncher` path (hardcoded `...\50_Claude\scripts\sync-jarvis-silent.vbs`, which no longer exists) — this one was live-consequential for the real 15-minute Windows Scheduled Task, since the script's fallback logic would have silently kept running off a stale Windows-side copy without ever re-syncing. Fixed to `60_Claude\scripts\...`.
4. `60_Claude/scripts/sync-jarvis.sh`'s comments (not its logic — `REPO_ROOT` is self-locating and was never actually broken) referenced `50_Claude/` and `Docs/` in its usage examples. Fixed.

**Why this matters beyond the one bug:** any file that hardcodes a folder path instead of deriving it will silently reintroduce drift the next time that folder gets renamed. Nothing else in the repo currently hardcodes `60_Claude/` this way after the 2026-08-08 fixes, but it's worth checking `60_Claude/scripts/*` again the next time any top-level folder is renamed.

## Templates merge (executed 2026-08-08)

Top-level `templates/` (7 Obsidian Templater note templates: `area-note`, `daily-note`, `idea-note`, `literature-note`, `meeting-note`, `person-note`, `project-note`) was `git mv`'d into `60_Claude/Templates/`, joining the 3 files already there (`pattern-note`, `session-log`, `weekly-summary` — AI session-artifact templates). No filename collisions. The empty `templates/` folder was removed.

Before the merge these were genuinely two non-overlapping sets serving two different documented purposes (vault-note templates vs. session-artifact templates) — Anant's reasoning for merging anyway: every template used anywhere in Jarvis, including future skill/agent/command templates, should have exactly one source-of-truth directory, not be split by template *type*. `README.md`, `CLAUDE.md`, and every command/hook that referenced `templates/*.md` were updated to `60_Claude/Templates/*.md`.

## Vault-rules move (executed 2026-08-08)

Top-level `vault-rules/` (`folder-structure.md`, `linking-strategy.md`, `naming-conventions.md`, `tagging-system.md`) was `git mv`'d to `60_Claude/vault-rules/` as a subfolder, per Anant's explicit instruction. Every reference to `vault-rules/` in `CLAUDE.md`, `README.md`, and `commands/capture.md` was updated to `60_Claude/vault-rules/`.

## Naming-convention drift (found and fixed 2026-08-08)

`60_Claude/vault-rules/folder-structure.md` documents a migration from an old hyphenated PARA structure to the current underscored one — this table is the authority and was left untouched (it's historical-reference by design):

| Old (pre-migration) | Current |
|---|---|
| `00-Inbox/` | `00_Daily/` |
| `10-Daily/` | `00_Daily/` |
| `20-Projects/` | `20_Projects/` |
| `30-Areas/` | `10_Areas/` |
| `40-Resources/` | `30_Knowledge/` |
| `50-Archive/` | `status: archived` frontmatter, or `_archive/` |
| `90-Templates/` | `60_Claude/Templates/` |

The old convention was still live in code that was never updated: `60_Claude/vault-rules/naming-conventions.md`'s own Folder Names section (contradicting `folder-structure.md` in the same directory), all 4 files in `agents/`, all 3 files in `hooks/`, and roughly half of `commands/` + `.claude/commands/` (`review.md`, `inbox-process.md`, `brainstorm.md`, `capture.md`, `journal.md`, `research.md`, `graduate.md`, `ghost.md`, `ideas.md` — some referenced both conventions in the same file). Even `CLAUDE.md` itself had one leftover instance. All traced to the single initial scaffold commit (`d35f0b7`, 2026-04-03) seeding both eras of the scheme at once.

**Fixed 2026-08-08** across every file above. One resulting semantic wrinkle, resolved by hand rather than blind find-replace: `hooks/post-note-create.md` inferred a note's `type` from its folder, with `10-Daily → daily` and `00-Inbox → idea` as separate rules — since both collapse into the same `00_Daily/` now, that folder alone can't distinguish `daily` from `idea` by path; the note now says to disambiguate by content instead (a dated journal entry vs. a standalone capture).

## Incident: the Jarvis sync silently stopped working (found and fixed 2026-08-09)

**Symptom:** `_docs/Sync.md` and Jarvis's own `Setup.md` both describe the 15-minute Windows Scheduled Task (`SecondBrainClaudekit-JarvisSync`) as live. Windows `Get-ScheduledTask`/`Get-ScheduledTaskInfo` agreed — `State: Ready`, `LastTaskResult: 0`, firing every 15 minutes. But the Jarvis-side mirror (`20_Progress/AI/Claude Code/second-brain-claudekit/`) was frozen at 2026-07-30: `Sync-Log.md` hadn't grown since `2026-08-06 16:31`, and the mirrored hook script still carried the old, since-fixed `50_Claude` bug from earlier in this same 2026-08-08/09 session.

**Root cause:** `60_Claude/scripts/sync-jarvis-silent.vbs` (both the repo's own copy and the live copy at Jarvis's `30_Order/System/claude-workflow/scripts/sync-jarvis-silent.vbs`, which Task Scheduler actually executes) hardcoded the pre-rename path `.../50_Claude/scripts/sync-jarvis.sh`. Its `sh.Run(cmd, 0, False)` call is fire-and-forget — the `False` means it doesn't wait for or check the launched command's exit code, so `wscript.exe` itself always exits 0 regardless of whether the inner command succeeds. Every 15 minutes, the launcher fired, tried to run a bash script at a path that no longer existed, failed instantly and silently (before `sync-jarvis.sh`'s own log-writing logic ever ran), while Task Scheduler recorded a false-positive success.

**Fix applied:** Updated the path in both `.vbs` copies to `60_Claude/scripts/sync-jarvis.sh`, re-ran `register-jarvis-sync-task.ps1` (re-copies the fixed launcher to the Windows-side location and re-registers the task), then ran `sync-jarvis.sh` manually to confirm end-to-end: it created a correct `.claude/` folder in the Jarvis mirror (this repo's mirror previously only had a differently-named `Da Shit/` folder), the synced hook now carries the `60_Claude` fix, and `Sync-Log.md` got a genuine new entry (`2026-08-09 00:39:04 OK exit=0`).

`Da Shit/` — the old, differently-named leftover copy — had its rename direction reversed 2026-08-10 (Anant's go-ahead was to drop the rename entirely, keep the literal `.claude/` name going forward). Whether the orphaned folder itself has actually been deleted from the Jarvis mirror was not re-verified in the fifth pass — carried forward as a live open item in `_docs/Repo-Map.md` rather than assumed done.

## Resolved open items, 2026-08-09 through 2026-08-19 (fourth pass)

- [x] `tested-skills/` → `tested-tools/` rename, executed 2026-08-09, restructured into `agents/`, `commands/`, `hooks/`, `skills/` subfolders. `mattpocock-engineering/` moved to `tested-tools/skills/mattpocock-engineering/`.
- [x] `50_Claude`→`60_Claude` naming-collision question, resolved 2026-08-09: intentional, done by Anant, "plainly just a joke or reference... does not mean anything." See `_docs/Design.md`'s amendment.
- [x] `_docs/PRD.md` rewritten 2026-08-09 — state table dropped, points to `Tool Map.md` as sole source of truth; dual-purpose statement added; project list corrected against `MOC.md`.
- [x] `_docs/Architecture.md`, `_docs/Design.md`, `_docs/Jarvis.md`, `_docs/Sync.md` rewritten/amended 2026-08-09 — dual-purpose framing, self-improvement sequencing, the full Jarvis folder map, the sync-launcher incident, and a Tier-1 citation correction (later superseded again 2026-08-19 by a second correction: the real, literally-labeled 6-item "Tier 1: INSTALL NOW" table lives in `PDF's Ingestion Implementation.md`'s Matrix section, not `GitHub Ingestion Implementation.md`'s unlabeled "Priority 1" list).
- [x] `_docs/Current-Setup.md` written up from the raw MCP/plugin/marketplace dump — 18 MCP servers, 3 plugins, 3 marketplaces, categorized with verified purpose where evidenced.
- [x] `60_Claude/Qualification-Checklist.md` updated for the `tested-tools/` use-case-granularity rule and Jarvis-promotion build-standard gate.
- [x] `sandbox/README.md` inventory extended with the 5 confirmed Jarvis-enhancer candidates (`obsidian-mind`, `obsidian-second-brain`, `claude-mem`, `agentic-inbox`, `memsearch` — the last already ruled out) — upstream remotes verified via `git remote get-url`, not guessed.
- [x] Manifest-driven multi-project sync engine built and live 2026-08-10: `60_Claude/scripts/sync-manifest.json` + `sync-all.sh` (superseding `sync-jarvis.sh`), driven by one Windows Scheduled Task (`ClaudeKit-Sync-All`). Old task `SecondBrainClaudekit-JarvisSync` disabled, not deleted, kept as rollback reference.
- [x] `instructions/`, `tests/`, and `tested-tools/_future/` scoped and built 2026-08-19 — `instructions/` populated (later rebuilt on a corrected premise, see below), `tests/` populated with two real entries, `tested-tools/_future/` correctly empty.
- [x] The 15 zero-provenance `agents/`/`commands/`/`hooks/` files (commit `d35f0b7`) and the 3 CPR commands (commit `726f6de`) resolved 2026-08-19 — the 15 relocated to `tested-tools/{agents,commands,hooks}/native-scaffold/` per Anant's `AskUserQuestion` decision; the CPR commands went through the real pipeline, verdict blend, `tested-tools/commands/cpr-compress-preserve-resume/VERDICT.md`. Top-level `agents/`, `commands/`, `hooks/` repurposed as per-destination-project staging (a `docs/<ProjectName>/` sibling added at this point turned out to be a naming error for `_docs/`, removed 2026-08-20).
- [x] `60_Claude/vault-rules/pipeline-conventions.md` written 2026-08-19 — covers `sandbox/<repo-name>/` naming, the `tested-tools/<type>/<use-case>/<repo>/` convention plus `FOR-WHAT.md`, per-destination-project staging, and `instructions/`/`tests/` conventions.
- [x] `60_Claude/README.md`'s `scripts/` row and `_docs/Sync.md`'s framing fixed 2026-08-19 — `sync-all.sh` named as the live engine, `sync-jarvis.sh` as legacy.
- [x] `_docs/How to/` written 2026-08-19 — `README.md`, `review-system.md`, `conversation-capture.md`, `using-staged-artifacts.md`, `tests-and-promotion.md`.
- [x] `CLAUDE.md` and `README.md` updated 2026-08-19 to stop describing the retired flat staging shape.
- [x] **"Still uncommitted," corrected 2026-08-20 (fifth pass).** Tracked as open through the 2026-08-19 third pass ("this session's own Phase 1-7 work... added substantially more on top" of 10+ days of uncommitted work). **Resolved for real** — `git log`/`git status` confirm 8 real commits landed 2026-08-20, working tree clean. This was a genuinely stale open item, corrected rather than carried forward once verified.

## Remaining open items not re-verified in the fifth pass

Carried forward to the live `_docs/Repo-Map.md` without re-checking (no new evidence either way this pass, so neither claimed resolved nor re-confirmed open):
- `gsd-core/`, `adx/`, `agency-agents/`, `agent-skill-simplified-technical-english/`, `Agent-Reach/` in `sandbox/` still have no session-verified intent recorded.
- The `.claude/rules/*.md` auto-load vector from `sandbox/`/`tested-tools/` clones still has no exclusion mechanism, unlike `CLAUDE.md`.
- Portfolio/Trading View/Resq/OpsPilot's flat Jarvis-mirror folders and `.claude_wsl` still need the same clean-rebuild treatment `.claude_windows`/CausalOps/Jarvis already got.
- `second-brain-claudekit/Da Shit/` in the Jarvis mirror — confirmed dead 2026-08-10, deletion itself not re-verified.
- `tested-tools/commands/cpr-compress-preserve-resume/`'s two-level-vs-three-level convention mismatch, flagged in its own `VERDICT.md`, still unresolved.

## `instructions/` build history

**First build (2026-08-19), wrong premise, corrected same day (third pass):** a discovery pass (`find sandbox/ -maxdepth 2 -iname 'CLAUDE.md' -o -iname 'AGENTS.md' -o -iname 'PRD.md'`) found 27 real hits across 19 of the 30 `sandbox/` repos, copied verbatim into `instructions/<repo-name>/<file>` — wrong, because every one of those files already lived unchanged in its source repo, adding a second location for the same fact with zero distinguishing value. Cleared out, rebuilt per the real project list in `60_Claude/scripts/sync-manifest.json` — 8 projects, 17 real instruction files initially, live-synced one-way via a new `instructions_paths` field + `sync-all.sh` logic (design confirmed with Anant via `AskUserQuestion` first; tested by extracting the identical jq+cp logic into a standalone harness, `diff -rq`'d byte-identical against the real tree).

**Scope corrected again 2026-08-20:** `second-brain-claudekit`'s own entry removed from `instructions_paths` — it was mirroring this repo's own root `CLAUDE.md` into a subfolder of itself, a same-repo self-copy with a real "one fact, one home" cost and no functional benefit. 7 projects, 16 real files, going forward.

## `60_Claude/Standards/` and artifact-authoring templates, built 2026-08-19 (third pass)

`Agent Standard.md`, `Skill Standard.md`, `Command Standard.md`, `Hook Standard.md`, `Instructions Standard.md`, `Tested-Tool Promotion Standard.md`, each adapted directly from Jarvis's real `30_Order/Standards/` shape (`Evergreen Standard.md`/`Review Standard.md` read in full first). Paired templates: `60_Claude/Templates/{agent,skill,command,hook}-template.md`. The 7 existing generic PARA vault-note templates were checked against this repo's real git history and confirmed never used here — not deleted, but the "unused in this repo" fact documented rather than left implicit.

## 2026-08-20, fourth pass — gbrain wired and promoted (decision), 3 dormant clones executed for real, `docs/<Project>/` dropped for good

- [x] **gbrain's OpenAI embedding provider wired and verified for real**, not just marked decided. `~/.gbrain/config.json` now correctly persists `embedding_model`/`embedding_dimensions` for the first time; `doctor`'s `embedding_provider` check reports a live, working `openai:text-embedding-3-large` connection; a real test page was imported, embedded, found via genuine semantic search (0.8275 similarity, non-keyword-overlapping query), then cleaned up. Found and worked around a real, previously-undocumented gbrain bug in the process — none of gbrain's own documented embedding-provider-switch commands (`config set`, `init --embedding-model`, `reinit-pglite`) actually clear a stuck `embedding_disabled: true` sentinel; only a direct `~/.gbrain/config.json` edit does. Full account: `tested-tools/mcp-servers/gbrain/VERDICT.md`.
- [x] **gbrain's promotion decision made and recorded: cleared, global candidate.** All four `Promotion-Criteria.md` questions walked through for real against the re-verified state. The actual global `~/.claude/` install has deliberately not happened here; that's a separate session at the Windows/WSL home directory per `_docs/Design.md`.
- [x] **3 of the 6 dormant `sandbox/` clones with recorded next steps actually executed this round**: `spec-kit` (`uv tool install specify-cli`, real `specify init --integration claude` scratch-project run — 10 real skill files scaffolded), `promptfoo` (a real `promptfoo eval` against this repo's own `/challenge` command — 1/2 passed, genuine finding), `claude-context` (real `pnpm install` + `pnpm build:core`; the first index+search run hit a real, named blocker — the Zilliz Cloud cluster was `STOPPED` — a retry after Anant resumed it succeeded: 108 files / 1369 chunks indexed, 4/4 topically correct hits). `TradingAgents`/`OpenBB` stayed out of scope (TradingView-side session). `hiring-agent` not attempted.
- [x] **`docs/<ProjectName>/` decided against, for good.** Asked Anant directly (`AskUserQuestion`); confirmed no live reference remained anywhere. Recorded in `_docs/Gaps.md` as the closing decision.

Full detail, real command output, and the tests/ transcripts for all of the above: `tested-tools/mcp-servers/gbrain/VERDICT.md`, `tests/skills/spec-kit/`, `tests/cli-tools/promptfoo/`, `tests/mcp-servers/claude-context/`, and `_docs/Gaps.md`.
