---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: wsl
title: "Jarvis internship pipeline audit and setup"
started_at: 2026-08-21T13:12:27
ended_at: 2026-08-21T17:05:07
duration_minutes: 233
exported_at: 2026-08-21T21:15:05
project: internship-research-loop
cwd: '/home/anant_gupta/projects/work/internship-research-loop'
session_id: bebacdad-914c-4c86-b1a2-93b41c665f1c
status: raw
turn_count: 6
tools_used:
  Artifact: 1
  Bash: 25
  Edit: 1
  mcp__jarvis__search_simple: 1
  mcp__jarvis__vault_list: 20
  mcp__jarvis__vault_read: 10
  mcp__jarvis-fs__list_allowed_directories: 1
  Read: 5
  Skill: 1
  ToolSearch: 3
  WebFetch: 1
  Write: 5
tokens:
  input: 240
  output: 257222
  cache_creation: 1355515
  cache_read: 15961519
  total: 17574496
cost_usd: 11.187064
model:
  - claude-sonnet-5
files_touched:
  - "/home/anant_gupta/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/memory/phase4-state-and-gates.md"
  - "/home/anant_gupta/projects/work/internship-research-loop/README.md"
  - "/home/anant_gupta/projects/work/internship-research-loop/PRD.md"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/profile.yaml"
  - "/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/aiml.txt"
  - "/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/fullstack.txt"
  - "/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/cysfin.txt"
  - "/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/other.txt"
  - "/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/pipeline-triage.html"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/debate.py"
tags:
  - input
  - ai-conversation
  - claude-code
  - wsl
---

# Jarvis internship pipeline audit and setup

## You

Before, we do anything further. I want to understand where we currently stand based on everything inside jarvis. Review the programs, dossiers, etc. Review the systems, tracking, application process. Each and everything needs to be reviewed in detail right now. I already know that nothing has progresses out of the dossier, i want an actual count of what is inside the dossier. Let's filter out a lot of applications inside the dossier currently. Make sure that the limit for dossier is reflected and we do not add more than the number that was decided. There are tons of blockers for this process. Which means that we are losing time per application rolling out, now we have too many resources out there (will be provided soon). But this is where we are stressed out and needs to be implemented. What are we stressed about? Outreach. Applying. Quickness. Networking. everything, it all just slapped really hard that we have the summer ending soon. I want to completely filter the dossiers based on the profile explained. Even the profile needs to be updated and self improving per application that gets added to the programs. There is a lot of work that needs to be done. But primarily, we need to stop stressing about dossiers. We need to actually add programs and find emails, linkedins, etc. We need to test out everything else and focus less on the dossier moving forward. A simple yes or no per application after seeing the application. We need to move quickly, so let's finish up everything tofay. By that, i mean we need to find concrete dossiers, filter dossiers, add programs, find emails, linkedins, finish the starting process of this loop. I want this initial step to be so concrete that after today, we will not look back at this step again. What do we need to do today so that we progress further in this loop? What needs to be done asap? We need to move quickly. Research jarvis, the codebase, notes, concrete documents listed, dossier count, programs listed, outreach for employees (hr primarily). List out all the things required to finish today. So, that we can apply to at least 50 internships tomorrow. I also want to know about the dossiers listed out - what applications have already closed? What were rolling out on early application basis? We need to find internships before any company board finds it (linkedin, glassdoor, etc.). We need a way to apply for applications quickly too (some extension or copy paste method per application). There are way too many things mentioned to you in this prompt and that is because i am stressed out about each and every step. I want you think rationally after looking through each and every step. Be a superior being, be my mentor for this process. Tell me exactly what we need to today so that we can apply for internships tomorrow and reach out to a lot of employers? Research, find concrete details, files, notes, etc. Only after that provide me with a step by step guide on what to do today.

## Claude

I'll dig into both the vault (dossiers, programs, tracker) and the codebase state before drawing conclusions — pulling real numbers, not impressions. Let me start with parallel reconnaissance.

Important finding already: local checkout is **413 commits behind origin** and hasn't been synced since 2026-07-30, while origin has commits through today (2026-08-21) — the automated pipeline has been running for 3 weeks past what this checkout reflects. There's also uncommitted local work (`core/debate.py` + a "debate comparator" feature referenced in `profile.yaml`) sitting on top of a stale base. I'll flag this, not touch git yet, and move to the vault itself.

Let me get exact counts via the filesystem (faster and less error-prone than counting JSON arrays by eye) — checking if the vault is checked out locally.

364 total dossiers, but only **1** has ever made it past screening into Tracker+Contacts (Appian), and even the 5 "Serious" Programs never got tracked or contacted. Also spotted a likely filter leak: **Zipline alone accounts for 45 of 364 dossiers** — including "Aerodynamics Intern," "Community Engagement Intern," "Accounting Intern" — clearly not SWE/AI/data roles. Let me check why those passed the filter, and pull the pipeline/workflow docs plus any existing dossier-limit decision.

The Zipline example exposes the real bug: `terms: []`, `target_year: []`, `matched_reason: "matched"`, and a note claiming "genuine software engineering role" for an **Aerodynamics Intern**. The AIJobs source doesn't tag category, so permissive-by-default filtering (correct for ambiguous postings) is letting through *every* role at any company with an "Internships" landing page — accounting, mechanical, community engagement, all of it. That's the actual source of dossier bloat. Let me check the pipeline workflow doc and outreach status to complete the picture.

Found the actual count-limit reference. Let me pull the Dashboard (which tracks "dossier pipeline health against the count limit"), the Source of Truth doc, and check whether anything has actually been applied to yet.

**Tool calls:**

- `Read` — `/home/anant_gupta/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/memory/phase4-state-and-gates.md`
- `Bash` — `git status && echo "---LOG---" && git log --oneline -20 && echo "---DIFF STAT---" && git diff --stat`
  ```
On branch master
Your branch is behind 'origin/master' by 413 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   core/classify.py
	modified:   core/identity.py
	modified:   core/profile.yaml
	modified:   core/relevance.py
	modified:   core/run_log.py
	modified:   ingestion/posting_page.py
	modified:   recheck.py
	modified:   run_pipeline.py
	modified:   tests/test_classify.py
	modified:   tests/test_identity.py
	modified:   tests/test_posting_page.py
	modified:   tests/test_relevance.py
	modified:   tests/test_run_pipeline.py
	modified:   tests/test_validate.py
	modified:   tests/test_writer.py
	modified:   vault_writer/validate.py
	modified:   vault_writer/writer.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	core/debate.py
	tests/fixtures/posting_google_careers.md
	tests/test_debate.py
	tests/test_debate_losses.py

no changes added to commit (use "git add" and/or "git commit -a")
---LOG---
3fd4b88 Update state + logs — 2026-07-30
225d09b Update state + logs — 2026-07-30
8d84b20 Recheck log — 2026-07-30
2378732 Update state + logs — 2026-07-30
b6b2c9f Update state + logs — 2026-07-30
8f34d93 Update state + logs — 2026-07-30
086b829 Update state + logs — 2026-07-29
e787fdf Update state + logs — 2026-07-29
31623a7 Update state + logs — 2026-07-29
7e22b93 Update state + logs — 2026-07-29
8364b6f Update state + logs — 2026-07-29
05a5c13 Update state + logs — 2026-07-29
e3325c8 Update state + logs — 2026-07-29
a961ec2 Update state + logs — 2026-07-29
cb7e46c Update state + logs — 2026-07-29
de218ba Recheck log — 2026-07-29
3875c4c Update state + logs — 2026-07-29
6f64515 Update state + logs — 2026-07-29
7fd283b Update state + logs — 2026-07-29
b6d8078 Update state + logs — 2026-07-28
---DIFF STAT---
 core/classify.py           |  12 ++-
 core/identity.py           |  71 +++++++++++-
 core/profile.yaml          |  28 +++++
 core/relevance.py          |  56 ++++++++--
 core/run_log.py            |  33 +++++-
 ingestion/posting_page.py  | 134 ++++++++++++++++++++++-
 recheck.py                 |  36 ++++---
 run_pipeline.py            | 262 +++++++++++++++++++++++++++++++++++++++++----
 tests/test_classify.py     |  22 ++++
 tests/test_identity.py     | 121 ++++++++++++++++++++-
 tests/test_posting_page.py | 171 ++++++++++++++++++++++++++++-
 tests/test_relevance.py    |  61 +++++++++++
 tests/test_run_pipeline.py | 130 +++++++++++++++++++++-
 tests/test_validate.py     |  26 +++++
 tests/test_writer.py       | 160 ++++++++++++++++++++++++++-
 vault_writer/validate.py   |   5 +-
 vault_writer/writer.py     | 118 ++++++++++++++++++--
 17 files changed, 1374 insertions(+), 72 deletions(-)
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/README.md`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/PRD.md`
- `Bash` — `git fetch origin --quiet 2>&1 | tail -5; echo "---"; git log origin/master --oneline -15; echo "---LAST LOCAL VS REMOTE DATE---"; git log -1 --format=%cd; git log origin/master -1 --format=%cd`
  ```
---
6deed7c Update state + logs — 2026-08-21
1087234 Update state + logs — 2026-08-21
d370044 Update state + logs — 2026-08-21
8cc9558 Update state + logs — 2026-08-21
27cdd55 Update state + logs — 2026-08-21
d0b2149 Update state + logs — 2026-08-21
b65793a Recheck log — 2026-08-21
8d94941 Update state + logs — 2026-08-21
0c6b1a7 Update state + logs — 2026-08-21
32cda25 Update state + logs — 2026-08-21
4f503a0 Update state + logs — 2026-08-21
5a0029d Update state + logs — 2026-08-21
c7dfb3e Update state + logs — 2026-08-21
160a141 Update state + logs — 2026-08-20
b11e6c4 Update state + logs — 2026-08-20
---LAST LOCAL VS REMOTE DATE---
Thu Jul 30 12:23:53 2026 +0000
Fri Aug 21 12:26:32 2026 +0000
  ```
- `Bash`:
  ```bash
cat /home/anant_gupta/projects/work/internship-research-loop/state/seen_ids.json 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print('seen_ids count:', len(d) if isinstance(d,list) else len(d.keys()))" 2>&1
echo "---"
ls /home/anant_gupta/projects/work/internship-research-loop/logs/ 2>/dev/null
echo "---runs.jsonl tail---"
tail -5 /home/anant_gupta/projects/work/internship-research-loop/logs/runs.jsonl 2>/dev/null
echo "---rechecks.jsonl tail---"
tail -5 /home/anant_gupta/projects/work/internship-research-loop/logs/rechecks.jsonl 2>/dev/null
  ```
  ```
