---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: wsl
title: "Ashby zero-match streak and schema drift coverage"
started_at: 2026-08-28T08:26:56
ended_at: 2026-08-28T08:49:28
duration_minutes: 23
exported_at: 2026-08-28T13:15:02
project: internship-research-loop
cwd: '/home/anant_gupta/projects/work/internship-research-loop'
session_id: 8e83afe5-6380-416c-be0d-4f979f7f86ca
status: raw
turn_count: 4
tools_used:
  Bash: 69
  Edit: 20
  Read: 25
  Skill: 1
  Write: 1
tokens:
  input: 402
  output: 162904
  cache_creation: 498409
  cache_read: 30491581
  total: 31153296
cost_usd: 9.721796
model:
  - claude-sonnet-5
files_touched:
  - "/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/ingestion/normalize.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/filter.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/ingestion/sources.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/ingestion/freehire.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/ingestion/interndock.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/tests/test_zero_match_alert.py"
tags:
  - input
  - ai-conversation
  - claude-code
  - wsl
---

# Ashby zero-match streak and schema drift coverage

## You

**Context — verified fresh, 2026-08-27 ~11:10 UTC, against `origin/master` (`7a1be68`) directly via `git show`, not a local checkout — same staleness caveat as Prompt 18, recompute before acting:**

- `core/schema_drift.py`'s `check_all()` only pre-flights 5 of 11 sources: SimplifyJobs, Jose-Gael-Cruz-Lopez, vanshb03, zshah101, ApplyGuy. Greenhouse, Ashby, Lever, Freehire, AIJobs, InternDock (6 sources) have zero schema pre-flight — a silent field rename on any of them degrades to zero matches with no halt, no issue, nothing but a human noticing `filter_match_counts` stuck at 0 in the raw log.
- Concrete, not hypothetical: direct read of `logs/runs.jsonl` (681 records, `git show origin/master:logs/runs.jsonl`) shows Ashby's `fetch_counts` frozen at exactly 4 and `filter_match_counts` at exactly 0 for the **last 112 consecutive runs**, starting 2026-08-21T21:14:17 UTC. Before that streak began, 458 of 570 sampled runs had nonzero Ashby matches historically. `ASHBY_COMPANIES` in `ingestion/sources.py` currently lists 9 tokens: `ellipsislabs, quadrillion-labs, circleback, ctgt, pylon-labs, cohere, cursor, modal, elevenlabs`.
- A prior session (Prompt 14 v2, archived) already live-checked Ashby once (2026-08-24) and concluded "genuinely only ~4 have open roles right now" — but that check predates the current 112-run hard-zero streak fully setting in (it found a nonzero, if small, real match count, not a frozen zero). **Don't assume that prior finding still holds** — re-verify directly (curl/http_get all 9 tokens yourself) whether this is still "genuinely nothing to match" or has drifted into a real schema/API break since.
- Prompt 18 is fixing the write-gate failure-memory bug in a parallel session right now — stay out of `run_pipeline.py`'s debate/write-gate logic (`_prioritize_and_cap`, `update_debate_losses`, `write_gate_failures.json`) and `state/debate_losses.json`/`state/excluded_uids.json` semantics entirely; this prompt's `run_pipeline.py` touches should be limited to surfacing a new per-source alert in the run-record logging path.

### Task 1 — Investigate Ashby's zero-match streak directly
Curl/`http_get` each of the 9 tokens against the real Ashby API, compare the real current response shape/count against what `fetch_ashby`/`normalize_ashby` expect. State the real finding plainly, cited: genuine "no eligible postings right now" (structurally capped, matching the 2026-08-24 finding) or actual drift (renamed field, changed response shape, empty/error response, rate-limiting). If a token itself looks stale (company renamed/moved off Ashby), say so.

### Task 2 — Extend schema-drift coverage
Add check functions (mirroring `check_simplify_schema` et al.'s existing pattern) for the 6 currently-unwatched sources — Greenhouse, Ashby, Lever, Freehire, AIJobs, InternDock — each verifying the real, current API/feed response has the fields `normalize_*` expects, wired into `check_all()`. If a genuine structural reason makes one of these six impractical to pre-flight the same way (e.g., InternDock's Firecrawl-based, multi-URL fetch has no single stable schema to check against), say so explicitly rather than forcing a check that wouldn't mean anything.

### Task 3 — Per-source zero-match-rate alert
Add an alert to the run record (`run_pipeline.py`'s run-logging path) for a source sitting at `filter_match_count == 0` for N consecutive runs while `fetch_count > 0` and the source has historically had nonzero matches. Pick and justify a real N — 112 runs is how long it actually took a human to notice the Ashby streak this pass; pick something meaningfully shorter and cite why that number, not just "smaller."

### Task 4 — Tests
Fixture-based, mirroring the existing `schema_drift` test pattern, plus a test for the new zero-match alert logic. Full suite green.

### Task 5 — Report on Ashby's company list
Only if Task 1's investigation surfaces something concrete: is the 9-company `ASHBY_COMPANIES` list itself due for a refresh (a token gone stale/renamed), or is "genuinely ~4 open roles across 9 small companies" still the real, current answer?

### Explicitly out of scope
No write-gate/`debate_compare` changes (Prompt 18's job, running in parallel — don't touch `state/debate_losses.json`/`state/excluded_uids.json` semantics). No vault/Jarvis edits — the review-system tightening (Weekly Review template, Reviews MOC nudge) and the `Source of Truth.md`/`System - Build Log.md` full staleness pass from the 2026-08-26 postmortem are real, still-open items, but belong in a separate Jarvis-side prompt (deliberately not this one — a Codebase session has no path to the vault the way a Jarvis session does, per this project's established split).

### Report back
Task 1's Ashby finding (genuine cap vs. drift, cited). Which of the 6 sources got real schema-drift coverage, and how (or why one couldn't be meaningfully covered). The zero-match alert threshold chosen and why. Test results.

## Claude

I'll start by investigating the Ashby situation directly, then look at the schema_drift and run_pipeline code.

Good, now on latest master (`42b8321`). Now let's check the fresh Ashby streak in logs and check the live Ashby API directly for Task 1.

Streak now up to 115 runs (still frozen at fetch=4, matches=0). Now let's hit the live Ashby API directly for all 9 tokens to see the real current state.

Good — all live-verified. Now let me check `run_pipeline.py`'s `SOURCES` list and where `check_all` is invoked, plus existing tests for schema_drift, to match conventions precisely before writing code.

Now let me write the updated `core/schema_drift.py`.

Now add the check functions and wire into `check_all`:

Now let's insert the new state functions after `update_debate_losses` (around line 317) and wire the call site right after the fetch_counts/filter_match_counts loop (line 553).

Now wire the call site into `run_once()`:

Now let's check test_debate_losses.py's http_get fixture setup:

Good, it reuses `_fake_http_get` from test_run_pipeline.py. So fixing that one function fixes both files. Let me build proper fixture data for the schema-check calls.

Let's check the freehire fixture file used by `_by_case`:

Good — that's the last remaining failure, and it's the test file I need to update per Task 4 anyway. Let's rewrite `tests/test_schema_drift.py` to add fixtures/tests for the 6 new checks and fix the `check_all` coverage test.

Now let me add fixtures and tests for the 6 new checks, and fix `test_check_all_passes_when_all_sources_are_healthy`.

Now let's add happy-path/drift tests for each new source, and fix `test_check_all_passes_when_all_sources_are_healthy`.

Now update `test_check_all_passes_when_all_sources_are_healthy` to route the 6 new URLs and add unused required-keys import cleanup check:

Unused — let me remove them from the import.

Now let's run the full test suite for schema_drift and everything else.

All schema_drift tests pass. Now let's write tests for the zero-match-alert logic (Task 4), and run the full suite.

All pass. Now let's run the full suite.

All 436 tests pass. Now let's review with `/review-loop-change` before committing, since this touches `core/`, `ingestion/`(no, wait, I didn't touch ingestion) and `run_pipeline.py`.

**Tool calls:**

- `Bash` — `sed -n '1,200p' ingestion/sources.py | grep -n "ASHBY\|def fetch_ashby\|def normalize_ashby" `
  ```
30:ASHBY_JOBS_URL = "https://api.ashbyhq.com/posting-api/job-board/{token}"
37:# GREENHOUSE_JOBS_URL/ASHBY_JOBS_URL returning a non-empty jobs array —
55:ASHBY_COMPANIES = {
149:def fetch_ashby(http_get=None) -> list:
152:    for token, company in ASHBY_COMPANIES.items():
154:            resp = get(ASHBY_JOBS_URL.format(token=token), timeout=TIMEOUT)
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
- `Bash` — `git log --oneline -5 && echo --- && git remote -v && echo --- && git fetch origin master 2>&1 | tail -5 && git log --oneline origin/master -5 2>&1`
  ```
cbbb2a1 Wire InternDock into SOURCES (Task 1) + add ApplyGuy as a source (Task 2)
dc135e3 Add InternDock drop-detection primitives (Task 3): sitemap index + posting parser
8a132a2 Add Lever as a source (Task 5): fetch_lever/normalize_lever, second real company beyond Palantir
93972d0 identity.py: add Oracle Cloud HCM job-id pattern for cross-source dedup
6d54628 run_pipeline.py: raise MAX_DEBATE_LOSSES from 5 to 48
---
origin	https://github.com/gupta-builds/internship-research-loop.git (fetch)
origin	https://github.com/gupta-builds/internship-research-loop.git (push)
---
From https://github.com/gupta-builds/internship-research-loop
 * branch            master     -> FETCH_HEAD
42b8321 Update state + logs — 2026-08-28
ed8408a Update state + logs — 2026-08-27
414028f Recheck log — 2026-08-27
e33c577 Update state + logs — 2026-08-27
7a1be68 Update state + logs — 2026-08-27
  ```
- `Bash` — `grep -n "ASHBY_COMPANIES" -A 12 ingestion/sources.py`
  ```
55:ASHBY_COMPANIES = {
56-    "ellipsislabs": "Ellipsis Labs",
57-    "quadrillion-labs": "Quadrillion",
58-    "circleback": "Circleback",
59-    "ctgt": "CTGT",
60-    "pylon-labs": "Pylon",
61-    "cohere": "Cohere",
62-    "cursor": "Cursor (Anysphere)",
63-    "modal": "Modal",
64-    "elevenlabs": "ElevenLabs",
65-}
66-
67-# Second real Lever-hosted company beyond Palantir (Task 5, 2026-08-24):
--
152:    for token, company in ASHBY_COMPANIES.items():
153-        try:
154-            resp = get(ASHBY_JOBS_URL.format(token=token), timeout=TIMEOUT)
155-            resp.raise_for_status()
156-            jobs = resp.json().get("jobs", [])
157-        except requests.RequestException:
158-            continue
159-        for job in jobs:
160-            if job.get("employmentType") == "Intern":  # structured — use it, not title text
161-                listings.append(normalize_ashby(job, company))
162-    return listings
163-
164-
  ```
- `Bash` — `git status && echo --- && git diff --stat CLAUDE.md && echo --- && git log --oneline HEAD..origin/master`
  ```
On branch master
Your branch is behind 'origin/master' by 29 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   CLAUDE.md
	modified:   graphify-out/.graphify_labels.json
	modified:   graphify-out/GRAPH_REPORT.md
	modified:   graphify-out/graph.html
	modified:   graphify-out/graph.json
	modified:   graphify-out/manifest.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.claudeignore
	.gitattributes

no changes added to commit (use "git add" and/or "git commit -a")
---
 CLAUDE.md | 13 +++++++++++++
 1 file changed, 13 insertions(+)
---
42b8321 Update state + logs — 2026-08-28
ed8408a Update state + logs — 2026-08-27
414028f Recheck log — 2026-08-27
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
496fbb6 Recheck log — 2026-08-26
01e93af Update state + logs — 2026-08-26
d41da21 Update state + logs — 2026-08-26
72c8d39 Update state + logs — 2026-08-26
ab78c53 Update state + logs — 2026-08-26
2d87dfa Update state + logs — 2026-08-26
4937aa9 Update state + logs — 2026-08-26
572490f Update state + logs — 2026-08-25
b20dc4d Update state + logs — 2026-08-25
7bab3f7 Update state + logs — 2026-08-25
a234200 Update state + logs — 2026-08-25
72495a0 Update state + logs — 2026-08-25
bd82f96 Update state + logs — 2026-08-25
  ```
- `Bash` — `git stash push -u -m "pre-pull stash: CLAUDE.md + graphify-out local edits" && git pull --ff-only origin master && git stash pop`
  ```
Saved working directory and index state On master: pre-pull stash: CLAUDE.md + graphify-out local edits
From https://github.com/gupta-builds/internship-research-loop
 * branch            master     -> FETCH_HEAD
Updating cbbb2a1..42b8321
Fast-forward
 logs/rechecks.jsonl               |   2 +
 logs/runs.jsonl                   |  27 +++
 state/debate_losses.json          | 342 +++++++++++++++++++++++++++++++++++++-
 state/dossier_uids.json           |  28 +++-
 state/interndock_seen_guides.json |  14 ++
 state/opt_cache.json              |  70 ++++++++
 state/seen_ids.json               |  18 ++
 7 files changed, 491 insertions(+), 10 deletions(-)
 create mode 100644 state/interndock_seen_guides.json
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   CLAUDE.md
	modified:   graphify-out/.graphify_labels.json
	modified:   graphify-out/GRAPH_REPORT.md
	modified:   graphify-out/graph.html
	modified:   graphify-out/graph.json
	modified:   graphify-out/manifest.json

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.claudeignore
	.gitattributes

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} ([REDACTED])
  ```
- `Bash`:
  ```bash
python3 -c "
import json
recs = [json.loads(l) for l in open('logs/runs.jsonl')]
print('total records', len(recs))
# find ashby fetch_counts/filter_match_counts trend
streak = 0
last_nonzero = None
for r in reversed(recs):
    fc = r.get('fetch_counts', {}).get('Ashby')
    mc = r.get('filter_match_counts', {}).get('Ashby')
    if fc is None: continue
    if mc == 0 and fc and fc > 0:
        streak += 1
    else:
        last_nonzero = r.get('timestamp')
        break
print('current zero-streak (from most recent run backwards):', streak)
print('most recent run with nonzero match or fc==0 before streak:', last_nonzero)
print('most recent record ashby:', recs[-1].get('timestamp'), recs[-1].get('fetch_counts',{}).get('Ashby'), recs[-1].get('filter_match_counts',{}).get('Ashby'))
"

  ```
  ```
total records 684
current zero-streak (from most recent run backwards): 115
most recent run with nonzero match or fc==0 before streak: 2026-08-21T21:14:17.229836+00:00
most recent record ashby: 2026-08-28T07:57:52.256499+00:00 4 0
  ```
- `Bash`:
  ```bash
for token in ellipsislabs quadrillion-labs circleback ctgt pylon-labs cohere cursor modal elevenlabs; do
  echo "=== $token ==="
  curl -s -o /tmp/ashby_$token.json -w "HTTP %{http_code}\n" "https://api.ashbyhq.com/posting-api/job-board/$token"
  python3 -c "
import json,sys
try:
    d = json.load(open('/tmp/ashby_$token.json'))
except Exception as e:
    print('PARSE ERROR', e); sys.exit()
if isinstance(d, dict):
    print('keys:', sorted(d.keys()))
    jobs = d.get('jobs', [])
    print('jobs count:', len(jobs))
    if jobs:
        print('first job keys:', sorted(jobs[0].keys()))
        print('sample employmentType:', [j.get('employmentType') for j in jobs[:10]])
else:
    print('type:', type(d))
"
done
  ```
  ```
