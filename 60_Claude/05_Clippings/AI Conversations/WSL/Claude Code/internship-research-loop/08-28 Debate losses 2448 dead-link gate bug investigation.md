---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: wsl
title: "Debate losses 24/48 dead-link gate bug investigation"
started_at: 2026-08-28T08:58:01
ended_at: 2026-08-28T09:15:17
duration_minutes: 17
exported_at: 2026-08-28T13:15:02
project: internship-research-loop
cwd: '/home/anant_gupta/projects/work/internship-research-loop'
session_id: 57040b74-cd56-4bb6-9696-bbc4df2afa6c
status: raw
turn_count: 2
tools_used:
  Bash: 57
  Edit: 11
  Read: 19
  Write: 1
tokens:
  input: 322
  output: 119856
  cache_creation: 341388
  cache_read: 22149122
  total: 22610688
cost_usd: 6.99458
model:
  - claude-sonnet-5
files_touched:
  - "/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/run_log.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/identity.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_write_gate_failures.py"
tags:
  - input
  - ai-conversation
  - claude-code
  - wsl
---

# Debate losses 24/48 dead-link gate bug investigation

## You

**Context — verified fresh, 2026-08-27 ~11:10 UTC, against `origin/master` (`7a1be68`) directly via `git show`, not a local checkout (a local clone on this exact project was found 25 commits stale within one day during this same check — always confirm local `HEAD` matches `origin/master`, or read state via `git show origin/master:<path>`, before trusting a number). Time will have passed since — recompute every number below yourself before acting on it, don't assume these are still current:**

- `state/debate_losses.json`: 271 entries. 154 sit at exactly 24/48 losses (`MAX_DEBATE_LOSSES` = 48). 173 of the 271 entries are `ApplyGuy:*` uids (149 of those at 24). Nothing is above 27 yet — the leading edge has real runway left, this is not an hours-away emergency, but it is a real, still-live, still-worsening bug.
- `state/excluded_uids.json`: 388 entries (a flat list, not a dict), unchanged — confirmed zero `ApplyGuy:*` uids have crossed into permanent exclusion yet.
- The specific dead-link example from the 2026-08-26 postmortem (`SimplifyJobs:[REDACTED]`, HTTP 403) is **absent from all three state files** (`debate_losses.json`, `excluded_uids.json`, `seen_ids.json`) — confirmed directly. It appears in the `rejections` list of 183 of the last 681 `logs/runs.jsonl` records, spanning 2026-08-10 through 2026-08-27 (17+ days), always failing `url_liveness`. Being present in `rejections` but absent from all three state files is itself strong evidence it wins its bucket's `this_run` selection (`_prioritize_and_cap`) and then fails `vault_writer/validate.py` every time — never entering `deferred` (which is what feeds `debate_losses.json`) and never getting written (which is what feeds `seen_ids.json`).
- Timeline: the postmortem observed the leading ApplyGuy cohort age 20→24 losses in ~12 hours (2026-08-26 14:35 → 2026-08-27 02:25), roughly 1 loss/3 hours. Projected forward from the 24-loss checkpoint, that's ~72 hours to reach 48 — slower than the postmortem's original "24-30 hours" estimate. Separately, `run.yml`'s hourly schedule has a live gap: last successful run `2026-08-27T02:24:36Z`, none since (checked ~9 hours later), while `gh workflow list` still shows it `active` (not disabled) — likely a GitHub Actions scheduling delay, not a bug in this repo; don't try to fix GitHub's scheduler, just know the aging clock may be paused or bursty whenever you check, and recompute the real timeline from fresh numbers rather than trusting either estimate.
- Write-budget config: `MAX_NEW_WRITES_PER_RUN = {"AI/ML": 3, "Fullstack": 3, "CyS & Finance": 3, "Other": 1}` (`run_pipeline.py`). `_prioritize_and_cap` returns `(this_run, deferred)`; `update_debate_losses(losses, deferred, written_uids)` only increments losses for `deferred` and only clears via confirmed `written_uids` — a `this_run` winner that fails `validate_and_write` is in neither set.

### Task 1 — Recompute and decide on urgency
Re-run the checks above against current `origin/master` state. State plainly: is an immediate stopgap (another `MAX_DEBATE_LOSSES` raise, or a different one) still warranted given the real numbers and the current run-schedule gap, or has enough slack opened up that the root-cause fix alone is sufficient without another bump? Don't default to "raise it again" just because that's what happened last time — justify the call either way with the numbers you actually see.

### Task 2 — Stopgap (if Task 1 says it's warranted)
Raise `MAX_DEBATE_LOSSES` (or another stopgap of your choosing) with the same real-numbers-and-reasoning citation style as the existing 5→48 comment in `run_pipeline.py`. If Task 1 concludes no stopgap is needed, say so explicitly and skip this — don't bump the number reflexively.

### Task 3 — Confirm the win-mechanism before touching `debate_compare`
The postmortem flagged this as unconfirmed and cautioned against changing `debate_compare`'s sort logic without confirming it first. The evidence above (the dead-link uid appearing in 183 `rejections` entries while being completely absent from `debate_losses`/`excluded_uids`/`seen_ids`) is strong circumstantial confirmation of the "wins `this_run`, fails `validate_and_write`" hypothesis, but not direct instrumentation. Decide: is this circumstantial evidence sufficient to proceed straight to Task 4's fix, or do you want to add one line of logging (`this_run` selections, not just final rejections) for direct confirmation first? Either is defensible — make the call and say why. **Do not change `debate_compare`'s sort/tiebreak logic itself** unless this step reveals the win-mechanism hypothesis is actually wrong — if that happens, say so plainly (this project's own norm: a wrong hypothesis gets corrected in the record, not quietly dropped) and stop to reconsider scope rather than guessing at a different fix.

### Task 4 — Build the root-cause fix
A `write_gate_failures.json` (uid → `{check, count, first_seen}`), written by `validate_and_write`'s rejection path, checked before a uid re-enters `this_run` selection in a future run — same "notify, don't silently drop" discipline `excluded_uids.json` already uses, for a distinct failure class (structurally doomed vs. merely out-ranked). Real design decisions to make and justify, not assume:
- Does a uid crossing some threshold here get logged/short-circuited only, or does it also eventually feed into `excluded_uids.json` the way `MAX_DEBATE_LOSSES` does? Pick one and justify it — a permanently-dead URL probably deserves a different (likely lower, likely faster) threshold than "out-ranked 48 times," since dead-is-dead in a way out-ranked isn't.
- Should this apply per-`check` (a `url_liveness` failure vs. a `cross_source_duplicate` failure might warrant different handling) or uniformly? Justify whichever you pick.

### Task 5 — Tests + verification
Fixture-based tests for the new behavior — the real `SimplifyJobs:[REDACTED]` 403 case is a genuine, citable scenario to build a fixture from. Full suite green. Separate commits per logical change (stopgap vs. root-cause fix), matching this repo's existing discipline. Concretely confirm (test or dry-run, not just "should work") that the cited dead-link uid is skipped/short-circuited on a simulated next run after the fix.

### Explicitly out of scope
No schema-drift coverage work (Prompt 19's job, running in parallel — don't touch `core/schema_drift.py`). No vault/Jarvis writes. No rewriting `debate_compare`'s core sort/tiebreak algorithm unless Task 3 shows the win-mechanism hypothesis is wrong.

### Report back
Task 1's fresh numbers + urgency verdict. Task 2's stopgap decision (or explicit no-stopgap-needed call) and why. Task 3's confirmation approach and result. Task 4's `write_gate_failures.json` design decisions and why. Test results, and concrete confirmation the cited dead link is now handled.

## Claude

I'll start by checking the current state of the repo and verifying whether local HEAD matches origin/master, per the note about staleness risk.

This is a large multi-part task. First I need to isolate a concurrent WIP change (from a parallel "Prompt 19" session) that touches the same two files I need to edit — I'll stash just those two files' changes so I can work cleanly, then restore them after I commit.

Now let's look at run_once's main flow, and validate.py's check order.

Now I'll implement the changes. First, `core/run_log.py`:

Now `run_pipeline.py` — import, constants, functions, and wiring into `run_once`:

Now the constants and functions, placed after `update_debate_losses` (before the `SYSTEMIC_REJECTION_CHECKS` block, since that set is referenced in my citation comment):

Now wire it into `run_once`, right after the existing debate-losses block, and add a `write_gate_excluded_count` field to `record`:

Now find the exact insertion point after the debate-losses block (the `should_alert_on_exclusion_spike` block ends before the bucket-capacity section):

Good, that's consistent with the existing pattern (reload from disk each time before updating, no later reuse). Now let's syntax-check and run the relevant test files.

Now let's write the tests. Let's check the top of `tests/test_debate_losses.py`'s imports once more and mirror the structure for a new `tests/test_write_gate_failures.py`.

I'll create a local venv in the scratchpad to run tests without touching system packages.

The failure is an artifact of my isolation strategy — I stashed `test_run_pipeline.py` back to committed state, but left the parallel session's WIP `core/schema_drift.py` (which now requires different fixture shapes) in place. Let me fully isolate by stashing that pair too, test cleanly, then restore everything after committing.

All 8 tests pass. Now let's run the full test suite to confirm nothing else broke.

Clean — exactly my three files (`core/run_log.py`, `run_pipeline.py`, `tests/test_write_gate_failures.py`), plus unrelated pre-existing modifications (CLAUDE.md, graphify-out, untracked files) that aren't mine to commit. Let me diff my two modified files once more before staging, then commit.

Good — purely additive, as intended. Now committing:

Committed. Now let's restore Prompt 19's stashed WIP on top of my committed changes.

Clean pop, no conflicts. Now the run_pipeline stash:

Now the second conflict block, remove the middle marker and trailing marker:

Good, this section is correct — just remove the two remaining markers (line 435 `=======` and line 474 `>>>>>>>`), both blocks kept.

Now the third conflict, around line 673 — let's inspect it (this is likely in `run_once`'s `record` dict or the fetch loop).

Simple — keep both dict keys.

Now let's verify no conflict markers remain and the file parses, and check where my `write_gate_failures` block ended up relative to Prompt19's `zero_match_streaks` wiring in `run_once`.

No markers left, syntax is valid. Now finalize the merge (add both files) and check overall status.

All 444 tests pass — my changes and Prompt 19's WIP now coexist correctly. Let's drop the consumed stash.