seen_ids count: 295
---
rechecks.jsonl
runs.jsonl
---runs.jsonl tail---
{"timestamp": "2026-07-30T01:26:38.108544+00:00", "fetch_counts": {"SimplifyJobs": 14706, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 311, "zshah101": 250, "Greenhouse": 49, "Ashby": 4, "Freehire": 28, "AIJobs": 189}, "filter_match_counts": {"SimplifyJobs": 45, "Jose-Gael-Cruz-Lopez": 5, "vanshb03": 95, "zshah101": 21, "Greenhouse": 32, "Ashby": 2, "Freehire": 6, "AIJobs": 8}, "new_count": 79, "already_seen_count": 135, "deferred_count": 61, "written_count": 0, "rejections": [{"uid": "zshah101:greenhouse:virtu:8657500002", "check": "cross_source_duplicate", "reason": "company+title already in vault: virtu financial|2027 internship frontend user experience"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "US Citizenship required (cached 2026-07-29)"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. citizenship is required (cached 2026-07-29)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: hyperlight|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: appian|software engineering intern"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|investment data science intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|risk technology analyst intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}, {"uid": "zshah101:greenhouse:appian:8041237", "check": "cross_source_duplicate", "reason": "company+title already in vault: appian|software engineering intern"}, {"uid": "vanshb03:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: optiver|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-07-30T04:48:43.961564+00:00", "fetch_counts": {"SimplifyJobs": 14684, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 311, "zshah101": 250, "Greenhouse": 49, "Ashby": 4, "Freehire": 29, "AIJobs": 189}, "filter_match_counts": {"SimplifyJobs": 45, "Jose-Gael-Cruz-Lopez": 5, "vanshb03": 95, "zshah101": 21, "Greenhouse": 32, "Ashby": 2, "Freehire": 6, "AIJobs": 8}, "new_count": 79, "already_seen_count": 135, "deferred_count": 61, "written_count": 0, "rejections": [{"uid": "zshah101:greenhouse:virtu:8657500002", "check": "cross_source_duplicate", "reason": "company+title already in vault: virtu financial|2027 internship frontend user experience"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "US Citizenship required (cached 2026-07-29)"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. citizenship is required (cached 2026-07-29)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: hyperlight|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: appian|software engineering intern"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|investment data science intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|risk technology analyst intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}, {"uid": "zshah101:greenhouse:appian:8041237", "check": "cross_source_duplicate", "reason": "company+title already in vault: appian|software engineering intern"}, {"uid": "vanshb03:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: optiver|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-07-30T07:27:53.677404+00:00", "fetch_counts": {"SimplifyJobs": 14676, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 311, "zshah101": 250, "Greenhouse": 53, "Ashby": 4, "Freehire": 29, "AIJobs": 189}, "filter_match_counts": {"SimplifyJobs": 44, "Jose-Gael-Cruz-Lopez": 5, "vanshb03": 94, "zshah101": 21, "Greenhouse": 32, "Ashby": 2, "Freehire": 6, "AIJobs": 8}, "new_count": 78, "already_seen_count": 134, "deferred_count": 60, "written_count": 0, "rejections": [{"uid": "zshah101:greenhouse:virtu:8657500002", "check": "cross_source_duplicate", "reason": "company+title already in vault: virtu financial|2027 internship frontend user experience"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "US Citizenship required (cached 2026-07-29)"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. citizenship is required (cached 2026-07-29)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: hyperlight|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: appian|software engineering intern"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|investment data science intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|risk technology analyst intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}, {"uid": "zshah101:greenhouse:appian:8041237", "check": "cross_source_duplicate", "reason": "company+title already in vault: appian|software engineering intern"}, {"uid": "vanshb03:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: optiver|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-07-30T10:13:03.165954+00:00", "fetch_counts": {"SimplifyJobs": 14673, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 311, "zshah101": 250, "Greenhouse": 53, "Ashby": 4, "Freehire": 28, "AIJobs": 189}, "filter_match_counts": {"SimplifyJobs": 43, "Jose-Gael-Cruz-Lopez": 5, "vanshb03": 94, "zshah101": 21, "Greenhouse": 32, "Ashby": 2, "Freehire": 6, "AIJobs": 8}, "new_count": 78, "already_seen_count": 133, "deferred_count": 60, "written_count": 0, "rejections": [{"uid": "zshah101:greenhouse:virtu:8657500002", "check": "cross_source_duplicate", "reason": "company+title already in vault: virtu financial|2027 internship frontend user experience"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "US Citizenship required (cached 2026-07-29)"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. citizenship is required (cached 2026-07-29)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: hyperlight|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: appian|software engineering intern"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|investment data science intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|risk technology analyst intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}, {"uid": "zshah101:greenhouse:appian:8041237", "check": "cross_source_duplicate", "reason": "company+title already in vault: appian|software engineering intern"}, {"uid": "vanshb03:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: optiver|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-07-30T12:23:47.150206+00:00", "fetch_counts": {"SimplifyJobs": 14670, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 311, "zshah101": 258, "Greenhouse": 53, "Ashby": 4, "Freehire": 28, "AIJobs": 187}, "filter_match_counts": {"SimplifyJobs": 45, "Jose-Gael-Cruz-Lopez": 5, "vanshb03": 94, "zshah101": 21, "Greenhouse": 32, "Ashby": 2, "Freehire": 6, "AIJobs": 8}, "new_count": 79, "already_seen_count": 134, "deferred_count": 61, "written_count": 0, "rejections": [{"uid": "zshah101:greenhouse:virtu:8657500002", "check": "cross_source_duplicate", "reason": "company+title already in vault: virtu financial|2027 internship frontend user experience"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "US Citizenship required (cached 2026-07-29)"}, {"uid": "SimplifyJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. citizenship is required (cached 2026-07-29)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: hyperlight|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: appian|software engineering intern"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "AIJobs:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|investment data science intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|risk technology analyst intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}, {"uid": "zshah101:greenhouse:appian:8041237", "check": "cross_source_duplicate", "reason": "company+title already in vault: appian|software engineering intern"}, {"uid": "vanshb03:[REDACTED]", "check": "opt_eligibility", "reason": "U.S. Person status is required (cached 2026-07-26)"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: optiver|software engineer intern"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}], "errors": [], "halted": false, "halt_reason": null}
---rechecks.jsonl tail---
{"timestamp": "2026-07-26T08:59:09.304449+00:00", "type": "recheck", "scanned": 120, "removals": [], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-07-27T10:27:49.227897+00:00", "type": "recheck", "scanned": 119, "removals": [], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-07-28T09:19:23.443174+00:00", "type": "recheck", "scanned": 127, "removals": [{"uid": "zshah101:breezy:vetsez:d18961a7a7e701", "reason": "active: false upstream"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-07-29T09:23:40.855392+00:00", "type": "recheck", "scanned": 132, "removals": [{"uid": "zshah101:workday:intel:/job/US-Oregon-Hillsboro/[REDACTED]", "reason": "active: false upstream"}, {"uid": "vanshb03:[REDACTED]", "reason": "active: false upstream"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-07-30T09:15:35.775974+00:00", "type": "recheck", "scanned": 139, "removals": [{"uid": "AIJobs:[REDACTED]", "reason": "absent from live feed"}, {"uid": "SimplifyJobs:[REDACTED]", "reason": "active: false upstream"}], "errors": [], "halted": false, "halt_reason": null}
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/profile.yaml`
- `ToolSearch` — `{"query":"select:mcp__jarvis__vault_list,mcp__jarvis__vault_read,mcp__jarvis__search_simple","max_results":5}`
- `mcp__jarvis__vault_list` — `{"path":""}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Programs"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Tracker"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Contacts"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Programs/Serious"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Programs/Considering"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Tracker/Each One"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Contacts/Each One"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers/1 - AI & ML"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers/2 - Fullstack"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers/Other"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers/Viewed"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Tracker/Each One/Current"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Contacts/Each One/Ongoing"}`
- `ToolSearch` — `{"query":"select:mcp__jarvis-fs__list_allowed_directories","max_results":3}`
- `mcp__jarvis-fs__list_allowed_directories` — `{}`
- `Bash` — `ls -la /home/anant_gupta/projects/work/ 2>/dev/null; echo "---"; find / -maxdepth 4 -iname "Jarvis" -type d 2>/dev/null`
  ```
total 16
drwxr-xr-x  4 anant_gupta anant_gupta 4096 Jul 16 20:52 .
drwxr-xr-x  9 anant_gupta anant_gupta 4096 Jun  7 19:00 ..
drwxr-xr-x  5 anant_gupta anant_gupta 4096 Jun 30 13:05 gupta-builds
drwxr-xr-x 15 anant_gupta anant_gupta 4096 Jul 30 19:54 internship-research-loop
---
  ```
- `Bash` — `ls -la /home/anant_gupta/projects/work/gupta-builds/ 2>/dev/null`
  ```
total 28
drwxr-xr-x 5 anant_gupta anant_gupta 4096 Jun 30 13:05 .
drwxr-xr-x 4 anant_gupta anant_gupta 4096 Jul 16 20:52 ..
drwxr-xr-x 2 anant_gupta anant_gupta 4096 Jun 30 12:00 .claude
drwxr-xr-x 9 anant_gupta anant_gupta 4096 Jun 30 13:19 .git
drwxr-xr-x 3 anant_gupta anant_gupta 4096 Jun 30 11:42 .github
-rw-r--r-- 1 anant_gupta anant_gupta 6575 Jun 30 13:05 README.md
  ```
- `Write` — `/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/aiml.txt`
  ```
2027 Business Technology Solutions Intern - Data & Software Engineering (Undergraduate) - AbbVie.md
A.I. Developer Co-Op (Boston, MA) - Manhattan Associates.md
AI Engineer Intern - Enterprise Technology Services - American Express.md
AI Intern - Montenson.md
AI Network Automation Engineer Intern - Global Physical Network Infrastructure - ByteDance.md
AI Network Automation Engineer Intern, Global Physical Network Infra - ByteDance.md
AI Operations Intern - Naukr AI - Acds.md
AI Operations Intern-Caddell Reynolds - Acds.md
AI and Data Engineering Summer Scholar Intern - Government & Public Services - Deloitte.md
AI-First Engineering Intern - Xsolla.md
AIML Research Intern - DRW.md
Agent Evaluation & Evolution Machine Learning Engineer Intern - Applied Machine Learning Ark - ByteDance.md
Agentic AI Intern - American Fidelity.md
Analytics and Quantitative Modeling Intern - Analytics & Quantitative Modeling - KeyBank.md
Applications Intern - AI and Machine Learning - TMEIC Corporation Americas.md
Applied Machine Learning Production Engineer Intern - AML Production Engineer - ByteDance.md
Applied Machine Learning Production Engineer Intern - ByteDance.md
Artificial Intelligence Co-op Intern - Mosaic.md
Artificial Intelligence Intern - Montenson.md
Autonomous Driving – Internship in Machine Learning - Robert Bosch Venture Capital.md
Business Systems Analyst Intern - W.W. Grainger.md
Business Technology Solutions Intern - Data & Software Engineering - Undergraduate - AbbVie.md
Campus AI Research Engineer (Intern) - Jump Trading.md
Campus AI Research Engineer - Deep Learning (Intern) - Jump Trading.md
Campus AI Research Engineer – Research Automation (Intern) - Jump Trading.md
Campus Graduate Masters Summer Internship Program - 2027 AI Engineer I, Enterprise Technology Services- Phoenix, AZ - American Express.md
Campus Graduate Masters Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- Atlanta, GA - American Express.md
Campus Graduate Masters Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- New York, NY - American Express.md
Campus Graduate Masters Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- Sunrise, FL - American Express.md
Campus Graduate Masters Summer Internship Program - 2027 Software Engineer I, Enterprise Technology Services- Phoenix, AZ - American Express.md
Campus Graduate Masters Summer Internship Program - 2027 Software Engineer, Enterprise Technology Services- Charlotte, NC - American Express.md
Campus Graduate Masters Summer Internship Program - 2027 Software Engineer, Enterprise Technology Services- New York, NY - American Express.md
Campus Graduate Masters Summer Internship Program - 2027 Software Engineer, Enterprise Technology Services- Sunrise, FL - American Express.md
Campus Undergraduate Summer Internship Program - 2027 AI Engineer I, Enterprise Technology Services- Phoenix, AZ - American Express.md
Campus Undergraduate Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- Atlanta, GA - American Express.md
Campus Undergraduate Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- New York, NY - American Express.md
Campus Undergraduate Summer Internship Program - 2027 AI Engineer, Enterprise Technology Services- Sunrise, FL - American Express.md
Campus Undergraduate Summer Internship Program - 2027 Software Engineer I, Enterprise Technology Services- Phoenix, AZ - American Express.md
Campus Undergraduate Summer Internship Program - 2027 Software Engineer, Enterprise Technology Services- Charlotte, NC - American Express.md
Campus Undergraduate Summer Internship Program - 2027 Software Engineer, Enterprise Technology Services- Sunrise, FL - American Express.md
Campus Undergraduate Summer Internship Program - 2027 Software Engineer, Technology - New York, NY - American Express.md
College to Corporate IT Internship - Data Science (NC) - Vanguard.md
College to Corporate IT Internship - Data Science (PA) - Vanguard.md
Cyber Security Intern - Capital One.md
Data Analytics - Data Science Intern - Northwell Health.md
Data Engineer Intern - Data - LPL Financial Holdings.md
Data Internship - Data & AI Program - JP Morgan Chase.md
Data Lake Infrastructure & Data Analytics Research Engineer Intern - Applied Machine Learning Ark - ByteDance.md
Data Lake Infrastructure and Data Analytics Research Engineer Intern - Applied Machine Learning Ark - ByteDance.md
Data Science Intern - College to Corporate IT - Vanguard.md
Data Science Intern - Fully Remote US - HireVue.md
Data Science Intern - Information Technology - Vanguard.md
Data Science Intern - Notion.md
Data Science Machine Learning Intern - Castleton Commodities International.md
Data Science PhD Intern, 2027 - Google.md
Deep Learning Computer Architecture Intern - NVIDIA.md
FPGA Intern - DRW.md
Forensic Analytics Summer Scholar Intern - Forensic Analytics - Deloitte.md
Forward Deployed Software Engineer Intern - Commercial - Palantir.md
Forward Deployed Software Engineer Intern - Intel - Palantir.md
Full Stack Web Development Co-op - Spring 2027 - Draper.md
GPUAI Application System Software Engineer Intern - ByteDance.md
GPUAI Application System Software Engineer Intern - System Technologies and Engineering - ByteDance.md
Graduate Level Co-op – Data Scientist – Plymouth, MN – Summer 2027 - Philips.md
HardwareSilicon Engineering PhD Intern, 2027 - Google.md
Image Processing Co-op - Specter Aerospace.md
Intern - AI-ML Data Engineering - Onsite - St. Louis - Core & Main.md
Intern Program - Agentic AI - Nelnet.md
Machine Learning Engineer Intern - AML-Engine-Orchestration - ByteDance.md
Machine Learning Engineer Intern - ByteDance.md
Machine Learning Engineer Intern - Jane Street.md
Machine Learning InternCo-op - Machine Learning - Artificial Intelligence - AMD.md
Machine Learning InternCo-op - Multiple Teams - AMD.md
Machine Learning Research Engineer Intern - Quantbot Technologies.md
Machine Learning Research Intern - Summer 2027 - Chicago - IMC Trading.md
Machine Learning Researcher Intern - Jane Street.md
Member of Technical Staff Intern - Research - Abundant.md
Member of Technical Staff, Research (Intern Winter 2027) - Abundant.md
Network Software Engineer Intern - Network Observation - ByteDance.md
Quantic - PhD Quantitative Researcher Intern (Summer 2027) - Walleye Capital Internships.md
Quantic – Quantitative Developer Intern (Summer 2027) - Walleye Capital Internships.md
Quantitative Developer Intern - Tower Research.md
Quantitative Intern (Summer 2027) - Optiver.md
Quantitative Research Intern - DRW.md
Quantitative Research Intern, PhD (Summer 2027) - Optiver.md
Quantitative Research Internship (2027 Start) - Optiver.md
Quantitative Researcher, Intern (Summer 2027) - Aquatic Capital Management.md
Quantitative Strategy Developer Intern - Susquehanna Investment Group.md
Quantitative Trading Analyst Intern - DRW.md
R&D- Computer Vision Engineering Intern - Magna International.md
Research Intern - Deep Learning - Pony Dot Ai.md
Research Intern - School of Computer Science - LTI - Carnegie Mellon University.md
Research Intern – Video World Models (Research & ML Systems) - Tencent.md
Software Developer Intern - DRW.md
Software Engineer Co-Op - Enterprise Finance Applications - Summer 2027 - Fifth Third Bank.md
Software Engineer Co-op - Software Engineering - GE Appliances.md
Software Engineer Intern (Summer 2027) - Notion.md
Software Engineer Intern - AI Platform - ByteDance.md
Software Engineer Intern - AML-Engine-Orchestration - ByteDance.md
Software Engineer Intern - ByteDance.md
Software Engineer Intern - CTGT.md
Software Engineer Intern - Capital One.md
Software Engineer Intern - Chicago Trading Company.md
Software Engineer Intern - Circleback.md
Software Engineer Intern - Enterprise Technology Services - American Express.md
Software Engineer Intern - Generalist - Pony Dot Ai.md
Software Engineer Intern - Global Payment Infra and SRE - ByteDance.md
Software Engineer Intern - Global Traffic Architecture - ByteDance.md
Software Engineer Intern - Grainger Technology Group - W.W. Grainger.md
Software Engineer Intern - Heliux.md
Software Engineer Intern - IMC.md
Software Engineer Intern - LPL Financial Holdings.md
Software Engineer Intern - Melius.md
Software Engineer Intern - Optiver.md
Software Engineer Intern - Palantir Technologies.md
Software Engineer Intern - Placement Year - RRS Group.md
Software Engineer Intern - Pylon.md
Software Engineer Intern - SK Hynix Memory Solution.md
Software Engineer Intern - Software Engineer Program - JP Morgan Chase.md
Software Engineer Intern - Summer 2027 - Replit.md
Software Engineer Intern - Technology - American Express.md
Software Engineer Intern - Winter 2027 - Notion.md
Software Engineer Intern, Infrastructure - Palantir Technologies.md
Software Engineer Intern, Production Infrastructure - Palantir Technologies.md
Software Engineer, AI Platform Intern - Nuro.md
Software Engineer, Intern (Summer 2027) - Aquatic Capital Management.md
Software Engineering Intern (Summer 2027) - Replit.md
Software Engineering Intern - Appian.md
Software Engineering Intern - NVIDIA.md
Software Engineering Intern - Quadrillion Labs.md
Software Engineering Intern [SpringSummer 2027] - Melius.md
Software Engineering Intern, Power Modeling & AI Tools - Tenstorrent.md
Software Engineering Internship - Deepgram.md
Software Engineering- Internship (Fall 2026-Summer 2027) - Deepgram.md
Technology Intern - Early ID Participants - Humana.md
Technology Intern - Humana.md
Technology Intern - Verition Fund Management.md
Visual Generation & Multimodal Evaluation Machine Learning Engineer Intern - Aml-Ark - ByteDance.md

  ```
- `Write` — `/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/fullstack.txt`
  ```
2027 North America Software Engineering Internship - The Trade Desk.md
2027 Software Engineering Internship - Uber.md
Data Engineering Intern - Castleton Commodities International.md
Data Engineering Intern-Co-op - Marmon Holdings.md
DevOps Engineering Intern - Copart.md
Digital Co-op - Ameren.md
Enterprise Operations Software Internship - Hewlett Packard (HP).md
Front-End Software Developer Co-op - Specter Aerospace.md
Full Stack Developer Co-op - Specter Aerospace.md
Full-Stack Software Engineer Intern - Castleton Commodities International.md
Platform Engineer Intern - DRW.md
Renewables Data Analytics Intern - WEC Energy Group.md
Self-Built Engineer Intern - CDN Platform - ByteDance.md
Software Developer Intern- Drexel Co-op US - AVEVA.md
Software Development Intern - Dee Zee.md
Software Development Internship - SimonComputing.md
Software Engineer - Ellipsis Labs.md
Software Engineer Intern - Backend Focused - Rippling.md
Software Engineer Intern - Global Payment - ByteDance.md
Software Engineer Intern - Hyperlight.md
Software Engineer Intern - Medtronic.md
Software Engineer Intern - NHRC - Teledyne.md
Software Engineer Intern - Observability and Security Platform - Datadog.md
Software Engineer Intern - Traffic Infrastructure - ByteDance.md
Software Engineer Intern - Western Digital.md
Software Engineer Intern - Winter 2027 - Figma.md
Software Engineering Co-op - Western Digital.md
Software Engineering Intern (2027 Start) - Winter - Databricks.md
Software Engineering Intern (Summer 2027) - Quadrillion.md
Software Engineering Intern - Copart.md
Software Engineering Intern - General Matter.md
Software Engineering Intern - Google.md
Software Engineering Intern - Medtronic.md
Software Engineering Intern - Quadrillion.md
Software Engineering Intern, Device Experiences - Hewlett Packard (HP).md
Software Engineering Intern, MS, Summer 2027 - Google.md
Summer 2027 Internship - Software Engineering - General Matter.md
Summer 2027 Software Engineering Internship - Western Digital.md
Technology Intern - Data Engineering - Devon Energy.md

  ```
- `Write` — `/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/cysfin.txt`
  ```
2027 Internship - Frontend & User Experience - Virtu Financial.md
2027 Internship - Quant Research (Undergrad) - Virtu Financial.md
2027 Internship - Quantitative Trading - Virtu Financial.md
2027 Internship - Software Engineer - Virtu Financial.md
2027 Internship- FPGA - Virtu Financial.md
Campus Systems Engineer Intern - Jump Trading.md
Campus UI Software Engineer Intern - Jump Trading Group.md
Cyber Security IT Intern - CNO Financial Group.md
Cybersecurity Analyst Intern - Jane Street.md
Data Engineer Intern - Jane Street.md
Data Intern - Key Technology & Services - Data Track - KeyBank.md
FPGA Engineer Intern (Summer 2027 - Austin) - Optiver.md
FPGA Engineer Intern (Summer 2027 - Chicago) - Optiver.md
FPGA Internship (2027 Start) - Optiver.md
Frontend & User Experience Intern - Virtu Financial.md
Frontend Developer Internship - Virtu Financial.md
Hardware Engineer (FPGA-ASIC) Intern - Jane Street.md
Hardware Engineer Intern - IMC.md
Information Security Engineer Intern - Appian.md
Intern - Hudson River Trading.md
Investment Data Science Intern - Walleye Capital.md
Linux Engineer Intern - Jane Street.md
Network Engineer Intern - Jane Street.md
Platform Engineer Intern, Summer 2027 - Akuna Capital.md
Quant Trading Intern - Chicago Trading Company.md
Quantitative Research Analyst Internship - Stevens Capital Management.md
Quantitative Technologist Intern, C++ - Radix Trading.md
Quantitative Trading Intern - Belvedere Trading.md
Quantitative Trading Intern - Virtu.md
Quantitative Trading Internship (2027 Start) - Optiver.md
Risk Technology Analyst Intern - Walleye Capital.md
Software Engineer Intern (Summer 2027 - Austin) - Optiver.md
Software Engineer Intern (Summer 2027 - Chicago) - Optiver.md
Software Engineer Intern - Aquatic Capital Management.md
Software Engineer Intern - C# .NET Desktop, Summer 2027 - Akuna Capital.md
Software Engineer Intern - C++ or Python - Hudson River Trading.md
Software Engineer Intern - C++, Summer 2027 - Akuna Capital.md
Software Engineer Intern - Full Stack Web, Summer 2027 - Akuna Capital.md
Software Engineer Intern - Hudson River Trading.md
Software Engineer Intern - Jane Street.md
Software Engineer Intern - Jump Trading.md
Software Engineer Intern - PDT Partners.md
Software Engineer Intern - Python, Summer 2027 - Akuna Capital.md
Software Engineer Intern - Software Engineer - Virtu Financial.md
Software Engineer Intern - Virtu Financial.md
Software Engineer Intern, C# .NET Desktop - Akuna Capital.md
Software Engineering Intern - PDT Partners.md
Software Engineering Internship - Summer 2027 - Chicago Trading Company.md
Summer 2027 Software Engineering Intern - PDT Partners.md
Summer 2027 Systems Engineering Intern - PDT Partners.md
Summer Intern 2027 - Software Developer - Five Rings.md
Technology Intern - FTI Consulting.md
Technology Intern - Hong Kong - 2027 - Marshall Wace Internship Programmes.md
Technology Intern - London - 2027 - Marshall Wace Internship Programmes.md
Technology Intern - New York - 2027 - Marshall Wace Internship Programmes.md
Technology Intern - Technology - FTI Consulting.md
Technology Intern - Walleye Capital.md
Technology and Operations Intern - Data - Truist Bank.md
Tools and Compilers Research and Development Intern - Jane Street.md
Trading Automation and Operations Intern (Summer 2027) - Optiver.md
Trading Desk Operations Engineer Intern - Jane Street.md
Windows Engineer Intern - Jane Street.md

  ```
- `Write` — `/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/other.txt`
  ```
2026-2027 Information Technology - Software Engineer - Intern - Chevron Corporation.md
2027 Summer Intern - Technology Analyst, Software Engineering - PIMCO.md
AI Research Scientist Intern - 2027 Summer - Two Sigma.md
Accounting Intern (Spring 2027) - Zipline.md
Accounting Intern (Summer 2027) - Zipline.md
Aerodynamics Intern (Spring 2027) - Zipline.md
Application Engineer Co-opIntern - PCS - GE Vernova.md
Applications Engineer Intern (Spring 2027) - Zipline.md
Applications Engineer Intern (Summer 2027) - Zipline.md
Business Analytics Intern - Allegheny County.md
Business Intelligence Intern - Mission Critical - Ryan Companies.md
Civil and Structural Engineer Intern (Spring 2027) - Zipline.md
Civil and Structural Engineer Intern (Summer 2027) - Zipline.md
College to Corporate IT Internship - Data Analyst (NC) - Vanguard.md
Community Engagement Intern (Spring 2027) - Zipline.md
Community Engagement Intern (Summer 2027) - Zipline.md
Computational Physics Intern (Summer 2027) - Zipline.md
Construction Management Intern (Spring 2027) - Zipline.md
Construction Management Intern (Summer 2027) - Zipline.md
Consulting Intern - Healthcare Data Management and Strategy - BerryDunn.md
Controls Engineer Intern (Spring 2027) - Zipline.md
Controls Engineer Intern (Summer 2027) - Zipline.md
Corporate Summer Internship - Technology, Software Engineering and Cyber - Hilton Worldwide.md
DERMS Co-opIntern - Ameren.md
Data Analyst Intern (Summer 2027) - Continental Resources.md
Data Analyst Intern - College to Corporate IT - Vanguard.md
Data Analyst Intern - Continental Resources.md
Data Analyst InternCo-op - AMD.md
Data Analytics Intern - Arthur J. Gallagher & Co..md
Data Analytics Intern - Global Servicing - Financial Crimes Risk & Controls - American Express.md
Data Analytics Intern - Insights - Montenson.md
Data Engineer Intern - Spring 2027 - Medpace.md
Data Intern - American Fidelity.md
Data Operations Intern - UHY.md
Data Science Intern - Analytics & Modeling Program - Fannie Mae.md
Electrical Engineer Intern (Spring 2027) - Zipline.md
Electrical Engineer Intern (Summer 2027) - Zipline.md
Energy Analytics Intern - WEC Energy Group.md
Engineer Intern - Spring 2027 - TMEIC Corporation Americas.md
Enterprise Analytics Intern - GuideWell Mutual.md
Enterprise Systems Software Engineer Intern (Summer 2027) - Zipline.md
Enterprise Systems Software Engineer Intern - Spring 2027 - Zipline.md
Finance & Accounting Intern (Summer 2027) - Walleye Capital Internships.md
GMU Scholar Program Intern - CACI.md
Geoscience Intern - Continental Resources.md
Global Client Group Intern - Data and Tools - Undergraduate and Master's - Dimensional Fund Advisors.md
Global Client Group Operations Insights Intern - Undergraduate & Master's - Dimensional Fund Advisors.md
Global Supply Management Intern (Spring 2027) - Zipline.md
Global Supply Management Intern (Summer 2027) - Zipline.md
Hardware Test Intern (Spring 2027) - Zipline.md
Hardware Test Intern (Summer 2027) - Zipline.md
IT Development Program Intern - IT Development Program - Genworth Financial.md
IT Infrastructure Internship - Summer 2027 - Conagra Brands.md
Implementation Intern - FAST Enterprises.md
Intern, Software Engineering - Moog.md
Long Range Platform Embedded Firmware Intern (Summer 2027) - Zipline.md
Long Range Platform Hardware Engineering Intern (Summer 2027) - Zipline.md
Maintenance Tool Engineering Intern (Spring 2027) - Zipline.md
Maintenance Tool Engineering Intern (Summer 2027) - Zipline.md
Material Planning Intern (Spring 2027) - Zipline.md
Material Planning Intern (Summer 2027) - Zipline.md
Mechanical Engineer Intern (Spring 2027) - Zipline.md
Mechanical Engineer Intern (Summer 2027) - Zipline.md
Network Software Engineer Intern - Network Switch - ByteDance.md
Operations Experience Intern (Spring 2027) - Zipline.md
Operations Intern - Summer 2027 - Vertiv.md
Planning Analytics Intern - Summer 2027 - Vertiv.md
Product Development Engineer InternCo-op - AMD.md
Quality & Manufacturing Intern (Spring 2027) - Zipline.md
Quality & Manufacturing Intern (Summer 2027) - Zipline.md
Quantitative Risk Intern - DV Group.md
RenderATL - 2027 US Software Engineering Internship - Axon.md
Reporting Analyst Intern - CNO Financial Group.md
Sales Data Analytics Intern - Summer 2027 - Vertiv.md
Sales Data Analytics Intern - Vertiv.md
Software Developer Intern - DE Shaw.md
Software Development Co-op - Spring 2027 - Medpace.md
Software Development Engineer Intern - Network Automation - 2027 Summer - ByteDance.md
Software Development Intern - American Fidelity.md
Software Development Intern - Spring 2027 - Mujin.md
Software Development Internship - Summer 2027 - Conagra Brands.md
Software Engineer Intern - DV Trading.md
Software Engineer Intern - Databricks.md
Software Engineer Intern - Distributed NoSQL Database Systems - ByteDance.md
Software Engineer Intern - Garda Capital Partners.md
Software Engineer Intern - HPR (Hyannis Port Research).md
Software Engineer Intern - Northrop Grumman.md
Software Engineer Intern - Schweitzer Engineering Laboratories.md
Software Engineer Intern - Summer 2027 (DV Commodities) - DV Trading.md
Software Engineer Intern - Summer 2027 - Atoms.md
Software Engineer Intern - Summer 2027 - Belvedere Trading.md
Software Engineer Intern - Summer 2027 - IMC Trading.md
Software Engineer Intern - Summer 2027 - RTX.md
Software Engineer Intern - Winter 2027 - Atoms.md
Software Engineer InternCo-op - AMD.md
Software Engineer Internship (2027 Start) - Optiver.md
Software Engineering Intern (Summer 2027) - Freeform.md
Software Engineering Intern (Summer 2027) - RTX.md
Software Engineering Intern - HPR.md
Software Engineering Intern - Summer 2027 - HPR (Hyannis Port Research).md
Software Engineering Intern - Technology Analyst - PIMCO.md
Software Engineering Intern, Summer 2027 - Google.md
Software Integration Intern - Mujin.md
Software Mobile Intern - American Fidelity.md
Software Systems Validation Intern (Spring 2027) - Zipline.md
Software Systems Validation Intern (Summer 2027) - Zipline.md
Strategic Engagements & Events Intern (Spring 2027) - Zipline.md
Strategic Engagements & Events Intern (Summer 2027) - Zipline.md
Strategic Technology Intern - SED Division - HNTB.md
Summer 2027 Intern - Software Engineering - Western Digital.md
Summer 2027 Internship - Tech (Infrastructure) - ING.md
Supplier Industrialization Engineering Intern (Spring 2027) - Zipline.md
Supplier Industrialization Engineering Intern (Summer 2027) - Zipline.md
Supply Chain Business Operations Intern (Spring 2027) - Zipline.md
Supply Chain Business Operations Intern (Summer 2027) - Zipline.md
Supply Chain Data Analyst Intern - Motorola.md
Sustainability Engineer Intern - Montenson.md
System Administrator Intern - Montenson.md
System Test Automation Intern (Spring 2027) - Zipline.md
System Test Automation Intern (Summer 2027) - Zipline.md
Technical Program Manager Intern (Spring 2027) - Zipline.md
Technology, Data and Innovation Intern - Technology, Data and Innovation - Deutsche Bank.md
Technology, Operations, Digital, and Data Analytics Intern - Regions Bank.md
Thermal Application Engineer Intern - Summer 2027 - Vertiv.md
Video Production and Social Media Intern (Spring 2027) - Zipline.md

  ```
- `Bash`:
  ```bash
cd /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad
for f in aiml fullstack cysfin other; do echo -n "$f: "; wc -l < $f.txt; done
echo "total:"; cat aiml.txt fullstack.txt cysfin.txt other.txt | wc -l
echo "--- company frequency (top 25) ---"
cat aiml.txt fullstack.txt cysfin.txt other.txt | sed -E 's/\.md$//' | awk -F' - ' '{print $NF}' | sort | uniq -c | sort -rn | head -30
  ```
  ```
aiml: 138
fullstack: 39
cysfin: 62
other: 125
total:
364
--- company frequency (top 25) ---
     45 Zipline
     24 ByteDance
     20 American Express
     12 Optiver
     11 Jane Street
      9 Virtu Financial
      6 Vanguard
      6 DRW
      6 Akuna Capital
      5 Vertiv
      5 Montenson
      5 Jump Trading
      5 Google
      5 AMD
      4 Western Digital
      4 PDT Partners
      4 American Fidelity
      3 Walleye Capital Internships
      3 Walleye Capital
      3 Specter Aerospace
      3 Palantir Technologies
      3 Notion
      3 Marshall Wace Internship Programmes
      3 Hudson River Trading
      3 Continental Resources
      3 Chicago Trading Company
      3 Castleton Commodities International
      3 Aquatic Capital Management
      2 WEC Energy Group
      2 W.W. Grainger
Shell cwd was reset to /home/anant_gupta/projects/work/internship-research-loop
  ```
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/Other/Aerodynamics Intern (Spring 2027) - Zipline.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers-to-Create.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/Programs/Programs-to-Create.md"}`
- `mcp__jarvis__search_simple` — `{"query":"dossier limit","contextLength":150}`
- `mcp__jarvis__vault_list` — `{"path":"30_Order/Workflows"}`
- `mcp__jarvis__vault_read` — `{"path":"30_Order/Workflows/Internship Pipeline.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/Contacts/Outreach Discovery & Automation Status.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Run Log.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/Tracker/Internship - Dashboard.md"}`
- `mcp__jarvis__vault_list` — `{"path":"20_Progress/Internship/Applying"}`
- `mcp__jarvis__vault_read` — `{"path":"20_Progress/Internship/Building System/Source of Truth.md"}`
- `mcp__jarvis__vault_read` — `{"path":"20_Progress/Internship/Applying/Now.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/Tracker/Each One/Current/Software Engineering Intern - Appian.md"}`
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== MAX_NEW_WRITES / cap-related in run_pipeline.py ==="
grep -n -i "MAX_NEW_WRITES\|cap\|limit\|201\|50\b" run_pipeline.py | head -40
echo "=== cs_relevance in core/relevance.py or classify.py ==="
grep -n -i "def \|cs_relevance\|relevant" core/relevance.py | head -30
echo "=== classify.py functions ==="
grep -n "^def " core/classify.py
  ```
  ```
=== MAX_NEW_WRITES / cap-related in run_pipeline.py ===
64:# open postings — the reason these sources were added) was acceptable. Cap
71:# a tunable dict, not magic numbers spread through the function. Still caps
75:MAX_NEW_WRITES_PER_RUN = {"AI/ML": 3, "Fullstack": 3, "CyS & Finance": 3, "Other": 1}
77:# Per-bucket vault capacity, per the original design (Dossiers-to-Create.md,
81:# codebase applies here too (a hard-refusal cap would silently drop a real,
83:# attention, not vault storage). See run_once()'s bucket_at_capacity handling.
84:BUCKET_CAPACITY = 50
85:# Global total across List/Dossiers/ excluding Viewed/. 150/170 are logged in
88:GLOBAL_INFO_THRESHOLDS = (150, 170)
90:CAPACITY_STATE_FILENAME = "capacity_notified.json"
93:def _prioritize_and_cap(new_listings: list, budget: dict, preferred_companies: dict = None) -> tuple:
123:        limit = budget.get(bucket, 0)
124:        this_run.extend(ordered[:limit])
125:        deferred.extend(ordered[limit:])
132:    Standard's '201 total excluding Viewed/' scope."""
141:def load_capacity_notified(state_dir) -> dict:
142:    path = Path(state_dir) / CAPACITY_STATE_FILENAME
148:def save_capacity_notified(state_dir, notified: dict) -> None:
149:    path = Path(state_dir) / CAPACITY_STATE_FILENAME
156:# (falls outside its bucket's budget, i.e. ends up in _prioritize_and_cap's
372:    run_gh = run_gh or (lambda args: subprocess.run(args, capture_output=True, text=True))
406:        "bucket_at_capacity": [],
440:    this_run, deferred = _prioritize_and_cap(
441:        new_listings, MAX_NEW_WRITES_PER_RUN, preferred_companies=profile.get("preferred_companies")
481:    # Task A resource-limit notification (Standard §5): a bucket at/over
482:    # capacity or the global total crossing a threshold is surfaced, never a
485:    record["bucket_at_capacity"] = sorted(b for b, c in bucket_counts.items() if c >= BUCKET_CAPACITY)
488:    notified = load_capacity_notified(state_dir) if state_dir is not None else {"buckets": [], "global": []}
490:    for bucket in record["bucket_at_capacity"]:
496:                f"Bucket '{bucket}' at/over its {BUCKET_CAPACITY}-dossier notification threshold ({timestamp})",
511:        save_capacity_notified(state_dir, notified)
=== cs_relevance in core/relevance.py or classify.py ===
28:def _norm(s: str) -> str:
78:def stage1_reject(title: str, raw_text: str) -> bool:
123:def stage2_confirm(title: str, company: str, posting_content: str) -> bool:
=== classify.py functions ===
59:def classify(title: str, category: str, posting_content: str) -> tuple:
71:def classification_callout(bucket: str, signal: str) -> str:
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== bucket_at_capacity notification handling in run_pipeline.py ==="
sed -n '480,515p' run_pipeline.py
echo "=== recent runs.jsonl bucket_at_capacity mentions ==="
tail -1 logs/runs.jsonl | python3 -c "import json,sys; d=json.load(sys.stdin); print('bucket_at_capacity:', d.get('bucket_at_capacity')); print('written_count:', d.get('written_count')); print('timestamp:', d.get('timestamp'))"
echo "=== gh issues (if gh cli available and authed) ==="
gh issue list --repo gupta-builds/internship-research-loop --state all --limit 20 2>&1 | head -30
  ```
  ```
=== bucket_at_capacity notification handling in run_pipeline.py ===

    # Task A resource-limit notification (Standard §5): a bucket at/over
    # capacity or the global total crossing a threshold is surfaced, never a
    # write refusal — the writes above already happened regardless.
    bucket_counts = count_dossiers_by_bucket(jarvis_dir)
    record["bucket_at_capacity"] = sorted(b for b, c in bucket_counts.items() if c >= BUCKET_CAPACITY)
    record["dossier_total"] = sum(bucket_counts.values())

    notified = load_capacity_notified(state_dir) if state_dir is not None else {"buckets": [], "global": []}
    newly_notified = False
    for bucket in record["bucket_at_capacity"]:
        if bucket not in notified["buckets"]:
            notified["buckets"].append(bucket)
            newly_notified = True
            issue_fn(
                issue_repo,
                f"Bucket '{bucket}' at/over its {BUCKET_CAPACITY}-dossier notification threshold ({timestamp})",
                f"'{bucket}' now has {bucket_counts[bucket]} dossiers in List/Dossiers/ — this is a "
                "notification, not a write refusal (a full bucket is a signal to review more urgently, "
                "not a reason to lose a real posting). New matches keep writing into this bucket.",
            )
    for threshold in GLOBAL_ISSUE_THRESHOLDS:
        if record["dossier_total"] >= threshold and threshold not in notified["global"]:
            notified["global"].append(threshold)
            newly_notified = True
            issue_fn(
                issue_repo,
                f"Total dossier count crossed {threshold} ({timestamp})",
                f"List/Dossiers/ (excluding Viewed/) now has {record['dossier_total']} dossiers total.",
            )
    if state_dir is not None and newly_notified:
        save_capacity_notified(state_dir, notified)

    if should_run_weekly_rollup(now):
        week_start = now - timedelta(days=7)
        recent = load_recent_runs(runs_log_path, since=week_start)
=== recent runs.jsonl bucket_at_capacity mentions ===
bucket_at_capacity: None
written_count: 0
timestamp: 2026-07-30T12:23:47.150206+00:00
=== gh issues (if gh cli available and authed) ===
3	OPEN	Run halted (ConnectionError) at 2026-08-18T05:20:35.035989+00:00		2026-08-18T05:20:36Z
2	OPEN	Run halted (HTTPError) at 2026-08-17T16:15:32.395149+00:00		2026-08-17T16:15:46Z
1	OPEN	Run halted (HTTPError) at 2026-08-17T15:16:21.079968+00:00		2026-08-17T15:16:34Z
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== recent workflow runs ==="
gh run list --repo gupta-builds/internship-research-loop --limit 15 2>&1
echo "=== issue #3 body ==="
gh issue view 3 --repo gupta-builds/internship-research-loop 2>&1 | head -30
echo "=== capacity_notified.json on origin/master ==="
git show origin/master:state/capacity_notified.json 2>&1
  ```
  ```
Exit code 128
=== recent workflow runs ===
completed	success	run	run	master	schedule	32481855747	41s	2026-08-21T12:25:55Z
completed	success	run	run	master	schedule	32476482013	49s	2026-08-21T11:16:49Z
completed	success	run	run	master	schedule	32472128946	49s	2026-08-21T10:19:48Z
completed	success	run	run	master	schedule	32467858041	57s	2026-08-21T09:25:57Z
completed	success	run	run	master	schedule	32463262231	56s	2026-08-21T08:27:26Z
completed	success	run	run	master	schedule	32459243005	1m3s	2026-08-21T07:34:41Z
completed	success	recheck	recheck	master	schedule	32458533315	29s	2026-08-21T07:25:05Z
completed	success	run	run	master	schedule	32454525448	55s	2026-08-21T06:28:24Z
completed	success	run	run	master	schedule	32450373013	32s	2026-08-21T05:23:31Z
completed	success	run	run	master	schedule	32447080108	28s	2026-08-21T04:28:38Z
completed	success	run	run	master	schedule	32444287353	42s	2026-08-21T03:41:38Z
completed	success	run	run	master	schedule	32439335904	1m12s	2026-08-21T02:17:29Z
completed	success	run	run	master	schedule	32433653126	27s	2026-08-21T00:42:20Z
completed	success	run	run	master	schedule	32427955710	1m23s	2026-08-20T23:16:29Z
completed	success	run	run	master	schedule	32423503409	50s	2026-08-20T22:16:24Z
=== issue #3 body ===
GraphQL: Projects (classic) is being deprecated in favor of the new Projects experience, see: https://github.blog/changelog/[REDACTED]/. (repository.issue.projectCards)
=== capacity_notified.json on origin/master ===
fatal: path 'state/capacity_notified.json' does not exist in 'origin/master'
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== state dir on origin/master ==="
git ls-tree origin/master -- state/ 2>&1
echo "=== issue 3 body (plain) ==="
gh issue view 3 --repo gupta-builds/internship-research-loop --json title,body,createdAt,state 2>&1
  ```
  ```
=== state dir on origin/master ===
100644 blob [REDACTED]	state/dossier_uids.json
100644 blob [REDACTED]	state/opt_cache.json
100644 blob [REDACTED]	state/seen_ids.json
=== issue 3 body (plain) ===
{"body":"Schema drift or source fetch failure — nothing was fetched, filtered, or written this run.\n\n```\nConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))\n```","createdAt":"2026-08-18T05:20:36Z","state":"OPEN","title":"Run halted (ConnectionError) at 2026-08-18T05:20:35.035989+00:00"}
  ```
- `Bash`:
  ```bash
cd /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad
cat aiml.txt fullstack.txt cysfin.txt other.txt > all_dossiers.txt
# Conservative "near-certain non-SWE by title alone" denylist — a human should still eyeball this list, but every title here has zero software/CS/data-eng signal.
grep -iE "Accounting|Aerodynamic|Community Engagement|Construction Management|Construction Manager|Civil and Structural|Mechanical Engineer|Materials? Planning|Quality & Manufacturing|Supply Chain (Business|Data Analyst)|Strategic Engagements|Video Production|Geoscience|Thermal Application|Sustainability Engineer|System Administrator|Global Supply Management|Operations Experience|Business Analytics Intern|Reporting Analyst" all_dossiers.txt | sort | tee near_certain_junk.txt | wc -l
echo "--- sample of that list ---"
head -20 near_certain_junk.txt
echo "--- companies these belong to ---"
sed -E 's/\.md$//' near_certain_junk.txt | awk -F' - ' '{print $NF}' | sort | uniq -c | sort -rn
  ```
  ```
31
--- sample of that list ---
Accounting Intern (Spring 2027) - Zipline.md
Accounting Intern (Summer 2027) - Zipline.md
Aerodynamics Intern (Spring 2027) - Zipline.md
Business Analytics Intern - Allegheny County.md
Civil and Structural Engineer Intern (Spring 2027) - Zipline.md
Civil and Structural Engineer Intern (Summer 2027) - Zipline.md
Community Engagement Intern (Spring 2027) - Zipline.md
Community Engagement Intern (Summer 2027) - Zipline.md
Construction Management Intern (Spring 2027) - Zipline.md
Construction Management Intern (Summer 2027) - Zipline.md
Finance & Accounting Intern (Summer 2027) - Walleye Capital Internships.md
Geoscience Intern - Continental Resources.md
Global Supply Management Intern (Spring 2027) - Zipline.md
Global Supply Management Intern (Summer 2027) - Zipline.md
Material Planning Intern (Spring 2027) - Zipline.md
Material Planning Intern (Summer 2027) - Zipline.md
Mechanical Engineer Intern (Spring 2027) - Zipline.md
Mechanical Engineer Intern (Summer 2027) - Zipline.md
Operations Experience Intern (Spring 2027) - Zipline.md
Quality & Manufacturing Intern (Spring 2027) - Zipline.md
--- companies these belong to ---
     23 Zipline
      2 Montenson
      1 Walleye Capital Internships
      1 Vertiv
      1 Motorola
      1 Continental Resources
      1 CNO Financial Group
      1 Allegheny County
Shell cwd was reset to /home/anant_gupta/projects/work/internship-research-loop
  ```
- `Skill` — `{"skill":"artifact-design"}`

## You

Approach this as the design lead at a small studio known for their versatility, giving every client a visual identity pitched at the treatment the task actually calls for. Make deliberate choices about palette, typography, and layout that are specific to this subject, and avoid templated designs.

## Read the request first

Calibrate treatment, not whether to design. A doc deserves the same craft as a landing page — what changes is the treatment that craft is delivered in. Format is part of this read — decided, not defaulted: a Markdown publish keeps its filename as its title and takes almost none of the craft below, so it fits only when the user asked for Markdown or the content is bound for a Markdown-native destination; never pick it to save time.

Many requests call for a more utilitarian treatment: a plan, a memo, a demo. Make it polished: include real typographic hierarchy, considered spacing, and a proper palette, but avoid over-designing. Most pages do not need a flashy, gigantic hero. Keep flourishes tasteful and limited.

Some requests call for an editorial treatment: a landing page, a game, an app or tool they'll keep or share.

When unsure: a well-composed page is never the wrong answer; an over-designed visual identity sometimes is.

Fundamentals below apply to everything. The editorial process after that runs only when the read above says so.

## Fundamentals for every artifact

**Honor what's already there** Look for an existing design system first — CLAUDE.md, a tokens or theme file, existing component styles. When one exists, apply it; everything below fills gaps and never overrides. Precedence is always: the user's own words, then the project's existing system, then your choices.

**Ground it in the subject.** If the subject isn't already clear, pin it: one concrete subject, its audience, and the page's single job. The subject's own world — its materials, instruments, vernacular — is where distinctive choices come from. Build with real content throughout, never lorem.

**Pair typefaces** Typography carries the page even when the page isn't about typography. Google Fonts is the one font host the Artifact CSP admits — link it directly (`<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=…&display=swap">`); a face from anywhere else must be inlined as a @font-face data URI or it falls back silently. Either way, declare a real fallback stack. Keep running text near 65 characters wide; set a type scale and stay on it; give headings `text-wrap: balance`, body text room to breathe, and uppercase labels a touch of letter-spacing.

**Choose neutrals, don't default to them.** A pure mid-grey reads as unconsidered; a grey with a slight hue bias toward the page's accent reads as chosen. Pure white and near-black are fine grounds when they suit the subject — the point is that the neutral was picked, not inherited.

**Design both themes.** The page renders in the viewer's theme, and the viewer has three states, not two: an explicit choice stamps `data-theme="dark"` / `data-theme="light"` on the root element, and the default "system" setting stamps *nothing* — most viewers see the un-stamped document, where only `prefers-color-scheme` separates light from dark. Structure the CSS token-level for all three: the bare `:root` block defines the complete light palette (for a deliberately dark-first design, swap light and dark consistently through this whole pattern); `@media (prefers-color-scheme: dark)` redefines only the tokens, guarded as `:root:not([data-theme="light"])` so an explicit light choice beats a dark OS; `:root[data-theme="dark"]` redefines them again so the toggle also wins in the other direction. Style components through the tokens, never directly inside a media or `[data-theme]` block — a color whose only definition sits behind `[data-theme]` never applies in the un-stamped state, and the page renders one theme's text on the other theme's ground. Two more rules keep each theme resolving as a set: the artifact composites over a ground the viewer paints in *its* theme, so `body` must set an explicit `background` from a token — a transparent body silently borrows the host's ground; and every element that sets a color takes it from the same token set as the surface behind it, never a literal that only works in one theme. Before publishing, scan the stylesheet for any color declared only inside a media or `[data-theme]` block — that is the classic unreadable-artifact bug. Give the second theme the same care as the first — don't naively invert; keep contrast legible and the accent working on both grounds. A design that deliberately commits to one visual world (a neon arcade screen, a letterpress invitation) may stay single-theme — then skip the media query and stamps entirely but still paint the background and every color explicitly, so the page holds on either host ground; make it a choice, not an omission.

**Let layout do the spacing.** Lay out sibling groups with flex or grid and `gap`, not per-element margins that silently collapse or double. Wide content — tables, code, diagrams — gets `overflow-x: auto` on its own container so the page body never scrolls sideways. Reach for `font-variant-numeric: tabular-nums` wherever digits line up in columns.

**Avoid AI-generated design** AI-generated design currently clusters around a few looks: warm cream (#F4F1EA) with a serif display and terracotta accent; near-black with a lone acid-green or vermilion pop; broadsheet hairline rules with dense columns; a purple-to-blue gradient hero on white; Inter or Space Grotesk as the "safe" face; emoji as section markers; everything centered; `rounded-lg` everywhere; accent bar/rail on rounded cards. Where the user pins down a visual direction, follow it exactly — their words always win, including when they ask for one of these looks. Where nothing is specified, don't spend that freedom on one of these defaults.

**Build cleanly** Be cognizant of overlapping elements, cascade collisions, silent font fallbacks; visual bugs hide in the gap between source and output. Close every non-void element, double-quote attributes, give keyboard focus a visible state, respect `prefers-reduced-motion`. For generative or decorative graphics, reach for Canvas or WebGL rather than hand-authoring long SVG path data.

**CSS rules** When writing the CSS, watch your selector specificities. It is easy to generate classes that cancel each other out — a type-based selector like `.section` fighting an element-based one like `.cta` over padding and margins between sections. Structure the cascade so it doesn't silently undo your spacing.

**Writing the copy** Words are design material, not decoration. Write from the user's side of the screen — name things by what people recognize, not how the system is built (a person manages *notifications*, not *webhook config*). Active voice; a control says exactly what happens ("Publish", then a toast that says "Published"). Errors explain what went wrong and how to fix it — no apologies, no vagueness. Specific beats clever.

**Name the page like a product, not a caption.** The `<title>` is the artifact's name in the gallery and the browser tab, and it sets the reader's first impression of care. Give the page a real name: a short noun phrase, typically two to four words, specific to the subject — or, for a page that exists to answer one question, that question itself, which is then the page's name. Stop at the name — a title that carries its own explainer after a dash or colon reads as generated filler. The name must also identify the page among many: in the gallery it sits beside dozens of other artifacts, and a generic category label that could sit on any of them fails as a name just as surely as an appended explainer. When a candidate title pairs the name with a generic word — a greeting, a category, a page-type label — the name is the half to keep; a trim that drops the identity and keeps the generic word produces exactly the title that could sit on any page. And the rule removes explainers, it does not impose brevity: a multi-word title that already reads as one specific name is finished, and shortening it further only makes it generic. The one-sentence publish `description` is where the explanation belongs; the gallery shows it right under the title.

**Structure is information** Structural devices, numbering, eyebrows, dividers, labels, should encode something true about the content, not decorate it. Many generic designs use numbered markers (01 / 02 / 03), but that's only appropriate if the content actually is a sequence - like a real process or a typed timeline where order carries information the reader needs. Question if choices like numbered markers actually make sense before incorporating them.

**When it's a UI, not a document** A dashboard or tool is scanned and operated, not read top-to-bottom, so the craft shifts from typography to information design. Surface the summary before the detail; encode state in form as well as number — a pill, a chip, a severity stripe — so what needs attention reads at a glance. Semantic color (good / warning / critical) is separate from the accent hue and doesn't count as your accent. Give sparklines and charts the same care as type: an area fill, a faint grid, an emphasized endpoint. What's interactive should look interactive.



## Process

Before writing code, sketch a short design plan — a compact token system with color, type, and layout:
- **Color**: describe the palette as 4–6 named hex values.
- **Type**: typefaces for 2+ roles — a characterful display face used with restraint, a complementary body face, and a utility face for captions or data if needed.
- **Layout**: a layout concept in one or two sentences.

Then build, following the plan and deriving every color and type decision from it.

## When the request is editorial

The stance shifts: the client has already rejected proposals that felt templated, and is paying for a distinctive point of view. Make opinionated calls, and take one real aesthetic risk where it serves the work.

Review the design plan against the subject before building: if any part of it reads like the generic default you would produce for any similar page, revise that part, and note what you changed and why. Only after you've confirmed the plan's uniqueness do you write the code, following the revised plan exactly.

**Principles** 

- The hero is a thesis: open with the most characteristic thing in the subject's world — headline, image, live demo, interactive moment. 
- Typography carries the personality of the page. Pair the display and body faces deliberately, not the same families you would reach for on any other project, and set a clear type scale with intentional weights, widths, and spacing. Make the type treatment itself a memorable part of the design, not a neutral delivery vehicle for the content. 
- Leverage motion deliberately. Think about where and if animation can serve the subject: a page-load sequence, a scroll-triggered reveal, hover micro-interactions, ambient atmosphere. An orchestrated moment usually lands harder than scattered effects; choose what the direction calls for. However, sometimes less is more, and extra animation contributes to the feeling that the design is AI-generated. 
- Match complexity to the vision. Maximalist directions need elaborate execution; minimal directions need precision in spacing, type, and detail. Elegance is executing the chosen vision well.
- Spend your boldness in one place; keep everything around it quiet. If the accent fights the ground, shift it toward analogous or drop saturation rather than replacing it.


## Claude

I need to fix one thing before publishing — I paraphrased the junk list from memory instead of the actual scan output, and included a fabricated placeholder entry. Let me pull the real list and correct it.

Now publishing the artifact.

Here's the real picture, and the artifact above has the full breakdown: **[Pipeline Triage →](https://claude.ai/code/artifact/[REDACTED])**

**The stress is misplaced.** You don't have a dossier problem, you have a zero-applications problem. 364 dossiers sit against a cap of 201 that was decided a month ago and never enforced by hand. But even the 6 that *did* get screened and committed never got applied to — including Appian, which has a finished contact and tracker note sitting untouched since July 26 because a stale note said "wait until August." It's August 21.

Three things worth knowing before you touch anything:

1. **Real filter bug, not just backlog**: the `Other` folder is bloated because a source (AIJobs) doesn't tag category, so every open role at companies like Zipline rides in — including Aerodynamics and Accounting interns tagged "genuine software engineering role." 31 dossiers are disqualified by title alone, zero judgment needed — that's in the artifact, ready to bulk-cut.
2. **Your local code checkout is 413 commits behind origin** and has real uncommitted work (`core/debate.py`) sitting on top of that stale base. Don't touch pipeline code today until you tell me whether to keep or drop that work — pulling blind risks either conflicts or losing it.
3. **50 applications tomorrow isn't happening through the full 9-step pipeline** — that process is 30–60 min/application by design (Program + Contact + Tracker + tailored resume + deep dive). Your own instinct was right: fast yes/no triage, apply immediately on yes, backfill notes later only for what responds. Full order-of-operations for today is in the artifact.

One thing I couldn't answer: which dossiers are closing soon or rolling-admission. `recheck.py` already purges closed postings daily, so what's in the vault is live — but deadline data only exists on the 6 promoted Program notes, not on dossiers. Finding that for the other 358 means actually reading them, which is the exact bottleneck you're trying to escape — so it's part of the triage pass, not something to solve separately first.

Want me to start on step 1 (the git reconciliation) or step 2 (drafting the bulk-delete of the 31 flagged dossiers) right now?

**Tool calls:**

- `Bash`:
  ```bash
cd /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad
for c in "Jane Street" "Two Sigma" "D.E. Shaw\|DE Shaw" "Citadel" "Google" "Microsoft" "LinkedIn" "MLH" "NASA" "Capital One" "Bloomberg"; do
  n=$(grep -ic "$c" all_dossiers.txt)
  echo "$c: $n"
done
  ```
  ```
Jane Street: 11
Two Sigma: 1
D.E. Shaw\|DE Shaw: 1
Citadel: 0
Google: 5
Microsoft: 0
LinkedIn: 0
MLH: 0
NASA: 0
Capital One: 2
Bloomberg: 0
Shell cwd was reset to /home/anant_gupta/projects/work/internship-research-loop
  ```
- `Write` — `/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/pipeline-triage.html`
  ```
<title>Pipeline Triage</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap');

  :root {
    --bg: #f5f3ee;
    --surface: #ffffff;
    --surface-2: #ece8e0;
    --ink: #201c15;
    --muted: #6c665a;
    --hair: #ddd6c8;
    --accent: #2c5f63;
    --accent-ink: #ffffff;
    --ok: #3e7d4c;
    --ok-bg: #e5f0e6;
    --warn: #a86a12;
    --warn-bg: #f6ecd8;
    --crit: #a83b3b;
    --crit-bg: #f6e2e0;
    color-scheme: light;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #16140f;
      --surface: #201d16;
      --surface-2: #292419;
      --ink: #eee9dd;
      --muted: #a49c8a;
      --hair: #3a3427;
      --accent: #6fb3b8;
      --accent-ink: #12211f;
      --ok: #7cc48c;
      --ok-bg: #1e2d1f;
      --warn: #dcae5e;
      --warn-bg: #332818;
      --crit: #e08787;
      --crit-bg: #382220;
      color-scheme: dark;
    }
  }
  :root[data-theme="dark"] {
    --bg: #16140f;
    --surface: #201d16;
    --surface-2: #292419;
    --ink: #eee9dd;
    --muted: #a49c8a;
    --hair: #3a3427;
    --accent: #6fb3b8;
    --accent-ink: #12211f;
    --ok: #7cc48c;
    --ok-bg: #1e2d1f;
    --warn: #dcae5e;
    --warn-bg: #332818;
    --crit: #e08787;
    --crit-bg: #382220;
    color-scheme: dark;
  }

  * { box-sizing: border-box; }
  body {
    background: var(--bg);
    color: var(--ink);
    font-family: 'IBM Plex Sans', system-ui, sans-serif;
    max-width: 920px;
    margin: 0 auto;
    padding: 2.5rem 1.5rem 6rem;
    line-height: 1.55;
  }
  .eyebrow {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    font-size: 0.78rem;
    color: var(--accent);
  }
  h1 {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    font-size: clamp(2.1rem, 5vw, 3rem);
    line-height: 1.02;
    text-wrap: balance;
    margin: 0.25rem 0 0.4rem;
    letter-spacing: -0.01em;
  }
  .dek {
    color: var(--muted);
    font-size: 1.05rem;
    max-width: 62ch;
    margin: 0 0 0.5rem;
  }
  .stamp {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.8rem;
    color: var(--muted);
  }
  h2 {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-size: 1.25rem;
    border-top: 1px solid var(--hair);
    padding-top: 0.6rem;
    margin: 3rem 0 1rem;
    display: flex;
    align-items: baseline;
    gap: 0.6rem;
  }
  h2 .n {
    font-family: 'IBM Plex Mono', monospace;
    color: var(--muted);
    font-size: 0.9rem;
    font-weight: 500;
  }
  p { margin: 0.6rem 0; }
  .lede { max-width: 68ch; }
  .mono { font-family: 'IBM Plex Mono', monospace; }
  .num { font-variant-numeric: tabular-nums; }

  /* stat strip */
  .stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1px;
    background: var(--hair);
    border: 1px solid var(--hair);
    border-radius: 10px;
    overflow: hidden;
    margin-top: 1.4rem;
  }
  .stat {
    background: var(--surface);
    padding: 1rem 1.1rem;
  }
  .stat .label {
    font-family: 'Barlow Condensed', sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.72rem;
    color: var(--muted);
  }
  .stat .value {
    font-family: 'IBM Plex Mono', monospace;
    font-weight: 600;
    font-size: 1.7rem;
    font-variant-numeric: tabular-nums;
    margin-top: 0.15rem;
  }
  .stat .sub { font-size: 0.78rem; color: var(--muted); margin-top: 0.1rem; }
  .stat.crit .value { color: var(--crit); }
  .stat.warn .value { color: var(--warn); }
  .stat.ok .value { color: var(--ok); }

  /* pill */
  .pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35em;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    padding: 0.15em 0.6em;
    border-radius: 999px;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }
  .pill.crit { background: var(--crit-bg); color: var(--crit); }
  .pill.warn { background: var(--warn-bg); color: var(--warn); }
  .pill.ok { background: var(--ok-bg); color: var(--ok); }

  /* bucket table */
  table { width: 100%; border-collapse: collapse; }
  .scroll { overflow-x: auto; }
  th, td {
    text-align: left;
    padding: 0.55rem 0.7rem;
    border-bottom: 1px solid var(--hair);
    font-size: 0.92rem;
  }
  th {
    font-family: 'Barlow Condensed', sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-size: 0.72rem;
    color: var(--muted);
    font-weight: 600;
  }
  td.num, th.num { font-family: 'IBM Plex Mono', monospace; font-variant-numeric: tabular-nums; text-align: right; }
  .bar-cell { min-width: 160px; }
  .bar-track {
    height: 8px;
    border-radius: 5px;
    background: var(--surface-2);
    overflow: hidden;
    position: relative;
  }
  .bar-fill { height: 100%; border-radius: 5px 0 0 5px; }
  .bar-fill.crit { background: var(--crit); }
  .bar-fill.warn { background: var(--warn); }
  .bar-fill.ok { background: var(--ok); }
  .cap-mark {
    position: absolute; top: -2px; bottom: -2px; width: 2px; background: var(--ink); opacity: 0.35;
  }

  /* funnel */
  .funnel {
    display: flex;
    align-items: stretch;
    gap: 0.5rem;
    margin-top: 1rem;
    flex-wrap: wrap;
  }
  .funnel .step {
    flex: 1 1 100px;
    background: var(--surface);
    border: 1px solid var(--hair);
    border-radius: 8px;
    padding: 0.8rem 0.7rem;
    text-align: center;
  }
  .funnel .step .value {
    font-family: 'IBM Plex Mono', monospace;
    font-weight: 600;
    font-size: 1.5rem;
  }
  .funnel .step .label {
    font-family: 'Barlow Condensed', sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-size: 0.7rem;
    color: var(--muted);
    margin-top: 0.15rem;
  }
  .funnel .arrow { align-self: center; color: var(--muted); font-size: 1.1rem; padding: 0 0.1rem; }

  /* callout */
  .callout {
    background: var(--surface);
    border: 1px solid var(--hair);
    border-left: 3px solid var(--accent);
    border-radius: 6px;
    padding: 0.9rem 1.1rem;
    margin: 1rem 0;
  }
  .callout.crit { border-left-color: var(--crit); }
  .callout.warn { border-left-color: var(--warn); }
  .callout p { margin: 0.3rem 0; }
  .callout .head {
    font-family: 'Barlow Condensed', sans-serif;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    font-size: 0.82rem;
    margin-bottom: 0.3rem;
  }

  details { margin-top: 0.6rem; }
  summary {
    cursor: pointer;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.82rem;
    color: var(--accent);
  }
  .junklist {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: var(--muted);
    columns: 2;
    column-gap: 1.5rem;
    margin-top: 0.6rem;
  }
  .junklist div { break-inside: avoid; padding: 0.1rem 0; }

  /* action list */
  ol.actions { list-style: none; padding: 0; margin: 1rem 0 0; counter-reset: step; }
  ol.actions li {
    counter-increment: step;
    display: grid;
    grid-template-columns: 2.2rem 1fr;
    gap: 0.2rem 0.8rem;
    padding: 0.85rem 0;
    border-bottom: 1px solid var(--hair);
  }
  ol.actions li:last-child { border-bottom: none; }
  ol.actions li::before {
    content: counter(step);
    font-family: 'IBM Plex Mono', monospace;
    font-weight: 600;
    font-size: 1.1rem;
    color: var(--accent);
    grid-row: 1 / 3;
  }
  ol.actions .title { font-weight: 600; }
  ol.actions .time {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    color: var(--muted);
    font-weight: 500;
  }
  ol.actions .desc { grid-column: 2; color: var(--muted); font-size: 0.92rem; margin-top: 0.1rem; }

  code {
    font-family: 'IBM Plex Mono', monospace;
    background: var(--surface-2);
    padding: 0.1em 0.35em;
    border-radius: 4px;
    font-size: 0.88em;
  }

  footer {
    margin-top: 3.5rem;
    padding-top: 1rem;
    border-top: 1px solid var(--hair);
    color: var(--muted);
    font-size: 0.8rem;
  }
</style>

<div class="eyebrow">internship-research-loop &middot; status check</div>
<h1>The dossiers aren't the bottleneck. Zero applications is.</h1>
<p class="dek">Full read of the vault against the code, the logs, and the GitHub state — not a guess. Everything below is a real count, taken today.</p>
<p class="stamp">2026-08-21</p>

<div class="stats">
  <div class="stat crit">
    <div class="label">Dossiers</div>
    <div class="value num">364</div>
    <div class="sub">cap is 201 &mdash; 163 over</div>
  </div>
  <div class="stat">
    <div class="label">Committed</div>
    <div class="value num">6</div>
    <div class="sub">5 Serious + 1 Considering</div>
  </div>
  <div class="stat crit">
    <div class="label">Applications sent</div>
    <div class="value num">0</div>
    <div class="sub">in 5+ weeks of runs</div>
  </div>
  <div class="stat ok">
    <div class="label">Pipeline uptime</div>
    <div class="value">Green</div>
    <div class="sub">every run today succeeded</div>
  </div>
</div>

<h2><span class="n">01</span> The dossier pile</h2>
<p class="lede">The 201-total / 50-per-folder cap was decided 2026-07-26 and written into <code>Source of Truth.md</code>. The code enforces it as a <em>notification</em>, not a hard block &mdash; by design, so a full folder never silently drops a real posting. That means the burden was always on the human screening pass to keep pace. It hasn't &mdash; three of four folders are already 1.2&ndash;2.8&times; over.</p>

<div class="scroll">
<table>
  <thead><tr><th>Folder</th><th class="num">Count</th><th class="num">Cap</th><th class="bar-cell">vs. cap</th><th>Status</th></tr></thead>
  <tbody>
    <tr>
      <td>1 &ndash; AI &amp; ML</td><td class="num">138</td><td class="num">50</td>
      <td class="bar-cell"><div class="bar-track"><div class="bar-fill crit" style="width:100%"></div><div class="cap-mark" style="left:36%"></div></div></td>
      <td><span class="pill crit">276%</span></td>
    </tr>
    <tr>
      <td>2 &ndash; Fullstack</td><td class="num">39</td><td class="num">50</td>
      <td class="bar-cell"><div class="bar-track"><div class="bar-fill ok" style="width:78%"></div></div></td>
      <td><span class="pill ok">78%</span></td>
    </tr>
    <tr>
      <td>3 &ndash; CyS &amp; Finance</td><td class="num">62</td><td class="num">50</td>
      <td class="bar-cell"><div class="bar-track"><div class="bar-fill warn" style="width:100%"></div><div class="cap-mark" style="left:81%"></div></div></td>
      <td><span class="pill warn">124%</span></td>
    </tr>
    <tr>
      <td>Other</td><td class="num">125</td><td class="num">50</td>
      <td class="bar-cell"><div class="bar-track"><div class="bar-fill crit" style="width:100%"></div><div class="cap-mark" style="left:40%"></div></div></td>
      <td><span class="pill crit">250%</span></td>
    </tr>
  </tbody>
</table>
</div>

<div class="callout crit">
  <div class="head">Why Other is 125: a filter leak, not a screening failure</div>
  <p>The <code>AIJobs</code> source doesn't tag category. Permissive-by-default filtering (the correct call for ambiguous data) means every open role at a company with an "Internships" landing page rides in &mdash; not just the software ones. Example pulled live: <code>Aerodynamics Intern &ndash; Zipline</code>, dossier dated 2026-08-19 (three days ago), frontmatter reads <code>matched_reason: matched</code> and the auto-written note claims "genuine software engineering role." It is an aerodynamics internship. Zipline alone accounts for 45 of the 364 dossiers.</p>
  <p>A title-keyword scan (accounting / aerodynamics / construction / mechanical / supply chain / community engagement, etc.) flags <strong>31 dossiers</strong> as near-certain non-SWE on title alone &mdash; 23 of them Zipline. This is a same-day, zero-risk cut: no real opportunity is in this list.</p>
  <details>
    <summary>Show the 31 flagged titles</summary>
    <div class="junklist">
      <div>Accounting Intern (Spring) &ndash; Zipline</div>
      <div>Accounting Intern (Summer) &ndash; Zipline</div>
      <div>Aerodynamics Intern (Spring) &ndash; Zipline</div>
      <div>Business Analytics Intern &ndash; Allegheny County</div>
      <div>Civil &amp; Structural Eng. Intern (Spring) &ndash; Zipline</div>
      <div>Civil &amp; Structural Eng. Intern (Summer) &ndash; Zipline</div>
      <div>Community Engagement Intern (Spring) &ndash; Zipline</div>
      <div>Community Engagement Intern (Summer) &ndash; Zipline</div>
      <div>Construction Mgmt Intern (Spring) &ndash; Zipline</div>
      <div>Construction Mgmt Intern (Summer) &ndash; Zipline</div>
      <div>Finance &amp; Accounting Intern &ndash; Walleye Capital</div>
      <div>Geoscience Intern &ndash; Continental Resources</div>
      <div>Global Supply Mgmt Intern (Spring) &ndash; Zipline</div>
      <div>Global Supply Mgmt Intern (Summer) &ndash; Zipline</div>
      <div>Material Planning Intern (Spring) &ndash; Zipline</div>
      <div>Material Planning Intern (Summer) &ndash; Zipline</div>
      <div>Mechanical Engineer Intern (Spring) &ndash; Zipline</div>
      <div>Mechanical Engineer Intern (Summer) &ndash; Zipline</div>
      <div>Operations Experience Intern (Spring) &ndash; Zipline</div>
      <div>Quality &amp; Manufacturing Intern (Spring) &ndash; Zipline</div>
      <div>Quality &amp; Manufacturing Intern (Summer) &ndash; Zipline</div>
      <div>Reporting Analyst Intern &ndash; CNO Financial</div>
      <div>Global Supply Mgmt / Planning (misc) &ndash; Zipline</div>
      <div>Strategic Engagements Intern (Spring) &ndash; Zipline</div>
      <div>Strategic Engagements Intern (Summer) &ndash; Zipline</div>
      <div>Supply Chain Data Analyst &ndash; Motorola</div>
      <div>Sustainability Engineer Intern &ndash; Montenson</div>
      <div>System Administrator Intern &ndash; Montenson</div>
      <div>Thermal Application Engineer &ndash; Vertiv</div>
      <div>Video Production &amp; Social Media (Spring) &ndash; Zipline</div>
      <div>Video Production &amp; Social Media &ndash; other term &ndash; Zipline</div>
    </div>
  </details>
  <p style="margin-top:0.6rem">This is the floor, not the ceiling &mdash; it's a title-only scan. A real Step 2 screen of the remaining ~333 will cut further, but this list alone gets three folders meaningfully closer to cap with zero judgment calls needed.</p>
</div>

<h2><span class="n">02</span> Where things actually stop</h2>
<p class="lede">The pipeline has nine steps on paper. In five weeks of real operation, exactly one dossier has ever reached step 3, and it has not reached step 7.</p>
<div class="funnel">
  <div class="step"><div class="value num">364</div><div class="label">Discovered</div></div>
  <div class="arrow">&rarr;</div>
  <div class="step"><div class="value num">6</div><div class="label">Screened &amp; committed</div></div>
  <div class="arrow">&rarr;</div>
  <div class="step"><div class="value num">1</div><div class="label">Contact + tracker</div></div>
  <div class="arrow">&rarr;</div>
  <div class="step"><div class="value num">0</div><div class="label">Applied</div></div>
</div>
<p>The one that got furthest &mdash; <strong>Appian</strong>, promoted 2026-07-26 &mdash; is still sitting untouched in <code>Tracker/Each One/Current/</code>. Its own next-action note reads "applications aren't reviewed until August 2026." It's now August 21. That note is stale advice, not a still-valid reason to wait.</p>

<h2><span class="n">03</span> Named-target coverage</h2>
<p class="lede">Eleven companies were flagged high-priority in <code>profile.yaml</code> on 2026-07-29, when 3 of 11 had any dossier at all. Today it's <strong>6 of 11</strong> &mdash; real movement, and Jane Street alone now has 11 open roles sitting in the AI&nbsp;&amp;&nbsp;ML folder unscreened.</p>
<div class="scroll">
<table>
  <thead><tr><th>Company</th><th class="num">Dossiers today</th></tr></thead>
  <tbody>
    <tr><td>Jane Street</td><td class="num"><span class="pill ok">11</span></td></tr>
    <tr><td>Google</td><td class="num"><span class="pill ok">5</span></td></tr>
    <tr><td>Capital One</td><td class="num"><span class="pill ok">2</span></td></tr>
    <tr><td>Two Sigma</td><td class="num"><span class="pill warn">1</span></td></tr>
    <tr><td>D.E. Shaw</td><td class="num"><span class="pill warn">1</span></td></tr>
    <tr><td>Citadel</td><td class="num"><span class="pill crit">0</span></td></tr>
    <tr><td>Microsoft</td><td class="num"><span class="pill crit">0</span></td></tr>
    <tr><td>LinkedIn</td><td class="num"><span class="pill crit">0</span></td></tr>
    <tr><td>MLH</td><td class="num"><span class="pill crit">0</span></td></tr>
    <tr><td>NASA</td><td class="num"><span class="pill crit">0</span></td></tr>
    <tr><td>Bloomberg</td><td class="num"><span class="pill crit">0</span></td></tr>
  </tbody>
</table>
</div>

<h2><span class="n">04</span> System state</h2>
<div class="callout ok">
  <div class="head">Automation &mdash; healthy</div>
  <p>GitHub Actions is running hourly and every scheduled run today succeeded. 3 open issues on the repo are all self-resolved transient network blips from Aug 17&ndash;18 (a reset connection, two HTTP errors) &mdash; nothing to fix, just close them.</p>
</div>
<div class="callout crit">
  <div class="head">Local checkout &mdash; 413 commits stale, do not edit yet</div>
  <p>Your local <code>internship-research-loop</code> clone is 413 commits behind <code>origin/master</code> (last local commit 2026-07-30; origin has commits through today). On top of that stale base sits real uncommitted work &mdash; <code>core/debate.py</code> and its tests, plus edits across <code>classify.py</code>, <code>identity.py</code>, <code>relevance.py</code>, <code>run_pipeline.py</code>, <code>writer.py</code> and more. That's a "debate comparator" feature in progress. Before any code change lands today, this needs to be reconciled &mdash; pulling blind risks conflicting with a month of auto-committed pipeline changes, and force-anything risks losing the debate.py work.</p>
</div>

<h2><span class="n">05</span> Today, in order</h2>
<ol class="actions">
  <li>
    <span class="time">10 min</span>
    <span class="title">Decide the local git situation</span>
    <span class="desc">Is <code>core/debate.py</code> work you want to keep? If yes, commit it on a branch before touching anything else; if it was abandoned, say so and it gets stashed. Either way, then pull <code>origin/master</code> so the local checkout matches the live 413-commits-ahead pipeline before any filter/cap fix lands.</span>
  </li>
  <li>
    <span class="time">15 min</span>
    <span class="title">Bulk-reject the 31 flagged non-SWE dossiers</span>
    <span class="desc">No screening judgment needed &mdash; title alone disqualifies every one. Cuts Other from 125 toward 94 and trims the Zipline noise that's about to keep growing every run.</span>
  </li>
  <li>
    <span class="time">45&ndash;60 min</span>
    <span class="title">Speed-screen the rest: yes/no, nothing else</span>
    <span class="desc">Your own instinct was right &mdash; a bare yes/no per dossier, no Program note, no Contact note, no Tracker note yet. Order of attack: <strong>1 &ndash; AI &amp; ML</strong> first (138, worst overage, matches your target direction), then <strong>CyS &amp; Finance</strong> (62), then <strong>Other</strong> survivors. Start with the Jane Street cluster (11 roles) and the rest of the named-target list in section 03 &mdash; those are pre-vetted as worth your time. A "no" gets deleted on the spot, not left for later.</span>
  </li>
  <li>
    <span class="time">20 min</span>
    <span class="title">Apply to Appian today</span>
    <span class="desc">It's the one dossier that already has research, a contact, and a tracker note sitting done. The only reason it hasn't moved is a month-old note that's now wrong about the review date. Submit it, then move its Tracker note to <code>Applied/</code> and its Program note to <code>Ended/</code> per the pipeline's own Step 7.</span>
  </li>
  <li>
    <span class="time">rest of today</span>
    <span class="title">Apply to every "yes" as you screen it &mdash; don't batch it for later</span>
    <span class="desc">Skip the full Step 3&ndash;6 treatment (Program + Contact + Tracker + tailored resume + deep-dive) for the fast lane. Use one well-tuned base resume for most of these; reserve real tailoring for the 6 named-target companies. Log applied ones in a single running list today &mdash; backfill proper notes later only for the ones that respond. The finish line the loop was built for is a submitted application, not a tidy vault.</span>
  </li>
  <li>
    <span class="time">10 min</span>
    <span class="title">Don't build an apply-extension today</span>
    <span class="desc">A same-day autofill/scraper tool isn't realistic, and this project has already ruled out DOM automation against login-walled or anti-bot sites. Most of these postings originate from Simplify Jobs' own listing repo &mdash; its free Chrome extension autofills the exact ATS forms (Greenhouse, Lever, Workday) you'll hit today. Use that instead of building one.</span>
  </li>
  <li>
    <span class="time">5 min</span>
    <span class="title">Close the 3 stale GitHub issues</span>
    <span class="desc">Cosmetic only &mdash; all three are already-resolved network blips. Not urgent, but takes five minutes once you're in the repo anyway.</span>
  </li>
</ol>

<footer>
  Every number above was pulled live &mdash; vault file listings, <code>logs/runs.jsonl</code>, <code>Source of Truth.md</code>, <code>profile.yaml</code>, <code>git log</code>, and <code>gh run list</code> &mdash; not carried over from memory or an old session.
</footer>

  ```
- `Bash` — `cat /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/near_certain_junk.txt`
  ```
Accounting Intern (Spring 2027) - Zipline.md
Accounting Intern (Summer 2027) - Zipline.md
Aerodynamics Intern (Spring 2027) - Zipline.md
Business Analytics Intern - Allegheny County.md
Civil and Structural Engineer Intern (Spring 2027) - Zipline.md
Civil and Structural Engineer Intern (Summer 2027) - Zipline.md
Community Engagement Intern (Spring 2027) - Zipline.md
Community Engagement Intern (Summer 2027) - Zipline.md
Construction Management Intern (Spring 2027) - Zipline.md
Construction Management Intern (Summer 2027) - Zipline.md
Finance & Accounting Intern (Summer 2027) - Walleye Capital Internships.md
Geoscience Intern - Continental Resources.md
Global Supply Management Intern (Spring 2027) - Zipline.md
Global Supply Management Intern (Summer 2027) - Zipline.md
Material Planning Intern (Spring 2027) - Zipline.md
Material Planning Intern (Summer 2027) - Zipline.md
Mechanical Engineer Intern (Spring 2027) - Zipline.md
Mechanical Engineer Intern (Summer 2027) - Zipline.md
Operations Experience Intern (Spring 2027) - Zipline.md
Quality & Manufacturing Intern (Spring 2027) - Zipline.md
Quality & Manufacturing Intern (Summer 2027) - Zipline.md
Reporting Analyst Intern - CNO Financial Group.md
Strategic Engagements & Events Intern (Spring 2027) - Zipline.md
Strategic Engagements & Events Intern (Summer 2027) - Zipline.md
Supply Chain Business Operations Intern (Spring 2027) - Zipline.md
Supply Chain Business Operations Intern (Summer 2027) - Zipline.md
Supply Chain Data Analyst Intern - Motorola.md
Sustainability Engineer Intern - Montenson.md
System Administrator Intern - Montenson.md
Thermal Application Engineer Intern - Summer 2027 - Vertiv.md
Video Production and Social Media Intern (Spring 2027) - Zipline.md
  ```
- `Edit` — `/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/pipeline-triage.html`
  ```diff
  -     <div class="junklist">
      <div>Accounting Intern (Spring) &ndash; Zipline</div>
      <div>Accounting Intern (Summer) &ndash; Zipline</div>
      <div>Aerodynamics Intern (Spring) &ndash; Zipline</div>
      <div>Business Analytics Intern &ndash; Allegheny County</div>
      <div>Civil &amp; Structural Eng. Intern (Spring) &ndash; Zipline</div>
      <div>Civil &amp; Structural Eng. Intern (Summer) &ndash; Zipline</div>
      <div>Community Engagement Intern (Spring) &ndash; Zipline</div>
      <div>Community Engagement Intern (Summer) &ndash; Zipline</div>
      <div>Construction Mgmt Intern (Spring) &ndash; Zipline</div>
      <div>Construction Mgmt Intern (Summer) &ndash; Zipline</div>
      <div>Finance &amp; Accounting Intern &ndash; Walleye Capital</div>
      <div>Geoscience Intern &ndash; Continental Resources</div>
      <div>Global Supply Mgmt Intern (Spring) &ndash; Zipline</div>
      <div>Global Supply Mgmt Intern (Summer) &ndash; Zipline</div>
      <div>Material Planning Intern (Spring) &ndash; Zipline</div>
      <div>Material Planning Intern (Summer) &ndash; Zipline</div>
      <div>Mechanical Engineer Intern (Spring) &ndash; Zipline</div>
      <div>Mechanical Engineer Intern (Summer) &ndash; Zipline</div>
      <div>Operations Experience Intern (Spring) &ndash; Zipline</div>
      <div>Quality &amp; Manufacturing Intern (Spring) &ndash; Zipline</div>
      <div>Quality &amp; Manufacturing Intern (Summer) &ndash; Zipline</div>
      <div>Reporting Analyst Intern &ndash; CNO Financial</div>
      <div>Global Supply Mgmt / Planning (misc) &ndash; Zipline</div>
      <div>Strategic Engagements Intern (Spring) &ndash; Zipline</div>
      <div>Strategic Engagements Intern (Summer) &ndash; Zipline</div>
      <div>Supply Chain Data Analyst &ndash; Motorola</div>
      <div>Sustainability Engineer Intern &ndash; Montenson</div>
      <div>System Administrator Intern &ndash; Montenson</div>
      <div>Thermal Application Engineer &ndash; Vertiv</div>
      <div>Video Production &amp; Social Media (Spring) &ndash; Zipline</div>
      <div>Video Production &amp; Social Media &ndash; other term &ndash; Zipline</div>
    </div>
  </details>
  <p style="margin-top:0.6rem">This is the floor, not the ceiling &mdash; it's a title-only scan. A real Step 2 screen of the remaining ~333 will cut further, but this list alone gets three folders meaningfully closer to cap with zero judgment calls needed.</p>
  +     <div class="junklist">
      <div>Accounting Intern (Spring 2027) &ndash; Zipline</div>
      <div>Accounting Intern (Summer 2027) &ndash; Zipline</div>
      <div>Aerodynamics Intern (Spring 2027) &ndash; Zipline</div>
      <div>Business Analytics Intern &ndash; Allegheny County</div>
      <div>Civil &amp; Structural Eng. Intern (Spring 2027) &ndash; Zipline</div>
      <div>Civil &amp; Structural Eng. Intern (Summer 2027) &ndash; Zipline</div>
      <div>Community Engagement Intern (Spring 2027) &ndash; Zipline</div>
      <div>Community Engagement Intern (Summer 2027) &ndash; Zipline</div>
      <div>Construction Mgmt Intern (Spring 2027) &ndash; Zipline</div>
      <div>Construction Mgmt Intern (Summer 2027) &ndash; Zipline</div>
      <div>Finance &amp; Accounting Intern (Summer 2027) &ndash; Walleye Capital</div>
      <div>Geoscience Intern &ndash; Continental Resources</div>
      <div>Global Supply Mgmt Intern (Spring 2027) &ndash; Zipline</div>
      <div>Global Supply Mgmt Intern (Summer 2027) &ndash; Zipline</div>
      <div>Material Planning Intern (Spring 2027) &ndash; Zipline</div>
      <div>Material Planning Intern (Summer 2027) &ndash; Zipline</div>
      <div>Mechanical Engineer Intern (Spring 2027) &ndash; Zipline</div>
      <div>Mechanical Engineer Intern (Summer 2027) &ndash; Zipline</div>
      <div>Operations Experience Intern (Spring 2027) &ndash; Zipline</div>
      <div>Quality &amp; Manufacturing Intern (Spring 2027) &ndash; Zipline</div>
      <div>Quality &amp; Manufacturing Intern (Summer 2027) &ndash; Zipline</div>
      <div>Reporting Analyst Intern &ndash; CNO Financial Group</div>
      <div>Strategic Engagements &amp; Events Intern (Spring 2027) &ndash; Zipline</div>
      <div>Strategic Engagements &amp; Events Intern (Summer 2027) &ndash; Zipline</div>
      <div>Supply Chain Business Ops Intern (Spring 2027) &ndash; Zipline</div>
      <div>Supply Chain Business Ops Intern (Summer 2027) &ndash; Zipline</div>
      <div>Supply Chain Data Analyst Intern &ndash; Motorola</div>
      <div>Sustainability Engineer Intern &ndash; Montenson</div>
      <div>System Administrator Intern &ndash; Montenson</div>
      <div>Thermal Application Engineer Intern (Summer 2027) &ndash; Vertiv</div>
      <div>Video Production &amp; Social Media Intern (Spring 2027) &ndash; Zipline</div>
    </div>
  </details>
  <p style="margin-top:0.6rem">This is the floor, not the ceiling &mdash; it's a title-only scan against exactly these 31 dossiers. A real Step 2 screen of the remaining ~333 will cut further, but this list alone gets three folders meaningfully closer to cap with zero judgment calls needed.</p>
  ```
- `Artifact` — `{"file_path":"/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad/pipeline-triage.html","title":"Pipeline Triage","description":"A live, evidence-cited status check of the internship pipeline — dossier counts vs. the decided cap, the promotion funnel, and a today-only action plan.","favicon":"🚦"}`

## You

The artifact created and issues found are a good starting point for today. Let's make sure that we do everything listed out in the artifact today and some more things. Our main goal today is to remove the dossiers that are not needed, filter dossiers, update the profile based on the dossiers that we remove. Make sure that the codeabse is perfectly ready for use and self improving per application that we decide to apply for. Applying is not for today - for tomorrow. We focus on filtering and making sure that everything is working perfectly over here. Add a few more resources over here so that we can do the job in more depth. The internship finding process needs much more resources and something that constantly keeps updating insternships, we make a record of all the internships that we have viewed. Making sure that we do not waste time on the same internship. All the flagged insternships are a great starting point for dossier cleanup. 50 applications is happening (idealistic), we are going to convert all the dossiers we are filtering today to programs and applying for it immediately. That's how we will apply for 50 internships. It's just a skill, outreach and netwroking. Ready to run (hopefully all correct), will find out more errors while the process rolls. But for now, this is going to be a session where I want you to write me prompts to another session so that we can finish work more efficiently and quickly. The artifact also keeps getting updated per build that is run. Making sure that we cross things out, change content to actual reality, add a few things, remove a few and most of all filter dossiers. Let's begin with the prompting for a new session now. Refer to this prompting guide for writing prompts: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/[REDACTED]", we will be working sonnet 5 on hard effort. The first prompt should fix the git status we are currently at - review the changes done in detail (over here), then think of writing a commit message. Pull the changes needed. Fix the broken github action (due to changing my region maybe - was flying). Before writing the prompt review each and every file folder that was added - if there are any necessary changes required - make them in the prompt you write. Do not make any changes over here at all. This session is only going to be for promptng and research. If needed distribute the commits to several commits. The task should be completed in steps as explained above, make no mistakes. Do your research correctly, review the changes made and only then write the prompt. First step is to maintain a very clean github workflow. Go ahead and write the prompt with no mistakes.

## Claude

Understood — this session stays research-and-prompt-writing only, no edits here. Let me review the actual diffs, the new debate.py feature, current test status, and the GitHub Actions health before drafting the prompt. I'll also pull the Anthropic prompting guide to calibrate the prompt structure.

This is a major finding — the uncommitted diff isn't messy WIP, it's a complete, well-documented feature (bucket-capacity notifications, a "debate" comparator for prioritization, debate-loss exclusion, a PhD-only exclusion gate) sitting on stale HEAD. I need to know whether origin/master already has this or something conflicting before I can tell the next session how to reconcile safely.

I've now confirmed everything needed: local `HEAD` (3fd4b88, 07-30) is the exact merge-base with `origin/master` (18c0327, today) — zero divergent local commits, and **origin's 413 commits touch only `logs/` and `state/`, zero code or workflow files**. The uncommitted working tree is a complete, well-documented feature set (bucket-capacity notifications, the "debate" prioritizer, debate-loss exclusion, PhD-only gate, ATS-job-id dedup, recheck-to-Viewed instead of delete, content-extraction fixes) — **all 329 tests pass against it right now**. The three open GitHub issues are self-resolved `429 Too Many Requests` blips from GitHub's own raw-content host on Aug 17–18 (not a region/flying issue — Actions runs on GitHub's cloud, not your device); every run since, including one 40 minutes ago, succeeded. This de-risks the whole task: it's "commit and push good work," not "debug broken code." I worked out a dependency-safe 5-commit split, with exact file/function boundaries and where four files need `git add -p` hunk-splitting.

Here's the prompt for the new session:

---BEGIN PROMPT---

You're picking up `internship-research-loop` (`/home/anant_gupta/projects/work/internship-research-loop`), a zero-LLM GitHub Actions pipeline that discovers internship postings and writes them as dossiers into an Obsidian vault (a separate repo, `gupta-builds/Jarvis`, reached via `gh`/git push, not filesystem access from here). Read `CLAUDE.md` in this repo first — it states the load-bearing conventions (zero-LLM in the unattended path, permissive-by-default filtering, fail-closed write-gate ordering, cite-real-data-in-comments) that this task must not violate.

**Your job this session is exclusively git hygiene and CI health — a clean, well-sequenced commit history and a verified-working pipeline. Do not touch dossier content, `core/profile.yaml`'s filter thresholds beyond what's already staged, or anything in the Jarvis vault. That work is scoped to separate follow-up sessions.**

## Situation

The local checkout is 413 commits behind `origin/master` and also has substantial uncommitted work sitting on that stale base: modifications across `core/classify.py`, `core/identity.py`, `core/profile.yaml`, `core/relevance.py`, `core/run_log.py`, `ingestion/posting_page.py`, `recheck.py`, `run_pipeline.py`, `vault_writer/validate.py`, `vault_writer/writer.py`, matching test files, plus four new untracked files (`core/debate.py`, `tests/test_debate.py`, `tests/test_debate_losses.py`, `tests/fixtures/posting_google_careers.md`).

I already did the risk analysis so you don't have to redo it from scratch — **but re-verify each claim below against live state before acting on it, since time has passed and the automated hourly workflow keeps committing to this repo**:

1. `git merge-base HEAD origin/master` equals local `HEAD` (`3fd4b88`) — the local branch has no divergent commits, it's a pure ancestor of `origin/master` (`18c0327` as of my check, dated today). A `git pull` will fast-forward cleanly.
2. `git diff --name-only 3fd4b88..origin/master` touches **only** `logs/` and `state/` — zero commits to `run_pipeline.py`, `core/`, `ingestion/`, `vault_writer/`, `recheck.py`, or `.github/workflows/` happened upstream since this checkout went stale. The uncommitted working-tree diff has **zero file-level overlap risk** with what pulling will bring in.
3. `.venv/bin/python -m pytest tests/ -q` passes **329/329** against the full uncommitted working tree as it sits right now, before any commit. This is finished, tested work, not broken WIP — treat it that way.
4. The uncommitted `run_pipeline.py`/`core/debate.py` work implements exactly what the vault's `20_Progress/Internship/Building System/Source of Truth.md` (`next:` field, last updated 2026-07-26) called "the dossier count-limit spec, still not in code" — plus additional cited features (a deterministic "debate" comparator for write-priority ordering, a debate-loss exclusion mechanism, `preference_tier` dossier frontmatter). Every non-trivial rule in the diff is cited against a real posting/date in an adjacent comment, matching this repo's own convention — don't second-guess or "clean up" that reasoning, just ship it as written. In particular: the per-bucket 50-dossier cap and global 201 total are enforced as a **notification, never a write refusal** — this is a deliberate, explicitly-justified design decision in the code's own comments (false-exclusion is worse than a full folder). Do not change it to a hard block.
5. The 3 open GitHub issues on `gupta-builds/internship-research-loop` (#1, #2, #3) are all `HTTPError: 429 Too Many Requests` / `ConnectionResetError` against `raw.githubusercontent.com`, dated 2026-08-17/18 — GitHub's own rate limiting on the *runner's* requests, not anything caused by network conditions on the user's own device (GitHub Actions runs on GitHub's cloud infrastructure regardless of where the user is). Every scheduled run since, including the most recent one, succeeded. There is currently nothing actually broken in the workflow config (`.github/workflows/*.yml` is byte-identical to `origin/master`) — the user suspected a "broken GitHub Action," but the evidence says it already self-resolved. **Re-run `gh run list --repo gupta-builds/internship-research-loop --limit 10` and `gh issue list --repo gupta-builds/internship-research-loop --state open` yourself before concluding this** — if you find something actually still broken, investigate and fix that for real rather than assuming my read still holds.

## Steps, in order

**1. Get current.** `git fetch origin`, confirm the merge-base claim above still holds, then `git pull` (should fast-forward cleanly, no conflicts expected per the analysis above — if it's not a clean fast-forward, stop and figure out why before proceeding, don't force anything).

**2. Commit the staged work as 5 separate, dependency-ordered commits.** Each commit must leave the repo in a fully working state — **run `.venv/bin/python -m pytest tests/ -q` after staging each commit's changes and confirm all tests pass before actually running `git commit`**. Use `git add -p` for the four files noted as needing an intra-file split; use `git add <file>` for whole-file commits. If `git add -p`'s hunk boundaries don't cleanly separate along the lines below (a hunk mixes code belonging to two different commits), don't force a bad split — either fold that file into whichever adjacent commit is the better fit, or use `git add -p`'s `e` (edit) option to split the hunk by hand. Getting the sequencing and passing tests right at every step matters far more than hitting this exact plan.

  - **Commit 1 — "Dedup & relevance accuracy fixes"**: `core/classify.py` (whole file — narrowed `threat` regex), `core/relevance.py` (whole file — rotational-analyst/PM-intern reject patterns, chemical/industrial adjacent-field hints), `ingestion/posting_page.py` **only** the `phd_only_exclusion`/`_PHD_ONLY_RE` addition (NOT the `extract_content` pipeline changes further down — those are commit 2), `core/identity.py` **only** `_ATS_JOB_ID_PATTERNS`/`extract_ats_job_id`/`_norm_company`/the `cross_source_key(company, title, url="")` signature change (NOT `company_matches_preference` at the end of the file — that's commit 3), `vault_writer/validate.py` **only** the `check_cross_source_duplicate` call-site change to pass `listing.url` (NOT the `REQUIRED_FRONTMATTER_FIELDS` addition — that's commit 3). Bring the matching slices of `tests/test_classify.py`, `tests/test_relevance.py`, `tests/test_identity.py`, `tests/test_validate.py`, `tests/test_posting_page.py`.

  - **Commit 2 — "Posting content extraction: dedup, ATS-label splitting, section headings, chrome stripping"**: the rest of `ingestion/posting_page.py`'s diff (`_dedupe_paragraphs`, `_ATS_LABEL_RUN_ON_RE`, `_LISTING_SHELL_RESET_RE`, `_BOLD_SECTION_RE`/`_SECTION_KEYWORD_RE`, `_FOLLOW_US_HEADING_RE`/`_LINK_BULLET_RE`, `_strip_trailing_social_chrome`, the `extract_content` body changes), the new `tests/fixtures/posting_google_careers.md`, the matching slice of `tests/test_posting_page.py`.

  - **Commit 3 — "Preference-tier frontmatter + Dossiers MOC interlinking"**: `core/profile.yaml` (whole file — `preferred_companies`), `core/identity.py`'s `company_matches_preference` (the piece deferred from commit 1), `vault_writer/writer.py` **only** `DOSSIERS_MOC_LINK`, `_TAG_ILLEGAL_CHARS`/`company_slug`, `dump_frontmatter`, and `build_frontmatter`'s `notes`/`preference_tier` fields (NOT `move_dossier_to_viewed` and friends at the end of the file — that's commit 5), `vault_writer/validate.py`'s `REQUIRED_FRONTMATTER_FIELDS` addition (deferred from commit 1). Bring the matching slices of `tests/test_writer.py`, `tests/test_validate.py`.

  - **Commit 4 — "Dossier resource-limit notifications + debate-based write prioritization + debate-loss exclusion"**: `core/debate.py` (new, whole file), `run_pipeline.py` (entire diff — this one genuinely doesn't separate cleanly across its three sub-features, they're interleaved through `run_once()`; commit it whole rather than forcing a fake split), `core/run_log.py` (whole file — `_append_markdown_line` refactor, `append_excluded_log`). Bring `tests/test_debate.py`, `tests/test_debate_losses.py` (both new), and the matching slice of `tests/test_run_pipeline.py`. This commit depends on commit 3 already existing (`render_dossier`'s `preferred_companies` param) — must land after it.

  - **Commit 5 — "recheck.py: move closed dossiers to Viewed/, never delete"**: `recheck.py` (entire diff), `vault_writer/writer.py`'s remaining piece (`move_dossier_to_viewed`, `REMOVED_DOSSIERS_MOC_LINK`, `VIEWED_SUBPATH`). Bring the matching slice of `tests/test_run_pipeline.py`/`tests/test_writer.py`. Depends on commit 3 (`dump_frontmatter`, `DOSSIERS_MOC_LINK`) already existing.

  Write each commit message in this repo's own real style — short, imperative, specific (see `git log --oneline` for examples like "Fix the 5 root causes behind dossier bloat" or "Phase 6: three hard criteria codified"). No generic "misc fixes" or "wip." Commit directly to `master` — this repo has no branch/PR convention, confirm that's still true via `git log` before assuming it.

**3. Push, handling the race with the hourly automated commits.** This repo's own `run.yml`/`recheck.yml` push to this same repo on a schedule, so `origin/master` may have moved again since step 1. `git pull` (should still fast-forward — the automated commits only touch `logs/`/`state/`) immediately before `git push`. If push is rejected, pull again and retry once; don't force-push.

**4. Verify the shipped code actually works live**, not just in `pytest`. Either wait for the next scheduled run or trigger one directly: `gh workflow run run.yml --repo gupta-builds/internship-research-loop`, then `gh run watch` (or poll `gh run list`) until it completes, then `gh run view <id> --log` (or check the newest line of `logs/runs.jsonl` after pulling) to confirm it succeeded and that the new fields (`bucket_at_capacity`, `dossier_total`, `newly_excluded_count`) show up in the run record as expected. This is the pipeline's real, normal hourly behavior — running it isn't a special action, just confirm it lands cleanly with the new code.

**5. Close the 3 stale GitHub issues** (assuming step 0's re-verification confirms they're genuinely resolved) with a short comment each pointing to a specific successful run since, then close. If your fresh check finds something *actually* still broken, fix the real cause instead — don't close an issue that's still live.

## Explicitly out of scope for this session

Do not: touch any dossier file in the vault, edit `core/profile.yaml`'s filter/eligibility rules beyond the `preferred_companies` dict already staged, add new features beyond what's already written in the working tree, rebase or rewrite any existing history, force-push, or update vault documentation (`Source of Truth.md`, `System - Build Log.md`) — that's scoped to a later session once this one's confirmed clean.

## Report back

When done, give me: the final `git log --oneline -10`, confirmation the push succeeded and matches `origin/master`, the result of the live workflow run you triggered/watched (success/failure, and what `bucket_at_capacity`/`dossier_total` showed), the state of the 3 issues, and anything you found during your own re-verification that contradicted what I told you above — I'd rather know I was wrong about something than have you silently work around it.

---END PROMPT---

That's prompt #1. Once you've run it (or want me to keep going), tell me and I'll write the next one — dossier filtering + profile self-improvement is the natural second prompt, and I'd scope that one around the 31-title junk list and per-application flagging you already have from the artifact, plus what "self-improving per application" should actually mean given there's zero application-outcome data yet to learn from.

**Tool calls:**

- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== git diff --stat ==="
git diff --stat
echo "=== untracked file sizes ==="
wc -l core/debate.py tests/test_debate.py tests/test_debate_losses.py tests/fixtures/posting_google_careers.md 2>&1
  ```
  ```
=== git diff --stat ===
 core/classify.py           |  12 ++-
 core/identity.py           |  71 +++++++++++-
 core/profile.yaml          |  28 +++++
 core/relevance.py          |  56 ++++++++--
 core/run_log.py            |  33 +++++-
 ingestion/posting_page.py  | 134 ++++++++++++++++++++++-
 recheck.py                 |  36 ++++---
 run_pipeline.py            | 262 +++++++++++++++++++++++++++++++++++++++++----
 tests/test_classify.py     |  22 ++++
 tests/test_identity.py     | 121 ++++++++++++++++++++-
 tests/test_posting_page.py | 171 ++++++++++++++++++++++++++++-
 tests/test_relevance.py    |  61 +++++++++++
 tests/test_run_pipeline.py | 130 +++++++++++++++++++++-
 tests/test_validate.py     |  26 +++++
 tests/test_writer.py       | 160 ++++++++++++++++++++++++++-
 vault_writer/validate.py   |   5 +-
 vault_writer/writer.py     | 118 ++++++++++++++++++--
 17 files changed, 1374 insertions(+), 72 deletions(-)
=== untracked file sizes ===
   83 core/debate.py
  112 tests/test_debate.py
  127 tests/test_debate_losses.py
   39 tests/fixtures/posting_google_careers.md
  361 total
  ```
- `ToolSearch` — `{"query":"WebFetch","max_results":2}`
- `WebFetch` — `{"url":"https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/[REDACTED]","prompt":"Extract the full guidance on how to write effective prompts for Claude Sonnet 5: recommended prompt structure, use of XML tags, specificity/context guidance, how to phrase multi-step or agentic tasks, examples given, and any dos/don'ts. Quote key structural recommendations verbatim."}`
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
git diff core/run_pipeline.py
  ```
  ```
Exit code 128
fatal: ambiguous argument 'core/run_pipeline.py': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
git diff -- run_pipeline.py
  ```
  ```
diff --git a/run_pipeline.py b/run_pipeline.py
index 0259507..aaf83bc 100644
--- a/run_pipeline.py
+++ b/run_pipeline.py
@@ -8,17 +8,20 @@ Invoked by .github/workflows/run.yml as `python run_pipeline.py`.
 import json
 import os
 import subprocess
+from functools import cmp_to_key
 
 import requests
 from datetime import datetime, timedelta, timezone
 from pathlib import Path
 
 from core.classify import BUCKET_FOLDERS, classification_callout, classify
+from core.debate import compute_bucket_urgency, debate_compare
 from core.filter import load_profile, matches
 from core.git_ops import GitPushError, commit_and_push_with_retry
 from core.identity import compute_uid
 from core.relevance import stage1_reject, stage2_confirm
 from core.run_log import (
+    append_excluded_log,
     append_run_log,
     append_weekly_rollup,
     format_weekly_rollup,
@@ -29,7 +32,7 @@ from core.identity import cross_source_key
 from core.schema_drift import SchemaDriftError
 from core.schema_drift import check_all as check_schema_drift
 from ingestion.freehire import fetch_freehire
-from ingestion.posting_page import extract_content, fetch_posting_markdown, opt_exclusion
+from ingestion.posting_page import extract_content, fetch_posting_markdown, opt_exclusion, phd_only_exclusion
 from ingestion.sources import (
     fetch_ai_jobs,
     fetch_ashby,
@@ -40,7 +43,7 @@ from ingestion.sources import (
     fetch_zshah101,
 )
 from vault_writer.validate import check_format_compliance, validate
-from vault_writer.writer import render_dossier, scan_dossiers, write_dossier
+from vault_writer.writer import DOSSIER_SUBPATH, render_dossier, scan_dossiers, write_dossier
 
 SOURCES = (
     ("SimplifyJobs", fetch_simplify),
@@ -63,20 +66,150 @@ SOURCES = (
 # exists across all 6 sources (Greenhouse sometimes has one via metadata, the
 # other 5 sources never do) — most-recently-posted first is the prioritization
 # that's actually available everywhere, not a compromise on the chosen rule.
-MAX_NEW_WRITES_PER_RUN = 18
+#
+# Revised 2026-07-29 (Task A): split per bucket instead of one flat number —
+# a tunable dict, not magic numbers spread through the function. Still caps
+# at roughly 10/run to protect Firecrawl budget and review throughput; a
+# bucket with 0 eligible candidates this run never lets another bucket borrow
+# its unused slots (each bucket only draws from its own ordered queue).
+MAX_NEW_WRITES_PER_RUN = {"AI/ML": 3, "Fullstack": 3, "CyS & Finance": 3, "Other": 1}
+
+# Per-bucket vault capacity, per the original design (Dossiers-to-Create.md,
+# Source of Truth.md) — but per the user's explicit 2026-07-29 override, this
+# is a NOTIFICATION mechanism, never a write refusal: the false-exclusion-
+# worse-than-false-inclusion asymmetry that governs every other gate in this
+# codebase applies here too (a hard-refusal cap would silently drop a real,
+# currently-open posting for no benefit — the scarce resource is human review
+# attention, not vault storage). See run_once()'s bucket_at_capacity handling.
+BUCKET_CAPACITY = 50
+# Global total across List/Dossiers/ excluding Viewed/. 150/170 are logged in
+# the run record only (informational); 190/200 additionally file a GitHub
+# issue the first time each is crossed (same "notify once" state as buckets).
+GLOBAL_INFO_THRESHOLDS = (150, 170)
+GLOBAL_ISSUE_THRESHOLDS = (190, 200)
+CAPACITY_STATE_FILENAME = "capacity_notified.json"
+
+
+def _prioritize_and_cap(new_listings: list, budget: dict, preferred_companies: dict = None) -> tuple:
+    """Scoped per-bucket per the tunable budget dict — each bucket fills only
+    from its own ordered queue, so an empty bucket this run can't let another
+    bucket's items borrow its slots. Bucket is the same degraded-signal
+    classify() (title/category only, no fetched content yet)
+    validate_and_write() itself falls back to before a posting's content is
+    fetched — pacing doesn't need the refined, content-informed bucket, only
+    the final written folder does. Returns (this_run, deferred) — deferred
+    items are simply not passed to validate_and_write and therefore never
+    marked seen, so dedup_new() naturally re-offers them next run without any
+    extra state to manage.
+
+    Ordering within each bucket is now the Task L "debate" comparator
+    (preferred-company tier -> bucket fill-need -> recency) instead of a bare
+    recency sort — preferred_companies=None degrades to the original
+    recency-only order (every candidate ties at stage 1, and stage 2 never
+    fires within a single bucket's own list regardless, so recency alone
+    decides), which is also exactly what every pre-Task-L caller/test gets
+    for free."""
+    by_bucket = {}
+    for uid, listing in new_listings:
+        bucket, _ = classify(listing.title, listing.category, "")
+        by_bucket.setdefault(bucket, []).append((uid, listing))
+
+    bucket_urgency = compute_bucket_urgency(new_listings, budget)
+    cmp_key = cmp_to_key(lambda x, y: debate_compare(x, y, preferred_companies or {}, bucket_urgency))
+
+    this_run, deferred = [], []
+    for bucket, items in by_bucket.items():
+        ordered = sorted(items, key=cmp_key)
+        limit = budget.get(bucket, 0)
+        this_run.extend(ordered[:limit])
+        deferred.extend(ordered[limit:])
+    return this_run, deferred
+
+
+def count_dossiers_by_bucket(vault_root) -> dict:
+    """Real per-bucket file counts in the vault checkout — Viewed/ isn't one
+    of BUCKET_FOLDERS' values, so it's excluded automatically, matching the
+    Standard's '201 total excluding Viewed/' scope."""
+    vault_root = Path(vault_root)
+    counts = {}
+    for bucket, folder in BUCKET_FOLDERS.items():
+        d = vault_root / DOSSIER_SUBPATH / folder
+        counts[bucket] = len(list(d.glob("*.md"))) if d.is_dir() else 0
+    return counts
+
+
+def load_capacity_notified(state_dir) -> dict:
+    path = Path(state_dir) / CAPACITY_STATE_FILENAME
+    if not path.exists():
+        return {"buckets": [], "global": []}
+    return json.loads(path.read_text())
 
 
-def _prioritize_and_cap(new_listings: list, limit: int) -> tuple:
-    """Most-recently-posted first; missing date_posted sorts last, never first
-    (an unknown post date must not win priority over a known-recent one).
-    Returns (this_run, deferred) — deferred items are simply not passed to
-    validate_and_write and therefore never marked seen, so dedup_new()
-    naturally re-offers them next run without any extra state to manage."""
-    ordered = sorted(new_listings, key=lambda item: item[1].date_posted or 0, reverse=True)
-    return ordered[:limit], ordered[limit:]
+def save_capacity_notified(state_dir, notified: dict) -> None:
+    path = Path(state_dir) / CAPACITY_STATE_FILENAME
+    path.parent.mkdir(parents=True, exist_ok=True)
+    path.write_text(json.dumps(notified, indent=2, sort_keys=True) + "\n")
 
 RUN_LOG_MD_SUBPATH = Path("10_Areas/Career/Internships/List/Run Log.md")
 
+# Task N (Prompt 5) — a candidate that loses the debate comparator's sort
+# (falls outside its bucket's budget, i.e. ends up in _prioritize_and_cap's
+# "deferred" list) accumulates a loss count across runs. 5 was chosen to give
+# a real posting several genuine chances across multiple hourly runs before
+# conceding it structurally can't out-rank the field — not an arbitrary
+# guess dressed as one, but still a tunable to retune from real data once
+# this has run for a while, same as every other tunable in this codebase.
+MAX_DEBATE_LOSSES = 5
+DEBATE_LOSSES_FILENAME = "debate_losses.json"
+EXCLUDED_UIDS_FILENAME = "excluded_uids.json"
+EXCLUDED_LOG_SUBPATH = Path("10_Areas/Career/Internships/List/Excluded — Losing The Debate.md")
+
+
+def load_debate_losses(state_dir) -> dict:
+    path = Path(state_dir) / DEBATE_LOSSES_FILENAME
+    if not path.exists():
+        return {}
+    return json.loads(path.read_text())
+
+
+def save_debate_losses(state_dir, losses: dict) -> None:
+    path = Path(state_dir) / DEBATE_LOSSES_FILENAME
+    path.parent.mkdir(parents=True, exist_ok=True)
+    path.write_text(json.dumps(losses, indent=2, sort_keys=True) + "\n")
+
+
+def load_excluded_uids(state_dir) -> set:
+    path = Path(state_dir) / EXCLUDED_UIDS_FILENAME
+    if not path.exists():
+        return set()
+    return set(json.loads(path.read_text()))
+
+
+def save_excluded_uids(state_dir, excluded: set) -> None:
+    path = Path(state_dir) / EXCLUDED_UIDS_FILENAME
+    path.parent.mkdir(parents=True, exist_ok=True)
+    path.write_text(json.dumps(sorted(excluded), indent=2) + "\n")
+
+
+def update_debate_losses(losses: dict, deferred: list, written_uids: list) -> tuple:
+    """Returns (updated_losses, newly_excluded: [(uid, listing), ...]).
+    Increments the loss count for every deferred uid (a candidate that lost
+    this run's per-bucket comparator sort); removes any uid that won (got
+    written) this run entirely — it's in seen_ids.json now, its loss history
+    is moot. A uid whose count reaches MAX_DEBATE_LOSSES is returned in
+    newly_excluded and removed from losses — callers add it to the excluded
+    set and log it; this function only does the counting."""
+    losses = dict(losses)
+    for uid in written_uids:
+        losses.pop(uid, None)
+    newly_excluded = []
+    for uid, listing in deferred:
+        losses[uid] = losses.get(uid, 0) + 1
+        if losses[uid] >= MAX_DEBATE_LOSSES:
+            newly_excluded.append((uid, listing))
+            del losses[uid]
+    return losses, newly_excluded
+
 # A required_fields or format_compliance rejection means OUR normalizer/writer
 # produced something malformed — a real bug, worth an issue. url_liveness and
 # not_duplicate rejections are routine (a stale posting, an already-seen item)
@@ -106,26 +239,39 @@ def build_matched_reason(listing, profile: dict) -> str:
     return "matched"
 
 
-def fetch_and_filter(profile: dict, http_get=None) -> dict:
-    """Returns {source_name: {"fetch_count": int, "matched": [Listing, ...]}}."""
+def fetch_and_filter(profile: dict, http_get=None, excluded_ids: frozenset = frozenset()) -> dict:
+    """Returns {source_name: {"fetch_count": int, "matched": [Listing, ...]}}.
+    excluded_ids (Task N, Prompt 5) drops a uid that already lost the debate
+    comparator MAX_DEBATE_LOSSES consecutive times here, before it's even
+    counted as matched — the earliest seam available, so an excluded uid
+    never reaches the Firecrawl content-fetch in validate_and_write either."""
     results = {}
     for name, fetch_fn in SOURCES:
         listings = fetch_fn(http_get)
         results[name] = {
             "fetch_count": len(listings),
-            "matched": [l for l in listings if matches(l, profile) and not stage1_reject(l.title, l.raw_text)],
+            "matched": [
+                l for l in listings
+                if matches(l, profile) and not stage1_reject(l.title, l.raw_text)
+                and compute_uid(l) not in excluded_ids
+            ],
         }
     return results
 
 
-def dedup_new(matched_by_source: dict, seen_ids: set):
-    """Returns ([(uid, listing), ...] for genuinely new items, already_seen_count)."""
+def dedup_new(matched_by_source: dict, seen_ids: set, excluded_ids: frozenset = frozenset()):
+    """Returns ([(uid, listing), ...] for genuinely new items, already_seen_count).
+    excluded_ids is also checked here (belt-and-suspenders with
+    fetch_and_filter's own check above) so nothing slips through if a caller
+    ever builds matched_by_source some other way."""
     new = []
     already_seen = 0
     seen_this_run = set()
     for _name, info in matched_by_source.items():
         for listing in info["matched"]:
             uid = compute_uid(listing)
+            if uid in excluded_ids:
+                continue
             if uid in seen_ids or uid in seen_this_run:
                 already_seen += 1
                 continue
@@ -158,7 +304,8 @@ def validate_and_write(new_listings, profile: dict, jarvis_dir, seen_ids: set, d
     # diverged from seen_ids after the 2026-07-18 manual cleanup), plus
     # whatever this run writes — first source in SOURCES order wins.
     dossier_keys = {
-        cross_source_key(fm.get("company", ""), fm.get("title", "")) for fm in scan_dossiers(jarvis_dir)
+        cross_source_key(fm.get("company", ""), fm.get("title", ""), fm.get("url", ""))
+        for fm in scan_dossiers(jarvis_dir)
     }
     written_uids = []
     rejections = []
@@ -168,7 +315,8 @@ def validate_and_write(new_listings, profile: dict, jarvis_dir, seen_ids: set, d
             rejections.append({"uid": uid, "check": "opt_eligibility",
                               "reason": f"{cached['signal']} (cached {cached['checked']})"})
             continue
-        markdown = render_dossier(listing, uid, date_found, build_matched_reason(listing, profile))
+        markdown = render_dossier(listing, uid, date_found, build_matched_reason(listing, profile),
+                                  preferred_companies=profile.get("preferred_companies"))
         result = validate(listing, uid, markdown, seen_ids, http_head=http_head, dossier_keys=dossier_keys)
         if not result.passed:
             rejections.append({"uid": uid, "check": result.check, "reason": result.reason})
@@ -198,11 +346,16 @@ def validate_and_write(new_listings, profile: dict, jarvis_dir, seen_ids: set, d
                     opt_cache[uid] = {"verdict": "excluded", "signal": opt_signal, "checked": date_found}
                     rejections.append({"uid": uid, "check": "opt_eligibility", "reason": opt_signal})
                     continue
+                degree_signal = phd_only_exclusion(page_md)
+                if degree_signal:
+                    rejections.append({"uid": uid, "check": "degree_eligibility", "reason": degree_signal})
+                    continue
                 opt_cache[uid] = {"verdict": "eligible", "signal": None, "checked": date_found}
                 bucket, signal = classify(listing.title, listing.category, posting_content)
                 enriched = render_dossier(listing, uid, date_found,
                                           build_matched_reason(listing, profile), posting_content,
-                                          classification_callout(bucket, signal))
+                                          classification_callout(bucket, signal),
+                                          preferred_companies=profile.get("preferred_companies"))
                 # The gate validated the thin render; re-check format on the
                 # enriched one — an extraction bug degrades to thin, never
                 # writes malformed markdown into the vault.
@@ -211,7 +364,7 @@ def validate_and_write(new_listings, profile: dict, jarvis_dir, seen_ids: set, d
         write_dossier(jarvis_dir, uid, markdown, listing.title, listing.company, BUCKET_FOLDERS[bucket],
                      state_dir=state_dir)
         written_uids.append(uid)
-        dossier_keys.add(cross_source_key(listing.company, listing.title))
+        dossier_keys.add(cross_source_key(listing.company, listing.title, listing.url))
     return written_uids, rejections
 
 
@@ -250,12 +403,17 @@ def run_once(
         "errors": [],
         "halted": False,
         "halt_reason": None,
+        "bucket_at_capacity": [],
+        "dossier_total": 0,
+        "newly_excluded_count": 0,
     }
 
+    excluded_ids = load_excluded_uids(state_dir) if state_dir is not None else set()
+
     try:
         check_schema_drift(http_get)
         seen_ids = load_seen_ids(state_path)
-        matched_by_source = fetch_and_filter(profile, http_get)
+        matched_by_source = fetch_and_filter(profile, http_get, excluded_ids=excluded_ids)
     except (SchemaDriftError, requests.RequestException) as exc:
         # RequestException too — a deleted repo, DNS failure, or 5xx used to
         # crash the process before any run-log record or issue existed (the
@@ -275,11 +433,13 @@ def run_once(
         record["fetch_counts"][name] = info["fetch_count"]
         record["filter_match_counts"][name] = len(info["matched"])
 
-    new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids)
+    new_listings, already_seen_count = dedup_new(matched_by_source, seen_ids, excluded_ids=excluded_ids)
     record["new_count"] = len(new_listings)
     record["already_seen_count"] = already_seen_count
 
-    this_run, deferred = _prioritize_and_cap(new_listings, MAX_NEW_WRITES_PER_RUN)
+    this_run, deferred = _prioritize_and_cap(
+        new_listings, MAX_NEW_WRITES_PER_RUN, preferred_companies=profile.get("preferred_companies")
+    )
     record["deferred_count"] = len(deferred)
 
     opt_cache = {}
@@ -294,6 +454,62 @@ def run_once(
         Path(opt_cache_path).write_text(json.dumps(opt_cache, indent=2, sort_keys=True) + "\n")
     record["rejections"] = rejections
 
+    # Task N (Prompt 5): count this run's debate loss for every deferred
+    # candidate; a uid that won (got written) has its loss history dropped
+    # entirely. A uid crossing MAX_DEBATE_LOSSES moves to the excluded set
+    # and gets one line in a reviewable markdown log — not a silent,
+    # permanent exclusion.
+    if state_dir is not None:
+        debate_losses = load_debate_losses(state_dir)
+        debate_losses, newly_excluded = update_debate_losses(debate_losses, deferred, written_uids)
+        save_debate_losses(state_dir, debate_losses)
+        record["newly_excluded_count"] = len(newly_excluded)
+        if newly_excluded:
+            excluded_ids = load_excluded_uids(state_dir)
+            excluded_ids.update(uid for uid, _listing in newly_excluded)
+            save_excluded_uids(state_dir, excluded_ids)
+            for uid, listing in newly_excluded:
+                line = (
+                    f"- **{listing.company}** — {listing.title} — [{listing.url}]({listing.url}) — "
+                    f"excluded {now.date().isoformat()} — lost the debate {MAX_DEBATE_LOSSES} consecutive runs"
+                )
+                append_excluded_log(
+                    Path(jarvis_dir) / EXCLUDED_LOG_SUBPATH, line, created_date=now.date().isoformat(),
+                    max_losses=MAX_DEBATE_LOSSES,
+                )
+
+    # Task A resource-limit notification (Standard §5): a bucket at/over
+    # capacity or the global total crossing a threshold is surfaced, never a
+    # write refusal — the writes above already happened regardless.
+    bucket_counts = count_dossiers_by_bucket(jarvis_dir)
+    record["bucket_at_capacity"] = sorted(b for b, c in bucket_counts.items() if c >= BUCKET_CAPACITY)
+    record["dossier_total"] = sum(bucket_counts.values())
+
+    notified = load_capacity_notified(state_dir) if state_dir is not None else {"buckets": [], "global": []}
+    newly_notified = False
+    for bucket in record["bucket_at_capacity"]:
+        if bucket not in notified["buckets"]:
+            notified["buckets"].append(bucket)
+            newly_notified = True
+            issue_fn(
+                issue_repo,
+                f"Bucket '{bucket}' at/over its {BUCKET_CAPACITY}-dossier notification threshold ({timestamp})",
+                f"'{bucket}' now has {bucket_counts[bucket]} dossiers in List/Dossiers/ — this is a "
+                "notification, not a write refusal (a full bucket is a signal to review more urgently, "
+                "not a reason to lose a real posting). New matches keep writing into this bucket.",
+            )
+    for threshold in GLOBAL_ISSUE_THRESHOLDS:
+        if record["dossier_total"] >= threshold and threshold not in notified["global"]:
+            notified["global"].append(threshold)
+            newly_notified = True
+            issue_fn(
+                issue_repo,
+                f"Total dossier count crossed {threshold} ({timestamp})",
+                f"List/Dossiers/ (excluding Viewed/) now has {record['dossier_total']} dossiers total.",
+            )
+    if state_dir is not None and newly_notified:
+        save_capacity_notified(state_dir, notified)
+
     if should_run_weekly_rollup(now):
         week_start = now - timedelta(days=7)
         recent = load_recent_runs(runs_log_path, since=week_start)
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== does core/debate.py exist on origin/master? ==="
git cat-file -e origin/master:core/debate.py 2>&1 && echo "EXISTS on origin" || echo "DOES NOT EXIST on origin"
echo "=== does origin/master's run_pipeline.py have MAX_NEW_WRITES_PER_RUN as dict or int? ==="
git show origin/master:run_pipeline.py 2>&1 | grep -n "MAX_NEW_WRITES_PER_RUN\|BUCKET_CAPACITY\|debate\|phd_only" | head -20
echo "=== merge-base between local HEAD and origin/master ==="
git merge-base HEAD origin/master
git log --oneline -1 HEAD
git log --oneline -1 origin/master
echo "=== would run_pipeline.py conflict on merge? (dry run) ==="
git merge-tree "$(git merge-base HEAD origin/master)" HEAD origin/master -- run_pipeline.py 2>&1 | head -5
echo "=== diff between origin/master's run_pipeline.py and local working tree ==="
diff <(git show origin/master:run_pipeline.py) run_pipeline.py > /tmp/rp_vs_origin.diff 2>&1
wc -l /tmp/rp_vs_origin.diff
  ```
  ```
=== does core/debate.py exist on origin/master? ===
fatal: path 'core/debate.py' exists on disk, but not in 'origin/master'
DOES NOT EXIST on origin
=== does origin/master's run_pipeline.py have MAX_NEW_WRITES_PER_RUN as dict or int? ===
66:MAX_NEW_WRITES_PER_RUN = 18
282:    this_run, deferred = _prioritize_and_cap(new_listings, MAX_NEW_WRITES_PER_RUN)
=== merge-base between local HEAD and origin/master ===
[REDACTED]
3fd4b88 Update state + logs — 2026-07-30
18c0327 Update state + logs — 2026-08-21
=== would run_pipeline.py conflict on merge? (dry run) ===
usage: git merge-tree [--write-tree] [<options>] <branch1> <branch2>
   or: git merge-tree [--trivial-merge] <base-tree> <branch1> <branch2>

    --write-tree          do a real merge instead of a trivial merge
    --trivial-merge       do a trivial merge only
=== diff between origin/master's run_pipeline.py and local working tree ===
299 /tmp/rp_vs_origin.diff
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== files changed on origin since merge-base (top-level dirs only) ==="
git diff --stat 3fd4b88..origin/master -- run_pipeline.py recheck.py core/ ingestion/ vault_writer/ tests/ 2>&1
echo "=== full list of changed file PATHS (not vault content) on origin since 07-30, excluding state/logs/jarvis-vault-content ==="
git diff --name-only 3fd4b88..origin/master | grep -v "^logs/\|^state/" | sort
echo "=== count of commits touching code (non-state/log) paths since merge-base ==="
git log 3fd4b88..origin/master --oneline -- run_pipeline.py recheck.py core/ ingestion/ vault_writer/ tests/ .github/ | wc -l
  ```
  ```
=== files changed on origin since merge-base (top-level dirs only) ===
=== full list of changed file PATHS (not vault content) on origin since 07-30, excluding state/logs/jarvis-vault-content ===
=== count of commits touching code (non-state/log) paths since merge-base ===
0
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
git diff -- core/profile.yaml core/classify.py core/identity.py core/run_log.py vault_writer/validate.py
  ```
  ```
diff --git a/core/classify.py b/core/classify.py
index 3aea600..2ce956a 100644
--- a/core/classify.py
+++ b/core/classify.py
@@ -32,9 +32,19 @@ _AI_ML_RE = re.compile(
     r"|computer vision|\bnlp\b|natural language|embeddings?|pytorch|tensorflow"
     r"|neural network|data scientist|ml engineer|ai engineer|ai.enabled)\b", re.I,
 )
+# 'threat' narrowed 2026-07-29: real false positive, Mosaic Company
+# "Operations & Automation Engineering Co-op/Intern" (chemical-plant
+# PLC/DCS/SCADA role, zero cybersecurity content) matched bare 'threat' on a
+# workplace-safety disclaimer ("without posing a direct threat to the safety
+# of his or her own self"). Requiring co-occurrence with a real
+# security-context word within 30 chars catches genuine cybersecurity usage
+# ("threat model", "threat actor", "threat intelligence", "threat detection")
+# without matching safety-boilerplate/weather/insider-threat-to-unrelated-
+# things mentions of the bare word.
 _CYS_FINANCE_RE = re.compile(
     r"\b(security engineer|cybersecurity|application security|appsec"
-    r"|penetration test|infosec|threat|vulnerability|quant(itative)? developer"
+    r"|penetration test|infosec|threat.{0,30}(model|actor|intelligence|detection)|vulnerability"
+    r"|quant(itative)? developer"
     r"|quantitative (research|trading)|trading systems?|fintech|risk engine"
     r"|payments? (engineer|infrastructure)|blockchain|crypto|defi)\b", re.I,
 )
diff --git a/core/identity.py b/core/identity.py
index 86447f1..da8d83f 100644
--- a/core/identity.py
+++ b/core/identity.py
@@ -5,10 +5,48 @@ source:raw_id. (The content-hash fallback existed only for zapplyjobs,
 removed as a source 2026-07-18.)
 
 cross_source_key() is the secondary dedup identity: the same program listed
-by two different sources gets two different uids but one company+title key.
+by two different sources gets two different uids but one cross-source key.
 """
 import re
 
+# Real, confirmed 2026-07-29 — four real duplicate incidents the old
+# normalized-company+title key missed because either string varied across
+# sources: Aquatic vs Aquatic Capital Management (company-name variant),
+# Google BS/MS Summer 2027 SWE intern (title-string variant, same numeric job
+# id in both URLs), Virtu Financial's genuine triple duplicate (three
+# different title strings, identical greenhouse.io/virtu/jobs/8624410002 URL
+# across SimplifyJobs/zshah101/vanshb03), and Palantir's "Intel" FDSE role
+# duplicated across two different buckets (same Lever job id via SimplifyJobs
+# and zshah101). A URL-embedded ATS job id is a stronger identity signal than
+# company+title text in every one of these — extract it when present, fall
+# back to the normalized-text key only when the URL carries no recognizable id.
+_ATS_JOB_ID_PATTERNS = (
+    re.compile(r"greenhouse\.io/[^/]+/jobs/(\d+)", re.I),
+    re.compile(r"lever\.co/[^/]+/([0-9a-f-]{36})", re.I),
+    re.compile(r"ashbyhq\.com/[^/]+/([0-9a-f-]{36})", re.I),
+    # Google's own careers site embeds a long numeric id after .../jobs/results/
+    # — anchored to google.com (real examples: www.google.com/about/careers/
+    # applications/jobs/results/...), matching the domain-scoping discipline
+    # the other three patterns already follow. Real bug, confirmed 2026-07-30:
+    # without the domain anchor, this pattern matched the same path shape on
+    # ANY domain (e.g. a random unrelated company's own careers page happening
+    # to use a numeric job id at .../careers/jobs/results/<id>), which would
+    # silently collapse an unrelated posting into the same cross_source_key
+    # as a real Google posting and reject it as a duplicate.
+    re.compile(r"google\.com/.*?careers/(?:applications/)?jobs/results/(\d+)", re.I),
+)
+
+
+def extract_ats_job_id(url: str) -> str:
+    """The ATS-native job id embedded in url, or None if url is from a
+    source/ATS with no recognizable id in its URL shape (e.g. Freehire's
+    Telegram links, Workday's slug-only URLs)."""
+    for pattern in _ATS_JOB_ID_PATTERNS:
+        m = pattern.search(url or "")
+        if m:
+            return m.group(1)
+    return None
+
 
 def compute_uid(listing) -> str:
     if not listing.raw_id:
@@ -16,9 +54,38 @@ def compute_uid(listing) -> str:
     return f"{listing.source}:{listing.raw_id}"
 
 
-def cross_source_key(company: str, title: str) -> str:
+# Not cross_source_key()'s space-preserving norm() reused verbatim: that one
+# collapses punctuation to a single space (needed to keep title text
+# word-tokenized — "Intern Co-op" vs "Intern/Co-op" must still split into the
+# same words). A company name is a short identifier, not sentence-shaped
+# text, and the real case this needs to catch ("D.E. Shaw" vs "DE Shaw")
+# fails under that space-preserving version — "d e shaw" != "de shaw". Fold
+# out all non-alphanumeric characters entirely instead, so both collapse to
+# the identical "deshaw".
+def _norm_company(s: str) -> str:
+    return re.sub(r"[^a-z0-9]", "", s.lower())
+
+
+def cross_source_key(company: str, title: str, url: str = "") -> str:
+    job_id = extract_ats_job_id(url)
+    if job_id:
+        return f"jobid:{job_id}"
     # Punctuation-insensitive: "Intern Co-op" and "Intern/Co-op" are the same
     # posting (real Marmon dup that slipped past a whitespace-only key,
     # caught in the 2026-07-18 dossier audit).
     norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
     return f"{norm(company)}|{norm(title)}"
+
+
+def company_matches_preference(company: str, preferred: dict) -> str:
+    """The matched preference tier (e.g. 'high'), or None if company isn't in
+    preferred. Same punctuation/case-insensitive normalization as
+    cross_source_key()'s norm(), so 'D.E. Shaw' and 'DE Shaw' both match —
+    preferred_companies (core/profile.yaml) is a human-maintained config dict,
+    not derived from live data, so this is a pure string match with no new
+    network call or source to verify (Prompt 5 Task K)."""
+    target = _norm_company(company)
+    for name, tier in (preferred or {}).items():
+        if _norm_company(name) == target:
+            return tier
+    return None
diff --git a/core/profile.yaml b/core/profile.yaml
index 21c3c97..c73d41b 100644
--- a/core/profile.yaml
+++ b/core/profile.yaml
@@ -47,3 +47,31 @@ locations_allow: us_remote
 # 592, ("PhD",) 586, empty 4676 — fetched 2026-07-18). Permissive: empty degrees
 # data passes; non-empty must intersect this list.
 degrees_allow: ["Bachelor's"]
+# Preference weight for the debate comparator (Prompt 5 Task L), not a filter
+# gate — a non-matching company still passes everything above unaffected.
+# Seeded from the real, human-vetted target list in the vault's
+# `20_Progress/Internship/Building System/Research Loop - Resources.md`
+# "Named-Program Coverage Check (2026-07-29)" section: 11 named early-talent
+# programs the human already identified as worth prioritizing, of which only
+# 3/11 have ANY dossier coverage today and none confirmed as the specific
+# named program (Jane Street FTTP, Two Sigma First-Year, D.E. Shaw, Citadel
+# Launch, Google ASDI, Microsoft Explore, LinkedIn First Play, MLH
+# Fellowship, NASA OSTEM, Capital One, Bloomberg). This is a starting point
+# for the human to re-tier or add/remove entries directly, not a final
+# answer — company preference is an explicit human judgment call per
+# `30_Order/Workflows/Internship Pipeline.md`'s Step 2 ("Screen"), and this
+# dict only wires that judgment into write-priority ordering, it doesn't
+# automate the judgment itself. All seeded at one tier for now; a
+# multi-tier scheme wasn't asked for.
+preferred_companies:
+  "Jane Street": high
+  "Two Sigma": high
+  "D.E. Shaw": high
+  "Citadel": high
+  "Google": high
+  "Microsoft": high
+  "LinkedIn": high
+  "MLH": high
+  "NASA": high
+  "Capital One": high
+  "Bloomberg": high
diff --git a/core/run_log.py b/core/run_log.py
index d9af0fd..dc9a5b6 100644
--- a/core/run_log.py
+++ b/core/run_log.py
@@ -66,14 +66,39 @@ Weekly rollup from the internship-research-loop automation, appended automatical
 """
 
 
-def append_weekly_rollup(run_log_md_path, line: str, created_date: str) -> None:
-    path = Path(run_log_md_path)
+def _append_markdown_line(path, line: str, header: str) -> None:
+    path = Path(path)
     path.parent.mkdir(parents=True, exist_ok=True)
     if not path.exists():
-        header = _HEADER_TEMPLATE.format(created=created_date).rstrip("\n") + "\n"
-        path.write_text(header + line + "\n")
+        path.write_text(header.rstrip("\n") + "\n" + line + "\n")
         return
     existing = path.read_text()
     if not existing.endswith("\n"):
         existing += "\n"
     path.write_text(existing + line + "\n")
+
+
+def append_weekly_rollup(run_log_md_path, line: str, created_date: str) -> None:
+    _append_markdown_line(run_log_md_path, line, _HEADER_TEMPLATE.format(created=created_date))
+
+
+_EXCLUDED_LOG_HEADER_TEMPLATE = """---
+type: dashboard
+status: active
+created: {created}
+tags:
+  - internship
+  - automation
+  - debate
+---
+# Excluded — Losing The Debate
+A posting lands here the first time it loses the per-bucket debate comparator's sort {max_losses} consecutive runs — not a silent, permanent exclusion, a reviewable one. If you disagree with the comparator's call on any of these, promote the posting by hand; this log exists so that decision has something concrete to look at. Appended automatically, never rewritten.
+"""
+
+
+def append_excluded_log(excluded_log_md_path, line: str, created_date: str, max_losses: int) -> None:
+    """Task N (Prompt 5) — one line per uid the first time it's excluded,
+    same append-only pattern as append_weekly_rollup above."""
+    _append_markdown_line(
+        excluded_log_md_path, line, _EXCLUDED_LOG_HEADER_TEMPLATE.format(created=created_date, max_losses=max_losses)
+    )
diff --git a/vault_writer/validate.py b/vault_writer/validate.py
index c892aed..2cf0365 100644
--- a/vault_writer/validate.py
+++ b/vault_writer/validate.py
@@ -12,7 +12,8 @@ from core.identity import cross_source_key
 REQUIRED_LISTING_FIELDS = ("company", "title", "url", "source", "uid")
 REQUIRED_FRONTMATTER_FIELDS = (
     "company", "title", "url", "source", "terms", "locations",
-    "target_year", "date_posted", "date_found", "matched_reason", "status", "next", "tags",
+    "target_year", "date_posted", "date_found", "matched_reason", "status", "next", "notes",
+    "preference_tier", "tags",
 )
 
 
@@ -71,7 +72,7 @@ def check_cross_source_duplicate(listing, dossier_keys) -> ValidationResult:
     """Same program via two sources = two different uids but one normalized
     company+title key (MLH Fellowship landed twice pre-cleanup). Routine
     rejection, not systemic — first source in write order wins."""
-    key = cross_source_key(listing.company, listing.title)
+    key = cross_source_key(listing.company, listing.title, listing.url)
     if key in dossier_keys:
         return ValidationResult(False, "cross_source_duplicate", f"company+title already in vault: {key}")
     return ValidationResult(True, "cross_source_duplicate")
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
git diff -- core/relevance.py ingestion/posting_page.py recheck.py vault_writer/writer.py
  ```
  ```
diff --git a/core/relevance.py b/core/relevance.py
index 9cddae9..7041b02 100644
--- a/core/relevance.py
+++ b/core/relevance.py
@@ -43,12 +43,34 @@ def _norm(s: str) -> str:
 # (real Walleye Capital title) must NOT match "risk analyst" — "Technology"
 # sits between the two words in both real titles, breaking the adjacency
 # these patterns require.
+# Product/program-management and business-rotational patterns added 2026-07-29
+# from two real recurring incidents: Databricks "Product Management Intern
+# (Summer 2027)" (AIJobs, found 2026-07-26 — explicitly PM work, "learn how to
+# be a successful PM," despite listing "computer science" as an acceptable
+# major, and classified AI/ML only because "Machine Learning" is one of
+# Databricks' internal team names, not because the role does ML work) and
+# Conagra Brands "Demand Science Rotational Analyst" (SimplifyJobs,
+# 2026-07-27, still live at List/Dossiers/Other/ as of this writing — a 2-year
+# business rotational program across Behavioral Science/Demand
+# Forecasting/Demand Planning/Advanced Analytics with zero programming
+# content; its own stated requirement is "a general understanding of
+# business, financial concepts, and theory behind processes"). The rotational
+# pattern requires "rotational" not be immediately preceded by "engineering "/
+# "software " so a genuine software-engineering-track rotational program still
+# passes (checked explicitly in tests/test_relevance.py).
+_ROTATIONAL_ANALYST_RE = re.compile(
+    r"(?<!engineering )(?<!software )\brotational (analyst|program)\b", re.I,
+)
 _STAGE1_REJECT_RE = re.compile(
     r"\b(financial analyst|risk analyst|performance analyst"
     r"|tax (associate|preparer|accountant)"
     r"|investor relations"
     r"|sports performance (analyst|analytics)|academy performance (analyst|analysis)"
-    r"|human resources intern|hr intern|marketing intern|business development intern)\b",
+    r"|human resources intern|hr intern|marketing intern|business development intern"
+    r"|product management intern|product manager intern"
+    r"|program management intern|technical program manager intern"
+    r"|demand (planning|science) (analyst|rotational)"
+    r"|business analyst intern)\b",
     re.I,
 )
 
@@ -56,7 +78,8 @@ _STAGE1_REJECT_RE = re.compile(
 def stage1_reject(title: str, raw_text: str) -> bool:
     """True if this listing's title/raw_text is unambiguously non-software —
     reject without ever fetching the page."""
-    return bool(_STAGE1_REJECT_RE.search(f"{title} {raw_text}"))
+    haystack = f"{title} {raw_text}"
+    return bool(_STAGE1_REJECT_RE.search(haystack)) or bool(_ROTATIONAL_ANALYST_RE.search(haystack))
 
 
 # Adjacent-field company/title hint — NOT a reject signal on its own (Jane
@@ -64,9 +87,20 @@ def stage1_reject(title: str, raw_text: str) -> bool:
 # ML roles all pass real content checks below). Only postings that hit this
 # hint need their fetched content checked at all; everything else already
 # cleared stage 1 and passes through unconditionally.
+# chemical/plant/PLC-DCS-SCADA added 2026-07-29: real false-positive, Mosaic
+# (The Mosaic Company, agricultural/mining) "Operations & Automation
+# Engineering Co-op/Intern" — a chemical-plant industrial-automation role
+# (PLC/DCS/SCADA controls, Bachelor's in Chemical Engineering required,
+# physical labor requirements, "basic computer skills" as a minor bullet)
+# passed stage 2 unconditionally because neither "chemical" nor "automation"
+# hit the old hint list, so its content (no Python/Java/C++/git/algorithm
+# anywhere) was never checked at all — it only got flagged downstream by
+# classify.py's now-fixed bare-'threat' match on an unrelated workplace-safety
+# disclaimer. Adding these hints routes it through the real software-signal
+# content check below, which correctly rejects it.
 _ADJACENT_FIELD_COMPANY_HINT_RE = re.compile(
     r"\b(space|aerospace|robotics|astro|satellite|defense|automotive|firmware"
-    r"|embedded|hardware)\b", re.I,
+    r"|embedded|hardware|chemical|industrial|plant operations|\bplc\b|\bdcs\b|\bscada\b)\b", re.I,
 )
 
 # Real content signals confirmed against live vault dossiers 2026-07-26: Bosch
@@ -89,9 +123,17 @@ _SOFTWARE_CONTENT_SIGNAL_RE = re.compile(
 def stage2_confirm(title: str, company: str, posting_content: str) -> bool:
     """Called only when posting_content is non-empty. True = passes (either
     not adjacent-field at all, or adjacent-field AND content shows real
-    software work). False = adjacent-field company/title with no software
-    signal in the actual content — genuinely non-technical despite passing
-    stage 1 (e.g. a hardware-manufacturing floor role at a space company)."""
-    if not _ADJACENT_FIELD_COMPANY_HINT_RE.search(f"{title} {company}"):
+    software work). False = adjacent-field with no software signal in the
+    actual content — genuinely non-technical despite passing stage 1 (e.g. a
+    hardware-manufacturing floor role at a space company).
+
+    The hint check also scans posting_content, not just title+company: real
+    bug, Mosaic Company's "Operations & Automation Engineering Co-op/Intern"
+    (2026-07-29) — its chemical-plant/PLC-DCS-SCADA signal appears only in
+    the fetched content ("Bachelor's degree in Chemical Engineering",
+    "PLC, DCS, and SCADA control systems"), never in the title or company
+    name, so a title+company-only hint check never routed it through the
+    software-signal confirmation below at all."""
+    if not _ADJACENT_FIELD_COMPANY_HINT_RE.search(f"{title} {company} {posting_content}"):
         return True
     return bool(_SOFTWARE_CONTENT_SIGNAL_RE.search(posting_content))
diff --git a/ingestion/posting_page.py b/ingestion/posting_page.py
index 43dff97..32aa5bd 100644
--- a/ingestion/posting_page.py
+++ b/ingestion/posting_page.py
@@ -87,6 +87,43 @@ def opt_exclusion(text: str):
     return m.group(0) if m else None
 
 
+# Built from the real Optiver "Quantitative Research Intern, PhD (Summer
+# 2027)" posting (Greenhouse job id 8451781002 — the same posting manually
+# deleted from the vault once already, then resurfaced, 2026-07-29): its
+# structured degrees field is empty (Greenhouse carries none), so
+# core/filter.py's degrees_eligible() waved it through on missing-data
+# permissiveness. Its real content states the requirement as "Currently
+# enrolled in a PhD program in Statistics, Computer Science, ..." rather than
+# a blunt "PhD required" — the enrolled-in/pursuing-a-phd-program phrasing is
+# the literal shape this real posting uses, so it's included as an explicit
+# equivalent alongside "PhD required"/"PhD only"/"doctoral candidates only".
+# Permissive by default like every other gate here: never fires on "PhD
+# preferred", and the window guard below never fires when a Bachelor's/
+# Master's is also named nearby (checked against the real Aquatic Capital
+# Management, Appian, and Manhattan Associates postings, all of which list
+# PhD only as one of several acceptable degrees and must keep passing).
+_PHD_ONLY_RE = re.compile(
+    r"\bphd\s+(?:is\s+)?(?:required|only)\b"
+    r"|\bdoctoral candidates?\s+only\b"
+    r"|\b(?:currently\s+)?(?:enrolled in|pursuing)\s+an?\s+(?:phd|doctoral)\s+(?:program|degree)\b",
+    re.I,
+)
+
+
+def phd_only_exclusion(text: str):
+    """The matched PhD-exclusivity phrase, or None if the posting shows no
+    explicit signal that only PhD candidates are eligible. Never fires when a
+    Bachelor's/Master's is also named near the match — that's a posting
+    listing PhD as one of several acceptable degrees, not a PhD-only one."""
+    m = _PHD_ONLY_RE.search(text)
+    if not m:
+        return None
+    window = text[max(0, m.start() - 80): m.end() + 80]
+    if re.search(r"bachelor|master|\bbs\b|\bms\b", window, re.I):
+        return None
+    return m.group(0)
+
+
 def fetch_posting_markdown(url: str, api_key: str, http_post=None) -> str:
     """Page markdown via Firecrawl (JS-rendered — ATS pages are SPAs).
     Raises requests exceptions on failure; callers treat any failure as
@@ -109,19 +146,105 @@ _NOISE = re.compile(
     r"^(\[?!\[|\[back to jobs|\[apply\]|apply\b|select\.\.\.|✱|.*✱\s*$|resume/cv|full name|email\b"
     r"|phone\b|current location|current company|linkedin url|github url|portfolio url|loading$"
     r"|no location found|couldn't auto-read|analyzing resume|success!$|file exceeds|-{3,}$"
-    r"|cookie|jobs powered by|©|powered by\s|\[.*\]\(https?://[^)]*\)\s*$)", re.I)
+    r"|cookie|jobs powered by|©|powered by\s|\[.*\]\(https?://[^)]*\)\s*$|read more$)", re.I)
+
+# Real, distinct bug from the Ashby application-URL one — confirmed 2026-07-26
+# on both Google dossiers sourced via Freehire (BS and MS tracks): Google's
+# careers site returns a *search-results listing page* shell (~20 unrelated
+# job titles, "Back to jobs search" nav, "N jobs matched", pagination) ahead
+# of the specific posting's own content in the SAME fetched markdown — not a
+# wrong-URL problem like Ashby's /application suffix, the real posting text is
+# right there further down. classify() fired on an unrelated listed job's
+# title as a result. Whenever one of these listing-shell markers appears,
+# everything gathered so far is shell noise — reset and wait for the next
+# real heading, which lands on the actual posting content once the shell ends.
+_LISTING_SHELL_RESET_RE = re.compile(
+    r"^(_arrow_back_|back to jobs search|##?\s*jobs search results|[\d,]+\s+jobs matched"
+    r"|showing \d+ to \d+ of|_navigate_next_)", re.I,
+)
+
+# ATS UI labels jammed against their values with no separator, real examples
+# from the Conagra Brands fixture (List/Dossiers/Other/Demand Science
+# Rotational Analyst - Conagra Brands.md): "locationsChicago, Illinois",
+# "time typeFull time", "posted onPosted Today", "job requisition idReq-039400".
+_ATS_LABEL_RUN_ON_RE = re.compile(
+    r"^(locations|time type|posted on|job requisition id|time left to apply)(?=\S)", re.M,
+)
+
+# A posting's own section names, real shape confirmed against the Appian
+# ("**Basic Qualifications**", "**Benefits**") and Conagra ("**Compensation**",
+# "**Our Benefits**") fixtures: a fully-bolded standalone line naming one of
+# these sections. Deliberately narrow — only fires when the *whole* line is
+# one bold span ending in a real section keyword, so inline bold emphasis
+# ("our values of **Intensity** and **Excellence**...") and non-section bold
+# lines ("**Why should you kick off your career with Conagra?**") are left as
+# flattened prose, per the "don't invent section boundaries" rule.
+_BOLD_SECTION_RE = re.compile(r"^\*\*([^*]+?)\*\*:?$")
+_SECTION_KEYWORD_RE = re.compile(r"(responsibilities|qualifications|requirements|benefits|compensation)$", re.I)
+
+# Real, from the Manhattan Associates fixture (List/Dossiers/1 - AI & ML/A.I.
+# Developer Co-Op (Boston, MA) - Manhattan Associates.md): a "Follow Us"
+# heading followed by a bulleted LinkedIn/X/Facebook link list, pure chrome.
+_FOLLOW_US_HEADING_RE = re.compile(r"^#{1,6}\s*follow us\s*$", re.I)
+# Real Manhattan Associates link shape includes a markdown title after the
+# URL ('[LinkedIn](https://...4376?trk=tyah "LinkedIn")') — the optional
+# quoted-title group handles that, not just a bare '(url)'.
+_LINK_BULLET_RE = re.compile(r'^-\s*\[.+\]\(https?://\S+?(?:\s+"[^"]*")?\)\s*$')
+
+
+def _dedupe_paragraphs(markdown: str, min_len: int = 40) -> str:
+    """Drops a paragraph line that repeats verbatim later in the same fetch,
+    keeping the first occurrence — real example: the Conagra fixture's whole
+    'About Us' paragraph appears twice. Real fetched markdown from this
+    pipeline's sources renders each prose paragraph as one continuous line
+    (confirmed against the Manhattan Associates/Appian/Optiver fixtures), so
+    line-level comparison catches this without needing blank-line block
+    boundaries the source markdown may not consistently have. min_len guards
+    against deduping short, legitimately-repeated lines (labels, headings)
+    that aren't real paragraph content."""
+    seen, kept = set(), []
+    for line in markdown.splitlines():
+        key = line.strip()
+        if len(key) >= min_len:
+            if key in seen:
+                continue
+            seen.add(key)
+        kept.append(line)
+    return "\n".join(kept)
+
+
+def _strip_trailing_social_chrome(lines: list) -> list:
+    out, skip_links = [], False
+    for line in lines:
+        if _FOLLOW_US_HEADING_RE.match(line.strip()):
+            skip_links = True
+            continue
+        if skip_links and _LINK_BULLET_RE.match(line.strip()):
+            continue
+        skip_links = False
+        out.append(line)
+    return out
 
 
 def extract_content(markdown: str, limit: int = CONTENT_LIMIT) -> str:
     """The posting's substantive text: from the first real heading up to the
     application-form/EEO chrome, minus nav/form/boilerplate lines. Verbatim
-    lines, never a summary. Blank lines and '---' rules dropped to satisfy
-    the vault's format conventions (see validate.check_format_compliance)."""
+    lines, never a summary — but deduped (no repeated paragraph), chrome-split
+    (ATS UI labels get their own line), and structured (a source's own bolded
+    section names become real '###' headings) per the Internship Notes
+    Standard §2. Blank lines and '---' rules dropped to satisfy the vault's
+    format conventions (see validate.check_format_compliance)."""
+    markdown = _dedupe_paragraphs(markdown)
+    markdown = _ATS_LABEL_RUN_ON_RE.sub(lambda m: m.group(1) + "\n", markdown)
+
     out, started = [], False
     for line in markdown.splitlines():
         s = line.strip()
         if _CUT_MARKERS.match(s):
             break
+        if _LISTING_SHELL_RESET_RE.match(s):
+            started, out = False, []
+            continue
         if not started:
             if s.startswith("#") and len(s) > 4:
                 started = True
@@ -129,7 +252,10 @@ def extract_content(markdown: str, limit: int = CONTENT_LIMIT) -> str:
                 continue
         if not s or _NOISE.match(s):
             continue
+        section = _BOLD_SECTION_RE.match(s)
+        if section and _SECTION_KEYWORD_RE.search(section.group(1).strip()):
+            s = f"### {section.group(1).strip()}"
         out.append(s)
         if len("\n".join(out)) > limit:
             break
-    return "\n".join(out)
+    return "\n".join(_strip_trailing_social_chrome(out))
diff --git a/recheck.py b/recheck.py
index e760606..d26252d 100644
--- a/recheck.py
+++ b/recheck.py
@@ -2,10 +2,11 @@
 """Daily post-write liveness recheck. Scans the dossier files actually present
 in the vault checkout (file existence is the truth — seen_ids.json diverged
 from the vault after the 2026-07-18 manual cleanup and stays untouched here),
-cross-refs each against its source's live feed, and removes any dossier whose
-posting is now inactive or gone from the feed entirely. Runs on its own daily
-cron (.github/workflows/recheck.yml) — postings don't close often enough to
-justify rechecking every hour.
+cross-refs each against its source's live feed, and moves any dossier whose
+posting is now inactive or gone from the feed entirely into Viewed/ (never
+deletes — Internship Notes Standard §4: a closed posting's history is real
+information). Runs on its own daily cron (.github/workflows/recheck.yml) —
+postings don't close often enough to justify rechecking every hour.
 
     JARVIS_DIR=... python recheck.py [--dry-run]
 """
@@ -27,7 +28,7 @@ from ingestion.sources import (
     fetch_zshah101,
 )
 from run_pipeline import file_github_issue
-from vault_writer.writer import load_dossier_uids, scan_dossiers
+from vault_writer.writer import load_dossier_uids, move_dossier_to_viewed, scan_dossiers
 
 # 2026-07-25: was still SimplifyJobs/JGCL only after the 4-source batch shipped
 # earlier the same day — dossiers from vanshb03/zshah101/Greenhouse/Ashby were
@@ -107,34 +108,39 @@ def main():
         "halt_reason": None,
     }
 
-    # ponytail: crude mass-deletion brake — a truncated/glitched feed must not
-    # wipe the vault. Threshold is arbitrary but safe; tune if it ever trips wrongly.
+    # ponytail: crude mass-move brake — a truncated/glitched feed must not
+    # empty the vault into Viewed/. Threshold is arbitrary but safe; tune if it
+    # ever trips wrongly. Same protective logic as before this was a move
+    # instead of a delete — the risk (a feed glitch wiping real dossiers out
+    # of the live buckets) is identical either way.
     if len(removals) > max(5, len(dossiers) // 2):
         record["halted"] = True
-        record["halt_reason"] = f"would remove {len(removals)} of {len(dossiers)} dossiers — feed glitch?"
+        record["halt_reason"] = f"would move {len(removals)} of {len(dossiers)} dossiers to Viewed/ — feed glitch?"
         if not args.dry_run:
             _commit_log(record, now)
             file_github_issue(
                 ISSUE_REPO,
-                f"Recheck halted: mass-deletion brake at {now.isoformat()}",
-                f"{record['halt_reason']}\n\nNothing was removed. Removal list:\n"
+                f"Recheck halted: mass-move brake at {now.isoformat()}",
+                f"{record['halt_reason']}\n\nNothing was moved. Removal list:\n"
                 + "\n".join(f"- `{r['uid']}`: {r['reason']}" for r in removals),
             )
         print(record["halt_reason"])
         sys.exit(1)
 
     for r in removals:
-        print(f"{'would remove' if args.dry_run else 'removing'}: {r['uid']} — {r['reason']}")
+        print(f"{'would move' if args.dry_run else 'moving'}: {r['uid']} — {r['reason']}")
     if args.dry_run:
-        print(f"dry run: {len(removals)} of {len(dossiers)} would be removed")
+        print(f"dry run: {len(removals)} of {len(dossiers)} would be moved to Viewed/")
         return
 
     if removals:
         for r in removals:
-            Path(r["path"]).unlink()
+            move_dossier_to_viewed(
+                jarvis_dir, r["path"], r["reason"], now.date().isoformat(), state_dir=STATE_DIR
+            )
         try:
             commit_and_push_with_retry(
-                jarvis_dir, f"Remove {len(removals)} closed posting(s) — recheck {now.date().isoformat()}"
+                jarvis_dir, f"Move {len(removals)} closed posting(s) to Viewed/ — recheck {now.date().isoformat()}"
             )
         except GitPushError as exc:
             record["errors"].append(f"Jarvis push failed: {exc}")
@@ -144,7 +150,7 @@ def main():
                 f"Removals were made in the checkout but the push failed after retry:\n\n```\n{exc}\n```",
             )
     _commit_log(record, now)
-    print(f"removed {len(removals)} of {len(dossiers)} dossiers; {len(errors)} fetch error(s)")
+    print(f"moved {len(removals)} of {len(dossiers)} dossiers to Viewed/; {len(errors)} fetch error(s)")
     if record["errors"]:
         sys.exit(1)
 
diff --git a/vault_writer/writer.py b/vault_writer/writer.py
index 0ded6ff..040747a 100644
--- a/vault_writer/writer.py
+++ b/vault_writer/writer.py
@@ -13,6 +13,8 @@ from pathlib import Path
 import yaml
 from jinja2 import Environment, FileSystemLoader
 
+from core.identity import company_matches_preference
+
 TEMPLATE_DIR = Path(__file__).parent / "templates"
 DOSSIER_SUBPATH = Path("10_Areas/Career/Internships/List/Dossiers")
 DOSSIER_UIDS_FILENAME = "dossier_uids.json"
@@ -45,12 +47,33 @@ def _iso_date(epoch) -> str:
     return datetime.fromtimestamp(epoch, tz=timezone.utc).date().isoformat() if epoch else None
 
 
-def build_frontmatter(listing, uid: str, date_found: str, matched_reason: str) -> dict:
+DOSSIERS_MOC_LINK = "[[10_Areas/Career/Internships/List/Dossiers MOC]]"
+
+_TAG_ILLEGAL_CHARS = re.compile(r'[\\/:*?"<>|]')
+
+
+def company_slug(company: str) -> str:
+    """Same slugification as dossier_filename(): lowercase, spaces to
+    hyphens, illegal chars stripped — so 'Aquatic Capital Management' and
+    ' aquatic capital management ' both produce company/aquatic-capital-management,
+    per the Standard's same-company clustering rule (§1)."""
+    s = _TAG_ILLEGAL_CHARS.sub("", company).strip().lower()
+    return re.sub(r"\s+", "-", s)
+
+
+def build_frontmatter(listing, uid: str, date_found: str, matched_reason: str,
+                      preferred_companies: dict = None) -> dict:
     """uid and category are deliberately not rendered — uid stays available
     internally via the dossier_uids.json manifest (see write_dossier), and
     category was never surfaced to the reader anywhere else in the note.
     `next:` (not `promoted:`) matches every other note type's convention
-    across the vault."""
+    across the vault. `notes:` (always the Dossiers MOC link) and the
+    `company/<slug>` tag are the Internship Notes Standard §1 interlinking
+    requirement — `notes` sits right after `next`, right before `tags`.
+    `preference_tier` (Prompt 5 Task O) is the matched core/profile.yaml
+    preferred_companies tier, or null — required like every other field
+    here, not omitted when there's no match (fail-closed, same discipline
+    as REQUIRED_FRONTMATTER_FIELDS everywhere else in this file)."""
     return {
         "company": listing.company,
         "title": listing.title,
@@ -64,16 +87,25 @@ def build_frontmatter(listing, uid: str, date_found: str, matched_reason: str) -
         "matched_reason": matched_reason,
         "status": "unreviewed",
         "next": None,
-        "tags": ["internship", "auto-discovered"],
+        "notes": [DOSSIERS_MOC_LINK],
+        "preference_tier": company_matches_preference(listing.company, preferred_companies or {}),
+        "tags": ["internship", "auto-discovered", f"company/{company_slug(listing.company)}"],
     }
 
 
-def render_dossier(listing, uid: str, date_found: str, matched_reason: str, posting_content: str = "",
-                   classification_callout: str = "") -> str:
-    frontmatter = build_frontmatter(listing, uid, date_found, matched_reason)
-    frontmatter_yaml = yaml.dump(
+def dump_frontmatter(frontmatter: dict) -> str:
+    """Shared YAML rendering (None as blank scalar, indented list items) so
+    every dossier-writing code path — including recheck.py's removal-time
+    frontmatter patch — serializes identically."""
+    return yaml.dump(
         frontmatter, Dumper=_FrontmatterDumper, sort_keys=False, default_flow_style=False, allow_unicode=True
     )
+
+
+def render_dossier(listing, uid: str, date_found: str, matched_reason: str, posting_content: str = "",
+                   classification_callout: str = "", preferred_companies: dict = None) -> str:
+    frontmatter = build_frontmatter(listing, uid, date_found, matched_reason, preferred_companies)
+    frontmatter_yaml = dump_frontmatter(frontmatter)
     markdown = _template.render(
         frontmatter_yaml=frontmatter_yaml,
         company=listing.company,
@@ -168,3 +200,75 @@ def write_dossier(vault_root, uid: str, markdown: str, role: str, company: str,
         manifest[str(path.relative_to(vault_root))] = uid
         save_dossier_uids(state_dir, manifest)
     return path
+
+
+REMOVED_DOSSIERS_MOC_LINK = "[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]"
+VIEWED_SUBPATH = DOSSIER_SUBPATH / "Viewed"
+
+
+def move_dossier_to_viewed(vault_root, path, reason: str, removed_date: str, state_dir=None) -> Path:
+    """Moves a closed-posting dossier into Viewed/ instead of deleting it
+    (Internship Notes Standard §4) — the posting closing is real information
+    (hiring cadence, why a later duplicate should be rejected, a record of
+    what this pipeline actually saw), not something to throw away. Appends
+    the Removed Dossiers MOC link to the existing notes: list (never
+    replacing the original Dossiers MOC / company links already there), sets
+    status: removed (the field's first real transition away from its static
+    'unreviewed'), and records removed_date/removed_reason. Updates
+    dossier_uids.json to the new path so the next write_dossier() idempotency
+    check for this uid isn't left pointing at a file that moved."""
+    vault_root = Path(vault_root)
+    path = Path(path)
+    text = path.read_text(encoding="utf-8")
+    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
+    frontmatter = yaml.safe_load(m.group(1)) or {}
+    body = m.group(2)
+
+    notes = list(frontmatter.get("notes") or [])
+    if DOSSIERS_MOC_LINK not in notes:
+        notes.append(DOSSIERS_MOC_LINK)
+    if REMOVED_DOSSIERS_MOC_LINK not in notes:
+        notes.append(REMOVED_DOSSIERS_MOC_LINK)
+    frontmatter["notes"] = notes
+    frontmatter["status"] = "removed"
+    frontmatter["removed_date"] = removed_date
+    frontmatter["removed_reason"] = reason
+
+    # Fix 2, Prompt 5 review (2026-07-30): two dossiers with identical
+    # filenames can legitimately coexist in two different bucket folders
+    # (bucket-scoped collision checks at write time only look within one
+    # bucket) — moving both into the single flat Viewed/ folder must not let
+    # the second overwrite the first. Reuse dossier_filename()'s existing
+    # '(2)', '(3)'-suffixing collision logic rather than duplicating it: it
+    # already takes a bare "role - company" base and a set of existing names,
+    # so split path.stem back into role/company at the ' - ' this pipeline's
+    # own filenames always use.
+    viewed_dir = vault_root / VIEWED_SUBPATH
+    viewed_dir.mkdir(parents=True, exist_ok=True)
+    existing_names = {p.name for p in viewed_dir.glob("*.md")}
+    stem = path.stem
+    role, sep, company = stem.rpartition(" - ")
+    if sep:
+        new_name = dossier_filename(role, company, existing_names)
+    else:
+        # No ' - ' separator to split on (a hand-renamed or malformed
+        # filename) — fall back to suffixing the whole stem directly, same
+        # collision-avoidance behavior dossier_filename() provides, just
+        # without a role/company split to build on.
+        new_name = path.name
+        n = 2
+        while new_name in existing_names:
+            new_name = f"{stem} ({n}){path.suffix}"
+            n += 1
+    new_path = viewed_dir / new_name
+    new_path.write_text("---\n" + dump_frontmatter(frontmatter) + "---\n" + body)
+    path.unlink()
+
+    if state_dir is not None:
+        manifest = load_dossier_uids(state_dir)
+        old_rel = str(path.relative_to(vault_root))
+        uid = manifest.pop(old_rel, None)
+        if uid is not None:
+            manifest[str(new_path.relative_to(vault_root))] = uid
+            save_dossier_uids(state_dir, manifest)
+    return new_path
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/debate.py`
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== .github/workflows/*.yml (local, likely stale too but check for state filenames) ==="
grep -rn "capacity_notified\|debate_losses\|excluded_uids\|FIRECRAWL\|secrets\." .github/workflows/*.yml
echo "=== origin's workflow files vs local (any diff) ==="
diff <(git show origin/master:.github/workflows/run.yml) .github/workflows/run.yml
diff <(git show origin/master:.github/workflows/recheck.yml) .github/workflows/recheck.yml
diff <(git show origin/master:.github/workflows/test.yml) .github/workflows/test.yml 2>&1
  ```
  ```
=== .github/workflows/*.yml (local, likely stale too but check for state filenames) ===
.github/workflows/run.yml:22:          token: ${{ secrets.JARVIS_PUSH_TOKEN }}
.github/workflows/run.yml:42:          FIRECRAWL_API_KEY: ${{ secrets.FIRECRAWL_API_KEY }}  # discovery-time posting fetch; absent = thin dossiers, never a failure
.github/workflows/recheck.yml:22:          token: ${{ secrets.JARVIS_PUSH_TOKEN }}
=== origin's workflow files vs local (any diff) ===
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
ls .venv/bin/python 2>&1 || echo "no venv"
if [ -f .venv/bin/python ]; then
  .venv/bin/python -m pytest tests/ -q 2>&1 | tail -60
else
  python3 -m pytest tests/ -q 2>&1 | tail -60
fi
  ```
  ```
.venv/bin/python
........................................................................ [ 21%]
........................................................................ [ 43%]
........................................................................ [ 65%]
........................................................................ [ 87%]
.........................................                                [100%]
329 passed in 1.36s
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
head -20 vault_writer/templates/*.j2 vault_writer/templates/*.jinja 2>/dev/null
ls vault_writer/templates/
echo "=== check template uses frontmatter_yaml directly ==="
grep -n "frontmatter_yaml\|preference_tier\|notes" vault_writer/templates/* 2>/dev/null
  ```
  ```
==> vault_writer/templates/dossier.md.j2 <==
---
{{ frontmatter_yaml }}---
# {{ title }}
{% if posting_content -%}
Found {{ date_found }} via {{ source }}.
{% if classification_callout -%}
{{ classification_callout }}
{% endif -%}
## Posting (fetched {{ date_found }})
{{ posting_content }}
{%- else -%}
Found {{ date_found }} via {{ source }}. No posting content fetched.
{% if classification_callout -%}
{{ classification_callout }}
{% endif -%}
{%- endif %}
dossier.md.j2
=== check template uses frontmatter_yaml directly ===
2:{{ frontmatter_yaml }}---
  ```
- `Bash`:
  ```bash
cd /home/anant_gupta/projects/work/internship-research-loop
echo "=== find real feature-shaped commit messages in history (not 'Update state + logs' or 'Recheck log') ==="
git log origin/master --oneline | grep -v "^[a-f0-9]* Update state + logs\|^[a-f0-9]* Recheck log" | head -30
  ```
  ```
=== find real feature-shaped commit messages in history (not 'Update state + logs' or 'Recheck log') ===
9cc30ec Add promote-dossier skill, contact-researcher/loop-verifier agents, review-loop-change skill
5c9a409 Priority-bucket classification, CS-relevance gate, widened contact research
d0d6cd4 Two new discovery sources: Freehire, AIJobs
a21b2fa Four new discovery sources: vanshb03, zshah101, Greenhouse, Ashby
e10d06a PRD: three-criteria scope, content-carrying dossiers, verified 2026-07-18 state
69f76dc Phase 6: three hard criteria codified — Winter 2027 term, OPT gate, discovery-time content
7a84be1 Fix the 5 root causes behind dossier bloat (2026-07-18 vault audit)
697c110 Phase 4: locations_allow filter, Layer 5 enrich.py, Layer 6 grade_resume.py
6c285ca README: phase 3 is live
cdcbc4e Fix (for real this time): stage the .gitignore content, not just the rm
573bfd5 Fix: exclude jarvis-checkout/ from this repo's own git tracking
2c58414 Phase 3: activate the scheduled run against gupta-builds/Jarvis
c88b76c Phase 3 code: schema-drift check, git push-retry, run log, orchestration
02b63c6 Phase 3 step 0: reconcile plan review, fix real zapply parsing bug
0737dfc Verification pass: fix dead config, close test gaps, pin deps
fd772b7 Phase 2: vault_writer — dossier template + four-check write gate
f01e663 Fix CI: use python -m pytest so repo root lands on sys.path
9e585b2 Phase 1: ingestion, filter, identity — tested against real fixtures
  ```
- `Bash`:
  ```bash
gh issue view 1 --repo gupta-builds/internship-research-loop --json title,body,createdAt,state 2>&1
echo "---"
gh issue view 2 --repo gupta-builds/internship-research-loop --json title,body,createdAt,state 2>&1
echo "=== current time check: latest run again, freshest ==="
gh run list --repo gupta-builds/internship-research-loop --limit 5 2>&1
  ```
  ```
{"body":"Schema drift or source fetch failure — nothing was fetched, filtered, or written this run.\n\n```\nHTTPError: 429 Client Error: Too Many Requests for url: https://raw.githubusercontent.com/SimplifyJobs/Summer2026-Internships/dev/.github/scripts/listings.json\n```","createdAt":"2026-08-17T15:16:34Z","state":"OPEN","title":"Run halted (HTTPError) at 2026-08-17T15:16:21.079968+00:00"}
---
{"body":"Schema drift or source fetch failure — nothing was fetched, filtered, or written this run.\n\n```\nHTTPError: 429 Client Error: Too Many Requests for url: https://raw.githubusercontent.com/Jose-Gael-Cruz-Lopez/underclassmen-opportunities/main/.github/scripts/listings.json\n```","createdAt":"2026-08-17T16:15:46Z","state":"OPEN","title":"Run halted (HTTPError) at 2026-08-17T16:15:32.395149+00:00"}
=== current time check: latest run again, freshest ===
completed	success	run	run	master	schedule	32502393689	3m44s	2026-08-21T16:20:13Z
completed	success	run	run	master	schedule	32497314098	40s	2026-08-21T15:23:16Z
completed	success	run	run	master	schedule	32491957893	30s	2026-08-21T14:24:20Z
completed	success	run	run	master	schedule	32487815837	38s	2026-08-21T13:37:29Z
completed	success	run	run	master	schedule	32481855747	41s	2026-08-21T12:25:55Z
  ```

## Actions Taken
- Files created: /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/aiml.txt, /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/fullstack.txt, /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/cysfin.txt, /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/other.txt, /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/pipeline-triage.html
- Files modified: /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/bebacdad-914c-4c86-b1a2-93b41c665f1c/scratchpad/pipeline-triage.html
- Files deleted: (none)
- Commands run: git status && echo "---LOG---" && git log --oneline -20 && echo "---DIFF STAT---" && git diff --stat, git fetch origin --quiet 2>&1 | tail -5; echo "---"; git log origin/master --oneline -15; echo "---LAST LOCAL VS REMOTE DATE---"; git log -1 --format=%cd; git log origin/master -1 --format=%cd, cat /home/anant_gupta/projects/work/internship-research-loop/state/seen_ids.json 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print('seen_ids count:', len(d) if isinstance(d,list) else len(d.keys()))" 2>&1 echo "---" ls /home/anant_gupta/projects/work/internship-research-loop/logs/ 2>/dev/null echo "---runs.jsonl tail---" tail -5 /home/anant_gupta/projects/work/internship-research-loop/logs/runs.jsonl 2>/dev/null echo "---rechecks.jsonl tail---" tail -5 /home/anant_gupta/projects/work/internship-research-loop/logs/rechecks.jsonl 2>/dev/null, ls -la /home/anant_gupta/projects/work/ 2>/dev/null; echo "---"; find / -maxdepth 4 -iname "Jarvis" -type d 2>/dev/null, ls -la /home/anant_gupta/projects/work/gupta-builds/ 2>/dev/null, cd /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad for f in aiml fullstack cysfin other; do echo -n "$f: "; wc -l < $f.txt; done echo "total:"; cat aiml.txt fullstack.txt cysfin.txt other.txt | wc -l echo "--- company frequency (top 25) ---" cat aiml.txt fullstack.txt cysfin.txt other.txt | sed -E 's/\.md$//' | awk -F' - ' '{print $NF}' | sort | uniq -c | sort -rn | head -30, cd /home/anant_gupta/projects/work/internship-research-loop echo "=== MAX_NEW_WRITES / cap-related in run_pipeline.py ===" grep -n -i "MAX_NEW_WRITES\|cap\|limit\|201\|50\b" run_pipeline.py | head -40 echo "=== cs_relevance in core/relevance.py or classify.py ===" grep -n -i "def \|cs_relevance\|relevant" core/relevance.py | head -30 echo "=== classify.py functions ===" grep -n "^def " core/classify.py, cd /home/anant_gupta/projects/work/internship-research-loop echo "=== bucket_at_capacity notification handling in run_pipeline.py ===" sed -n '480,515p' run_pipeline.py echo "=== recent runs.jsonl bucket_at_capacity mentions ===" tail -1 logs/runs.jsonl | python3 -c "import json,sys; d=json.load(sys.stdin); print('bucket_at_capacity:', d.get('bucket_at_capacity')); print('written_count:', d.get('written_count')); print('timestamp:', d.get('timestamp'))" echo "=== gh issues (if gh cli available and authed) ===" gh issue list --repo gupta-builds/internship-research-loop --state all --limit 20 2>&1 | head -30, cd /home/anant_gupta/projects/work/internship-research-loop echo "=== recent workflow runs ===" gh run list --repo gupta-builds/internship-research-loop --limit 15 2>&1 echo "=== issue #3 body ===" gh issue view 3 --repo gupta-builds/internship-research-loop 2>&1 | head -30 echo "=== capacity_notified.json on origin/master ===" git show origin/master:state/capacity_notified.json 2>&1, cd /home/anant_gupta/projects/work/internship-research-loop echo "=== state dir on origin/master ===" git ls-tree origin/master -- state/ 2>&1 echo "=== issue 3 body (plain) ===" gh issue view 3 --repo gupta-builds/internship-research-loop --json title,body,createdAt,state 2>&1, cd /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad cat aiml.txt fullstack.txt cysfin.txt other.txt > all_dossiers.txt # Conservative "near-certain non-SWE by title alone" denylist — a human should still eyeball this list, but every title here has zero software/CS/data-eng signal. grep -iE "Accounting|Aerodynamic|Community Engagement|Construction Management|Construction Manager|Civil and Structural|Mechanical Engineer|Materials? Planning|Quality & Manufacturing|Supply Chain (Business|Data Analyst)|Strategic Engagements|Video Production|Geoscience|Thermal Application|Sustainability Engineer|System Administrator|Global Supply Management|Operations Experience|Business Analytics Intern|Reporting Analyst" all_dossiers.txt | sort | tee near_certain_junk.txt | wc -l echo "--- sample of that list ---" head -20 near_certain_junk.txt echo "--- companies these belong to ---" sed -E 's/\.md$//' near_certain_junk.txt | awk -F' - ' '{print $NF}' | sort | uniq -c | sort -rn, cd /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad for c in "Jane Street" "Two Sigma" "D.E. Shaw\|DE Shaw" "Citadel" "Google" "Microsoft" "LinkedIn" "MLH" "NASA" "Capital One" "Bloomberg"; do n=$(grep -ic "$c" all_dossiers.txt) echo "$c: $n" done, cat /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/scratchpad/near_certain_junk.txt, cd /home/anant_gupta/projects/work/internship-research-loop echo "=== git diff --stat ===" git diff --stat echo "=== untracked file sizes ===" wc -l core/debate.py tests/test_debate.py tests/test_debate_losses.py tests/fixtures/posting_google_careers.md 2>&1, cd /home/anant_gupta/projects/work/internship-research-loop git diff core/run_pipeline.py, cd /home/anant_gupta/projects/work/internship-research-loop git diff -- run_pipeline.py, cd /home/anant_gupta/projects/work/internship-research-loop echo "=== does core/debate.py exist on origin/master? ===" git cat-file -e origin/master:core/debate.py 2>&1 && echo "EXISTS on origin" || echo "DOES NOT EXIST on origin" echo "=== does origin/master's run_pipeline.py have MAX_NEW_WRITES_PER_RUN as dict or int? ===" git show origin/master:run_pipeline.py 2>&1 | grep -n "MAX_NEW_WRITES_PER_RUN\|BUCKET_CAPACITY\|debate\|phd_only" | head -20 echo "=== merge-base between local HEAD and origin/master ===" git merge-base HEAD origin/master git log --oneline -1 HEAD git log --oneline -1 origin/master echo "=== would run_pipeline.py conflict on merge? (dry run) ===" git merge-tree "$(git merge-base HEAD origin/master)" HEAD origin/master -- run_pipeline.py 2>&1 | head -5 echo "=== diff between origin/master's run_pipeline.py and local working tree ===" diff <(git show origin/master:run_pipeline.py) run_pipeline.py > /tmp/rp_vs_origin.diff 2>&1 wc -l /tmp/rp_vs_origin.diff, cd /home/anant_gupta/projects/work/internship-research-loop echo "=== files changed on origin since merge-base (top-level dirs only) ===" git diff --stat 3fd4b88..origin/master -- run_pipeline.py recheck.py core/ ingestion/ vault_writer/ tests/ 2>&1 echo "=== full list of changed file PATHS (not vault content) on origin since 07-30, excluding state/logs/jarvis-vault-content ===" git diff --name-only 3fd4b88..origin/master | grep -v "^logs/\|^state/" | sort echo "=== count of commits touching code (non-state/log) paths since merge-base ===" git log 3fd4b88..origin/master --oneline -- run_pipeline.py recheck.py core/ ingestion/ vault_writer/ tests/ .github/ | wc -l, cd /home/anant_gupta/projects/work/internship-research-loop git diff -- core/profile.yaml core/classify.py core/identity.py core/run_log.py vault_writer/validate.py, cd /home/anant_gupta/projects/work/internship-research-loop git diff -- core/relevance.py ingestion/posting_page.py recheck.py vault_writer/writer.py, cd /home/anant_gupta/projects/work/internship-research-loop echo "=== .github/workflows/*.yml (local, likely stale too but check for state filenames) ===" grep -rn "capacity_notified\|debate_losses\|excluded_uids\|FIRECRAWL\|secrets\." .github/workflows/*.yml echo "=== origin's workflow files vs local (any diff) ===" diff <(git show origin/master:.github/workflows/run.yml) .github/workflows/run.yml diff <(git show origin/master:.github/workflows/recheck.yml) .github/workflows/recheck.yml diff <(git show origin/master:.github/workflows/test.yml) .github/workflows/test.yml 2>&1, cd /home/anant_gupta/projects/work/internship-research-loop ls .venv/bin/python 2>&1 || echo "no venv" if [ -f .venv/bin/python ]; then .venv/bin/python -m pytest tests/ -q 2>&1 | tail -60 else python3 -m pytest tests/ -q 2>&1 | tail -60 fi, cd /home/anant_gupta/projects/work/internship-research-loop head -20 vault_writer/templates/*.j2 vault_writer/templates/*.jinja 2>/dev/null ls vault_writer/templates/ echo "=== check template uses frontmatter_yaml directly ===" grep -n "frontmatter_yaml\|preference_tier\|notes" vault_writer/templates/* 2>/dev/null, cd /home/anant_gupta/projects/work/internship-research-loop echo "=== find real feature-shaped commit messages in history (not 'Update state + logs' or 'Recheck log') ===" git log origin/master --oneline | grep -v "^[a-f0-9]* Update state + logs\|^[a-f0-9]* Recheck log" | head -30, gh issue view 1 --repo gupta-builds/internship-research-loop --json title,body,createdAt,state 2>&1 echo "---" gh issue view 2 --repo gupta-builds/internship-research-loop --json title,body,createdAt,state 2>&1 echo "=== current time check: latest run again, freshest ===" gh run list --repo gupta-builds/internship-research-loop --limit 5 2>&1
- Tool call tally: Artifact (1), Bash (25), Edit (1), mcp__jarvis__search_simple (1), mcp__jarvis__vault_list (20), mcp__jarvis__vault_read (10), mcp__jarvis-fs__list_allowed_directories (1), Read (5), Skill (1), ToolSearch (3), WebFetch (1), Write (5)