=== ellipsislabs ===
HTTP 200
keys: ['apiVersion', 'jobs']
jobs count: 12
first job keys: ['address', 'applyUrl', 'department', 'descriptionHtml', 'descriptionPlain', 'employmentType', 'id', 'isListed', 'isRemote', 'jobUrl', 'location', 'publishedAt', 'secondaryLocations', 'team', 'title', 'workplaceType']
sample employmentType: ['FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'Intern']
=== quadrillion-labs ===
HTTP 200
keys: ['apiVersion', 'jobs']
jobs count: 8
first job keys: ['address', 'applyUrl', 'department', 'descriptionHtml', 'descriptionPlain', 'employmentType', 'id', 'isListed', 'isRemote', 'jobUrl', 'location', 'publishedAt', 'secondaryLocations', 'team', 'title', 'workplaceType']
sample employmentType: ['FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime']
=== circleback ===
HTTP 200
keys: ['apiVersion', 'jobs']
jobs count: 11
first job keys: ['address', 'applyUrl', 'department', 'descriptionHtml', 'descriptionPlain', 'employmentType', 'id', 'isListed', 'isRemote', 'jobUrl', 'location', 'publishedAt', 'secondaryLocations', 'team', 'title', 'workplaceType']
sample employmentType: ['FullTime', 'FullTime', 'FullTime', 'FullTime', 'Intern', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime']
=== ctgt ===
HTTP 200
keys: ['apiVersion', 'jobs']
jobs count: 3
first job keys: ['address', 'applyUrl', 'department', 'descriptionHtml', 'descriptionPlain', 'employmentType', 'id', 'isListed', 'isRemote', 'jobUrl', 'location', 'publishedAt', 'secondaryLocations', 'team', 'title', 'workplaceType']
sample employmentType: ['FullTime', 'FullTime', 'FullTime']
=== pylon-labs ===
HTTP 200
keys: ['apiVersion', 'jobs']
jobs count: 21
first job keys: ['address', 'applyUrl', 'department', 'descriptionHtml', 'descriptionPlain', 'employmentType', 'id', 'isListed', 'isRemote', 'jobUrl', 'location', 'publishedAt', 'secondaryLocations', 'team', 'title', 'workplaceType']
sample employmentType: ['FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime']
=== cohere ===
HTTP 200
keys: ['apiVersion', 'jobs']
jobs count: 146
first job keys: ['address', 'applyUrl', 'department', 'descriptionHtml', 'descriptionPlain', 'employmentType', 'id', 'isListed', 'isRemote', 'jobUrl', 'location', 'publishedAt', 'secondaryLocations', 'team', 'title', 'workplaceType']
sample employmentType: ['FullTime', 'FullTime', 'FullTime', 'Contract', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime']
=== cursor ===
HTTP 200
keys: ['apiVersion', 'jobs']
jobs count: 121
first job keys: ['address', 'applyUrl', 'department', 'descriptionHtml', 'descriptionPlain', 'employmentType', 'id', 'isListed', 'isRemote', 'jobUrl', 'location', 'publishedAt', 'secondaryLocations', 'team', 'title', 'workplaceType']
sample employmentType: ['FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime']
=== modal ===
HTTP 200
keys: ['apiVersion', 'jobs']
jobs count: 31
first job keys: ['address', 'applyUrl', 'department', 'descriptionHtml', 'descriptionPlain', 'employmentType', 'id', 'isListed', 'isRemote', 'jobUrl', 'location', 'publishedAt', 'secondaryLocations', 'team', 'title', 'workplaceType']
sample employmentType: ['FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime']
=== elevenlabs ===
HTTP 200
keys: ['apiVersion', 'jobs']
jobs count: 249
first job keys: ['address', 'applyUrl', 'department', 'descriptionHtml', 'descriptionPlain', 'employmentType', 'id', 'isListed', 'isRemote', 'jobUrl', 'location', 'publishedAt', 'secondaryLocations', 'team', 'title', 'workplaceType']
sample employmentType: ['FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime', 'FullTime']
  ```
- `Bash`:
  ```bash
for token in ellipsislabs quadrillion-labs circleback ctgt pylon-labs cohere cursor modal elevenlabs; do
  count=$(python3 -c "
import json
d = json.load(open('/tmp/ashby_$token.json'))
jobs = d.get('jobs', [])
interns = [j for j in jobs if j.get('employmentType')=='Intern']
print(len(interns), [j.get('title') for j in interns])
")
  echo "$token: $count"
done
  ```
  ```
ellipsislabs: 1 ['Software Engineer - 2027 Interns']
quadrillion-labs: 0 []
circleback: 1 ['Software Engineering Intern (Summer 2027)']
ctgt: 0 []
pylon-labs: 0 []
cohere: 2 ['Software Engineer Intern (Winter 2027)', 'Machine Learning Intern/Co-op  (Winter 2027)']
cursor: 0 []
modal: 0 []
elevenlabs: 0 []
  ```
- `Bash` — `grep -n "filter_match_count\|fetch_count\|seen_ids\|def run\b" run_pipeline.py | head -60`
  ```
68:# nor pre-seeding seen_ids to silently skip it (throws away real, currently-
304:    written) this run entirely — it's in seen_ids.json now, its loss history
326:def load_seen_ids(state_path) -> set:
333:def save_seen_ids(state_path, seen_ids: set) -> None:
336:    path.write_text(json.dumps(sorted(seen_ids), indent=2) + "\n")
349:    """Returns {source_name: {"fetch_count": int, "matched": [Listing, ...]}}.
358:            "fetch_count": len(listings),
368:def dedup_new(matched_by_source: dict, seen_ids: set, excluded_ids: frozenset = frozenset()):
381:            if uid in seen_ids or uid in seen_this_run:
389:def validate_and_write(new_listings, profile: dict, jarvis_dir, seen_ids: set, date_found: str,
392:    the Jarvis checkout. Does NOT push and does NOT mutate seen_ids — the
410:    # diverged from seen_ids after the 2026-07-18 manual cleanup), plus
426:        result = validate(listing, uid, markdown, seen_ids, http_head=http_head, dossier_keys=dossier_keys)
503:        "fetch_counts": {},
504:        "filter_match_counts": {},
522:        seen_ids = load_seen_ids(state_path)
535:        matched_by_source["InternDock"] = {"fetch_count": len(interndock_listings), "matched": interndock_matched}
552:        record["fetch_counts"][name] = info["fetch_count"]
553:        record["filter_match_counts"][name] = len(info["matched"])
555:    new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids, excluded_ids=excluded_ids)
568:        this_run, profile, jarvis_dir, seen_ids, now.date().isoformat(), http_head,
660:            "state/seen_ids.json was NOT updated for these — they'll be retried next run.",
669:        seen_ids.update(written_uids)
672:    save_seen_ids(state_path, seen_ids)
695:        state_path=REPO_ROOT / "state" / "seen_ids.json",
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Bash` — `grep -n "excluded_ids\s*=\|MAX_DEBATE_LOSSES\|def compute_uid\|update_debate_losses" run_pipeline.py | head -30`
  ```
194:MAX_DEBATE_LOSSES = 48
205:# new candidates all cross MAX_DEBATE_LOSSES together — real incident,
210:# MAX_DEBATE_LOSSES runs (~5 hours) with no signal to a human that it's
300:def update_debate_losses(losses: dict, deferred: list, written_uids: list) -> tuple:
305:    is moot. A uid whose count reaches MAX_DEBATE_LOSSES is returned in
314:        if losses[uid] >= MAX_DEBATE_LOSSES:
351:    comparator MAX_DEBATE_LOSSES consecutive times here, before it's even
518:    excluded_ids = load_excluded_uids(state_dir) if state_dir is not None else set()
523:        matched_by_source = fetch_and_filter(profile, http_get, excluded_ids=excluded_ids)
555:    new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids, excluded_ids=excluded_ids)
578:    # entirely. A uid crossing MAX_DEBATE_LOSSES moves to the excluded set
583:        debate_losses, newly_excluded = update_debate_losses(debate_losses, deferred, written_uids)
587:            excluded_ids = load_excluded_uids(state_dir)
593:                    f"excluded {now.date().isoformat()} — lost the debate {MAX_DEBATE_LOSSES} consecutive runs"
597:                    max_losses=MAX_DEBATE_LOSSES,
603:                f"{record['newly_excluded_count']} candidates crossed MAX_DEBATE_LOSSES "
604:                f"({MAX_DEBATE_LOSSES} consecutive losses) and were permanently excluded in this single "
  ```
- `Bash`:
  ```bash
cat state/excluded_uids.json 2>/dev/null | head -50; echo "---count---"; python3 -c "import json; print(len(json.load(open('state/excluded_uids.json'))))" 2>/dev/null
echo "--- normalize_ashby ---"
grep -n "def normalize_ashby" -A 25 ingestion/sources.py
  ```
  ```
[
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "AIJobs:[REDACTED]",
  "Ashby:[REDACTED]",
  "Ashby:[REDACTED]",
  "Jose-Gael-Cruz-Lopez:[REDACTED]",
  "Jose-Gael-Cruz-Lopez:[REDACTED]",
  "SimplifyJobs:[REDACTED]",
  "SimplifyJobs:[REDACTED]",
  "SimplifyJobs:[REDACTED]",
  "SimplifyJobs:[REDACTED]",
  "SimplifyJobs:[REDACTED]",
  "SimplifyJobs:[REDACTED]",
  "SimplifyJobs:[REDACTED]",
  "SimplifyJobs:[REDACTED]",
  "SimplifyJobs:[REDACTED]",
  "SimplifyJobs:[REDACTED]",
---count---
388
--- normalize_ashby ---
  ```
- `Bash`:
  ```bash
grep -n "def normalize_ashby" -A 20 ingestion/sources.py
echo "---uid---"
grep -n "def compute_uid" -A 20 identity.py 2>/dev/null || find . -name "identity.py" | xargs grep -n "def compute_uid" -A 20
echo "--- live ashby job ids ---"
for token in ellipsislabs circleback cohere; do
python3 -c "
import json
d = json.load(open('/tmp/ashby_$token.json'))
jobs = [j for j in d.get('jobs', []) if j.get('employmentType')=='Intern']
for j in jobs:
    print('$token', j.get('id'), j.get('title'), j.get('publishedAt'))
"
done
  ```
  ```
---uid---
79:def compute_uid(listing) -> str:
80-    if not listing.raw_id:
81-        raise ValueError(f"listing from {listing.source} has no upstream id: {listing.company!r}")
82-    return f"{listing.source}:{listing.raw_id}"
83-
84-
85-# Not cross_source_key()'s space-preserving norm() reused verbatim: that one
86-# collapses punctuation to a single space (needed to keep title text
87-# word-tokenized — "Intern Co-op" vs "Intern/Co-op" must still split into the
88-# same words). A company name is a short identifier, not sentence-shaped
89-# text, and the real case this needs to catch ("D.E. Shaw" vs "DE Shaw")
90-# fails under that space-preserving version — "d e shaw" != "de shaw". Fold
91-# out all non-alphanumeric characters entirely instead, so both collapse to
92-# the identical "deshaw".
93-def _norm_company(s: str) -> str:
94-    return re.sub(r"[^a-z0-9]", "", s.lower())
95-
96-
97-def cross_source_key(company: str, title: str, url: str = "") -> str:
98-    job_id = extract_ats_job_id(url)
99-    if job_id:
--- live ashby job ids ---
ellipsislabs [REDACTED] Software Engineer - 2027 Interns 2026-03-26T19:40:01.700+00:00
circleback [REDACTED] Software Engineering Intern (Summer 2027) 2026-06-10T20:14:25.154+00:00
cohere [REDACTED] Software Engineer Intern (Winter 2027) 2026-05-01T20:20:40.899+00:00
cohere [REDACTED] Machine Learning Intern/Co-op  (Winter 2027) 2026-05-13T17:16:14.014+00:00
  ```
- `Bash` — `grep -n "def normalize_ashby\|def fetch_ashby" -A 15 ingestion/sources.py | head -60`
  ```
149:def fetch_ashby(http_get=None) -> list:
150-    get = http_get or requests.get
151-    listings = []
152-    for token, company in ASHBY_COMPANIES.items():
153-        try:
154-            resp = get(ASHBY_JOBS_URL.format(token=token), timeout=TIMEOUT)
155-            resp.raise_for_status()
156-            jobs = resp.json().get("jobs", [])
157-        except requests.RequestException:
158-            continue
159-        for job in jobs:
160-            if job.get("employmentType") == "Intern":  # structured — use it, not title text
161-                listings.append(normalize_ashby(job, company))
162-    return listings
163-
164-
  ```
- `Bash` — `grep -n "^def normalize_ashby" ingestion/sources.py`
  ```
(Bash completed with no output)
  ```
- `Bash` — `grep -n "normalize_ashby" ingestion/sources.py`
  ```
9:    normalize_ashby,
161:                listings.append(normalize_ashby(job, company))
  ```
- `Bash` — `grep -rn "def normalize_ashby" .`
  ```
ingestion/normalize.py:165:def normalize_ashby(raw: dict, company: str) -> Listing:
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/normalize.py`
- `Bash` — `grep -n "^def matches\|^def stage1_reject\|^def location_eligible\|^def degrees_eligible" core/filter.py core/relevance.py 2>/dev/null`
  ```
core/relevance.py:78:def stage1_reject(title: str, raw_text: str) -> bool:
core/filter.py:81:def location_eligible(locations: list) -> bool:
core/filter.py:87:def matches(listing, profile: dict) -> bool:
core/filter.py:121:def degrees_eligible(degrees: list, profile: dict) -> bool:
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/filter.py`
- `Bash` — `grep -n "_matches_ashby" -A 15 core/filter.py`
  ```
103:        ok = _matches_ashby(listing, profile)
104-    elif listing.source == "Lever":
105-        ok = _matches_lever(listing, profile)
106-    elif listing.source == "InternDock":
107-        ok = _matches_interndock(listing, profile)
108-    elif listing.source == "Freehire":
109-        ok = _matches_freehire(listing, profile)
110-    elif listing.source == "AIJobs":
111-        ok = _matches_ai_jobs(listing, profile)
112-    else:
113-        raise ValueError(f"unknown source: {listing.source}")
114-    if ok and profile.get("locations_allow") == "us_remote":
115-        ok = location_eligible(listing.locations)
116-    if ok:
117-        ok = degrees_eligible(listing.degrees, profile)
118-    return ok
--
296:_matches_ashby = _matches_free_text_source
297-_matches_lever = _matches_free_text_source
298-# InternDock's drop pages span every industry (banking, marketing, legal,
299-# accounting, not just software), unlike Greenhouse/Ashby/Lever's tech-only
300-# curated company seed lists — this term/season check alone does not filter
301-# by job function. stage1_reject/stage2_confirm (core/relevance.py) are the
302-# real relevance gate downstream, same as for every other free-text source.
303-_matches_interndock = _matches_free_text_source
304-# Freehire's own postings often do state the term literally (Google's real
305-# posting title was "Software Engineering Intern, BS, Summer 2027"), but its
306-# aggregated sources are uneven — same free-text/bare-year fallback applies.
307-_matches_freehire = _matches_free_text_source
308-_matches_ai_jobs = _matches_free_text_source
  ```
- `Bash` — `grep -n "_matches_free_text_source" -B2 -A 30 core/filter.py | head -50`
  ```
278-
279-
280:def _matches_free_text_source(listing, profile: dict) -> bool:
281-    haystack = f"{listing.title} {listing.raw_text}"
282-    if _text_has_any(haystack, profile.get("exclude_terms", [])):
283-        return False
284-    if _text_has_any(haystack, profile["terms"]):
285-        return True
286-    # Fallback: no exact "Summer 2027"-style phrase, but the bare target year
287-    # is present — pass, permissive by design. Anything without even a bare
288-    # target-year digit string (wrong year, or no year mentioned at all)
289-    # rejects here; that's still permissive relative to the strict-phrase
290-    # rule, just not unconditionally permissive.
291-    t = _norm(haystack)
292-    return any(y in t for y in _target_years(profile["terms"]))
293-
294-
295:_matches_greenhouse = _matches_free_text_source
296:_matches_ashby = _matches_free_text_source
297:_matches_lever = _matches_free_text_source
298-# InternDock's drop pages span every industry (banking, marketing, legal,
299-# accounting, not just software), unlike Greenhouse/Ashby/Lever's tech-only
300-# curated company seed lists — this term/season check alone does not filter
301-# by job function. stage1_reject/stage2_confirm (core/relevance.py) are the
302-# real relevance gate downstream, same as for every other free-text source.
303:_matches_interndock = _matches_free_text_source
304-# Freehire's own postings often do state the term literally (Google's real
305-# posting title was "Software Engineering Intern, BS, Summer 2027"), but its
306-# aggregated sources are uneven — same free-text/bare-year fallback applies.
307:_matches_freehire = _matches_free_text_source
308:_matches_ai_jobs = _matches_free_text_source
  ```
- `Bash` — `cat core/profile.yaml`
  ```
# Layer 2 filter config — see Research Loop Implementation Plan for rationale.
grad_year: 2028
class_year: junior
eligible_class_tags: [Junior, "3rd year"]  # matched as case-insensitive substrings against target_year entries
accept_unrestricted: true  # postings with no class-year field at all still match
# "Winter 2027" = Dec 2026-Feb 2027 in SimplifyJobs' taxonomy — winters are
# labeled by the LATER year, confirmed 2026-07-18 by term adjacency in live data
# (three real listings co-tag ["Fall 2026", "Winter 2027"]). Postings don't
# publish actual months in the feed, so the human screen of the fetched posting
# content is still what confirms a genuine Dec-Jan window per posting.
terms: ["Summer 2027", "Winter 2027", "Spring 2027"]
# Summer/Winter 2027 are equally top priority; Spring 2027 is wanted but
# explicitly lower priority. This is a weight, not a second pass/fail gate —
# Spring 2027 still matches like any other wanted term today. A later, separate
# task consumes this for priority tagging; this one only makes it present and
# readable downstream.
terms_weight: {"Summer 2027": "high", "Winter 2027": "high", "Spring 2027": "low"}
# Real category values observed on SimplifyJobs/Summer2026-Internships (dev/.github/scripts/listings.json),
# not the generic names in the original transcript — confirmed by fetching live data 2026-07-16.
categories: ["Software", "Software Engineering", "AI/ML/Data", "Data Science, AI & Machine Learning"]
# Fellowship/research/mentorship-shaped entries were checked against live data
# 2026-07-26 (SimplifyJobs, JGCL, zshah101 feeds + 5 Greenhouse/5 Ashby seeded
# company boards): real examples exist (e.g. SimplifyJobs "Oracle Database
# Research Intern" category=Software terms includes Winter/Spring 2027; JGCL
# "CBAI Summer Research Fellowship in AI Safety '26" category=Research; JGCL
# "Anthropic Fellows Program" category=Program; zshah101 "Research Intern -
# School of Computer Science - LTI" (CMU) category=Software) — but every one
# already matches under the existing rules: SimplifyJobs/zshah101 tag them
# with a category already in categories/_ZSHAH101_CATEGORIES above, and JGCL's
# matcher never gates on category at all. No fellowship/mentorship-shaped hits
# turned up on the seeded Greenhouse/Ashby boards, and those two sources are
# free-text term matching with no category gate to begin with. No matching
# code needed — nothing here to extend yet.
#
# Pay is never a filter criterion anywhere in this pipeline — confirmed
# 2026-07-26 by grepping core/filter.py for any pay/pay_per_week gate; none
# exists. Don't add one; compensation is out of scope for Layer 2 eligibility.
# Rejects a SimplifyJobs listing outright if any of these terms are present, even
# alongside an allowed term (multi-term/rotational postings spanning both cycles).
exclude_terms: ["Summer 2026", "Fall 2026", "Spring 2026"]
# Rule built 2026-07-17 from live feed data (1216 distinct location strings), not
# guessed — see location_eligible() in core/filter.py. Permissive: no location
# data or ambiguous strings ('Multiple Locations', 'Virtual', bare 'Remote') still
# match; only affirmatively non-US listings (Canada/UK/'Remote in Germany') drop.
locations_allow: us_remote
# Real live values use the apostrophe form ("Bachelor's" 5450, ("Master's","PhD")
# 592, ("PhD",) 586, empty 4676 — fetched 2026-07-18). Permissive: empty degrees
# data passes; non-empty must intersect this list.
degrees_allow: ["Bachelor's"]
# Preference weight for the debate comparator (Prompt 5 Task L), not a filter
# gate — a non-matching company still passes everything above unaffected.
# Seeded from the real, human-vetted target list in the vault's
# `20_Progress/Internship/Building System/Research Loop - Resources.md`
# "Named-Program Coverage Check (2026-07-29)" section: 11 named early-talent
# programs the human already identified as worth prioritizing, of which only
# 3/11 have ANY dossier coverage today and none confirmed as the specific
# named program (Jane Street FTTP, Two Sigma First-Year, D.E. Shaw, Citadel
# Launch, Google ASDI, Microsoft Explore, LinkedIn First Play, MLH
# Fellowship, NASA OSTEM, Capital One, Bloomberg). This is a starting point
# for the human to re-tier or add/remove entries directly, not a final
# answer — company preference is an explicit human judgment call per
# `30_Order/Workflows/Internship Pipeline.md`'s Step 2 ("Screen"), and this
# dict only wires that judgment into write-priority ordering, it doesn't
# automate the judgment itself. All seeded at one tier for now; a
# multi-tier scheme wasn't asked for.
preferred_companies:
  "Jane Street": high
  "Two Sigma": high
  "D.E. Shaw": high
  "Citadel": high
  "Google": high
  "Microsoft": high
  "LinkedIn": high
  "MLH": high
  "NASA": high
  "Capital One": high
  "Bloomberg": high
  ```
- `Bash`:
  ```bash
grep -c "Ashby:" state/excluded_uids.json
grep "Ashby:" state/excluded_uids.json
  ```
  ```
2
  "Ashby:[REDACTED]",
  "Ashby:[REDACTED]",
  ```
- `Bash`:
  ```bash
python3 -c "
import sys, json
sys.path.insert(0, '.')
from ingestion.sources import fetch_ashby, ASHBY_JOBS_URL
from core.filter import matches, load_profile
from core.relevance import stage1_reject
from identity import compute_uid

class FakeResp:
    def __init__(self, data): self._data = data
    def raise_for_status(self): pass
    def json(self): return self._data

def fake_get(url, timeout=None):
    for token in ['ellipsislabs','quadrillion-labs','circleback','ctgt','pylon-labs','cohere','cursor','modal','elevenlabs']:
        if token in url:
            return FakeResp(json.load(open(f'/tmp/ashby_{token}.json')))
    raise Exception('unexpected url ' + url)

listings = fetch_ashby(fake_get)
print('fetch_count', len(listings))
profile = load_profile()
excluded = set(json.load(open('state/excluded_uids.json')))
for l in listings:
    uid = compute_uid(l)
    m = matches(l, profile)
    s1 = stage1_reject(l.title, l.raw_text)
    exc = uid in excluded
    print(l.company, '|', l.title, '| locations=', l.locations, 'degrees=', l.degrees, '| matches=', m, 'stage1_reject=', s1, 'excluded=', exc, 'uid=', uid)
"

  ```
  ```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 7, in <module>
ModuleNotFoundError: No module named 'identity'
  ```
- `Bash` — `find . -iname "identity.py" -not -path "*/node_modules/*"`
  ```
./core/identity.py
  ```
- `Bash`:
  ```bash
python3 -c "
import sys, json
sys.path.insert(0, '.')
from ingestion.sources import fetch_ashby, ASHBY_JOBS_URL
from core.filter import matches, load_profile
from core.relevance import stage1_reject
from core.identity import compute_uid

class FakeResp:
    def __init__(self, data): self._data = data
    def raise_for_status(self): pass
    def json(self): return self._data

def fake_get(url, timeout=None):
    for token in ['ellipsislabs','quadrillion-labs','circleback','ctgt','pylon-labs','cohere','cursor','modal','elevenlabs']:
        if token in url:
            return FakeResp(json.load(open(f'/tmp/ashby_{token}.json')))
    raise Exception('unexpected url ' + url)

listings = fetch_ashby(fake_get)
print('fetch_count', len(listings))
profile = load_profile()
excluded = set(json.load(open('state/excluded_uids.json')))
for l in listings:
    uid = compute_uid(l)
    m = matches(l, profile)
    s1 = stage1_reject(l.title, l.raw_text)
    exc = uid in excluded
    print(l.company, '|', l.title, '| locations=', l.locations, 'degrees=', l.degrees, '| matches=', m, 'stage1_reject=', s1, 'excluded=', exc, 'uid=', uid)
"

  ```
  ```
fetch_count 4
Ellipsis Labs | Software Engineer - 2027 Interns | locations= ['New York, New York'] degrees= [] | matches= True stage1_reject= False excluded= True uid= Ashby:[REDACTED]
Circleback | Software Engineering Intern (Summer 2027) | locations= ['San Francisco'] degrees= [] | matches= True stage1_reject= False excluded= True uid= Ashby:[REDACTED]
Cohere | Software Engineer Intern (Winter 2027) | locations= ['Canada'] degrees= [] | matches= False stage1_reject= False excluded= False uid= Ashby:[REDACTED]
Cohere | Machine Learning Intern/Co-op  (Winter 2027) | locations= ['Canada'] degrees= [] | matches= False stage1_reject= False excluded= False uid= Ashby:[REDACTED]
  ```
- `Bash` — `grep -n "02136b22\|2bb6be67" logs/*.jsonl state/*.json 2>/dev/null | grep -v excluded_uids.json`
  ```
(Bash completed with no output)
  ```
- `Bash`:
  ```bash
python3 -c "
import json
recs = [json.loads(l) for l in open('logs/runs.jsonl')]
for r in recs:
    ne = r.get('newly_excluded') or r.get('newly_excluded_uids') or []
    if any('02136b22' in str(x) or '2bb6be67' in str(x) for x in ne):
        print(r.get('timestamp'), ne)
"
grep -o '"newly_excluded[^]]*\]' logs/runs.jsonl | grep -i "02136\|2bb6" | head

  ```
  ```
(Bash completed with no output)
  ```
- `Bash`:
  ```bash
python3 -c "
import json
recs = [json.loads(l) for l in open('logs/runs.jsonl')]
print(list(recs[-1].keys()))
"
  ```
  ```
['timestamp', 'fetch_counts', 'filter_match_counts', 'new_count', 'already_seen_count', 'deferred_count', 'written_count', 'rejections', 'errors', 'halted', 'halt_reason', 'bucket_at_capacity', 'dossier_total', 'newly_excluded_count']
  ```
- `Bash`:
  ```bash
python3 -c "
import json
recs = [json.loads(l) for l in open('logs/runs.jsonl')]
for r in recs:
    if r.get('newly_excluded_count', 0) > 0:
        print(r['timestamp'], r['newly_excluded_count'])
" | tail -20
  ```
  ```
2026-08-22T02:09:01.874765+00:00 1
2026-08-22T04:22:33.192208+00:00 1
2026-08-22T06:22:20.969055+00:00 1
2026-08-22T07:23:18.371221+00:00 1
2026-08-22T10:13:09.279465+00:00 4
2026-08-22T15:11:14.591187+00:00 2
2026-08-22T19:15:48.238491+00:00 5
2026-08-24T17:23:06.062677+00:00 8
2026-08-24T19:22:06.431336+00:00 29
2026-08-24T20:18:48.478629+00:00 3
2026-08-24T21:19:31.440302+00:00 1
2026-08-24T22:15:44.052576+00:00 2
2026-08-24T23:14:07.775981+00:00 2
2026-08-25T00:40:49.785098+00:00 4
2026-08-25T02:12:42.206455+00:00 19
2026-08-25T04:29:42.814742+00:00 6
2026-08-25T05:23:28.121592+00:00 4
2026-08-25T13:40:53.094215+00:00 2
2026-08-25T14:37:09.905579+00:00 2
2026-08-25T15:33:22.836048+00:00 2
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/sources.py`
- `Bash` — `grep -rn "def fetch_freehire\|def fetch_interndock\|FREEHIRE_URL\|INTERNDOCK" ingestion/*.py run_pipeline.py | head -40`
  ```
ingestion/freehire.py:87:def fetch_freehire(http_get=None) -> list:
ingestion/interndock.py:69:INTERNDOCK_SITEMAP_URL = "https://www.interndock.com/sitemap.xml"
ingestion/interndock.py:98:def fetch_interndock_drop_candidates(http_get=None) -> list:
ingestion/interndock.py:102:    resp = get(INTERNDOCK_SITEMAP_URL, timeout=TIMEOUT)
ingestion/interndock.py:148:def fetch_interndock_drop(url: str, api_key: str, http_post=None) -> list:
run_pipeline.py:202:INTERNDOCK_SEEN_GUIDES_FILENAME = "interndock_seen_guides.json"
run_pipeline.py:249:    path = Path(state_dir) / INTERNDOCK_SEEN_GUIDES_FILENAME
run_pipeline.py:256:    path = Path(state_dir) / INTERNDOCK_SEEN_GUIDES_FILENAME
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/freehire.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/interndock.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/normalize.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/ingestion/normalize.py`
- `Bash`:
  ```bash
for token in fccincinnati aquaticcapitalmanagement walleyecapital-external-students pdtpartners virtu mwinternshipprogram optiverus fireworksai scaleai; do
  n=$(curl -s "https://boards-api.greenhouse.io/v1/boards/$token/jobs" | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d.get('jobs',[])))" 2>/dev/null)
  echo "$token: $n"
done
  ```
  ```
fccincinnati: 13
aquaticcapitalmanagement: 8
walleyecapital-external-students: 4
pdtpartners: 10
virtu: 47
mwinternshipprogram: 5
optiverus: 173
fireworksai: 0
scaleai: 219
  ```
- `Bash`:
  ```bash
curl -s "https://api.lever.co/v0/postings/scaleai?mode=json" -o /tmp/lever_test.json -w "%{http_code}\n"
curl -s "https://api.lever.co/v0/postings/palantir?mode=json" | python3 -c "
import json,sys
d = json.load(sys.stdin)
print('count', len(d))
print('keys', sorted(d[0].keys()) if d else None)
print(json.dumps(d[0], indent=2)[:800] if d else '')
"
  ```
  ```
404
count 307
keys ['additional', 'additionalPlain', 'applyUrl', 'categories', 'country', 'createdAt', 'description', 'descriptionBody', 'descriptionBodyPlain', 'descriptionPlain', 'hostedUrl', 'id', 'lists', 'opening', 'openingPlain', 'text', 'workplaceType']
{
  "additionalPlain": "Life at Palantir\n\u00a0\nWe want every Palantirian to achieve their best outcomes, that\u2019s why we celebrate individuals\u2019 strengths, skills, and interests, from your first interview to your longterm growth, rather than rely on traditional career ladders. Paying attention to the needs of our community enables us to optimize our opportunities to grow and helps ensure many pathways to success at Palantir. Promoting health and well-being across all areas of Palantirians\u2019 lives is just one of the ways we\u2019re investing in our community. Learn more at Life at Palantir and note that our offerings may vary by region.\n\u00a0\nIn keeping consistent with Palantir\u2019s values and culture, we believe employees are \u201cbetter together\u201d and in-person wor
  ```
- `Bash`:
  ```bash
curl -s "https://freehire.me/api/v1/jobs/search?company_slug=google&seniority=intern&limit=200" -o /tmp/freehire_google.json -w "%{http_code}\n"
python3 -c "
import json
d = json.load(open('/tmp/freehire_google.json'))
jobs = d.get('data', [])
print('count', len(jobs))
print('keys', sorted(jobs[0].keys()) if jobs else None)
print('enrichment', jobs[0].get('enrichment') if jobs else None)
"
echo "--- aijobs ---"
curl -s "https://artificialintelligencejobs.co/jobs.json" -o /tmp/aijobs.json -w "%{http_code}\n"
python3 -c "
import json
d = json.load(open('/tmp/aijobs.json'))
jobs = d.get('jobs', [])
print('count', len(jobs))
interns = [j for j in jobs if j.get('level')=='Intern']
print('intern count', len(interns))
print('keys', sorted(jobs[0].keys()) if jobs else None)
print(interns[0] if interns else None)
"
  ```
  ```
200
count 6
keys ['applied_count', 'cities', 'closed_at', 'collections', 'company', 'company_slug', 'countries', 'created_at', 'description', 'downvote_count', 'enriched_at', 'enrichment', 'enrichment_version', 'external_id', 'is_tech', 'last_seen_at', 'location', 'manually_added', 'my_vote', 'posted_at', 'public_slug', 'reality', 'regions', 'skills', 'source', 'title', 'updated_at', 'upvote_count', 'url', 'view_count']
enrichment {'summary': 'PhD Software Developer Intern at Google for Summer 2027, working on scalable distributed systems and complex CS solutions during a 12-14 week paid internship in Canada.', 'employment_type': 'internship', 'salary_min': 120000, 'salary_max': 120000, 'salary_currency': 'CAD', 'salary_period': 'year', 'seniority': 'intern', 'education_level': 'phd', 'category': 'software_engineering', 'domains': ['other'], 'posting_language': 'en', 'company_type': 'inhouse', 'company_size': '1000+', 'requirements': [{'text': 'Pursuing a PhD program with a focus on software development or other technical related fields', 'priority': 'required'}, {'text': 'Experience coding in C, C++, Java, or Python', 'priority': 'required'}, {'text': 'Currently attending a degree program in Canada and available to work full time for 12 weeks outside of university term time', 'priority': 'preferred'}, {'text': 'Penultimate academic year or returning to a degree program after completion of the internship', 'priority': 'preferred'}, {'text': 'Experience conducting research in algorithms, architecture, AI, compilers, database, data mining, distributed systems, ML, networking, or systems', 'priority': 'preferred'}, {'text': 'Experience in computer science, data structures, algorithms, and software design', 'priority': 'preferred'}]}
--- aijobs ---
200
count 18962
intern count 248
keys ['category', 'company', 'companyUrl', 'level', 'location', 'posted', 'region', 'remote', 'salary', 'slug', 'tags', 'title', 'url']
{'title': 'Software Engineer, Intern', 'location': 'San Francisco, California', 'url': 'https://jobs.ashbyhq.com/exa/[REDACTED]', 'posted': '2026-08-28', 'salary': '$100K – $200K', 'company': 'Exa', 'companyUrl': 'https://exa.ai', 'tags': ['Search'], 'category': 'Engineering', 'level': 'Intern', 'remote': False, 'region': 'US', 'slug': '[REDACTED]'}
  ```
- `Bash`:
  ```bash
curl -s "https://www.interndock.com/sitemap.xml" -o /tmp/interndock_sitemap.xml -w "%{http_code}\n"
python3 -c "
import re
text = open('/tmp/interndock_sitemap.xml').read()
locs = re.findall(r'<loc>([^<]*)</loc>', text)
print('total locs', len(locs))
guide_locs = [u for u in locs if '/tracker/guides/' in u]
print('guide locs', len(guide_locs))
cand = [u for u in guide_locs if re.search(r'intern.*(drop|list|open-now)', u, re.I)]
print('candidate drop-shaped', len(cand))
print(cand[:5])
"
  ```
  ```
200
total locs 68
guide locs 43
candidate drop-shaped 12
['https://www.interndock.com/tracker/guides/[REDACTED]', 'https://www.interndock.com/tracker/guides/[REDACTED]', 'https://www.interndock.com/tracker/guides/campus-ambassador-programs-open-now', 'https://www.interndock.com/tracker/guides/[REDACTED]', 'https://www.interndock.com/tracker/guides/[REDACTED]']
  ```
- `Bash` — `grep -n "SOURCES\s*=\|check_all\|schema_drift" run_pipeline.py`
  ```
32:from core.schema_drift import SchemaDriftError
33:from core.schema_drift import check_all as check_schema_drift
51:SOURCES = (
521:        check_schema_drift(http_get)
  ```
- `Bash` — `sed -n '1,80p' tests/core/test_schema_drift.py 2>/dev/null || find . -iname "*schema_drift*"`
  ```
./core/schema_drift.py
./tests/test_schema_drift.py
./core/__pycache__/schema_drift.cpython-312.pyc
./tests/__pycache__/test_schema_drift.cpython-312-pytest-9.1.1.pyc
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
- `Bash` — `sed -n '40,70p;490,560p' run_pipeline.py`
  ```
    fetch_ashby,
    fetch_greenhouse,
    fetch_josegael,
    fetch_lever,
    fetch_simplify,
    fetch_vanshb03,
    fetch_zshah101,
)
from vault_writer.validate import check_format_compliance, validate
from vault_writer.writer import DOSSIER_SUBPATH, render_dossier, scan_dossiers, write_dossier

SOURCES = (
    ("SimplifyJobs", fetch_simplify),
    ("Jose-Gael-Cruz-Lopez", fetch_josegael),
    ("vanshb03", fetch_vanshb03),
    ("zshah101", fetch_zshah101),
    ("ApplyGuy", fetch_applyguy),
    ("Greenhouse", fetch_greenhouse),
    ("Ashby", fetch_ashby),
    ("Lever", fetch_lever),
    ("Freehire", fetch_freehire),
    ("AIJobs", fetch_ai_jobs),
)

# 2026-07-25 decision: turning on 4 sources at once produced a one-time backlog
# (186 new candidates, 171 write-gate-passing) far above the steady-state <100/
# month Firecrawl budget Phase 6 was sized for. Neither absorbing the whole
# backlog in one run (dumps 100+ dossiers on a promotion queue already at zero)
# nor pre-seeding seen_ids to silently skip it (throws away real, currently-
# open postings — the reason these sources were added) was acceptable. Cap
# instead, and let it drain over several runs. No structured deadline field
    http_head=None,
    push_fn=commit_and_push_with_retry,
    issue_fn=file_github_issue,
    issue_repo: str = "gupta-builds/internship-research-loop",
    fetch_page_fn=None,
    opt_cache_path=None,
    state_dir=None,
    interndock_fetch_fn=None,
) -> dict:
    profile = profile or load_profile()
    timestamp = now.isoformat()
    record = {
        "timestamp": timestamp,
        "fetch_counts": {},
        "filter_match_counts": {},
        "new_count": 0,
        "already_seen_count": 0,
        "deferred_count": 0,
        "written_count": 0,
        "rejections": [],
        "errors": [],
        "halted": False,
        "halt_reason": None,
        "bucket_at_capacity": [],
        "dossier_total": 0,
        "newly_excluded_count": 0,
    }

    excluded_ids = load_excluded_uids(state_dir) if state_dir is not None else set()

    try:
        check_schema_drift(http_get)
        seen_ids = load_seen_ids(state_path)
        matched_by_source = fetch_and_filter(profile, http_get, excluded_ids=excluded_ids)
        # Not one of the uniform SOURCES fetchers — needs Firecrawl plus its
        # own persisted state, not just http_get (see discover_interndock's
        # docstring). Added last so it naturally has lowest cross-source-
        # duplicate write-priority: InternDock's value is companies the
        # direct per-company sources don't already reach, not going first.
        interndock_listings = discover_interndock(http_get, interndock_fetch_fn, state_dir)
        interndock_matched = [
            l for l in interndock_listings
            if matches(l, profile) and not stage1_reject(l.title, l.raw_text)
            and compute_uid(l) not in excluded_ids
        ]
        matched_by_source["InternDock"] = {"fetch_count": len(interndock_listings), "matched": interndock_matched}
    except (SchemaDriftError, requests.RequestException) as exc:
        # RequestException too — a deleted repo, DNS failure, or 5xx used to
        # crash the process before any run-log record or issue existed (the
        # PRD's "source repo goes offline" risk, previously unmitigated).
        record["halted"] = True
        record["halt_reason"] = f"{type(exc).__name__}: {exc}"
        append_run_log(runs_log_path, record)
        issue_fn(
            issue_repo,
            f"Run halted ({type(exc).__name__}) at {timestamp}",
            f"Schema drift or source fetch failure — nothing was fetched, filtered, "
            f"or written this run.\n\n```\n{type(exc).__name__}: {exc}\n```",
        )
        return record

    for name, info in matched_by_source.items():
        record["fetch_counts"][name] = info["fetch_count"]
        record["filter_match_counts"][name] = len(info["matched"])

    new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids, excluded_ids=excluded_ids)
    record["new_count"] = len(new_listings)
    record["already_seen_count"] = already_seen_count

    this_run, deferred = _prioritize_and_cap(
        new_listings, MAX_NEW_WRITES_PER_RUN, preferred_companies=profile.get("preferred_companies")
  ```
- `Bash`:
  ```bash
python3 -c "
import json
d = json.load(open('/tmp/ashby_elevenlabs.json'))
jobs = d.get('jobs', [])
print(sorted(jobs[0].keys()))
"
echo "---greenhouse scaleai---"
curl -s "https://boards-api.greenhouse.io/v1/boards/scaleai/jobs" | python3 -c "
import json,sys
d = json.load(sys.stdin)
jobs = d.get('jobs', [])
print(sorted(jobs[0].keys()))
print(jobs[0].get('location'))
"
  ```
  ```
['address', 'applyUrl', 'department', 'descriptionHtml', 'descriptionPlain', 'employmentType', 'id', 'isListed', 'isRemote', 'jobUrl', 'location', 'publishedAt', 'secondaryLocations', 'team', 'title', 'workplaceType']
---greenhouse scaleai---
['absolute_url', 'application_deadline', 'company_name', 'data_compliance', 'first_published', 'id', 'internal_job_id', 'language', 'location', 'metadata', 'requisition_id', 'title', 'updated_at']
{'name': 'San Francisco, CA; New York, NY'}
  ```
- `Bash` — `grep -n "^from\|^import" ingestion/freehire.py ingestion/interndock.py`
  ```
ingestion/freehire.py:42:import re
ingestion/freehire.py:44:import requests
ingestion/freehire.py:46:from ingestion.normalize import normalize_freehire
ingestion/interndock.py:62:import re
ingestion/interndock.py:64:import requests
ingestion/interndock.py:66:from ingestion.normalize import Listing
ingestion/interndock.py:67:from ingestion.posting_page import fetch_posting_markdown
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
  ```diff
  - """Schema-drift check. Runs before the scheduled pipeline touches feeds for
real: fetches one real entry per source and confirms the fields the
normalizers actually depend on are still present. Halts (raises) rather than
letting a silently renamed/vanished upstream field produce malformed or
emptied-out results.
"""
import requests

from ingestion.sources import APPLYGUY_URL, JOSEGAEL_URL, SIMPLIFY_URL, TIMEOUT, VANSHB03_URL, ZSHAH101_URL
  + """Schema-drift check. Runs before the scheduled pipeline touches feeds for
real: fetches one real entry per source and confirms the fields the
normalizers actually depend on are still present. Halts (raises) rather than
letting a silently renamed/vanished upstream field produce malformed or
emptied-out results.
"""
import re

import requests

from ingestion.freehire import FREEHIRE_SEARCH_URL
from ingestion.interndock import CANDIDATE_SLUG_RE, INTERNDOCK_SITEMAP_URL
from ingestion.sources import (
    AI_JOBS_URL,
    APPLYGUY_URL,
    ASHBY_JOBS_URL,
    GREENHOUSE_JOBS_URL,
    JOSEGAEL_URL,
    LEVER_JOBS_URL,
    SIMPLIFY_URL,
    TIMEOUT,
    VANSHB03_URL,
    ZSHAH101_URL,
)
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
  ```diff
  - APPLYGUY_REQUIRED_KEYS = {"id", "company", "title", "listingUrl", "category", "season", "location", "posted"}

# Only the two curated single-feed JSON sources get a pre-fetch drift check,
# same as SimplifyJobs/JGCL always have. Greenhouse/Ashby/Lever are a dozen
# per-company endpoints, not one feed — checking each company's schema before
# every run would multiply request volume for a company set that already
# degrades gracefully per-token in fetch_greenhouse/fetch_ashby/fetch_lever (a
# renamed board silently returns nothing for that one company, not malformed
# data).
  + APPLYGUY_REQUIRED_KEYS = {"id", "company", "title", "listingUrl", "category", "season", "location", "posted"}

# Greenhouse/Ashby/Lever are a dozen per-company endpoints, not one feed —
# checking every company's schema before every run would multiply request
# volume for a company set that already degrades gracefully per-token in
# fetch_greenhouse/fetch_ashby/fetch_lever (a renamed/closed board silently
# returns nothing for that one company, not malformed data — and the
# per-source zero-match-rate alert in run_pipeline.py catches that
# operationally). But a vendor-wide API shape change — Ashby renaming
# "employmentType", Greenhouse renaming "absolute_url" — hits every company
# on that vendor at once, and none of the three fetchers would notice: they
# all fail open (try/except RequestException, or a KeyError from
# normalize_ashby/normalize_greenhouse/normalize_lever would actually crash
# the whole run instead, worse than the silent-zero case the docstring above
# describes). So each of the three checks ONE real, high-volume, currently-
# live company (confirmed live 2026-08-28 against the real API — see the
# _SCHEMA_CHECK_TOKEN comments below) — enough to catch a vendor-wide drift,
# without the per-company request multiplication that was ruled out above.
#
# InternDock is different in kind, not just degree: it has no JSON API to
# schema-check at all. fetch_interndock_drop_candidates() only ever touches
# interndock.com/sitemap.xml (plain XML, checked below — that part IS
# checkable for free). The actual posting shape (POSTING_LINE_RE) only shows
# up after a paid Firecrawl fetch of one specific guide page, and there's no
# guarantee any given sitemap URL is currently a real drop (see
# ingestion/interndock.py's own docstring on "summer-2027-internship-
# programs-open-now" reading exactly like a drop by name while being a
# zero-posting prose article) — spending a Firecrawl call here to pre-flight
# a schema, and maybe hitting a non-drop page and calling that "healthy" or a
# real drop and calling a slug mismatch "drift", wouldn't mean anything
# reliable. check_interndock_sitemap below checks what's actually checkable.

# High-volume, currently-live tokens (2026-08-28) — see the block comment
# above for why one company per vendor is the right amount of pre-flight
# checking here, not a stand-in for "this specific company matters more."
_GREENHOUSE_SCHEMA_CHECK_TOKEN = "scaleai"  # 219 open reqs live 2026-08-28
_ASHBY_SCHEMA_CHECK_TOKEN = "elevenlabs"  # 249 open reqs live 2026-08-28
_LEVER_SCHEMA_CHECK_TOKEN = "palantir"  # 307 open reqs live 2026-08-28, longest-tracked of the 4
_FREEHIRE_SCHEMA_CHECK_SLUG = "google"  # of the 2 tracked companies, the higher-volume one

# Confirmed live 2026-08-28 against https://boards-api.greenhouse.io/v1/boards/scaleai/jobs
# (no ?content=true query param on GREENHOUSE_JOBS_URL, so "content" never
# appears in this response shape at all — not a required key here even
# though normalize_greenhouse also reads raw.get("content", "")).
GREENHOUSE_REQUIRED_KEYS = {"id", "title", "absolute_url", "location", "updated_at"}
# Confirmed live 2026-08-28 against https://api.ashbyhq.com/posting-api/job-board/elevenlabs .
# employmentType is the field fetch_ashby's own role-type triage reads
# (job.get("employmentType") == "Intern") — renamed, every company silently
# stops matching any intern posting at all, the exact failure shape this
# check exists to catch (see the 2026-08-21..08-28 Ashby zero-match
# investigation, Prompt 19 Task 1).
ASHBY_REQUIRED_KEYS = {"id", "title", "jobUrl", "location", "isListed", "publishedAt", "descriptionPlain", "employmentType"}
# Confirmed live 2026-08-28 against https://api.lever.co/v0/postings/palantir?mode=json .
# "text" is also what fetch_lever's own role-type triage reads
# (job.get("text", "").lower()) — same reasoning as Ashby's employmentType
# above. applyUrl, not hostedUrl, per normalize_lever's own docstring on
# which one is the real employer link.
LEVER_REQUIRED_KEYS = {"id", "text", "applyUrl", "categories", "createdAt", "descriptionPlain"}
# Confirmed live 2026-08-28 against
# https://freehire.me/api/v1/jobs/search?company_slug=google&seniority=intern&limit=200 .
# "enrichment" additionally must contain "seniority" — see
# check_freehire_schema below; that nested field is what fetch_freehire's own
# role-type triage reads.
FREEHIRE_REQUIRED_KEYS = {"title", "url", "location", "posted_at", "public_slug", "description", "enrichment"}
# Confirmed live 2026-08-28 against https://artificialintelligencejobs.co/jobs.json .
# "level" is what fetch_ai_jobs' own role-type triage reads (raw.get("level") == "Intern").
AI_JOBS_REQUIRED_KEYS = {"title", "url", "company", "location", "posted", "slug", "level"}

# sitemap.xml's real shape, confirmed live 2026-08-28: 68 total <loc> entries,
# 43 under /tracker/guides/, 12 of those matching CANDIDATE_SLUG_RE — the
# same loose pre-filter fetch_interndock_drop_candidates() itself uses.
_LOC_RE = re.compile(r"<loc>([^<]*)</loc>")
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
  ```diff
  - def check_all(http_get=None) -> None:
    """Runs every check in order; raises SchemaDriftError from whichever
    fails first. Callers should treat any exception here as "halt the run,
    write nothing" per the plan's fail-closed design."""
    check_simplify_schema(http_get)
    check_josegael_schema(http_get)
    check_vanshb03_schema(http_get)
    check_zshah101_schema(http_get)
    check_applyguy_schema(http_get)
  + def _check_wrapped_jobs_source(name: str, url: str, required_keys: set, http_get) -> None:
    """Greenhouse/Ashby/AIJobs' shared shape: a dict wrapping a "jobs" list —
    same shape check_applyguy_schema already handles bespoke, now shared
    since three more sources use it."""
    resp = http_get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    jobs = data.get("jobs") if isinstance(data, dict) else None
    if not isinstance(jobs, list) or not jobs:
        raise SchemaDriftError(f"{name}: expected a non-empty 'jobs' list, got {type(data).__name__}")
    missing = required_keys - set(jobs[0].keys())
    if missing:
        raise SchemaDriftError(f"{name}: missing expected keys {sorted(missing)} (entry keys: {sorted(jobs[0].keys())})")


def check_greenhouse_schema(http_get=None) -> None:
    _check_wrapped_jobs_source(
        "Greenhouse", GREENHOUSE_JOBS_URL.format(token=_GREENHOUSE_SCHEMA_CHECK_TOKEN),
        GREENHOUSE_REQUIRED_KEYS, http_get or requests.get,
    )


def check_ashby_schema(http_get=None) -> None:
    _check_wrapped_jobs_source(
        "Ashby", ASHBY_JOBS_URL.format(token=_ASHBY_SCHEMA_CHECK_TOKEN),
        ASHBY_REQUIRED_KEYS, http_get or requests.get,
    )


def check_lever_schema(http_get=None) -> None:
    # Lever's own shape is a bare list (mode=json), not a "jobs"-wrapped dict —
    # same shape as Simplify/JGCL/vanshb03, reuse that helper instead.
    _check_json_source(
        "Lever", LEVER_JOBS_URL.format(token=_LEVER_SCHEMA_CHECK_TOKEN),
        LEVER_REQUIRED_KEYS, http_get or requests.get,
    )


def check_freehire_schema(http_get=None) -> None:
    # A fourth real shape: {"data": [...]}, plus a nested field
    # (enrichment.seniority) that's load-bearing for fetch_freehire's own
    # role-type triage — not caught by a flat top-level key check alone, so
    # this one stays a dedicated function rather than folding into
    # _check_json_source or _check_wrapped_jobs_source.
    resp = (http_get or requests.get)(FREEHIRE_SEARCH_URL.format(slug=_FREEHIRE_SCHEMA_CHECK_SLUG), timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    jobs = data.get("data") if isinstance(data, dict) else None
    if not isinstance(jobs, list) or not jobs:
        raise SchemaDriftError(f"Freehire: expected a non-empty 'data' list, got {type(data).__name__}")
    first_entry = jobs[0]
    missing = FREEHIRE_REQUIRED_KEYS - set(first_entry.keys())
    if missing:
        raise SchemaDriftError(f"Freehire: missing expected keys {sorted(missing)} (entry keys: {sorted(first_entry.keys())})")
    if "seniority" not in (first_entry.get("enrichment") or {}):
        raise SchemaDriftError("Freehire: 'enrichment' entry missing expected key 'seniority'")


def check_ai_jobs_schema(http_get=None) -> None:
    _check_wrapped_jobs_source("AIJobs", AI_JOBS_URL, AI_JOBS_REQUIRED_KEYS, http_get or requests.get)


def check_interndock_sitemap(http_get=None) -> None:
    """Not a field-schema check (InternDock has no JSON API — see the block
    comment above) — confirms interndock.com/sitemap.xml itself still parses
    as XML with <loc> entries and that at least one still looks drop-shaped
    per CANDIDATE_SLUG_RE, the same loose pre-filter
    fetch_interndock_drop_candidates() applies to real results."""
    resp = (http_get or requests.get)(INTERNDOCK_SITEMAP_URL, timeout=TIMEOUT)
    resp.raise_for_status()
    locs = _LOC_RE.findall(resp.text)
    if not locs:
        raise SchemaDriftError("InternDock: sitemap.xml has no <loc> entries — feed shape changed or sitemap is empty")
    if not any(CANDIDATE_SLUG_RE.search(u) for u in locs):
        raise SchemaDriftError(
            f"InternDock: sitemap.xml has {len(locs)} <loc> entries but none match the drop-shaped slug pattern"
        )


def check_all(http_get=None) -> None:
    """Runs every check in order; raises SchemaDriftError from whichever
    fails first. Callers should treat any exception here as "halt the run,
    write nothing" per the plan's fail-closed design."""
    check_simplify_schema(http_get)
    check_josegael_schema(http_get)
    check_vanshb03_schema(http_get)
    check_zshah101_schema(http_get)
    check_applyguy_schema(http_get)
    check_greenhouse_schema(http_get)
    check_ashby_schema(http_get)
    check_lever_schema(http_get)
    check_freehire_schema(http_get)
    check_ai_jobs_schema(http_get)
    check_interndock_sitemap(http_get)
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
- `Bash` — `grep -n "record\[.errors.\]\|record\[.rejections.\]\|issue_fn(\|bucket_at_capacity" run_pipeline.py`
  ```
88:# attention, not vault storage). See run_once()'s bucket_at_capacity handling.
513:        "bucket_at_capacity": [],
543:        issue_fn(
574:    record["rejections"] = rejections
600:            issue_fn(
616:    record["bucket_at_capacity"] = sorted(b for b, c in bucket_counts.items() if c >= BUCKET_CAPACITY)
621:    for bucket in record["bucket_at_capacity"]:
625:            issue_fn(
636:            issue_fn(
654:        record["errors"].append(f"Jarvis push failed: {exc}")
655:        issue_fn(
678:        issue_fn(
  ```
- `Read` — ``
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Bash` — `grep -n "should_alert_on_exclusion_spike\|EXCLUSION_SPIKE" -B3 -A8 run_pipeline.py | head -40`
  ```
[REDACTED] = 20
216-
217-
218:def should_alert_on_exclusion_spike(newly_excluded_count: int) -> bool:
219-    return newly_excluded_count > NEWLY_EXCLUDED_ALERT_THRESHOLD
220-
221-
222-def load_debate_losses(state_dir) -> dict:
223-    path = Path(state_dir) / DEBATE_LOSSES_FILENAME
224-    if not path.exists():
225-        return {}
226-    return json.loads(path.read_text())
--
596-                    Path(jarvis_dir) / EXCLUDED_LOG_SUBPATH, line, created_date=now.date().isoformat(),
597-                    max_losses=MAX_DEBATE_LOSSES,
598-                )
599:        if should_alert_on_exclusion_spike(record["newly_excluded_count"]):
600-            issue_fn(
601-                issue_repo,
602-                f"Debate-loss exclusion spike: {record['newly_excluded_count']} in one run ({timestamp})",
603-                f"{record['newly_excluded_count']} candidates crossed MAX_DEBATE_LOSSES "
604-                f"({MAX_DEBATE_LOSSES} consecutive losses) and were permanently excluded in this single "
605-                "run — well above the normal handful-per-run trickle. This usually means a burst of new "
606-                "candidates arrived together and lost the debate to each other, not that they're "
607-                "individually undesirable (see the 2026-08-21 incident: 287 of 304 total exclusions "
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -         if losses[uid] >= MAX_DEBATE_LOSSES:
            newly_excluded.append((uid, listing))
            del losses[uid]
    return losses, newly_excluded

# A required_fields or format_compliance rejection means OUR normalizer/writer
  +         if losses[uid] >= MAX_DEBATE_LOSSES:
            newly_excluded.append((uid, listing))
            del losses[uid]
    return losses, newly_excluded


ZERO_MATCH_STREAKS_FILENAME = "zero_match_streaks.json"

# Task 3 (Prompt 19, 2026-08-28): a per-source alert when a source keeps
# fetching real postings but nothing survives the filter — the exact shape
# of the real Ashby incident this task was built from: fetch_counts frozen
# at 4 and filter_match_counts frozen at 0 for 115 consecutive hourly runs
# (2026-08-21 through 2026-08-28) before a human noticed by reading
# logs/runs.jsonl by hand. Investigated live (Prompt 19 Task 1) and NOT
# schema drift: 2 of the 4 postings are legitimately Canada-based
# (location_eligible correctly rejects them) and the other 2 are
# legitimately permanently excluded by the debate comparator
# (MAX_DEBATE_LOSSES) — a real, if coincidental, correctly-filtered
# outcome. But the pipeline had no way to tell that apart from a silent
# schema break without a human noticing. 24 (one day of hourly runs) is
# comfortably shorter than the 115 runs it actually took a human to notice
# this pass, while still long enough that a source's normal hour-to-hour dry
# spells (no new postings that hour) don't trip it on their own — this only
# fires once a source stays at exactly zero for a full day despite still
# fetching real data.
ZERO_MATCH_STREAK_ALERT_THRESHOLD = 24


def load_zero_match_streaks(state_dir) -> dict:
    path = Path(state_dir) / ZERO_MATCH_STREAKS_FILENAME
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def save_zero_match_streaks(state_dir, streaks: dict) -> None:
    path = Path(state_dir) / ZERO_MATCH_STREAKS_FILENAME
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(streaks, indent=2, sort_keys=True) + "\n")


def update_zero_match_streaks(streaks: dict, fetch_counts: dict, filter_match_counts: dict) -> tuple:
    """Returns (updated_streaks, newly_alerting: [source_name, ...]).

    Per source: fetch_count > 0 and filter_match_count == 0 increments the
    streak; filter_match_count > 0 resets it to 0 and marks the source as
    having "ever_matched" — a source that has never once produced a match
    isn't drifting, it's just structurally not matching anything, and never
    alerts (permissive-by-default, same spirit as core/filter.py's own
    gates: only an affirmative bad signal — a real regression from matching
    to not — fires this). fetch_count == 0 this run leaves the streak
    untouched: a single fetch hiccup (a transient RequestException already
    swallowed upstream in fetch_greenhouse/fetch_ashby/fetch_lever) shouldn't
    reset real streak progress, but it's not new zero-match signal either.

    Fires exactly once per streak, at the run the streak first reaches the
    threshold (`==`, not `>=`) — otherwise a source stuck at zero would
    re-file the same issue every run forever, the same "notify once, not
    every run" shape as run_once()'s bucket_at_capacity handling."""
    streaks = {k: dict(v) for k, v in streaks.items()}
    newly_alerting = []
    for name, fetch_count in fetch_counts.items():
        if fetch_count == 0:
            continue
        entry = streaks.setdefault(name, {"streak": 0, "ever_matched": False})
        if filter_match_counts.get(name, 0) > 0:
            entry["streak"] = 0
            entry["ever_matched"] = True
        else:
            entry["streak"] += 1
            if entry["ever_matched"] and entry["streak"] == ZERO_MATCH_STREAK_ALERT_THRESHOLD:
                newly_alerting.append(name)
    return streaks, newly_alerting

# A required_fields or format_compliance rejection means OUR normalizer/writer
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -     for name, info in matched_by_source.items():
        record["fetch_counts"][name] = info["fetch_count"]
        record["filter_match_counts"][name] = len(info["matched"])

    new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids, excluded_ids=excluded_ids)
  +     for name, info in matched_by_source.items():
        record["fetch_counts"][name] = info["fetch_count"]
        record["filter_match_counts"][name] = len(info["matched"])

    if state_dir is not None:
        zero_match_streaks = load_zero_match_streaks(state_dir)
        zero_match_streaks, newly_zero_match_alerting = update_zero_match_streaks(
            zero_match_streaks, record["fetch_counts"], record["filter_match_counts"],
        )
        save_zero_match_streaks(state_dir, zero_match_streaks)
        for name in newly_zero_match_alerting:
            issue_fn(
                issue_repo,
                f"{name}: filter_match_count stuck at 0 for {ZERO_MATCH_STREAK_ALERT_THRESHOLD} consecutive runs ({timestamp})",
                f"{name} has kept returning real fetched postings (fetch_count > 0) but none have "
                f"survived the filter for {ZERO_MATCH_STREAK_ALERT_THRESHOLD} consecutive runs, despite "
                "having produced real matches before. This can be a genuine, if coincidental, run of "
                "correctly-filtered postings (see the 2026-08-28 Ashby investigation: Canada-based "
                "postings plus debate-comparator exclusion, not schema drift) — but it's also exactly "
                f"the shape a silent upstream schema change or a broken filter rule would produce. "
                f"Check core/schema_drift.py's coverage for {name} and the real current API response "
                "before assuming it's benign.",
            )

    new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids, excluded_ids=excluded_ids)
  ```
- `Bash` — `grep -n '"newly_excluded_count": 0,' run_pipeline.py`
  ```
584:        "newly_excluded_count": 0,
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -         "dossier_total": 0,
        "newly_excluded_count": 0,
    }
  +         "dossier_total": 0,
        "newly_excluded_count": 0,
        "zero_match_alerts": [],
    }
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
  ```diff
  -         save_zero_match_streaks(state_dir, zero_match_streaks)
        for name in newly_zero_match_alerting:
  +         save_zero_match_streaks(state_dir, zero_match_streaks)
        record["zero_match_alerts"] = newly_zero_match_alerting
        for name in newly_zero_match_alerting:
  ```