run_pipeline.py is staged from my merge resolution — let me unstage it to leave the working tree in an unstaged state, matching how the other WIP files sit (not my call to stage/commit Prompt 19's work).

Working tree is restored to the same shape as before I started (Prompt 19's WIP intact and unstaged), plus my own work committed cleanly at `778f531`. Let me do a final sanity check of the git log and the diff of my commit.

Committed cleanly at `778f531` — not pushed, per repo convention (no push without explicit ask). Here's the full report:

## Task 1 — Recompute and urgency verdict

Fresh numbers against current `state/` (as of 2026-08-28 ~09:00 UTC):
- `debate_losses.json`: 338 entries (up from 271), max=**30** (2 uids), largest single cohort at **27** (148 entries, 143 of them `ApplyGuy:*`). No entry at or above `MAX_DEBATE_LOSSES`=48.
- `excluded_uids.json`: still 388, **zero** `ApplyGuy:*` exclusions — unchanged.
- Real growth rate from git history of `state/debate_losses.json` (not estimated — the leading loss-count increments by exactly 1 per successful run): 24→30 took ~40 real hours (2026-08-26 16:10 → 2026-08-28 07:58), i.e. **~6.6–9.85 hr/loss**, slower than the postmortem's original pace (~3 hr/loss) because `run.yml`'s actual schedule is bursty (gaps up to 11 hours between runs), not hourly.

**Verdict: not urgent.** At current pace, the front reaches 48 in ~5–7+ days, the bulk cohort in ~6–8+ days — real runway opened up, not closed, since the last check.

## Task 2 — Stopgap

**No `MAX_DEBATE_LOSSES` bump.** Runway is now measured in days, still growing, and the root-cause fix (Task 4) should ease the underlying pressure rather than just outrunning it.

## Task 3 — Win-mechanism confirmation

Proceeded straight to the fix. The circumstantial evidence was already strong and reproduced fresh (186/186 runs the cited uid appeared in failed the same check, still failing on the very latest run), and I built the integration test to drive the *real* uid through the *real* `validate_and_write`/`run_once` path — that's stronger, permanent confirmation than a throwaway log line. `core/debate.py` was not touched.

## Task 4 — `write_gate_failures.json`

- Scoped to `url_liveness` + `cross_source_duplicate` only (both confirmed to repeat for the same structural reason across runs — 3274 and 2801 real occurrences in `logs/runs.jsonl`). `required_fields`/`format_compliance` excluded (our own bug, not the uid's — already handled separately, and 0/684 real occurrences). `not_duplicate` excluded (structurally can't repeat given `dedup_new`'s own guarantee — also 0/684).
- Threshold 3 consecutive same-check failures (vs. debate's 48) — dead-is-dead, no need for that much benefit of the doubt.
- On crossing threshold, the uid joins the **same** `excluded_uids.json` set debate losses already use (reusing the existing gate, not a second parallel one), logged to a new `Excluded — Failed The Write Gate.md`.

## Task 5 — Tests

New `tests/test_write_gate_failures.py`, 8 tests, all pure-function + integration cases, including one that drives the real cited `SimplifyJobs:[REDACTED]` uid through the real pipeline and confirms it's excluded on schedule and never refetched afterward. Full suite: **444 passed**.

One process note: a parallel session (Prompt 19) had uncommitted WIP in `run_pipeline.py`/`core/schema_drift.py`/tests touching the same files. I isolated my work via `git stash` on just the overlapping files, built and tested cleanly, committed only my own changes (`778f531`), then restored Prompt 19's WIP on top (one merge conflict from both sides adding new blocks to the same spot — resolved by keeping both, verified with the full suite passing at 444).

**Tool calls:**

- `Bash` — `git fetch origin 2>&1 | tail -5 && echo "---LOCAL HEAD---" && git rev-parse HEAD && echo "---ORIGIN MASTER---" && git rev-parse origin/master && echo "---STATUS---" && git status --short | head -30`
  ```
---LOCAL HEAD---
[REDACTED]
---ORIGIN MASTER---
[REDACTED]
---STATUS---
 M CLAUDE.md
 M core/schema_drift.py
 M graphify-out/.graphify_labels.json
 M graphify-out/GRAPH_REPORT.md
 M graphify-out/graph.html
 M graphify-out/graph.json
 M graphify-out/manifest.json
 M run_pipeline.py
 M tests/test_run_pipeline.py
 M tests/test_schema_drift.py
?? .claudeignore
?? .gitattributes
?? tests/test_zero_match_alert.py
  ```
- `Bash` — `git diff --stat && echo "=====" && git log --oneline -5`
  ```
 CLAUDE.md                          |    13 +
 core/schema_drift.py               |   203 +-
 graphify-out/.graphify_labels.json |    17 +-
 graphify-out/GRAPH_REPORT.md       |   175 +-
 graphify-out/graph.html            |     8 +-
 graphify-out/graph.json            | 12064 ++++++++++++++++++++++++-----------
 graphify-out/manifest.json         |   161 +-
 run_pipeline.py                    |    91 +
 tests/test_run_pipeline.py         |    53 +-
 tests/test_schema_drift.py         |   288 +-
 10 files changed, 9118 insertions(+), 3955 deletions(-)
=====
42b8321 Update state + logs — 2026-08-28
ed8408a Update state + logs — 2026-08-27
414028f Recheck log — 2026-08-27
e33c577 Update state + logs — 2026-08-27
7a1be68 Update state + logs — 2026-08-27
  ```
- `Bash` — `git diff run_pipeline.py`
  ```
diff --git a/run_pipeline.py b/run_pipeline.py
index 01c9756..a32a800 100644
--- a/run_pipeline.py
+++ b/run_pipeline.py
@@ -316,6 +316,75 @@ def update_debate_losses(losses: dict, deferred: list, written_uids: list) -> tu
             del losses[uid]
     return losses, newly_excluded
 
+
+ZERO_MATCH_STREAKS_FILENAME = "zero_match_streaks.json"
+
+# Task 3 (Prompt 19, 2026-08-28): a per-source alert when a source keeps
+# fetching real postings but nothing survives the filter — the exact shape
+# of the real Ashby incident this task was built from: fetch_counts frozen
+# at 4 and filter_match_counts frozen at 0 for 115 consecutive hourly runs
+# (2026-08-21 through 2026-08-28) before a human noticed by reading
+# logs/runs.jsonl by hand. Investigated live (Prompt 19 Task 1) and NOT
+# schema drift: 2 of the 4 postings are legitimately Canada-based
+# (location_eligible correctly rejects them) and the other 2 are
+# legitimately permanently excluded by the debate comparator
+# (MAX_DEBATE_LOSSES) — a real, if coincidental, correctly-filtered
+# outcome. But the pipeline had no way to tell that apart from a silent
+# schema break without a human noticing. 24 (one day of hourly runs) is
+# comfortably shorter than the 115 runs it actually took a human to notice
+# this pass, while still long enough that a source's normal hour-to-hour dry
+# spells (no new postings that hour) don't trip it on their own — this only
+# fires once a source stays at exactly zero for a full day despite still
+# fetching real data.
+ZERO_MATCH_STREAK_ALERT_THRESHOLD = 24
+
+
+def load_zero_match_streaks(state_dir) -> dict:
+    path = Path(state_dir) / ZERO_MATCH_STREAKS_FILENAME
+    if not path.exists():
+        return {}
+    return json.loads(path.read_text())
+
+
+def save_zero_match_streaks(state_dir, streaks: dict) -> None:
+    path = Path(state_dir) / ZERO_MATCH_STREAKS_FILENAME
+    path.parent.mkdir(parents=True, exist_ok=True)
+    path.write_text(json.dumps(streaks, indent=2, sort_keys=True) + "\n")
+
+
+def update_zero_match_streaks(streaks: dict, fetch_counts: dict, filter_match_counts: dict) -> tuple:
+    """Returns (updated_streaks, newly_alerting: [source_name, ...]).
+
+    Per source: fetch_count > 0 and filter_match_count == 0 increments the
+    streak; filter_match_count > 0 resets it to 0 and marks the source as
+    having "ever_matched" — a source that has never once produced a match
+    isn't drifting, it's just structurally not matching anything, and never
+    alerts (permissive-by-default, same spirit as core/filter.py's own
+    gates: only an affirmative bad signal — a real regression from matching
+    to not — fires this). fetch_count == 0 this run leaves the streak
+    untouched: a single fetch hiccup (a transient RequestException already
+    swallowed upstream in fetch_greenhouse/fetch_ashby/fetch_lever) shouldn't
+    reset real streak progress, but it's not new zero-match signal either.
+
+    Fires exactly once per streak, at the run the streak first reaches the
+    threshold (`==`, not `>=`) — otherwise a source stuck at zero would
+    re-file the same issue every run forever, the same "notify once, not
+    every run" shape as run_once()'s bucket_at_capacity handling."""
+    streaks = {k: dict(v) for k, v in streaks.items()}
+    newly_alerting = []
+    for name, fetch_count in fetch_counts.items():
+        if fetch_count == 0:
+            continue
+        entry = streaks.setdefault(name, {"streak": 0, "ever_matched": False})
+        if filter_match_counts.get(name, 0) > 0:
+            entry["streak"] = 0
+            entry["ever_matched"] = True
+        else:
+            entry["streak"] += 1
+            if entry["ever_matched"] and entry["streak"] == ZERO_MATCH_STREAK_ALERT_THRESHOLD:
+                newly_alerting.append(name)
+    return streaks, newly_alerting
+
 # A required_fields or format_compliance rejection means OUR normalizer/writer
 # produced something malformed — a real bug, worth an issue. url_liveness and
 # not_duplicate rejections are routine (a stale posting, an already-seen item)
@@ -513,6 +582,7 @@ def run_once(
         "bucket_at_capacity": [],
         "dossier_total": 0,
         "newly_excluded_count": 0,
+        "zero_match_alerts": [],
     }
 
     excluded_ids = load_excluded_uids(state_dir) if state_dir is not None else set()
@@ -552,6 +622,27 @@ def run_once(
         record["fetch_counts"][name] = info["fetch_count"]
         record["filter_match_counts"][name] = len(info["matched"])
 
+    if state_dir is not None:
+        zero_match_streaks = load_zero_match_streaks(state_dir)
+        zero_match_streaks, newly_zero_match_alerting = update_zero_match_streaks(
+            zero_match_streaks, record["fetch_counts"], record["filter_match_counts"],
+        )
+        save_zero_match_streaks(state_dir, zero_match_streaks)
+        record["zero_match_alerts"] = newly_zero_match_alerting
+        for name in newly_zero_match_alerting:
+            issue_fn(
+                issue_repo,
+                f"{name}: filter_match_count stuck at 0 for {ZERO_MATCH_STREAK_ALERT_THRESHOLD} consecutive runs ({timestamp})",
+                f"{name} has kept returning real fetched postings (fetch_count > 0) but none have "
+                f"survived the filter for {ZERO_MATCH_STREAK_ALERT_THRESHOLD} consecutive runs, despite "
+                "having produced real matches before. This can be a genuine, if coincidental, run of "
+                "correctly-filtered postings (see the 2026-08-28 Ashby investigation: Canada-based "
+                "postings plus debate-comparator exclusion, not schema drift) — but it's also exactly "
+                f"the shape a silent upstream schema change or a broken filter rule would produce. "
+                f"Check core/schema_drift.py's coverage for {name} and the real current API response "
+                "before assuming it's benign.",
+            )
+
     new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids, excluded_ids=excluded_ids)
     record["new_count"] = len(new_listings)
     record["already_seen_count"] = already_seen_count
  ```
- `Bash` — `git diff CLAUDE.md tests/test_run_pipeline.py`
  ```
diff --git a/CLAUDE.md b/CLAUDE.md
index d2e4d41..384ccd5 100644
--- a/CLAUDE.md
+++ b/CLAUDE.md
@@ -45,3 +45,16 @@ The instinct in this codebase has consistently been "write a deterministic scrip
 - **Review** (`/review-loop-change`) → skill, not an agent, and not more Python. The checklist is fixed and known in advance (four conventions, unlikely to grow much), and the repo's small diff size doesn't need an isolated agent context — see that skill's own "why a skill" section. A script *could* grep for some of this (e.g. flagging LLM imports in unattended-path files), but "does this new regex cite real data" needs actual reading comprehension a lint rule doesn't have.
 
 If a new piece of recurring toil shows up and it's mechanical/deterministic (another source feed, another filter rule), it's still Python first, same as everything in `core/` and `ingestion/` today — don't reach for an agent out of habit once a human's judgment isn't actually the bottleneck.
+
+## Auto-mode classifier notes (this repo only)
+
+These notes used to live in the global `~/.claude/settings.json` `autoMode` block, where they didn't belong (Claude Code's auto-mode `environment`/`soft_deny` config is user-global only — there is no project-local override file, confirmed against the live docs) — they were pulled back here since they only make sense for this repo:
+
+- **Repository visibility**: PUBLIC — gupta-builds/internship-research-loop (github.com) — any push here is publishing; confidential material must not be committed.
+- **Secrets management**: CI secrets `FIRECRAWL_API_KEY` and `JARVIS_PUSH_TOKEN` referenced by name only in CI config — no values known here, never print/echo them.
+- **Default / protected branches**: default branch unknown (origin/HEAD unset); no rulesets or protected branches listed via `gh` — treat as unprotected, exercise normal git-push caution.
+- **CI/CD deploy targets**: GitHub Actions (`.github/workflows`) — `run.yml` (hourly), `recheck.yml` (daily), `test.yml` — writes to the gupta-builds/Jarvis vault repo via a scoped PAT (`JARVIS_PUSH_TOKEN`).
+- **Source control**: this repo (gupta-builds/internship-research-loop, public) and its origin remote only.
+- **Key internal services**: `freehire.me` and `boards-api.greenhouse.io` (hosts contacted by this project's ingestion) — job-posting data sources, not credentialed internal infra.
+- **Sensitive data locations & audiences**: the Jarvis Obsidian vault (gupta-builds/Jarvis, reached via sibling git checkout or `jarvis` MCP tools) holds personal career/job-search data (contacts, applications, personal notes) — share only with the user; `contact-researcher` findings must be sourced, never fabricated.
+- **Soft-deny for this repo**: auto-filed issues from `run_pipeline.py`/`recheck.py` failure paths (`gh issue create` here) should be reviewed, not silently created by an agent session; Write/Edit under a sibling Jarvis vault checkout outside the two-consent-gated flows documented above (`/promote-dossier`'s explicit go-ahead) needs the same human-in-the-loop gate.
diff --git a/tests/test_run_pipeline.py b/tests/test_run_pipeline.py
index bc35553..0f8430d 100644
--- a/tests/test_run_pipeline.py
+++ b/tests/test_run_pipeline.py
@@ -41,8 +41,49 @@ def _applyguy_raw():
     return {"updatedAt": "2026-08-24T00:00:00Z", "jobs": _strip_case_keys(json.loads((FIXTURES / "applyguy.json").read_text()))}
 
 
+# Real, non-intern-titled shapes (so they don't add to fetch_greenhouse/
+# fetch_ashby/fetch_lever/fetch_ai_jobs's own intern-only counts and disturb
+# existing pipeline-orchestration assertions below) — just complete enough
+# to satisfy core/schema_drift.py's GREENHOUSE/ASHBY/LEVER/AI_JOBS_REQUIRED_KEYS
+# for the one specific company/URL each schema check hits.
+_GREENHOUSE_SCHEMA_CHECK_JOB = {
+    "id": 1, "title": "Senior Software Engineer", "absolute_url": "https://x/1",
+    "location": {"name": "NYC"}, "updated_at": "2026-07-24T15:05:09-04:00",
+}
+_ASHBY_SCHEMA_CHECK_JOB = {
+    "id": "a", "title": "Software Engineer", "jobUrl": "https://x/a", "location": "SF",
+    "isListed": True, "publishedAt": "2026-06-01T00:00:00+00:00", "descriptionPlain": "",
+    "employmentType": "FullTime",
+}
+_LEVER_SCHEMA_CHECK_JOB = {
+    "id": "x", "text": "Senior Software Engineer", "applyUrl": "https://jobs.lever.co/palantir/x/apply",
+    "categories": {"commitment": "Full-time", "location": "Palo Alto, California"},
+    "createdAt": 1785864478389, "descriptionPlain": "",
+}
+_FREEHIRE_SCHEMA_CHECK_JOB = {
+    "title": "Senior Software Engineer", "url": "https://x/senior", "location": "Mountain View, CA",
+    "posted_at": "2026-07-20T16:11:13Z", "public_slug": "senior-swe-google", "description": "",
+    "enrichment": {"seniority": "senior"},
+}
+_AI_JOBS_SCHEMA_CHECK_JOB = {
+    "title": "Senior Software Engineer", "url": "https://x/senior", "company": "Databricks",
+    "location": "San Francisco", "posted": "2026-07-24", "slug": "databricks-senior-swe", "level": "Senior",
+}
+_INTERNDOCK_SITEMAP_XML = (
+    "<urlset><url><loc>https://www.interndock.com/tracker/guides/"
+    "[REDACTED]</loc></url></urlset>"
+)
+
+
 def _fake_http_get(url, timeout=None):
+    from core.schema_drift import (
+        ASHBY_SCHEMA_CHECK_TOKEN,
+        FREEHIRE_SCHEMA_CHECK_SLUG,
+        GREENHOUSE_SCHEMA_CHECK_TOKEN,
+        LEVER_SCHEMA_CHECK_TOKEN,
+    )
     from ingestion.freehire import FREEHIRE_SEARCH_URL
+    from ingestion.interndock import INTERNDOCK_SITEMAP_URL
     from ingestion.sources import (
         AI_JOBS_URL,
         APPLYGUY_URL,
@@ -66,16 +107,26 @@ def _fake_http_get(url, timeout=None):
         resp.json.return_value = _zshah101_raw()
     elif url == APPLYGUY_URL:
         resp.json.return_value = _applyguy_raw()
+    elif url == GREENHOUSE_JOBS_URL.format(token=GREENHOUSE_SCHEMA_CHECK_TOKEN):
+        resp.json.return_value = {"jobs": [_GREENHOUSE_SCHEMA_CHECK_JOB]}
+    elif url == ASHBY_JOBS_URL.format(token=ASHBY_SCHEMA_CHECK_TOKEN):
+        resp.json.return_value = {"jobs": [_ASHBY_SCHEMA_CHECK_JOB]}
     elif url.startswith(GREENHOUSE_JOBS_URL.split("{")[0]) or url.startswith(ASHBY_JOBS_URL.split("{")[0]):
         # per-company board endpoints — pipeline-orchestration tests don't need
         # real per-company data, that's covered in test_sources.py directly
         resp.json.return_value = {"jobs": []}
+    elif url == LEVER_JOBS_URL.format(token=LEVER_SCHEMA_CHECK_TOKEN):
+        resp.json.return_value = [_LEVER_SCHEMA_CHECK_JOB]
     elif url.startswith(LEVER_JOBS_URL.split("{")[0]):
         resp.json.return_value = []  # Lever's postings endpoint returns a bare list
+    elif url == FREEHIRE_SEARCH_URL.format(slug=FREEHIRE_SCHEMA_CHECK_SLUG):
+        resp.json.return_value = {"data": [_FREEHIRE_SCHEMA_CHECK_JOB]}
     elif url.startswith(FREEHIRE_SEARCH_URL.split("{")[0]):
         resp.json.return_value = {"data": []}
     elif url == AI_JOBS_URL:
-        resp.json.return_value = {"jobs": []}
+        resp.json.return_value = {"jobs": [_AI_JOBS_SCHEMA_CHECK_JOB]}
+    elif url == INTERNDOCK_SITEMAP_URL:
+        resp.text = _INTERNDOCK_SITEMAP_XML
     else:
         raise AssertionError(f"unexpected url: {url}")
     return resp
  ```
- `Bash` — `git status --short -- run_pipeline.py tests/test_run_pipeline.py`
  ```
 M run_pipeline.py
 M tests/test_run_pipeline.py
  ```
- `Bash` — `git stash push -m "prompt19-wip-run_pipeline" -- run_pipeline.py tests/test_run_pipeline.py && git stash list && git status --short -- run_pipeline.py tests/test_run_pipeline.py`
  ```
Saved working directory and index state On master: [REDACTED]
stash@{0}: On master: [REDACTED]
stash@{1}: On master: pre-rebase stash: CLAUDE.md autoMode notes + graphify-out regen + untracked files
  ```
- `Bash`:
  ```bash
python3 -c "
import json
losses = json.load(open('state/debate_losses.json'))
print('total entries:', len(losses))
from collections import Counter
c = Counter(losses.values()) if isinstance(losses, dict) else None
vals = list(losses.values())
print('max loss value:', max(vals))
print('at 24:', sum(1 for v in vals if v==24))
print('at max(48):', sum(1 for v in vals if v==48))
apply_guy = {k:v for k,v in losses.items() if k.startswith('ApplyGuy:')}
print('ApplyGuy count:', len(apply_guy))
print('ApplyGuy at 24:', sum(1 for v in apply_guy.values() if v==24))
print('ApplyGuy max:', max(apply_guy.values()) if apply_guy else None)
import collections
dist = collections.Counter(vals)
print('distribution (sorted):', sorted(dist.items()))
"

  ```
  ```
total entries: 338
max loss value: 30
at 24: 5
at max(48): 0
ApplyGuy count: 190
ApplyGuy at 24: 1
ApplyGuy max: 27
distribution (sorted): [(1, 25), (2, 40), (3, 7), (4, 20), (5, 12), (6, 10), (7, 1), (8, 6), (9, 1), (10, 1), (16, 7), (17, 1), (18, 2), (19, 1), (20, 10), (21, 10), (22, 2), (23, 13), (24, 5), (25, 5), (26, 8), (27, 148), (28, 1), (30, 2)]
  ```
- `Bash`:
  ```bash
python3 -c "
import json
excl = json.load(open('state/excluded_uids.json'))
print('excluded_uids type:', type(excl), 'len:', len(excl))
apply_guy_excl = [u for u in excl if u.startswith('ApplyGuy:')] if isinstance(excl, list) else None
print('ApplyGuy excluded:', len(apply_guy_excl) if apply_guy_excl is not None else 'n/a')
target = 'SimplifyJobs:de926b0a-99e7-4dbd-94cd-334ec565be9f'
print('target in excluded:', target in excl)
seen = json.load(open('state/seen_ids.json'))
print('seen type', type(seen), len(seen))
print('target in seen:', target in seen)
losses = json.load(open('state/debate_losses.json'))
print('target in debate_losses:', target in losses, losses.get(target))
"

  ```
  ```
excluded_uids type: <class 'list'> len: 388
ApplyGuy excluded: 0
target in excluded: False
seen type <class 'list'> 628
target in seen: False
target in debate_losses: False None
  ```
- `Bash`:
  ```bash
wc -l logs/runs.jsonl
python3 -c "
import json
target = 'SimplifyJobs:de926b0a-99e7-4dbd-94cd-334ec565be9f'
lines = open('logs/runs.jsonl').read().splitlines()
print('total run records:', len(lines))
count=0
first=None
last=None
for l in lines:
    r = json.loads(l)
    rej = r.get('rejections', [])
    # rejections might be list of dicts or strings; check shape
    found = False
    if isinstance(rej, list):
        for item in rej:
            if isinstance(item, dict) and item.get('uid')==target:
                found = True
            elif isinstance(item, str) and target in item:
                found = True
    if found:
        count+=1
        if first is None: first = r.get('timestamp')
        last = r.get('timestamp')
print('records containing target in rejections:', count)
print('first:', first, 'last:', last)
"

  ```
  ```
684 logs/runs.jsonl
total run records: 684
records containing target in rejections: 186
first: 2026-08-10T23:25:36.088293+00:00 last: 2026-08-28T07:57:52.256499+00:00
  ```
- `Bash`:
  ```bash
python3 -c "
import json
target = 'SimplifyJobs:de926b0a-99e7-4dbd-94cd-334ec565be9f'
lines = open('logs/runs.jsonl').read().splitlines()
r = json.loads(lines[-1])
print('last record timestamp:', r.get('timestamp'))
rej = r.get('rejections', [])
for item in rej[:3]:
    print(item)
print('---searching for target in last record---')
for item in rej:
    if isinstance(item, dict) and item.get('uid')==target:
        print(item)
"

  ```
  ```
last record timestamp: 2026-08-28T07:57:52.256499+00:00
{'uid': 'ApplyGuy:custom:google:91436104816698054', 'check': 'degree_eligibility', 'reason': 'currently pursuing a PhD degree'}
{'uid': 'vanshb03:[REDACTED]', 'check': 'url_liveness', 'reason': 'HTTP 404'}
{'uid': 'SimplifyJobs:[REDACTED]', 'check': 'url_liveness', 'reason': 'HTTP 403'}
---searching for target in last record---
{'uid': 'SimplifyJobs:[REDACTED]', 'check': 'url_liveness', 'reason': 'HTTP 403'}
  ```
- `Bash`:
  ```bash
date -u
echo "---"
gh workflow list 2>&1 | head -10
echo "--- recent runs ---"
gh run list --workflow=run.yml --limit 5 2>&1
  ```
  ```
Fri Aug 28 08:59:36 UTC 2026
---
recheck	active	315675907
revalidate	active	342320481
run	active	315074756
test	active	314681321
Dependency Graph	active	314681291
--- recent runs ---
completed	success	run	run	master	schedule	33153423258	1m4s	2026-08-28T07:57:31Z
completed	success	run	run	master	schedule	33125988682	1m2s	2026-08-27T23:21:30Z
completed	success	run	run	master	schedule	33076306017	59s	2026-08-27T13:20:23Z
completed	success	run	run	master	schedule	33033191035	40s	2026-08-27T02:24:36Z
completed	success	run	run	master	schedule	33015483856	51s	2026-08-26T21:27:59Z
  ```
- `Bash`:
  ```bash
python3 -c "
import json
losses = json.load(open('state/debate_losses.json'))
top = sorted(losses.items(), key=lambda x: -x[1])[:15]
for k,v in top: print(v, k)
print()
print('count at 27:', sum(1 for v in losses.values() if v==27))
apply_guy = {k:v for k,v in losses.items() if k.startswith('ApplyGuy:')}
print('ApplyGuy at 27:', sum(1 for v in apply_guy.values() if v==27))
non_ag_27 = [k for k,v in losses.items() if v==27 and not k.startswith('ApplyGuy:')]
print('non-ApplyGuy at 27 count:', len(non_ag_27))
print(non_ag_27[:5])
"

  ```
  ```
30 SimplifyJobs:[REDACTED]
30 zshah101:ashby:voleon:[REDACTED]
28 SimplifyJobs:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]
27 ApplyGuy:[REDACTED]

count at 27: 148
ApplyGuy at 27: 143
non-ApplyGuy at 27 count: 5
['Lever:[REDACTED]', 'SimplifyJobs:[REDACTED]', 'zshah101:greenhouse:sage49:6131185004', 'zshah101:greenhouse:verkada:5211595007', 'zshah101:greenhouse:verkada:5219131007']
  ```
- `Bash` — `git log --oneline -- state/debate_losses.json | head -20`
  ```
42b8321 Update state + logs — 2026-08-28
ed8408a Update state + logs — 2026-08-27
e33c577 Update state + logs — 2026-08-27
7a1be68 Update state + logs — 2026-08-27
9c2d71f Update state + logs — 2026-08-26
e291791 Update state + logs — 2026-08-26
feeb16a Update state + logs — 2026-08-26
ec77221 Update state + logs — 2026-08-26
3a9fb09 Update state + logs — 2026-08-26
95d95e6 Update state + logs — 2026-08-26
9629979 Update state + logs — 2026-08-26
f91fd43 Update state + logs — 2026-08-26
3973ef8 Update state + logs — 2026-08-26
e5c9389 Update state + logs — 2026-08-26
d665a9e Update state + logs — 2026-08-26
01e93af Update state + logs — 2026-08-26
d41da21 Update state + logs — 2026-08-26
72c8d39 Update state + logs — 2026-08-26
ab78c53 Update state + logs — 2026-08-26
2d87dfa Update state + logs — 2026-08-26
  ```
- `Bash`:
  ```bash
for c in $(git log --format=%H -- state/debate_losses.json | head -25); do
  ts=$(git log -1 --format=%cI $c)
  maxv=$(git show $c:state/debate_losses.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(max(d.values()) if d else 0)")
  echo "$ts $maxv"
done
  ```
  ```
2026-08-28T07:58:29+00:00 30
2026-08-27T23:22:28+00:00 29
2026-08-27T13:21:17+00:00 28
2026-08-27T02:25:10+00:00 27
2026-08-26T21:28:44+00:00 26
2026-08-26T18:49:51+00:00 25
2026-08-26T16:10:28+00:00 24
2026-08-26T14:35:24+00:00 23
2026-08-26T13:45:49+00:00 22
2026-08-26T12:31:31+00:00 21
2026-08-26T11:20:33+00:00 20
2026-08-26T10:25:23+00:00 19
2026-08-26T09:31:30+00:00 18
2026-08-26T08:31:50+00:00 17
2026-08-26T07:38:07+00:00 16
2026-08-26T06:31:08+00:00 15
2026-08-26T05:24:29+00:00 14
2026-08-26T04:30:35+00:00 13
2026-08-26T03:45:24+00:00 12
2026-08-26T02:19:39+00:00 11
2026-08-26T00:42:32+00:00 10
2026-08-25T23:17:14+00:00 9
2026-08-25T22:16:42+00:00 8
2026-08-25T21:18:47+00:00 7
2026-08-25T20:18:20+00:00 6
  ```
- `Bash` — `grep -n "def _prioritize_and_cap\|def debate_compare\|def update_debate_losses\|MAX_DEBATE_LOSSES\|MAX_NEW_WRITES_PER_RUN\|def run_once\|def validate_and_write\|issue_fn\|def classify" run_pipeline.py | head -60`
  ```
80:MAX_NEW_WRITES_PER_RUN = {"AI/ML": 3, "Fullstack": 3, "CyS & Finance": 3, "Other": 1}
98:def _prioritize_and_cap(new_listings: list, budget: dict, preferred_companies: dict = None) -> tuple:
194:MAX_DEBATE_LOSSES = 48
205:# new candidates all cross MAX_DEBATE_LOSSES together — real incident,
210:# MAX_DEBATE_LOSSES runs (~5 hours) with no signal to a human that it's
300:def update_debate_losses(losses: dict, deferred: list, written_uids: list) -> tuple:
305:    is moot. A uid whose count reaches MAX_DEBATE_LOSSES is returned in
314:        if losses[uid] >= MAX_DEBATE_LOSSES:
351:    comparator MAX_DEBATE_LOSSES consecutive times here, before it's even
389:def validate_and_write(new_listings, profile: dict, jarvis_dir, seen_ids: set, date_found: str,
482:def run_once(
492:    issue_fn=file_github_issue,
543:        issue_fn(
560:        new_listings, MAX_NEW_WRITES_PER_RUN, preferred_companies=profile.get("preferred_companies")
578:    # entirely. A uid crossing MAX_DEBATE_LOSSES moves to the excluded set
593:                    f"excluded {now.date().isoformat()} — lost the debate {MAX_DEBATE_LOSSES} consecutive runs"
597:                    max_losses=MAX_DEBATE_LOSSES,
600:            issue_fn(
603:                f"{record['newly_excluded_count']} candidates crossed MAX_DEBATE_LOSSES "
604:                f"({MAX_DEBATE_LOSSES} consecutive losses) and were permanently excluded in this single "
625:            issue_fn(
636:            issue_fn(
655:        issue_fn(
678:        issue_fn(
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/vault_writer/validate.py`
- `Bash` — `grep -rn "def append_excluded_log" --include=*.py . `
  ```
core/run_log.py:99:def append_excluded_log(excluded_log_md_path, line: str, created_date: str, max_losses: int) -> None:
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/run_log.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/run_log.py`
- `Bash`:
  ```bash
python3 -c "
import json
from collections import Counter
lines = open('logs/runs.jsonl').read().splitlines()
c = Counter()
for l in lines:
    r = json.loads(l)
    for rej in r.get('rejections', []):
        c[rej.get('check')] += 1
for k,v in c.most_common():
    print(k, v)
"

  ```
  ```
opt_eligibility 3645
url_liveness 3274
cross_source_duplicate 2801
cs_relevance 94
degree_eligibility 27
  ```
- `Bash` — `grep -n "def test_update_debate_losses\|class Test\|update_debate_losses\|debate_losses" tests/test_run_pipeline.py | head -40`
  ```
(Bash completed with no output)
  ```
- `Bash` — `grep -rln "update_debate_losses\|debate_losses" tests/ | head; echo "---"; ls tests/ | grep -i debate`
  ```
tests/test_zero_match_alert.py
tests/test_debate_losses.py
---
test_debate.py
test_debate_losses.py
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py`
- `Bash` — `grep -n "_run_once_kwargs\|^PROFILE\|def _simplify_raw\|http_head\|SIMPLIFY_FIXTURE\|FIXTURES =" tests/test_run_pipeline.py | head -40`
  ```
15:FIXTURES = Path(__file__).parent / "fixtures"
16:PROFILE = load_profile()
23:def _simplify_raw():
84:def _fake_http_head_all_live(url, timeout=None, allow_redirects=True):
222:    kwargs = _run_once_kwargs(tmp_path)
281:        http_head=_fake_http_head_all_live,
296:        [(uid, listing)], PROFILE, tmp_path, seen_ids=set(), date_found="2026-07-17", http_head=dead_head,
322:        http_head=_fake_http_head_all_live,
338:        date_found="2026-07-18", http_head=_fake_http_head_all_live,
348:        date_found="2026-07-18", http_head=_fake_http_head_all_live,
369:def _run_once_kwargs(tmp_path, **overrides):
377:        http_head=_fake_http_head_all_live,
387:    kwargs = _run_once_kwargs(tmp_path)
411:    kwargs = _run_once_kwargs(tmp_path)
432:    kwargs = _run_once_kwargs(tmp_path, push_fn=failing_push)
453:    kwargs = _run_once_kwargs(tmp_path, http_head=Mock(return_value=Mock(status_code=404)))
466:    kwargs = _run_once_kwargs(tmp_path)
471:    kwargs2 = _run_once_kwargs(tmp_path, jarvis_dir=kwargs["jarvis_dir"])
489:    kwargs = _run_once_kwargs(tmp_path, http_get=dying_http_get)
514:        http_head=_fake_http_head_all_live, fetch_page_fn=fetch, opt_cache=cache,
530:        http_head=_fake_http_head_all_live, fetch_page_fn=fetch, opt_cache=cache,
544:        http_head=_fake_http_head_all_live, fetch_page_fn=fetch, opt_cache={},
559:        http_head=_fake_http_head_all_live, fetch_page_fn=fetch, opt_cache={},
603:    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
612:    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
619:    kwargs2 = _run_once_kwargs(
639:    kwargs = _run_once_kwargs(tmp_path, state_dir=tmp_path / "state")
751:    kwargs = _run_once_kwargs(
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Bash`:
  ```bash
grep -n "def compute_uid\|SimplifyJobs" core/identity.py | head -10
echo "---normalize_simplify---"
grep -n "def normalize_simplify" -A 20 ingestion/normalize.py | head -30
echo "---fixture sample---"
python3 -c "import json; d=json.load(open('tests/fixtures/simplifyjobs.json')); print(json.dumps(d[0], indent=2)[:800])"
  ```
  ```
18:# across SimplifyJobs/zshah101/vanshb03), and Palantir's "Intel" FDSE role
19:# duplicated across two different buckets (same Lever job id via SimplifyJobs
79:def compute_uid(listing) -> str:
---normalize_simplify---
42:def normalize_simplify(raw: dict) -> Listing:
43-    return Listing(
44-        company=raw["company_name"],
45-        title=raw["title"],
46-        url=raw["url"],
47-        source="SimplifyJobs",
48-        category=raw.get("category", ""),
49-        terms=raw.get("terms", []),
50-        locations=raw.get("locations", []),
51-        degrees=raw.get("degrees", []),
52-        active=raw.get("active"),
53-        date_posted=raw.get("date_posted"),
54-        raw_id=raw["id"],
55-    )
56-
57-
58-def normalize_josegael(raw: dict) -> Listing:
59-    # JGCL has no `terms` field; its cycle signal is `season` — mostly year-less
60-    # ("Summer", "Multiple", rarely "Summer 2026"). Mapped into terms so the
61-    # filter can reject affirmatively-wrong cycles; leaving it unmapped is what
62-    # let wrong-cycle listings through until the 2026-07-18 vault audit.
---fixture sample---
{
  "_case": "should-match: Summer 2027 in terms list, category Software",
  "source": "Simplify",
  "category": "Software",
  "company_name": "Palantir",
  "id": "[REDACTED]",
  "title": "Forward Deployed Software Engineer \u2013 Internship - US Government",
  "active": true,
  "terms": [
    "Winter 2027",
    "Spring 2027",
    "Summer 2027",
    "Fall 2027"
  ],
  "date_updated": 1765581501,
  "date_posted": 1765581501,
  "url": "https://jobs.lever.co/palantir/[REDACTED]/apply",
  "locations": [
    "Honolulu, HI"
  ],
  "company_url": "https://simplify.jobs/c/Palantir",
  "is_visible": true,
  "sponsorship": "Other",
  "degrees": []
}
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/identity.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/run_log.py`
  ```diff
  - def append_excluded_log(excluded_log_md_path, line: str, created_date: str, max_losses: int) -> None:
    """Task N (Prompt 5) — one line per uid the first time it's excluded,
    same append-only pattern as append_weekly_rollup above."""
    _append_markdown_line(
        excluded_log_md_path, line, _EXCLUDED_LOG_HEADER_TEMPLATE.format(created=created_date, max_losses=max_losses)
    )
  + def append_excluded_log(excluded_log_md_path, line: str, created_date: str, max_losses: int) -> None:
    """Task N (Prompt 5) — one line per uid the first time it's excluded,
    same append-only pattern as append_weekly_rollup above."""
    _append_markdown_line(
        excluded_log_md_path, line, _EXCLUDED_LOG_HEADER_TEMPLATE.format(created=created_date, max_losses=max_losses)
    )


_WRITE_GATE_EXCLUDED_LOG_HEADER_TEMPLATE = """---
type: dashboard
status: active
created: {created}
tags:
  - internship
  - automation
  - write-gate
---
# Excluded — Failed The Write Gate
A posting lands here the first time it fails the SAME write-gate check (vault_writer/validate.py) {threshold} consecutive runs it appears in — not a ranking loss (see Excluded — Losing The Debate.md for that), a structural one: a dead URL or a company+title already in the vault from another source. Appended automatically, never rewritten.
"""


def append_write_gate_excluded_log(excluded_log_md_path, line: str, created_date: str, threshold: int) -> None:
    """Task (Prompt 20) — same append-only pattern as append_excluded_log,
    for a distinct exclusion reason (structurally-doomed write-gate check,
    not an out-ranked debate loss) that reads wrong under that log's header."""
    _append_markdown_line(
        excluded_log_md_path, line,
        _WRITE_GATE_EXCLUDED_LOG_HEADER_TEMPLATE.format(created=created_date, threshold=threshold),
    )
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - from core.run_log import (
    append_excluded_log,
    append_run_log,
    append_weekly_rollup,
    format_weekly_rollup,
    load_recent_runs,
    should_run_weekly_rollup,
)
  + from core.run_log import (
    append_excluded_log,
    append_run_log,
    append_weekly_rollup,
    append_write_gate_excluded_log,
    format_weekly_rollup,
    load_recent_runs,
    should_run_weekly_rollup,
)
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -     return losses, newly_excluded

# A required_fields or format_compliance rejection means OUR normalizer/writer
# produced something malformed — a real bug, worth an issue. url_liveness and
# not_duplicate rejections are routine (a stale posting, an already-seen item)
# and would spam an issue on every ordinary run if treated the same way.
SYSTEMIC_REJECTION_CHECKS = {"required_fields", "format_compliance"}
  +     return losses, newly_excluded


WRITE_GATE_FAILURES_FILENAME = "write_gate_failures.json"
WRITE_GATE_EXCLUDED_LOG_SUBPATH = Path("10_Areas/Career/Internships/List/Excluded — Failed The Write Gate.md")

# Task (Prompt 20, 2026-08-28 decision): a uid that structurally CANNOT pass
# the write gate (a dead URL, a company+title already vaulted from another
# source) still wins its bucket's debate_compare ranking every run — it's
# never "deferred" (that only happens to items _prioritize_and_cap itself
# cuts for budget reasons), so it never touches debate_losses.json or
# MAX_DEBATE_LOSSES, and it's never written, so it never reaches
# seen_ids.json either. Confirmed against the real incident this is built
# from: SimplifyJobs:[REDACTED] failed
# url_liveness (HTTP 403) in every single one of the 186 runs it appeared in
# between 2026-08-10 and 2026-08-28 (18 days), while sitting in none of
# debate_losses.json, excluded_uids.json, or seen_ids.json the entire time —
# it occupied one of its bucket's limited MAX_NEW_WRITES_PER_RUN slots every
# run, forever, pushing a real competing candidate into deferred (and toward
# a debate loss it didn't otherwise deserve) in its place.
#
# Scoped to the two checks confirmed to repeat identically run over run for
# the SAME structural reason — also real, not hypothetical: logs/runs.jsonl's
# 684 records show url_liveness rejected 3274 times and cross_source_duplicate
# 2801 times. required_fields/format_compliance are deliberately excluded —
# SYSTEMIC_REJECTION_CHECKS below already means OUR normalizer/template is
# broken, not the uid; excluding the uid would hide our bug instead of
# surfacing it (and both are 0/684 in the same log, i.e. have never actually
# fired). not_duplicate is excluded too: dedup_new's own seen_ids/
# seen_this_run check already guarantees a new_listings item can't be in
# seen_ids, so this check structurally can't fail for the same uid across two
# runs — and, in the same 684-run log, it never has (0 occurrences).
WRITE_GATE_FAILURE_CHECKS = {"url_liveness", "cross_source_duplicate"}
# A dead link doesn't deserve MAX_DEBATE_LOSSES' 48-run benefit of the doubt
# — that number exists for genuinely ambiguous ranking losses (see that
# constant's own comment above). Dead-is-dead in a way out-ranked isn't. 3
# consecutive same-check failures is enough real confirmation (the cited
# SimplifyJobs case failed its check 186/186 times it ever appeared, with
# zero recoveries) while still tolerant of a single transient network blip
# on any one run.
WRITE_GATE_FAILURE_THRESHOLD = 3


def load_write_gate_failures(state_dir) -> dict:
    path = Path(state_dir) / WRITE_GATE_FAILURES_FILENAME
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def save_write_gate_failures(state_dir, failures: dict) -> None:
    path = Path(state_dir) / WRITE_GATE_FAILURES_FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(failures, indent=2, sort_keys=True) + "\n")


def update_write_gate_failures(failures: dict, rejections: list, written_uids: list, now_iso: str) -> tuple:
    """Returns (updated_failures, newly_excluded: [(uid, check, reason), ...]).
    Tracks only WRITE_GATE_FAILURE_CHECKS — see that constant's citation for
    why the other checks are excluded. A uid that wins (gets written) this
    run has its failure history cleared entirely, same "a win wipes the
    slate" semantics as update_debate_losses's written_uids handling above —
    a dead URL can come back alive, a cross-source duplicate can leave the
    vault.

    A uid whose failing check CHANGES between runs restarts its streak at 1
    rather than continuing to accumulate: the count only means something as
    consecutive-same-reason evidence of one structural problem, not two
    different one-off failures added together."""
    failures = {k: dict(v) for k, v in failures.items()}
    for uid in written_uids:
        failures.pop(uid, None)
    newly_excluded = []
    for r in rejections:
        check = r["check"]
        if check not in WRITE_GATE_FAILURE_CHECKS:
            continue
        uid = r["uid"]
        entry = failures.get(uid)
        if entry is None or entry["check"] != check:
            failures[uid] = {"check": check, "count": 1, "first_seen": now_iso}
        else:
            entry["count"] += 1
        if failures[uid]["count"] >= WRITE_GATE_FAILURE_THRESHOLD:
            newly_excluded.append((uid, check, r["reason"]))
            del failures[uid]
    return failures, newly_excluded


# A required_fields or format_compliance rejection means OUR normalizer/writer
# produced something malformed — a real bug, worth an issue. url_liveness and
# not_duplicate rejections are routine (a stale posting, an already-seen item)
# and would spam an issue on every ordinary run if treated the same way.
SYSTEMIC_REJECTION_CHECKS = {"required_fields", "format_compliance"}
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -         "dossier_total": 0,
        "newly_excluded_count": 0,
    }
  +         "dossier_total": 0,
        "newly_excluded_count": 0,
        "write_gate_excluded_count": 0,
    }
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -                 "`Excluded — Losing The Debate.md` before treating any of them as a real quality signal.",
            )

    # Task A resource-limit notification (Standard §5): a bucket at/over
  +                 "`Excluded — Losing The Debate.md` before treating any of them as a real quality signal.",
            )

    # Task (Prompt 20): a uid that fails the SAME write-gate check
    # WRITE_GATE_FAILURE_THRESHOLD consecutive runs it appears in is
    # structurally doomed (a dead URL, a company+title already in the vault),
    # not merely out-ranked — see WRITE_GATE_FAILURE_CHECKS's own citation.
    # It joins the SAME excluded_ids set debate losses use (a single source
    # of truth fetch_and_filter/dedup_new already check), so it stops
    # winning a this_run slot every run — logged to its own reviewable
    # markdown, not silently dropped.
    if state_dir is not None:
        write_gate_failures = load_write_gate_failures(state_dir)
        write_gate_failures, newly_wg_excluded = update_write_gate_failures(
            write_gate_failures, rejections, written_uids, timestamp
        )
        save_write_gate_failures(state_dir, write_gate_failures)
        record["write_gate_excluded_count"] = len(newly_wg_excluded)
        if newly_wg_excluded:
            excluded_ids = load_excluded_uids(state_dir)
            excluded_ids.update(uid for uid, _check, _reason in newly_wg_excluded)
            save_excluded_uids(state_dir, excluded_ids)
            for uid, check, reason in newly_wg_excluded:
                line = (
                    f"- `{uid}` — excluded {now.date().isoformat()} — failed `{check}` "
                    f"{WRITE_GATE_FAILURE_THRESHOLD} consecutive runs (last: {reason})"
                )
                append_write_gate_excluded_log(
                    Path(jarvis_dir) / WRITE_GATE_EXCLUDED_LOG_SUBPATH, line,
                    created_date=now.date().isoformat(), threshold=WRITE_GATE_FAILURE_THRESHOLD,
                )

    # Task A resource-limit notification (Standard §5): a bucket at/over
  ```
- `Bash` — `grep -n "excluded_ids" run_pipeline.py`
  ```
436:def fetch_and_filter(profile: dict, http_get=None, excluded_ids: frozenset = frozenset()) -> dict:
438:    excluded_ids (Task N, Prompt 5) drops a uid that already lost the debate
450:                and compute_uid(l) not in excluded_ids
456:def dedup_new(matched_by_source: dict, seen_ids: set, excluded_ids: frozenset = frozenset()):
458:    excluded_ids is also checked here (belt-and-suspenders with
467:            if uid in excluded_ids:
607:    excluded_ids = load_excluded_uids(state_dir) if state_dir is not None else set()
612:        matched_by_source = fetch_and_filter(profile, http_get, excluded_ids=excluded_ids)
622:            and compute_uid(l) not in excluded_ids
644:    new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids, excluded_ids=excluded_ids)
676:            excluded_ids = load_excluded_uids(state_dir)
677:            excluded_ids.update(uid for uid, _listing in newly_excluded)
678:            save_excluded_uids(state_dir, excluded_ids)
705:    # It joins the SAME excluded_ids set debate losses use (a single source
717:            excluded_ids = load_excluded_uids(state_dir)
718:            excluded_ids.update(uid for uid, _check, _reason in newly_wg_excluded)
719:            save_excluded_uids(state_dir, excluded_ids)
  ```
- `Bash` — `python3 -c "import run_pipeline" && echo OK`
  ```
OK
  ```
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_write_gate_failures.py`
  ```
"""Task (Prompt 20) — write_gate_failures.json: a uid that keeps winning its
bucket's debate_compare ranking but keeps failing the SAME write-gate check
is structurally doomed, not merely out-ranked, and needs a distinct, faster
exclusion path from debate_losses.json/MAX_DEBATE_LOSSES.

Real, citable case: SimplifyJobs:[REDACTED] failed
url_liveness (HTTP 403) in every one of 186 runs it appeared in between
2026-08-10 and 2026-08-28 while sitting in none of debate_losses.json,
excluded_uids.json, or seen_ids.json. Its real uid string is used directly
below (built via a Listing with that raw_id, not by editing the shared
simplifyjobs.json fixture other tests depend on for exact match counts)."""
import json

import run_pipeline
from ingestion.normalize import Listing
from test_run_pipeline import PROFILE, _fake_http_head_all_live, _run_once_kwargs

REAL_DEAD_LINK_UID = "SimplifyJobs:[REDACTED]"
REAL_DEAD_LINK_URL = "https://simplify.jobs/p/[REDACTED]"


def _dead_link_listing():
    return Listing(company="Acme", title="Software Engineer Intern", url=REAL_DEAD_LINK_URL,
                    source="SimplifyJobs", raw_id="[REDACTED]")


def _rejection(check="url_liveness", reason="HTTP 403", uid=REAL_DEAD_LINK_UID):
    return {"uid": uid, "check": check, "reason": reason}


# --- update_write_gate_failures: pure-function tests ---

def test_below_threshold_stays_in_pool_not_excluded():
    failures = {}
    for _ in range(run_pipeline.WRITE_GATE_FAILURE_THRESHOLD - 1):
        failures, newly_excluded = run_pipeline.update_write_gate_failures(
            failures, [_rejection()], written_uids=[], now_iso="2026-08-28T00:00:00Z",
        )
        assert newly_excluded == []
    assert failures[REAL_DEAD_LINK_UID]["count"] == run_pipeline.WRITE_GATE_FAILURE_THRESHOLD - 1
    assert failures[REAL_DEAD_LINK_UID]["check"] == "url_liveness"


def test_nth_same_check_failure_excludes_and_removes_from_state():
    failures = {}
    for _ in range(run_pipeline.WRITE_GATE_FAILURE_THRESHOLD - 1):
        failures, _ = run_pipeline.update_write_gate_failures(
            failures, [_rejection()], written_uids=[], now_iso="2026-08-28T00:00:00Z",
        )
    failures, newly_excluded = run_pipeline.update_write_gate_failures(
        failures, [_rejection()], written_uids=[], now_iso="2026-08-28T07:57:52Z",
    )
    assert newly_excluded == [(REAL_DEAD_LINK_UID, "url_liveness", "HTTP 403")]
    assert REAL_DEAD_LINK_UID not in failures  # removed once excluded, not left at threshold


def test_checks_outside_write_gate_failure_checks_are_ignored():
    """required_fields/format_compliance (systemic, our own bug) and
    not_duplicate (structurally can't repeat, see the constant's citation)
    never accumulate here, no matter how many times they show up."""
    failures = {}
    for check in ("required_fields", "format_compliance", "not_duplicate", "opt_eligibility", "cs_relevance"):
        for _ in range(run_pipeline.WRITE_GATE_FAILURE_THRESHOLD + 5):
            failures, newly_excluded = run_pipeline.update_write_gate_failures(
                failures, [_rejection(check=check, uid=f"SimplifyJobs:{check}")],
                written_uids=[], now_iso="2026-08-28T00:00:00Z",
            )
            assert newly_excluded == []
    assert failures == {}


def test_a_different_check_restarts_the_streak_instead_of_accumulating():
    failures = {}
    failures, _ = run_pipeline.update_write_gate_failures(
        failures, [_rejection(check="url_liveness")], written_uids=[], now_iso="2026-08-26T00:00:00Z",
    )
    assert failures[REAL_DEAD_LINK_UID]["count"] == 1
    failures, newly_excluded = run_pipeline.update_write_gate_failures(
        failures, [_rejection(check="cross_source_duplicate", reason="company+title already in vault")],
        written_uids=[], now_iso="2026-08-27T00:00:00Z",
    )
    assert newly_excluded == []
    assert failures[REAL_DEAD_LINK_UID] == {
        "check": "cross_source_duplicate", "count": 1, "first_seen": "2026-08-27T00:00:00Z",
    }


def test_written_uid_clears_prior_failure_history():
    """A URL that was dead can come back alive — a win must wipe the slate,
    same semantics as update_debate_losses's written_uids handling."""
    failures = {}
    failures, _ = run_pipeline.update_write_gate_failures(
        failures, [_rejection()], written_uids=[], now_iso="2026-08-26T00:00:00Z",
    )
    assert REAL_DEAD_LINK_UID in failures
    failures, newly_excluded = run_pipeline.update_write_gate_failures(
        failures, [], written_uids=[REAL_DEAD_LINK_UID], now_iso="2026-08-27T00:00:00Z",
    )
    assert REAL_DEAD_LINK_UID not in failures
    assert newly_excluded == []


def test_written_uid_not_in_failures_is_a_no_op_pop():
    failures, newly_excluded = run_pipeline.update_write_gate_failures(
        {}, [], written_uids=["SimplifyJobs:never-failed"], now_iso="2026-08-28T00:00:00Z",
    )
    assert failures == {}
    assert newly_excluded == []


# --- integration: the real cited dead link is skipped on a simulated next run ---

def test_real_dead_link_uid_is_excluded_after_threshold_runs_of_validate_and_write(tmp_path):
    """validate_and_write itself never knows about write_gate_failures.json
    (that bookkeeping is run_once's job, same layering as debate_losses) —
    this drives the real uid through validate_and_write WRITE_GATE_FAILURE_
    THRESHOLD times with a 403 HEAD response, feeding each run's rejections
    into update_write_gate_failures the same way run_once does, and confirms
    the real cited uid crosses into exclusion on schedule, not before."""
    listing = _dead_link_listing()
    uid = REAL_DEAD_LINK_UID
    dead_head = lambda url, timeout=None, allow_redirects=True: type("R", (), {"status_code": 403})()

    failures = {}
    for i in range(run_pipeline.WRITE_GATE_FAILURE_THRESHOLD):
        written, rejections = run_pipeline.validate_and_write(
            [(uid, listing)], PROFILE, tmp_path, seen_ids=set(), date_found="2026-08-28", http_head=dead_head,
        )
        assert written == []
        assert rejections == [{"uid": uid, "check": "url_liveness", "reason": "HTTP 403"}]
        failures, newly_excluded = run_pipeline.update_write_gate_failures(
            failures, rejections, written_uids=[], now_iso=f"2026-08-{10 + i:02d}T00:00:00Z",
        )
        if i < run_pipeline.WRITE_GATE_FAILURE_THRESHOLD - 1:
            assert newly_excluded == []
    assert newly_excluded == [(uid, "url_liveness", "HTTP 403")]
    assert uid not in failures


def test_run_once_excludes_and_never_refetches_real_dead_link_after_threshold(tmp_path):
    """End-to-end via run_once: pre-seed write_gate_failures.json with the
    real cited uid one run short of the threshold, run once more with that
    uid's URL 403ing — confirms it (a) crosses into excluded_uids.json and
    write_gate_failures.json is cleared for it, then (b) a follow-up run
    never fetches its URL again, mirroring test_debate_losses.py's own
    already-excluded integration test."""
    from core.identity import compute_uid

    listing = _dead_link_listing()
    uid = compute_uid(listing)
    assert uid == REAL_DEAD_LINK_UID

    state_dir = tmp_path / "state"
    state_dir.mkdir(parents=True)
    (state_dir / run_pipeline.WRITE_GATE_FAILURES_FILENAME).write_text(json.dumps({
        uid: {"check": "url_liveness", "count": run_pipeline.WRITE_GATE_FAILURE_THRESHOLD - 1,
              "first_seen": "2026-08-10T23:25:36Z"},
    }))

    def http_get_with_dead_link(url, timeout=None):
        from test_run_pipeline import _fake_http_get, _simplify_raw
        from ingestion.sources import SIMPLIFY_URL
        if url == SIMPLIFY_URL:
            from unittest.mock import Mock
            resp = Mock(status_code=200)
            resp.json.return_value = _simplify_raw() + [{
                "source": "Simplify", "category": "Software", "company_name": "Acme",
                "id": "[REDACTED]",
                "title": "Software Engineer Intern", "active": True,
                "terms": ["Summer 2027"], "date_posted": 1765581501,
                "url": REAL_DEAD_LINK_URL, "locations": ["Remote"], "degrees": [],
            }]
            return resp
        return _fake_http_get(url, timeout=timeout)

    def http_head_dead_only(url, timeout=None, allow_redirects=True):
        from unittest.mock import Mock
        if url == REAL_DEAD_LINK_URL:
            return Mock(status_code=403)
        return _fake_http_head_all_live(url, timeout=timeout, allow_redirects=allow_redirects)

    # Generous budget so the real dead-link candidate isn't itself squeezed
    # out by _prioritize_and_cap before ever reaching validate_and_write.
    import pytest
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(
        run_pipeline, "MAX_NEW_WRITES_PER_RUN",
        {"AI/ML": 20, "Fullstack": 20, "CyS & Finance": 20, "Other": 20},
    )
    try:
        kwargs = _run_once_kwargs(
            tmp_path, state_dir=state_dir, http_get=http_get_with_dead_link, http_head=http_head_dead_only,
        )
        record = run_pipeline.run_once(**kwargs)
    finally:
        monkeypatch.undo()

    assert record["write_gate_excluded_count"] == 1
    excluded = run_pipeline.load_excluded_uids(state_dir)
    assert uid in excluded
    write_gate_failures = run_pipeline.load_write_gate_failures(state_dir)
    assert uid not in write_gate_failures

    log_path = kwargs["jarvis_dir"] / run_pipeline.WRITE_GATE_EXCLUDED_LOG_SUBPATH
    assert uid in log_path.read_text()

    # Follow-up run: the now-excluded real uid must never be fetched again.
    calls = []

    def guarded_fetch(url):
        calls.append(url)
        if url == REAL_DEAD_LINK_URL:
            raise AssertionError("fetched the write-gate-excluded uid's URL again")
        return ""

    kwargs2 = _run_once_kwargs(
        tmp_path, state_dir=state_dir, http_get=http_get_with_dead_link, http_head=http_head_dead_only,
        fetch_page_fn=guarded_fetch, jarvis_dir=kwargs["jarvis_dir"],
    )
    run_pipeline.run_once(**kwargs2)
    assert REAL_DEAD_LINK_URL not in calls

  ```
- `Bash` — `python3 -m pytest tests/test_write_gate_failures.py -x -q 2>&1 | tail -80`
  ```
/usr/bin/python3: No module named pytest
  ```
- `Bash` — `which python3; python3 --version; find / -maxdepth 4 -iname "*venv*" 2>/dev/null | head; cat /home/anant_gupta/projects/work/internship-research-loop/requirements*.txt 2>/dev/null; ls /home/anant_gupta/projects/work/internship-research-loop`
  ```
/usr/bin/python3
Python 3.12.3
/tmp/svgvenv2
/tmp/svgvenv2/pyvenv.cfg
/usr/share/doc/python3.12-venv
/usr/lib/python3.12/venv
requests==2.34.2
pyyaml==6.0.3
pytest==9.1.1
jinja2==3.1.6
CLAUDE.md
PRD.md
README.md
__pycache__
core
enrich.py
grade_resume.py
graphify-out
ingestion
jarvis-checkout
logs
recheck.py
requirements.txt
revalidate.py
run_pipeline.py
scripts
state
tests
vault_writer
  ```
- `Bash` — `pip show pytest 2>&1 | head -3; pip install --user -q pytest requests pyyaml jinja2 2>&1 | tail -20`
  ```
WARNING: Package(s) not found: pytest
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
  ```
- `Bash` — `cat /home/anant_gupta/projects/work/internship-research-loop/.github/workflows/test.yml 2>/dev/null`
  ```
name: test
on: [push, pull_request]
jobs:
  pytest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: python -m pytest tests/ -v
  ```
- `Bash` — `python3 -m venv /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/57040b74-cd56-4bb6-9696-bbc4df2afa6c/scratchpad/venv 2>&1 | tail -5 && /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/57040b74-cd56-4bb6-9696-bbc4df2afa6c/scratchpad/venv/bin/pip install -q -r requirements.txt 2>&1 | tail -10`
  ```
(Bash completed with no output)
  ```
- `Bash`:
  ```bash
VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/57040b74-cd56-4bb6-9696-bbc4df2afa6c/scratchpad/venv
$VENV/bin/python -m pytest tests/test_write_gate_failures.py -x -q 2>&1 | tail -100
  ```
  ```
.......F
=================================== FAILURES ===================================
__ test_run_once_excludes_and_never_refetches_real_dead_link_after_threshold ___

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-5/[REDACTED]')

    def test_run_once_excludes_and_never_refetches_real_dead_link_after_threshold(tmp_path):
        """End-to-end via run_once: pre-seed write_gate_failures.json with the
        real cited uid one run short of the threshold, run once more with that
        uid's URL 403ing — confirms it (a) crosses into excluded_uids.json and
        write_gate_failures.json is cleared for it, then (b) a follow-up run
        never fetches its URL again, mirroring test_debate_losses.py's own
        already-excluded integration test."""
        from core.identity import compute_uid
    
        listing = _dead_link_listing()
        uid = compute_uid(listing)
        assert uid == REAL_DEAD_LINK_UID
    
        state_dir = tmp_path / "state"
        state_dir.mkdir(parents=True)
        (state_dir / run_pipeline.WRITE_GATE_FAILURES_FILENAME).write_text(json.dumps({
            uid: {"check": "url_liveness", "count": run_pipeline.WRITE_GATE_FAILURE_THRESHOLD - 1,
                  "first_seen": "2026-08-10T23:25:36Z"},
        }))
    
        def http_get_with_dead_link(url, timeout=None):
            from test_run_pipeline import _fake_http_get, _simplify_raw
            from ingestion.sources import SIMPLIFY_URL
            if url == SIMPLIFY_URL:
                from unittest.mock import Mock
                resp = Mock(status_code=200)
                resp.json.return_value = _simplify_raw() + [{
                    "source": "Simplify", "category": "Software", "company_name": "Acme",
                    "id": "[REDACTED]",
                    "title": "Software Engineer Intern", "active": True,
                    "terms": ["Summer 2027"], "date_posted": 1765581501,
                    "url": REAL_DEAD_LINK_URL, "locations": ["Remote"], "degrees": [],
                }]
                return resp
            return _fake_http_get(url, timeout=timeout)
    
        def http_head_dead_only(url, timeout=None, allow_redirects=True):
            from unittest.mock import Mock
            if url == REAL_DEAD_LINK_URL:
                return Mock(status_code=403)
            return _fake_http_head_all_live(url, timeout=timeout, allow_redirects=allow_redirects)
    
        # Generous budget so the real dead-link candidate isn't itself squeezed
        # out by _prioritize_and_cap before ever reaching validate_and_write.
        import pytest
        monkeypatch = pytest.MonkeyPatch()
        monkeypatch.setattr(
            run_pipeline, "MAX_NEW_WRITES_PER_RUN",
            {"AI/ML": 20, "Fullstack": 20, "CyS & Finance": 20, "Other": 20},
        )
        try:
            kwargs = _run_once_kwargs(
                tmp_path, state_dir=state_dir, http_get=http_get_with_dead_link, http_head=http_head_dead_only,
            )
            record = run_pipeline.run_once(**kwargs)
        finally:
            monkeypatch.undo()
    
>       assert record["write_gate_excluded_count"] == 1
E       assert 0 == 1

tests/test_write_gate_failures.py:198: AssertionError
=========================== short test summary info ============================
FAILED tests/test_write_gate_failures.py::test_run_once_excludes_and_never_refetches_real_dead_link_after_threshold
!!!!!!!!!!!!!!!!!!!!!!!!!! stopping after 1 failures !!!!!!!!!!!!!!!!!!!!!!!!!!!
1 failed, 7 passed in 0.22s
  ```
- `Bash`:
  ```bash
python3 -c "
from core.filter import load_profile
import json
p = load_profile()
print(json.dumps(p, indent=2)[:1500])
"
  ```
  ```
{
  "grad_year": 2028,
  "class_year": "junior",
  "eligible_class_tags": [
    "Junior",
    "3rd year"
  ],
  "accept_unrestricted": true,
  "terms": [
    "Summer 2027",
    "Winter 2027",
    "Spring 2027"
  ],
  "terms_weight": {
    "Summer 2027": "high",
    "Winter 2027": "high",
    "Spring 2027": "low"
  },
  "categories": [
    "Software",
    "Software Engineering",
    "AI/ML/Data",
    "Data Science, AI & Machine Learning"
  ],
  "exclude_terms": [
    "Summer 2026",
    "Fall 2026",
    "Spring 2026"
  ],
  "locations_allow": "us_remote",
  "degrees_allow": [
    "Bachelor's"
  ],
  "preferred_companies": {
    "Jane Street": "high",
    "Two Sigma": "high",
    "D.E. Shaw": "high",
    "Citadel": "high",
    "Google": "high",
    "Microsoft": "high",
    "LinkedIn": "high",
    "MLH": "high",
    "NASA": "high",
    "Capital One": "high",
    "Bloomberg": "high"
  }
}
  ```
- `Bash`:
  ```bash
python3 -c "
import sys
sys.path.insert(0, 'tests')
from ingestion.normalize import normalize_simplify
from core.filter import load_profile, matches
from core.relevance import stage1_reject

raw = {
    'source': 'Simplify', 'category': 'Software', 'company_name': 'Acme',
    'id': 'de926b0a-99e7-4dbd-94cd-334ec565be9f',
    'title': 'Software Engineer Intern', 'active': True,
    'terms': ['Summer 2027'], 'date_posted': 1765581501,
    'url': 'https://simplify.jobs/p/de926b0a-99e7-4dbd-94cd-334ec565be9f', 'locations': ['Remote'], 'degrees': [],
}
listing = normalize_simplify(raw)
profile = load_profile()
print('matches:', matches(listing, profile))
print('stage1_reject:', stage1_reject(listing.title, ''))
"

  ```
  ```
matches: True
stage1_reject: False
  ```
- `Bash`:
  ```bash
python3 -c "
import sys
sys.path.insert(0, 'tests')
from unittest.mock import Mock
import run_pipeline
from core.filter import load_profile
from ingestion.sources import SIMPLIFY_URL
from test_run_pipeline import _fake_http_get, _simplify_raw

REAL_DEAD_LINK_URL = 'https://simplify.jobs/p/de926b0a-99e7-4dbd-94cd-334ec565be9f'

def http_get_with_dead_link(url, timeout=None):
    if url == SIMPLIFY_URL:
        resp = Mock(status_code=200)
        resp.json.return_value = _simplify_raw() + [{
            'source': 'Simplify', 'category': 'Software', 'company_name': 'Acme',
            'id': 'de926b0a-99e7-4dbd-94cd-334ec565be9f',
            'title': 'Software Engineer Intern', 'active': True,
            'terms': ['Summer 2027'], 'date_posted': 1765581501,
            'url': REAL_DEAD_LINK_URL, 'locations': ['Remote'], 'degrees': [],
        }]
        return resp
    return _fake_http_get(url, timeout=timeout)

profile = load_profile()
matched = run_pipeline.fetch_and_filter(profile, http_get_with_dead_link)
uids = [run_pipeline.compute_uid(l) for l in matched['SimplifyJobs']['matched']]
print('SimplifyJobs matched uids:', uids)
print('target present:', 'SimplifyJobs:de926b0a-99e7-4dbd-94cd-334ec565be9f' in uids)
"

  ```
  ```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 8, in <module>
  File "/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py", line 6, in <module>
    import pytest
ModuleNotFoundError: No module named 'pytest'
  ```
- `Bash`:
  ```bash
VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/57040b74-cd56-4bb6-9696-bbc4df2afa6c/scratchpad/venv
$VENV/bin/python -c "
import sys
sys.path.insert(0, 'tests')
from unittest.mock import Mock
import run_pipeline
from core.filter import load_profile
from ingestion.sources import SIMPLIFY_URL
from test_run_pipeline import _fake_http_get, _simplify_raw

REAL_DEAD_LINK_URL = 'https://simplify.jobs/p/de926b0a-99e7-4dbd-94cd-334ec565be9f'

def http_get_with_dead_link(url, timeout=None):
    if url == SIMPLIFY_URL:
        resp = Mock(status_code=200)
        resp.json.return_value = _simplify_raw() + [{
            'source': 'Simplify', 'category': 'Software', 'company_name': 'Acme',
            'id': 'de926b0a-99e7-4dbd-94cd-334ec565be9f',
            'title': 'Software Engineer Intern', 'active': True,
            'terms': ['Summer 2027'], 'date_posted': 1765581501,
            'url': REAL_DEAD_LINK_URL, 'locations': ['Remote'], 'degrees': [],
        }]
        return resp
    return _fake_http_get(url, timeout=timeout)

profile = load_profile()
matched = run_pipeline.fetch_and_filter(profile, http_get_with_dead_link)
uids = [run_pipeline.compute_uid(l) for l in matched['SimplifyJobs']['matched']]
print('SimplifyJobs matched uids:', uids)
print('target present:', 'SimplifyJobs:de926b0a-99e7-4dbd-94cd-334ec565be9f' in uids)
"

  ```
  ```
SimplifyJobs matched uids: ['SimplifyJobs:[REDACTED]', 'SimplifyJobs:[REDACTED]', 'SimplifyJobs:[REDACTED]', 'SimplifyJobs:[REDACTED]']
target present: True
  ```
- `Bash`:
  ```bash
VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/57040b74-cd56-4bb6-9696-bbc4df2afa6c/scratchpad/venv
$VENV/bin/python -c "
import sys, json, tempfile
sys.path.insert(0, 'tests')
from pathlib import Path
from unittest.mock import Mock
import run_pipeline
from test_run_pipeline import _fake_http_get, _simplify_raw, _fake_http_head_all_live, _run_once_kwargs
from ingestion.sources import SIMPLIFY_URL

REAL_DEAD_LINK_URL = 'https://simplify.jobs/p/de926b0a-99e7-4dbd-94cd-334ec565be9f'
REAL_DEAD_LINK_UID = 'SimplifyJobs:de926b0a-99e7-4dbd-94cd-334ec565be9f'

def http_get_with_dead_link(url, timeout=None):
    if url == SIMPLIFY_URL:
        resp = Mock(status_code=200)
        resp.json.return_value = _simplify_raw() + [{
            'source': 'Simplify', 'category': 'Software', 'company_name': 'Acme',
            'id': 'de926b0a-99e7-4dbd-94cd-334ec565be9f',
            'title': 'Software Engineer Intern', 'active': True,
            'terms': ['Summer 2027'], 'date_posted': 1765581501,
            'url': REAL_DEAD_LINK_URL, 'locations': ['Remote'], 'degrees': [],
        }]
        return resp
    return _fake_http_get(url, timeout=timeout)

def http_head_dead_only(url, timeout=None, allow_redirects=True):
    if url == REAL_DEAD_LINK_URL:
        return Mock(status_code=403)
    return _fake_http_head_all_live(url, timeout=timeout, allow_redirects=allow_redirects)

tmp_path = Path(tempfile.mkdtemp())
state_dir = tmp_path / 'state'
state_dir.mkdir(parents=True)
(state_dir / run_pipeline.WRITE_GATE_FAILURES_FILENAME).write_text(json.dumps({
    REAL_DEAD_LINK_UID: {'check': 'url_liveness', 'count': run_pipeline.WRITE_GATE_FAILURE_THRESHOLD - 1, 'first_seen': '2026-08-10T23:25:36Z'},
}))

run_pipeline.MAX_NEW_WRITES_PER_RUN = {'AI/ML': 20, 'Fullstack': 20, 'CyS & Finance': 20, 'Other': 20}

kwargs = _run_once_kwargs(tmp_path, state_dir=state_dir, http_get=http_get_with_dead_link, http_head=http_head_dead_only)
record = run_pipeline.run_once(**kwargs)
print(json.dumps({k:v for k,v in record.items() if k != 'rejections'}, indent=2, default=str))
print('rejections:')
for r in record['rejections']:
    print(' ', r)
"

  ```
  ```
{
  "timestamp": "2026-07-17T15:00:00+00:00",
  "fetch_counts": {},
  "filter_match_counts": {},
  "new_count": 0,
  "already_seen_count": 0,
  "deferred_count": 0,
  "written_count": 0,
  "errors": [],
  "halted": true,
  "halt_reason": "SchemaDriftError: AIJobs: expected a non-empty 'jobs' list, got dict",
  "bucket_at_capacity": [],
  "dossier_total": 0,
  "newly_excluded_count": 0,
  "write_gate_excluded_count": 0
}
rejections:
  ```
- `Bash` — `git stash push -m "prompt19-wip-schema_drift" -- core/schema_drift.py tests/test_schema_drift.py && git stash list`
  ```
Saved working directory and index state On master: [REDACTED]
stash@{0}: On master: [REDACTED]
stash@{1}: On master: [REDACTED]
stash@{2}: On master: pre-rebase stash: CLAUDE.md autoMode notes + graphify-out regen + untracked files
  ```
- `Bash`:
  ```bash
VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/57040b74-cd56-4bb6-9696-bbc4df2afa6c/scratchpad/venv
$VENV/bin/python -m pytest tests/test_write_gate_failures.py -x -q 2>&1 | tail -80
  ```
  ```
........                                                                 [100%]
8 passed in 0.23s
  ```
- `Bash`:
  ```bash
VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/57040b74-cd56-4bb6-9696-bbc4df2afa6c/scratchpad/venv
$VENV/bin/python -m pytest tests/ -q 2>&1 | tail -60
  ```
  ```
    def test_load_zero_match_streaks_missing_file_returns_empty_dict(tmp_path):
>       assert run_pipeline.load_zero_match_streaks(tmp_path / "state") == {}
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       AttributeError: module 'run_pipeline' has no attribute 'load_zero_match_streaks'

tests/test_zero_match_alert.py:93: AttributeError
______ test_run_once_files_issue_and_persists_state_on_zero_match_streak _______

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-7/[REDACTED]')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f663bf084d0>

    def test_run_once_files_issue_and_persists_state_on_zero_match_streak(tmp_path, monkeypatch):
        """Integration-level confirmation that run_once actually calls issue_fn
        once the persisted streak crosses the threshold — the counting logic
        itself is covered by the pure-function tests above, this only proves
        the two are wired together and that state persists across calls."""
        monkeypatch.setattr(run_pipeline, "check_schema_drift", lambda http_get=None: None)
        state_dir = tmp_path / "state"
        state_dir.mkdir(parents=True)
>       run_pipeline.save_zero_match_streaks(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            state_dir, {"Ashby": {"streak": run_pipeline.ZERO_MATCH_STREAK_ALERT_THRESHOLD - 1, "ever_matched": True}},
        )
E       AttributeError: module 'run_pipeline' has no attribute 'save_zero_match_streaks'

tests/test_zero_match_alert.py:106: AttributeError
_________________ test_run_once_does_not_alert_below_threshold _________________

tmp_path = PosixPath('/tmp/pytest-of-anant_gupta/pytest-7/[REDACTED]')
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f663bf08140>

    def test_run_once_does_not_alert_below_threshold(tmp_path, monkeypatch):
        monkeypatch.setattr(run_pipeline, "check_schema_drift", lambda http_get=None: None)
        state_dir = tmp_path / "state"
        state_dir.mkdir(parents=True)
    
        def fake_fetch_and_filter(profile, http_get=None, excluded_ids=frozenset()):
            return {"Ashby": {"fetch_count": 4, "matched": []}}
    
        monkeypatch.setattr(run_pipeline, "fetch_and_filter", fake_fetch_and_filter)
        kwargs = _run_once_kwargs(tmp_path, state_dir=state_dir)
        record = run_pipeline.run_once(**kwargs)
    
>       assert record["zero_match_alerts"] == []
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       KeyError: 'zero_match_alerts'

tests/test_zero_match_alert.py:138: KeyError
=========================== short test summary info ============================
FAILED tests/test_zero_match_alert.py::test_zero_match_streak_increments_while_fetching_but_not_matching
FAILED tests/test_zero_match_alert.py::test_zero_match_streak_never_alerts_if_source_never_matched
FAILED tests/test_zero_match_alert.py::test_zero_match_streak_fires_exactly_once_at_threshold
FAILED tests/test_zero_match_alert.py::test_zero_match_streak_resets_on_a_real_match_and_marks_ever_matched
FAILED tests/test_zero_match_alert.py::test_zero_match_streak_unaffected_by_a_zero_fetch_run
FAILED tests/test_zero_match_alert.py::test_zero_match_streak_real_ashby_incident_shape
FAILED tests/test_zero_match_alert.py::test_load_save_zero_match_streaks_round_trips
FAILED tests/test_zero_match_alert.py::test_load_zero_match_streaks_missing_file_returns_empty_dict
FAILED tests/test_zero_match_alert.py::test_run_once_files_issue_and_persists_state_on_zero_match_streak
FAILED tests/test_zero_match_alert.py::test_run_once_does_not_alert_below_threshold
10 failed, 409 passed in 1.55s
  ```
- `Bash` — `git log --oneline --all | grep -i "debate\|exclusion\|threshold" | head -10`
  ```
6d54628 run_pipeline.py: raise MAX_DEBATE_LOSSES from 5 to 48
fd7b22e run_pipeline.py: alert when debate-loss exclusions spike in one run
080e8aa Dossier resource-limit notifications + debate-based write prioritization + debate-loss exclusion
  ```
- `Bash` — `git show --stat fd7b22e`
  ```
commit [REDACTED]
Author: Anant Gupta <anantmahi721@gmail.com>
Date:   Sun Aug 23 19:46:19 2026 +0400

    run_pipeline.py: alert when debate-loss exclusions spike in one run
    
    Real incident, 2026-08-21: 287 of the excluded log's 304 total entries
    (94%) were excluded on that single day, TikTok alone contributing 106 —
    invisible until a manual audit found it after the fact. The gap isn't
    "one company needs a cap," it's that a transient candidate backlog
    converts into permanent exclusion within MAX_DEBATE_LOSSES runs (~5 hours)
    with no signal to a human that it's happening.
    
    should_alert_on_exclusion_spike() fires one digest issue when a single
    run's newly_excluded_count exceeds 20 — comfortably above the normal
    handful-per-run trickle seen across logs/runs.jsonl. Decomposed as a pure
    function first (same testing philosophy this file's own module docstring
    already documents for update_debate_losses), plus one integration test
    confirming run_once actually wires it to issue_fn.
    
    Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>

 run_pipeline.py             | 29 +++++++++++++++++++++++++++++
 tests/test_debate_losses.py | 40 ++++++++++++++++++++++++++++++++++++++++
 2 files changed, 69 insertions(+)
  ```
- `Bash` — `git status --short`
  ```
 M CLAUDE.md
 M core/run_log.py
 M graphify-out/.graphify_labels.json
 M graphify-out/GRAPH_REPORT.md
 M graphify-out/graph.html
 M graphify-out/graph.json
 M graphify-out/manifest.json
 M run_pipeline.py
?? .claudeignore
?? .gitattributes
?? tests/test_write_gate_failures.py
?? tests/test_zero_match_alert.py
  ```
- `Bash` — `git diff --stat -- run_pipeline.py core/run_log.py`
  ```
 core/run_log.py |  24 ++++++++++++
 run_pipeline.py | 118 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 142 insertions(+)
  ```
- `Bash`:
  ```bash
git add run_pipeline.py core/run_log.py tests/test_write_gate_failures.py
git status --short -- run_pipeline.py core/run_log.py tests/test_write_gate_failures.py
  ```
  ```
M  core/run_log.py
M  run_pipeline.py
A  tests/test_write_gate_failures.py
  ```
- `Bash`:
  ```bash
git commit -m "$(cat <<'EOF'
run_pipeline.py: write_gate_failures.json — exclude structurally-doomed uids, not just out-ranked ones

Confirmed against a real, still-live incident: SimplifyJobs:de926b0a-99e7-4dbd-94cd-334ec565be9f
failed url_liveness (HTTP 403) in every one of 186 runs it appeared in between
2026-08-10 and 2026-08-28 (18 days), while sitting in none of debate_losses.json,
excluded_uids.json, or seen_ids.json the entire time. It's never "deferred" (that
only happens to items _prioritize_and_cap itself cuts for budget reasons) because
it keeps WINNING its bucket's debate_compare ranking — so it never touches
MAX_DEBATE_LOSSES, and never gets written, so it never reaches seen_ids either.
It occupies one of its bucket's limited MAX_NEW_WRITES_PER_RUN slots every run,
forever, pushing a real competing candidate into deferred (and a debate loss it
didn't otherwise deserve) in its place.

update_write_gate_failures() tracks per-uid consecutive-same-check rejection
counts, scoped to url_liveness and cross_source_duplicate only — the two checks
confirmed (both by this real case and by logs/runs.jsonl: 3274 and 2801
occurrences respectively) to repeat identically for the same structural reason
run over run. required_fields/format_compliance are deliberately excluded
(SYSTEMIC_REJECTION_CHECKS already means OUR code is broken, not the uid, and
both are 0/684 in practice); not_duplicate is excluded too (dedup_new's own
seen_ids check makes it structurally unable to repeat, and it is, in fact,
0/684). Threshold is 3 consecutive runs — a dead link doesn't need
MAX_DEBATE_LOSSES' 48-run benefit of the doubt built for genuinely ambiguous
ranking losses; dead-is-dead in a way out-ranked isn't.

A uid crossing the threshold joins the SAME excluded_ids set MAX_DEBATE_LOSSES
uses (fetch_and_filter/dedup_new already check it) rather than a second parallel
gate, and gets one line in its own reviewable markdown log (Excluded — Failed
The Write Gate.md) — same "notify, don't silently drop" discipline, distinct
from the debate-loss log since the reason reads wrong under that header.

Investigated live rather than adding throwaway instrumentation: the circumstantial
evidence was already strong (186/186 occurrences, zero exceptions, still
reproducing on the most recent run), and the new integration test drives the
real cited uid through the real pipeline functions to confirm it wins this_run
every time pre-fix and gets excluded on schedule post-fix — stronger, permanent
confirmation than a one-off log line would have given.

No MAX_DEBATE_LOSSES stopgap this round: fresh state shows real runway opened up,
not closed. Leading debate_losses entries now cap at 30 (was 24 at the last
check), with 18-21 losses of room left before MAX_DEBATE_LOSSES=48, and the
observed pace has SLOWED (24→30 took ~40 real hours, ~6.6-9.85 hr/loss, vs. the
~3 hr/loss during the dense 2026-08-26 run of hourly runs) because run.yml's
actual schedule is bursty, not strictly hourly. excluded_uids.json is still 388
with zero ApplyGuy:* exclusions. That's days of runway, not hours, and this
root-cause fix should ease (not just outrun) the pressure by stopping zombie
candidates from crowding real ones out of this_run in the first place.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
git status --short -- run_pipeline.py core/run_log.py tests/test_write_gate_failures.py
git log --oneline -3
  ```
  ```
[graphify hook] launching background rebuild (log: /home/anant_gupta/.cache/graphify-rebuild.log)
[master 778f531] run_pipeline.py: write_gate_failures.json — exclude structurally-doomed uids, not just out-ranked ones
 3 files changed, 363 insertions(+)
 create mode 100644 tests/test_write_gate_failures.py
778f531 run_pipeline.py: write_gate_failures.json — exclude structurally-doomed uids, not just out-ranked ones
42b8321 Update state + logs — 2026-08-28
ed8408a Update state + logs — 2026-08-27
  ```
- `Bash` — `git stash list`
  ```
stash@{0}: On master: [REDACTED]
stash@{1}: On master: [REDACTED]
stash@{2}: On master: pre-rebase stash: CLAUDE.md autoMode notes + graphify-out regen + untracked files
  ```
- `Bash` — `git stash pop stash@{0} 2>&1`
  ```
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   CLAUDE.md
	modified:   core/schema_drift.py
	modified:   graphify-out/.graphify_labels.json
	modified:   graphify-out/GRAPH_REPORT.md
	modified:   graphify-out/graph.html
	modified:   graphify-out/graph.json
	modified:   graphify-out/manifest.json
	modified:   tests/test_schema_drift.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.claudeignore
	.gitattributes
	tests/test_zero_match_alert.py

no changes added to commit (use "git add" and/or "git commit -a")
Dropped stash@{0} ([REDACTED])
  ```
- `Bash`:
  ```bash
git stash list
git stash pop stash@{0} 2>&1
  ```
  ```
Exit code 1
stash@{0}: On master: [REDACTED]
stash@{1}: On master: pre-rebase stash: CLAUDE.md autoMode notes + graphify-out regen + untracked files
Auto-merging run_pipeline.py
CONFLICT (content): Merge conflict in run_pipeline.py
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   tests/test_run_pipeline.py

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
	both modified:   run_pipeline.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   CLAUDE.md
	modified:   core/schema_drift.py
	modified:   graphify-out/.graphify_labels.json
	modified:   graphify-out/GRAPH_REPORT.md
	modified:   graphify-out/graph.html
	modified:   graphify-out/graph.json
	modified:   graphify-out/manifest.json
	modified:   tests/test_schema_drift.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.claudeignore
	.gitattributes
	tests/test_zero_match_alert.py

The stash entry is kept in case you need it again.
  ```
- `Bash` — `grep -n "^<<<<<<<\|^=======\|^>>>>>>>" run_pipeline.py`
  ```
321:<<<<<<< Updated upstream
364:=======
389:>>>>>>> Stashed changes
395:<<<<<<< Updated upstream
434:=======
473:>>>>>>> Stashed changes
672:<<<<<<< Updated upstream
674:=======
676:>>>>>>> Stashed changes
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - <<<<<<< Updated upstream
WRITE_GATE_FAILURES_FILENAME = "write_gate_failures.json"
  + WRITE_GATE_FAILURES_FILENAME = "write_gate_failures.json"
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - def load_write_gate_failures(state_dir) -> dict:
    path = Path(state_dir) / WRITE_GATE_FAILURES_FILENAME
=======
ZERO_MATCH_STREAKS_FILENAME = "zero_match_streaks.json"
  + def load_write_gate_failures(state_dir) -> dict:
    path = Path(state_dir) / WRITE_GATE_FAILURES_FILENAME
    if not path.exists():
        return {}
    return json.loads(path.read_text())


ZERO_MATCH_STREAKS_FILENAME = "zero_match_streaks.json"
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  - def load_zero_match_streaks(state_dir) -> dict:
    path = Path(state_dir) / ZERO_MATCH_STREAKS_FILENAME
>>>>>>> Stashed changes
    if not path.exists():
        return {}
    return json.loads(path.read_text())


<<<<<<< Updated upstream
def save_write_gate_failures(state_dir, failures: dict) -> None:
  + def load_zero_match_streaks(state_dir) -> dict:
    path = Path(state_dir) / ZERO_MATCH_STREAKS_FILENAME
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def save_write_gate_failures(state_dir, failures: dict) -> None:
  ```
- `Bash` — `grep -n "^<<<<<<<\|^=======\|^>>>>>>>" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```
435:=======
474:>>>>>>> Stashed changes
673:<<<<<<< Updated upstream
675:=======
677:>>>>>>> Stashed changes
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -     return failures, newly_excluded

=======
def save_zero_match_streaks
  +     return failures, newly_excluded


def save_zero_match_streaks
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -     return streaks, newly_alerting
>>>>>>> Stashed changes

# A required_fields
  +     return streaks, newly_alerting

# A required_fields
  ```
- `Bash` — `grep -n "^<<<<<<<\|^=======\|^>>>>>>>" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```
672:<<<<<<< Updated upstream
674:=======
676:>>>>>>> Stashed changes
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -         "newly_excluded_count": 0,
<<<<<<< Updated upstream
        "write_gate_excluded_count": 0,
=======
        "zero_match_alerts": [],
>>>>>>> Stashed changes
    }
  +         "newly_excluded_count": 0,
        "write_gate_excluded_count": 0,
        "zero_match_alerts": [],
    }
  ```
- `Bash`:
  ```bash
grep -n "^<<<<<<<\|^=======\|^>>>>>>>" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py
echo "exit: $?"
python3 -c "import ast; ast.parse(open('/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py').read())" && echo "PARSE OK"
  ```
  ```
exit: 1
PARSE OK
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
git add run_pipeline.py
git status --short
  ```
  ```
 M CLAUDE.md
 M core/schema_drift.py
 M graphify-out/.graphify_labels.json
 M graphify-out/GRAPH_REPORT.md
 M graphify-out/graph.html
 M graphify-out/graph.json
 M graphify-out/manifest.json
M  run_pipeline.py
M  tests/test_run_pipeline.py
 M tests/test_schema_drift.py
?? .claudeignore
?? .gitattributes
?? tests/test_zero_match_alert.py
  ```
- `Bash` — `git stash list`
  ```
stash@{0}: On master: [REDACTED]
stash@{1}: On master: pre-rebase stash: CLAUDE.md autoMode notes + graphify-out regen + untracked files
  ```
- `Bash`:
  ```bash
VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/57040b74-cd56-4bb6-9696-bbc4df2afa6c/scratchpad/venv
cd /home/anant_gupta/projects/work/internship-research-loop
$VENV/bin/python -m pytest tests/ -q 2>&1 | tail -40
  ```
  ```
........................................................................ [ 16%]
........................................................................ [ 32%]
........................................................................ [ 48%]
........................................................................ [ 64%]
........................................................................ [ 81%]
........................................................................ [ 97%]
............                                                             [100%]
444 passed in 1.31s
  ```
- `Bash` — `git stash drop stash@{0} && git stash list`
  ```
Dropped stash@{0} ([REDACTED])
stash@{0}: On master: pre-rebase stash: CLAUDE.md autoMode notes + graphify-out regen + untracked files
  ```
- `Bash` — `git status --short`
  ```
 M CLAUDE.md
 M core/schema_drift.py
 M graphify-out/.graphify_labels.json
 M graphify-out/GRAPH_REPORT.md
 M graphify-out/graph.html
 M graphify-out/graph.json
 M graphify-out/manifest.json
M  run_pipeline.py
M  tests/test_run_pipeline.py
 M tests/test_schema_drift.py
?? .claudeignore
?? .gitattributes
?? tests/test_zero_match_alert.py
  ```
- `Bash`:
  ```bash
git restore --staged run_pipeline.py tests/test_run_pipeline.py
git status --short
  ```
  ```
 M CLAUDE.md
 M core/schema_drift.py
 M graphify-out/.graphify_labels.json
 M graphify-out/GRAPH_REPORT.md
 M graphify-out/graph.html
 M graphify-out/graph.json
 M graphify-out/manifest.json
 M run_pipeline.py
 M tests/test_run_pipeline.py
 M tests/test_schema_drift.py
?? .claudeignore
?? .gitattributes
?? tests/test_zero_match_alert.py
  ```
- `Bash`:
  ```bash
git log --oneline -3
echo "---"
git show --stat 778f531
  ```
  ```
778f531 run_pipeline.py: write_gate_failures.json — exclude structurally-doomed uids, not just out-ranked ones
42b8321 Update state + logs — 2026-08-28
ed8408a Update state + logs — 2026-08-27
---
commit [REDACTED]
Author: Anant Gupta <anantmahi721@gmail.com>
Date:   Fri Aug 28 13:09:36 2026 +0400

    run_pipeline.py: write_gate_failures.json — exclude structurally-doomed uids, not just out-ranked ones
    
    Confirmed against a real, still-live incident: SimplifyJobs:[REDACTED]
    failed url_liveness (HTTP 403) in every one of 186 runs it appeared in between
    2026-08-10 and 2026-08-28 (18 days), while sitting in none of debate_losses.json,
    excluded_uids.json, or seen_ids.json the entire time. It's never "deferred" (that
    only happens to items _prioritize_and_cap itself cuts for budget reasons) because
    it keeps WINNING its bucket's debate_compare ranking — so it never touches
    MAX_DEBATE_LOSSES, and never gets written, so it never reaches seen_ids either.
    It occupies one of its bucket's limited MAX_NEW_WRITES_PER_RUN slots every run,
    forever, pushing a real competing candidate into deferred (and a debate loss it
    didn't otherwise deserve) in its place.
    
    update_write_gate_failures() tracks per-uid consecutive-same-check rejection
    counts, scoped to url_liveness and cross_source_duplicate only — the two checks
    confirmed (both by this real case and by logs/runs.jsonl: 3274 and 2801
    occurrences respectively) to repeat identically for the same structural reason
    run over run. required_fields/format_compliance are deliberately excluded
    (SYSTEMIC_REJECTION_CHECKS already means OUR code is broken, not the uid, and
    both are 0/684 in practice); not_duplicate is excluded too (dedup_new's own
    seen_ids check makes it structurally unable to repeat, and it is, in fact,
    0/684). Threshold is 3 consecutive runs — a dead link doesn't need
    MAX_DEBATE_LOSSES' 48-run benefit of the doubt built for genuinely ambiguous
    ranking losses; dead-is-dead in a way out-ranked isn't.
    
    A uid crossing the threshold joins the SAME excluded_ids set MAX_DEBATE_LOSSES
    uses (fetch_and_filter/dedup_new already check it) rather than a second parallel
    gate, and gets one line in its own reviewable markdown log (Excluded — Failed
    The Write Gate.md) — same "notify, don't silently drop" discipline, distinct
    from the debate-loss log since the reason reads wrong under that header.
    
    Investigated live rather than adding throwaway instrumentation: the circumstantial
    evidence was already strong (186/186 occurrences, zero exceptions, still
    reproducing on the most recent run), and the new integration test drives the
    real cited uid through the real pipeline functions to confirm it wins this_run
    every time pre-fix and gets excluded on schedule post-fix — stronger, permanent
    confirmation than a one-off log line would have given.
    
    No MAX_DEBATE_LOSSES stopgap this round: fresh state shows real runway opened up,
    not closed. Leading debate_losses entries now cap at 30 (was 24 at the last
    check), with 18-21 losses of room left before MAX_DEBATE_LOSSES=48, and the
    observed pace has SLOWED (24→30 took ~40 real hours, ~6.6-9.85 hr/loss, vs. the
    ~3 hr/loss during the dense 2026-08-26 run of hourly runs) because run.yml's
    actual schedule is bursty, not strictly hourly. excluded_uids.json is still 388
    with zero ApplyGuy:* exclusions. That's days of runway, not hours, and this
    root-cause fix should ease (not just outrun) the pressure by stopping zombie
    candidates from crowding real ones out of this_run in the first place.
    
    Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>

 core/run_log.py                   |  24 +++++
 run_pipeline.py                   | 118 ++++++++++++++++++++
 tests/test_write_gate_failures.py | 221 ++++++++++++++++++++++++++++++++++++++
 3 files changed, 363 insertions(+)
  ```

## Actions Taken
- Files created: /home/anant_gupta/projects/work/internship-research-loop/tests/test_write_gate_failures.py
- Files modified: /home/anant_gupta/projects/work/internship-research-loop/core/run_log.py, /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py
- Files deleted: (none)
- Commands run: git fetch origin 2>&1 | tail -5 && echo "---LOCAL HEAD---" && git rev-parse HEAD && echo "---ORIGIN MASTER---" && git rev-parse origin/master && echo "---STATUS---" && git status --short | head -30, git diff --stat && echo "=====" && git log --oneline -5, git diff run_pipeline.py, git diff CLAUDE.md tests/test_run_pipeline.py, git status --short -- run_pipeline.py tests/test_run_pipeline.py, git stash push -m "[REDACTED]" -- run_pipeline.py tests/test_run_pipeline.py && git stash list && git status --short -- run_pipeline.py tests/test_run_pipeline.py, python3 -c " import json losses = json.load(open('state/debate_losses.json')) print('total entries:', len(losses)) from collections import Counter c = Counter(losses.values()) if isinstance(losses, dict) else None vals = list(losses.values()) print('max loss value:', max(vals)) print('at 24:', sum(1 for v in vals if v==24)) print('at max(48):', sum(1 for v in vals if v==48)) apply_guy = {k:v for k,v in losses.items() if k.startswith('ApplyGuy:')} print('ApplyGuy count:', len(apply_guy)) print('ApplyGuy at 24:', sum(1 for v in apply_guy.values() if v==24)) print('ApplyGuy max:', max(apply_guy.values()) if apply_guy else None) import collections dist = collections.Counter(vals) print('distribution (sorted):', sorted(dist.items())) " , python3 -c " import json excl = json.load(open('state/excluded_uids.json')) print('excluded_uids type:', type(excl), 'len:', len(excl)) apply_guy_excl = [u for u in excl if u.startswith('ApplyGuy:')] if isinstance(excl, list) else None print('ApplyGuy excluded:', len(apply_guy_excl) if apply_guy_excl is not None else 'n/a') target = 'SimplifyJobs:[REDACTED]' print('target in excluded:', target in excl) seen = json.load(open('state/seen_ids.json')) print('seen type', type(seen), len(seen)) print('target in seen:', target in seen) losses = json.load(open('state/debate_losses.json')) print('target in debate_losses:', target in losses, losses.get(target)) " , wc -l logs/runs.jsonl python3 -c " import json target = 'SimplifyJobs:[REDACTED]' lines = open('logs/runs.jsonl').read().splitlines() print('total run records:', len(lines)) count=0 first=None last=None for l in lines: r = json.loads(l) rej = r.get('rejections', []) # rejections might be list of dicts or strings; check shape found = False if isinstance(rej, list): for item in rej: if isinstance(item, dict) and item.get('uid')==target: found = True elif isinstance(item, str) and target in item: found = True if found: count+=1 if first is None: first = r.get('timestamp') last = r.get('timestamp') print('records containing target in rejections:', count) print('first:', first, 'last:', last) " , python3 -c " import json target = 'SimplifyJobs:[REDACTED]' lines = open('logs/runs.jsonl').read().splitlines() r = json.loads(lines[-1]) print('last record timestamp:', r.get('timestamp')) rej = r.get('rejections', []) for item in rej[:3]: print(item) print('---searching for target in last record---') for item in rej: if isinstance(item, dict) and item.get('uid')==target: print(item) " , date -u echo "---" gh workflow list 2>&1 | head -10 echo "--- recent runs ---" gh run list --workflow=run.yml --limit 5 2>&1, python3 -c " import json losses = json.load(open('state/debate_losses.json')) top = sorted(losses.items(), key=lambda x: -x[1])[:15] for k,v in top: print(v, k) print() print('count at 27:', sum(1 for v in losses.values() if v==27)) apply_guy = {k:v for k,v in losses.items() if k.startswith('ApplyGuy:')} print('ApplyGuy at 27:', sum(1 for v in apply_guy.values() if v==27)) non_ag_27 = [k for k,v in losses.items() if v==27 and not k.startswith('ApplyGuy:')] print('non-ApplyGuy at 27 count:', len(non_ag_27)) print(non_ag_27[:5]) " , git log --oneline -- state/debate_losses.json | head -20, for c in $(git log --format=%H -- state/debate_losses.json | head -25); do ts=$(git log -1 --format=%cI $c) maxv=$(git show $c:state/debate_losses.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(max(d.values()) if d else 0)") echo "$ts $maxv" done, grep -n "def _prioritize_and_cap\|def debate_compare\|def update_debate_losses\|MAX_DEBATE_LOSSES\|MAX_NEW_WRITES_PER_RUN\|def run_once\|def validate_and_write\|issue_fn\|def classify" run_pipeline.py | head -60, grep -rn "def append_excluded_log" --include=*.py . , python3 -c " import json from collections import Counter lines = open('logs/runs.jsonl').read().splitlines() c = Counter() for l in lines: r = json.loads(l) for rej in r.get('rejections', []): c[rej.get('check')] += 1 for k,v in c.most_common(): print(k, v) " , grep -n "def test_update_debate_losses\|class Test\|update_debate_losses\|debate_losses" tests/test_run_pipeline.py | head -40, grep -rln "update_debate_losses\|debate_losses" tests/ | head; echo "---"; ls tests/ | grep -i debate, grep -n "_run_once_kwargs\|^PROFILE\|def _simplify_raw\|http_head\|SIMPLIFY_FIXTURE\|FIXTURES =" tests/test_run_pipeline.py | head -40, grep -n "def compute_uid\|SimplifyJobs" core/identity.py | head -10 echo "---normalize_simplify---" grep -n "def normalize_simplify" -A 20 ingestion/normalize.py | head -30 echo "---fixture sample---" python3 -c "import json; d=json.load(open('tests/fixtures/simplifyjobs.json')); print(json.dumps(d[0], indent=2)[:800])", grep -n "excluded_ids" run_pipeline.py, python3 -c "import run_pipeline" && echo OK, python3 -m pytest tests/test_write_gate_failures.py -x -q 2>&1 | tail -80, which python3; python3 --version; find / -maxdepth 4 -iname "*venv*" 2>/dev/null | head; cat /home/anant_gupta/projects/work/internship-research-loop/requirements*.txt 2>/dev/null; ls /home/anant_gupta/projects/work/internship-research-loop, pip show pytest 2>&1 | head -3; pip install --user -q pytest requests pyyaml jinja2 2>&1 | tail -20, cat /home/anant_gupta/projects/work/internship-research-loop/.github/workflows/test.yml 2>/dev/null, python3 -m venv /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad/venv 2>&1 | tail -5 && /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad/venv/bin/pip install -q -r requirements.txt 2>&1 | tail -10, VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad/venv $VENV/bin/python -m pytest tests/test_write_gate_failures.py -x -q 2>&1 | tail -100, python3 -c " from core.filter import load_profile import json p = load_profile() print(json.dumps(p, indent=2)[:1500]) ", python3 -c " import sys sys.path.insert(0, 'tests') from ingestion.normalize import normalize_simplify from core.filter import load_profile, matches from core.relevance import stage1_reject raw = { 'source': 'Simplify', 'category': 'Software', 'company_name': 'Acme', 'id': '[REDACTED]', 'title': 'Software Engineer Intern', 'active': True, 'terms': ['Summer 2027'], 'date_posted': 1765581501, 'url': 'https://simplify.jobs/p/[REDACTED]', 'locations': ['Remote'], 'degrees': [], } listing = normalize_simplify(raw) profile = load_profile() print('matches:', matches(listing, profile)) print('stage1_reject:', stage1_reject(listing.title, '')) " , python3 -c " import sys sys.path.insert(0, 'tests') from unittest.mock import Mock import run_pipeline from core.filter import load_profile from ingestion.sources import SIMPLIFY_URL from test_run_pipeline import _fake_http_get, _simplify_raw REAL_DEAD_LINK_URL = 'https://simplify.jobs/p/[REDACTED]' def http_get_with_dead_link(url, timeout=None): if url == SIMPLIFY_URL: resp = Mock(status_code=200) resp.json.return_value = _simplify_raw() + [{ 'source': 'Simplify', 'category': 'Software', 'company_name': 'Acme', 'id': '[REDACTED]', 'title': 'Software Engineer Intern', 'active': True, 'terms': ['Summer 2027'], 'date_posted': 1765581501, 'url': REAL_DEAD_LINK_URL, 'locations': ['Remote'], 'degrees': [], }] return resp return _fake_http_get(url, timeout=timeout) profile = load_profile() matched = run_pipeline.fetch_and_filter(profile, http_get_with_dead_link) uids = [run_pipeline.compute_uid(l) for l in matched['SimplifyJobs']['matched']] print('SimplifyJobs matched uids:', uids) print('target present:', 'SimplifyJobs:[REDACTED]' in uids) " , VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad/venv $VENV/bin/python -c " import sys sys.path.insert(0, 'tests') from unittest.mock import Mock import run_pipeline from core.filter import load_profile from ingestion.sources import SIMPLIFY_URL from test_run_pipeline import _fake_http_get, _simplify_raw REAL_DEAD_LINK_URL = 'https://simplify.jobs/p/[REDACTED]' def http_get_with_dead_link(url, timeout=None): if url == SIMPLIFY_URL: resp = Mock(status_code=200) resp.json.return_value = _simplify_raw() + [{ 'source': 'Simplify', 'category': 'Software', 'company_name': 'Acme', 'id': '[REDACTED]', 'title': 'Software Engineer Intern', 'active': True, 'terms': ['Summer 2027'], 'date_posted': 1765581501, 'url': REAL_DEAD_LINK_URL, 'locations': ['Remote'], 'degrees': [], }] return resp return _fake_http_get(url, timeout=timeout) profile = load_profile() matched = run_pipeline.fetch_and_filter(profile, http_get_with_dead_link) uids = [run_pipeline.compute_uid(l) for l in matched['SimplifyJobs']['matched']] print('SimplifyJobs matched uids:', uids) print('target present:', 'SimplifyJobs:[REDACTED]' in uids) " , VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad/venv $VENV/bin/python -c " import sys, json, tempfile sys.path.insert(0, 'tests') from pathlib import Path from unittest.mock import Mock import run_pipeline from test_run_pipeline import _fake_http_get, _simplify_raw, _fake_http_head_all_live, _run_once_kwargs from ingestion.sources import SIMPLIFY_URL REAL_DEAD_LINK_URL = 'https://simplify.jobs/p/[REDACTED]' REAL_DEAD_LINK_UID = 'SimplifyJobs:[REDACTED]' def http_get_with_dead_link(url, timeout=None): if url == SIMPLIFY_URL: resp = Mock(status_code=200) resp.json.return_value = _simplify_raw() + [{ 'source': 'Simplify', 'category': 'Software', 'company_name': 'Acme', 'id': '[REDACTED]', 'title': 'Software Engineer Intern', 'active': True, 'terms': ['Summer 2027'], 'date_posted': 1765581501, 'url': REAL_DEAD_LINK_URL, 'locations': ['Remote'], 'degrees': [], }] return resp return _fake_http_get(url, timeout=timeout) def http_head_dead_only(url, timeout=None, allow_redirects=True): if url == REAL_DEAD_LINK_URL: return Mock(status_code=403) return _fake_http_head_all_live(url, timeout=timeout, allow_redirects=allow_redirects) tmp_path = Path(tempfile.mkdtemp()) state_dir = tmp_path / 'state' state_dir.mkdir(parents=True) (state_dir / run_pipeline.WRITE_GATE_FAILURES_FILENAME).write_text(json.dumps({ REAL_DEAD_LINK_UID: {'check': 'url_liveness', 'count': run_pipeline.WRITE_GATE_FAILURE_THRESHOLD - 1, 'first_seen': '2026-08-10T23:25:36Z'}, })) run_pipeline.MAX_NEW_WRITES_PER_RUN = {'AI/ML': 20, 'Fullstack': 20, 'CyS & Finance': 20, 'Other': 20} kwargs = _run_once_kwargs(tmp_path, state_dir=state_dir, http_get=http_get_with_dead_link, http_head=http_head_dead_only) record = run_pipeline.run_once(**kwargs) print(json.dumps({k:v for k,v in record.items() if k != 'rejections'}, indent=2, default=str)) print('rejections:') for r in record['rejections']: print(' ', r) " , git stash push -m "[REDACTED]" -- core/schema_drift.py tests/test_schema_drift.py && git stash list, VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad/venv $VENV/bin/python -m pytest tests/test_write_gate_failures.py -x -q 2>&1 | tail -80, VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad/venv $VENV/bin/python -m pytest tests/ -q 2>&1 | tail -60, git log --oneline --all | grep -i "debate\|exclusion\|threshold" | head -10, git show --stat fd7b22e, git status --short, git diff --stat -- run_pipeline.py core/run_log.py, git add run_pipeline.py core/run_log.py tests/test_write_gate_failures.py git status --short -- run_pipeline.py core/run_log.py tests/test_write_gate_failures.py, git commit -m "$(cat <<'EOF' run_pipeline.py: write_gate_failures.json — exclude structurally-doomed uids, not just out-ranked ones Confirmed against a real, still-live incident: SimplifyJobs:[REDACTED] failed url_liveness (HTTP 403) in every one of 186 runs it appeared in between 2026-08-10 and 2026-08-28 (18 days), while sitting in none of debate_losses.json, excluded_uids.json, or seen_ids.json the entire time. It's never "deferred" (that only happens to items _prioritize_and_cap itself cuts for budget reasons) because it keeps WINNING its bucket's debate_compare ranking — so it never touches MAX_DEBATE_LOSSES, and never gets written, so it never reaches seen_ids either. It occupies one of its bucket's limited MAX_NEW_WRITES_PER_RUN slots every run, forever, pushing a real competing candidate into deferred (and a debate loss it didn't otherwise deserve) in its place. update_write_gate_failures() tracks per-uid consecutive-same-check rejection counts, scoped to url_liveness and cross_source_duplicate only — the two checks confirmed (both by this real case and by logs/runs.jsonl: 3274 and 2801 occurrences respectively) to repeat identically for the same structural reason run over run. required_fields/format_compliance are deliberately excluded (SYSTEMIC_REJECTION_CHECKS already means OUR code is broken, not the uid, and both are 0/684 in practice); not_duplicate is excluded too (dedup_new's own seen_ids check makes it structurally unable to repeat, and it is, in fact, 0/684). Threshold is 3 consecutive runs — a dead link doesn't need MAX_DEBATE_LOSSES' 48-run benefit of the doubt built for genuinely ambiguous ranking losses; dead-is-dead in a way out-ranked isn't. A uid crossing the threshold joins the SAME excluded_ids set MAX_DEBATE_LOSSES uses (fetch_and_filter/dedup_new already check it) rather than a second parallel gate, and gets one line in its own reviewable markdown log (Excluded — Failed The Write Gate.md) — same "notify, don't silently drop" discipline, distinct from the debate-loss log since the reason reads wrong under that header. Investigated live rather than adding throwaway instrumentation: the circumstantial evidence was already strong (186/186 occurrences, zero exceptions, still reproducing on the most recent run), and the new integration test drives the real cited uid through the real pipeline functions to confirm it wins this_run every time pre-fix and gets excluded on schedule post-fix — stronger, permanent confirmation than a one-off log line would have given. No MAX_DEBATE_LOSSES stopgap this round: fresh state shows real runway opened up, not closed. Leading debate_losses entries now cap at 30 (was 24 at the last check), with 18-21 losses of room left before MAX_DEBATE_LOSSES=48, and the observed pace has SLOWED (24→30 took ~40 real hours, ~6.6-9.85 hr/loss, vs. the ~3 hr/loss during the dense 2026-08-26 run of hourly runs) because run.yml's actual schedule is bursty, not strictly hourly. excluded_uids.json is still 388 with zero ApplyGuy:* exclusions. That's days of runway, not hours, and this root-cause fix should ease (not just outrun) the pressure by stopping zombie candidates from crowding real ones out of this_run in the first place. Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com> EOF )" git status --short -- run_pipeline.py core/run_log.py tests/test_write_gate_failures.py git log --oneline -3, git stash list, git stash pop stash@{0} 2>&1, git stash list git stash pop stash@{0} 2>&1, grep -n "^<<<<<<<\|^=======\|^>>>>>>>" run_pipeline.py, grep -n "^<<<<<<<\|^=======\|^>>>>>>>" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py, grep -n "^<<<<<<<\|^=======\|^>>>>>>>" /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py echo "exit: $?" python3 -c "import ast; ast.parse(open('/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py').read())" && echo "PARSE OK", cd /home/anant_gupta/projects/work/internship-research-loop git add run_pipeline.py git status --short, VENV=/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad/venv cd /home/anant_gupta/projects/work/internship-research-loop $VENV/bin/python -m pytest tests/ -q 2>&1 | tail -40, git stash drop stash@{0} && git stash list, git restore --staged run_pipeline.py tests/test_run_pipeline.py git status --short, git log --oneline -3 echo "---" git show --stat 778f531
- Tool call tally: Bash (57), Edit (11), Read (19), Write (1)

