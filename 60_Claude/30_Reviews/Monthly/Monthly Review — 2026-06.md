---
type: review
status: complete
created: 2026-06-24
tags:
  - review
  - monthly
  - vault-ops
notes:
  - "[[60_Claude/07_AI_Information/Jarvis OS — North Star]]"
  - "[[60_Claude/30_Reviews/North Star Convergence — Change Report 2026-06-11]]"
  - "[[AGENTS.md]]"
  - "[[CLAUDE.md]]"
  - "[[00_Dashboard]]"
---
# Monthly Review — June 2026 (first monthly review)

No monthly-review convention existed before this note — `30_Order/Templates/Enumerate/Better Month.md` is a personal habit-reflection template, not a vault-ops review. This is the first one, built from the full session log (970 lines), all 89 git commits, and a live re-check of the dashboard, capability engine, and `.claude/` layer against what they claim to do.

## The one-sentence theme

The vault produces real, deep work session by session, but nothing has yet verified that a "done" deliverable stays done — three flagship completions this month (the dashboard rebuild, the `.claude/` path-alignment, the MGMT 3001 template standard) were each silently broken or contradicted within two weeks of being signed off, by changes nobody checked against them.

## Scope and method

Reviewed: the entire session log from its first entry (2026-04-08) to its last (2026-06-20); all 89 commits (`git log`) with per-commit file lists for the active period; current folder structure against the log's claims; `00_Dashboard.md`'s actual Dataview queries against the real folder tree; every `next_drill:` date in the vault; and the `.claude/` alignment work done earlier in this same session. Cross-referenced against the vault's own stated plan (`Jarvis OS — North Star`, Part 9's four-move convergence) and the 2026-06-11 Convergence Change Report that claims to have executed it.

## Timeline: what "a month" actually contains

The repo's first commit is 2026-04-23, but real day-to-day usage has a sharp shape:

| Period | Activity |
|---|---|
| 2026-04-23 → 04-28 | Initial build burst: ops CLI, capability engine design, multi-agent PKM plan. 6 commits. |
| 2026-04-28 → 05-26 | **28-day near-silence.** One commit (05-06, BIOL notes). The April capability-engine buildout (24 enriched notes, drill schedules) sat untouched. |
| 05-26 → 06-01 | Restart: Claude Pro workflow setup, vault audits, GitHub-starred-repo ingestion (~95 repos), the first Standards layer. |
| **06-02 → 06-03** | Two commits of 4,185 and 3,320 files. This is not two days of writing — it's the auto-commit hook (likely `obsidian-git` on an interval) sweeping in **five weeks of previously-untracked vault content** in one shot. |
| 06-02 → 06-21 | The real "month": daily auto-commits every 1-3 hours, 70 of the 89 total commits, all dated within these 19 days. |

So "almost a month since we've been using Claude" is accurate for *continuous* use, but the calendar month contains a 4-week dead zone. The dense, evaluable period is 06-02 → 06-24 — about three weeks, not four.

**Finding:** the vault had no real version-control safety net for its first ~5.5 weeks. `Git Recovery and Vault Safety.md` documents a recovery workflow that depended on commits existing to recover *to* — for over a month, they didn't. If anything had been lost between 04-28 and 06-02, there was nothing to roll back to.

## Git hygiene: the log is the only narrative that exists

All 89 commit messages follow one of two patterns: 9 early commits with real messages (`feat: capability engine enrichment...`, `Rearrange Jarvis notes`), and **80 commits reading `auto: YYYY-MM-DD HH:MM | N files`** with zero content description. This is consistent with an interval-based auto-commit plugin, not deliberate checkpoints.

Practical consequence: `git log` cannot answer "what changed and why" for 90% of this vault's history — only "how many files, when." The session log is the *only* place that narrative survives. That makes the log a single point of failure, and the next section shows it has gaps.

**Folder churn since 06-01** (file-touches, excluding `.obsidian`/`.vscode` plugin noise):

| Folder | Touches |
|---|---|
| `60_Claude/` | 569 |
| `10_Areas/` | 394 |
| `20_Progress/` | 307 |
| `40_Resources/` | 74 |
| `.claude/` | 67 |
| `30_Order/` | 56 |

`60_Claude/` being the most-touched folder matches its designed role as the AI workshop. But it's also the folder that got renamed/restructured the most (`50_Reviews`→`30_Reviews`, `35_Outputs` deleted, numbering churn) — which is exactly why `.claude/` (67 touches, mostly path-repair) had to keep chasing it.