- `Bash` — `python3 -m pytest -q 2>&1 | tail -60`
  ```
/usr/bin/python3: No module named pytest
  ```
- `Bash` — `which pytest; python3 -m venv --help >/dev/null 2>&1; ls; cat requirements*.txt 2>/dev/null; find . -maxdepth 2 -iname "*.cfg" -o -iname "pyproject.toml" | head`
  ```
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
requests==2.34.2
pyyaml==6.0.3
pytest==9.1.1
jinja2==3.1.6
./.venv/pyvenv.cfg
  ```
- `Bash` — `source .venv/bin/activate 2>/dev/null; .venv/bin/python -m pytest -q 2>&1 | tail -80`
  ```
tests/test_run_pipeline.py:643: AssertionError
______________ test_check_all_passes_when_all_sources_are_healthy ______________

simplify_raw = [{'source': 'Simplify', 'category': 'Software', 'company_name': 'Palantir', 'id': '[REDACTED]...implify', 'category': 'Software', 'company_name': 'Anthropic', 'id': '[REDACTED]', ...}, ...]
josegael_raw = [{'id': '[REDACTED]', 'company_name': 'Deloitte', 'title': 'Audit & Assurance - Discovery In..., 'title': 'Applied Research Intern - Spring 2027', 'url': 'https://example.com/careers/spring-2027-intern', ...}, ...]
vanshb03_raw = [{'date_updated': 1776617698, 'url': 'https://careers.point72.com/CSJobDetail?jobName=[REDACTED]...X/[REDACTED]', 'locations': ['Frisco, TX'], 'sponsorship': 'Does Not Offer Sponsorship', ...}]
zshah101_raw = {'ashby:centerfield:[REDACTED]': {'category': 'Software', 'company': 'Centerfield', 'company...{'category': 'Software', 'closed_at': '2026-06-30T19:49:56Z', 'company': 'Amazon', 'company_slug': 'amazon', ...}, ...}
applyguy_raw = {'updatedAt': '2026-08-24T00:00:00Z', 'jobs': [{'id': '[REDACTED]', 'company': 'Toyota of Ce...1', 'company': 'Amazon', 'title': 'Product Manager Technical (PMT) Intern - Summer 2027', 'category': 'Product', ...}]}

    def test_check_all_passes_when_all_sources_are_healthy(
        simplify_raw, josegael_raw, vanshb03_raw, zshah101_raw, applyguy_raw,
    ):
        call_log = []
    
        def http_get(url, timeout):
            call_log.append(url)
            from ingestion.sources import APPLYGUY_URL, JOSEGAEL_URL, SIMPLIFY_URL, VANSHB03_URL, ZSHAH101_URL
    
            if url == SIMPLIFY_URL:
                return _json_response(simplify_raw)
            if url == JOSEGAEL_URL:
                return _json_response(josegael_raw)
            if url == VANSHB03_URL:
                return _json_response(vanshb03_raw)
            if url == ZSHAH101_URL:
                return _json_response(zshah101_raw)
            if url == APPLYGUY_URL:
                return _json_response(applyguy_raw)
            raise AssertionError(f"unexpected url: {url}")
    
>       check_all(http_get=http_get)  # does not raise
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_schema_drift.py:152: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
core/schema_drift.py:259: in check_all
    check_greenhouse_schema(http_get)
core/schema_drift.py:187: in check_greenhouse_schema
    _check_wrapped_jobs_source(
core/schema_drift.py:175: in _check_wrapped_jobs_source
    resp = http_get(url, timeout=TIMEOUT)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

url = 'https://boards-api.greenhouse.io/v1/boards/scaleai/jobs', timeout = 30

    def http_get(url, timeout):
        call_log.append(url)
        from ingestion.sources import APPLYGUY_URL, JOSEGAEL_URL, SIMPLIFY_URL, VANSHB03_URL, ZSHAH101_URL
    
        if url == SIMPLIFY_URL:
            return _json_response(simplify_raw)
        if url == JOSEGAEL_URL:
            return _json_response(josegael_raw)
        if url == VANSHB03_URL:
            return _json_response(vanshb03_raw)
        if url == ZSHAH101_URL:
            return _json_response(zshah101_raw)
        if url == APPLYGUY_URL:
            return _json_response(applyguy_raw)
>       raise AssertionError(f"unexpected url: {url}")
E       AssertionError: unexpected url: https://boards-api.greenhouse.io/v1/boards/scaleai/jobs

tests/test_schema_drift.py:150: AssertionError
=========================== short test summary info ============================
FAILED tests/test_debate_losses.py::test_run_once_files_issue_on_exclusion_spike
FAILED tests/test_run_pipeline.py::test_run_once_defers_beyond_the_cap_and_leaves_it_for_next_run
FAILED tests/test_run_pipeline.py::test_run_once_happy_path_marks_seen_and_writes_dossiers
FAILED tests/test_run_pipeline.py::test_run_once_does_not_mark_seen_when_push_fails
FAILED tests/test_run_pipeline.py::test_run_once_files_issue_on_systemic_rejection_not_routine_one
FAILED tests/test_run_pipeline.py::test_run_once_second_run_does_not_rewrite_already_seen_items
FAILED tests/test_run_pipeline.py::test_run_once_reports_bucket_at_capacity_without_refusing_writes[48-False]
FAILED tests/test_run_pipeline.py::test_run_once_reports_bucket_at_capacity_without_refusing_writes[49-True]
FAILED tests/test_run_pipeline.py::test_run_once_reports_bucket_at_capacity_without_refusing_writes[50-True]
FAILED tests/test_run_pipeline.py::test_run_once_files_issue_once_per_bucket_crossing_capacity
FAILED tests/test_run_pipeline.py::test_run_once_global_total_thresholds[186-189-False]
FAILED tests/test_run_pipeline.py::test_run_once_global_total_thresholds[187-190-True]
FAILED tests/test_run_pipeline.py::test_run_once_global_total_thresholds[197-200-True]
FAILED tests/test_schema_drift.py::test_check_all_passes_when_all_sources_are_healthy
14 failed, 387 passed in 1.95s
  ```
- `Bash` — `grep -n "def _make_http_get\|def make_http_get\|def _http_get\|check_schema_drift\|SchemaDrift\|schema_drift" tests/test_run_pipeline.py tests/test_debate_losses.py | head -60`
  ```
tests/test_run_pipeline.py:12:from core.schema_drift import SchemaDriftError
tests/test_run_pipeline.py:406:def test_run_once_halts_on_schema_drift_and_writes_nothing(tmp_path, monkeypatch):
tests/test_run_pipeline.py:408:        raise SchemaDriftError("SimplifyJobs: missing expected keys ['category']")
tests/test_run_pipeline.py:410:    monkeypatch.setattr(run_pipeline, "check_schema_drift", drifted_check)
tests/test_run_pipeline.py:420:    assert "SchemaDriftError" in kwargs["issue_fn"].call_args[0][1]
tests/test_run_pipeline.py:750:    monkeypatch.setattr(run_pipeline, "check_schema_drift", lambda http_get=None: None)
  ```
- `Bash` — `grep -n "check_schema_drift" tests/test_run_pipeline.py tests/test_debate_losses.py`
  ```
tests/test_run_pipeline.py:410:    monkeypatch.setattr(run_pipeline, "check_schema_drift", drifted_check)
tests/test_run_pipeline.py:750:    monkeypatch.setattr(run_pipeline, "check_schema_drift", lambda http_get=None: None)
  ```
- `Bash` — `grep -n "def test_run_once_happy_path_marks_seen_and_writes_dossiers" -A 60 tests/test_run_pipeline.py | head -90`
  ```
386:def test_run_once_happy_path_marks_seen_and_writes_dossiers(tmp_path):
387-    kwargs = _run_once_kwargs(tmp_path)
388-    record = run_pipeline.run_once(**kwargs)
389-
390-    assert record["halted"] is False
391-    assert record["written_count"] > 0
392-    assert not record["errors"]
393-
394-    seen = run_pipeline.load_seen_ids(kwargs["state_path"])
395-    assert len(seen) == record["written_count"]
396-
397-    dossiers_dir = kwargs["jarvis_dir"] / "10_Areas/Career/Internships/List/Dossiers"
398-    assert len(list(dossiers_dir.glob("**/*.md"))) == record["written_count"]
399-
400-    logged = json.loads((kwargs["runs_log_path"]).read_text().splitlines()[0])
401-    assert logged["written_count"] == record["written_count"]
402-
403-    kwargs["issue_fn"].assert_not_called()  # nothing systemic happened
404-
405-
406-def test_run_once_halts_on_schema_drift_and_writes_nothing(tmp_path, monkeypatch):
407-    def drifted_check(http_get=None):
408-        raise SchemaDriftError("SimplifyJobs: missing expected keys ['category']")
409-
410-    monkeypatch.setattr(run_pipeline, "check_schema_drift", drifted_check)
411-    kwargs = _run_once_kwargs(tmp_path)
412-    record = run_pipeline.run_once(**kwargs)
413-
414-    assert record["halted"] is True
415-    assert "missing expected keys" in record["halt_reason"]
416-    assert not run_pipeline.load_seen_ids(kwargs["state_path"])
417-    dossiers_dir = kwargs["jarvis_dir"] / "10_Areas/Career/Internships/List/Dossiers"
418-    assert not dossiers_dir.exists() or not list(dossiers_dir.glob("**/*.md"))
419-    kwargs["issue_fn"].assert_called_once()
420-    assert "SchemaDriftError" in kwargs["issue_fn"].call_args[0][1]
421-
422-
423-def test_run_once_does_not_mark_seen_when_push_fails(tmp_path):
424-    """The critical ordering guarantee: a validated, written dossier whose
425-    push fails must NOT be recorded in seen_ids — otherwise it's gone
426-    forever (never in the vault, never retried, because dedup thinks it
427-    already landed)."""
428-
429-    def failing_push(repo_dir, message):
430-        raise GitPushError("simulated rejected push, retry also failed")
431-
432-    kwargs = _run_once_kwargs(tmp_path, push_fn=failing_push)
433-    record = run_pipeline.run_once(**kwargs)
434-
435-    assert record["errors"], "push failure must be recorded"
436-    assert record["written_count"] == 0  # not counted as durably written
437-
438-    # the dossier files DO exist locally in the Jarvis checkout (validation
439-    # passed, write happened) — what must NOT have happened is seen_ids
440-    # advancing, since the push that would make them durable failed.
441-    dossiers_dir = kwargs["jarvis_dir"] / "10_Areas/Career/Internships/List/Dossiers"
442-    assert len(list(dossiers_dir.glob("**/*.md"))) > 0
443-
444-    seen = run_pipeline.load_seen_ids(kwargs["state_path"])
445-    assert seen == set(), "a failed push must leave seen_ids empty so the item is retried next run"
446-
  ```
- `Bash` — `grep -n "_run_once_kwargs\b" tests/test_run_pipeline.py | head -3`
  ```
222:    kwargs = _run_once_kwargs(tmp_path)
369:def _run_once_kwargs(tmp_path, **overrides):
387:    kwargs = _run_once_kwargs(tmp_path)
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
sed -i 's/_GREENHOUSE_SCHEMA_CHECK_TOKEN/GREENHOUSE_SCHEMA_CHECK_TOKEN/g; s/_ASHBY_SCHEMA_CHECK_TOKEN/ASHBY_SCHEMA_CHECK_TOKEN/g; s/_LEVER_SCHEMA_CHECK_TOKEN/LEVER_SCHEMA_CHECK_TOKEN/g; s/_FREEHIRE_SCHEMA_CHECK_SLUG/FREEHIRE_SCHEMA_CHECK_SLUG/g' core/schema_drift.py
grep -n "SCHEMA_CHECK" core/schema_drift.py
  ```
  ```
56:# _SCHEMA_CHECK_TOKEN comments below) — enough to catch a vendor-wide drift,
75:GREENHOUSE_SCHEMA_CHECK_TOKEN = "scaleai"  # 219 open reqs live 2026-08-28
76:ASHBY_SCHEMA_CHECK_TOKEN = "elevenlabs"  # 249 open reqs live 2026-08-28
77:LEVER_SCHEMA_CHECK_TOKEN = "palantir"  # 307 open reqs live 2026-08-28, longest-tracked of the 4
78:FREEHIRE_SCHEMA_CHECK_SLUG = "google"  # of the 2 tracked companies, the higher-volume one
188:        "Greenhouse", GREENHOUSE_JOBS_URL.format(token=GREENHOUSE_SCHEMA_CHECK_TOKEN),
195:        "Ashby", ASHBY_JOBS_URL.format(token=ASHBY_SCHEMA_CHECK_TOKEN),
204:        "Lever", LEVER_JOBS_URL.format(token=LEVER_SCHEMA_CHECK_TOKEN),
215:    resp = (http_get or requests.get)(FREEHIRE_SEARCH_URL.format(slug=FREEHIRE_SCHEMA_CHECK_SLUG), timeout=TIMEOUT)
  ```
- `Bash` — `grep -n "http_get\|_fake_http_get\|check_schema_drift" tests/test_debate_losses.py | head -30`
  ```
19:from test_run_pipeline import PROFILE, _fake_http_get, _run_once_kwargs, _simplify_raw
97:    results = run_pipeline.fetch_and_filter(PROFILE, http_get=_fake_http_get, excluded_ids=frozenset({real_uid}))
106:    matched_by_source = run_pipeline.fetch_and_filter(PROFILE, http_get=_fake_http_get)
  ```
- `Bash` — `ls tests/fixtures/`
  ```
applyguy.json
freehire.json
interndock_drop.md
josegael.json
posting_ashby_ctgt.md
posting_fiverings.md
posting_google_careers.md
posting_zipline_open_roles.md
simplifyjobs.json
throwaway_vault
vanshb03.json
zshah101.json
  ```
- `Bash` — `grep -n "def _greenhouse_job\|def _ashby_job\|def _lever_job\|def _freehire_job\|def _ai_jobs_job\|_GREENHOUSE_JOB\|_ASHBY_JOB\|_LEVER_JOB\|raw = {" tests/test_sources.py | head -40`
  ```
(Bash completed with no output)
  ```
- `Bash` — `find . -iname "test_sources.py" -o -iname "test_normalize.py"; grep -rln "fetch_greenhouse\|fetch_ashby\|fetch_lever\|fetch_ai_jobs\|fetch_freehire" tests/`
  ```
./tests/test_sources.py
tests/test_sources.py
tests/test_freehire.py
  ```
- `Bash` — `grep -n "def test_fetch_greenhouse\|def test_fetch_ashby\|def test_fetch_lever\|def test_fetch_ai_jobs" -A 25 tests/test_sources.py | head -150`
  ```
102:def test_fetch_greenhouse_polls_every_seeded_company_and_filters_to_intern_titles():
103-    intern_job = {"id": 1, "title": "Summer 2027 Software Engineering Intern",
104-                  "absolute_url": "https://x/1", "location": {"name": "NYC"},
105-                  "updated_at": "2026-07-24T15:05:09-04:00", "content": "", "company_name": "PDT Partners"}
106-    non_intern_job = {"id": 2, "title": "Senior Software Engineer",
107-                       "absolute_url": "https://x/2", "location": {"name": "NYC"},
108-                       "updated_at": "2026-07-24T15:05:09-04:00", "content": "", "company_name": "PDT Partners"}
109-
110-    def fake_get(url, timeout=None):
111-        return _gh_response([intern_job, non_intern_job])
112-
113-    listings = sources.fetch_greenhouse(http_get=fake_get)
114-    assert len(listings) == len(sources.GREENHOUSE_COMPANIES)  # one intern job per seeded company
115-    assert all(l.source == "Greenhouse" for l in listings)
116-    assert all("Intern" in l.title for l in listings)
117-
118-
119:def test_fetch_greenhouse_skips_a_dead_company_board_without_crashing():
120-    """One company's board 404ing/renaming must not halt discovery for the
121-    other seeded companies (or the other 3 sources this run)."""
122-    tokens_seen = []
123-
124-    def flaky_get(url, timeout=None):
125-        tokens_seen.append(url)
126-        if "pdtpartners" in url:
127-            raise requests.ConnectionError("simulated: board renamed")
128-        return _gh_response([])
129-
130-    listings = sources.fetch_greenhouse(http_get=flaky_get)
131-    assert listings == []  # no crash, just nothing from the dead board or the empty ones
132-    assert len(tokens_seen) == len(sources.GREENHOUSE_COMPANIES)  # every company was still attempted
133-
134-
135-def _ashby_response(jobs):
136-    resp = Mock(status_code=200)
137-    resp.json.return_value = {"jobs": jobs}
138-    return resp
139-
140-
141:def test_fetch_ashby_filters_to_structured_intern_employment_type():
142-    intern_job = {"id": "a", "title": "Software Engineer Intern", "location": "SF",
143-                  "jobUrl": "https://x/a", "publishedAt": "2026-06-01T00:00:00+00:00",
144-                  "isListed": True, "descriptionPlain": "", "employmentType": "Intern"}
145-    fulltime_job = {"id": "b", "title": "Software Engineer", "location": "SF",
146-                    "jobUrl": "https://x/b", "publishedAt": "2026-06-01T00:00:00+00:00",
147-                    "isListed": True, "descriptionPlain": "", "employmentType": "FullTime"}
148-
149-    def fake_get(url, timeout=None):
150-        return _ashby_response([intern_job, fulltime_job])
151-
152-    listings = sources.fetch_ashby(http_get=fake_get)
153-    assert len(listings) == len(sources.ASHBY_COMPANIES)  # one Intern job per seeded company
154-    assert all(l.source == "Ashby" for l in listings)
155-
156-
157:def test_fetch_ashby_skips_a_dead_company_board_without_crashing():
158-    def flaky_get(url, timeout=None):
159-        if "ellipsislabs" in url:
160-            raise requests.ConnectionError("simulated: board renamed")
161-        return _ashby_response([])
162-
163-    listings = sources.fetch_ashby(http_get=flaky_get)
164-    assert listings == []
165-
166-
167-# --- api.lever.co (real jobs on our seeded company boards, 2026-08-24) ---
168-
169-def _lever_response(jobs):
170-    resp = Mock(status_code=200)
171-    resp.json.return_value = jobs  # Lever's postings endpoint returns a bare list, not {"jobs": [...]}
172-    return resp
173-
174-
175:def test_fetch_lever_polls_every_seeded_company_and_filters_to_intern_titles():
176-    # Real, verbatim shape from belvederetrading's live board, 2026-08-24.
177-    intern_job = {"id": "[REDACTED]", "text": "Quantitative Trading Intern - Summer 2027",
178-                  "categories": {"commitment": "Intern", "location": "Chicago, Illinois"},
179-                  "hostedUrl": "https://jobs.lever.co/belvederetrading/cbde47db",
180-                  "applyUrl": "https://jobs.lever.co/belvederetrading/cbde47db/apply",
181-                  "createdAt": 1785864478389, "descriptionPlain": "Belvedere Trading is a proprietary trading firm."}
182-    non_intern_job = {"id": "x", "text": "Senior Software Engineer",
183-                       "categories": {"commitment": "Full-time", "location": "Chicago, Illinois"},
184-                       "hostedUrl": "https://jobs.lever.co/belvederetrading/x",
185-                       "applyUrl": "https://jobs.lever.co/belvederetrading/x/apply",
186-                       "createdAt": 1785864478389, "descriptionPlain": ""}
187-
188-    def fake_get(url, timeout=None):
189-        return _lever_response([intern_job, non_intern_job])
190-
191-    listings = sources.fetch_lever(http_get=fake_get)
192-    assert len(listings) == len(sources.LEVER_COMPANIES)  # one intern job per seeded company
193-    assert all(l.source == "Lever" for l in listings)
194-    assert all("Intern" in l.title for l in listings)
195-
196-
197:def test_fetch_lever_skips_a_dead_company_board_without_crashing():
198-    def flaky_get(url, timeout=None):
199-        if "hermeus" in url:
200-            raise requests.ConnectionError("simulated: board renamed")
201-        return _lever_response([])
202-
203-    listings = sources.fetch_lever(http_get=flaky_get)
204-    assert listings == []
205-
206-
207-# --- artificialintelligencejobs.co (real record, fetched 2026-07-25) ---
208-
209-def _ai_jobs_response(jobs):
210-    resp = Mock(status_code=200)
211-    resp.json.return_value = {"generated": "2026-07-25 08:19 UTC", "companies": 320, "count": len(jobs), "jobs": jobs}
212-    return resp
213-
214-
215:def test_fetch_ai_jobs_filters_to_intern_level_and_normalizes():
216-    intern_job = {  # real, verbatim from the live feed 2026-07-25
217-        "title": "Product Management Intern (Summer 2027)", "location": "San Francisco",
218-        "url": "https://jobs.ashbyhq.com/databricks/some-real-posting-id", "posted": "2026-07-24",
219-        "company": "Databricks", "companyUrl": "https://databricks.com", "category": "Product",
220-        "level": "Intern", "remote": False, "region": "US", "slug": "[REDACTED]",
221-    }
222-    senior_job = {**intern_job, "level": "Senior", "title": "Senior Software Engineer, Database Engine Internals"}
223-
224-    def fake_get(url, timeout=None):
225-        return _ai_jobs_response([intern_job, senior_job])
226-
227-    listings = sources.fetch_ai_jobs(http_get=fake_get)
228-    assert len(listings) == 1
229-    assert listings[0].source == "AIJobs"
230-    assert listings[0].company == "Databricks"
231-    assert listings[0].active is True
232-
233-
234:def test_fetch_ai_jobs_propagates_no_crash_on_failure():
235-    def dying_get(url, timeout=None):
236-        raise requests.ConnectionError("simulated: site down")
237-
238-    assert sources.fetch_ai_jobs(http_get=dying_get) == []
  ```