**Net markdown churn since 06-01:** 303 files added, 233 deleted (by git history), 883 total `.md` files in the vault today. The deletions are not mostly content loss — most are renames-as-delete+add (git doesn't always detect renames across directory moves) from the multiple `60_Claude` and `40_Resources/CS/AI` restructurings. But that also means: **there is no clean record of which deletions were intentional cleanup versus accidental loss during a reorg.** Nobody has run a "what disappeared and was it supposed to" pass.

## Session log: real gaps, not just thin entries

The log's header claims "append-only," but the first three entries in the file (06-01 ×2, then a 05-31 entry) sit *above* a long, otherwise-chronological run from 2026-04-08 through 2026-05-31 starting at line 52. Three entries were prepended out of normal order at some point; nothing else was. Minor, but worth knowing before trusting line position as a date signal.

The substantive gap: **2026-06-13 18:25 through 2026-06-20 01:29 has no narrative session-log entries**, but git shows 19 commits and real work in that window:
- HIST 1103 and MATH 2230 coursework (assignments, quizzes, homework) — likely direct human edits, not Claude sessions, so its absence from the log is expected.
- Portfolio: 5 security-phase notes (`phase-1-auth-clerk.md` through `phase-5-monitoring.md`), Orby UI fixes, a dark-mode toggle note, a "Global Fixes" note — **none logged.**
- A **second, separate graphify-style codebase export** appeared at `40_Resources/CS/portfolio-graph/` (`00_INDEX`, `01_Overview` through `07_Test_And_Config`) on 06-13 — see Finding 2 below. **Not logged anywhere**, and not mentioned in this conversation's earlier Portfolio-folder audit because it wasn't known to exist until this git-history pass.

The Working Rule "after meaningful vault changes, append a concise continuity entry" was not followed for roughly a third of the active period. This is the direct cause of the `.claude/` repair cycles below — the tool layer kept being told about reorgs after the fact, not from the log, but from someone hitting a stale path.

## What's broken right now (verified, not inferred)

**1. `00_Dashboard.md` — the "Move 3" flagship deliverable — has at least 4 dead Dataview blocks.** The 2026-06-11 Convergence Change Report marks Move 3 complete ("all 13 Dataview queries preserved"). They were preserved verbatim — including paths that don't exist:
- `FROM "10_UMN"` — used in **three** blocks (Open Tasks, Active Classes, Knowledge Enrichment Queue). No `10_UMN` folder has existed since 2026-05-30, when the log itself records this exact bug being found and "fixed" in `AGENTS.md`. It was never fixed in the dashboard.
- `FROM "60_Claude/60_Indexes"` (Recent Claude Outputs exclusion clause) — the real folder is `44_Indexes`, renamed before the dashboard rewrite.
- `FROM "60_Claude/50_Reviews"` + a check against a file named `"50_Reviews Board"` (Recent Reviews) — broken again as of this week's `50_Reviews`→`30_Reviews` rename.

Net effect: the dashboard's "Decay" and "Classes" sections and half its "Vault Health" section have been silently returning empty or wrong results since before this review started. Nobody ran the dashboard and looked at it after the restructure that claimed to fix it.

**2. Two unrelated, non-cross-linked graphify-style exports exist for the same Portfolio codebase.** `20_Progress/Projects/CS/Portfolio/{architecture,chatbot,components,data,communities}` (audited earlier this session — confirmed real graphify output) and `40_Resources/CS/portfolio-graph/{00_INDEX...07_Test_And_Config}` (found only via this git-history pass). Different file-naming conventions, different folders, same source repo, zero links between them found in the earlier audit. This is the over-built-under-converged pattern recurring at the project level, not just the instruction-layer level the North Star diagnosed.

**3. The Capability Engine has been completely idle since 2026-05-09.** Every `next_drill:` date in the vault reads 2026-05-02 or 2026-05-09 — six to seven weeks overdue, zero drilling activity logged in June. This was flagged as a problem in the 2026-05-28 audit ("223-note enrichment queue sitting idle... overdue drills since May 2") and has not moved since. The `learning-agent` exists, is well-specified, and has never been invoked against a real drill session per the log.

**4. The MGMT 3001 gold-standard reference is wired into four live templates, against information the vault owner gave directly this session.** The 2026-06-11 convergence pass added "gold-standard link to MGMT 3001 Week - 4" to `Deep Dive Template.md`, `For Evergreen.md`, `Textbook Template.md`, and `Week Template.md` — not a passing mention, a structural decision baked into the templates every future note inherits from. The vault owner's own assessment (this session): those notes are ungraded AI output dumped during the course, never reviewed, and not a standard to build toward. This isn't a stale path — it's a now-contradicted design decision sitting in the four templates new notes are built from.

**5. `00_Inbox/copilot/` has carried unrouted conversation exports for 80+ days with no triage cadence**, confirmed in this session's earlier audit and unchanged since.

**6. `.claude/` needed reactive path-repair three separate times in under two weeks** — the 2026-06-11 convergence pass (instruction-layer collapse), two separate 2026-06-20 "skill-repair" sessions (12+ stale paths fixed, then a second pass for `45_Outputs`→`35_Outputs`), and this session's pass (`50_Reviews`→`30_Reviews`, `35_Outputs` deleted entirely, `40_Resources/CS/AI` subfoldered, UMN split). `mcp-hub.md` was specifically designed in April to catch exactly this class of drift via `/mcp-hub sync` — checking that every wrapper file's referenced paths actually resolve. There is no log entry showing it has ever been run.

## What was done correctly — specific, not generic credit

**Coursework production is the most consistently strong work all month.** CSCI 2041 (24 concept notes, 15 weekly notes, final review map, lab anchors, project notes — built, then re-polished twice for Weeks 1-5), BIOL 1012 Theme 4 (9 notes, then independently re-reviewed and deepened by Claude *against* what Codex produced, catching real gaps), and the June HIST 1103/MATH 2230 ingestion (verified line-by-line against source PDFs, with genuine source conflicts flagged rather than silently resolved) all show the same good pattern: read the actual source, cross-check claims against it, name disagreements instead of papering over them.

**The Standards + Workflows layer filled a real, long-open gap.** `30_Order/Standards/` (5 docs) and `30_Order/Workflows/` (8 docs) were explicitly named as missing in the 2026-05-31 audit and the Vault Architecture's own "open questions" list, and got built within days — not just stubbed, but mapped one-to-one to existing templates with failure modes and done-conditions.

**The ingestion pipeline was hardened by live testing, not speculation.** The 2026-06-20 GitHub-ingestion work didn't just add a routing-table row — it ran two real ingestions in parallel (a web clip vs. a live `gh api` pull of the same repo), found a real discrepancy between them, and used that to design the two-tier depth rule (reference-only vs. adoption-candidate). Two more failure modes (empty iframe, index-page-not-article) were discovered the same way: by running the method and watching it fail, then documenting the fix.

**This session's `.claude/` repair was thorough and verified on disk**, not just edited and assumed correct — every corrected path was checked against the actual filesystem before being called done. That's the standard the dashboard fix and the others above did not meet.

## Root cause, stated once

Every recurring failure this month traces to one mechanism: **structural changes to the vault (renames, deletions, folder moves) happen faster than anything checks whether dependents still resolve, and the one tool built to check this (`/mcp-hub sync`) has never been run.** The North Star's own diagnosis — "no deletion discipline... redundancy multiplies" — is about instruction files, but the same disease is now visible in project folders (the duplicate Portfolio exports) and in the dashboard (queries nobody re-ran). The fix isn't more documentation; it's running the verification step that already exists, and doing it as part of finishing a restructure, not as a separate reactive session two weeks later.

## Priorities for month 2, ranked

1. **Fix `00_Dashboard.md`'s four dead queries** (`10_UMN`→`10_Areas/UMN` or split per the UMN reorg, `60_Indexes`→`44_Indexes`, `50_Reviews`→`30_Reviews`) and actually open the dashboard to confirm each block renders rows. This is cheap and the dashboard is supposed to be the daily surface — right now a third of it is silently empty.
2. **Run `/mcp-hub sync` (or build it if it was never wired) at the end of any session that renames or deletes a folder.** This is the single highest-leverage fix for the recurring `.claude/` breakage — it turns a 2-week-later reactive repair into a same-session catch.
3. **Decide what to do with the duplicate Portfolio graph exports** (`20_Progress/.../Portfolio/{architecture,...}` vs `40_Resources/CS/portfolio-graph/`) before a third one appears from a future graphify run landing in `40_Project_Briefs/` per the plan discussed earlier this session.
4. **Either resume the Capability Engine or formally retire it.** Six-plus weeks idle on a system designed for spaced repetition is past the point where "next_drill" dates mean anything; either run a real drill session or stop pretending the dates are live.
5. **Strip or re-source the MGMT 3001 gold-standard links in the four templates** now that their basis has been explicitly invalidated by the vault owner.
6. **Close the Inbox backlog** — 80+ days of Copilot exports sitting unrouted in `00_Inbox/copilot/`.
7. **Reconcile the 233 net-deleted markdown files since 06-01** — confirm none of them were real content loss from a reorg rather than intentional cleanup.

## Open questions for you

- Should session-log discipline be enforced by a hook (PostToolUse / SessionEnd already exist) rather than relying on remembering to write the entry? The 7-day gap this month happened despite the rule already being written down.
- Now that `60_Claude/40_Project_Briefs/` is slated to become the graphify landing zone, does the `40_Resources/CS/portfolio-graph/` export get folded into that pipeline retroactively, deleted, or left as-is?
- Do you want a monthly review to become a recurring skill (like `/weekly-review` but scaled), or was this a one-time forensic pass?