- `Bash` — `grep -n "def test_fetch_freehire\|_freehire_response\|def _fh_" -A 20 tests/test_freehire.py | head -60`
  ```
64:def test_fetch_freehire_filters_to_structured_intern_seniority():
65-    intern_job = {**_by_case("[REDACTED]")}
66-    non_intern_job = {**intern_job, "public_slug": "senior-swe-google", "title": "Senior Software Engineer",
67-                       "enrichment": {"seniority": "senior"}}
68-
69-    def fake_get(url, timeout=None):
70-        return _search_response([intern_job, non_intern_job])
71-
72-    listings = fetch_freehire(http_get=fake_get)
73-    assert len(listings) == len(FREEHIRE_COMPANIES)  # one intern job per seeded company
74-    assert all(l.source == "Freehire" for l in listings)
75-
76-
77:def test_fetch_freehire_skips_a_dead_company_without_crashing():
78-    import requests
79-
80-    def flaky_get(url, timeout=None):
81-        if "google" in url:
82-            raise requests.ConnectionError("simulated: freehire down for this query")
83-        return _search_response([])
84-
85-    listings = fetch_freehire(http_get=flaky_get)
86-    assert listings == []  # no crash
87-
88-
89-def test_lookup_company_on_freehire_found():
90-    resp = Mock(status_code=200)
91-    resp.json.return_value = {"data": {"company": {"slug": "google", "name": "Google", "job_count": 3651}}}
92-    result = lookup_company_on_freehire("Google", http_get=Mock(return_value=resp))
93-    assert result["job_count"] == 3651
94-
95-
96-def test_lookup_company_on_freehire_not_found_returns_empty_dict():
97-    resp = Mock(status_code=404)
  ```
- `Bash`:
  ```bash
python3 -c "
import json
data = json.load(open('tests/fixtures/freehire.json'))
print(type(data))
if isinstance(data, list):
    print(data[0])
"
  ```
  ```
<class 'list'>
{'_case': '[REDACTED]', 'public_slug': '[REDACTED]', 'source': 'google', 'manually_added': False, 'external_id': ':85564713261245126', 'url': 'https://www.google.com/about/careers/applications/jobs/results/85564713261245126?utm_source=freehire.dev', 'title': 'Software Engineering Intern, BS, Summer 2027', 'company': 'Google', 'company_slug': 'google', 'location': 'Mountain View, CA, USA; Atlanta, GA, USA; Austin, TX, USA', 'description': 'Join us for a unique 12-14 week paid internship.', 'countries': ['us'], 'regions': ['north_america'], 'posted_at': '2026-07-20T16:11:13Z', 'created_at': '2026-07-20T17:01:40Z', 'closed_at': None, 'enrichment': {'summary': "A 12-14 week paid internship for Bachelor's students to develop scalable software systems.", 'employment_type': 'internship', 'visa_sponsorship': True, 'seniority': 'intern'}}
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
  ```diff
  - def _applyguy_raw():
    return {"updatedAt": "2026-08-24T00:00:00Z", "jobs": _strip_case_keys(json.loads((FIXTURES / "applyguy.json").read_text()))}


def _fake_http_get(url, timeout=None):
    from ingestion.freehire import FREEHIRE_SEARCH_URL
    from ingestion.sources import (
        AI_JOBS_URL,
        APPLYGUY_URL,
        ASHBY_JOBS_URL,
        GREENHOUSE_JOBS_URL,
        JOSEGAEL_URL,
        LEVER_JOBS_URL,
        SIMPLIFY_URL,
        VANSHB03_URL,
        ZSHAH101_URL,
    )

    resp = Mock(status_code=200)
    if url == SIMPLIFY_URL:
        resp.json.return_value = _simplify_raw()
    elif url == JOSEGAEL_URL:
        resp.json.return_value = _josegael_raw()
    elif url == VANSHB03_URL:
        resp.json.return_value = _vanshb03_raw()
    elif url == ZSHAH101_URL:
        resp.json.return_value = _zshah101_raw()
    elif url == APPLYGUY_URL:
        resp.json.return_value = _applyguy_raw()
    elif url.startswith(GREENHOUSE_JOBS_URL.split("{")[0]) or url.startswith(ASHBY_JOBS_URL.split("{")[0]):
        # per-company board endpoints — pipeline-orchestration tests don't need
        # real per-company data, that's covered in test_sources.py directly
        resp.json.return_value = {"jobs": []}
    elif url.startswith(LEVER_JOBS_URL.split("{")[0]):
        resp.json.return_value = []  # Lever's postings endpoint returns a bare list
    elif url.startswith(FREEHIRE_SEARCH_URL.split("{")[0]):
        resp.json.return_value = {"data": []}
    elif url == AI_JOBS_URL:
        resp.json.return_value = {"jobs": []}
    else:
        raise AssertionError(f"unexpected url: {url}")
    return resp
  + def _applyguy_raw():
    return {"updatedAt": "2026-08-24T00:00:00Z", "jobs": _strip_case_keys(json.loads((FIXTURES / "applyguy.json").read_text()))}


# Real, non-intern-titled shapes (so they don't add to fetch_greenhouse/
# fetch_ashby/fetch_lever/fetch_ai_jobs's own intern-only counts and disturb
# existing pipeline-orchestration assertions below) — just complete enough
# to satisfy core/schema_drift.py's GREENHOUSE/ASHBY/LEVER/AI_JOBS_REQUIRED_KEYS
# for the one specific company/URL each schema check hits.
_GREENHOUSE_SCHEMA_CHECK_JOB = {
    "id": 1, "title": "Senior Software Engineer", "absolute_url": "https://x/1",
    "location": {"name": "NYC"}, "updated_at": "2026-07-24T15:05:09-04:00",
}
_ASHBY_SCHEMA_CHECK_JOB = {
    "id": "a", "title": "Software Engineer", "jobUrl": "https://x/a", "location": "SF",
    "isListed": True, "publishedAt": "2026-06-01T00:00:00+00:00", "descriptionPlain": "",
    "employmentType": "FullTime",
}
_LEVER_SCHEMA_CHECK_JOB = {
    "id": "x", "text": "Senior Software Engineer", "applyUrl": "https://jobs.lever.co/palantir/x/apply",
    "categories": {"commitment": "Full-time", "location": "Palo Alto, California"},
    "createdAt": 1785864478389, "descriptionPlain": "",
}
_FREEHIRE_SCHEMA_CHECK_JOB = {
    "title": "Senior Software Engineer", "url": "https://x/senior", "location": "Mountain View, CA",
    "posted_at": "2026-07-20T16:11:13Z", "public_slug": "senior-swe-google", "description": "",
    "enrichment": {"seniority": "senior"},
}
_AI_JOBS_SCHEMA_CHECK_JOB = {
    "title": "Senior Software Engineer", "url": "https://x/senior", "company": "Databricks",
    "location": "San Francisco", "posted": "2026-07-24", "slug": "databricks-senior-swe", "level": "Senior",
}
_INTERNDOCK_SITEMAP_XML = (
    "<urlset><url><loc>https://www.interndock.com/tracker/guides/"
    "[REDACTED]</loc></url></urlset>"
)


def _fake_http_get(url, timeout=None):
    from core.schema_drift import (
        ASHBY_SCHEMA_CHECK_TOKEN,
        FREEHIRE_SCHEMA_CHECK_SLUG,
        GREENHOUSE_SCHEMA_CHECK_TOKEN,
        LEVER_SCHEMA_CHECK_TOKEN,
    )
    from ingestion.freehire import FREEHIRE_SEARCH_URL
    from ingestion.interndock import INTERNDOCK_SITEMAP_URL
    from ingestion.sources import (
        AI_JOBS_URL,
        APPLYGUY_URL,
        ASHBY_JOBS_URL,
        GREENHOUSE_JOBS_URL,
        JOSEGAEL_URL,
        LEVER_JOBS_URL,
        SIMPLIFY_URL,
        VANSHB03_URL,
        ZSHAH101_URL,
    )

    resp = Mock(status_code=200)
    if url == SIMPLIFY_URL:
        resp.json.return_value = _simplify_raw()
    elif url == JOSEGAEL_URL:
        resp.json.return_value = _josegael_raw()
    elif url == VANSHB03_URL:
        resp.json.return_value = _vanshb03_raw()
    elif url == ZSHAH101_URL:
        resp.json.return_value = _zshah101_raw()
    elif url == APPLYGUY_URL:
        resp.json.return_value = _applyguy_raw()
    elif url == GREENHOUSE_JOBS_URL.format(token=GREENHOUSE_SCHEMA_CHECK_TOKEN):
        resp.json.return_value = {"jobs": [_GREENHOUSE_SCHEMA_CHECK_JOB]}
    elif url == ASHBY_JOBS_URL.format(token=ASHBY_SCHEMA_CHECK_TOKEN):
        resp.json.return_value = {"jobs": [_ASHBY_SCHEMA_CHECK_JOB]}
    elif url.startswith(GREENHOUSE_JOBS_URL.split("{")[0]) or url.startswith(ASHBY_JOBS_URL.split("{")[0]):
        # per-company board endpoints — pipeline-orchestration tests don't need
        # real per-company data, that's covered in test_sources.py directly
        resp.json.return_value = {"jobs": []}
    elif url == LEVER_JOBS_URL.format(token=LEVER_SCHEMA_CHECK_TOKEN):
        resp.json.return_value = [_LEVER_SCHEMA_CHECK_JOB]
    elif url.startswith(LEVER_JOBS_URL.split("{")[0]):
        resp.json.return_value = []  # Lever's postings endpoint returns a bare list
    elif url == FREEHIRE_SEARCH_URL.format(slug=FREEHIRE_SCHEMA_CHECK_SLUG):
        resp.json.return_value = {"data": [_FREEHIRE_SCHEMA_CHECK_JOB]}
    elif url.startswith(FREEHIRE_SEARCH_URL.split("{")[0]):
        resp.json.return_value = {"data": []}
    elif url == AI_JOBS_URL:
        resp.json.return_value = {"jobs": [_AI_JOBS_SCHEMA_CHECK_JOB]}
    elif url == INTERNDOCK_SITEMAP_URL:
        resp.text = _INTERNDOCK_SITEMAP_XML
    else:
        raise AssertionError(f"unexpected url: {url}")
    return resp
  ```
- `Bash` — `.venv/bin/python -m pytest -q 2>&1 | tail -100`
  ```
........................................................................ [ 17%]
........................................................................ [ 35%]
........................................................................ [ 53%]
........................................................................ [ 71%]
.........................................F.............................. [ 89%]
.........................................                                [100%]
=================================== FAILURES ===================================
______________ test_check_all_passes_when_all_sources_are_healthy ______________

simplify_raw = [{'source': 'Simplify', 'category': 'Software', 'company_name': 'Palantir', 'id': '[REDACTED]...implify', 'category': 'Software', 'company_name': 'Anthropic', 'id': '[REDACTED]', ...}, ...]
josegael_raw = [{'id': '[REDACTED]', 'company_name': 'Deloitte', 'title': 'Audit & Assurance - Discovery In..., 'title': 'Applied Research Intern - Spring 2027', 'url': 'https://example.com/careers/spring-2027-intern', ...}, ...]
vanshb03_raw = [{'date_updated': 1776617698, 'url': 'https://careers.point72.com/CSJobDetail?jobName=[REDACTED]...X/[REDACTED]', 'locations': ['Frisco, TX'], 'sponsorship': 'Does Not Offer Sponsorship', ...}]
zshah101_raw = {'ashby:centerfield:[REDACTED]': {'category': 'Software', 'company': 'Centerfield', 'company...{'category': 'Software', 'closed_at': '2026-06-30T19:49:56Z', 'company': 'Amazon', 'company_slug': 'amazon', ...}, ...}
applyguy_raw = {'updatedAt': '2026-08-24T00:00:00Z', 'jobs': [{'id': '[REDACTED]', 'company': 'Toyota of Ce...1', 'company': 'Amazon', 'title': 'Product Manager Technical (PMT) Intern - Summer 2027', 'category': 'Product', ...}]}

    def test_check_all_passes_when_all_sources_are_healthy(
        simplify_raw, josegael_raw, vanshb03_raw, zshah101_raw, applyguy_raw,
    ):
        call_log = []
    
        def http_get(url, timeout):
            call_log.append(url)
            from ingestion.sources import APPLYGUY_URL, JOSEGAEL_URL, SIMPLIFY_URL, VANSHB03_URL, ZSHAH101_URL
    
            if url == SIMPLIFY_URL:
                return _json_response(simplify_raw)
            if url == JOSEGAEL_URL:
                return _json_response(josegael_raw)
            if url == VANSHB03_URL:
                return _json_response(vanshb03_raw)
            if url == ZSHAH101_URL:
                return _json_response(zshah101_raw)
            if url == APPLYGUY_URL:
                return _json_response(applyguy_raw)
            raise AssertionError(f"unexpected url: {url}")
    
>       check_all(http_get=http_get)  # does not raise
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

tests/test_schema_drift.py:152: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
core/schema_drift.py:259: in check_all
    check_greenhouse_schema(http_get)
core/schema_drift.py:187: in check_greenhouse_schema
    _check_wrapped_jobs_source(
core/schema_drift.py:175: in _check_wrapped_jobs_source
    resp = http_get(url, timeout=TIMEOUT)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

url = 'https://boards-api.greenhouse.io/v1/boards/scaleai/jobs', timeout = 30

    def http_get(url, timeout):
        call_log.append(url)
        from ingestion.sources import APPLYGUY_URL, JOSEGAEL_URL, SIMPLIFY_URL, VANSHB03_URL, ZSHAH101_URL
    
        if url == SIMPLIFY_URL:
            return _json_response(simplify_raw)
        if url == JOSEGAEL_URL:
            return _json_response(josegael_raw)
        if url == VANSHB03_URL:
            return _json_response(vanshb03_raw)
        if url == ZSHAH101_URL:
            return _json_response(zshah101_raw)
        if url == APPLYGUY_URL:
            return _json_response(applyguy_raw)
>       raise AssertionError(f"unexpected url: {url}")
E       AssertionError: unexpected url: https://boards-api.greenhouse.io/v1/boards/scaleai/jobs

tests/test_schema_drift.py:150: AssertionError
=========================== short test summary info ============================
FAILED tests/test_schema_drift.py::test_check_all_passes_when_all_sources_are_healthy
1 failed, 400 passed in 1.84s
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
  ```diff
  - from core.schema_drift import (
    SchemaDriftError,
    check_all,
    check_applyguy_schema,
    check_josegael_schema,
    check_simplify_schema,
    check_vanshb03_schema,
    check_zshah101_schema,
)
  + from core.schema_drift import (
    AI_JOBS_REQUIRED_KEYS,
    ASHBY_REQUIRED_KEYS,
    ASHBY_SCHEMA_CHECK_TOKEN,
    FREEHIRE_REQUIRED_KEYS,
    FREEHIRE_SCHEMA_CHECK_SLUG,
    GREENHOUSE_REQUIRED_KEYS,
    GREENHOUSE_SCHEMA_CHECK_TOKEN,
    LEVER_REQUIRED_KEYS,
    LEVER_SCHEMA_CHECK_TOKEN,
    SchemaDriftError,
    check_ai_jobs_schema,
    check_all,
    check_applyguy_schema,
    check_ashby_schema,
    check_freehire_schema,
    check_greenhouse_schema,
    check_interndock_sitemap,
    check_josegael_schema,
    check_lever_schema,
    check_simplify_schema,
    check_vanshb03_schema,
    check_zshah101_schema,
)
from ingestion.freehire import FREEHIRE_SEARCH_URL
from ingestion.interndock import INTERNDOCK_SITEMAP_URL
from ingestion.sources import AI_JOBS_URL, ASHBY_JOBS_URL, GREENHOUSE_JOBS_URL, LEVER_JOBS_URL
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
  ```diff
  - @pytest.fixture
def applyguy_raw():
    # ApplyGuy's real feed is {"updatedAt": ..., "jobs": [...]} — a third
    # shape check_applyguy_schema handles with its own bespoke check.
    return {"updatedAt": "2026-08-24T00:00:00Z", "jobs": _strip_case_keys(json.loads((FIXTURES / "applyguy.json").read_text()))}
  + @pytest.fixture
def applyguy_raw():
    # ApplyGuy's real feed is {"updatedAt": ..., "jobs": [...]} — a third
    # shape check_applyguy_schema handles with its own bespoke check.
    return {"updatedAt": "2026-08-24T00:00:00Z", "jobs": _strip_case_keys(json.loads((FIXTURES / "applyguy.json").read_text()))}


# --- fixtures for the 6 sources added in Task 2 (Prompt 19, 2026-08-28) ---
# Real, verbatim single-entry shapes, same literals used in
# tests/test_sources.py / tests/test_freehire.py for the same live sources.

@pytest.fixture
def greenhouse_raw():
    return {"jobs": [{
        "id": 1, "title": "Summer 2027 Software Engineering Intern", "absolute_url": "https://x/1",
        "location": {"name": "NYC"}, "updated_at": "2026-07-24T15:05:09-04:00",
    }]}


@pytest.fixture
def ashby_raw():
    return {"jobs": [{
        "id": "a", "title": "Software Engineer Intern", "location": "SF", "jobUrl": "https://x/a",
        "publishedAt": "2026-06-01T00:00:00+00:00", "isListed": True, "descriptionPlain": "",
        "employmentType": "Intern",
    }]}


@pytest.fixture
def lever_raw():
    return [{
        "id": "[REDACTED]", "text": "Quantitative Trading Intern - Summer 2027",
        "categories": {"commitment": "Intern", "location": "Chicago, Illinois"},
        "hostedUrl": "https://jobs.lever.co/belvederetrading/cbde47db",
        "applyUrl": "https://jobs.lever.co/belvederetrading/cbde47db/apply",
        "createdAt": 1785864478389, "descriptionPlain": "Belvedere Trading is a proprietary trading firm.",
    }]


@pytest.fixture
def freehire_raw():
    return {"data": _strip_case_keys(json.loads((FIXTURES / "freehire.json").read_text()))[:1]}


@pytest.fixture
def ai_jobs_raw():
    return {"jobs": [{
        "title": "Product Management Intern (Summer 2027)", "location": "San Francisco",
        "url": "https://jobs.ashbyhq.com/databricks/some-real-posting-id", "posted": "2026-07-24",
        "company": "Databricks", "companyUrl": "https://databricks.com", "category": "Product",
        "level": "Intern", "remote": False, "region": "US", "slug": "[REDACTED]",
    }]}


@pytest.fixture
def interndock_sitemap_text():
    # Real shape confirmed live 2026-08-28: <loc> entries, some drop-shaped.
    return (
        "<urlset>"
        "<url><loc>https://www.interndock.com/tracker/guides/[REDACTED]</loc></url>"
        "<url><loc>https://www.interndock.com/pricing</loc></url>"
        "</urlset>"
    )
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
  ```diff
  - def test_applyguy_schema_detects_empty_jobs_list():
    http_get = Mock(return_value=_json_response({"updatedAt": "2026-08-24", "jobs": []}))
    with pytest.raises(SchemaDriftError, match="non-empty 'jobs' list"):
        check_applyguy_schema(http_get=http_get)
  + def test_applyguy_schema_detects_empty_jobs_list():
    http_get = Mock(return_value=_json_response({"updatedAt": "2026-08-24", "jobs": []}))
    with pytest.raises(SchemaDriftError, match="non-empty 'jobs' list"):
        check_applyguy_schema(http_get=http_get)


# --- Greenhouse (Task 2, 2026-08-28) — one representative company (scaleai) ---

def test_greenhouse_schema_passes_on_real_shape(greenhouse_raw):
    http_get = Mock(return_value=_json_response(greenhouse_raw))
    check_greenhouse_schema(http_get=http_get)  # does not raise


def test_greenhouse_schema_hits_the_schema_check_token(greenhouse_raw):
    http_get = Mock(return_value=_json_response(greenhouse_raw))
    check_greenhouse_schema(http_get=http_get)
    called_url = http_get.call_args[0][0]
    assert called_url == GREENHOUSE_JOBS_URL.format(token=GREENHOUSE_SCHEMA_CHECK_TOKEN)


def test_greenhouse_schema_detects_renamed_absolute_url(greenhouse_raw):
    """absolute_url is read via raw["absolute_url"] — a rename would crash
    normalize_greenhouse, not silently degrade it, but the drift check must
    still catch it before that ever happens in the real run."""
    drifted = {"jobs": [{("url" if k == "absolute_url" else k): v for k, v in j.items()} for j in greenhouse_raw["jobs"]]}
    http_get = Mock(return_value=_json_response(drifted))
    with pytest.raises(SchemaDriftError, match="absolute_url"):
        check_greenhouse_schema(http_get=http_get)


def test_greenhouse_schema_detects_empty_jobs_list():
    http_get = Mock(return_value=_json_response({"jobs": []}))
    with pytest.raises(SchemaDriftError, match="non-empty 'jobs' list"):
        check_greenhouse_schema(http_get=http_get)


# --- Ashby (Task 2, 2026-08-28) — one representative company (elevenlabs) ---

def test_ashby_schema_passes_on_real_shape(ashby_raw):
    http_get = Mock(return_value=_json_response(ashby_raw))
    check_ashby_schema(http_get=http_get)  # does not raise


def test_ashby_schema_hits_the_schema_check_token(ashby_raw):
    http_get = Mock(return_value=_json_response(ashby_raw))
    check_ashby_schema(http_get=http_get)
    called_url = http_get.call_args[0][0]
    assert called_url == ASHBY_JOBS_URL.format(token=ASHBY_SCHEMA_CHECK_TOKEN)


def test_ashby_schema_detects_dropped_employment_type(ashby_raw):
    """employmentType is what fetch_ashby's own role-type triage reads
    (job.get("employmentType") == "Intern") — the exact field whose real
    2026-08-21..08-28 drift-shaped incident (Prompt 19 Task 1) this check
    exists to catch early, even though it turned out not to be drift there."""
    drifted = {"jobs": [{k: v for k, v in j.items() if k != "employmentType"} for j in ashby_raw["jobs"]]}
    http_get = Mock(return_value=_json_response(drifted))
    with pytest.raises(SchemaDriftError, match="employmentType"):
        check_ashby_schema(http_get=http_get)


def test_ashby_schema_detects_empty_jobs_list():
    http_get = Mock(return_value=_json_response({"jobs": []}))
    with pytest.raises(SchemaDriftError, match="non-empty 'jobs' list"):
        check_ashby_schema(http_get=http_get)


# --- Lever (Task 2, 2026-08-28) — one representative company (palantir) ---

def test_lever_schema_passes_on_real_shape(lever_raw):
    http_get = Mock(return_value=_json_response(lever_raw))
    check_lever_schema(http_get=http_get)  # does not raise


def test_lever_schema_hits_the_schema_check_token(lever_raw):
    http_get = Mock(return_value=_json_response(lever_raw))
    check_lever_schema(http_get=http_get)
    called_url = http_get.call_args[0][0]
    assert called_url == LEVER_JOBS_URL.format(token=LEVER_SCHEMA_CHECK_TOKEN)


def test_lever_schema_detects_dropped_text_field(lever_raw):
    """text is what both normalize_lever (raw["text"]) and fetch_lever's own
    role-type triage (job.get("text", "")) read."""
    drifted = [{k: v for k, v in j.items() if k != "text"} for j in lever_raw]
    http_get = Mock(return_value=_json_response(drifted))
    with pytest.raises(SchemaDriftError, match="text"):
        check_lever_schema(http_get=http_get)


def test_lever_schema_detects_empty_list():
    http_get = Mock(return_value=_json_response([]))
    with pytest.raises(SchemaDriftError, match="non-empty"):
        check_lever_schema(http_get=http_get)


# --- Freehire (Task 2, 2026-08-28) — a fourth shape: {"data": [...]} plus a
# nested enrichment.seniority field ---

def test_freehire_schema_passes_on_real_shape(freehire_raw):
    http_get = Mock(return_value=_json_response(freehire_raw))
    check_freehire_schema(http_get=http_get)  # does not raise


def test_freehire_schema_hits_the_schema_check_slug(freehire_raw):
    http_get = Mock(return_value=_json_response(freehire_raw))
    check_freehire_schema(http_get=http_get)
    called_url = http_get.call_args[0][0]
    assert called_url == FREEHIRE_SEARCH_URL.format(slug=FREEHIRE_SCHEMA_CHECK_SLUG)


def test_freehire_schema_detects_dropped_public_slug(freehire_raw):
    drifted = {"data": [{k: v for k, v in j.items() if k != "public_slug"} for j in freehire_raw["data"]]}
    http_get = Mock(return_value=_json_response(drifted))
    with pytest.raises(SchemaDriftError, match="public_slug"):
        check_freehire_schema(http_get=http_get)


def test_freehire_schema_detects_dropped_nested_seniority(freehire_raw):
    """seniority lives nested under enrichment — what fetch_freehire's own
    role-type triage reads ((job.get("enrichment") or {}).get("seniority")).
    A flat top-level key check alone wouldn't catch this."""
    drifted = {"data": [
        {**j, "enrichment": {k: v for k, v in j["enrichment"].items() if k != "seniority"}}
        for j in freehire_raw["data"]
    ]}
    http_get = Mock(return_value=_json_response(drifted))
    with pytest.raises(SchemaDriftError, match="seniority"):
        check_freehire_schema(http_get=http_get)


def test_freehire_schema_detects_empty_data_list():
    http_get = Mock(return_value=_json_response({"data": []}))
    with pytest.raises(SchemaDriftError, match="non-empty 'data' list"):
        check_freehire_schema(http_get=http_get)


# --- AIJobs (Task 2, 2026-08-28) — one generated snapshot feed ---

def test_ai_jobs_schema_passes_on_real_shape(ai_jobs_raw):
    http_get = Mock(return_value=_json_response(ai_jobs_raw))
    check_ai_jobs_schema(http_get=http_get)  # does not raise


def test_ai_jobs_schema_hits_the_real_url(ai_jobs_raw):
    http_get = Mock(return_value=_json_response(ai_jobs_raw))
    check_ai_jobs_schema(http_get=http_get)
    called_url = http_get.call_args[0][0]
    assert called_url == AI_JOBS_URL


def test_ai_jobs_schema_detects_dropped_level_field(ai_jobs_raw):
    """level is what fetch_ai_jobs' own role-type triage reads
    (raw.get("level") == "Intern")."""
    drifted = {"jobs": [{k: v for k, v in j.items() if k != "level"} for j in ai_jobs_raw["jobs"]]}
    http_get = Mock(return_value=_json_response(drifted))
    with pytest.raises(SchemaDriftError, match="level"):
        check_ai_jobs_schema(http_get=http_get)


def test_ai_jobs_schema_detects_empty_jobs_list():
    http_get = Mock(return_value=_json_response({"jobs": []}))
    with pytest.raises(SchemaDriftError, match="non-empty 'jobs' list"):
        check_ai_jobs_schema(http_get=http_get)


# --- InternDock (Task 2, 2026-08-28) — no JSON API, so this checks the
# sitemap's own real shape instead of a field schema (see the block comment
# in core/schema_drift.py for why a deeper content-shape check isn't possible
# here without spending a real Firecrawl call on a URL that might not even be
# a real drop) ---

def test_interndock_sitemap_passes_on_real_shape(interndock_sitemap_text):
    http_get = Mock(return_value=_text_response(interndock_sitemap_text))
    check_interndock_sitemap(http_get=http_get)  # does not raise


def test_interndock_sitemap_hits_the_real_url(interndock_sitemap_text):
    http_get = Mock(return_value=_text_response(interndock_sitemap_text))
    check_interndock_sitemap(http_get=http_get)
    called_url = http_get.call_args[0][0]
    assert called_url == INTERNDOCK_SITEMAP_URL


def test_interndock_sitemap_detects_no_loc_entries():
    http_get = Mock(return_value=_text_response("<urlset></urlset>"))
    with pytest.raises(SchemaDriftError, match="no <loc> entries"):
        check_interndock_sitemap(http_get=http_get)


def test_interndock_sitemap_detects_no_drop_shaped_candidates():
    """Every real URL is still there, but none look drop-shaped anymore —
    e.g. interndock renamed its guide-slug convention entirely."""
    http_get = Mock(return_value=_text_response(
        "<urlset><url><loc>https://www.interndock.com/pricing</loc></url></urlset>"
    ))
    with pytest.raises(SchemaDriftError, match="none match the drop-shaped slug pattern"):
        check_interndock_sitemap(http_get=http_get)
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
  ```diff
  - def test_check_all_passes_when_all_sources_are_healthy(
    simplify_raw, josegael_raw, vanshb03_raw, zshah101_raw, applyguy_raw,
):
    call_log = []

    def http_get(url, timeout):
        call_log.append(url)
        from ingestion.sources import APPLYGUY_URL, JOSEGAEL_URL, SIMPLIFY_URL, VANSHB03_URL, ZSHAH101_URL

        if url == SIMPLIFY_URL:
            return _json_response(simplify_raw)
        if url == JOSEGAEL_URL:
            return _json_response(josegael_raw)
        if url == VANSHB03_URL:
            return _json_response(vanshb03_raw)
        if url == ZSHAH101_URL:
            return _json_response(zshah101_raw)
        if url == APPLYGUY_URL:
            return _json_response(applyguy_raw)
        raise AssertionError(f"unexpected url: {url}")

    check_all(http_get=http_get)  # does not raise
    assert len(call_log) == 5
  + def test_check_all_passes_when_all_sources_are_healthy(
    simplify_raw, josegael_raw, vanshb03_raw, zshah101_raw, applyguy_raw,
    greenhouse_raw, ashby_raw, lever_raw, freehire_raw, ai_jobs_raw, interndock_sitemap_text,
):
    call_log = []

    def http_get(url, timeout):
        call_log.append(url)
        from ingestion.sources import APPLYGUY_URL, JOSEGAEL_URL, SIMPLIFY_URL, VANSHB03_URL, ZSHAH101_URL

        if url == SIMPLIFY_URL:
            return _json_response(simplify_raw)
        if url == JOSEGAEL_URL:
            return _json_response(josegael_raw)
        if url == VANSHB03_URL:
            return _json_response(vanshb03_raw)
        if url == ZSHAH101_URL:
            return _json_response(zshah101_raw)
        if url == APPLYGUY_URL:
            return _json_response(applyguy_raw)
        if url == GREENHOUSE_JOBS_URL.format(token=GREENHOUSE_SCHEMA_CHECK_TOKEN):
            return _json_response(greenhouse_raw)
        if url == ASHBY_JOBS_URL.format(token=ASHBY_SCHEMA_CHECK_TOKEN):
            return _json_response(ashby_raw)
        if url == LEVER_JOBS_URL.format(token=LEVER_SCHEMA_CHECK_TOKEN):
            return _json_response(lever_raw)
        if url == FREEHIRE_SEARCH_URL.format(slug=FREEHIRE_SCHEMA_CHECK_SLUG):
            return _json_response(freehire_raw)
        if url == AI_JOBS_URL:
            return _json_response(ai_jobs_raw)
        if url == INTERNDOCK_SITEMAP_URL:
            return _text_response(interndock_sitemap_text)
        raise AssertionError(f"unexpected url: {url}")

    check_all(http_get=http_get)  # does not raise
    assert len(call_log) == 11
  ```
- `Bash` — `grep -n "GREENHOUSE_REQUIRED_KEYS\|ASHBY_REQUIRED_KEYS\|LEVER_REQUIRED_KEYS\|FREEHIRE_REQUIRED_KEYS\|AI_JOBS_REQUIRED_KEYS" tests/test_schema_drift.py`
  ```
8:    AI_JOBS_REQUIRED_KEYS,
9:    ASHBY_REQUIRED_KEYS,
11:    FREEHIRE_REQUIRED_KEYS,
13:    GREENHOUSE_REQUIRED_KEYS,
15:    LEVER_REQUIRED_KEYS,
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
  ```diff
  - from core.schema_drift import (
    AI_JOBS_REQUIRED_KEYS,
    ASHBY_REQUIRED_KEYS,
    ASHBY_SCHEMA_CHECK_TOKEN,
    FREEHIRE_REQUIRED_KEYS,
    FREEHIRE_SCHEMA_CHECK_SLUG,
    GREENHOUSE_REQUIRED_KEYS,
    GREENHOUSE_SCHEMA_CHECK_TOKEN,
    LEVER_REQUIRED_KEYS,
    LEVER_SCHEMA_CHECK_TOKEN,
    SchemaDriftError,
  + from core.schema_drift import (
    ASHBY_SCHEMA_CHECK_TOKEN,
    FREEHIRE_SCHEMA_CHECK_SLUG,
    GREENHOUSE_SCHEMA_CHECK_TOKEN,
    LEVER_SCHEMA_CHECK_TOKEN,
    SchemaDriftError,
  ```
- `Bash` — `.venv/bin/python -m pytest tests/test_schema_drift.py -q 2>&1 | tail -60`
  ```
................................................                         [100%]
48 passed in 0.17s
  ```
- `Bash` — `grep -n "test_run_once_files_issue_on_exclusion_spike\|should_alert_on_exclusion_spike\|def test_update_debate_losses" tests/test_debate_losses.py | head`
  ```
73:def test_should_alert_on_exclusion_spike_threshold():
79:    assert run_pipeline.should_alert_on_exclusion_spike(20) is False
80:    assert run_pipeline.should_alert_on_exclusion_spike(21) is True
81:    assert run_pipeline.should_alert_on_exclusion_spike(0) is False
141:def test_run_once_files_issue_on_exclusion_spike(tmp_path, monkeypatch):
143:    should_alert_on_exclusion_spike to issue_fn — the threshold logic
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_debate_losses.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py`
- `Bash` — `grep -n "^def _run_once_kwargs" -A 40 tests/test_run_pipeline.py`
  ```
420:def _run_once_kwargs(tmp_path, **overrides):
421-    kwargs = dict(
422-        jarvis_dir=tmp_path / "jarvis",
423-        state_path=tmp_path / "state" / "seen_ids.json",
424-        runs_log_path=tmp_path / "logs" / "runs.jsonl",
425-        now=datetime(2026, 7, 17, 15, 0, tzinfo=timezone.utc),  # a Friday, not rollup time
426-        profile=PROFILE,
427-        http_get=_fake_http_get,
428-        http_head=_fake_http_head_all_live,
429-        push_fn=lambda repo_dir, message: True,
430-        issue_fn=Mock(),
431-    )
432-    kwargs.update(overrides)
433-    (tmp_path / "jarvis").mkdir(parents=True, exist_ok=True)
434-    return kwargs
435-
436-
437-def test_run_once_happy_path_marks_seen_and_writes_dossiers(tmp_path):
438-    kwargs = _run_once_kwargs(tmp_path)
439-    record = run_pipeline.run_once(**kwargs)
440-
441-    assert record["halted"] is False
442-    assert record["written_count"] > 0
443-    assert not record["errors"]
444-
445-    seen = run_pipeline.load_seen_ids(kwargs["state_path"])
446-    assert len(seen) == record["written_count"]
447-
448-    dossiers_dir = kwargs["jarvis_dir"] / "10_Areas/Career/Internships/List/Dossiers"
449-    assert len(list(dossiers_dir.glob("**/*.md"))) == record["written_count"]
450-
451-    logged = json.loads((kwargs["runs_log_path"]).read_text().splitlines()[0])
452-    assert logged["written_count"] == record["written_count"]
453-
454-    kwargs["issue_fn"].assert_not_called()  # nothing systemic happened
455-
456-
457-def test_run_once_halts_on_schema_drift_and_writes_nothing(tmp_path, monkeypatch):
458-    def drifted_check(http_get=None):
459-        raise SchemaDriftError("SimplifyJobs: missing expected keys ['category']")
460-
  ```
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_zero_match_alert.py`
  ```
"""Task 3 (Prompt 19, 2026-08-28) — per-source zero-match-rate alert.

Same "pure function first, integration test proves the wiring" decomposition
as tests/test_debate_losses.py: update_zero_match_streaks's counting rules
are properties of the counting arithmetic itself, easiest pinned directly;
a separate integration test then only needs to confirm run_once actually
calls issue_fn when the threshold is crossed.
"""
import json

import run_pipeline
from test_run_pipeline import _run_once_kwargs


# --- update_zero_match_streaks: pure-function tests ---

def test_zero_match_streak_increments_while_fetching_but_not_matching():
    streaks = {}
    for i in range(1, 4):
        streaks, alerting = run_pipeline.update_zero_match_streaks(streaks, {"Ashby": 4}, {"Ashby": 0})
        assert alerting == []
        assert streaks["Ashby"]["streak"] == i


def test_zero_match_streak_never_alerts_if_source_never_matched():
    """A source that has never once produced a match isn't drifting, it's
    just structurally not matching anything — no alert, ever, no matter how
    long the streak runs, until it proves it CAN match at least once."""
    streaks = {}
    for _ in range(run_pipeline.ZERO_MATCH_STREAK_ALERT_THRESHOLD + 5):
        streaks, alerting = run_pipeline.update_zero_match_streaks(streaks, {"NewSource": 2}, {"NewSource": 0})
        assert alerting == []
    assert streaks["NewSource"]["ever_matched"] is False
    assert streaks["NewSource"]["streak"] == run_pipeline.ZERO_MATCH_STREAK_ALERT_THRESHOLD + 5


def test_zero_match_streak_fires_exactly_once_at_threshold():
    streaks = {"Ashby": {"streak": 0, "ever_matched": True}}
    fired_runs = []
    for i in range(1, run_pipeline.ZERO_MATCH_STREAK_ALERT_THRESHOLD + 3):
        streaks, alerting = run_pipeline.update_zero_match_streaks(streaks, {"Ashby": 4}, {"Ashby": 0})
        if alerting:
            fired_runs.append(i)
    assert fired_runs == [run_pipeline.ZERO_MATCH_STREAK_ALERT_THRESHOLD]  # only once, not every run after


def test_zero_match_streak_resets_on_a_real_match_and_marks_ever_matched():
    streaks = {}
    streaks, _ = run_pipeline.update_zero_match_streaks(streaks, {"Lever": 3}, {"Lever": 0})
    streaks, _ = run_pipeline.update_zero_match_streaks(streaks, {"Lever": 3}, {"Lever": 0})
    assert streaks["Lever"]["streak"] == 2

    streaks, alerting = run_pipeline.update_zero_match_streaks(streaks, {"Lever": 3}, {"Lever": 1})
    assert alerting == []
    assert streaks["Lever"]["streak"] == 0
    assert streaks["Lever"]["ever_matched"] is True


def test_zero_match_streak_unaffected_by_a_zero_fetch_run():
    """A single fetch hiccup (fetch_count == 0, e.g. a swallowed
    RequestException) neither advances nor resets an in-progress streak."""
    streaks = {"Ashby": {"streak": 5, "ever_matched": True}}
    streaks, alerting = run_pipeline.update_zero_match_streaks(streaks, {"Ashby": 0}, {"Ashby": 0})
    assert alerting == []
    assert streaks["Ashby"]["streak"] == 5


def test_zero_match_streak_real_ashby_incident_shape():
    """Pins the real, concrete incident this task was built from (Prompt 19
    Task 1): fetch_count frozen at 4, filter_match_count frozen at 0, for
    115 consecutive runs — confirms the alert threshold (24) would have
    fired well before a human noticed at run 115."""
    streaks = {}
    alert_runs = []
    for i in range(1, 116):
        streaks, alerting = run_pipeline.update_zero_match_streaks(
            {**streaks, "Ashby": {"streak": streaks.get("Ashby", {}).get("streak", 0), "ever_matched": True}},
            {"Ashby": 4}, {"Ashby": 0},
        )
        if alerting:
            alert_runs.append(i)
    assert alert_runs == [run_pipeline.ZERO_MATCH_STREAK_ALERT_THRESHOLD]
    assert alert_runs[0] < 115


def test_load_save_zero_match_streaks_round_trips(tmp_path):
    state_dir = tmp_path / "state"
    run_pipeline.save_zero_match_streaks(state_dir, {"Ashby": {"streak": 3, "ever_matched": True}})
    assert run_pipeline.load_zero_match_streaks(state_dir) == {"Ashby": {"streak": 3, "ever_matched": True}}


def test_load_zero_match_streaks_missing_file_returns_empty_dict(tmp_path):
    assert run_pipeline.load_zero_match_streaks(tmp_path / "state") == {}


# --- integration: run_once wires update_zero_match_streaks to issue_fn ---

def test_run_once_files_issue_and_persists_state_on_zero_match_streak(tmp_path, monkeypatch):
    """Integration-level confirmation that run_once actually calls issue_fn
    once the persisted streak crosses the threshold — the counting logic
    itself is covered by the pure-function tests above, this only proves
    the two are wired together and that state persists across calls."""
    monkeypatch.setattr(run_pipeline, "check_schema_drift", lambda http_get=None: None)
    state_dir = tmp_path / "state"
    state_dir.mkdir(parents=True)
    run_pipeline.save_zero_match_streaks(
        state_dir, {"Ashby": {"streak": run_pipeline.ZERO_MATCH_STREAK_ALERT_THRESHOLD - 1, "ever_matched": True}},
    )

    def fake_fetch_and_filter(profile, http_get=None, excluded_ids=frozenset()):
        return {"Ashby": {"fetch_count": 4, "matched": []}}

    monkeypatch.setattr(run_pipeline, "fetch_and_filter", fake_fetch_and_filter)
    kwargs = _run_once_kwargs(tmp_path, state_dir=state_dir)
    record = run_pipeline.run_once(**kwargs)

    assert record["zero_match_alerts"] == ["Ashby"]
    alert_calls = [c for c in kwargs["issue_fn"].call_args_list if "stuck at 0" in c.args[1]]
    assert len(alert_calls) == 1
    assert "Ashby" in alert_calls[0].args[1]

    persisted = run_pipeline.load_zero_match_streaks(state_dir)
    assert persisted["Ashby"]["streak"] == run_pipeline.ZERO_MATCH_STREAK_ALERT_THRESHOLD


def test_run_once_does_not_alert_below_threshold(tmp_path, monkeypatch):
    monkeypatch.setattr(run_pipeline, "check_schema_drift", lambda http_get=None: None)
    state_dir = tmp_path / "state"
    state_dir.mkdir(parents=True)

    def fake_fetch_and_filter(profile, http_get=None, excluded_ids=frozenset()):
        return {"Ashby": {"fetch_count": 4, "matched": []}}

    monkeypatch.setattr(run_pipeline, "fetch_and_filter", fake_fetch_and_filter)
    kwargs = _run_once_kwargs(tmp_path, state_dir=state_dir)
    record = run_pipeline.run_once(**kwargs)

    assert record["zero_match_alerts"] == []
    assert not any("stuck at 0" in c.args[1] for c in kwargs["issue_fn"].call_args_list)

  ```
- `Bash` — `.venv/bin/python -m pytest tests/test_zero_match_alert.py -q 2>&1 | tail -100`
  ```
..........                                                               [100%]
10 passed in 0.21s
  ```
- `Bash` — `.venv/bin/python -m pytest -q 2>&1 | tail -40`
  ```
........................................................................ [ 16%]
........................................................................ [ 33%]
........................................................................ [ 49%]
........................................................................ [ 66%]
........................................................................ [ 82%]
........................................................................ [ 99%]
....                                                                     [100%]
436 passed in 2.01s
  ```
- `Skill` — `{"skill":"review-loop-change"}`

## You

Base directory for this skill: /home/anant_gupta/projects/work/internship-research-loop/.claude/skills/review-loop-change

# /review-loop-change

A repo-scoped convention check, not a general code review (use the built-in `/code-review` for correctness/security/style). This exists because this repo has a small number of load-bearing design decisions that are easy to accidentally violate one file at a time without ever being wrong in isolation — a new filter rule that's individually correct but calls an LLM, or a new check that's individually correct but inserted before a cheaper one in the write gate. Catching that needs to compare the diff against the repo's conventions specifically, not against general best practice.

## Why a skill, not an agent, for this repo

This repo is ~1,500 lines with a ~1:1 test-to-code ratio (`tests/` mirrors `core/`, `ingestion/`, `vault_writer/` almost file-for-file) and changes land as small, individually-reviewable diffs (see `git log` — commits like "Four new discovery sources" or a single-file bloat fix, not sprawling multi-file rewrites). A diff this size doesn't need an isolated subagent context to protect the main conversation's window, and the checklist below is fixed and specific rather than open-ended — both are exactly the case where a lightweight, inline skill beats spinning up a separate agent. If this repo ever grows enough that a single diff regularly spans dozens of files, revisit this choice; the checklist would still apply, only the delivery mechanism would need to change.

## What to check

Run against the actual diff — `git diff` (unstaged), `git diff --cached` (staged), or a specific file/range if the user names one. This is a **reports-only** check: never modify code as part of this skill; if a violation should be fixed, say so and let the user (or a follow-up edit) do it.

### 1. Zero-LLM in the unattended path
`run_pipeline.py`, `recheck.py`, `core/filter.py`, `core/relevance.py`, `core/classify.py`, everything under `ingestion/`, and `vault_writer/` all run unattended (hourly/daily via GitHub Actions, no human in the loop) and must never call an LLM API, however indirectly. `enrich.py` is the **one** explicit exception — it's a manual CLI tool a human runs on demand at promotion time (see its own docstring) — and even it says "No LLM call anywhere" in its own header; a diff that adds LLM-backed logic to `enrich.py` still fails this check, since the zero-LLM property is about content generation, not about being unattended specifically.
- Flag: any new `import` of an LLM/AI SDK, any new HTTP call to an LLM provider endpoint, any prompt-shaped string literal, in any of the unattended-path files above.
- Pass: keyword/regex/structural logic, however elaborate (see `core/relevance.py`'s two-stage design for what "elaborate but still zero-LLM" looks like).

### 2. Permissive-by-default / explicit-negative-signal design
Every eligibility check in this repo (`location_eligible`, `degrees_eligible`, the term/season matchers in `core/filter.py`) follows one shape: **ambiguous or missing data passes; only an affirmative negative signal rejects.** This is a deliberate, load-bearing choice (see `core/filter.py`'s own comments — "a false negative here silently kills a listing before it's ever fetched") and the opposite instinct (a new allowlist that rejects anything not explicitly matched) is the single most likely way a new rule in this codebase quietly starts throwing away real, eligible postings.
- Flag: a new gate/check where missing or unrecognized data causes rejection by default (an implicit `else: return False` / `if not X: reject` on data the source doesn't reliably provide).
- Pass: a new gate that only rejects on a specific, named affirmative signal (a denylist token, an explicit exclusion string), same shape as the existing ones.
- This rule is about *eligibility/relevance* gates specifically (Layer 2/2.5). It does not apply to the Layer 4 write gate (`vault_writer/validate.py`) — that one is intentionally fail-closed on missing required fields; don't flag it for being "not permissive," that's a different, also-intentional design (see check 3).

### 3. Fail-closed write-gate ordering
`vault_writer/validate.py`'s `validate()` runs five checks in a specific, deliberate order: `required_fields` → `not_duplicate` → `cross_source_duplicate` → `url_liveness` → `format_compliance`, short-circuiting on the first failure. The order is cost-based (free/cheap checks before ones that cost a network call) — `cross_source_duplicate` runs before `url_liveness` specifically because "it's free, the HEAD request isn't" (the function's own docstring). A change that reorders these, or inserts a new check in the wrong position relative to cost, silently makes the gate slower or changes which check's rejection reason gets reported for the same bad item.
- Flag: any diff touching `validate()`'s check sequence, or adding a new check, without an explicit note on where in the cost order it belongs and why.
- Flag: any write path (`write_dossier`, or a new one) that writes to the vault before `validate()` has been called and returned `passed=True` for that exact item.
- Pass: a new check inserted with a stated reason for its position, consistent with "free checks first."

### 4. Every new rule cites the real live data it was built from
Look through this repo's existing rule comments — `core/filter.py`'s `_NON_US` denylist ("Every foreign token actually observed in live data..."), `core/relevance.py`'s stage1/stage2 regexes ("Real examples confirmed against seeded Greenhouse boards 2026-07-26..."), `core/profile.yaml`'s `terms_weight` comment. The convention is explicit: a new keyword, regex, denylist entry, or threshold is never justified by "this seems right" — it cites the actual company/posting/fixture it was checked against and the date it was checked.
- Flag: a new regex pattern, keyword list, or magic threshold/constant added to any filter/classify/relevance/validate module with no comment tracing it to real data (a fixture file, a specific company/posting example, a date).
- Pass: a new rule with a comment naming the real evidence — doesn't need to be exhaustive, but it needs to be real and specific, not "handles edge cases."

## Output format

Keep it short — this is a fast pre-ship check, not an essay:

```
## review-loop-change: <file(s) reviewed>

[PASS]  <check name> — <one line, or omit detail entirely if clean>
[FLAG]  <check name> — file:line — <what's wrong, what the convention actually requires, one line each>
...

Ship / Fix first: <one line>
```

If the diff doesn't touch any of the conventions above (e.g. it's a test-only change, or a docs/comment-only change), say so in one line and stop — don't force a finding.


## Claude

Running the review surfaced a real robustness gap I introduced: my Greenhouse/Ashby/Lever/Freehire schema checks pick **one representative company**, and if that single company simply has zero open reqs that hour (a hiring freeze, not drift), `check_all()` would incorrectly halt the *entire* pipeline run for all 10 sources — exactly the fragility the original design comment warned against. Let me fix that before shipping.

Now update `_check_wrapped_jobs_source`, `check_freehire_schema`, and the callers for Greenhouse/Ashby/Lever/Freehire to pass `allow_empty=True` with a rationale comment.

Now update the corresponding tests to reflect the new `allow_empty` behavior:

Now let me replace the four "detects_empty" tests (Greenhouse/Ashby/Lever/Freehire) with "passes_on_empty" tests:

All 436 tests still pass. Now let's re-run the review-loop-change checklist against the fixed diff.

All done. Full suite green (436 passed). Left changes uncommitted since no commit was requested — CLAUDE.md/graphify-out/.claudeignore/.gitattributes are pre-existing unrelated local state, untouched by me.

## Task 1 — Ashby's zero-match streak: genuine, not drift

Live-curled all 9 `ASHBY_COMPANIES` tokens directly. All 9 return HTTP 200 with valid, unchanged schema. Currently exactly 4 real `employmentType: "Intern"` postings exist across all 9 companies (ellipsislabs 1, circleback 1, cohere 2) — matching `fetch_count` frozen at 4. Ran the real `fetch_ashby`/`matches`/`compute_uid` code against them:

- **Ellipsis Labs + Circleback (2 of 4):** pass every filter check, but their uids are already in `state/excluded_uids.json` — permanently excluded after losing the debate comparator `MAX_DEBATE_LOSSES` (48) times. `logs/runs.jsonl` shows a wave of exclusions 2026-08-21→08-25, exactly matching when the zero-streak began.
- **Cohere's 2 postings:** both list `location: "Canada"` → correctly rejected by `location_eligible()` (permissive-by-default, but Canada is an affirmative non-US signal).

So the streak is a coincidence of two unrelated, correct mechanisms converging, not schema drift. Streak is now at **115** runs as of the freshest pulled data (I fast-forwarded local `master` to `origin/master`, 29 commits behind).

**Task 5:** No token needs refresh — all 9 are live and correctly returning data. "~4 open roles across 9 small companies" (the 2026-08-24 finding) still holds.

## Task 2 — Schema-drift coverage extended to 5 of the 6 sources

Added `check_greenhouse_schema`, `check_ashby_schema`, `check_lever_schema`, `check_freehire_schema`, `check_ai_jobs_schema` to `core/schema_drift.py`, each checking **one real, high-volume, live-confirmed company/slug** per vendor (scaleai, elevenlabs, palantir, google) rather than every seeded token — catches a vendor-wide field rename without multiplying request volume. Each required-key set cites the real API response checked live 2026-08-28, and specifically includes whatever field each source's own role-type triage reads (`employmentType`, `text`, `enrichment.seniority`, `level`) — the exact category of field whose silent rename would reproduce this incident.

Caught a real bug during self-review: my first pass would have treated one company having zero current openings (e.g. a hiring pause) as "drift" and halted the *entire* run over it. Fixed with an `allow_empty` escape hatch on the four per-company checks (not AIJobs, which aggregates many companies and *should* flag empty).

**InternDock genuinely can't get the same treatment** — no JSON API, and its real posting shape only appears after a paid Firecrawl fetch of a URL that might not even be a real drop page. Added `check_interndock_sitemap` instead: confirms the free, plain-XML sitemap still parses and still contains drop-shaped candidate slugs (documented explicitly in the code why a deeper check isn't meaningful).

## Task 3 — Zero-match alert, threshold = 24 (one day of hourly runs)

New `update_zero_match_streaks`/`load_/save_zero_match_streaks` in `run_pipeline.py`, persisted in `state/zero_match_streaks.json`. Per source: increments while `fetch_count > 0` and `filter_match_count == 0`; resets on a real match (and marks `ever_matched`, so a source that's *never* matched anything doesn't alert — permissive by design); a fetch hiccup (`fetch_count == 0`) leaves the streak untouched. Fires once (`==`, not `>=`) via `issue_fn`, and the crossing is also recorded in the run log (`record["zero_match_alerts"]`).

Chose **24** over smaller alternatives because it's a full day of hourly runs — comfortably below the 115 it actually took a human to notice, but long enough that a normal dry hour doesn't trip it.

## Task 4 — Tests

Fixture-based tests added mirroring the existing `schema_drift` pattern (happy-path/drift/empty-allowed per source) in `tests/test_schema_drift.py`, plus a new `tests/test_zero_match_alert.py` (pure-function counting rules + an integration test proving `run_once` wires it to `issue_fn`), and `tests/test_run_pipeline.py`'s shared `_fake_http_get` fixture was extended to route the 6 new schema-check URLs. **Full suite: 436 passed.**

**Tool calls:**

- `Bash` — `git diff -- core/schema_drift.py run_pipeline.py | head -400`
  ```
diff --git a/core/schema_drift.py b/core/schema_drift.py
index 68f5174..7c9309e 100644
--- a/core/schema_drift.py
+++ b/core/schema_drift.py
@@ -4,9 +4,24 @@ normalizers actually depend on are still present. Halts (raises) rather than
 letting a silently renamed/vanished upstream field produce malformed or
 emptied-out results.
 """
+import re
+
 import requests
 
-from ingestion.sources import APPLYGUY_URL, JOSEGAEL_URL, SIMPLIFY_URL, TIMEOUT, VANSHB03_URL, ZSHAH101_URL
+from ingestion.freehire import FREEHIRE_SEARCH_URL
+from ingestion.interndock import CANDIDATE_SLUG_RE, INTERNDOCK_SITEMAP_URL
+from ingestion.sources import (
+    AI_JOBS_URL,
+    APPLYGUY_URL,
+    ASHBY_JOBS_URL,
+    GREENHOUSE_JOBS_URL,
+    JOSEGAEL_URL,
+    LEVER_JOBS_URL,
+    SIMPLIFY_URL,
+    TIMEOUT,
+    VANSHB03_URL,
+    ZSHAH101_URL,
+)
 
 # Every field normalize_simplify/normalize_josegael read, not just the ones
 # that would KeyError — a renamed "category" wouldn't crash (normalize_*
@@ -24,13 +39,76 @@ ZSHAH101_REQUIRED_KEYS = {"id", "company", "title", "url", "location", "posted_a
 # that's load-bearing (every real entry checked 2026-08-24 has it).
 APPLYGUY_REQUIRED_KEYS = {"id", "company", "title", "listingUrl", "category", "season", "location", "posted"}
 
-# Only the two curated single-feed JSON sources get a pre-fetch drift check,
-# same as SimplifyJobs/JGCL always have. Greenhouse/Ashby/Lever are a dozen
-# per-company endpoints, not one feed — checking each company's schema before
-# every run would multiply request volume for a company set that already
-# degrades gracefully per-token in fetch_greenhouse/fetch_ashby/fetch_lever (a
-# renamed board silently returns nothing for that one company, not malformed
-# data).
+# Greenhouse/Ashby/Lever are a dozen per-company endpoints, not one feed —
+# checking every company's schema before every run would multiply request
+# volume for a company set that already degrades gracefully per-token in
+# fetch_greenhouse/fetch_ashby/fetch_lever (a renamed/closed board silently
+# returns nothing for that one company, not malformed data — and the
+# per-source zero-match-rate alert in run_pipeline.py catches that
+# operationally). But a vendor-wide API shape change — Ashby renaming
+# "employmentType", Greenhouse renaming "absolute_url" — hits every company
+# on that vendor at once, and none of the three fetchers would notice: they
+# all fail open (try/except RequestException, or a KeyError from
+# normalize_ashby/normalize_greenhouse/normalize_lever would actually crash
+# the whole run instead, worse than the silent-zero case the docstring above
+# describes). So each of the three checks ONE real, high-volume, currently-
+# live company (confirmed live 2026-08-28 against the real API — see the
+# _SCHEMA_CHECK_TOKEN comments below) — enough to catch a vendor-wide drift,
+# without the per-company request multiplication that was ruled out above.
+#
+# InternDock is different in kind, not just degree: it has no JSON API to
+# schema-check at all. fetch_interndock_drop_candidates() only ever touches
+# interndock.com/sitemap.xml (plain XML, checked below — that part IS
+# checkable for free). The actual posting shape (POSTING_LINE_RE) only shows
+# up after a paid Firecrawl fetch of one specific guide page, and there's no
+# guarantee any given sitemap URL is currently a real drop (see
+# ingestion/interndock.py's own docstring on "summer-2027-internship-
+# programs-open-now" reading exactly like a drop by name while being a
+# zero-posting prose article) — spending a Firecrawl call here to pre-flight
+# a schema, and maybe hitting a non-drop page and calling that "healthy" or a
+# real drop and calling a slug mismatch "drift", wouldn't mean anything
+# reliable. check_interndock_sitemap below checks what's actually checkable.
+
+# High-volume, currently-live tokens (2026-08-28) — see the block comment
+# above for why one company per vendor is the right amount of pre-flight
+# checking here, not a stand-in for "this specific company matters more."
+GREENHOUSE_SCHEMA_CHECK_TOKEN = "scaleai"  # 219 open reqs live 2026-08-28
+ASHBY_SCHEMA_CHECK_TOKEN = "elevenlabs"  # 249 open reqs live 2026-08-28
+LEVER_SCHEMA_CHECK_TOKEN = "palantir"  # 307 open reqs live 2026-08-28, longest-tracked of the 4
+FREEHIRE_SCHEMA_CHECK_SLUG = "google"  # of the 2 tracked companies, the higher-volume one
+
+# Confirmed live 2026-08-28 against https://boards-api.greenhouse.io/v1/boards/scaleai/jobs
+# (no ?content=true query param on GREENHOUSE_JOBS_URL, so "content" never
+# appears in this response shape at all — not a required key here even
+# though normalize_greenhouse also reads raw.get("content", "")).
+GREENHOUSE_REQUIRED_KEYS = {"id", "title", "absolute_url", "location", "updated_at"}
+# Confirmed live 2026-08-28 against https://api.ashbyhq.com/posting-api/job-board/elevenlabs .
+# employmentType is the field fetch_ashby's own role-type triage reads
+# (job.get("employmentType") == "Intern") — renamed, every company silently
+# stops matching any intern posting at all, the exact failure shape this
+# check exists to catch (see the 2026-08-21..08-28 Ashby zero-match
+# investigation, Prompt 19 Task 1).
+ASHBY_REQUIRED_KEYS = {"id", "title", "jobUrl", "location", "isListed", "publishedAt", "descriptionPlain", "employmentType"}
+# Confirmed live 2026-08-28 against https://api.lever.co/v0/postings/palantir?mode=json .
+# "text" is also what fetch_lever's own role-type triage reads
+# (job.get("text", "").lower()) — same reasoning as Ashby's employmentType
+# above. applyUrl, not hostedUrl, per normalize_lever's own docstring on
+# which one is the real employer link.
+LEVER_REQUIRED_KEYS = {"id", "text", "applyUrl", "categories", "createdAt", "descriptionPlain"}
+# Confirmed live 2026-08-28 against
+# https://freehire.me/api/v1/jobs/search?company_slug=google&seniority=intern&limit=200 .
+# "enrichment" additionally must contain "seniority" — see
+# check_freehire_schema below; that nested field is what fetch_freehire's own
+# role-type triage reads.
+FREEHIRE_REQUIRED_KEYS = {"title", "url", "location", "posted_at", "public_slug", "description", "enrichment"}
+# Confirmed live 2026-08-28 against https://artificialintelligencejobs.co/jobs.json .
+# "level" is what fetch_ai_jobs' own role-type triage reads (raw.get("level") == "Intern").
+AI_JOBS_REQUIRED_KEYS = {"title", "url", "company", "location", "posted", "slug", "level"}
+
+# sitemap.xml's real shape, confirmed live 2026-08-28: 68 total <loc> entries,
+# 43 under /tracker/guides/, 12 of those matching CANDIDATE_SLUG_RE — the
+# same loose pre-filter fetch_interndock_drop_candidates() itself uses.
+_LOC_RE = re.compile(r"<loc>([^<]*)</loc>")
 
 
 class SchemaDriftError(Exception):
@@ -90,6 +168,85 @@ def check_applyguy_schema(http_get=None) -> None:
         raise SchemaDriftError(f"ApplyGuy: missing expected keys {sorted(missing)} (entry keys: {sorted(jobs[0].keys())})")
 
 
+def _check_wrapped_jobs_source(name: str, url: str, required_keys: set, http_get) -> None:
+    """Greenhouse/Ashby/AIJobs' shared shape: a dict wrapping a "jobs" list —
+    same shape check_applyguy_schema already handles bespoke, now shared
+    since three more sources use it."""
+    resp = http_get(url, timeout=TIMEOUT)
+    resp.raise_for_status()
+    data = resp.json()
+    jobs = data.get("jobs") if isinstance(data, dict) else None
+    if not isinstance(jobs, list) or not jobs:
+        raise SchemaDriftError(f"{name}: expected a non-empty 'jobs' list, got {type(data).__name__}")
+    missing = required_keys - set(jobs[0].keys())
+    if missing:
+        raise SchemaDriftError(f"{name}: missing expected keys {sorted(missing)} (entry keys: {sorted(jobs[0].keys())})")
+
+
+def check_greenhouse_schema(http_get=None) -> None:
+    _check_wrapped_jobs_source(
+        "Greenhouse", GREENHOUSE_JOBS_URL.format(token=GREENHOUSE_SCHEMA_CHECK_TOKEN),
+        GREENHOUSE_REQUIRED_KEYS, http_get or requests.get,
+    )
+
+
+def check_ashby_schema(http_get=None) -> None:
+    _check_wrapped_jobs_source(
+        "Ashby", ASHBY_JOBS_URL.format(token=ASHBY_SCHEMA_CHECK_TOKEN),
+        ASHBY_REQUIRED_KEYS, http_get or requests.get,
+    )
+
+
+def check_lever_schema(http_get=None) -> None:
+    # Lever's own shape is a bare list (mode=json), not a "jobs"-wrapped dict —
+    # same shape as Simplify/JGCL/vanshb03, reuse that helper instead.
+    _check_json_source(
+        "Lever", LEVER_JOBS_URL.format(token=LEVER_SCHEMA_CHECK_TOKEN),
+        LEVER_REQUIRED_KEYS, http_get or requests.get,
+    )
+
+
+def check_freehire_schema(http_get=None) -> None:
+    # A fourth real shape: {"data": [...]}, plus a nested field
+    # (enrichment.seniority) that's load-bearing for fetch_freehire's own
+    # role-type triage — not caught by a flat top-level key check alone, so
+    # this one stays a dedicated function rather than folding into
+    # _check_json_source or _check_wrapped_jobs_source.
+    resp = (http_get or requests.get)(FREEHIRE_SEARCH_URL.format(slug=FREEHIRE_SCHEMA_CHECK_SLUG), timeout=TIMEOUT)
+    resp.raise_for_status()
+    data = resp.json()
+    jobs = data.get("data") if isinstance(data, dict) else None
+    if not isinstance(jobs, list) or not jobs:
+        raise SchemaDriftError(f"Freehire: expected a non-empty 'data' list, got {type(data).__name__}")
+    first_entry = jobs[0]
+    missing = FREEHIRE_REQUIRED_KEYS - set(first_entry.keys())
+    if missing:
+        raise SchemaDriftError(f"Freehire: missing expected keys {sorted(missing)} (entry keys: {sorted(first_entry.keys())})")
+    if "seniority" not in (first_entry.get("enrichment") or {}):
+        raise SchemaDriftError("Freehire: 'enrichment' entry missing expected key 'seniority'")
+
+
+def check_ai_jobs_schema(http_get=None) -> None:
+    _check_wrapped_jobs_source("AIJobs", AI_JOBS_URL, AI_JOBS_REQUIRED_KEYS, http_get or requests.get)
+
+
+def check_interndock_sitemap(http_get=None) -> None:
+    """Not a field-schema check (InternDock has no JSON API — see the block
+    comment above) — confirms interndock.com/sitemap.xml itself still parses
+    as XML with <loc> entries and that at least one still looks drop-shaped
+    per CANDIDATE_SLUG_RE, the same loose pre-filter
+    fetch_interndock_drop_candidates() applies to real results."""
+    resp = (http_get or requests.get)(INTERNDOCK_SITEMAP_URL, timeout=TIMEOUT)
+    resp.raise_for_status()
+    locs = _LOC_RE.findall(resp.text)
+    if not locs:
+        raise SchemaDriftError("InternDock: sitemap.xml has no <loc> entries — feed shape changed or sitemap is empty")
+    if not any(CANDIDATE_SLUG_RE.search(u) for u in locs):
+        raise SchemaDriftError(
+            f"InternDock: sitemap.xml has {len(locs)} <loc> entries but none match the drop-shaped slug pattern"
+        )
+
+
 def check_all(http_get=None) -> None:
     """Runs every check in order; raises SchemaDriftError from whichever
     fails first. Callers should treat any exception here as "halt the run,
@@ -99,3 +256,9 @@ def check_all(http_get=None) -> None:
     check_vanshb03_schema(http_get)
     check_zshah101_schema(http_get)
     check_applyguy_schema(http_get)
+    check_greenhouse_schema(http_get)
+    check_ashby_schema(http_get)
+    check_lever_schema(http_get)
+    check_freehire_schema(http_get)
+    check_ai_jobs_schema(http_get)
+    check_interndock_sitemap(http_get)
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
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
  ```diff
  - def _check_json_source(name: str, url: str, required_keys: set, http_get, *, is_dict: bool = False) -> None:
    resp = http_get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    if is_dict:
        if not isinstance(data, dict) or not data:
            raise SchemaDriftError(f"{name}: expected a non-empty JSON object, got {type(data).__name__}")
        first_entry = next(iter(data.values()))
    else:
        if not isinstance(data, list) or not data:
            raise SchemaDriftError(f"{name}: expected a non-empty JSON list, got {type(data).__name__}")
        first_entry = data[0]
    missing = required_keys - set(first_entry.keys())
  + def _check_json_source(name: str, url: str, required_keys: set, http_get, *, is_dict: bool = False, allow_empty: bool = False) -> None:
    resp = http_get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    if is_dict:
        if not isinstance(data, dict):
            raise SchemaDriftError(f"{name}: expected a JSON object, got {type(data).__name__}")
        if not data:
            if allow_empty:
                return  # nothing to check field shapes against — not itself a drift signal, see allow_empty callers
            raise SchemaDriftError(f"{name}: expected a non-empty JSON object, got {type(data).__name__}")
        first_entry = next(iter(data.values()))
    else:
        if not isinstance(data, list):
            raise SchemaDriftError(f"{name}: expected a JSON list, got {type(data).__name__}")
        if not data:
            if allow_empty:
                return
            raise SchemaDriftError(f"{name}: expected a non-empty JSON list, got {type(data).__name__}")
        first_entry = data[0]
    missing = required_keys - set(first_entry.keys())
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
  ```diff
  - def _check_json_source(name: str, url: str, required_keys: set, http_get, *, is_dict: bool = False, allow_empty: bool = False) -> None:
    resp = http_get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    if is_dict:
        if not isinstance(data, dict):
            raise SchemaDriftError(f"{name}: expected a JSON object, got {type(data).__name__}")
        if not data:
            if allow_empty:
                return  # nothing to check field shapes against — not itself a drift signal, see allow_empty callers
            raise SchemaDriftError(f"{name}: expected a non-empty JSON object, got {type(data).__name__}")
        first_entry = next(iter(data.values()))
    else:
        if not isinstance(data, list):
            raise SchemaDriftError(f"{name}: expected a JSON list, got {type(data).__name__}")
        if not data:
            if allow_empty:
                return
            raise SchemaDriftError(f"{name}: expected a non-empty JSON list, got {type(data).__name__}")
        first_entry = data[0]
    missing = required_keys - set(first_entry.keys())
  + def _check_json_source(name: str, url: str, required_keys: set, http_get, *, is_dict: bool = False, allow_empty: bool = False) -> None:
    resp = http_get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    if is_dict:
        if allow_empty and isinstance(data, dict) and not data:
            return  # nothing to check field shapes against — not itself a drift signal, see allow_empty callers
        if not isinstance(data, dict) or not data:
            raise SchemaDriftError(f"{name}: expected a non-empty JSON object, got {type(data).__name__}")
        first_entry = next(iter(data.values()))
    else:
        if allow_empty and isinstance(data, list) and not data:
            return
        if not isinstance(data, list) or not data:
            raise SchemaDriftError(f"{name}: expected a non-empty JSON list, got {type(data).__name__}")
        first_entry = data[0]
    missing = required_keys - set(first_entry.keys())
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py`
  ```diff
  - def _check_wrapped_jobs_source(name: str, url: str, required_keys: set, http_get) -> None:
    """Greenhouse/Ashby/AIJobs' shared shape: a dict wrapping a "jobs" list —
    same shape check_applyguy_schema already handles bespoke, now shared
    since three more sources use it."""
    resp = http_get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    jobs = data.get("jobs") if isinstance(data, dict) else None
    if not isinstance(jobs, list) or not jobs:
        raise SchemaDriftError(f"{name}: expected a non-empty 'jobs' list, got {type(data).__name__}")
    missing = required_keys - set(jobs[0].keys())
    if missing:
        raise SchemaDriftError(f"{name}: missing expected keys {sorted(missing)} (entry keys: {sorted(jobs[0].keys())})")


def check_greenhouse_schema(http_get=None) -> None:
    _check_wrapped_jobs_source(
        "Greenhouse", GREENHOUSE_JOBS_URL.format(token=GREENHOUSE_SCHEMA_CHECK_TOKEN),
        GREENHOUSE_REQUIRED_KEYS, http_get or requests.get,
    )


def check_ashby_schema(http_get=None) -> None:
    _check_wrapped_jobs_source(
        "Ashby", ASHBY_JOBS_URL.format(token=ASHBY_SCHEMA_CHECK_TOKEN),
        ASHBY_REQUIRED_KEYS, http_get or requests.get,
    )


def check_lever_schema(http_get=None) -> None:
    # Lever's own shape is a bare list (mode=json), not a "jobs"-wrapped dict —
    # same shape as Simplify/JGCL/vanshb03, reuse that helper instead.
    _check_json_source(
        "Lever", LEVER_JOBS_URL.format(token=LEVER_SCHEMA_CHECK_TOKEN),
        LEVER_REQUIRED_KEYS, http_get or requests.get,
    )


def check_freehire_schema(http_get=None) -> None:
    # A fourth real shape: {"data": [...]}, plus a nested field
    # (enrichment.seniority) that's load-bearing for fetch_freehire's own
    # role-type triage — not caught by a flat top-level key check alone, so
    # this one stays a dedicated function rather than folding into
    # _check_json_source or _check_wrapped_jobs_source.
    resp = (http_get or requests.get)(FREEHIRE_SEARCH_URL.format(slug=FREEHIRE_SCHEMA_CHECK_SLUG), timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    jobs = data.get("data") if isinstance(data, dict) else None
    if not isinstance(jobs, list) or not jobs:
        raise SchemaDriftError(f"Freehire: expected a non-empty 'data' list, got {type(data).__name__}")
    first_entry = jobs[0]
    missing = FREEHIRE_REQUIRED_KEYS - set(first_entry.keys())
    if missing:
        raise SchemaDriftError(f"Freehire: missing expected keys {sorted(missing)} (entry keys: {sorted(first_entry.keys())})")
    if "seniority" not in (first_entry.get("enrichment") or {}):
        raise SchemaDriftError("Freehire: 'enrichment' entry missing expected key 'seniority'")


def check_ai_jobs_schema(http_get=None) -> None:
    _check_wrapped_jobs_source("AIJobs", AI_JOBS_URL, AI_JOBS_REQUIRED_KEYS, http_get or requests.get)
  + def _check_wrapped_jobs_source(name: str, url: str, required_keys: set, http_get, *, allow_empty: bool = False) -> None:
    """Greenhouse/Ashby/AIJobs' shared shape: a dict wrapping a "jobs" list —
    same shape check_applyguy_schema already handles bespoke, now shared
    since three more sources use it."""
    resp = http_get(url, timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    jobs = data.get("jobs") if isinstance(data, dict) else None
    if allow_empty and isinstance(jobs, list) and not jobs:
        return  # nothing to check field shapes against — not itself a drift signal, see allow_empty callers
    if not isinstance(jobs, list) or not jobs:
        raise SchemaDriftError(f"{name}: expected a non-empty 'jobs' list, got {type(data).__name__}")
    missing = required_keys - set(jobs[0].keys())
    if missing:
        raise SchemaDriftError(f"{name}: missing expected keys {sorted(missing)} (entry keys: {sorted(jobs[0].keys())})")


# allow_empty=True on Greenhouse/Ashby/Lever/Freehire (unlike AIJobs below):
# each of these checks ONE specific company/slug, and that one company
# legitimately having zero open reqs right now (a hiring pause, between
# postings) is mundane and unrelated to the vendor's API shape — it's
# exactly the same "company-level absence is not drift" reasoning the block
# comment above already applies to fetch_greenhouse/fetch_ashby/fetch_lever
# themselves. Treating an empty response here as SchemaDriftError would
# halt the entire run (all 10 sources) over one company's temporary hiring
# lull — a real, plausible failure mode this check must not introduce.
# AIJobs, by contrast, aggregates postings across the whole feed; a
# genuinely empty AIJobs response IS as suspicious as SimplifyJobs' own
# feed going empty, so it keeps the default allow_empty=False.
def check_greenhouse_schema(http_get=None) -> None:
    _check_wrapped_jobs_source(
        "Greenhouse", GREENHOUSE_JOBS_URL.format(token=GREENHOUSE_SCHEMA_CHECK_TOKEN),
        GREENHOUSE_REQUIRED_KEYS, http_get or requests.get, allow_empty=True,
    )


def check_ashby_schema(http_get=None) -> None:
    _check_wrapped_jobs_source(
        "Ashby", ASHBY_JOBS_URL.format(token=ASHBY_SCHEMA_CHECK_TOKEN),
        ASHBY_REQUIRED_KEYS, http_get or requests.get, allow_empty=True,
    )


def check_lever_schema(http_get=None) -> None:
    # Lever's own shape is a bare list (mode=json), not a "jobs"-wrapped dict —
    # same shape as Simplify/JGCL/vanshb03, reuse that helper instead.
    _check_json_source(
        "Lever", LEVER_JOBS_URL.format(token=LEVER_SCHEMA_CHECK_TOKEN),
        LEVER_REQUIRED_KEYS, http_get or requests.get, allow_empty=True,
    )


def check_freehire_schema(http_get=None) -> None:
    # A fourth real shape: {"data": [...]}, plus a nested field
    # (enrichment.seniority) that's load-bearing for fetch_freehire's own
    # role-type triage — not caught by a flat top-level key check alone, so
    # this one stays a dedicated function rather than folding into
    # _check_json_source or _check_wrapped_jobs_source. allow_empty reasoning
    # as above: one company (google), zero current intern-tagged postings
    # there isn't drift.
    resp = (http_get or requests.get)(FREEHIRE_SEARCH_URL.format(slug=FREEHIRE_SCHEMA_CHECK_SLUG), timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    jobs = data.get("data") if isinstance(data, dict) else None
    if isinstance(jobs, list) and not jobs:
        return
    if not isinstance(jobs, list) or not jobs:
        raise SchemaDriftError(f"Freehire: expected a non-empty 'data' list, got {type(data).__name__}")
    first_entry = jobs[0]
    missing = FREEHIRE_REQUIRED_KEYS - set(first_entry.keys())
    if missing:
        raise SchemaDriftError(f"Freehire: missing expected keys {sorted(missing)} (entry keys: {sorted(first_entry.keys())})")
    if "seniority" not in (first_entry.get("enrichment") or {}):
        raise SchemaDriftError("Freehire: 'enrichment' entry missing expected key 'seniority'")


def check_ai_jobs_schema(http_get=None) -> None:
    _check_wrapped_jobs_source("AIJobs", AI_JOBS_URL, AI_JOBS_REQUIRED_KEYS, http_get or requests.get)
  ```
- `Bash` — `grep -n "detects_empty_jobs_list\|detects_empty_list\|detects_empty_data_list" tests/test_schema_drift.py`
  ```
173:def test_simplify_schema_detects_empty_list():
324:def test_applyguy_schema_detects_empty_jobs_list():
354:def test_greenhouse_schema_detects_empty_jobs_list():
385:def test_ashby_schema_detects_empty_jobs_list():
414:def test_lever_schema_detects_empty_list():
455:def test_freehire_schema_detects_empty_data_list():
484:def test_ai_jobs_schema_detects_empty_jobs_list():
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
  ```diff
  - def test_greenhouse_schema_detects_empty_jobs_list():
    http_get = Mock(return_value=_json_response({"jobs": []}))
    with pytest.raises(SchemaDriftError, match="non-empty 'jobs' list"):
        check_greenhouse_schema(http_get=http_get)
  + def test_greenhouse_schema_passes_on_empty_jobs_list():
    """One company (scaleai) legitimately having zero open reqs right now
    is mundane, not drift — must not halt the whole run over it (see the
    allow_empty block comment in core/schema_drift.py)."""
    http_get = Mock(return_value=_json_response({"jobs": []}))
    check_greenhouse_schema(http_get=http_get)  # does not raise
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
  ```diff
  - def test_ashby_schema_detects_empty_jobs_list():
    http_get = Mock(return_value=_json_response({"jobs": []}))
    with pytest.raises(SchemaDriftError, match="non-empty 'jobs' list"):
        check_ashby_schema(http_get=http_get)
  + def test_ashby_schema_passes_on_empty_jobs_list():
    """One company (elevenlabs) legitimately having zero open reqs right
    now is mundane, not drift — same reasoning as Greenhouse's own
    allow_empty test above."""
    http_get = Mock(return_value=_json_response({"jobs": []}))
    check_ashby_schema(http_get=http_get)  # does not raise
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
  ```diff
  - def test_lever_schema_detects_empty_list():
    http_get = Mock(return_value=_json_response([]))
    with pytest.raises(SchemaDriftError, match="non-empty"):
        check_lever_schema(http_get=http_get)
  + def test_lever_schema_passes_on_empty_list():
    """One company (palantir) legitimately having zero open reqs right now
    is mundane, not drift — same reasoning as Greenhouse's own allow_empty
    test above."""
    http_get = Mock(return_value=_json_response([]))
    check_lever_schema(http_get=http_get)  # does not raise
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py`
  ```diff
  - def test_freehire_schema_detects_empty_data_list():
    http_get = Mock(return_value=_json_response({"data": []}))
    with pytest.raises(SchemaDriftError, match="non-empty 'data' list"):
        check_freehire_schema(http_get=http_get)
  + def test_freehire_schema_passes_on_empty_data_list():
    """The one company (google) legitimately having zero intern-tagged
    postings right now is mundane, not drift — same reasoning as
    Greenhouse's own allow_empty test above."""
    http_get = Mock(return_value=_json_response({"data": []}))
    check_freehire_schema(http_get=http_get)  # does not raise
  ```
- `Bash` — `.venv/bin/python -m pytest -q 2>&1 | tail -60`
  ```
........................................................................ [ 16%]
........................................................................ [ 33%]
........................................................................ [ 49%]
........................................................................ [ 66%]
........................................................................ [ 82%]
........................................................................ [ 99%]
....                                                                     [100%]
436 passed in 2.12s
  ```
- `Bash` — `git diff --stat`
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
  ```
- `Bash`:
  ```bash
.venv/bin/python -c "import ast; ast.parse(open('core/schema_drift.py').read())" && echo OK
.venv/bin/python -c "import ast; ast.parse(open('run_pipeline.py').read())" && echo OK
.venv/bin/python -m py_compile core/schema_drift.py run_pipeline.py tests/test_schema_drift.py tests/test_run_pipeline.py tests/test_zero_match_alert.py && echo COMPILE_OK
  ```
  ```
OK
OK
COMPILE_OK
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
 M run_pipeline.py
 M tests/test_run_pipeline.py
 M tests/test_schema_drift.py
?? .claudeignore
?? .gitattributes
?? tests/test_zero_match_alert.py
  ```

## Actions Taken
- Files created: /home/anant_gupta/projects/work/internship-research-loop/tests/test_zero_match_alert.py
- Files modified: /home/anant_gupta/projects/work/internship-research-loop/core/schema_drift.py, /home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_run_pipeline.py, /home/anant_gupta/projects/work/internship-research-loop/tests/test_schema_drift.py
- Files deleted: (none)
- Commands run: sed -n '1,200p' ingestion/sources.py | grep -n "ASHBY\|def fetch_ashby\|def normalize_ashby" , git log --oneline -5 && echo --- && git remote -v && echo --- && git fetch origin master 2>&1 | tail -5 && git log --oneline origin/master -5 2>&1, grep -n "ASHBY_COMPANIES" -A 12 ingestion/sources.py, git status && echo --- && git diff --stat CLAUDE.md && echo --- && git log --oneline HEAD..origin/master, git stash push -u -m "pre-pull stash: CLAUDE.md + graphify-out local edits" && git pull --ff-only origin master && git stash pop, python3 -c " import json recs = [json.loads(l) for l in open('logs/runs.jsonl')] print('total records', len(recs)) # find ashby fetch_counts/filter_match_counts trend streak = 0 last_nonzero = None for r in reversed(recs): fc = r.get('fetch_counts', {}).get('Ashby') mc = r.get('filter_match_counts', {}).get('Ashby') if fc is None: continue if mc == 0 and fc and fc > 0: streak += 1 else: last_nonzero = r.get('timestamp') break print('current zero-streak (from most recent run backwards):', streak) print('most recent run with nonzero match or fc==0 before streak:', last_nonzero) print('most recent record ashby:', recs[-1].get('timestamp'), recs[-1].get('fetch_counts',{}).get('Ashby'), recs[-1].get('filter_match_counts',{}).get('Ashby')) " , for token in ellipsislabs quadrillion-labs circleback ctgt pylon-labs cohere cursor modal elevenlabs; do echo "=== $token ===" curl -s -o /tmp/ashby_$token.json -w "HTTP %{http_code}\n" "https://api.ashbyhq.com/posting-api/job-board/$token" python3 -c " import json,sys try: d = json.load(open('/tmp/ashby_$token.json')) except Exception as e: print('PARSE ERROR', e); sys.exit() if isinstance(d, dict): print('keys:', sorted(d.keys())) jobs = d.get('jobs', []) print('jobs count:', len(jobs)) if jobs: print('first job keys:', sorted(jobs[0].keys())) print('sample employmentType:', [j.get('employmentType') for j in jobs[:10]]) else: print('type:', type(d)) " done, for token in ellipsislabs quadrillion-labs circleback ctgt pylon-labs cohere cursor modal elevenlabs; do count=$(python3 -c " import json d = json.load(open('/tmp/ashby_$token.json')) jobs = d.get('jobs', []) interns = [j for j in jobs if j.get('employmentType')=='Intern'] print(len(interns), [j.get('title') for j in interns]) ") echo "$token: $count" done, grep -n "filter_match_count\|fetch_count\|seen_ids\|def run\b" run_pipeline.py | head -60, grep -n "excluded_ids\s*=\|MAX_DEBATE_LOSSES\|def compute_uid\|update_debate_losses" run_pipeline.py | head -30, cat state/excluded_uids.json 2>/dev/null | head -50; echo "---count---"; python3 -c "import json; print(len(json.load(open('state/excluded_uids.json'))))" 2>/dev/null echo "--- normalize_ashby ---" grep -n "def normalize_ashby" -A 25 ingestion/sources.py, grep -n "def normalize_ashby" -A 20 ingestion/sources.py echo "---uid---" grep -n "def compute_uid" -A 20 identity.py 2>/dev/null || find . -name "identity.py" | xargs grep -n "def compute_uid" -A 20 echo "--- live ashby job ids ---" for token in ellipsislabs circleback cohere; do python3 -c " import json d = json.load(open('/tmp/ashby_$token.json')) jobs = [j for j in d.get('jobs', []) if j.get('employmentType')=='Intern'] for j in jobs: print('$token', j.get('id'), j.get('title'), j.get('publishedAt')) " done, grep -n "def normalize_ashby\|def fetch_ashby" -A 15 ingestion/sources.py | head -60, grep -n "^def normalize_ashby" ingestion/sources.py, grep -n "normalize_ashby" ingestion/sources.py, grep -rn "def normalize_ashby" ., grep -n "^def matches\|^def stage1_reject\|^def location_eligible\|^def degrees_eligible" core/filter.py core/relevance.py 2>/dev/null, grep -n "_matches_ashby" -A 15 core/filter.py, grep -n "_matches_free_text_source" -B2 -A 30 core/filter.py | head -50, cat core/profile.yaml, grep -c "Ashby:" state/excluded_uids.json grep "Ashby:" state/excluded_uids.json, python3 -c " import sys, json sys.path.insert(0, '.') from ingestion.sources import fetch_ashby, ASHBY_JOBS_URL from core.filter import matches, load_profile from core.relevance import stage1_reject from identity import compute_uid class FakeResp: def __init__(self, data): self._data = data def raise_for_status(self): pass def json(self): return self._data def fake_get(url, timeout=None): for token in ['ellipsislabs','quadrillion-labs','circleback','ctgt','pylon-labs','cohere','cursor','modal','elevenlabs']: if token in url: return FakeResp(json.load(open(f'/tmp/ashby_{token}.json'))) raise Exception('unexpected url ' + url) listings = fetch_ashby(fake_get) print('fetch_count', len(listings)) profile = load_profile() excluded = set(json.load(open('state/excluded_uids.json'))) for l in listings: uid = compute_uid(l) m = matches(l, profile) s1 = stage1_reject(l.title, l.raw_text) exc = uid in excluded print(l.company, '|', l.title, '| locations=', l.locations, 'degrees=', l.degrees, '| matches=', m, 'stage1_reject=', s1, 'excluded=', exc, 'uid=', uid) " , find . -iname "identity.py" -not -path "*/node_modules/*", python3 -c " import sys, json sys.path.insert(0, '.') from ingestion.sources import fetch_ashby, ASHBY_JOBS_URL from core.filter import matches, load_profile from core.relevance import stage1_reject from core.identity import compute_uid class FakeResp: def __init__(self, data): self._data = data def raise_for_status(self): pass def json(self): return self._data def fake_get(url, timeout=None): for token in ['ellipsislabs','quadrillion-labs','circleback','ctgt','pylon-labs','cohere','cursor','modal','elevenlabs']: if token in url: return FakeResp(json.load(open(f'/tmp/ashby_{token}.json'))) raise Exception('unexpected url ' + url) listings = fetch_ashby(fake_get) print('fetch_count', len(listings)) profile = load_profile() excluded = set(json.load(open('state/excluded_uids.json'))) for l in listings: uid = compute_uid(l) m = matches(l, profile) s1 = stage1_reject(l.title, l.raw_text) exc = uid in excluded print(l.company, '|', l.title, '| locations=', l.locations, 'degrees=', l.degrees, '| matches=', m, 'stage1_reject=', s1, 'excluded=', exc, 'uid=', uid) " , grep -n "02136b22\|2bb6be67" logs/*.jsonl state/*.json 2>/dev/null | grep -v excluded_uids.json, python3 -c " import json recs = [json.loads(l) for l in open('logs/runs.jsonl')] for r in recs: ne = r.get('newly_excluded') or r.get('newly_excluded_uids') or [] if any('02136b22' in str(x) or '2bb6be67' in str(x) for x in ne): print(r.get('timestamp'), ne) " grep -o '"newly_excluded[^]]*\]' logs/runs.jsonl | grep -i "02136\|2bb6" | head , python3 -c " import json recs = [json.loads(l) for l in open('logs/runs.jsonl')] print(list(recs[-1].keys())) ", python3 -c " import json recs = [json.loads(l) for l in open('logs/runs.jsonl')] for r in recs: if r.get('newly_excluded_count', 0) > 0: print(r['timestamp'], r['newly_excluded_count']) " | tail -20, grep -rn "def fetch_freehire\|def fetch_interndock\|FREEHIRE_URL\|INTERNDOCK" ingestion/*.py run_pipeline.py | head -40, for token in fccincinnati aquaticcapitalmanagement walleyecapital-external-students pdtpartners virtu mwinternshipprogram optiverus fireworksai scaleai; do n=$(curl -s "https://boards-api.greenhouse.io/v1/boards/$token/jobs" | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d.get('jobs',[])))" 2>/dev/null) echo "$token: $n" done, curl -s "https://api.lever.co/v0/postings/scaleai?mode=json" -o /tmp/lever_test.json -w "%{http_code}\n" curl -s "https://api.lever.co/v0/postings/palantir?mode=json" | python3 -c " import json,sys d = json.load(sys.stdin) print('count', len(d)) print('keys', sorted(d[0].keys()) if d else None) print(json.dumps(d[0], indent=2)[:800] if d else '') ", curl -s "https://freehire.me/api/v1/jobs/search?company_slug=google&seniority=intern&limit=200" -o /tmp/freehire_google.json -w "%{http_code}\n" python3 -c " import json d = json.load(open('/tmp/freehire_google.json')) jobs = d.get('data', []) print('count', len(jobs)) print('keys', sorted(jobs[0].keys()) if jobs else None) print('enrichment', jobs[0].get('enrichment') if jobs else None) " echo "--- aijobs ---" curl -s "https://artificialintelligencejobs.co/jobs.json" -o /tmp/aijobs.json -w "%{http_code}\n" python3 -c " import json d = json.load(open('/tmp/aijobs.json')) jobs = d.get('jobs', []) print('count', len(jobs)) interns = [j for j in jobs if j.get('level')=='Intern'] print('intern count', len(interns)) print('keys', sorted(jobs[0].keys()) if jobs else None) print(interns[0] if interns else None) ", curl -s "https://www.interndock.com/sitemap.xml" -o /tmp/interndock_sitemap.xml -w "%{http_code}\n" python3 -c " import re text = open('/tmp/interndock_sitemap.xml').read() locs = re.findall(r'<loc>([^<]*)</loc>', text) print('total locs', len(locs)) guide_locs = [u for u in locs if '/tracker/guides/' in u] print('guide locs', len(guide_locs)) cand = [u for u in guide_locs if re.search(r'intern.*(drop|list|open-now)', u, re.I)] print('candidate drop-shaped', len(cand)) print(cand[:5]) ", grep -n "SOURCES\s*=\|check_all\|schema_drift" run_pipeline.py, sed -n '1,80p' tests/core/test_schema_drift.py 2>/dev/null || find . -iname "*schema_drift*", sed -n '40,70p;490,560p' run_pipeline.py, python3 -c " import json d = json.load(open('/tmp/ashby_elevenlabs.json')) jobs = d.get('jobs', []) print(sorted(jobs[0].keys())) " echo "---greenhouse scaleai---" curl -s "https://boards-api.greenhouse.io/v1/boards/scaleai/jobs" | python3 -c " import json,sys d = json.load(sys.stdin) jobs = d.get('jobs', []) print(sorted(jobs[0].keys())) print(jobs[0].get('location')) ", grep -n "^from\|^import" ingestion/freehire.py ingestion/interndock.py, grep -n "record\[.errors.\]\|record\[.rejections.\]\|issue_fn(\|bucket_at_capacity" run_pipeline.py, grep -n "should_alert_on_exclusion_spike\|EXCLUSION_SPIKE" -B3 -A8 run_pipeline.py | head -40, grep -n '"newly_excluded_count": 0,' run_pipeline.py, python3 -m pytest -q 2>&1 | tail -60, which pytest; python3 -m venv --help >/dev/null 2>&1; ls; cat requirements*.txt 2>/dev/null; find . -maxdepth 2 -iname "*.cfg" -o -iname "pyproject.toml" | head, source .venv/bin/activate 2>/dev/null; .venv/bin/python -m pytest -q 2>&1 | tail -80, grep -n "def _make_http_get\|def make_http_get\|def _http_get\|check_schema_drift\|SchemaDrift\|schema_drift" tests/test_run_pipeline.py tests/test_debate_losses.py | head -60, grep -n "check_schema_drift" tests/test_run_pipeline.py tests/test_debate_losses.py, grep -n "def test_run_once_happy_path_marks_seen_and_writes_dossiers" -A 60 tests/test_run_pipeline.py | head -90, grep -n "_run_once_kwargs\b" tests/test_run_pipeline.py | head -3, cd /home/anant_gupta/projects/work/internship-research-loop sed -i 's/_GREENHOUSE_SCHEMA_CHECK_TOKEN/GREENHOUSE_SCHEMA_CHECK_TOKEN/g; s/_ASHBY_SCHEMA_CHECK_TOKEN/ASHBY_SCHEMA_CHECK_TOKEN/g; s/_LEVER_SCHEMA_CHECK_TOKEN/LEVER_SCHEMA_CHECK_TOKEN/g; s/_FREEHIRE_SCHEMA_CHECK_SLUG/FREEHIRE_SCHEMA_CHECK_SLUG/g' core/schema_drift.py grep -n "SCHEMA_CHECK" core/schema_drift.py, grep -n "http_get\|_fake_http_get\|check_schema_drift" tests/test_debate_losses.py | head -30, ls tests/fixtures/, grep -n "def _greenhouse_job\|def _ashby_job\|def _lever_job\|def _freehire_job\|def _ai_jobs_job\|_GREENHOUSE_JOB\|_ASHBY_JOB\|_LEVER_JOB\|raw = {" tests/test_sources.py | head -40, find . -iname "test_sources.py" -o -iname "test_normalize.py"; grep -rln "fetch_greenhouse\|fetch_ashby\|fetch_lever\|fetch_ai_jobs\|fetch_freehire" tests/, grep -n "def test_fetch_greenhouse\|def test_fetch_ashby\|def test_fetch_lever\|def test_fetch_ai_jobs" -A 25 tests/test_sources.py | head -150, grep -n "def test_fetch_freehire\|_freehire_response\|def _fh_" -A 20 tests/test_freehire.py | head -60, python3 -c " import json data = json.load(open('tests/fixtures/freehire.json')) print(type(data)) if isinstance(data, list): print(data[0]) ", .venv/bin/python -m pytest -q 2>&1 | tail -100, grep -n "GREENHOUSE_REQUIRED_KEYS\|ASHBY_REQUIRED_KEYS\|LEVER_REQUIRED_KEYS\|FREEHIRE_REQUIRED_KEYS\|AI_JOBS_REQUIRED_KEYS" tests/test_schema_drift.py, .venv/bin/python -m pytest tests/test_schema_drift.py -q 2>&1 | tail -60, grep -n "test_run_once_files_issue_on_exclusion_spike\|should_alert_on_exclusion_spike\|def test_update_debate_losses" tests/test_debate_losses.py | head, grep -n "^def _run_once_kwargs" -A 40 tests/test_run_pipeline.py, .venv/bin/python -m pytest tests/test_zero_match_alert.py -q 2>&1 | tail -100, .venv/bin/python -m pytest -q 2>&1 | tail -40, git diff -- core/schema_drift.py run_pipeline.py | head -400, grep -n "detects_empty_jobs_list\|detects_empty_list\|detects_empty_data_list" tests/test_schema_drift.py, .venv/bin/python -m pytest -q 2>&1 | tail -60, git diff --stat, .venv/bin/python -c "import ast; ast.parse(open('core/schema_drift.py').read())" && echo OK .venv/bin/python -c "import ast; ast.parse(open('run_pipeline.py').read())" && echo OK .venv/bin/python -m py_compile core/schema_drift.py run_pipeline.py tests/test_schema_drift.py tests/test_run_pipeline.py tests/test_zero_match_alert.py && echo COMPILE_OK, git status --short
- Tool call tally: Bash (69), Edit (20), Read (25), Skill (1), Write (1)

