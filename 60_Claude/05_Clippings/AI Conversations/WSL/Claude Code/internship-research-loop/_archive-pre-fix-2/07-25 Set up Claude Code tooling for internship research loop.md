---
type: input
input_kind: ai-conversation
source_app: claude-code
source_os: wsl
title: "Set up Claude Code tooling for internship research loop"
started_at: 2026-07-25T20:51:15
ended_at: 2026-07-30T08:42:18
duration_minutes: 6471
exported_at: 2026-07-30T15:28:59.6972445+04:00
project: internship-research-loop
cwd: '/home/anant_gupta/projects/work/internship-research-loop'
session_id: f80cd4cf-b82c-4b53-a7b9-0bb8c67543f0
status: raw
turn_count: 14
tools_used:
  Agent: 2
  AskUserQuestion: 2
  Bash: 43
  Edit: 16
  mcp__jarvis__vault_list: 11
  mcp__jarvis__vault_read: 10
  mcp__jarvis__vault_write: 5
  mcp__jarvis-fs__list_allowed_directories: 1
  Read: 22
  Skill: 1
  TaskCreate: 6
  TaskUpdate: 12
  ToolSearch: 4
  Write: 8
tokens:
  input: 624
  output: 311319
  cache_creation: 2500870
  cache_read: 54133146
  total: 56945959
cost_usd: 23.944547
model:
  - claude-sonnet-5
files_touched:
  - "/home/anant_gupta/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/memory/phase4-state-and-gates.md"
  - "/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/filter.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/recheck.py"
  - "/home/anant_gupta/projects/work/internship-research-loop/core/git_ops.py"
  - "/home/anant_gupta/projects/hub/portfolio/.claude/agents/security-reviewer.md"
  - "/home/anant_gupta/.claude/agents/obsidian-researcher.md"
  - "/home/anant_gupta/projects/work/internship-research-loop/.claude/agents/contact-researcher.md"
  - "/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/reference/note-templates.md"
  - "/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/SKILL.md"
  - "/home/anant_gupta/projects/work/internship-research-loop/.claude/agents/loop-verifier.md"
  - "/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/review-loop-change/SKILL.md"
  - "/home/anant_gupta/projects/hub/tradingview/.claude/settings.json"
  - "/home/anant_gupta/projects/work/internship-research-loop/.claude/settings.json"
  - "/home/anant_gupta/projects/work/internship-research-loop/CLAUDE.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Internship Notes Standard.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers MOC.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Other/Demand Science Rotational Analyst - Conagra Brands.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/A.I. Developer Co-Op (Boston, MA) - Manhattan Associates.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/System - Build Log.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Research Loop - Improvement Plan.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md"
  - "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian.md"
tags:
  - input
  - ai-conversation
  - claude-code
  - wsl
---

# Set up Claude Code tooling for internship research loop

## You

You are setting up gupta-builds/internship-research-loop's own .claude/ tooling — skills, agents, and settings scoped to this repo, separate from and not to be confused with the Jarvis vault's own .claude/ setup (a different, unrelated piece of work). This prompt assumes Prompt 1 and Prompt 2 (persona config, priority classification, dossier template fixes, contact-research widening) have already run — if core/priority.py, the four vault subfolders, or the widened enrich.py don't exist yet, stop and say so rather than building on top of an assumption.

## Real architectural constraint, resolve explicitly, don't silently assume
The promotion skill below (Task A) needs to read a dossier note and write three new notes — all of which live in the Jarvis vault (a separate GitHub repo, gupta-builds/Jarvis), not in this repo. This repo's own automation never touches the vault interactively (run_pipeline.py writes once, non-interactively, via a scoped PAT). A human-in-the-loop skill is a different shape: it needs a Claude Code session with both this repo and the Jarvis vault present in the same working environment. State this prerequisite plainly in the skill's own instructions file (a session invoking /promote-dossier needs the Jarvis vault checked out locally, sibling to or alongside this repo — document the expected layout, don't assume it silently). Do not attempt to make the skill write across repos via the GitHub API instead — that reintroduces exactly the push-race/token-scope complexity core/git_ops.py already exists to solve for the one automated writer this pipeline has; a second interactive writer using a different mechanism is a real design smell, flag it rather than build around it if you hit this.

## Task A — The promote-dossier skill
Build a Claude Code skill (.claude/skills/promote-dossier/ in this repo, following the standard SKILL.md + reference file pattern) that turns one dossier into a Program note + Contacts/Each One note + Tracker/Each One note, with manual consent at the write step — never auto-writing silently. Behavior, in order:
1. Take a dossier file path (or company/title) as input.
2. Ask two small, concrete questions, not open-ended ones: (a) target folder — Programs/Serious/ or Programs/Considering/; (b) does the dossier's auto-assigned priority/category still hold, or does it need a human override? Offer the current auto-assigned value as the default answer, don't force retyping it.
3. Invoke contact research (this repo's enrich.py, as widened in Prompt 2 Task E) and show the human what was found — company info, any contacts, any LinkedIn search-snippet hits — before writing anything.
4. On explicit go-ahead only, write all three notes together, cross-linked (program field on Applying-adjacent notes, applying_note-equivalent links, etc. — match the existing cross-linking convention documented in 30_Order/Workflows/Internship Pipeline.md in the Jarvis vault; read that file directly for the exact field names before writing the templates below, don't invent new ones).
Write strict, enforced templates for all three note types (Program, Contacts/Each One, Tracker/Each One) as part of this task — not loose prose guidance. Each template's required frontmatter fields and the rule that they must always be present go into this repo's own CLAUDE.md so any future Claude Code session working in this repo (or the paired vault session) knows the contract without re-deriving it.

## Task B — contact-researcher subagent
The contact-pulling step in Task A above is exploratory, not deterministic (unlike everything else in this pipeline) — it's better modeled as a subagent the skill invokes than as a rigid script. Build a Claude Code agent (.claude/agents/contact-researcher.md) whose only job is: given a company name and the widened Firecrawl search scope from Prompt 2 Task E, return whatever real contact signal exists (recruiter, HR, engineering-blog byline, GitHub org member, LinkedIn search-snippet hit) with a source cited for each — never fabricate a plausible-sounding contact, report "nothing found" honestly when that's the real outcome; a wrong guess here is worse than an empty result, same principle as every filter rule in core/filter.py.

## Task C — loop-verifier agent
Build a Claude Code agent (.claude/agents/loop-verifier.md) that can be launched standalone to check the whole pipeline's actual live health in one pass: full test suite pass count, the last N scheduled run.yml / recheck.yml results via gh api, current dossier counts per priority subfolder in the vault against what run logs claim was written, whether seen_ids.json and the vault's actual dossier files have diverged, and whether any GitHub issues have been auto-filed. This is the automated version of the manual audits already run twice in this project's history (2026-07-19, 2026-07-25) — model its output the same way: a dated, evidence-cited verdict, not a vague "looks fine."

## Task D — Code-review skill/agent for this repo
Add a repo-scoped code-review setup: either a .claude/skills/review-loop-change/ skill or a .claude/agents/loop-reviewer.md agent (pick whichever fits this repo's actual size and change frequency better — this is a ~1,500-line repo with a ~1:1 test ratio, not a large codebase, say which you picked and why). It should check any proposed change against this repo's own established conventions before it ships: the zero-LLM-in-the-unattended-path rule, the permissive-by-default / explicit-negative-signal filter design, the fail-closed write-gate ordering, and the requirement that every new rule cites the real live data it was built from in a comment.

## Task E — .claude/settings.json for this repo
Tune permissions for what this repo's actual workflow needs: pytest runs, git operations short of force-push, gh CLI read operations (api, run list, issue list) without prompting every time, and explicit confirmation still required for anything that pushes to origin/master or modifies GitHub Actions secrets. Document in this repo's CLAUDE.md what each skill/agent above is for and when to reach for it instead of writing more Python by hand — the actual question to answer here is which of this repo's remaining manual toil (contact research, promotion, verification, review) is genuinely better solved by an agent than by more deterministic code, and say so explicitly rather than defaulting to "write a script" out of habit.

## Verification
Report each task's outcome individually. For Task A specifically, state clearly whether the skill was tested against a real dossier end-to-end (up to but not including the final write-consent step, which requires a human) or only reviewed for correctness — don't claim it works if it was never actually run.

## Claude

I'll start by verifying the stated prerequisites (Prompt 1/2 work) actually exist before building anything on top of them.

Stopping before building anything — the prerequisite check fails on all three points named in the prompt.

**Checked:**
1. `core/priority.py` — doesn't exist. Only "priority" hit in the repo is an unrelated comment in `run_pipeline.py` about post-date tie-breaking, not classification.
2. Four vault subfolders (`Programs/Serious/`, `Programs/Considering/`, `Contacts/Each One/`, `Tracker/Each One/`) — no references anywhere in this repo, and the Jarvis vault isn't even checked out locally right now: `jarvis-checkout/` is empty and gitignored (populated only by the scheduled CI workflow, per the `.gitignore` comment). Nothing to check them against.
3. Widened `enrich.py` — not widened. It still carries the original hard line verbatim: *"Hard line per the plan: no LinkedIn, no CAPTCHA bypass, no cookie injection, no stealth browsing, no login walls."* That directly contradicts what Task B/A of this prompt expect (LinkedIn search-snippet hits as a valid contact signal).

My memory of this project (`phase4-state-and-gates.md`) corroborates: it tracks Phases 1–6 (filter rules, enrich.py Layer 5, grade_resume.py, recheck.py bloat fixes) and explicitly records that same unmodified LinkedIn hard line as of 2026-07-18. There's no record of a "Prompt 1"/"Prompt 2" persona-config or priority-classification pass ever having run.

So: Prompt 1 and Prompt 2 have not run in this repo. Building the promote-dossier skill, the contact-researcher agent, or documenting a priority contract in this repo's CLAUDE.md right now would mean inventing the priority scheme, the frontmatter fields, and the enrichment scope from scratch — exactly the "build on top of an assumption" this prompt told me to avoid.

Want me to go ahead and do Prompt 1 + Prompt 2 first (persona config, `core/priority.py`, the four vault subfolders, widened `enrich.py`), or did you expect those to already be on a different branch/machine I should look at instead?

**Tool calls:**

- `Bash` — `echo "=== repo root ===" && ls -la && echo "=== core/ ===" && ls -la core/ 2>/dev/null && echo "=== priority.py exists? ===" && test -f core/priority.py && echo YES || echo NO && echo "=== enrich.py ===" && find . -iname "enrich.py" && echo "=== git log ===" && git log --oneline -20`
  ```
=== repo root ===
total 120
drwxr-xr-x 15 anant_gupta anant_gupta  4096 Jul 25 21:16 .
drwxr-xr-x  4 anant_gupta anant_gupta  4096 Jul 16 20:52 ..
drwxr-xr-x  2 anant_gupta anant_gupta  4096 Jul 16 21:47 .claude
drwxr-xr-x  9 anant_gupta anant_gupta  4096 Jul 25 21:26 .git
drwxr-xr-x  3 anant_gupta anant_gupta  4096 Jul 16 23:46 .github
-rw-r--r--  1 anant_gupta anant_gupta   468 Jul 17 15:24 .gitignore
drwxr-xr-x  3 anant_gupta anant_gupta  4096 Jul 17 15:31 .pytest_cache
drwxr-xr-x  5 anant_gupta anant_gupta  4096 Jul 16 21:52 .venv
-rw-r--r--  1 anant_gupta anant_gupta  9341 Jul 18 18:24 PRD.md
-rw-r--r--  1 anant_gupta anant_gupta  1352 Jul 18 14:56 README.md
drwxr-xr-x  2 anant_gupta anant_gupta  4096 Jul 25 21:26 __pycache__
drwxr-xr-x  3 anant_gupta anant_gupta  4096 Jul 26 00:35 core
-rw-r--r--  1 anant_gupta anant_gupta  6622 Jul 18 10:54 enrich.py
-rw-r--r--  1 anant_gupta anant_gupta  3390 Jul 18 10:55 grade_resume.py
drwxr-xr-x  3 anant_gupta anant_gupta  4096 Jul 25 21:16 ingestion
drwxr-xr-x  2 anant_gupta anant_gupta  4096 Jul 17 15:24 jarvis-checkout
drwxr-xr-x  2 anant_gupta anant_gupta  4096 Jul 25 21:15 logs
-rw-r--r--  1 anant_gupta anant_gupta  6074 Jul 25 21:16 recheck.py
-rw-r--r--  1 anant_gupta anant_gupta    59 Jul 17 10:51 requirements.txt
-rw-r--r--  1 anant_gupta anant_gupta 14709 Jul 25 21:16 run_pipeline.py
drwxr-xr-x  2 anant_gupta anant_gupta  4096 Jul 25 21:15 state
drwxr-xr-x  4 anant_gupta anant_gupta  4096 Jul 26 00:38 tests
drwxr-xr-x  4 anant_gupta anant_gupta  4096 Jul 18 18:23 vault_writer
=== core/ ===
total 44
drwxr-xr-x  3 anant_gupta anant_gupta  4096 Jul 26 00:35 .
drwxr-xr-x 15 anant_gupta anant_gupta  4096 Jul 25 21:16 ..
drwxr-xr-x  2 anant_gupta anant_gupta  4096 Jul 26 00:36 __pycache__
-rw-r--r--  1 anant_gupta anant_gupta 12047 Jul 26 00:35 filter.py
-rw-r--r--  1 anant_gupta anant_gupta  2403 Jul 17 11:30 git_ops.py
-rw-r--r--  1 anant_gupta anant_gupta   966 Jul 18 18:23 identity.py
-rw-r--r--  1 anant_gupta anant_gupta  3503 Jul 26 00:32 profile.yaml
-rw-r--r--  1 anant_gupta anant_gupta  2699 Jul 17 11:31 run_log.py
-rw-r--r--  1 anant_gupta anant_gupta  3784 Jul 25 20:45 schema_drift.py
=== priority.py exists? ===
NO
=== enrich.py ===
./enrich.py
=== git log ===
cdb4299 Update state + logs — 2026-07-25
a21b2fa Four new discovery sources: vanshb03, zshah101, Greenhouse, Ashby
b60a751 Update state + logs — 2026-07-25
3e88959 Update state + logs — 2026-07-25
bdc2416 Update state + logs — 2026-07-25
5075dd5 Update state + logs — 2026-07-25
d128a1c Update state + logs — 2026-07-25
f62c3d0 Recheck log — 2026-07-25
a9c2c64 Update state + logs — 2026-07-25
e615623 Update state + logs — 2026-07-25
18ff2ad Update state + logs — 2026-07-25
388202e Update state + logs — 2026-07-24
6f970b8 Update state + logs — 2026-07-24
6b974c3 Update state + logs — 2026-07-24
910c1f7 Update state + logs — 2026-07-24
c2ad6f5 Update state + logs — 2026-07-24
e9aca8c Update state + logs — 2026-07-24
eb06ec6 Update state + logs — 2026-07-24
4d1bf26 Update state + logs — 2026-07-24
b2dc704 Recheck log — 2026-07-24
  ```
- `Bash` — `echo "=== search for priority anywhere ===" && grep -rl "priority" --include="*.py" . | grep -v .venv | grep -v __pycache__
echo "=== jarvis-checkout dir ===" && ls -la jarvis-checkout/
echo "=== is jarvis-checkout a git repo / submodule? ===" && cat .gitmodules 2>/dev/null; git -C jarvis-checkout status 2>&1 | head -5
echo "=== search repo for any Jarvis vault path references ===" && grep -rn "Jarvis" --include="*.py" --include="*.yaml" --include="*.md" . | grep -v .venv | grep -v __pycache__ | head -30`
  ```
=== search for priority anywhere ===
run_pipeline.py
=== jarvis-checkout dir ===
total 8
drwxr-xr-x  2 anant_gupta anant_gupta 4096 Jul 17 15:24 .
drwxr-xr-x 15 anant_gupta anant_gupta 4096 Jul 25 21:16 ..
=== is jarvis-checkout a git repo / submodule? ===
On branch master
Your branch is behind 'origin/master' by 3 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
=== search repo for any Jarvis vault path references ===
grade_resume.py:16:DEFAULT_RESUME = ("/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/"
run_pipeline.py:2:validate -> write (Jarvis checkout) -> push (Jarvis, retry-safe) -> mark seen
run_pipeline.py:135:    the Jarvis checkout. Does NOT push and does NOT mutate seen_ids — the
run_pipeline.py:286:        record["errors"].append(f"Jarvis push failed: {exc}")
run_pipeline.py:289:            f"Jarvis push failed at {timestamp}",
run_pipeline.py:291:            f"gupta-builds/Jarvis failed after retry:\n\n```\n{exc}\n```\n\n"
core/run_log.py:2:markdown rollup appended (never rewritten) into the Jarvis vault.
core/git_ops.py:3:The Jarvis vault has its own independent auto-commit-and-push cycle running
recheck.py:131:            record["errors"].append(f"Jarvis push failed: {exc}")
recheck.py:134:                f"Recheck push to Jarvis failed at {now.isoformat()}",
tests/test_run_pipeline.py:336:    # the dossier files DO exist locally in the Jarvis checkout (validation
README.md:10:Full spec lives in the Jarvis vault: `Internship/Building System/Research Loop —
README.md:16:`gupta-builds/Jarvis` repo — schema-drift check, fetch, filter, dedup,
tests/test_git_ops.py:29:    simulating our scheduled workflow and Jarvis's own auto-commit cycle
PRD.md:3:**Status:** Verified against live repo/GitHub state on 2026-07-18 (git log, `pytest` [167/167], `gh run list`, `gh api`, live feed fetches — not assumed from memory). Still not independently product-reviewed; this was built spec-first in conversation, not PRD-first. Read this file alone for orientation — it does not require the Jarvis vault to make sense. For build history, decisions, and how each number below was verified, see `20_Progress/Internship/Building System/Phases 1-3 Run.md` in the Jarvis vault; it is not required reading to pick this project up, only to understand *why* it looks this way.
PRD.md:11:A 24/7 background process that watches known internship-listing sources, keeps only postings the user is actually eligible for under **three hard criteria** — timing (Summer 2027 or the Dec 2026–Jan 2027 winter window), location (US/Remote), and OPT eligibility (excluded only on an explicit citizenship/clearance/no-OPT signal) — and writes a live, deduplicated, dead-link-free, **content-carrying** list into the user's Obsidian vault (Jarvis), so screening happens in the vault without visiting posting pages by hand.
PRD.md:87:This file is the standalone orientation document. `20_Progress/Internship/Building System/Phases 1-3 Run.md` in the Jarvis vault is the deeper record: build-by-build history, bugs found and fixed, audit evidence, and reasoning. If the two disagree on a fact, re-verify against live state — most-recently-verified wins, and the disagreement itself means one of them needs updating.
  ```
- `Bash` — `echo "=== jarvis-checkout remote ===" && git -C jarvis-checkout remote -v
echo "=== jarvis-checkout full status ===" && git -C jarvis-checkout status
echo "=== jarvis-checkout top-level dirs ===" && ls jarvis-checkout/ 2>/dev/null; find jarvis-checkout -maxdepth 1 2>/dev/null
echo "=== .gitignore mentions jarvis-checkout? ===" && grep -n "jarvis" .gitignore -i`
  ```
=== jarvis-checkout remote ===
origin	https://github.com/gupta-builds/internship-research-loop.git (fetch)
origin	https://github.com/gupta-builds/internship-research-loop.git (push)
=== jarvis-checkout full status ===
On branch master
Your branch is behind 'origin/master' by 3 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   ../core/filter.py
	modified:   ../core/profile.yaml
	modified:   ../ingestion/normalize.py
	modified:   ../ingestion/sources.py
	modified:   ../recheck.py
	modified:   ../run_pipeline.py
	modified:   ../tests/fixtures/josegael.json
	modified:   ../tests/fixtures/simplifyjobs.json
	modified:   ../tests/fixtures/vanshb03.json
	modified:   ../tests/fixtures/zshah101.json
	modified:   ../tests/test_filter.py
	modified:   ../tests/test_run_pipeline.py
	modified:   ../tests/test_sources.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	../ingestion/freehire.py
	../tests/fixtures/freehire.json
	../tests/test_freehire.py

no changes added to commit (use "git add" and/or "git commit -a")
=== jarvis-checkout top-level dirs ===
jarvis-checkout
=== .gitignore mentions jarvis-checkout? ===
5:# The scheduled workflow checks out gupta-builds/Jarvis into this path (a
8:# harmless to Jarvis, but corrupts this repo's own history and breaks
10:# submodule path 'jarvis-checkout' in .gitmodules").
11:jarvis-checkout/
  ```
- `Bash` — `echo "=== run_pipeline.py priority context ===" && grep -n -i "priority" run_pipeline.py
echo "=== enrich.py content ===" && cat enrich.py | head -60
echo "=== search for Programs/Serious Considering Contacts Tracker ===" && grep -rn -i "Programs/Serious\|Programs/Considering\|Contacts/Each\|Tracker/Each\|Each One" . --include="*.py" --include="*.md" --include="*.yaml" 2>/dev/null | grep -v .venv`
  ```
=== run_pipeline.py priority context ===
69:    (an unknown post date must not win priority over a known-recent one).
=== enrich.py content ===
#!/usr/bin/env python3
"""Layer 5 — on-demand company/contact enrichment for one promoted dossier.

Run manually at Step 2 (Commit) of the vault's Internship Pipeline workflow —
deliberately NOT called from run_pipeline.py and never automatic on dossiers
the discovery loop writes:

    FIRECRAWL_API_KEY=... python enrich.py "<path to dossier .md>"

Public sources only: company site/blog scraped via Firecrawl, GitHub org
public members, blog author bylines, pattern-inferred first.last@domain
checked against the domain's MX records (DNS-over-HTTPS — no new dependency).
Hard line per the plan: no LinkedIn, no CAPTCHA bypass, no cookie injection,
no stealth browsing, no login walls. Anything behind one gets skipped.

No LLM call anywhere — scraped text is trimmed verbatim, never summarized.
"""
import os
import re
import sys
from datetime import date
from urllib.parse import urlparse

import requests
import yaml

FIRECRAWL = "https://api.firecrawl.dev/v1"
TIMEOUT = 30


def read_dossier(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        raise ValueError("no YAML frontmatter found — is this a dossier file?")
    return yaml.safe_load(m.group(1))


def replace_enrichment(text: str, section: str) -> str:
    """Idempotent: a re-run replaces the previous Enrichment section."""
    base = re.split(r"\n## Enrichment\b", text)[0].rstrip("\n")
    return base + "\n\n" + section


def _fc(path: str, payload: dict, key: str) -> dict:
    r = requests.post(f"{FIRECRAWL}/{path}", json=payload, timeout=TIMEOUT,
                      headers={"Authorization": f"Bearer {key}"})
    r.raise_for_status()
    return r.json()


def fc_search(query: str, key: str) -> list:
    return _fc("search", {"query": query, "limit": 5}, key).get("data", [])


def fc_scrape(url: str, key: str) -> str:
    data = _fc("scrape", {"url": url, "formats": ["markdown"]}, key).get("data", {})
    return data.get("markdown", "")


def trim(md: str, limit: int = 800) -> str:
=== search for Programs/Serious Considering Contacts Tracker ===
  ```
- `Read` — `/home/anant_gupta/.claude/projects/-home-anant-gupta-projects-work-internship-research-loop/memory/phase4-state-and-gates.md`

## You

Prompt 1 and 2 have finished running. Review the work done and go ahead and run the prompt pasted above - Prompt 3. Do the task with no mistakes, focusing on the goal at hand. Do all the tasks correctly and stick to what's been listed down in jarvis (prompt above). Finish the task.

## Claude

The Jarvis vault isn't checked out in this git repo, but I have live MCP access to it (`jarvis-fs`, `jarvis`). Let me verify the vault-side prerequisites directly and review the classify.py/relevance.py/enrich.py changes in parallel.

258/258 tests pass on the current working tree. Let me set up a task list and start building — five tasks plus verification.

Good, plenty of local examples. Let me check the format of a couple of relevant ones (a reviewer agent and an Obsidian one, since our agents touch both domains).

Task E's settings.json changes match exactly what the `update-config` skill is meant for — let me use it instead of hand-rolling the permissions format.

Settings file written and validated. Now for the CLAUDE.md documenting note-template contracts and when to use each skill/agent.

Now let's verify promote-dossier end-to-end against a real dossier, up to (not including) the write step. First, pick a real dossier from the vault.

Found a real, unpromoted dossier to test against: Appian's "Software Engineering Intern" (vanshb03 source). One honest complication already surfaced — this dossier predates `core/classify.py`, so it has no auto-assigned bucket/classification callout to default to. Let me run the actual skill flow, including that edge case.

No response requested.

**Tool calls:**

- `Bash` — `echo "=== git log ===" && git log --oneline -10 && echo "=== git status ===" && git status && echo "=== core/ ===" && ls -la core/ && echo "=== priority.py? ===" && test -f core/priority.py && echo YES || echo NO`
  ```
=== git log ===
cdb4299 Update state + logs — 2026-07-25
a21b2fa Four new discovery sources: vanshb03, zshah101, Greenhouse, Ashby
b60a751 Update state + logs — 2026-07-25
3e88959 Update state + logs — 2026-07-25
bdc2416 Update state + logs — 2026-07-25
5075dd5 Update state + logs — 2026-07-25
d128a1c Update state + logs — 2026-07-25
f62c3d0 Recheck log — 2026-07-25
a9c2c64 Update state + logs — 2026-07-25
e615623 Update state + logs — 2026-07-25
=== git status ===
On branch master
Your branch is behind 'origin/master' by 3 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   core/filter.py
	modified:   core/profile.yaml
	modified:   enrich.py
	modified:   ingestion/normalize.py
	modified:   ingestion/posting_page.py
	modified:   ingestion/sources.py
	modified:   recheck.py
	modified:   run_pipeline.py
	modified:   tests/fixtures/josegael.json
	modified:   tests/fixtures/simplifyjobs.json
	modified:   tests/fixtures/vanshb03.json
	modified:   tests/fixtures/zshah101.json
	modified:   tests/test_enrich.py
	modified:   tests/test_filter.py
	modified:   tests/test_posting_page.py
	modified:   tests/test_recheck.py
	modified:   tests/test_run_pipeline.py
	modified:   tests/test_sources.py
	modified:   tests/test_writer.py
	modified:   vault_writer/templates/dossier.md.j2
	modified:   vault_writer/validate.py
	modified:   vault_writer/writer.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	core/classify.py
	core/relevance.py
	ingestion/freehire.py
	tests/fixtures/freehire.json
	tests/fixtures/posting_ashby_ctgt.md
	tests/test_classify.py
	tests/test_freehire.py
	tests/test_relevance.py

no changes added to commit (use "git add" and/or "git commit -a")
=== core/ ===
total 56
drwxr-xr-x  3 anant_gupta anant_gupta  4096 Jul 26 01:23 .
drwxr-xr-x 15 anant_gupta anant_gupta  4096 Jul 26 01:28 ..
drwxr-xr-x  2 anant_gupta anant_gupta  4096 Jul 26 01:24 __pycache__
-rw-r--r--  1 anant_gupta anant_gupta  3289 Jul 26 01:23 classify.py
-rw-r--r--  1 anant_gupta anant_gupta 12047 Jul 26 00:35 filter.py
-rw-r--r--  1 anant_gupta anant_gupta  2403 Jul 17 11:30 git_ops.py
-rw-r--r--  1 anant_gupta anant_gupta   966 Jul 18 18:23 identity.py
-rw-r--r--  1 anant_gupta anant_gupta  3503 Jul 26 00:32 profile.yaml
-rw-r--r--  1 anant_gupta anant_gupta  5159 Jul 26 01:16 relevance.py
-rw-r--r--  1 anant_gupta anant_gupta  2699 Jul 17 11:31 run_log.py
-rw-r--r--  1 anant_gupta anant_gupta  3784 Jul 25 20:45 schema_drift.py
=== priority.py? ===
NO
  ```
- `Bash` — `echo "=== jarvis-checkout ===" && ls -la jarvis-checkout/ && find jarvis-checkout -maxdepth 3 2>/dev/null
echo "=== git diff stat ===" && git diff --stat HEAD`
  ```
=== jarvis-checkout ===
total 8
drwxr-xr-x  2 anant_gupta anant_gupta 4096 Jul 17 15:24 .
drwxr-xr-x 15 anant_gupta anant_gupta 4096 Jul 26 01:28 ..
jarvis-checkout
=== git diff stat ===
 core/filter.py                       |  29 +++++++++-
 core/profile.yaml                    |  25 ++++++++-
 enrich.py                            |  37 +++++++++++++
 ingestion/normalize.py               |  41 ++++++++++++++
 ingestion/posting_page.py            |  25 ++++++++-
 ingestion/sources.py                 |  39 +++++++++++---
 recheck.py                           |  52 ++++++++++++++----
 run_pipeline.py                      |  46 ++++++++++++----
 tests/fixtures/josegael.json         |  22 ++++++++
 tests/fixtures/simplifyjobs.json     |  22 ++++++++
 tests/fixtures/vanshb03.json         |  16 ++++++
 tests/fixtures/zshah101.json         |  21 ++++++++
 tests/test_enrich.py                 |  47 +++++++++++++++-
 tests/test_filter.py                 |  76 ++++++++++++++++++++++++++
 tests/test_posting_page.py           |  44 ++++++++++++++-
 tests/test_recheck.py                |  28 ++++++++--
 tests/test_run_pipeline.py           |  22 +++++---
 tests/test_sources.py                |  34 ++++++++++++
 tests/test_writer.py                 |  84 +++++++++++++++++++++++++----
 vault_writer/templates/dossier.md.j2 |  14 +++--
 vault_writer/validate.py             |   4 +-
 vault_writer/writer.py               | 100 ++++++++++++++++++++++++++++-------
 22 files changed, 751 insertions(+), 77 deletions(-)
  ```
- `Bash` — `echo "=== core/classify.py ===" && cat core/classify.py
echo "=== core/relevance.py ===" && cat core/relevance.py`
  ```
=== core/classify.py ===
"""Layer 2.5b — priority-bucket classification for listings that already
passed core/relevance.py's gate. Deterministic keyword matching against
title + category + fetched posting content (empty content degrades
gracefully — title/category alone still register). Zero-LLM, same style as
core/filter.py and core/relevance.py.

Exactly one bucket, checked in this order (first match wins — a posting can
show signals for more than one, e.g. AI infra at a fintech should read
AI/ML, not CyS & Finance):
  1. AI/ML       — LLM, RAG, agents, ML infra, applied AI, deep learning
  2. CyS & Finance — security or finance-adjacent software engineering
  3. Fullstack   — product/frontend/backend/systems engineering
  4. Other       — genuine software engineering (relevance gate already
                   confirmed this), matching none of the above
"""
import re

BUCKET_FOLDERS = {
    "AI/ML": "1 - AI & ML",
    "Fullstack": "2 - Fullstack",
    "CyS & Finance": "3 - CyS & Finance",
    "Other": "Other",
}

# Real examples: Bosch "Autonomous Driving – Internship in ML" (model
# training, AI-enabled robotics test system, PyTorch) and Magna "R&D-
# Computer Vision Engineering Intern" (TensorFlow or PyTorch, ML data
# pipeline) both match here despite being automotive companies.
_AI_ML_RE = re.compile(
    r"\b(llm|large language models?|\brag\b|retrieval.augmented|agentic|ai agent"
    r"|machine learning|deep learning|ml infra|applied ai|generative ai"
    r"|computer vision|\bnlp\b|natural language|embeddings?|pytorch|tensorflow"
    r"|neural network|data scientist|ml engineer|ai engineer|ai.enabled)\b", re.I,
)
_CYS_FINANCE_RE = re.compile(
    r"\b(security engineer|cybersecurity|application security|appsec"
    r"|penetration test|infosec|threat|vulnerability|quant(itative)? developer"
    r"|quantitative (research|trading)|trading systems?|fintech|risk engine"
    r"|payments? (engineer|infrastructure)|blockchain|crypto|defi)\b", re.I,
)
_FULLSTACK_RE = re.compile(
    r"\b(full.?stack|frontend|front.end|backend|back.end|\breact\b|next\.?js"
    r"|web (developer|engineer)|product engineer|api (design|development)"
    r"|systems? engineer|infrastructure engineer|platform engineer|devops"
    r"|mobile (developer|engineer)|\bios\b|\bandroid\b)\b", re.I,
)


def classify(title: str, category: str, posting_content: str) -> tuple:
    """Returns (bucket_name, signal) — signal is the specific real phrase
    that drove the classification (empty string for the Other bucket, since
    there's nothing bucket-specific to point at)."""
    haystack = f"{title} {category} {posting_content}"
    for bucket, pattern in (("AI/ML", _AI_ML_RE), ("CyS & Finance", _CYS_FINANCE_RE), ("Fullstack", _FULLSTACK_RE)):
        m = pattern.search(haystack)
        if m:
            return bucket, m.group(0)
    return "Other", ""


def classification_callout(bucket: str, signal: str) -> str:
    """No numeric label ('Priority 1/2/3') — the folder location already
    encodes the category; a number in the callout text was explicitly
    rejected in design review."""
    if not signal:
        return f"> [!NOTE] {bucket}: genuine software engineering role, no bucket-specific signal matched."
    return f'> [!NOTE] {bucket}: matched on "{signal}".'
=== core/relevance.py ===
"""Layer 2.5 — CS/software-relevance gate. Runs after matches() passes, before
the write gate. Two-stage, zero-LLM, same keyword-heuristic style as
core/filter.py:

  stage1_reject: cheap, title/raw_text only, no fetch. Called in
  fetch_and_filter alongside matches() — catches the unambiguous
  non-software cases for free before a Firecrawl credit is ever spent.

  stage2_confirm: content-based, called only once posting_content has
  actually been fetched (same point the OPT-eligibility check already uses
  it). Adjacent fields (hardware, robotics, astrophysics, space,
  embedded/firmware) are not auto-excluded by stage 1 — they pass stage 2
  only if the posting's real content shows genuine software/CS work.

Persona bar: BS Computer Science, full-stack + AI/ML + backend/systems
skillset (Main Resume.md: Python/Rust/TS/JS/React/Java/C, RAG/embeddings/LLM
APIs/data pipelines, Next.js/full-stack, Postgres/Docker/infra; Engineer Edge
Roadmap.md: "systems-minded AI engineer" — full-stack products + backend
systems + observability + AI workflows). A posting passes if its real duties
involve software/CS work, even at a company in an adjacent industry (space,
robotics, astrophysics, automotive/hardware). A posting fails if it's
fundamentally non-technical (financial/risk analyst, tax preparer, sports
performance analytics) regardless of company.
"""
import re


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


# Real live examples confirmed against seeded Greenhouse boards 2026-07-26:
# FC Cincinnati "Academy Performance Analyst Intern" / "FCC2 Performance
# Analyst Intern" (pure sports video coding/KPI labeling, zero software —
# see tests/fixtures/relevance for the real fetched content), Walleye
# Capital "Investor Relations Intern". Deliberately narrow — a false
# positive here silently kills a listing before it's ever fetched, so only
# unambiguous non-software role nouns go here, and each pattern requires the
# non-software noun to be the role itself, not a qualifier ahead of a
# software-shaped word: "Tax Technology Intern" (real SimplifyJobs fixture,
# category AI/ML/Data, genuinely technology-consulting work) must NOT match
# "tax accountant"/"tax preparer", and "Risk Technology Analyst Intern"
# (real Walleye Capital title) must NOT match "risk analyst" — "Technology"
# sits between the two words in both real titles, breaking the adjacency
# these patterns require.
_STAGE1_REJECT_RE = re.compile(
    r"\b(financial analyst|risk analyst|performance analyst"
    r"|tax (associate|preparer|accountant)"
    r"|investor relations"
    r"|sports performance (analyst|analytics)|academy performance (analyst|analysis)"
    r"|human resources intern|hr intern|marketing intern|business development intern)\b",
    re.I,
)


def stage1_reject(title: str, raw_text: str) -> bool:
    """True if this listing's title/raw_text is unambiguously non-software —
    reject without ever fetching the page."""
    return bool(_STAGE1_REJECT_RE.search(f"{title} {raw_text}"))


# Adjacent-field company/title hint — NOT a reject signal on its own (Jane
# Street "Hardware Engineer (FPGA/ASIC) Intern" and Bosch/Magna's automotive
# ML roles all pass real content checks below). Only postings that hit this
# hint need their fetched content checked at all; everything else already
# cleared stage 1 and passes through unconditionally.
_ADJACENT_FIELD_COMPANY_HINT_RE = re.compile(
    r"\b(space|aerospace|robotics|astro|satellite|defense|automotive|firmware"
    r"|embedded|hardware)\b", re.I,
)

# Real content signals confirmed against live vault dossiers 2026-07-26: Bosch
# "Autonomous Driving – Internship in ML" (Python, data pipelines, model
# training, robotics test framework built in software) and Magna "R&D-
# Computer Vision Engineering Intern" (Python, TensorFlow/PyTorch, ML data
# pipeline, cloud platforms) both pass on these signals despite being
# automotive/hardware companies. Jane Street's "Hardware Engineer (FPGA/ASIC)
# Intern" passes on "programming language"/"software" signals despite being a
# genuine hardware role.
_SOFTWARE_CONTENT_SIGNAL_RE = re.compile(
    r"\b(python|java|c\+\+|rust|typescript|javascript|ocaml|api|apis|rest api"
    r"|software (development|engineering)|programming language|data pipeline"
    r"|machine learning|deep learning|tensorflow|pytorch|full.?stack|backend"
    r"|frontend|front.end|database|\bsql\b|\bgit\b|ci/cd|microservice"
    r"|algorithm|codebase|debug|unit test|source code)\b", re.I,
)


def stage2_confirm(title: str, company: str, posting_content: str) -> bool:
    """Called only when posting_content is non-empty. True = passes (either
    not adjacent-field at all, or adjacent-field AND content shows real
    software work). False = adjacent-field company/title with no software
    signal in the actual content — genuinely non-technical despite passing
    stage 1 (e.g. a hardware-manufacturing floor role at a space company)."""
    if not _ADJACENT_FIELD_COMPANY_HINT_RE.search(f"{title} {company}"):
        return True
    return bool(_SOFTWARE_CONTENT_SIGNAL_RE.search(posting_content))
  ```
- `Bash` — `git diff HEAD -- enrich.py
echo "=====VAULT_WRITER TEMPLATE====="
git diff HEAD -- vault_writer/templates/dossier.md.j2
echo "=====VAULT_WRITER WRITER====="
git diff HEAD -- vault_writer/writer.py`
  ```
diff --git a/enrich.py b/enrich.py
index e99d93c..3ced3d0 100644
--- a/enrich.py
+++ b/enrich.py
@@ -57,6 +57,30 @@ def fc_scrape(url: str, key: str) -> str:
     return data.get("markdown", "")
 
 
+# Confirmed live 2026-07-26: simplify.jobs is a real, live site (SimplifyJobs'
+# own job board, separate from their GitHub feed) — resolves 200. A search
+# hit landing on any of these domains is noise, not a real contact.
+_EXCLUDED_CONTACT_DOMAINS_RE = re.compile(
+    r"indeed\.com|glassdoor\.com|simplify\.jobs|linkedin\.com/jobs/", re.I,
+)
+
+
+def _search_and_filter(query: str, key: str) -> list:
+    return [h for h in fc_search(query, key) if not _EXCLUDED_CONTACT_DOMAINS_RE.search(h.get("url", ""))]
+
+
+def linkedin_recruiter_snippet(company: str, key: str) -> list:
+    # Search-snippet text only — NEVER fc_scrape() or otherwise fetch the
+    # underlying linkedin.com URL; that crosses the "no LinkedIn... no login
+    # walls" line in this module's docstring above. Whatever text Firecrawl's
+    # search-result snippet itself contains (title/description fields,
+    # confirmed live 2026-07-26 — a real hit returned "Katie Nielsen - Senior
+    # Recruiter at Anduril Industries" as its title) is all we ever see.
+    hits = fc_search(f"site:linkedin.com {company} recruiter", key)
+    return [(h.get("title", ""), h.get("description", ""), h.get("url", ""))
+            for h in hits if "linkedin.com" in h.get("url", "")]
+
+
 def trim(md: str, limit: int = 800) -> str:
     # ponytail: naive trim keeps nav/link junk at the top of some pages —
     # good enough to orient a human; add a boilerplate stripper if it annoys.
@@ -143,6 +167,19 @@ def main():
         sources.append(f"https://github.com/orgs/{org}/people")
         contacts += [(n, u) for n, u in members]
 
+    for query, label in ((f"{company} recruiter", "recruiter search"),
+                         (f"{company} university recruiting", "university recruiting search")):
+        for hit in _search_and_filter(query, key):
+            name = hit.get("title", "").strip()
+            if name:
+                contacts.append((name, f"{label}: {hit['url']}"))
+                sources.append(hit["url"])
+
+    for name, snippet, url in linkedin_recruiter_snippet(company, key):
+        if name:
+            contacts.append((name, f"linkedin search snippet: {snippet or url}"))
+            sources.append(url)
+
     mx = mx_ok(domain) if domain else False
     rows = []
     for name, src in contacts:
=====VAULT_WRITER TEMPLATE=====
diff --git a/vault_writer/templates/dossier.md.j2 b/vault_writer/templates/dossier.md.j2
index 56dc587..2b6e5c0 100644
--- a/vault_writer/templates/dossier.md.j2
+++ b/vault_writer/templates/dossier.md.j2
@@ -1,8 +1,16 @@
 ---
 {{ frontmatter_yaml }}---
-# {{ company }} — {{ title }}
-{% if posting_content %}Auto-discovered {{ date_found }} from {{ source }}. Posting content below fetched at discovery (verbatim extraction, trimmed); company/contact enrichment happens on promotion, per [[30_Order/Workflows/Internship Pipeline]].
+# {{ title }}
+{% if posting_content -%}
+Found {{ date_found }} via {{ source }}.
+{% if classification_callout -%}
+{{ classification_callout }}
+{% endif -%}
 ## Posting (fetched {{ date_found }})
 {{ posting_content }}
-{%- else %}Auto-discovered {{ date_found }} from {{ source }}. No enrichment yet — company/contact research happens on promotion, per [[30_Order/Workflows/Internship Pipeline]].
+{%- else -%}
+Found {{ date_found }} via {{ source }}. No posting content fetched.
+{% if classification_callout -%}
+{{ classification_callout }}
+{% endif -%}
 {%- endif %}
=====VAULT_WRITER WRITER=====
diff --git a/vault_writer/writer.py b/vault_writer/writer.py
index 2c6c423..0ded6ff 100644
--- a/vault_writer/writer.py
+++ b/vault_writer/writer.py
@@ -5,7 +5,9 @@ same markdown before anything touches disk. write_dossier() itself does not
 re-run the write gate — callers are expected to have already gotten a passing
 ValidationResult from validate.validate() before calling it.
 """
+import json
 import re
+from datetime import datetime, timezone
 from pathlib import Path
 
 import yaml
@@ -13,6 +15,7 @@ from jinja2 import Environment, FileSystemLoader
 
 TEMPLATE_DIR = Path(__file__).parent / "templates"
 DOSSIER_SUBPATH = Path("10_Areas/Career/Internships/List/Dossiers")
+DOSSIER_UIDS_FILENAME = "dossier_uids.json"
 
 _env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
 _template = _env.get_template("dossier.md.j2")
@@ -38,28 +41,35 @@ def _yaml_list(items) -> list:
     return list(items) if items else []
 
 
+def _iso_date(epoch) -> str:
+    return datetime.fromtimestamp(epoch, tz=timezone.utc).date().isoformat() if epoch else None
+
+
 def build_frontmatter(listing, uid: str, date_found: str, matched_reason: str) -> dict:
-    """The exact field set from the plan's Dossier Note Shape, in order."""
+    """uid and category are deliberately not rendered — uid stays available
+    internally via the dossier_uids.json manifest (see write_dossier), and
+    category was never surfaced to the reader anywhere else in the note.
+    `next:` (not `promoted:`) matches every other note type's convention
+    across the vault."""
     return {
-        "uid": uid,
         "company": listing.company,
         "title": listing.title,
         "url": listing.url,
         "source": listing.source,
-        "category": listing.category or None,
         "terms": _yaml_list(listing.terms),
         "locations": _yaml_list(listing.locations),
         "target_year": _yaml_list(listing.target_year),
-        "date_posted": listing.date_posted,
+        "date_posted": _iso_date(listing.date_posted),
         "date_found": date_found,
         "matched_reason": matched_reason,
         "status": "unreviewed",
-        "promoted": None,
+        "next": None,
         "tags": ["internship", "auto-discovered"],
     }
 
 
-def render_dossier(listing, uid: str, date_found: str, matched_reason: str, posting_content: str = "") -> str:
+def render_dossier(listing, uid: str, date_found: str, matched_reason: str, posting_content: str = "",
+                   classification_callout: str = "") -> str:
     frontmatter = build_frontmatter(listing, uid, date_found, matched_reason)
     frontmatter_yaml = yaml.dump(
         frontmatter, Dumper=_FrontmatterDumper, sort_keys=False, default_flow_style=False, allow_unicode=True
@@ -71,36 +81,90 @@ def render_dossier(listing, uid: str, date_found: str, matched_reason: str, post
         date_found=date_found,
         source=listing.source,
         posting_content=posting_content,
+        classification_callout=classification_callout,
     )
     return markdown.rstrip("\n") + "\n"
 
 
-def slugify_uid(uid: str) -> str:
-    slug = re.sub(r"[^a-zA-Z0-9]+", "-", uid).strip("-").lower()
-    return slug
+_ILLEGAL_FILENAME_CHARS = re.compile(r'[\\/:*?"<>|\n\r\t]')
+
+
+def dossier_filename(role: str, company: str, existing_names) -> str:
+    """'[Role] - [Company].md', Windows-unsafe chars stripped (the vault lives
+    on a Windows-mounted drive), collision tie-broken with ' (2)', ' (3)', ...
+    matching the candidate's own hand-renamed 'Software Engineer -
+    Ellipsis Labs.md'. existing_names is scoped to wherever the collision
+    check should happen (the target bucket subfolder)."""
+
+    def sanitize(s: str) -> str:
+        return _ILLEGAL_FILENAME_CHARS.sub("", s).strip()
+
+    base = f"{sanitize(role)} - {sanitize(company)}"
+    existing = set(existing_names)
+    name = f"{base}.md"
+    n = 2
+    while name in existing:
+        name = f"{base} ({n}).md"
+        n += 1
+    return name
+
+
+def load_dossier_uids(state_dir) -> dict:
+    path = Path(state_dir) / DOSSIER_UIDS_FILENAME
+    if not path.exists():
+        return {}
+    return json.loads(path.read_text())
+
+
+def save_dossier_uids(state_dir, manifest: dict) -> None:
+    path = Path(state_dir) / DOSSIER_UIDS_FILENAME
+    path.parent.mkdir(parents=True, exist_ok=True)
+    path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
 
 
 def scan_dossiers(vault_root) -> list:
     """Frontmatter dicts of every dossier file actually present in the vault
-    checkout. File existence is the truth here, deliberately not
+    checkout — recursively, across the flat legacy root and every priority-
+    bucket subfolder (Viewed/ included if anything's ever there; nothing in
+    this pipeline ever writes into it, but its contents still count for
+    cross-source dedup). File existence is the truth here, deliberately not
     seen_ids.json — the two diverged permanently after the 2026-07-18 manual
     vault cleanup (110 dossiers deleted outside the pipeline, uids kept)."""
     dossiers_dir = Path(vault_root) / DOSSIER_SUBPATH
     out = []
-    for path in sorted(dossiers_dir.glob("*.md")) if dossiers_dir.is_dir() else []:
+    for path in sorted(dossiers_dir.glob("**/*.md")) if dossiers_dir.is_dir() else []:
         m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.DOTALL)
         fm = yaml.safe_load(m.group(1)) if m else None
-        if isinstance(fm, dict) and fm.get("uid"):
+        if isinstance(fm, dict) and fm.get("company"):
             fm["_path"] = path
             out.append(fm)
     return out
 
 
-def write_dossier(vault_root, uid: str, markdown: str) -> Path:
-    """Writes an already-rendered, already-validated dossier. Idempotent on uid:
-    re-writing the same uid overwrites the same file rather than creating a new one."""
-    dossiers_dir = Path(vault_root) / DOSSIER_SUBPATH
-    dossiers_dir.mkdir(parents=True, exist_ok=True)
-    path = dossiers_dir / f"{slugify_uid(uid)}.md"
+def write_dossier(vault_root, uid: str, markdown: str, role: str, company: str, bucket_folder: str,
+                  state_dir=None) -> Path:
+    """Writes an already-rendered, already-validated dossier into its
+    priority-bucket subfolder. Idempotent on uid: if state_dir's manifest
+    already maps this uid to a path, that exact file is overwritten instead
+    of a new collision-suffixed one being created — re-rendering the same
+    uid (e.g. a same-day re-run with enriched content) must not duplicate the
+    note. uid itself is never rendered into the note; state_dir (if given) is
+    where it's recorded instead, for recheck.py's removal-checking."""
+    vault_root = Path(vault_root)
+    manifest = load_dossier_uids(state_dir) if state_dir is not None else {}
+    existing_rel_path = next((rel for rel, u in manifest.items() if u == uid), None)
+
+    if existing_rel_path is not None:
+        path = vault_root / existing_rel_path
+        path.parent.mkdir(parents=True, exist_ok=True)
+    else:
+        dossiers_dir = vault_root / DOSSIER_SUBPATH / bucket_folder
+        dossiers_dir.mkdir(parents=True, exist_ok=True)
+        existing_names = {p.name for p in dossiers_dir.glob("*.md")}
+        path = dossiers_dir / dossier_filename(role, company, existing_names)
+
     path.write_text(markdown)
+    if state_dir is not None:
+        manifest[str(path.relative_to(vault_root))] = uid
+        save_dossier_uids(state_dir, manifest)
     return path
  ```
- `ToolSearch` — `{"query":"select:mcp__jarvis-fs__list_allowed_directories,mcp__jarvis-fs__list_directory,mcp__jarvis-fs__read_text_file,mcp__jarvis-fs__search_files,mcp__jarvis-fs__directory_tree","max_results":10}`
- `mcp__jarvis-fs__list_allowed_directories` — `{}`
- `ToolSearch` — `{"query":"select:mcp__jarvis__vault_list,mcp__jarvis__search_simple,mcp__jarvis__vault_read,mcp__jarvis__vault_get_document_map","max_results":10}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/List/Dossiers"}`
- `mcp__jarvis__vault_list` — `{"path":"30_Order/Workflows"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships"}`
- `mcp__jarvis__vault_read` — `{"path":"30_Order/Workflows/Internship Pipeline.md"}`
- `mcp__jarvis__vault_read` — `{"path":"30_Order/Workflows/Promotion.md"}`
- `mcp__jarvis__vault_list` — `{"path":"30_Order/Templates/Career"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Programs"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Contacts"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Tracker"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Programs/Serious"}`
- `mcp__jarvis__vault_read` — `{"path":"30_Order/Templates/Career/Program Template.md"}`
- `mcp__jarvis__vault_read` — `{"path":"30_Order/Templates/Career/Contact Template.md"}`
- `mcp__jarvis__vault_read` — `{"path":"30_Order/Templates/Career/Applying Template.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/Programs/Serious/2026-HRT-Sophomore.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/Tracker/Internship - Dashboard.md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/Tracker/Tracker.md"}`
- `Bash` — `echo "=== does repo already have CLAUDE.md? ===" && find . -iname "CLAUDE.md" -not -path "./.venv/*"
echo "=== .claude dir ===" && ls -la .claude/
echo "=== profile.yaml diff ===" && git diff HEAD -- core/profile.yaml
echo "=== .github workflows ===" && ls .github/workflows/ 2>/dev/null && find .github -type f`
  ```
=== does repo already have CLAUDE.md? ===
=== .claude dir ===
total 16
drwxr-xr-x  2 anant_gupta anant_gupta 4096 Jul 26 00:54 .
drwxr-xr-x 15 anant_gupta anant_gupta 4096 Jul 26 01:28 ..
-rw-r--r--  1 anant_gupta anant_gupta  111 Jul 26 00:54 scheduled_tasks.lock
-rw-r--r--  1 anant_gupta anant_gupta  116 Jul 16 21:47 settings.local.json
=== profile.yaml diff ===
diff --git a/core/profile.yaml b/core/profile.yaml
index 896af93..21c3c97 100644
--- a/core/profile.yaml
+++ b/core/profile.yaml
@@ -8,10 +8,33 @@ accept_unrestricted: true  # postings with no class-year field at all still matc
 # (three real listings co-tag ["Fall 2026", "Winter 2027"]). Postings don't
 # publish actual months in the feed, so the human screen of the fetched posting
 # content is still what confirms a genuine Dec-Jan window per posting.
-terms: ["Summer 2027", "Winter 2027"]
+terms: ["Summer 2027", "Winter 2027", "Spring 2027"]
+# Summer/Winter 2027 are equally top priority; Spring 2027 is wanted but
+# explicitly lower priority. This is a weight, not a second pass/fail gate —
+# Spring 2027 still matches like any other wanted term today. A later, separate
+# task consumes this for priority tagging; this one only makes it present and
+# readable downstream.
+terms_weight: {"Summer 2027": "high", "Winter 2027": "high", "Spring 2027": "low"}
 # Real category values observed on SimplifyJobs/Summer2026-Internships (dev/.github/scripts/listings.json),
 # not the generic names in the original transcript — confirmed by fetching live data 2026-07-16.
 categories: ["Software", "Software Engineering", "AI/ML/Data", "Data Science, AI & Machine Learning"]
+# Fellowship/research/mentorship-shaped entries were checked against live data
+# 2026-07-26 (SimplifyJobs, JGCL, zshah101 feeds + 5 Greenhouse/5 Ashby seeded
+# company boards): real examples exist (e.g. SimplifyJobs "Oracle Database
+# Research Intern" category=Software terms includes Winter/Spring 2027; JGCL
+# "CBAI Summer Research Fellowship in AI Safety '26" category=Research; JGCL
+# "Anthropic Fellows Program" category=Program; zshah101 "Research Intern -
+# School of Computer Science - LTI" (CMU) category=Software) — but every one
+# already matches under the existing rules: SimplifyJobs/zshah101 tag them
+# with a category already in categories/_ZSHAH101_CATEGORIES above, and JGCL's
+# matcher never gates on category at all. No fellowship/mentorship-shaped hits
+# turned up on the seeded Greenhouse/Ashby boards, and those two sources are
+# free-text term matching with no category gate to begin with. No matching
+# code needed — nothing here to extend yet.
+#
+# Pay is never a filter criterion anywhere in this pipeline — confirmed
+# 2026-07-26 by grepping core/filter.py for any pay/pay_per_week gate; none
+# exists. Don't add one; compensation is out of scope for Layer 2 eligibility.
 # Rejects a SimplifyJobs listing outright if any of these terms are present, even
 # alongside an allowed term (multi-term/rotational postings spanning both cycles).
 exclude_terms: ["Summer 2026", "Fall 2026", "Spring 2026"]
=== .github workflows ===
recheck.yml
run.yml
test.yml
.github/workflows/run.yml
.github/workflows/test.yml
.github/workflows/recheck.yml
  ```
- `Bash` — `cat .claude/settings.local.json
echo "=== run tests ==="
source .venv/bin/activate 2>/dev/null; python -m pytest -q 2>&1 | tail -20`
  ```
{
  "enabledMcpjsonServers": [
    "jarvis",
    "the-plan",
    "jarvis-fs",
    "the-plan-fs",
    "github"
  ]
}
=== run tests ===
........................................................................ [ 27%]
........................................................................ [ 55%]
........................................................................ [ 83%]
..........................................                               [100%]
258 passed in 2.30s
  ```
- `Bash` — `gh repo view gupta-builds/internship-research-loop --json name,defaultBranchRef 2>&1 | head -5
gh api user -q .login 2>&1`
  ```
{"defaultBranchRef":{"name":"master"},"name":"internship-research-loop"}
gupta-builds
  ```
- `ToolSearch` — `{"query":"select:TaskCreate,TaskUpdate","max_results":5}`
- `TaskCreate` — `{"subject":"Task A: promote-dossier skill","description":"Build .claude/skills/promote-dossier/ (SKILL.md + reference files): read dossier, ask target-folder + priority-override questions, invoke contact-researcher, show findings, write Program+Contact+Tracker notes on explicit consent only. State Jarvis-vault-checked-out-locally prerequisite. Write strict templates matching Program Template.md/Contact Template.md/pipeline doc's Tracker fields.","activeForm":"Building promote-dossier skill"}`
- `TaskCreate` — `{"subject":"Task B: contact-researcher subagent","description":"Build .claude/agents/contact-researcher.md: given company name, use enrich.py's widened Firecrawl scope (recruiter/HR/GitHub org/blog byline/LinkedIn search-snippet) to report real contact signal with source cited per item, or honestly report nothing found. Never fabricate.","activeForm":"Building contact-researcher agent"}`
- `TaskCreate` — `{"subject":"Task C: loop-verifier agent","description":"Build .claude/agents/loop-verifier.md: standalone health check of pipeline - test suite pass count, last N run.yml/recheck.yml results via gh api, vault dossier counts per priority folder vs run-log claims, seen_ids.json vs actual vault files divergence, auto-filed GitHub issues. Output: dated evidence-cited verdict.","activeForm":"Building loop-verifier agent"}`
- `TaskCreate` — `{"subject":"Task D: code-review skill/agent for this repo","description":"Pick skill vs agent (repo is ~1,500 lines, ~1:1 test ratio) and build it. Check proposed changes against: zero-LLM-in-unattended-path, permissive-by-default/explicit-negative-signal filter design, fail-closed write-gate ordering, every new rule cites real live data it was built from.","activeForm":"Building code-review skill/agent"}`
- `TaskCreate` — `{"subject":"Task E: .claude/settings.json + repo CLAUDE.md","description":"Tune permissions: pytest, git ops short of force-push/push to origin/master, gh read ops without prompting, explicit confirm still required for origin/master pushes and Actions secrets changes. Write repo CLAUDE.md documenting note-template contracts and when to use each skill/agent vs writing more Python.","activeForm":"Building settings.json and CLAUDE.md"}`
- `TaskCreate` — `{"subject":"Verification: test promote-dossier against a real dossier","description":"Actually invoke the skill flow (or as much as possible without a live Claude Code session invoking Skill tool recursively) against a real dossier file up to the write-consent gate. Report honestly whether it was run or only reviewed.","activeForm":"Verifying promote-dossier end-to-end"}`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/run_pipeline.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/filter.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/recheck.py`
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/core/git_ops.py`
- `Bash` — `ls state/ logs/ && echo "=== seen_ids sample ===" && head -c 300 state/seen_ids.json && echo && echo "=== runs.jsonl tail ===" && tail -3 logs/runs.jsonl 2>/dev/null
echo "=== workflows ===" && cat .github/workflows/run.yml`
  ```
logs/:
rechecks.jsonl
runs.jsonl

state/:
opt_cache.json
seen_ids.json
=== seen_ids sample ===
[
  "Greenhouse:8077685",
  "Greenhouse:8083292",
  "Jose-Gael-Cruz-Lopez:[REDACTED]",
  "Jose-Gael-Cruz-Lopez:[REDACTED]",
  "Jose-Gael-Cruz-Lopez:[REDACTED]",
  "Jose-Gael-Cruz-Lopez:[REDACTED]"
=== runs.jsonl tail ===
{"timestamp": "2026-07-25T14:55:10.343465+00:00", "fetch_counts": {"SimplifyJobs": 14766, "Jose-Gael-Cruz-Lopez": 112}, "filter_match_counts": {"SimplifyJobs": 35, "Jose-Gael-Cruz-Lopez": 5}, "new_count": 3, "already_seen_count": 37, "written_count": 0, "rejections": [{"uid": "SimplifyJobs:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir|forward deployed software engineer intern commercial"}, {"uid": "Jose-Gael-Cruz-Lopez:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}, {"uid": "Jose-Gael-Cruz-Lopez:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-07-25T15:57:16.062145+00:00", "fetch_counts": {"SimplifyJobs": 14766, "Jose-Gael-Cruz-Lopez": 112}, "filter_match_counts": {"SimplifyJobs": 35, "Jose-Gael-Cruz-Lopez": 5}, "new_count": 3, "already_seen_count": 37, "written_count": 0, "rejections": [{"uid": "SimplifyJobs:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir|forward deployed software engineer intern commercial"}, {"uid": "Jose-Gael-Cruz-Lopez:[REDACTED]", "check": "url_liveness", "reason": "HTTP 404"}, {"uid": "Jose-Gael-Cruz-Lopez:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}], "errors": [], "halted": false, "halt_reason": null}
{"timestamp": "2026-07-25T16:52:23.893535+00:00", "fetch_counts": {"SimplifyJobs": 14762, "Jose-Gael-Cruz-Lopez": 112, "vanshb03": 274, "zshah101": 214, "Greenhouse": 47, "Ashby": 2}, "filter_match_counts": {"SimplifyJobs": 35, "Jose-Gael-Cruz-Lopez": 5, "vanshb03": 85, "zshah101": 63, "Greenhouse": 31, "Ashby": 2}, "new_count": 184, "already_seen_count": 37, "deferred_count": 166, "written_count": 13, "rejections": [{"uid": "zshah101:greenhouse:pdtpartners:8077685", "check": "cross_source_duplicate", "reason": "company+title already in vault: pdt partners|summer 2027 software engineering intern"}, {"uid": "vanshb03:[REDACTED]", "check": "url_liveness", "reason": "HTTP 403"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|investment data science intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: walleye capital|risk technology analyst intern"}, {"uid": "vanshb03:[REDACTED]", "check": "cross_source_duplicate", "reason": "company+title already in vault: palantir technologies|software engineer intern"}], "errors": [], "halted": false, "halt_reason": null}
=== workflows ===
name: run
on:
  schedule:
    - cron: '0 * * * *'  # hourly to start — sources update ~30min, tighten later once a week of clean runs builds confidence
  workflow_dispatch: {}   # manual trigger, for verifying end-to-end before/while trusting the schedule

permissions:
  contents: write  # commit state/seen_ids.json + logs/runs.jsonl back to this repo
  issues: write    # gh issue create on schema-drift / push-failure / systemic write-gate rejection

jobs:
  pipeline:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout internship-research-loop
        uses: actions/checkout@v4

      - name: Checkout gupta-builds/Jarvis
        uses: actions/checkout@v4
        with:
          repository: gupta-builds/Jarvis
          token: ${{ secrets.JARVIS_PUSH_TOKEN }}
          path: jarvis-checkout
          fetch-depth: 0  # full history — a shallow clone can fail `git pull --rebase`
                          # if the vault's own auto-commit cycle has diverged by more than one commit

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install -r requirements.txt

      - name: Configure git identity
        run: |
          git config --global user.name "internship-research-loop bot"
          git config --global user.email "actions@users.noreply.github.com"

      - name: Run pipeline
        env:
          JARVIS_DIR: ${{ github.workspace }}/jarvis-checkout
          GH_TOKEN: ${{ github.token }}
          FIRECRAWL_API_KEY: ${{ secrets.FIRECRAWL_API_KEY }}  # discovery-time posting fetch; absent = thin dossiers, never a failure
        run: python run_pipeline.py
  ```
- `Bash` — `cat enrich.py
echo "=====VALIDATE====="
cat vault_writer/validate.py`
  ```
#!/usr/bin/env python3
"""Layer 5 — on-demand company/contact enrichment for one promoted dossier.

Run manually at Step 2 (Commit) of the vault's Internship Pipeline workflow —
deliberately NOT called from run_pipeline.py and never automatic on dossiers
the discovery loop writes:

    FIRECRAWL_API_KEY=... python enrich.py "<path to dossier .md>"

Public sources only: company site/blog scraped via Firecrawl, GitHub org
public members, blog author bylines, pattern-inferred first.last@domain
checked against the domain's MX records (DNS-over-HTTPS — no new dependency).
Hard line per the plan: no LinkedIn, no CAPTCHA bypass, no cookie injection,
no stealth browsing, no login walls. Anything behind one gets skipped.

No LLM call anywhere — scraped text is trimmed verbatim, never summarized.
"""
import os
import re
import sys
from datetime import date
from urllib.parse import urlparse

import requests
import yaml

FIRECRAWL = "https://api.firecrawl.dev/v1"
TIMEOUT = 30


def read_dossier(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        raise ValueError("no YAML frontmatter found — is this a dossier file?")
    return yaml.safe_load(m.group(1))


def replace_enrichment(text: str, section: str) -> str:
    """Idempotent: a re-run replaces the previous Enrichment section."""
    base = re.split(r"\n## Enrichment\b", text)[0].rstrip("\n")
    return base + "\n\n" + section


def _fc(path: str, payload: dict, key: str) -> dict:
    r = requests.post(f"{FIRECRAWL}/{path}", json=payload, timeout=TIMEOUT,
                      headers={"Authorization": f"Bearer {key}"})
    r.raise_for_status()
    return r.json()


def fc_search(query: str, key: str) -> list:
    return _fc("search", {"query": query, "limit": 5}, key).get("data", [])


def fc_scrape(url: str, key: str) -> str:
    data = _fc("scrape", {"url": url, "formats": ["markdown"]}, key).get("data", {})
    return data.get("markdown", "")


# Confirmed live 2026-07-26: simplify.jobs is a real, live site (SimplifyJobs'
# own job board, separate from their GitHub feed) — resolves 200. A search
# hit landing on any of these domains is noise, not a real contact.
_EXCLUDED_CONTACT_DOMAINS_RE = re.compile(
    r"indeed\.com|glassdoor\.com|simplify\.jobs|linkedin\.com/jobs/", re.I,
)


def _search_and_filter(query: str, key: str) -> list:
    return [h for h in fc_search(query, key) if not _EXCLUDED_CONTACT_DOMAINS_RE.search(h.get("url", ""))]


def linkedin_recruiter_snippet(company: str, key: str) -> list:
    # Search-snippet text only — NEVER fc_scrape() or otherwise fetch the
    # underlying linkedin.com URL; that crosses the "no LinkedIn... no login
    # walls" line in this module's docstring above. Whatever text Firecrawl's
    # search-result snippet itself contains (title/description fields,
    # confirmed live 2026-07-26 — a real hit returned "Katie Nielsen - Senior
    # Recruiter at Anduril Industries" as its title) is all we ever see.
    hits = fc_search(f"site:linkedin.com {company} recruiter", key)
    return [(h.get("title", ""), h.get("description", ""), h.get("url", ""))
            for h in hits if "linkedin.com" in h.get("url", "")]


def trim(md: str, limit: int = 800) -> str:
    # ponytail: naive trim keeps nav/link junk at the top of some pages —
    # good enough to orient a human; add a boilerplate stripper if it annoys.
    return re.sub(r"\s+", " ", md).strip()[:limit]


BYLINE_RE = re.compile(r"\b[Bb]y[: ]+\[?([A-Z][a-z]+ [A-Z][a-z]+(?:-[A-Z][a-z]+)?)\]?")


def extract_bylines(md: str) -> list:
    return sorted(set(BYLINE_RE.findall(md)))


def github_org_members(company: str) -> tuple:
    """Best-match public GitHub org and up to 5 public members. Unauthenticated
    (60 req/hr is plenty for an on-demand tool); uses GITHUB_TOKEN if set."""
    h = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        h["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    r = requests.get("https://api.github.com/search/users",
                     params={"q": f"{company} type:org", "per_page": 1},
                     headers=h, timeout=TIMEOUT)
    if r.status_code != 200 or not r.json().get("items"):
        return None, []
    org = r.json()["items"][0]["login"]
    r = requests.get(f"https://api.github.com/orgs/{org}/public_members",
                     params={"per_page": 5}, headers=h, timeout=TIMEOUT)
    members = []
    for m in (r.json() if r.status_code == 200 else []):
        detail = requests.get(m["url"], headers=h, timeout=TIMEOUT).json()
        members.append((detail.get("name") or m["login"], m["html_url"]))
    return org, members


def mx_ok(domain: str) -> bool:
    """MX lookup via DNS-over-HTTPS — validates the domain accepts mail,
    not that the specific inferred address exists."""
    try:
        r = requests.get("https://dns.google/resolve",
                         params={"name": domain, "type": "MX"}, timeout=TIMEOUT)
        return bool(r.json().get("Answer"))
    except requests.RequestException:
        return False


def infer_email(name: str, domain: str):
    parts = re.sub(r"[^a-z \-]", "", name.lower()).replace("-", "").split()
    if len(parts) < 2 or not domain:
        return None
    return f"{parts[0]}.{parts[-1]}@{domain}"


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    key = os.environ.get("FIRECRAWL_API_KEY")
    if not key:
        sys.exit("FIRECRAWL_API_KEY is not set — get one at firecrawl.dev and "
                 "export it before running.")
    path = sys.argv[1]
    text = open(path, encoding="utf-8").read()
    company = read_dossier(text)["company"]
    print(f"Enriching {company} …")

    sources, contacts = [], []
    site_url = about = blog_url = ""
    hits = fc_search(f"{company} official site", key)
    if hits:
        site_url = hits[0]["url"]
        sources.append(site_url)
        about = trim(fc_scrape(site_url, key))
    domain = urlparse(site_url).netloc.removeprefix("www.") if site_url else ""

    for hit in fc_search(f"{company} engineering blog", key):
        if re.search(r"blog|engineering|tech", hit["url"], re.I):
            blog_url = hit["url"]
            sources.append(blog_url)
            for name in extract_bylines(fc_scrape(blog_url, key)):
                contacts.append((name, f"blog byline ({blog_url})"))
            break

    org, members = github_org_members(company)
    if org:
        sources.append(f"https://github.com/orgs/{org}/people")
        contacts += [(n, u) for n, u in members]

    for query, label in ((f"{company} recruiter", "recruiter search"),
                         (f"{company} university recruiting", "university recruiting search")):
        for hit in _search_and_filter(query, key):
            name = hit.get("title", "").strip()
            if name:
                contacts.append((name, f"{label}: {hit['url']}"))
                sources.append(hit["url"])

    for name, snippet, url in linkedin_recruiter_snippet(company, key):
        if name:
            contacts.append((name, f"linkedin search snippet: {snippet or url}"))
            sources.append(url)

    mx = mx_ok(domain) if domain else False
    rows = []
    for name, src in contacts:
        email = infer_email(name, domain)
        rows.append(f"| {name} | {src} | {email or '—'} | "
                    f"{'✓' if email and mx else '—'} |")

    today = date.today().isoformat()
    section = "\n".join(
        [f"## Enrichment ({today})",
         f"- **Site:** {site_url or 'not found'}",
         f"- **About (scraped, verbatim):** {about or '—'}",
         f"- **Engineering blog:** {blog_url or 'not found'}",
         f"- **GitHub org:** {f'https://github.com/{org}' if org else 'not found'}",
         f"- **Email domain MX:** {'valid' if mx else 'no MX record found — inferred emails unvalidated'}",
         "", "### Contacts (public sources only — verify before sending anything)",
         "| Name | Source | Inferred email | MX |", "| --- | --- | --- | --- |"]
        + (rows or ["| — | none found | — | — |"])
        + ["", "### Sources"] + [f"- {s}" for s in sources]) + "\n"

    open(path, "w", encoding="utf-8").write(replace_enrichment(text, section))
    print(f"Wrote Enrichment section: {len(contacts)} contact(s), "
          f"{len(sources)} source(s) → {path}")


if __name__ == "__main__":
    main()
=====VALIDATE=====
"""Layer 4 — the five-check write gate. Fail any check -> item is rejected and
never touches the vault (fail-closed). Each check is independently callable so
run.yml can log which specific check rejected an item and why.
"""
from dataclasses import dataclass

import requests
import yaml

from core.identity import cross_source_key

REQUIRED_LISTING_FIELDS = ("company", "title", "url", "source", "uid")
REQUIRED_FRONTMATTER_FIELDS = (
    "company", "title", "url", "source", "terms", "locations",
    "target_year", "date_posted", "date_found", "matched_reason", "status", "next", "tags",
)


@dataclass
class ValidationResult:
    passed: bool
    check: str = ""
    reason: str = ""


class _DupeKeyLoader(yaml.SafeLoader):
    """Like SafeLoader, but raises on duplicate mapping keys instead of
    silently keeping the last one — plain safe_load can't detect this."""


def _construct_mapping_no_dupes(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise ValueError(f"duplicate frontmatter key: {key!r}")
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


_DupeKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping_no_dupes
)


def check_required_fields(listing, uid: str) -> ValidationResult:
    values = {"uid": uid, **{f: getattr(listing, f) for f in REQUIRED_LISTING_FIELDS if f != "uid"}}
    missing = [name for name in REQUIRED_LISTING_FIELDS if not values[name]]
    if missing:
        return ValidationResult(False, "required_fields", f"missing/empty: {', '.join(missing)}")
    return ValidationResult(True, "required_fields")


def check_url_live(url: str, http_head=None, timeout: int = 10) -> ValidationResult:
    try:
        resp = (http_head or requests.head)(url, timeout=timeout, allow_redirects=True)
    except requests.RequestException as exc:
        return ValidationResult(False, "url_liveness", f"request failed: {exc}")
    if 200 <= resp.status_code < 400:
        return ValidationResult(True, "url_liveness")
    return ValidationResult(False, "url_liveness", f"HTTP {resp.status_code}")


def check_not_duplicate(uid: str, seen_ids) -> ValidationResult:
    if uid in seen_ids:
        return ValidationResult(False, "not_duplicate", f"uid already seen: {uid}")
    return ValidationResult(True, "not_duplicate")


def check_cross_source_duplicate(listing, dossier_keys) -> ValidationResult:
    """Same program via two sources = two different uids but one normalized
    company+title key (MLH Fellowship landed twice pre-cleanup). Routine
    rejection, not systemic — first source in write order wins."""
    key = cross_source_key(listing.company, listing.title)
    if key in dossier_keys:
        return ValidationResult(False, "cross_source_duplicate", f"company+title already in vault: {key}")
    return ValidationResult(True, "cross_source_duplicate")


def check_format_compliance(markdown: str) -> ValidationResult:
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return ValidationResult(False, "format_compliance", "does not start with frontmatter '---'")

    try:
        closing_idx = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return ValidationResult(False, "format_compliance", "no closing frontmatter '---' found")

    frontmatter_text = "\n".join(lines[1:closing_idx])
    try:
        frontmatter = yaml.load(frontmatter_text, Loader=_DupeKeyLoader) or {}
    except ValueError as exc:
        return ValidationResult(False, "format_compliance", str(exc))
    except yaml.YAMLError as exc:
        return ValidationResult(False, "format_compliance", f"frontmatter is not valid YAML: {exc}")

    missing = [f for f in REQUIRED_FRONTMATTER_FIELDS if f not in frontmatter]
    if missing:
        return ValidationResult(False, "format_compliance", f"frontmatter missing fields: {', '.join(missing)}")

    body_lines = lines[closing_idx + 1:]
    if not body_lines or body_lines[0].strip() == "":
        return ValidationResult(False, "format_compliance", "blank line between frontmatter close and title")
    if not body_lines[0].lstrip().startswith("#"):
        return ValidationResult(False, "format_compliance", "no '#' title immediately after frontmatter")

    for i, line in enumerate(body_lines):
        if line.strip() == "---":
            return ValidationResult(False, "format_compliance", "'---' used as a body separator")
        if line.strip() == "":
            prev = body_lines[i - 1].strip() if i > 0 else ""
            if not (prev.startswith(">")):
                return ValidationResult(False, "format_compliance", f"disallowed blank line at body line {i}")

    if body_lines and body_lines[-1].strip() == "":
        return ValidationResult(False, "format_compliance", "trailing blank line at end of file")

    return ValidationResult(True, "format_compliance")


def validate(listing, uid: str, markdown: str, seen_ids, http_head=None, dossier_keys=frozenset()) -> ValidationResult:
    """Runs all checks in the plan's order, fail-closed on the first failure.
    Short-circuits for real (no HEAD request if required fields are already
    missing) — each check only runs once the previous one has passed.
    cross_source_duplicate runs before url_liveness: it's free, the HEAD
    request isn't."""
    result = check_required_fields(listing, uid)
    if not result.passed:
        return result
    result = check_not_duplicate(uid, seen_ids)
    if not result.passed:
        return result
    result = check_cross_source_duplicate(listing, dossier_keys)
    if not result.passed:
        return result
    result = check_url_live(listing.url, http_head=http_head)
    if not result.passed:
        return result
    result = check_format_compliance(markdown)
    if not result.passed:
        return result
    return ValidationResult(True)
  ```
- `Bash` — `find ~/.claude/skills -maxdepth 2 -iname "SKILL.md" | head -5
echo "---"
cat ~/.claude/skills/graphify/SKILL.md 2>/dev/null | head -40
echo "=== any local project skill examples elsewhere on disk? ==="
find / -maxdepth 6 -path "*/.claude/skills/*/SKILL.md" 2>/dev/null | grep -v "^/home/anant_gupta/.claude/skills" | head -10`
  ```
/home/anant_gupta/.claude/skills/sandbox-sdk/SKILL.md
/home/anant_gupta/.claude/skills/web-perf/SKILL.md
/home/anant_gupta/.claude/skills/agents-sdk/SKILL.md
/home/anant_gupta/.claude/skills/turnstile-spin/SKILL.md
/home/anant_gupta/.claude/skills/wrangler/SKILL.md
---
---
name: graphify
description: "any input (code, docs, papers, images, videos) to knowledge graph. Use when user asks any question about a codebase, documents, or project content - especially if graphify-out/ exists, treat the question as a /graphify query."
trigger: /graphify
---

# /graphify

Turn any folder of files into a navigable knowledge graph with community detection, an honest audit trail, and three outputs: interactive HTML, GraphRAG-ready JSON, and a plain-language GRAPH_REPORT.md.

## Usage

```
/graphify                                             # full pipeline on current directory → Obsidian vault
/graphify <path>                                      # full pipeline on specific path
/graphify https://github.com/<owner>/<repo>           # clone repo then run full pipeline on it
/graphify https://github.com/<owner>/<repo> --branch <branch>  # clone a specific branch
/graphify <url1> <url2> ...                           # clone multiple repos, build each, merge into one cross-repo graph
/graphify <path> --mode deep                          # thorough extraction, richer INFERRED edges
/graphify <path> --update                             # incremental - re-extract only new/changed files
/graphify <path> --directed                            # build directed graph (preserves edge direction: source→target)
/graphify <path> --whisper-model medium                # use a larger Whisper model for better transcription accuracy
/graphify <path> --cluster-only                       # rerun clustering on existing graph
/graphify <path> --no-viz                             # skip visualization, just report + JSON
/graphify <path> --html                               # (HTML is generated by default - this flag is a no-op)
/graphify <path> --svg                                # also export graph.svg (embeds in Notion, GitHub)
/graphify <path> --graphml                            # export graph.graphml (Gephi, yEd)
/graphify <path> --neo4j                              # generate graphify-out/cypher.txt for Neo4j
/graphify <path> --neo4j-push bolt://localhost:7687   # push directly to Neo4j
/graphify <path> --mcp                                # start MCP stdio server for agent access
/graphify <path> --watch                              # watch folder, auto-rebuild on code changes (no LLM needed)
/graphify <path> --wiki                               # build agent-crawlable wiki (index.md + one article per community)
/graphify <path> --obsidian --obsidian-dir ~/vaults/my-project  # write vault to custom path (e.g. existing vault)
/graphify add <url>                                   # fetch URL, save to ./raw, update graph
/graphify add <url> --author "Name"                   # tag who wrote it
/graphify add <url> --contributor "Name"              # tag who added it to the corpus
/graphify query "<question>"                          # BFS traversal - broad context
/graphify query "<question>" --dfs                    # DFS - trace a specific path
/graphify query "<question>" --budget 1500            # cap answer at N tokens
/graphify path "AuthModule" "Database"                # shortest path between two concepts
=== any local project skill examples elsewhere on disk? ===
  ```
- `Bash` — `find ~/.claude/agents -maxdepth 1 -iname "*.md" 2>/dev/null | head -5
find / -maxdepth 8 -path "*/.claude/agents/*.md" 2>/dev/null | grep -v "^/home/anant_gupta/.claude/agents" | head -10
echo "=== check plugin agents for example frontmatter ==="
find / -path "*agents*" -iname "*.md" 2>/dev/null | grep -iv "node_modules\|/.venv/\|/.git/" | grep -i "code-reviewer\|explore" | head -10`
  ```
Command did not complete within its 120s timeout and was moved to the background (ID: b0w0wai02). Output is being written to: /tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/tasks/b0w0wai02.output. You will be notified when it completes. To check interim output, use Read on that file path.
  ```
- `Bash` — `find /home/anant_gupta -maxdepth 10 -path "*/.claude/agents/*.md" 2>/dev/null | head -20`
  ```
/home/anant_gupta/.claude/agents/obsidian-session-archivist.md
/home/anant_gupta/.claude/agents/obsidian-architect.md
/home/anant_gupta/.claude/agents/obsidian-researcher.md
/home/anant_gupta/projects/ai/claude/second-brain-claudekit/.claude/agents/weekly-reviewer.md
/home/anant_gupta/projects/ai/claude/second-brain-claudekit/.claude/agents/vault-curator.md
/home/anant_gupta/projects/ai/claude/second-brain-claudekit/.claude/agents/research-distiller.md
/home/anant_gupta/projects/hub/portfolio/.claude/agents/sanity-schema.md
/home/anant_gupta/projects/hub/portfolio/.claude/agents/eval-runner.md
/home/anant_gupta/projects/hub/portfolio/.claude/agents/three-artist.md
/home/anant_gupta/projects/hub/portfolio/.claude/agents/security-reviewer.md
/home/anant_gupta/projects/hub/portfolio/.claude/agents/test-runner.md
/home/anant_gupta/projects/hub/portfolio/.claude/agents/ai-engineer.md
/home/anant_gupta/projects/hub/portfolio/.claude/agents/frontend-builder.md
/home/anant_gupta/projects/hub/CausalOps/.claude/agents/coordinator-expert.md
/home/anant_gupta/projects/hub/CausalOps/.claude/agents/memory-layer-specialist.md
/home/anant_gupta/projects/hub/CausalOps/.claude/agents/causal-safeguard-reviewer.md
/home/anant_gupta/projects/hub/tradingview/.claude/agents/guardrail-auditor.md
/home/anant_gupta/projects/hub/tradingview/.claude/agents/spec-implementer.md
  ```
- `Read` — `/home/anant_gupta/projects/hub/portfolio/.claude/agents/security-reviewer.md`
- `Read` — `/home/anant_gupta/.claude/agents/obsidian-researcher.md`
- `TaskUpdate` — `{"taskId":"2","status":"in_progress"}`
- `Bash` — `mkdir -p .claude/agents .claude/skills/promote-dossier/reference .claude/skills/review-loop-change`
  ```
(Bash completed with no output)
  ```
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/agents/contact-researcher.md`
  ```
---
name: contact-researcher
description: Given a company name, finds real, sourced contact signal (recruiter, HR, engineering-blog byline, GitHub org member, LinkedIn search-snippet hit) using this repo's enrich.py. Never fabricates a plausible-sounding contact — reports "nothing found" honestly when that's the real outcome. Invoked by the promote-dossier skill at Step 3 (Commit); can also be called standalone for one company.
tools: Bash, Read
---

You research **one company's** real, public contact signal for the internship-research-loop pipeline. You are the exploratory step in an otherwise deterministic pipeline (see `core/filter.py`, `core/relevance.py`, `core/classify.py` — all zero-LLM, keyword-based) — that is exactly why this step is a subagent instead of a script. Your only job is to look, and to say precisely what you found and where it came from.

## The one rule that overrides everything else

**A wrong guess here is worse than an empty result.** If you are not looking at an actual name, title, or byline that a real tool call returned, do not report it. Never infer a plausible name from a company's size or industry. Never invent an email address that "looks right." Never present a guess as a finding. If nothing real turns up, say so — "nothing found" is a valid, complete, honest answer and is the expected outcome for most small/private companies.

## What you have available

This repo's `enrich.py` (repo root) already implements every legitimate search surface this pipeline is allowed to use. Read it first if you haven't — don't reimplement its logic from scratch. Reuse its functions directly via `python3 -c` or a short inline script:

- `fc_search(query, key)` — Firecrawl web search, returns `[{title, description, url}, ...]`
- `github_org_members(company)` — best-match public GitHub org + up to 5 public members
- `linkedin_recruiter_snippet(company, key)` — **search-snippet text only**, via `site:linkedin.com {company} recruiter`. This function deliberately never calls `fc_scrape()` on a linkedin.com URL and neither should you — that crosses the vault's hard line (see below).
- `mx_ok(domain)` / `infer_email(name, domain)` — only meaningful once you have a real name and a real company domain

`FIRECRAWL_API_KEY` must be set in the environment for any of this to work (`echo $FIRECRAWL_API_KEY | cut -c1-4` to sanity-check without printing the whole key — do not print secrets to output). If it is unset, stop and report that plainly instead of silently returning nothing (an empty key and an empty result look identical to a caller unless you say which one happened).

Example invocation pattern:
```bash
python3 -c "
import os, sys
sys.path.insert(0, '.')
from enrich import fc_search, github_org_members, linkedin_recruiter_snippet
key = os.environ['FIRECRAWL_API_KEY']
company = '<company>'
print(fc_search(f'{company} recruiter', key))
print(github_org_members(company))
print(linkedin_recruiter_snippet(company, key))
"
```

## Hard line (non-negotiable, inherited from enrich.py's own docstring)

Public sources only. No LinkedIn scraping, no CAPTCHA bypass, no cookie injection, no stealth browsing, no login walls. If a search result lands behind one of these, skip it — do not try to work around it, do not ask the user to paste in cookies, do not use a browser tool to load a login-walled page. This line existed before you and is not yours to renegotiate; if a technique feels borderline, stop and flag it in your output rather than trying it.

No LLM-generated content stands in for a real finding: you may use your own reasoning to decide *which* search queries to run and to filter obvious noise (job-board mirrors, `indeed.com`, `glassdoor.com`, `simplify.jobs` — see `enrich.py`'s `_EXCLUDED_CONTACT_DOMAINS_RE`), but every name, title, or snippet you report must trace back to an actual tool-call result, never to your own inference about what a recruiter at that company is probably named.

## What to look for, and how to report each

Search across all of these; report each independently, with its source:

1. **Recruiter / university recruiting search hits** — `fc_search(f"{company} recruiter")` and `fc_search(f"{company} university recruiting")`, filtered through the same excluded-domain list `enrich.py` uses.
2. **Engineering blog byline** — a company eng/tech blog with an author name on a real post.
3. **GitHub org public member** — `github_org_members(company)`.
4. **LinkedIn search-snippet hit** — `linkedin_recruiter_snippet(company, key)`. Report the snippet text and URL, never the profile content itself (you never fetched it).

For each hit, report: **name/title found → source URL → which query surfaced it**. If a category turned up nothing, say "nothing found" for that category explicitly — don't just omit it silently, since a silent omission reads as "not checked" rather than "checked, empty."

## Output format

```
## Contact research: <Company>

### Recruiter / university recruiting search
- <name/title> — <url> (query: "<company> recruiter")
  -- or --
- nothing found

### Engineering blog byline
- <name> — <blog post url>
  -- or --
- nothing found

### GitHub org
- org: <github.com/orgs/<org>>
  - <name or login> — <profile url>
  -- or --
- no matching public org found

### LinkedIn search-snippet
- "<exact snippet text>" — <url> (search-snippet only, not scraped)
  -- or --
- nothing found

### Notes
Anything borderline you skipped and why (e.g. a hit that required a login wall).
```

Return this as your final message — it is read programmatically by the skill that invoked you, not narrated to a human directly, so keep it in this exact structure and do not add conversational filler before or after it.

  ```
- `TaskUpdate` — `{"taskId":"2","status":"completed"}`
- `TaskUpdate` — `{"taskId":"1","status":"in_progress"}`
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/reference/note-templates.md`
  ```
# promote-dossier note templates

These are the **only** three note shapes `/promote-dossier` is allowed to write. They are strict contracts, not starting points — every field listed as required below must be present on every note this skill writes, even when the value is genuinely empty (use `null` / `[]`, never omit the key). This mirrors `vault_writer/validate.py`'s `REQUIRED_FRONTMATTER_FIELDS` fail-closed pattern in this repo: a missing required field is a bug, not a stylistic choice.

Field names below are copied verbatim from the vault's own templates — `30_Order/Templates/Career/Program Template.md` and `30_Order/Templates/Career/Contact Template.md` — read directly from the Jarvis vault on 2026-07-26. **Tracker/Each One has no pre-existing template in the vault** (only `Tracker/Internship - Dashboard.md` and `Tracker/Tracker.md` exist, both roll-up views, not per-item notes); its shape below is authored from `30_Order/Workflows/Internship Pipeline.md`'s own field description ("noted/researched/created/applied/result, deadline, contact link, related notes, url") since there was nothing existing to copy. If a real Tracker/Each One template later gets added to the vault, this skill should switch to it instead of its own.

**Filename convention**, all three note types: `<Role> - <Company>.md`, same sanitization as `vault_writer/writer.py`'s `dossier_filename()` (strip `\/:*?"<>|` and control chars — the vault lives on a Windows-mounted drive) and the real hand-renamed example already in the vault, `Programs/Serious/Software Engineer - Ellipsis Labs.md`'s dossier counterpart. Collision handling: append ` (2)`, ` (3)`, ... same as dossiers.

**Folder existence as of 2026-07-26** (checked live via the `jarvis` MCP tools): `Programs/Serious/` exists (1 note in it). `Programs/Considering/`, `Contacts/Each One/`, and `Tracker/Each One/` do **not** exist yet — nothing has ever promoted into them. Creating a missing folder is part of the write step itself (it happens only after explicit go-ahead, same as the notes) — never create it speculatively before the human has said yes.

---

## 1. Program note

Path: `10_Areas/Career/Internships/Programs/Serious/<Role> - <Company>.md` or `.../Considering/<Role> - <Company>.md` (per the human's answer to question (a)).

```yaml
---
name:                # "<Role> at <Company>" — human-readable, not the filename
company:
program_type:        # e.g. "Software", "Quant", "Research" — from the dossier's category/classification bucket
eligible_classes: []  # from dossier target_year if present, else []
grad_year:            # leave null unless the dossier states one explicitly — don't infer
role_type: internship
wave:                 # null unless known
opens_date:           # null unless known
deadline_posted:      # from dossier content if stated, else null
deadline_real:        # null unless independently confirmed — never assume posted == real
pay_per_week:         # null unless stated
pay_currency: USD
duration_weeks:       # null unless stated
benefits: []
application_url:      # dossier's url field
careers_page:         # null unless found during contact research
list_origin: "[[10_Areas/Career/Internships/List/Dossiers/<bucket-folder>/<dossier-filename>]]"
applying_note: null   # Step 4 hasn't happened yet — this skill never creates an Applying note
recruiter_contact: "[[10_Areas/Career/Internships/Contacts/Each One/<Role> - <Company>]]"
tags:
  - internship
  - program
---
```

Required fields, always present: every key listed above. Body sections, verbatim structure from the vault's own `Program Template.md` (do not invent new headings):

```markdown
# <Role> — <Company>
Static research only — comp, eligibility, deadlines, traps, prep. Live status (applied, interview, offer) lives on the matching note in `20_Progress/Internship/Applying/`, linked via `applying_note` above.
## Program Overview
What the role is, who runs it, what makes it worth the hours to prepare for. (pull from the dossier's posting content)
## Eligibility
Who can apply, what year/major requirement, and anything that disqualifies you before you start.
## Traps & Gotchas
> [!WARNING]
> The thing most applicants get wrong about this program. (only include real traps found in the dossier/enrichment — never invent one)
## Prep Checklist
- [ ]
## Related Resources
- [[<dossier note>]] (List/Dossiers origin)
```

**Do not** write a `status` or `next` field on the Program note — the pipeline doc is explicit that Program notes are durable/static and only change when a fact about the program itself changes; funnel status belongs on the (not-yet-created) Applying note or the Tracker note.

---

## 2. Contact note

Path: `10_Areas/Career/Internships/Contacts/Each One/<Role> - <Company>.md` — company-level research, filed under the same `<Role> - <Company>` name as the Program note it's paired with (not the contact person's own name — one company can have several people found, the note is about the company relationship, matching the pipeline doc's "company-level contact research").

```yaml
---
type: contact
name:                 # the PRIMARY contact person's name, if contact-researcher found exactly one strong hit — else null
role:                 # that person's title (e.g. "Senior Recruiter") — else null
company:
linkedin_url:         # only if contact-researcher returned a linkedin.com URL as a source — else null
email:                # only a contact-researcher/enrich.py-inferred address with a real MX record — else null
how_found:            # cite the actual query/source, e.g. "linkedin search snippet: site:linkedin.com <company> recruiter"
relationship: cold
related_programs:
  - "[[10_Areas/Career/Internships/Programs/<Serious|Considering>/<Role> - <Company>]]"
last_contact_date: null
tags:
  - contact
next: null
---
```

Required fields, always present: every key listed above (`null`/`cold`/`[]` are valid values, omission is not). Body, verbatim structure from `Contact Template.md`:

```markdown
# <Role> — <Company>
## Facts
Everything contact-researcher actually returned, with its source cited per item — see "How this section gets filled" below. If it found nothing, say so explicitly: "No public contact signal found as of <date>." Never pad this section with a guess.
## Current Draft
The live, unsent message to this person right now. Build it from [[Mimic]] and edit until it sounds like you, not the template. Leave this section empty (just the heading) if no contact was found — there is no one to draft to yet.
## Conversation Log
Dated entries, newest at the bottom.
- **<today's date, YYYY-MM-DD>:** Note created via /promote-dossier.
## Next Action
The single next move — send, follow up, or wait. If nothing was found: "Recheck contact research once <company>'s public presence changes, or apply cold through the portal."
```

**How this section gets filled**: paste the contact-researcher subagent's structured output (recruiter/university-recruiting hits, engineering-blog byline, GitHub org member, LinkedIn search-snippet — each with its source) into Facts verbatim, one bullet per finding, source in parentheses. Do not summarize away the source citation — the whole point of this note is that every claim in it traces back to something real.

---

## 3. Tracker/Each One note

Path: `10_Areas/Career/Internships/Tracker/Each One/<Role> - <Company>.md`. Created only once the Program note exists (same commit/sitting), per pipeline Step 3.

```yaml
---
type: tracker
program: "[[10_Areas/Career/Internships/Programs/<Serious|Considering>/<Role> - <Company>]]"
contact: "[[10_Areas/Career/Internships/Contacts/Each One/<Role> - <Company>]]"
company:
url:                  # dossier's application_url, duplicated here per the pipeline doc's explicit field list
date_noted:           # the dossier's own date_found field
date_researched:       # today — the date this promotion actually happened
date_created: null    # filled in once/if an Applying note is created (Step 4)
date_applied: null
date_result: null
result: null
deadline: null         # mirrors Program note's deadline_real once known; null until then
related_notes:
  - "[[10_Areas/Career/Internships/List/Dossiers/<bucket-folder>/<dossier-filename>]]"
tags:
  - internship
  - tracker
next: null
---
```

Required fields, always present: every key listed above. Body:

```markdown
# <Role> — <Company>
The dated index for this internship — source of truth for "where does this stand" until an Applying note exists (see [[30_Order/Workflows/Internship Pipeline]] Step 8).
## Timeline
- **Noted:** <date_noted>
- **Researched:** <date_researched>
- **Created:** —
- **Applied:** —
- **Result:** —
## Next Action
The single next move. Mirrors `next:` above.
```

Do not add a Dataview query or dashboard block to this note — those already exist at `Tracker/Internship - Dashboard.md` and `Tracker/Tracker.md`; duplicating them here is exactly the kind of redundant note the pipeline doc's Step 8 explicitly warns against ("not a replacement for the Dashboard or Kanban").

---

## Cross-linking summary (all three notes, written together, in one sitting)

- Program `list_origin` → dossier note
- Program `recruiter_contact` → Contact note
- Contact `related_programs` → Program note (back-link)
- Tracker `program` → Program note
- Tracker `contact` → Contact note
- Tracker `related_notes` → dossier note

No other cross-link fields exist in the vault's current templates for this step — don't invent a `tracker_note` field on the Program note or a `program` field on the dossier; if a future session needs one, that's a vault-template change to propose explicitly, not something this skill should add silently.

  ```
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/SKILL.md`
  ```
---
name: promote-dossier
description: "Turns one internship-research-loop dossier into a Program note + Contacts/Each One note + Tracker/Each One note in the Jarvis vault, with manual consent required before any write. Use when the user wants to promote/commit a dossier from List/Dossiers into the real pipeline (Internship Pipeline.md Step 3)."
trigger: /promote-dossier
---

# /promote-dossier

Promotes one dossier from `List/Dossiers/` (auto-written by this repo's discovery loop) into `Programs/`, `Contacts/Each One/`, and `Tracker/Each One/` — Step 3 ("Commit") of the Jarvis vault's `30_Order/Workflows/Internship Pipeline.md`. This is a human-in-the-loop step: it never writes anything without an explicit go-ahead, and it never invents a fact it can't source.

## Prerequisite — read this before running

**This skill needs a session with both this repo and the Jarvis vault (`gupta-builds/Jarvis`) present in the same working environment.** This repo's own automation (`run_pipeline.py`, `recheck.py`) never touches the vault interactively — it writes once, non-interactively, via a scoped PAT in CI. This skill is the opposite shape: a human reviewing real findings before a write happens, which means it needs to actually read and write vault files directly, not through a second automated writer.

Two ways that access can exist, and this skill works with either — but do not assume either one silently, check first:

1. **Git checkout, sibling to this repo** — the layout this repo's own code already expects (`run_pipeline.py`'s `JARVIS_DIR` env var, same pattern as `jarvis-checkout/` in CI). Expected layout:
   ```
   internship-research-loop/     <- this repo
   Jarvis/                       <- gupta-builds/Jarvis, checked out alongside it
   ```
   If this is how the vault is reachable, use plain `Read`/`Edit`/`Write` on paths under `../Jarvis/` (or wherever it's actually checked out — ask if it's not obviously sibling), and use `git status`/`git diff` in that checkout before committing so the human can see exactly what's about to be written, same review discipline as any other repo.
2. **Obsidian MCP tools** (`jarvis`, `jarvis-fs` in this session's `.claude/settings.json` — confirmed connected in this repo as of 2026-07-26) — if Obsidian is running locally with its Local REST API plugin enabled, `mcp__jarvis__vault_read` / `vault_write` / `vault_patch` reach the live vault directly. This is what was actually used to verify this skill's templates against the real vault. It does not require a separate git checkout, but it does require Obsidian to actually be open with that plugin active — don't assume it's connected just because the tools are listed; call `mcp__jarvis__vault_list` first and confirm it returns real vault content before proceeding.

If neither is available, **stop and tell the user** — don't guess at paths or fabricate vault content from memory of what this document says the vault contains.

**Do not attempt to write across the two repos via the GitHub API** (`mcp__github__create_or_update_file` etc.) as a substitute for either path above. `core/git_ops.py` in this repo exists specifically to solve the two-writer collision problem (this pipeline's own CI + the vault's own independent auto-commit cycle) for the one automated writer this pipeline has. Adding a second interactive writer that pushes through a different mechanism (the API instead of a local checkout + normal git) reintroduces exactly that race with no equivalent retry/rebase handling. If you find yourself reaching for the GitHub API here, stop — that's a sign this prerequisite isn't actually met, not a reason to route around it.

## Note templates

Read `reference/note-templates.md` before writing anything — it has the exact, required frontmatter for all three note types (Program, Contact, Tracker/Each One), copied from the vault's own `Program Template.md` / `Contact Template.md` where those exist, and authored from `Internship Pipeline.md`'s own field description where (Tracker/Each One) no template exists yet. These are enforced contracts, not loose guidance — every required field must be present on every note, even as `null`.

## Steps

### 1. Take the input
Accept a dossier file path, or a company/title to search for under `List/Dossiers/` (recursively — dossiers are sorted into priority-bucket subfolders `1 - AI & ML/`, `2 - Fullstack/`, `3 - CyS & Finance/`, `Other/`, per `core/classify.py`'s `BUCKET_FOLDERS`). Read the dossier's frontmatter and body, including its classification callout (the `> [!NOTE] <bucket>: ...` line in the body — dossiers don't carry a `category` frontmatter field, per `vault_writer/writer.py`'s `build_frontmatter()`, so the callout text and the folder it's filed under are the only record of the auto-assigned bucket).

### 2. Ask two concrete questions
Use `AskUserQuestion` with exactly these two questions — not open-ended prose:

- **(a) Target folder**: `Programs/Serious/` or `Programs/Considering/`. Per the pipeline doc, this is a preference/timing split only, never a rigor split — don't imply one is a lesser commitment than the other in how you phrase it. No default is auto-derivable here (nothing upstream computes "serious vs. considering"), so present both options on equal footing.
- **(b) Priority/category override**: state the dossier's auto-assigned bucket (from the classification callout / folder) as the **default answer**, and offer "keep as classified" alongside an explicit override option (with the three other buckets as alternatives, or "Other"). Don't force the human to retype the bucket name if they're keeping it — "keep as classified" should be a single selectable option, not something they have to spell out.

### 3. Invoke contact research and show findings — before writing anything
Launch the `contact-researcher` subagent (`.claude/agents/contact-researcher.md`) with the dossier's company name. Its job is exploratory — real, sourced findings or an honest "nothing found," never a guess — which is exactly why it's a subagent here rather than a script (see that file's own docstring for why). Do not call `enrich.py`'s `main()` CLI directly from this skill: that function writes an "## Enrichment" section straight into the dossier file as a side effect the moment it runs, which would be exactly the silent, pre-consent write this skill exists to avoid. The subagent uses `enrich.py`'s underlying functions (`fc_search`, `github_org_members`, `linkedin_recruiter_snippet`, etc.) without that write.

Show the subagent's full structured output to the human as-is — company info, contacts found (with source), LinkedIn search-snippet hits, or the honest "nothing found" for any category that came up empty. This is a checkpoint, not a formality: the human needs to actually see this before deciding to proceed.

### 4. On explicit go-ahead only, write all three notes together
Ask plainly: "Write the Program, Contact, and Tracker notes now?" A yes/no, not implied by silence or by having answered the two questions in step 2 — answering those questions is not the same as authorizing the write.

On yes:
1. Create any missing folder (`Programs/Considering/`, `Contacts/Each One/`, `Tracker/Each One/` — as of 2026-07-26 none of these three exist in the vault yet, only `Programs/Serious/` does) as part of this same write, not speculatively beforehand.
2. Write the Program note, Contact note, and Tracker/Each One note per `reference/note-templates.md`, cross-linked as documented there (`list_origin`, `recruiter_contact`, `related_programs`, `program`, `contact`, `related_notes`).
3. Fold the contact-researcher subagent's real findings (with sources) into the Contact note's Facts section verbatim — don't paraphrase away the citations.
4. Report back the three paths written and a one-line summary of what's now true that wasn't before.

On no (or if the human wants changes): go back to step 2/3 as needed. Never write partial output — if any of the three notes can't be completed (e.g. a required cross-link target doesn't exist yet), stop and say so rather than writing two of three and leaving the third for later.

## What this skill does not do

- Does not create an Applying note (`Internship Pipeline.md` Step 4) — that happens later, only once real application activity starts, and is out of scope here.
- Does not run `enrich.py`'s CLI to append an Enrichment section to the dossier itself. If the human wants that too, tell them it's a separate, optional manual step (`FIRECRAWL_API_KEY=... python enrich.py "<dossier path>"`) — not something this skill does on their behalf, since that's a second write path with its own idempotency story already documented in `enrich.py`.
- Does not push/commit the vault changes. Leave that to the human (or to whatever the vault's own auto-commit cycle already does) unless explicitly asked to, and if asked, follow the same git-safety discipline as anywhere else — show the diff before committing.

  ```
- `Bash` — `cat .github/workflows/recheck.yml
echo "=====test.yml====="
cat .github/workflows/test.yml
echo "=== state/dossier_uids.json exists? ===" && ls state/`
  ```
name: recheck
on:
  schedule:
    - cron: '30 6 * * *'  # daily — postings don't close often enough to justify hourly rechecks
  workflow_dispatch: {}   # manual trigger, for verifying end-to-end before trusting the schedule

permissions:
  contents: write  # commit logs/rechecks.jsonl back to this repo
  issues: write    # gh issue create on mass-deletion brake / push failure

jobs:
  recheck:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout internship-research-loop
        uses: actions/checkout@v4

      - name: Checkout gupta-builds/Jarvis
        uses: actions/checkout@v4
        with:
          repository: gupta-builds/Jarvis
          token: ${{ secrets.JARVIS_PUSH_TOKEN }}
          path: jarvis-checkout
          fetch-depth: 0  # full history — a shallow clone can fail `git pull --rebase`
                          # if the vault's own auto-commit cycle has diverged by more than one commit

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install -r requirements.txt

      - name: Configure git identity
        run: |
          git config --global user.name "internship-research-loop bot"
          git config --global user.email "actions@users.noreply.github.com"

      - name: Run recheck
        env:
          JARVIS_DIR: ${{ github.workspace }}/jarvis-checkout
          GH_TOKEN: ${{ github.token }}
        run: python recheck.py
=====test.yml=====
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
=== state/dossier_uids.json exists? ===
opt_cache.json
seen_ids.json
  ```
- `TaskUpdate` — `{"taskId":"3","status":"in_progress"}`
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/agents/loop-verifier.md`
  ```
---
name: loop-verifier
description: Standalone health check of the whole internship-research-loop pipeline — test suite, scheduled-run history, vault-vs-log agreement, seen_ids/vault divergence, auto-filed issues. Produces a dated, evidence-cited verdict, the automated equivalent of the manual audits run on 2026-07-19 and 2026-07-25. Invoke when asked "is the pipeline actually healthy", before trusting a cadence change, or periodically as a sanity check — never invents a result it didn't verify.
tools: Bash, Read, Grep, Glob, mcp__jarvis__vault_list, mcp__jarvis__vault_read, mcp__jarvis__search_simple
---

You audit this pipeline's **actual live state**, the same way this project's manual audits (recorded 2026-07-19, 2026-07-25 — see the vault's `20_Progress/Internship/Building System/Phases Run.md` and related build-log notes for their exact prior findings, if you want precedent) were done: every claim in your final report must be backed by a command you actually ran or a file you actually read this session. Never write "looks fine" or "should be working" — write what you checked, what it returned, and what that does or doesn't tell you. If a check is inconclusive (e.g. a token is missing, a folder doesn't exist to check), say that plainly instead of skipping it silently.

You are read-only. Never modify code, never write to the vault, never delete state files, never file or comment on issues yourself — you report, a human or a separate task acts on it.

## Checks to run, in this order

### 1. Full test suite
```bash
cd /home/anant_gupta/projects/work/internship-research-loop && python -m pytest -q
```
Report the exact pass/fail/error count and, if anything failed, which test and why (last ~15 lines of output). This repo's tests run in CI on every push/PR (`.github/workflows/test.yml`) — a red suite here means CI would be red too, worth flagging even if you can't see CI's own run for this exact commit yet.

### 2. Scheduled workflow history (last N runs each)
```bash
gh run list --repo gupta-builds/internship-research-loop --workflow=run.yml --limit 10 --json databaseId,status,conclusion,createdAt,displayTitle
gh run list --repo gupta-builds/internship-research-loop --workflow=recheck.yml --limit 10 --json databaseId,status,conclusion,createdAt,displayTitle
gh run list --repo gupta-builds/internship-research-loop --workflow=test.yml --limit 10 --json databaseId,status,conclusion,createdAt,displayTitle
```
`run.yml` is hourly, `recheck.yml` is daily at 06:30 UTC (`.github/workflows/*.yml` — read them if the cadence looks off, cron schedules can be re-tuned). Report conclusion counts (success/failure) over the sampled window and call out any run that failed or is still in progress unexpectedly. Cross-reference failures against `logs/runs.jsonl` / `logs/rechecks.jsonl` (`halted`/`halt_reason`/`errors` fields) in this repo for the matching timestamp — a CI failure and a logged `halted: true` should usually correlate; if they don't, that's itself worth reporting.

### 3. Vault dossier counts vs. what run logs claim was written
Read the tail of `logs/runs.jsonl` (this repo) and sum `written_count` across some recent window. Then check the vault's actual `List/Dossiers/` contents via `mcp__jarvis__vault_list` — both the flat root and, since `core/classify.py`'s priority-bucket subfolders (`1 - AI & ML/`, `2 - Fullstack/`, `3 - CyS & Finance/`, `Other/`) may or may not have actually been exercised live yet, check whether those subfolders exist at all before assuming they do. As of 2026-07-26 they did not — the vault's dossiers were still all flat, uid-named files (`simplifyjobs-*.md`, `vanshb03-*.md`) with no bucket subfolders, meaning the bucket-sorting code that landed in this repo's working tree had not yet run against the real vault. If that's still true when you check, say so explicitly rather than assuming the code shipped just because it's in the repo — "the code exists" and "the code has run live" are different claims, and this repo's own history (`enrich.py` sat unused for weeks after being merged) is exactly why that distinction matters here.

### 4. seen_ids.json / vault divergence
Read `state/seen_ids.json` and, if it exists, `state/dossier_uids.json` (this repo). Compare against the actual files in the vault's `List/Dossiers/` (recursively, via `mcp__jarvis__vault_list`) — read each dossier's frontmatter (`mcp__jarvis__vault_read` with `targetType: frontmatter`) far enough to recover its identity (company/title, or a `uid` if an older-format dossier still has one in frontmatter). `core/git_ops.py` and `vault_writer/writer.py`'s own docstrings already document one **known, permanent** divergence source: the 2026-07-18 manual vault cleanup removed 110 dossiers outside the pipeline while keeping their uids in `seen_ids.json`, so `seen_ids.json` will never again exactly equal "what's in the vault" and that's expected, not a bug. What you're actually checking for is *new*, *unexplained* divergence beyond that baseline — dossiers in the vault with no corresponding seen_id (a manual add, or a write that didn't update state), or `dossier_uids.json` manifest entries pointing at vault paths that no longer exist (a dossier deleted outside `recheck.py`'s own removal path).

### 5. Auto-filed GitHub issues
```bash
gh issue list --repo gupta-builds/internship-research-loop --state all --json number,title,createdAt,state --limit 30
```
This repo's own code only ever files an issue from four call sites — schema-drift/fetch-halt and Jarvis-push-failure and systemic (required_fields/format_compliance) write-gate rejections in `run_pipeline.py`, and mass-deletion-brake/push-failure in `recheck.py` (`file_github_issue`/`_commit_log` in both files — grep for `issue_fn(` and `file_github_issue(` if you want the exact call sites). Report what's actually open/closed and match each real issue's title against one of those four triggers if you can — an issue that doesn't match any of them is either manually filed or evidence of a fifth trigger nobody's documented, either way worth flagging.

## Output format

```
# Loop Verifier Report — <today's date, YYYY-MM-DD>

## 1. Test suite
<pass/fail count, evidence>

## 2. Scheduled runs (last 10 each)
run.yml:     <N success, N failure, N in-progress>
recheck.yml: <...>
test.yml:    <...>
<any anomalies, with run IDs>

## 3. Vault vs. run-log dossier counts
<counts, bucket-folder existence check, any mismatch explained>

## 4. seen_ids / vault divergence
<baseline (2026-07-18 cleanup) acknowledged; new divergence found or not, with evidence>

## 5. Auto-filed issues
<open/closed counts, each mapped to a trigger or flagged as unmapped>

## Verdict
<one of: HEALTHY / DEGRADED / BROKEN, one paragraph justifying it from the five sections above — no hedge words ("should be", "probably") without the check that would remove the hedge>
```

If `gh` isn't authenticated, or the `jarvis` MCP tools aren't connected to a live vault (verify with a cheap `mcp__jarvis__vault_list` call before relying on it — an error there means "not connected," not "empty vault"), say exactly that in the relevant section instead of silently omitting the check or guessing at what it would probably show.

  ```
- `TaskUpdate` — `{"taskId":"3","status":"completed"}`
- `TaskUpdate` — `{"taskId":"4","status":"in_progress"}`
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/review-loop-change/SKILL.md`
  ```
---
name: review-loop-change
description: "Reviews a proposed change to internship-research-loop against this repo's own established conventions (zero-LLM in the unattended path, permissive-by-default filtering, fail-closed write-gate ordering, cited-real-data rule comments) before it ships. Use before committing/pushing a change to core/, ingestion/, vault_writer/, run_pipeline.py, or recheck.py."
trigger: /review-loop-change
---

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

  ```
- `TaskUpdate` — `{"taskId":"4","status":"completed"}`
- `TaskUpdate` — `{"taskId":"5","status":"in_progress"}`
- `Bash` — `cat ~/.claude/settings.json 2>/dev/null | head -60
echo "=== any other settings.json examples with permissions block ==="
find /home/anant_gupta/projects -maxdepth 4 -path "*/.claude/settings.json" 2>/dev/null | head -5`
  ```
{
  "permissions": {
    "allow": [
      "mcp__pencil"
    ],
    "defaultMode": "acceptEdits"
  },
  "model": "sonnet",
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "pwsh -ExecutionPolicy Bypass -File /home/anant_gupta/.claude/hooks/after-edit-log.ps1"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "pwsh -ExecutionPolicy Bypass -File /home/anant_gupta/.claude/hooks/session-wrapup.ps1"
          }
        ]
      }
    ]
  },
  "enableWorkflows": true,
  "statusLine": {
    "type": "command",
    "command": "bash ~/.claude/statusline.sh",
    "padding": 0,
    "refreshInterval": 30
  },
  "enabledPlugins": {
    "linter@anthropic-tools": true,
    "smart-connections@anthropic-tools": true,
    "claudian@anthropic-tools": true,
    "otel-monitoring@anthropic-tools": true,
    "vercel@claude-plugins-official": true,
    "pyright-lsp@claude-plugins-official": true,
    "ponytail@ponytail": true
  },
  "extraKnownMarketplaces": {
    "cloudflare": {
      "source": {
        "source": "github",
        "repo": "cloudflare/skills"
      }
    },
    "ponytail": {
      "source": {
        "source": "github",
        "repo": "DietrichGebert/ponytail"
      }
    }
=== any other settings.json examples with permissions block ===
/home/anant_gupta/projects/hub/tradingview/.claude/settings.json
/home/anant_gupta/projects/hackathon/Resq/.claude/settings.json
  ```
- `Read` — `/home/anant_gupta/projects/hub/tradingview/.claude/settings.json`
- `Skill` — `{"skill":"update-config","args":"Configure .claude/settings.json for this repo (internship-research-loop). Needs: (1) pytest runs allowed without prompting — `python -m pytest`, `pytest` and common variants; (2) git operations short of force-push allowed without prompting — status, diff, log, branch, show, add, commit (local), pull; explicitly do NOT blanket-allow `git push` or `git push --force`/`-f` — those must still prompt for confirmation every time, especially anything pushing to origin/master; (3) gh CLI read operations without prompting — `gh api ...` (GET-style reads), `gh run list`, `gh run view`, `gh issue list`, `gh issue view`, `gh workflow list`; explicitly do NOT allow `gh secret set`/`gh secret remove` or any GitHub Actions secret modification — those must still require confirmation. This is a small repo (internship-research-loop) with an existing .claude/settings.local.json that already has enabledMcpjsonServers — add a new .claude/settings.json (project-shared, not local) with a permissions.allow list matching the above, plus explicit deny/ask entries (whichever the schema supports) for force-push and secret-modifying gh commands so they're not just \"unlisted\" but explicitly guarded. Follow this repo's own existing pattern seen in sibling repos (e.g. Bash(pytest *), Bash(git status *) style glob permission strings)."}`
- `Bash` — `test -f /home/anant_gupta/projects/work/internship-research-loop/.claude/settings.json && echo EXISTS || echo MISSING`
  ```
MISSING
  ```
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/settings.json`
  ```
{
  "permissions": {
    "allow": [
      "Bash(pytest)",
      "Bash(pytest *)",
      "Bash(python -m pytest)",
      "Bash(python -m pytest *)",
      "Bash(git status)",
      "Bash(git status *)",
      "Bash(git diff)",
      "Bash(git diff *)",
      "Bash(git log)",
      "Bash(git log *)",
      "Bash(git branch)",
      "Bash(git branch *)",
      "Bash(git show)",
      "Bash(git show *)",
      "Bash(git add *)",
      "Bash(git commit)",
      "Bash(git commit *)",
      "Bash(git pull)",
      "Bash(git pull *)",
      "Bash(git fetch)",
      "Bash(git fetch *)",
      "Bash(gh api *)",
      "Bash(gh run list*)",
      "Bash(gh run view*)",
      "Bash(gh issue list*)",
      "Bash(gh issue view*)",
      "Bash(gh workflow list*)",
      "Bash(gh workflow view*)"
    ],
    "ask": [
      "Bash(git push)",
      "Bash(git push *)",
      "Bash(gh secret set*)",
      "Bash(gh secret remove*)",
      "Bash(gh secret delete*)",
      "Bash(gh api *repos/*/actions/secrets*)"
    ]
  }
}

  ```
- `Bash` — `python3 -m json.tool .claude/settings.json > /dev/null && echo "valid JSON"`
  ```
valid JSON
  ```
- `Bash` — `cat README.md`
  ```
# internship-research-loop

24/7 internship discovery automation — polls SimplifyJobs and Jose-Gael-Cruz-Lopez,
filters against a profile, dedups (per-source uid + cross-source company+title), and
writes dossiers into an Obsidian vault through a validated template + five-check
write gate. A daily recheck (`recheck.yml`) removes dossiers whose postings close
upstream. (zapplyjobs was dropped as a source 2026-07-18 — its entries are program
landing pages, not deadline-bearing postings.)

Full spec lives in the Jarvis vault: `Internship/Building System/Research Loop —
Implementation Plan.md`.

## Status

Phases 1–3 are live. `.github/workflows/run.yml` runs hourly against the real
`gupta-builds/Jarvis` repo — schema-drift check, fetch, filter, dedup,
validate, write, push (retry-safe against the vault's own independent
auto-commit cycle), with `state/seen_ids.json` only updated after a confirmed
push. First live run (2026-07-17) wrote 137 real dossiers into
`10_Areas/Career/Internships/List/Dossiers/`; a follow-up run correctly
recognized all 137 as already-seen and wrote zero duplicates. Per the plan's
build order: watch the Run Log rollup for a full week before tightening the
cadence past hourly.

## Local dev

```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest tests/ -v
```
  ```
- `Write` — `/home/anant_gupta/projects/work/internship-research-loop/CLAUDE.md`
  ```
# internship-research-loop — Claude Code guidance

This repo is small (~1,500 lines) with a ~1:1 test-to-code ratio (`tests/` mirrors `core/`, `ingestion/`, `vault_writer/` file-for-file). See `README.md` for what it does and `PRD.md` for the full spec/status. This file is about how a Claude Code session should work in it.

## Conventions this codebase enforces — read before touching core/, ingestion/, vault_writer/, run_pipeline.py, or recheck.py

These are load-bearing design decisions, not style preferences. `/review-loop-change` checks a diff against all four before it ships — but know them regardless of whether you run that skill.

1. **Zero-LLM in the unattended path.** `run_pipeline.py`, `recheck.py`, `core/filter.py`, `core/relevance.py`, `core/classify.py`, everything under `ingestion/`, and `vault_writer/` run hourly/daily via GitHub Actions with no human in the loop, and must never call an LLM, however elaborate the logic gets (see `core/relevance.py`'s two-stage design for "elaborate but still zero-LLM"). `enrich.py` is the one manual-CLI exception — a human runs it on demand — and even it stays zero-LLM by its own docstring's rule.
2. **Permissive-by-default / explicit-negative-signal filtering.** Every eligibility gate in `core/filter.py` (`location_eligible`, `degrees_eligible`, the term/season matchers) lets ambiguous or missing data pass; only an affirmative negative signal (a denylist token, an explicit exclusion string) rejects. A false negative here silently kills a real, eligible posting before a human ever sees it — worse than a false positive, which a human screens out at Step 2 of the pipeline anyway.
3. **Fail-closed write-gate ordering.** `vault_writer/validate.py`'s `validate()` runs five checks in a specific cost order — `required_fields` → `not_duplicate` → `cross_source_duplicate` → `url_liveness` → `format_compliance` — free checks before ones that cost a network call, first failure wins. Don't reorder without restating the cost reasoning.
4. **Every new rule cites the real live data it was built from, in a comment.** A new regex, keyword, denylist entry, or threshold names the actual company/posting/fixture it was checked against and the date, right next to the code (see `core/filter.py`'s `_NON_US` denylist or `core/relevance.py`'s stage1/stage2 patterns for the expected shape). "Seems right" is not a citation.

## Note-template contracts (for `/promote-dossier` and any future vault-writing code)

When writing Program, Contact, or Tracker/Each One notes into the Jarvis vault, every field below is **required and must always be present**, even as `null`/`[]` — same fail-closed-on-missing-fields discipline as `vault_writer/validate.py`'s `REQUIRED_FRONTMATTER_FIELDS` for dossiers. Full field-by-field templates with body structure live in `.claude/skills/promote-dossier/reference/note-templates.md`; this is the contract summary.

**Program note** (`Programs/Serious/` or `Programs/Considering/`) — copied from the vault's own `30_Order/Templates/Career/Program Template.md`:
`name, company, program_type, eligible_classes, grad_year, role_type, wave, opens_date, deadline_posted, deadline_real, pay_per_week, pay_currency, duration_weeks, benefits, application_url, careers_page, list_origin, applying_note, recruiter_contact, tags`. No `status`/`next` field — Program notes are durable/static, they change only when a fact about the program itself changes.

**Contact note** (`Contacts/Each One/`) — copied from `30_Order/Templates/Career/Contact Template.md`:
`type: contact, name, role, company, linkedin_url, email, how_found, relationship, related_programs, last_contact_date, tags, next`.

**Tracker/Each One note** (`Tracker/Each One/`) — the vault has **no pre-existing template** for this one (only roll-up views `Tracker/Internship - Dashboard.md` and `Tracker/Tracker.md` exist); this shape is authored from `30_Order/Workflows/Internship Pipeline.md`'s own field description:
`type: tracker, program, contact, company, url, date_noted, date_researched, date_created, date_applied, date_result, result, deadline, related_notes, tags, next`. If a real template later gets added to the vault, switch to it instead.

Cross-links: Program `list_origin` → dossier, Program `recruiter_contact` ↔ Contact `related_programs`, Tracker `program`/`contact`/`related_notes` → the other three notes. Don't invent new cross-link fields (e.g. a `tracker_note` field on Program) — propose a vault-template change explicitly if one's ever needed instead of adding it silently from a skill.

## Skills and agents available in this repo

| Name | Kind | Use when |
|---|---|---|
| `/promote-dossier` | skill | Promoting one dossier from `List/Dossiers/` into the real pipeline (`Programs/` + `Contacts/Each One/` + `Tracker/Each One/`) — Internship Pipeline Step 3. Human-in-the-loop, needs the Jarvis vault reachable (git checkout sibling to this repo, or the `jarvis` MCP tools if Obsidian's running) — see the skill's own prerequisite section. |
| `contact-researcher` | agent | Invoked by `/promote-dossier` (step 3) to find real, sourced contact signal for one company. Can also be launched standalone for a single company. Never fabricates — reports "nothing found" honestly. |
| `loop-verifier` | agent | Standalone health check of the whole pipeline — tests, scheduled-run history, vault-vs-log agreement, seen_ids divergence, auto-filed issues. Run it when you need to know if the pipeline is *actually* healthy, not just whether the code looks right. |
| `/review-loop-change` | skill | Before committing/pushing a change to `core/`, `ingestion/`, `vault_writer/`, `run_pipeline.py`, or `recheck.py` — checks the diff against the four conventions above. Not a substitute for `/code-review` (correctness/security/style) — this one's repo-specific. |

## Agent vs. more Python — the actual judgment call for each

The instinct in this codebase has consistently been "write a deterministic script" (`core/filter.py`, `core/relevance.py`, `core/classify.py` are all zero-LLM by design, and rightly so — they run unattended). That instinct stops being right exactly where a human has to look at something novel and judge it, which is genuinely different work:

- **Contact research** → agent (`contact-researcher`), not a script. Finding a real recruiter/byline/GitHub member for an arbitrary company is exploratory search with an unbounded input space and a real cost to getting it wrong (see the "wrong guess is worse than empty" rule in the agent file) — not something a fixed set of regexes can do safely. `enrich.py`'s functions are still the right *tools* for this; the agent decides *how* to use them for a given company, a script can't.
- **Promotion** (`/promote-dossier`) → skill with a human consent gate, not automation. This step already involves a judgment call the pipeline doc is explicit is not automatable (Serious vs. Considering, whether the auto-classified bucket still holds) — the point of Step 2/3 being manual by design. A skill structures the human's own workflow; it doesn't remove the human.
- **Verification** (`loop-verifier`) → agent, not a cron script, specifically because it cross-references several independently-drifting sources (test results, GitHub Actions history, live vault state, local state files) and has to *notice* when they disagree in a way that wasn't anticipated in advance — a fixed script would need to enumerate every possible mismatch up front, which is exactly the kind of audit this project has so far only done by hand (2026-07-19, 2026-07-25).
- **Review** (`/review-loop-change`) → skill, not an agent, and not more Python. The checklist is fixed and known in advance (four conventions, unlikely to grow much), and the repo's small diff size doesn't need an isolated agent context — see that skill's own "why a skill" section. A script *could* grep for some of this (e.g. flagging LLM imports in unattended-path files), but "does this new regex cite real data" needs actual reading comprehension a lint rule doesn't have.

If a new piece of recurring toil shows up and it's mechanical/deterministic (another source feed, another filter rule), it's still Python first, same as everything in `core/` and `ingestion/` today — don't reach for an agent out of habit once a human's judgment isn't actually the bottleneck.

  ```
- `TaskUpdate` — `{"taskId":"5","status":"completed"}`
- `TaskUpdate` — `{"taskId":"6","status":"in_progress"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/[REDACTED].md"}`
- `mcp__jarvis__vault_read` — `{"path":"10_Areas/Career/Internships/List/Dossiers/[REDACTED].md"}`
- `AskUserQuestion` — `{"questions":[{"question":"Promoting the Appian \"Software Engineering Intern\" dossier (vanshb03, McLean VA, Summer 2027) — which Programs folder should it go in?","header":"Target folder","multiSelect":false,"options":[{"label":"Programs/Serious/","description":"Pursuing this now — same research depth as Considering, just signals active intent."},{"label":"Programs/Considering/","description":"Later/undecided for now — same research depth, just a timing signal."}]},{"question":"This dossier predates core/classify.py (written 2026-07-25, before the bucket-classifier landed) — it has no auto-assigned priority bucket or classification callout to default to. Pick one manually, or leave it Other/unclassified?","header":"Priority bucket","multiSelect":false,"options":[{"label":"Fullstack","description":"Posting content: full-stack components, production-adjacent engineering, data structures/OOP — matches core/classify.py's Fullstack signals most closely."},{"label":"AI/ML","description":"Posting mentions AI tooling/LLMs, but as a workflow accelerant (\"engineer with AI\"), not the actual engineering domain of the role itself."},{"label":"Other","description":"Leave unclassified rather than force-fit a bucket onto a dossier the classifier never actually saw."}]}]}`

## You

<task-notification>
<task-id>b0w0wai02</task-id>
<tool-use-id>[REDACTED]</tool-use-id>
<status>stopped</status>
<summary>No completion record was found for this background shell command from the previous session. It may have been stopped (via the UI, Monitor timeout, or agent teardown — these leave no transcript marker), or it may have been running when the previous Claude Code process exited. Check the output file for partial results before assuming it completed.</summary>
</task-notification>

## Claude

Noted — stopping there and not re-triggering that prompt. Here's where things actually stand:

**Built and in place:**
- Task B: `.claude/agents/contact-researcher.md`
- Task C: `.claude/agents/loop-verifier.md`
- Task D: `.claude/skills/review-loop-change/SKILL.md`
- Task E: `.claude/settings.json` (validated JSON) + repo `CLAUDE.md`
- Task A: `.claude/skills/promote-dossier/SKILL.md` + `reference/note-templates.md`

All five are written and registered (both skills already show up in the skill listing). Full test suite was green (258/258) before I started, and I haven't touched any pipeline code, so that's unaffected.

**Where I got interrupted:** verifying Task A end-to-end against a real dossier (Appian, `vanshb03-22b1b26d...`). I'd picked it and was about to ask the two required questions (target folder, priority-bucket override) when you rejected that prompt. I won't re-fire the same question.

Real complication that surfaced before the rejection, worth flagging regardless of how we verify: **this dossier — and the ones sitting in the vault generally — predate the classify/bucket-folder code** (`core/classify.py`, the `writer.py` changes dropping `uid`/`category`/`promoted` in favor of `next`). They're still flat, old-format files with no classification callout. So question (b) of the skill ("does the auto-assigned bucket still hold?") has no real default to offer on any dossier that currently exists — that's true of every live dossier right now, not just this one.

How do you want to handle verification from here — answer the two questions now so I can run it to the write-consent gate, walk through it a different way, or skip live verification and I'll report Task A as reviewed-but-not-run?

## You

· Promoting the Appian "Software Engineering Intern" dossier (vanshb03, McLean VA, Summer 2027) — which Programs folder should it go in? (Programs/Considering) - because not ai/ml related.
· This dossier predates core/classify.py (written 2026-07-25, before the bucket-classifier landed) — it has no auto-assigned priority bucket or classification callout to default to. Pick one manually, or leave it Other/unclassified? (Fullstack / AI/ML / Other) - The dossier file written should be puhsing notes into jarvis based on the priority folders created. Focusing number 1 first and then moving down to others. But each and every single dossier is written in detail the same way. Just a preference of what gets hunted first.

## Claude

Got it — Considering, and Fullstack (matches your "not AI/ML" read on the posting: full-stack production-adjacent engineering, AI as a tool not the domain). Priority buckets are hunting-order only, not depth — noted, matches what's already in the pipeline doc and what I built into the skill. Continuing to step 3: invoking contact-researcher for Appian.

Real, useful findings — but the subagent's own tool call tripped a security flag: it ran `echo $FIRECRAWL_API_KEY | cut -c1-4`, which counts as credential materialization even truncated. That's a mistake in my own agent instructions — let me fix it before going further.

Contact research done and shown. Last step per the skill: explicit go-ahead before any write.

Good — it auto-creates missing parent directories. Writing all three notes now.

Still 258/258 — no pipeline code touched. All tasks complete.

All five tasks are done, and Task A ran for real, not just reviewed. Summary:

**Review of Prompt 1/2 state (before building):** partially met the assumption. `core/priority.py` doesn't exist under that name, but its functional equivalent does — `core/classify.py` (bucket classification) + `core/relevance.py` (CS-relevance gate), both wired into `run_pipeline.py`. `enrich.py` was genuinely widened with LinkedIn search-snippet support (respecting the no-scrape hard line). The "four vault subfolders" claim was only 1/4 true live: `Programs/Serious/` existed, but `Programs/Considering/`, `Contacts/Each One/`, and `Tracker/Each One/` did not — and every dossier in the vault still predates the classifier (old frontmatter, no bucket folders, no classification callout). I built around this reality rather than the assumption.

**Task A — `/promote-dossier` skill:** built (`SKILL.md` + `reference/note-templates.md`), and **run for real, end-to-end, including the write step** — not just reviewed. Promoted Appian's "Software Engineering Intern" dossier: asked the two required questions (you picked Considering / Fullstack), invoked contact-researcher, showed you real findings, got explicit consent, and wrote all three notes live into the Jarvis vault (creating `Programs/Considering/`, `Contacts/Each One/`, `Tracker/Each One/`, which didn't exist before). This is the first time Internship Pipeline Step 3 has ever run against real output — the pipeline doc itself notes it never had been.

**Task B — `contact-researcher` agent:** built and exercised live. Found real, sourced contacts for Appian (4 recruiters via LinkedIn snippets, 1 blog byline, a real-but-memberless GitHub org). One real bug surfaced and fixed during the run: my original instructions had it `echo`ing 4 characters of the live `FIRECRAWL_API_KEY` to "sanity check" it, which tripped a credential-materialization security flag even truncated — replaced with a boolean set/unset check.

**Task C — `loop-verifier` agent:** built, not run (no request to audit pipeline health this session — it's designed to be launched standalone whenever that's needed).

**Task D — review-loop-change:** built as a **skill**, not an agent — reasoning is in the skill file itself: ~1,500-line repo, diffs land small, checklist is fixed and known in advance, no need for isolated agent context.

**Task E — settings + CLAUDE.md:** `.claude/settings.json` allows pytest/safe-git/gh-read without prompting, explicitly requires confirmation (`ask`) for any `git push` or `gh secret` command — built via the `update-config` skill. Repo `CLAUDE.md` documents the note-template contracts and the explicit agent-vs-script reasoning for each of the four toil areas.

Tests: 258/258 passing throughout — no pipeline code was touched, only `.claude/` and `CLAUDE.md`.

**Tool calls:**

- `Agent` — `{"description":"Contact research for Appian","subagent_type":"contact-researcher","prompt":"Company: Appian (Appian Corporation, enterprise low-code/AI process automation software, Nasdaq: APPN, headquartered McLean, Virginia). This is real verification work for the promote-dossier skill in gupta-builds/internship-research-loop — find real, sourced contact signal for this company per your instructions in .claude/agents/contact-researcher.md. Report using your standard output format.","run_in_background":false}`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/agents/contact-researcher.md`
  ```diff
  - `FIRECRAWL_API_KEY` must be set in the environment for any of this to work (`echo $FIRECRAWL_API_KEY | cut -c1-4` to sanity-check without printing the whole key — do not print secrets to output). If it is unset, stop and report that plainly instead of silently returning nothing (an empty key and an empty result look identical to a caller unless you say which one happened).
  + `FIRECRAWL_API_KEY` must be set in the environment for any of this to work. Check with `[ -n "$FIRECRAWL_API_KEY" ] && echo set || echo unset` — never echo, print, or otherwise materialize any part of the key's actual value, truncated or not; that counts as credential exposure even at 4 characters. If it is unset, stop and report that plainly instead of silently returning nothing (an empty key and an empty result look identical to a caller unless you say which one happened).
  ```
- `AskUserQuestion` — `{"questions":[{"question":"Write the Program, Contact, and Tracker notes now for Appian — Software Engineering Intern (Programs/Considering/, Fullstack bucket, using Adam Goetz's LinkedIn search-snippet hit as the primary contact)?","header":"Write consent","multiSelect":false,"options":[{"label":"Yes, write all three","description":"Creates Programs/Considering/, Contacts/Each One/, and Tracker/Each One/ (none exist yet) and writes the three cross-linked notes for real into the live Jarvis vault."},{"label":"No, stop here","description":"Verification ends at this gate — confirms the skill reaches write-consent correctly without actually mutating the vault."}]}]}`
- `ToolSearch` — `{"query":"select:mcp__jarvis__vault_write","max_results":3}`
- `mcp__jarvis__vault_write` — `{"path":"10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian.md","content":"---\nname: Software Engineering Intern at Appian\ncompany: Appian\nprogram_type: Fullstack\neligible_classes: []\ngrad_year:\nrole_type: internship\nwave:\nopens_date:\ndeadline_posted:\ndeadline_real:\npay_per_week: 2000\npay_currency: USD\nduration_weeks: 10\nbenefits:\n  - Health coverage\n  - Employee Assistance Program (EAP)\n  - Employee Stock Purchase Program (ESPP)\n  - Retirement/pension plan\n  - Tuition reimbursement\napplication_url: https://careers.appian.com/jobs/[REDACTED]\ncareers_page: https://careers.appian.com/students\nlist_origin: \"[[10_Areas/Career/Internships/List/Dossiers/[REDACTED]]]\"\napplying_note:\nrecruiter_contact: \"[[10_Areas/Career/Internships/Contacts/Each One/Software Engineering Intern - Appian]]\"\ntags:\n  - internship\n  - program\n---\n# Software Engineering Intern — Appian\nStatic research only — comp, eligibility, deadlines, traps, prep. Live status (applied, interview, offer) lives on the matching note in `20_Progress/Internship/Applying/`, linked via `applying_note` above.\n## Program Overview\nAppian is an enterprise low-code/AI process automation software company (Nasdaq: APPN), headquartered in McLean, VA. The Software Engineering Intern role sits within Appian Engineering, contributing to production-adjacent work across the AI-powered Process Automation platform: full-stack components, AI-assisted development tooling, debugging/systems thinking, and design/code-review collaboration. 10-week program. Pay stated on the posting as $50.00/hour ($8,666/month) — `pay_per_week` above is derived from that hourly rate at 40 hrs/week, not a figure Appian states directly.\n## Eligibility\nCurrently pursuing a Bachelor's or Master's in CS or Computer Engineering; must be returning to school after the internship to continue degree requirements. Full-time (40 hrs/week) commitment required for the full 10 weeks. Considered for Summer 2027, students only.\n## Traps & Gotchas\n> [!WARNING]\n> In-person 5 days/week at the McLean, VA headquarters is mandatory (\"Interns in this program are expected to be in the office 5 days a week\"). Applications aren't reviewed and interviews aren't scheduled until August 2026 even though the posting is live now. The posting also states \"Appian will not sponsor a new applicant for employment authorization for this position\" — that's a sponsorship exclusion, not necessarily an OPT exclusion, but confirm it doesn't conflict with OPT usage before investing further time.\n## Prep Checklist\n- [ ]\n## Related Resources\n- [[10_Areas/Career/Internships/List/Dossiers/[REDACTED]]] (List/Dossiers origin)\n"}`
- `mcp__jarvis__vault_write` — `{"path":"10_Areas/Career/Internships/Contacts/Each One/Software Engineering Intern - Appian.md","content":"---\ntype: contact\nname: Adam Goetz\nrole: Lead Talent Acquisition Partner\ncompany: Appian\nlinkedin_url: https://www.linkedin.com/in/adamggoetz\nemail:\nhow_found: \"linkedin search snippet: site:linkedin.com Appian recruiter\"\nrelationship: cold\nrelated_programs:\n  - \"[[10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian]]\"\nlast_contact_date:\ntags:\n  - contact\nnext:\n---\n# Software Engineering Intern — Appian\n## Facts\nFound via the `contact-researcher` subagent (2026-07-26), using this repo's `enrich.py` search primitives. Every item below is a real tool-call result with its source — no guesses.\n\n**Recruiter / university recruiting search:**\n- Adam Goetz — Lead Talent Acquisition Partner at Appian — https://www.linkedin.com/in/adamggoetz (query: \"Appian recruiter\")\n- Senior Talent Acquisition Partner (Technical) job posting, referencing Appian's Talent Acquisition team — https://job-boards.greenhouse.io/appian/jobs/8079317 (query: \"Appian recruiter\")\n- Students/campus recruiting hub page (no individual name) — https://careers.appian.com/students (query: \"Appian university recruiting\")\n\n**Engineering blog byline:**\n- Amy Horton — \"Evolving My Role, Impact, and Leadership at Appian\" (AppianLife Blog, Engineering and Product category, 2025-07-28) — https://careers.appian.com/blog/engineering-and-product/evolving-my-role--impact--and-leadership-at-appian\n\n**GitHub org:** https://github.com/orgs/appian exists but returned zero public members.\n\n**LinkedIn search-snippet hits** (snippet text only — no LinkedIn pages were fetched or scraped):\n- \"Adam Goetz - Lead Talent Acquisition Partner at Appian\" — https://www.linkedin.com/in/adamggoetz\n- \"Summer Bartholomew - Talent Acquisition @ Appian\" — https://www.linkedin.com/in/summerleadawson\n- \"Donald Zimmer - Lead Talent Acquisition Partner @ Appian\" — https://www.linkedin.com/in/donald-zimmer-09486342\n- \"Mary Kate Messina (Olson) - Early Talent Acquisition\" / \"Currently leading University Recruiting at Appian, where I own strategy and execution for early career hiring across Engineering, IT, Customer Success, Sales...\" — https://www.linkedin.com/in/[REDACTED]\n\nMary Kate Messina's snippet (\"leading University Recruiting... early career hiring across Engineering\") is arguably the strongest fit for a student internship specifically, ahead of Adam Goetz — worth leading with either, note kept here rather than silently picking one.\n## Current Draft\nNot yet written — no outreach has happened yet.\n## Conversation Log\nDated entries, newest at the bottom.\n- **2026-07-26:** Note created via /promote-dossier.\n## Next Action\nDecide which of the four Talent Acquisition contacts above to reach out to first (Mary Kate Messina for university-recruiting fit, or Adam Goetz as the first/most-cited hit), then draft a message from [[Mimic]].\n"}`
- `mcp__jarvis__vault_write` — `{"path":"10_Areas/Career/Internships/Tracker/Each One/Software Engineering Intern - Appian.md","content":"---\ntype: tracker\nprogram: \"[[10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian]]\"\ncontact: \"[[10_Areas/Career/Internships/Contacts/Each One/Software Engineering Intern - Appian]]\"\ncompany: Appian\nurl: https://careers.appian.com/jobs/[REDACTED]\ndate_noted: 2026-07-25\ndate_researched: 2026-07-26\ndate_created:\ndate_applied:\ndate_result:\nresult:\ndeadline:\nrelated_notes:\n  - \"[[10_Areas/Career/Internships/List/Dossiers/[REDACTED]]]\"\ntags:\n  - internship\n  - tracker\nnext:\n---\n# Software Engineering Intern — Appian\nThe dated index for this internship — source of truth for \"where does this stand\" until an Applying note exists (see [[30_Order/Workflows/Internship Pipeline]] Step 8).\n## Timeline\n- **Noted:** 2026-07-25\n- **Researched:** 2026-07-26\n- **Created:** —\n- **Applied:** —\n- **Result:** —\n## Next Action\nDecide whether to move this from Considering to actually applying — applications aren't reviewed until August 2026 per the Program note's Traps section, so there's no rush, but the in-person 5-day/week requirement is worth weighing before committing further.\n"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Programs"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Contacts/Each One"}`
- `mcp__jarvis__vault_list` — `{"path":"10_Areas/Career/Internships/Tracker/Each One"}`
- `Bash` — `python -m pytest -q 2>&1 | tail -5`
  ```
/bin/bash: line 1: python: command not found
  ```
- `Bash` — `source .venv/bin/activate && python -m pytest -q 2>&1 | tail -5`
  ```
........................................................................ [ 27%]
........................................................................ [ 55%]
........................................................................ [ 83%]
..........................................                               [100%]
258 passed in 2.31s
  ```
- `TaskUpdate` — `{"taskId":"1","status":"completed"}`
- `TaskUpdate` — `{"taskId":"6","status":"completed"}`

## You

Two things, in order — the first blocks the second from meaning anything.

1. Nothing you built is committed anywhere. No .claude/skills/, .claude/agents/, CLAUDE.md, or .claude/settings.json exist on GitHub. This has to land after Prompt 2's changes are pushed (your work depends on core/classify.py, core/relevance.py, and the widened enrich.py existing) — pull/rebase on top of Prompt 2's pushed commit first, then commit your additions separately on top, so the history reflects the real dependency order. Right now this tooling is unreadable and unusable by anyone except whatever local session built it — including a future me.

2. I read the actual Appian promotion output directly (all three notes it wrote into the vault) against the real Program Template (30_Order/Templates/Career/Program Template.md). The skill matches the template exactly — that's not the problem. The problem: it's leaving structured frontmatter empty in cases where the fetched posting content already had the answer in prose two lines below.
   - eligible_classes: [] — but the Eligibility section it wrote says "Considered for Summer 2027, students only" and "Bachelor's or Master's in CS"
   - deadline_real, deadline_posted, opens_date — all blank, but the Traps section it wrote says "applications
aren't reviewed... until August 2026."
   - grad_year — blank, same pattern.
   - Tracker note's date_created — blankcreation date (the day it was written).
   Fix the skill's instructions so it back-fills these specific frontmatter fields from the same fetched
content it already narrates into prose, This matters more than it looks — thePrograms MOC (10_Areas/Career/Internships/Programs/Programs MOC.md in the vault) sorts and filters on
deadline_real and eligible_classes; righrites is invisible to that view.

Separately: Program Template.md's own Pr bare "- [ ]" — decide explicitly whether the fix belongs in the skill (generate 3-5 real prep items from the JD's actual requirements section) or the
template (add guidance text so a human fetter), and say which you changed andwhy.

Once Task B (classify.py) is actually on GitHub, run Task C (loop-verifier) for real against the live repo and
report real findings — it was built but now enough real change in this repo tomake that check worth something.

That's the verification pass — the shared blocker (commit/push, in dependency order 1 → 2 → 3) and the specific, evidence-based fix for Prompt rther needed from me until those land;want me to hold here, or should I also check the vault-side Programs MOC/Dossiers MOC render correctly against
what's there now (they'll mostly be empt

## Claude

Clear priorities, executing in the order given. Let me first check the actual git state before touching anything.

Clean fast-forward, no conflicts. Now committing Prompt 1+2's work first (the actual dependency), running tests, then my Prompt 3 additions on top.

Everything except `.claude/` and `CLAUDE.md` is staged. Running the full suite once more before committing.

Now the Prompt 3 tooling, on top of that commit — but first, let me apply the two evidence-based fixes before committing, so the commit reflects working, corrected tooling rather than tooling I already know has a bug.

Now the Tracker note's `date_created` mismapping — my original design deferred it to Applying-note creation, which is wrong; it should be filled at write time.

Now applying these fixes to the already-written Appian notes so the artifact matches the corrected skill, not just the instructions.

Both notes corrected in the live vault. Now committing and pushing the Prompt 3 tooling (with the fixes already applied, so the committed version is the corrected one, not the buggy one).

Two commits ready in dependency order, sitting on top of the pulled `origin/master`. Pushing now.

Pushed cleanly, in the right order. Blocker resolved — now running loop-verifier for real against the live, now-current repo.

All four items done. Summary:

**1. Commit/push — done, in dependency order.** Pulled 8 pending automated state/log commits from origin first (no conflicts), then committed Prompt 1+2's work (`6622bca`) and Prompt 3's tooling (`f56ac8c`) as two separate commits, pushed both. Both are live on `origin/master` now.

**2. Frontmatter backfill — fixed in the skill, and in the already-written Appian notes.**
- `eligible_classes` now populated (`["Bachelor's", "Master's"]`) — was genuinely a bug, fixed.
- `grad_year` and the three date fields (`opens_date`/`deadline_posted`/`deadline_real`) — I checked these against your specific complaint and left them null, on purpose: the posting states a *review-start* date ("won't review until August 2026"), which isn't literally an open date, a posted deadline, or a real deadline — none of the three concepts match. Force-fitting it into the closest-sounding field would put a wrong value where the Programs MOC filters on it, which is worse than null, not better. That fact now lives explicitly in the Traps prose instead, with a note explaining why the frontmatter field stays empty. Said differently: 1 of your 4 flagged fields was a real miss (fixed), 3 were correctly empty once I checked what the posting actually states vs. implies — I didn't want to silently comply with the letter of the ask if it meant writing a fact where it doesn't belong.
- Tracker's `date_created` — this one was a real design mistake on my part (I'd wrongly deferred it to Applying-note creation, which isn't even one of the pipeline doc's five listed milestones). Fixed to today, matching `date_researched`.

**3. Prep Checklist — fixed in the skill, not the template.** `Program Template.md` stays a blank scaffold (correct for a human filling it from scratch). `/promote-dossier` already has the fetched JD in hand, so leaving it bare was the same bug as #2 — the skill now generates 3-5 items traceable to specific lines in the posting. Appian's note now has 5 real ones.

**4. loop-verifier — run for real, found something real.** Tests/CI/schedules are all green. But it surfaced a genuine, previously-undocumented problem: **~81 dossiers from vanshb03/zshah101/Greenhouse are marked "seen" in `state/seen_ids.json` (i.e., logged as confirmed-pushed) but don't exist in the live vault** — no recheck-removal log entry, no pipeline error, no GitHub issue filed for any of it. Verdict: **DEGRADED**. Since `dedup_new()` never re-offers an already-seen uid, these are real postings the pipeline has now permanently forgotten. This is outside what you asked me to fix — flagging it, not touching it.

One loose end: your last message cut off mid-sentence on the vault-side MOC question. Want me to look into the `seen_ids`/vault divergence loop-verifier found, or was that the thing you meant to ask about?

**Tool calls:**

- `Bash` — `cd /home/anant_gupta/projects/work/internship-research-loop
git fetch origin 2>&1
echo "=== local vs origin/master ==="
git log --oneline -5 origin/master
echo "=== current branch status ==="
git status
echo "=== is local master behind/ahead of origin ==="
git rev-list --left-right --count origin/master...HEAD`
  ```
=== local vs origin/master ===
ba2bdcd Update state + logs — 2026-07-26
1c3ddc4 Update state + logs — 2026-07-26
ea1a38b Update state + logs — 2026-07-25
2734ca3 Update state + logs — 2026-07-25
3df6a34 Update state + logs — 2026-07-25
=== current branch status ===
On branch master
Your branch is behind 'origin/master' by 8 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   core/filter.py
	modified:   core/profile.yaml
	modified:   enrich.py
	modified:   ingestion/normalize.py
	modified:   ingestion/posting_page.py
	modified:   ingestion/sources.py
	modified:   recheck.py
	modified:   run_pipeline.py
	modified:   tests/fixtures/josegael.json
	modified:   tests/fixtures/simplifyjobs.json
	modified:   tests/fixtures/vanshb03.json
	modified:   tests/fixtures/zshah101.json
	modified:   tests/test_enrich.py
	modified:   tests/test_filter.py
	modified:   tests/test_posting_page.py
	modified:   tests/test_recheck.py
	modified:   tests/test_run_pipeline.py
	modified:   tests/test_sources.py
	modified:   tests/test_writer.py
	modified:   vault_writer/templates/dossier.md.j2
	modified:   vault_writer/validate.py
	modified:   vault_writer/writer.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.claude/
	CLAUDE.md
	core/classify.py
	core/relevance.py
	ingestion/freehire.py
	tests/fixtures/freehire.json
	tests/fixtures/posting_ashby_ctgt.md
	tests/test_classify.py
	tests/test_freehire.py
	tests/test_relevance.py

no changes added to commit (use "git add" and/or "git commit -a")
=== is local master behind/ahead of origin ===
8	0
  ```
- `Bash` — `cd /home/anant_gupta/projects/work/internship-research-loop
git diff --stat HEAD origin/master
echo "=== do incoming commits touch any file I have modified locally? ==="
comm -12 <(git diff --stat HEAD origin/master --name-only | sort) <(git status --porcelain | awk '{print $2}' | sort)`
  ```
 logs/runs.jsonl      |   8 ++
 state/opt_cache.json | 385 +++++++++++++++++++++++++++++++++++++++++++++++++++
 state/seen_ids.json  |  78 ++++++++++-
 3 files changed, 470 insertions(+), 1 deletion(-)
=== do incoming commits touch any file I have modified locally? ===
  ```
- `Bash` — `cd /home/anant_gupta/projects/work/internship-research-loop
git diff HEAD --stat -- ingestion/ vault_writer/ tests/test_writer.py tests/test_filter.py
echo "=== ingestion/freehire.py head ==="
head -20 ingestion/freehire.py`
  ```
 ingestion/normalize.py               |  41 ++++++++++++++
 ingestion/posting_page.py            |  25 ++++++++-
 ingestion/sources.py                 |  39 +++++++++++---
 tests/test_filter.py                 |  76 ++++++++++++++++++++++++++
 tests/test_writer.py                 |  84 +++++++++++++++++++++++++----
 vault_writer/templates/dossier.md.j2 |  14 +++--
 vault_writer/validate.py             |   4 +-
 vault_writer/writer.py               | 100 ++++++++++++++++++++++++++++-------
 8 files changed, 342 insertions(+), 41 deletions(-)
=== ingestion/freehire.py head ===
"""freehire (github.com/strelov1/freehire) — a real, live, no-auth public API
aggregating 3.4M+ postings from 187,542+ companies across 78 ATS platforms,
including direct company crawls (Google, Uber) that no ATS-token approach can
ever reach. Verified live 2026-07-25 against three real ground-truth misses a
manual clipping audit surfaced: exact match found for Nuro's posting; exact
match found for Google's — freehire's own created_at (17:01:40Z) predates
SimplifyJobs' date_posted for the same posting (23:56:31Z) by ~7 hours, real
evidence it can be faster than the curated lists; Uber's exact req wasn't
found, but the same-titled "Career Prep" campaign was, under a different req
number, posted a few days earlier — a real but partial match, reported as
such rather than rounded up.

Scoped deliberately: NOT a crawl of the whole 3.4M-job dataset. Queried
per-company, for companies confirmed (this session, live) to have no
reachable Greenhouse/Ashby/Lever token — that's the value freehire adds over
the other 7 sources; querying it for companies we already reach directly
would just be redundant traffic against someone else's free API.

Reliability, checked before depending on it: no documented rate limit
anywhere (README, SECURITY.md, robots.txt all checked; robots.txt fully
  ```
- `Bash` — `cd /home/anant_gupta/projects/work/internship-research-loop
git pull --ff-only origin master
echo "=== post-pull status ==="
git status --short | head -5
git log --oneline -3`
  ```
From https://github.com/gupta-builds/internship-research-loop
 * branch            master     -> FETCH_HEAD
Updating cdb4299..ba2bdcd
Fast-forward
 logs/runs.jsonl      |   8 ++
 state/opt_cache.json | 385 +++++++++++++++++++++++++++++++++++++++++++++++++++
 state/seen_ids.json  |  78 ++++++++++-
 3 files changed, 470 insertions(+), 1 deletion(-)
=== post-pull status ===
 M core/filter.py
 M core/profile.yaml
 M enrich.py
 M ingestion/normalize.py
 M ingestion/posting_page.py
ba2bdcd Update state + logs — 2026-07-26
1c3ddc4 Update state + logs — 2026-07-26
ea1a38b Update state + logs — 2026-07-25
  ```
- `Bash` — `cd /home/anant_gupta/projects/work/internship-research-loop
git add core/filter.py core/profile.yaml core/classify.py core/relevance.py \
  enrich.py \
  ingestion/normalize.py ingestion/posting_page.py ingestion/sources.py ingestion/freehire.py \
  recheck.py run_pipeline.py \
  vault_writer/templates/dossier.md.j2 vault_writer/validate.py vault_writer/writer.py \
  tests/fixtures/josegael.json tests/fixtures/simplifyjobs.json tests/fixtures/vanshb03.json tests/fixtures/zshah101.json \
  tests/fixtures/freehire.json tests/fixtures/posting_ashby_ctgt.md \
  tests/test_enrich.py tests/test_filter.py tests/test_posting_page.py tests/test_recheck.py \
  tests/test_run_pipeline.py tests/test_sources.py tests/test_writer.py tests/test_classify.py tests/test_relevance.py tests/test_freehire.py
git status --short`
  ```
A  core/classify.py
M  core/filter.py
M  core/profile.yaml
A  core/relevance.py
M  enrich.py
A  ingestion/freehire.py
M  ingestion/normalize.py
M  ingestion/posting_page.py
M  ingestion/sources.py
M  recheck.py
M  run_pipeline.py
A  tests/fixtures/freehire.json
M  tests/fixtures/josegael.json
A  tests/fixtures/posting_ashby_ctgt.md
M  tests/fixtures/simplifyjobs.json
M  tests/fixtures/vanshb03.json
M  tests/fixtures/zshah101.json
A  tests/test_classify.py
M  tests/test_enrich.py
M  tests/test_filter.py
A  tests/test_freehire.py
M  tests/test_posting_page.py
M  tests/test_recheck.py
A  tests/test_relevance.py
M  tests/test_run_pipeline.py
M  tests/test_sources.py
M  tests/test_writer.py
M  vault_writer/templates/dossier.md.j2
M  vault_writer/validate.py
M  vault_writer/writer.py
?? .claude/
?? CLAUDE.md
  ```
- `Bash` — `source .venv/bin/activate && python -m pytest -q 2>&1 | tail -5`
  ```
........................................................................ [ 27%]
........................................................................ [ 55%]
........................................................................ [ 83%]
..........................................                               [100%]
258 passed in 6.71s
  ```
- `Bash` — `cd /home/anant_gupta/projects/work/internship-research-loop
git commit -m "$(cat <<'EOF'
Priority-bucket classification, CS-relevance gate, widened contact research

Adds core/classify.py (Layer 2.5b, zero-LLM keyword bucketing into AI/ML,
CyS & Finance, Fullstack, Other) and core/relevance.py (Layer 2.5, two-stage
CS/software-relevance gate: cheap title-only reject before fetch, content
-confirmed adjacent-field check after). vault_writer/writer.py and the
dossier template now sort writes into priority-bucket subfolders under
List/Dossiers/, drop the unused uid/category/promoted frontmatter fields in
favor of next (matching the vault's own note convention), and add a
dossier_uids.json manifest for idempotent re-writes and recheck.py's
removal-checking.

Widens enrich.py's contact search to recruiter/university-recruiting queries
and LinkedIn search-snippet hits (site:linkedin.com, snippet text only —
never scrapes or logs into linkedin.com, per its own hard line).

Adds ingestion/freehire.py as an 8th discovery source (scoped to companies
with no reachable Greenhouse/Ashby/Lever token) and wires Greenhouse/Ashby/
AIJobs into recheck.py's removal checks.

258/258 tests passing.
EOF
)"
git log --oneline -3`
  ```
[master 6622bca] Priority-bucket classification, CS-relevance gate, widened contact research
 30 files changed, 1492 insertions(+), 77 deletions(-)
 create mode 100644 core/classify.py
 create mode 100644 core/relevance.py
 create mode 100644 ingestion/freehire.py
 create mode 100644 tests/fixtures/freehire.json
 create mode 100644 tests/fixtures/posting_ashby_ctgt.md
 create mode 100644 tests/test_classify.py
 create mode 100644 tests/test_freehire.py
 create mode 100644 tests/test_relevance.py
6622bca Priority-bucket classification, CS-relevance gate, widened contact research
ba2bdcd Update state + logs — 2026-07-26
1c3ddc4 Update state + logs — 2026-07-26
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/reference/note-templates.md`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/reference/note-templates.md`
  ```diff
  - **Folder existence as of 2026-07-26** (checked live via the `jarvis` MCP tools): `Programs/Serious/` exists (1 note in it). `Programs/Considering/`, `Contacts/Each One/`, and `Tracker/Each One/` do **not** exist yet — nothing has ever promoted into them. Creating a missing folder is part of the write step itself (it happens only after explicit go-ahead, same as the notes) — never create it speculatively before the human has said yes.

---
  + **Folder existence as of 2026-07-26** (checked live via the `jarvis` MCP tools): `Programs/Serious/` exists (1 note in it). `Programs/Considering/`, `Contacts/Each One/`, and `Tracker/Each One/` do **not** exist yet — nothing has ever promoted into them. Creating a missing folder is part of the write step itself (it happens only after explicit go-ahead, same as the notes) — never create it speculatively before the human has said yes.

## Backfill structured fields from the same content the body prose is drawn from — don't default to null

Found live in the first real run of this skill (Appian dossier, 2026-07-26): the body sections below (`Program Overview`, `Eligibility`, `Traps & Gotchas`) are written from the dossier's fetched posting content, and it is very easy to write a fact into that prose while leaving the frontmatter field that same fact belongs in untouched at its template default (`null`/`[]`). That's a real defect, not a cosmetic one — `10_Areas/Career/Internships/Programs/Programs MOC.md` sorts and filters on `deadline_real` and `eligible_classes`; a fact that only exists in prose is invisible to that view.

Before finalizing the Program note, re-read the Eligibility and Traps paragraphs you just drafted and check each one against the frontmatter fields below. If a fact you're about to narrate in prose maps to one of these fields, write it into both places — never only the prose:

- **`eligible_classes`**: whatever concrete class-year or degree-level signal the posting actually states — e.g. `["Bachelor's", "Master's"]` if the posting says "currently pursuing a Bachelor's or Master's degree", or `["Sophomore"]` if it names a class year directly (matching the real `Programs/Serious/2026-HRT-Sophomore.md` example in the vault). Use whatever's literally stated; never invent a class year the posting doesn't name.
- **`grad_year`**: only a literal year the posting states directly (e.g. "Class of 2028", "graduating May 2028"). A constraint like "must return to school after this internship" tells you the candidate ISN'T graduating in the internship's own year — that's a fact for `eligible_classes` or the Eligibility prose, not license to compute a specific `grad_year` the posting never states. Leave `grad_year` null in that case rather than guess a number.
- **`opens_date` / `deadline_posted` / `deadline_real`**: use whichever of these three literally matches what the posting states — an application-open date, a stated/official deadline, or a confirmed-different real deadline, respectively. A vaguer timeline signal (e.g. "applications won't be reviewed until August 2026") is real and worth keeping, but if it doesn't literally match any of the three concepts, don't force it into the closest-sounding field — a wrong date in `deadline_real` is worse than a null one, since the MOC would sort/filter on a value that isn't actually a deadline. Put it in the Traps & Gotchas prose (as this skill already does) and, if only a month/year is known and not a day, it's fine to write a coarser `YYYY-MM` value into whichever field it does genuinely match rather than defaulting to null just because the day is unknown.
- This same check applies to the Tracker note's `deadline` field (mirrors Program's `deadline_real`) and to `careers_page` (often stated or discoverable in the same contact-research pass, not just the dossier).

---
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/reference/note-templates.md`
  ```diff
  - program_type:        # e.g. "Software", "Quant", "Research" — from the dossier's category/classification bucket
eligible_classes: []  # from dossier target_year if present, else []
grad_year:            # leave null unless the dossier states one explicitly — don't infer
role_type: internship
wave:                 # null unless known
opens_date:           # null unless known
deadline_posted:      # from dossier content if stated, else null
deadline_real:        # null unless independently confirmed — never assume posted == real
  + program_type:        # e.g. "Software", "Quant", "Research" — from the dossier's category/classification bucket
eligible_classes: []  # from dossier target_year, or from the fetched posting content — see "Backfill" rule above, don't leave [] if the Eligibility prose states one
grad_year:            # only a literal year the posting states — see "Backfill" rule above, don't infer one from a "must return to school" style constraint
role_type: internship
wave:                 # null unless known
opens_date:           # see "Backfill" rule above — only if the posting literally states an open date
deadline_posted:      # from dossier content if stated — see "Backfill" rule above
deadline_real:        # null unless independently confirmed — never assume posted == real; see "Backfill" rule above
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/reference/note-templates.md`
  ```diff
  - ## Traps & Gotchas
> [!WARNING]
> The thing most applicants get wrong about this program. (only include real traps found in the dossier/enrichment — never invent one)
## Prep Checklist
- [ ]
## Related Resources
- [[<dossier note>]] (List/Dossiers origin)
```

**Do not** write a `status` or `next` field on the Program note — the pipeline doc is explicit that Program notes are durable/static and only change when a fact about the program itself changes; funnel status belongs on the (not-yet-created) Applying note or the Tracker note.
  + ## Traps & Gotchas
> [!WARNING]
> The thing most applicants get wrong about this program. (only include real traps found in the dossier/enrichment — never invent one)
## Prep Checklist
- [ ] <3-5 real items, generated from this posting's own stated requirements/duties — see below>
## Related Resources
- [[<dossier note>]] (List/Dossiers origin)
```

**Do not** write a `status` or `next` field on the Program note — the pipeline doc is explicit that Program notes are durable/static and only change when a fact about the program itself changes; funnel status belongs on the (not-yet-created) Applying note or the Tracker note.

**Prep Checklist: the skill fills this, not a blank template.** `30_Order/Templates/Career/Program Template.md` itself (the vault's generic template, used when someone creates a Program note by hand) is correctly left as a bare `- [ ]` — a blank scaffold is the right contract for a template a human fills in from scratch. But `/promote-dossier` isn't starting from scratch: it already has the dossier's fetched posting content in hand, the same content it's already turning into the Eligibility and Traps prose above. Leaving the checklist bare when that source material is right there is the same class of bug as the frontmatter-backfill issue — known, derivable content going unused. Generate 3-5 concrete items straight from the posting's own "What You'll Do" / "Qualifications" / "Basic Qualifications" sections (e.g. Appian's real posting → "Review data structures, algorithms, and OOP fundamentals", "Prepare to discuss using AI coding tools critically, not just as autocomplete", "Have a portfolio example of full-stack work ready to discuss" — each traceable to a specific line in the fetched content, never generic interview-prep advice that isn't grounded in this specific JD).
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/reference/note-templates.md`
  ```diff
  - date_noted:           # the dossier's own date_found field
date_researched:       # today — the date this promotion actually happened
date_created: null    # filled in once/if an Applying note is created (Step 4)
date_applied: null
  + date_noted:           # the dossier's own date_found field
date_researched:       # today — the date this promotion actually happened
date_created:         # ALSO today — this is the day the Program/Contact/Tracker notes themselves were created, not the (much later, Step 4) Applying note. Fixed 2026-07-26: an earlier version of this template wrongly deferred this to Applying-note creation, which isn't even one of the pipeline doc's five listed Tracker milestones (noted/researched/created/applied/result) — "created" in that list means these three notes, written in one sitting, same day as date_researched.
date_applied: null
  ```
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/reference/note-templates.md`
  ```diff
  - ## Timeline
- **Noted:** <date_noted>
- **Researched:** <date_researched>
- **Created:** —
- **Applied:** —
- **Result:** —
  + ## Timeline
- **Noted:** <date_noted>
- **Researched:** <date_researched>
- **Created:** <date_created — same day as Researched, not left blank>
- **Applied:** —
- **Result:** —
  ```
- `Read` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/SKILL.md`
- `Edit` — `/home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/SKILL.md`
  ```diff
  - 2. Write the Program note, Contact note, and Tracker/Each One note per `reference/note-templates.md`, cross-linked as documented there (`list_origin`, `recruiter_contact`, `related_programs`, `program`, `contact`, `related_notes`).
  + 2. Write the Program note, Contact note, and Tracker/Each One note per `reference/note-templates.md`, cross-linked as documented there (`list_origin`, `recruiter_contact`, `related_programs`, `program`, `contact`, `related_notes`). Before finalizing, run the "Backfill structured fields from the same content the body prose is drawn from" check in `reference/note-templates.md` — a fact narrated in the Eligibility/Traps prose (class year, degree level, a stated date) must also land in its matching frontmatter field, not just the prose; `Programs/Programs MOC.md` sorts and filters on `deadline_real`/`eligible_classes`, so a fact that's only in prose is invisible to it. Fill the Prep Checklist with 3-5 real items grounded in the posting's own stated requirements/duties, not a bare checkbox. Tracker's `date_created` is today, same as `date_researched` — not deferred to a later Applying note.
  ```
- `mcp__jarvis__vault_write` — `{"path":"10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian.md","content":"---\nname: Software Engineering Intern at Appian\ncompany: Appian\nprogram_type: Fullstack\neligible_classes:\n  - Bachelor's\n  - Master's\ngrad_year:\nrole_type: internship\nwave:\nopens_date:\ndeadline_posted:\ndeadline_real:\npay_per_week: 2000\npay_currency: USD\nduration_weeks: 10\nbenefits:\n  - Health coverage\n  - Employee Assistance Program (EAP)\n  - Employee Stock Purchase Program (ESPP)\n  - Retirement/pension plan\n  - Tuition reimbursement\napplication_url: https://careers.appian.com/jobs/[REDACTED]\ncareers_page: https://careers.appian.com/students\nlist_origin: \"[[10_Areas/Career/Internships/List/Dossiers/[REDACTED]]]\"\napplying_note:\nrecruiter_contact: \"[[10_Areas/Career/Internships/Contacts/Each One/Software Engineering Intern - Appian]]\"\ntags:\n  - internship\n  - program\n---\n# Software Engineering Intern — Appian\nStatic research only — comp, eligibility, deadlines, traps, prep. Live status (applied, interview, offer) lives on the matching note in `20_Progress/Internship/Applying/`, linked via `applying_note` above.\n## Program Overview\nAppian is an enterprise low-code/AI process automation software company (Nasdaq: APPN), headquartered in McLean, VA. The Software Engineering Intern role sits within Appian Engineering, contributing to production-adjacent work across the AI-powered Process Automation platform: full-stack components, AI-assisted development tooling, debugging/systems thinking, and design/code-review collaboration. 10-week program. Pay stated on the posting as $50.00/hour ($8,666/month) — `pay_per_week` above is derived from that hourly rate at 40 hrs/week, not a figure Appian states directly.\n## Eligibility\nCurrently pursuing a Bachelor's or Master's degree in Computer Science or Computer Engineering (`eligible_classes` above); must be returning to school after the internship to continue degree requirements — that rules out graduating in the internship's own cycle but the posting never states a specific class year or grad year, so `grad_year` stays unset rather than a guessed number. Full-time (40 hrs/week) commitment required for the full 10 weeks. Considered for Summer 2027, students only.\n## Traps & Gotchas\n> [!WARNING]\n> In-person 5 days/week at the McLean, VA headquarters is mandatory (\"Interns in this program are expected to be in the office 5 days a week\"). Applications aren't reviewed and interviews aren't scheduled until August 2026 even though the posting is live now — this is a review-start signal, not a stated application-open date or deadline, so `opens_date`/`deadline_posted`/`deadline_real` stay unset above rather than forcing this fact into a field it doesn't actually match; the fact itself lives here instead. The posting also states \"Appian will not sponsor a new applicant for employment authorization for this position\" — that's a sponsorship exclusion, not necessarily an OPT exclusion, but confirm it doesn't conflict with OPT usage before investing further time.\n## Prep Checklist\n- [ ] Review data structures, algorithms, and object-oriented programming fundamentals — the posting names these directly as what you'll apply to \"full-stack components and engineering tasks\"\n- [ ] Practice using an AI coding assistant critically (generating AND reviewing/evaluating its output, not just accepting suggestions) — the posting explicitly wants \"AI fluency,\" not just familiarity\n- [ ] Prepare a debugging / root-cause-analysis story from a real project — matches \"support issue investigation, learn how to identify root causes\"\n- [ ] Have a portfolio project or prior technical internship ready to discuss — explicitly named as a Preferred Qualification\n- [ ] Practice explaining a technical decision in a design-discussion/code-review format — the posting lists \"design discussions, stand-ups, and code reviews\" as core day-to-day work\n## Related Resources\n- [[10_Areas/Career/Internships/List/Dossiers/[REDACTED]]] (List/Dossiers origin)\n"}`
- `mcp__jarvis__vault_write` — `{"path":"10_Areas/Career/Internships/Tracker/Each One/Software Engineering Intern - Appian.md","content":"---\ntype: tracker\nprogram: \"[[10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian]]\"\ncontact: \"[[10_Areas/Career/Internships/Contacts/Each One/Software Engineering Intern - Appian]]\"\ncompany: Appian\nurl: https://careers.appian.com/jobs/[REDACTED]\ndate_noted: 2026-07-25\ndate_researched: 2026-07-26\ndate_created: 2026-07-26\ndate_applied:\ndate_result:\nresult:\ndeadline:\nrelated_notes:\n  - \"[[10_Areas/Career/Internships/List/Dossiers/[REDACTED]]]\"\ntags:\n  - internship\n  - tracker\nnext:\n---\n# Software Engineering Intern — Appian\nThe dated index for this internship — source of truth for \"where does this stand\" until an Applying note exists (see [[30_Order/Workflows/Internship Pipeline]] Step 8).\n## Timeline\n- **Noted:** 2026-07-25\n- **Researched:** 2026-07-26\n- **Created:** 2026-07-26\n- **Applied:** —\n- **Result:** —\n## Next Action\nDecide whether to move this from Considering to actually applying — applications aren't reviewed until August 2026 per the Program note's Traps section, so there's no rush, but the in-person 5-day/week requirement is worth weighing before committing further.\n"}`
- `Bash` — `cd /home/anant_gupta/projects/work/internship-research-loop
source .venv/bin/activate && python -m pytest -q 2>&1 | tail -3
git add .claude/ CLAUDE.md
git status --short`
  ```
........................................................................ [ 83%]
..........................................                               [100%]
258 passed in 2.52s
A  .claude/agents/contact-researcher.md
A  .claude/agents/loop-verifier.md
A  .claude/settings.json
A  .claude/skills/promote-dossier/SKILL.md
A  .claude/skills/promote-dossier/reference/note-templates.md
A  .claude/skills/review-loop-change/SKILL.md
A  CLAUDE.md
  ```
- `Bash` — `cd /home/anant_gupta/projects/work/internship-research-loop
git commit -m "$(cat <<'EOF'
Add promote-dossier skill, contact-researcher/loop-verifier agents, review-loop-change skill

.claude/skills/promote-dossier/ — turns one List/Dossiers entry into a Program
note + Contacts/Each One note + Tracker/Each One note (Internship Pipeline.md
Step 3), human-consent-gated before any write. Templates copied verbatim from
the vault's own Program Template.md/Contact Template.md; Tracker/Each One has
no pre-existing vault template so its shape is authored from the pipeline
doc's own field description. Requires the Jarvis vault present in the same
working environment (git checkout sibling to this repo, or the jarvis MCP
tools) — documented explicitly rather than assumed, per this being the first
interactive (human-in-the-loop) writer this pipeline has ever had, distinct
from run_pipeline.py/recheck.py's non-interactive scoped-PAT writes.

.claude/agents/contact-researcher.md — exploratory subagent invoked by
promote-dossier's Step 3, using enrich.py's widened search primitives
(recruiter/university-recruiting search, GitHub org members, engineering
blog bylines, LinkedIn search-snippets). Never fabricates a contact; reports
"nothing found" honestly.

.claude/agents/loop-verifier.md — standalone pipeline health check (tests,
scheduled-run history via gh api, vault-vs-run-log dossier counts,
seen_ids/vault divergence, auto-filed issues), the automated version of this
project's prior manual audits (2026-07-19, 2026-07-25).

.claude/skills/review-loop-change/ — checks a diff against this repo's four
established conventions (zero-LLM unattended path, permissive-by-default
filtering, fail-closed write-gate ordering, cited-real-data rule comments)
before it ships. Built as a skill rather than an agent — reasoning is in the
skill file's own "why a skill" section.

.claude/settings.json — pytest/safe-git-reads/gh-reads allowed without
prompting; git push and gh secret modification explicitly require
confirmation every time (permissions.ask), never silently allowed or denied.

CLAUDE.md — documents the three note-template contracts (required fields,
always present even as null) and the explicit agent-vs-script judgment call
for each of contact research / promotion / verification / review.

Verified live against a real dossier (Appian — Software Engineering Intern):
promote-dossier run end-to-end including the write step, contact-researcher
found real sourced contacts, and a real gap this surfaced (structured
frontmatter fields left null while the same fact was already narrated in
body prose — eligible_classes, Tracker's date_created) is fixed in this
commit, not left for later.

258/258 tests passing (no pipeline code touched by this commit).
EOF
)"
git log --oneline -5`
  ```
[master f56ac8c] Add promote-dossier skill, contact-researcher/loop-verifier agents, review-loop-change skill
 7 files changed, 535 insertions(+)
 create mode 100644 .claude/agents/contact-researcher.md
 create mode 100644 .claude/agents/loop-verifier.md
 create mode 100644 .claude/settings.json
 create mode 100644 .claude/skills/promote-dossier/SKILL.md
 create mode 100644 .claude/skills/promote-dossier/reference/note-templates.md
 create mode 100644 .claude/skills/review-loop-change/SKILL.md
 create mode 100644 CLAUDE.md
f56ac8c Add promote-dossier skill, contact-researcher/loop-verifier agents, review-loop-change skill
6622bca Priority-bucket classification, CS-relevance gate, widened contact research
ba2bdcd Update state + logs — 2026-07-26
1c3ddc4 Update state + logs — 2026-07-26
ea1a38b Update state + logs — 2026-07-25
  ```
- `Bash` — `cd /home/anant_gupta/projects/work/internship-research-loop
git push origin master
git log --oneline -5 origin/master 2>&1 || git fetch origin && git log --oneline -5 origin/master`
  ```
To https://github.com/gupta-builds/internship-research-loop.git
   ba2bdcd..f56ac8c  master -> master
f56ac8c Add promote-dossier skill, contact-researcher/loop-verifier agents, review-loop-change skill
6622bca Priority-bucket classification, CS-relevance gate, widened contact research
ba2bdcd Update state + logs — 2026-07-26
1c3ddc4 Update state + logs — 2026-07-26
ea1a38b Update state + logs — 2026-07-25
f56ac8c Add promote-dossier skill, contact-researcher/loop-verifier agents, review-loop-change skill
6622bca Priority-bucket classification, CS-relevance gate, widened contact research
ba2bdcd Update state + logs — 2026-07-26
1c3ddc4 Update state + logs — 2026-07-26
ea1a38b Update state + logs — 2026-07-25
  ```
- `Agent` — `{"description":"Run loop-verifier health check","subagent_type":"loop-verifier","prompt":"Run a full health check of gupta-builds/internship-research-loop right now (2026-07-26). This is the first real run of this agent — it was just built and pushed to origin/master (commit f56ac8c on top of 6622bca, which added core/classify.py, core/relevance.py, the widened enrich.py, and the priority-bucket vault_writer changes). Report real, evidence-cited findings per your standard five-check format. Note: since core/classify.py's bucket-folder writing landed in this same push, the live vault's dossiers under List/Dossiers/ almost certainly still predate it (flat, uid-named files, no bucket subfolders) — confirm this live rather than assuming it, it's directly relevant to your check #3.","run_in_background":false}`

## You

<task-notification>
<task-id>b0w0wai02</task-id>
<tool-use-id>[REDACTED]</tool-use-id>
<output-file>/tmp/claude-1001/-home-anant-gupta-projects-work-internship-research-loop/[REDACTED]/tasks/b0w0wai02.output</output-file>
<status>killed</status>
<summary>Background command "find ~/.claude/agents -maxdepth 1 -iname "*.md" 2&gt;/dev/null | head -5
find / -maxdepth 8 -path "*/.claude/agents/*.md" 2&gt;/dev/null | grep -v "^/home/anant_gupta/.claude/agents" | head -10
echo "=== check plugin agents for example frontmatter ==="
find / -path "*agents*" -iname "*.md" 2&gt;/dev/null | grep -iv "node_modules\|/.venv/\|/.git/" | grep -i "code-reviewer\|explore" | head -10" was stopped</summary>
</task-notification>

## Claude

No response requested.

## You

There are faults in the current dossier listings - ```The core fact: nothing shipped

33 new dossiers landed in the last ~2 days (94 → 127). But the commit log shows zero code commits since I wrote Prompt 4 — only routine "Update state + logs" and one "Recheck log" entry. Prompt 4 was never run. Every one of those 33 new dossiers went through the exact same unfixed gate that produced the Databricks/Mosaic/Aquatic/Google bugs two days ago. And it shows: I found the same bug patterns again, plus one new one, in a fraction of the time it took to find them the first time.

The 201 cap is still not in code — run_pipeline.py:66 unchanged, MAX_NEW_WRITES_PER_RUN = 18, no per-bucket split, no warnings. This is no longer theoretical: 1 - AI & ML/ is sitting at exactly 50 files right now — if the cap you designed were live, it would already be refusing new writes to that bucket.

What I verified, with real evidence (not sampling guesses)

Confirmed real bugs, same classes as before, now recurring:
- Conagra "Demand Science Rotational Analyst" — a business/forecasting rotational program (zero programming anywhere in the posting; "general understanding of business, financial concepts") — passed the CS-relevance gate, landed in Other. Same bug class as Databricks: stage1_reject has no pattern for rotational-analyst-style business roles.
- Optiver "Quantitative Research Intern, PhD" resurfaced — this is the literal same posting I manually deleted two days ago (matched by Greenhouse job ID 8451781002). Two real problems here: (1) it's PhD-only and should never pass degrees_allow, but Greenhouse carries no structured degree field, so the permissive-on-missing-data rule waves it through — the gate is structurally blind on 5 of 8 sources for degree requirements; (2) my manual rejection two days ago taught the system nothing — there's no feedback path, so the same wrong match just comes back. This is exactly the gap the Improvement Plan's Priority 4 already named and nobody's built yet.
- Virtu Financial — a genuine triple duplicate. Three separate dossier files (2027 Internship - Software Engineer, Software Engineer Intern - Software Engineer, Software Engineer Intern) all point to the exact same URL (greenhouse.io/virtu/jobs/8624410002), just sourced through Greenhouse/zshah101/vanshb03 with different title strings each time. Dedup missed all three.
- Palantir Intel — duplicate across two different buckets. Same Lever job ID, sourced via SimplifyJobs (landed in AI/ML) and zshah101 (landed in Fullstack) — same posting classified two different ways depending on which source's copy got matched first.

Not a bug, correctly working as designed: Tower Research's "Quantitative Developer Intern" — I initially suspected this was another "machine learning in a majors list" false positive, but the real content genuinely describes engineers doing "low-latency programming, FPGA technology, hardware acceleration and machine learning" as real day-to-day work. It's AI/ML because AI/ML is checked first in the classifier's deliberate ordering, and the signal is real, not incidental. Worth knowing the line here is blurrier than I assumed, not that the code is wrong.

Direct answers to your questions

- Are these real, good internships? Yes — every posting I read in full (Tower Research, Optiver, Conagra, DE Shaw) is a real, substantive, currently-open listing. Discovery itself works. The damage is entirely at the classification/gate/dedup layer downstream of a valid fetch.
- Are we satisfying all criteria? Mostly, but with a real hole: OPT and CS-relevance both get a content-level check; degree requirements don't, and that's now demonstrated, not theoretical.
- Have we found all the useful internships out there? Can't fully answer, but the pattern above tells you the honest sequencing question: adding more sources (which niche-targeting requires) makes every one of these bugs worse, not better — more sources means more chances for the same posting to arrive under a different company-name spelling, more chances for a non-engineering role to slip the gate. Widening intake before fixing intake quality multiplies the mess.

Where I think this leaves us

Prompt 4 (already written, sitting in Runs/Claude Code Prompts.md, never executed) covers the count-limit, and three of what are now four confirmed bug classes. It needs one addition — the degree-requirement content check, mirroring how OPT already works — and it needs to actually run this time.

The FAANG/Fortune 100/YC-backed direction is a good next lever, but I'd sequence it after Prompt 4 ships and you've watched one clean cycle, not before — otherwise you're pointing a leaky funnel at a bigger firehose.

Want me to update Prompt 4 with the degree-check addition now (still just editing the prompt file, not touching the repo), or do you want to talk through the niche-targeting design first while it's fresh?```. There have not been many files pushed to programs because the dossier is not entirely built. We lack multiple things right now. The count that is being talked about is a notification that arrives on the trackers and dashboard of jarvis. When hit 50 on each you mention it to me in the codebase also if necessary. The notes are not being interconnected or related to anything. These are just notes floating around according to obsidian. There should interlinks in the frontmatter of each internship the template needs to have a must `10_Areas/Career/Internships/List/Dossiers MOC` interlink. Rest should be interlinked if they are from the same company, the removed ones are going to be interlinked to this: `10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC` and moved to `10_Areas/Career/Internships/List/Dossiers/Viewed`. The comapny interlink will still be there but the removed is clearly stated. Except that the template for each and every internship that I see written down in jarvis varies per internship. The content from the entire job posting should be pasted into jarvis and in a readable manner satisfying the `30_Order/Standards/Internship Notes Standard` & other rules noted files(`20_Progress/Internship/Building System`). I want you to have a very detailed understanding of what exactly that is being talked about over here. Do your research and verify everything that has not beein built correctly for the dossiers. Based on that, let's write a prompt for brand new session running sonnet 5 to finish the task. We need to improve our current dossier setup based on everything that was mentioned in the reply and content explained above. After that we have tons of niches to apply to this process. Specific runs based. So we have a long way of planning to do for this step still. Let's first reflect these changes that were mentioned.

## Claude

Found direct filesystem access to the real Jarvis vault at `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/` (no MCP needed). Let me do the deep research now — reading the standards docs, the actual dossier state, and the existing Prompt 4.

Now I have the full picture — let me check one more piece (recheck.py's exact current delete behavior, already confirmed) and then write up the findings. First, the vault-side standard document that's currently an empty stub — everything else in this system cites it, so it needs real content before the code prompt can reference it meaningfully.

Let me add the live "at-capacity" notification directly to the vault dashboard now — this is a markdown edit, not a code change, so I can do it immediately rather than deferring it to the coding session.

Now Task B (add the Conagra rotational-analyst pattern to the existing Databricks PM finding) and Task D (add the Virtu/Palantir real evidence):

This reads correctly. Let me fix the frontmatter dates and add a note about the important prerequisite the fresh session will need (the vault checkout/access path).

Now let's add the dated Build Log entry documenting this verification pass, matching the vault's own established convention.

All the vault-side reflection is done. Here's what I found and wrote:

**Verified against the real vault** (`/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis`, direct filesystem — Obsidian's MCP tools had disconnected mid-session):

- Prompt 4 (written 2026-07-26) is confirmed **still never run** — zero commits against it.
- Live bucket counts right now: `1 - AI & ML` 53, `2 - Fullstack` 21, `3 - CyS & Finance` 54, `Other` 11 — **two buckets are already past 50**, so the cap question is no longer theoretical.
- All four original bugs (Databricks PM, Mosaic "threat", Aquatic/Google dedup, Google extraction) are still live and unfixed. The pasted report's new findings check out: Conagra rotational-analyst (same class as Databricks), Virtu triple-dup and Palantir cross-bucket dup (same `cross_source_key()` gap, now with matching job IDs across all variant URLs — strong evidence a URL/job-ID fix is the right general solution), and Optiver's PhD posting resurfacing (a genuinely new gap: no source has a structured degree field, and there's no content-level PhD check the way there is for OPT).
- `30_Order/Standards/Internship Notes Standard.md` and `Viewed/Removed Dossiers MOC.md` — both referenced everywhere, **both were 0-byte empty stubs**. Nothing was ever actually defined.
- Dossier template is structurally consistent (good) but the *content* is raw scraped junk (Conagra's "About Us" paragraph is duplicated verbatim; ATS chrome jammed into text with no line breaks) and **zero interlinking** exists — no dossier points at the Dossiers MOC, no company clustering, nothing.

**Written directly (vault-side, no code touched):**
1. Real content for `Internship Notes Standard.md` — the actual contract now: required `notes:` MOC-link field, `company/<slug>` tag for same-company clustering (chose a tag over a maintained link list — no per-company hub note exists, and backfilling N-1 dossiers on every new arrival is exactly the kind of cost this repo avoids elsewhere), move-not-delete + `Removed Dossiers MOC` linking on removal, deterministic (zero-LLM) content-structuring rules for readability, and the cap reframed as a notification.
2. A live `dataviewjs` capacity table on `Dossiers MOC.md` — this *is* the "notification on the dashboard" you asked for, already working, no code needed.
3. Prompt 4 revised in place (kept, not wiped, since it never ran) — Tasks A/B/D updated with the new recurring evidence, plus four new tasks: **F** (degree-content gate, explicitly *not* building a rejection-feedback-loop yet — that's Priority 4's job once Priority 1 has real data), **G** (interlinking), **H** (`recheck.py` move-not-delete), **I** (readable structured content).
4. A dated Build Log entry tying it all together.

One judgment call worth flagging: I made the cap a *soft* notification per your instruction rather than a hard write-refusal, on the reasoning that a hard block would violate this codebase's own permissive-by-default asymmetry (a dropped real posting costs more than a full bucket does). Redirect me if you actually wanted a hard stop at 50.

Ready to run the revised Prompt 4 against the repo whenever you want — it's not run yet, same as before.

**Tool calls:**

- `Bash` — `cat /home/anant_gupta/projects/work/internship-research-loop/grade_resume.py | head -25
echo "=== jarvis-checkout populated now? ==="
ls -la /home/anant_gupta/projects/work/internship-research-loop/jarvis-checkout/ 2>/dev/null
echo "=== check /mnt/d for a Jarvis vault ==="
ls /mnt/d/Users/_Anant/ 2>/dev/null
find /mnt/d -maxdepth 3 -iname "*jarvis*" 2>/dev/null
echo "=== check /mnt for other drives ==="
ls /mnt/ 2>/dev/null`
  ```
#!/usr/bin/env python3
"""Layer 6 — resume grader: keyword-overlap scorer, no LLM, no network.

Ranks Main Resume.md's `#skill/*`-tagged bullets against a pasted JD so the
top-third tailoring step of the Internship Pipeline starts from evidence,
not vibes:

    python grade_resume.py jd.txt            # or: pbpaste | python grade_resume.py -
    python grade_resume.py jd.txt --resume "path/to/Main Resume.md"
"""
import argparse
import re
import sys
from collections import Counter

DEFAULT_RESUME = ("/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/"
                  "Internship/Resumes/Main Resume.md")
# Just enough stopwords to keep JD boilerplate from scoring; not a linguistics project.
STOP = set("""a an and are as at be by for from has have in is it of on or our the
to we will with you your this that they them their its into within using able
work team who what when where required preferred qualifications responsibilities
experience years strong skills ability including etc more than least about
""".split())
_TAG_RE = re.compile(r"#skill/[\w-]+")
_WORD_RE = re.compile(r"[a-z][a-z0-9.+#/-]{2,}")
=== jarvis-checkout populated now? ===
total 8
drwxr-xr-x  2 anant_gupta anant_gupta 4096 Jul 17 15:24 .
drwxr-xr-x 15 anant_gupta anant_gupta 4096 Jul 26 11:35 ..
=== check /mnt/d for a Jarvis vault ===
00_Inbox
10_Areas
20_Progress
30_Resources
99_Archive
Downloads
Favorites
Inbox
Media
Music
Videos
=== check /mnt for other drives ===
c
d
wsl
wslg
  ```
- `Bash` — `echo "=== does the literal DEFAULT_RESUME path exist? ==="
ls -la "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Resumes/" 2>&1
echo "=== what's actually in /mnt/d/Users/_Anant/10_Areas/ ==="
ls "/mnt/d/Users/_Anant/10_Areas/" 2>&1
echo "=== search for a folder literally named Jarvis anywhere under /mnt/d ==="
find /mnt/d -maxdepth 5 -iname "Jarvis" -type d 2>/dev/null
echo "=== does /mnt/d/Users/_Anant/10_Areas/Career/Internships exist (the vault path used throughout this repo)? ==="
ls "/mnt/d/Users/_Anant/10_Areas/Career/Internships/" 2>&1 | head -20`
  ```
=== does the literal DEFAULT_RESUME path exist? ===
total 252
drwxrwxrwx 1 anant_gupta anant_gupta   4096 Jul 25 17:12 .
drwxrwxrwx 1 anant_gupta anant_gupta   4096 Jul 29 13:17 ..
drwxrwxrwx 1 anant_gupta anant_gupta   4096 Jul 25 17:12 Altered
-rwxrwxrwx 1 anant_gupta anant_gupta   4714 Jul 16 19:57 Main Resume.md
-rwxrwxrwx 1 anant_gupta anant_gupta 247465 May  1 07:00 Main Resume.pdf
=== what's actually in /mnt/d/Users/_Anant/10_Areas/ ===
DevConfig
Documents
Finance
Job & Apartment
Real coding
UMN
=== search for a folder literally named Jarvis anywhere under /mnt/d ===
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis
=== does /mnt/d/Users/_Anant/10_Areas/Career/Internships exist (the vault path used throughout this repo)? ===
ls: cannot access '/mnt/d/Users/_Anant/10_Areas/Career/Internships/': No such file or directory
  ```
- `Bash` — `JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== vault root ===" && ls "$JARVIS"
echo "=== 30_Order/Standards ===" && find "$JARVIS/30_Order" -iname "*standard*" 2>/dev/null
echo "=== 20_Progress/Internship/Building System ===" && ls "$JARVIS/20_Progress/Internship/Building System/" 2>/dev/null
echo "=== Runs dir ===" && find "$JARVIS" -maxdepth 4 -iname "Runs" -type d 2>/dev/null
find "$JARVIS" -iname "*Claude Code Prompts*" 2>/dev/null
echo "=== Dossiers dir ===" && ls "$JARVIS/10_Areas/Career/Internships/List/Dossiers/" | head -30
echo "=== count dossiers ===" && ls "$JARVIS/10_Areas/Career/Internships/List/Dossiers/" | grep -c "\.md$"
echo "=== is there a Viewed subfolder already? ===" && ls "$JARVIS/10_Areas/Career/Internships/List/Dossiers/Viewed/" 2>&1
echo "=== is there a Dossiers MOC already? ===" && find "$JARVIS/10_Areas/Career/Internships" -iname "*MOC*" 2>/dev/null`
  ```
=== vault root ===
00_Dashboard.md
10_Areas
20_Progress
30_Order
40_Resources
50_Archive
60_Claude
AGENTS.md
CLAUDE.md
HUMAN_WRITING.md
excalidraw.log
=== 30_Order/Standards ===
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Concept Standard.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Course Week Standard.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Daily Workflow Standard.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Evergreen Standard.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Internship Notes Standard.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Project Standard.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Source Summary Standard.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/v3/standard-schema.cjs
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/v3/standard-schema.d.cts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/v3/standard-schema.d.ts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/v3/standard-schema.js
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/src/v3/standard-schema.ts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/v4/core/standard-schema.cjs
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/v4/core/standard-schema.d.cts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/v4/core/standard-schema.d.ts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/v4/core/standard-schema.js
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/src/v3/tests/standard-schema.test.ts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/src/v4/core/standard-schema.ts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/esm/server/webStandardStreamableHttp.d.ts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/esm/server/webStandardStreamableHttp.d.ts.map
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/esm/server/webStandardStreamableHttp.js
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/esm/server/webStandardStreamableHttp.js.map
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/cjs/server/webStandardStreamableHttp.d.ts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/cjs/server/webStandardStreamableHttp.d.ts.map
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/cjs/server/webStandardStreamableHttp.js
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/cjs/server/webStandardStreamableHttp.js.map
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/zod/src/v4/classic/tests/standard-schema.test.ts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/esm/examples/server/honoWebStandardStreamableHttp.d.ts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/esm/examples/server/honoWebStandardStreamableHttp.d.ts.map
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/esm/examples/server/honoWebStandardStreamableHttp.js
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/esm/examples/server/honoWebStandardStreamableHttp.js.map
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/cjs/examples/server/honoWebStandardStreamableHttp.d.ts
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/cjs/examples/server/honoWebStandardStreamableHttp.d.ts.map
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/cjs/examples/server/honoWebStandardStreamableHttp.js
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/System/excalidraw-mcp/node_modules/@modelcontextprotocol/sdk/dist/cjs/examples/server/honoWebStandardStreamableHttp.js.map
=== 20_Progress/Internship/Building System ===
Internship Research Loop — Full Pipeline.excalidraw
Research Loop - Implementation Plan.md
Research Loop - Improvement Plan.md
Research Loop - Resources.md
Runs
Source of Truth.md
System - Build Log.md
=== Runs dir ===
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md
=== Dossiers dir ===
1 - AI & ML
2 - Fullstack
3 - CyS & Finance
Dossiers-to-Create.md
Other
Viewed
=== count dossiers ===
1
=== is there a Viewed subfolder already? ===
Removed Dossiers MOC.md
=== is there a Dossiers MOC already? ===
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/Contacts/Contacts MOC.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers MOC.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/Programs/Programs MOC.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC.md
  ```
- `Bash` — `JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== recursive dossier count per bucket ==="
for d in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other"; do
  echo "$d: $(find "$JARVIS/10_Areas/Career/Internships/List/Dossiers/$d" -maxdepth 1 -iname "*.md" 2>/dev/null | wc -l)"
done
echo "Viewed: $(find "$JARVIS/10_Areas/Career/Internships/List/Dossiers/Viewed" -maxdepth 1 -iname "*.md" 2>/dev/null | wc -l)"
echo "flat root: $(find "$JARVIS/10_Areas/Career/Internships/List/Dossiers" -maxdepth 1 -iname "*.md" 2>/dev/null | wc -l)"
echo "TOTAL recursive: $(find "$JARVIS/10_Areas/Career/Internships/List/Dossiers" -iname "*.md" 2>/dev/null | wc -l)"`
  ```
=== recursive dossier count per bucket ===
1 - AI & ML: 53
2 - Fullstack: 21
3 - CyS & Finance: 54
Other: 11
Viewed: 1
flat root: 1
TOTAL recursive: 141
  ```
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Internship Notes Standard.md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers MOC.md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC.md`
- `Bash` — `JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== sample dossiers from each bucket (filenames) ==="
find "$JARVIS/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML" -iname "*.md" | head -5
echo "---"
find "$JARVIS/10_Areas/Career/Internships/List/Dossiers/Other" -iname "*.md" | head -5
echo "=== the one flat-root dossier still there ==="
find "$JARVIS/10_Areas/Career/Internships/List/Dossiers" -maxdepth 1 -iname "*.md"`
  ```
=== sample dossiers from each bucket (filenames) ===
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/A.I. Developer Co-Op (Boston, MA) - Manhattan Associates.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/Agentic Software Engineering intern - Toshiba Global Commerce.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/AI Engineering Intern - Toshiba Global Commerce.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/AI Operations Intern - Naukr AI - Acds.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/AI Operations Intern-Caddell Reynolds - Acds.md
---
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Other/2026-2027 Information Technology - Software Engineer - Intern - Chevron Corporation.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Other/Demand Science Rotational Analyst - Conagra Brands.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Other/FPGA Digital Design Engineering Intern (January 2027) (4-16 months) - Kepler.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Other/Intern, Software Engineering - Moog.md
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Other/RenderATL - 2027 US Software Engineering Internship - Axon.md
=== the one flat-root dossier still there ===
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create.md
  ```
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Other/Demand Science Rotational Analyst - Conagra Brands.md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML/A.I. Developer Co-Op (Boston, MA) - Manhattan Associates.md`
- `Bash` — `JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== Internship Notes Standard.md ===" && wc -c "$JARVIS/30_Order/Standards/Internship Notes Standard.md" && ls -la "$JARVIS/30_Order/Standards/Internship Notes Standard.md"
echo "=== Removed Dossiers MOC.md ===" && wc -c "$JARVIS/10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC.md"
echo "=== Dossiers-to-Create.md ===" && wc -l "$JARVIS/10_Areas/Career/Internships/List/Dossiers-to-Create.md"
cat "$JARVIS/10_Areas/Career/Internships/List/Dossiers-to-Create.md"`
  ```
Exit code 1
=== Internship Notes Standard.md ===
0 /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Internship Notes Standard.md
-rwxrwxrwx 1 anant_gupta anant_gupta 0 Jul 27 16:18 /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Internship Notes Standard.md
=== Removed Dossiers MOC.md ===
0 /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC.md
=== Dossiers-to-Create.md ===
wc: /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers-to-Create.md: No such file or directory
cat: /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers-to-Create.md: No such file or directory
  ```
- `Bash` — `JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
cat "$JARVIS/10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create.md"`
  ```
---
type: evergreen
status: active
created: 2026-07-26
tags:
  - internship
  - process
  - automation
notes:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[Dossiers MOC]]"
next: "[[20_Progress/Internship/Building System/Claude Code Prompts]] for the priority-classification build that sorts these into subfolders."
---
# Dossiers — How Notes Get Created Here
==Nothing in this folder is hand-created, ever.== Every file here is written by `gupta-builds/internship-research-loop` (GitHub Actions, hourly, six live sources as of 2026-07-25). This note exists so the gate is legible without reading the codebase — what has to be true about a posting before it lands here, and how it gets sorted once it does.
## The Gate, In Order
1. **Eligibility** — US location (permissive: no data or ambiguous strings pass, only an affirmative foreign signal rejects), OPT-compatible (excluded only on an explicit citizenship/clearance/no-OPT signal, never a guessed allowlist), Bachelor's-eligible (permissive on missing data), and timing (Summer 2027 and Winter 2027 weighted equally high, Spring 2027 wanted but lower-weight — see [[Source of Truth]] for the full three-criteria history).
2. **CS/software relevance** — a new hard rule: the posting has to be genuinely software engineering at its core. Adjacent fields (hardware, robotics, astrophysics, space, firmware) aren't auto-excluded, but they only pass if the specific posting's content shows real software/CS relevance a real fit — not just adjacency. Anything that isn't software engineering at all (analyst, risk, tax, sports-performance-analytics roles) is rejected outright, before it reaches step 3 — it does not land in `Other` either.
3. **Priority classification** — every survivor gets sorted into exactly one subfolder: `1 - AI & ML/`, `2 - Fullstack/`, `3 - CyS & Finance/`, or `Other/` (real software engineering that just isn't one of the three named niches — same research rigor applies to `Other`, it is not a lesser bucket). Each dossier carries a short callout at the top stating which real signal from the posting drove the classification — never a numeric "Priority N" label; the folder location already encodes the category.
## What Does Not Belong Here
A lead you found yourself — career fair, LinkedIn, a referral — never becomes a dossier. It goes straight into `Programs/Considering/` (or `Serious/`) per [[30_Order/Workflows/Internship Pipeline]] Step 1, skipping this folder entirely.
## What Good Dossier Content Looks Like
- **Real posting substance, not chrome.** Role summary, requirements, comp if stated — verbatim/structural extraction, trimmed of nav/form/EEO boilerplate. If a fetch comes back thin (form-only page, JS-rendered content that didn't load), that's a real extraction gap to flag, not something to pad with invented detail.
- **The classification callout cites a real signal**, quoted or paraphrased from the actual posting or company description — never a generic "seems AI-related" guess. If you can't point to the sentence that justified the bucket, the classification is wrong or the content is too thin to classify yet.
- **One dossier, one posting.** A duplicate role at a different location or a different req number is a separate dossier — don't merge two real postings into one note to save a file.
> [!NOTE]
> If you find a dossier with a classification you disagree with, or content that's clearly wrong (wrong company matched, stale/closed posting still marked active), fix it directly and note what changed — this is exactly the kind of real miss that should turn into a permanent rule fix upstream in the codebase, not just a one-off correction. See [[20_Progress/Internship/Building System/Research Loop - Improvement Plan]] Priority 4 for the feedback-loop design this is meant to feed.
## The Count Limit — Designed 2026-07-26
> [!IMPORTANT]
> This folder (excluding `Viewed/`) caps at **201 files**: 50 per priority folder (`1 - AI & ML/`, `2 - Fullstack/`, `3 - CyS & Finance/`, `Other/`) plus this one directive note at the root. Each push to the vault writes **at most ~10 new dossiers** — a starting split of roughly 3 AI/ML, 3 Fullstack, 3 CyS & Finance, 1 Other, meant to be tuned against real data over time, not treated as fixed. **Warning stages at 150, 170, 190, and 200** total files force an explicit review before the cap is ever hit — the whole point is that every push is a deliberate, reviewed decision about which internships are actually worth a human's attention, not a firehose. **Not yet implemented in `run_pipeline.py`** — see [[System - Build Log]]'s Open section.
## Status
The manual reorganization (2026-07-26) sorted the 117 dossiers that had accumulated flat into the four priority subfolders by hand, applying the same rules the codebase is supposed to enforce going forward. **The classification/routing code is now confirmed live**: `core/relevance.py` and `core/classify.py` exist on `master`, verified directly — see [[System - Build Log]]. Not yet confirmed: whether a real fresh dossier has landed correctly classified since the push (check the next `run.yml` output directly). The count-limit spec below is still not implemented regardless. [[Dossiers MOC]] keeps surfacing both sorted and flat states in case anything still lands unsorted.
  ```
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/System - Build Log.md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Research Loop - Improvement Plan.md`
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md`
- `Bash` — `JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== Programs MOC frontmatter ===" && head -20 "$JARVIS/10_Areas/Career/Internships/Programs/Programs MOC.md"
echo "=== Contacts MOC frontmatter ===" && head -20 "$JARVIS/10_Areas/Career/Internships/Contacts/Contacts MOC.md"
echo "=== a real Program note frontmatter (Appian, since it was actually promoted) ===" && find "$JARVIS/10_Areas/Career/Internships/Programs" -iname "*ppian*"
echo "=== Source of Truth (head) ===" && head -40 "$JARVIS/20_Progress/Internship/Building System/Source of Truth.md"`
  ```
=== Programs MOC frontmatter ===
---
type: evergreen
status: active
created: 2026-07-26
tags:
  - internship
  - moc
notes:
  - "[[10_Areas/Career/Internships/Programs/Programs-to-Create]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[10_Areas/Career/Internships/Tracker/Internship - Dashboard]]"
---
# Programs — Map of Content
==Everything currently in `Programs/`, live.== This is a folder-scoped visualization, not a replacement for [[10_Areas/Career/Internships/Tracker/Internship - Dashboard]] — that dashboard also joins in live Applying status; this note only shows what's actually sitting in `Programs/` right now, split by folder. See [[10_Areas/Career/Internships/Programs/Programs-to-Create]] for how a note gets here at all.
## Serious — Pursuing Now
```dataview
TABLE
  company,
  wave,
  deadline_real as "Real Deadline",
=== Contacts MOC frontmatter ===
---
type: evergreen
status: active
created: 2026-07-26
notes:
  - "[[10_Areas/Career/Internships/Contacts/Each One/Contacts-to-Create]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
tags:
  - internship
  - moc
---
# Contacts — Map of Content
==Everything currently in `Contacts/Each One/`, live, by relationship state.== See [[10_Areas/Career/Internships/Contacts/Each One/Contacts-to-Create]] for how a note gets here and what belongs in it.
## Ongoing — Active Right Now
```dataview
TABLE company, role, relationship, last_contact_date
FROM "10_Areas/Career/Internships/Contacts/Each One/Ongoing"
SORT last_contact_date DESC
```
## Come Back — Something Specific Still Worth Raising
=== a real Program note frontmatter (Appian, since it was actually promoted) ===
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian.md
=== Source of Truth (head) ===
---
type: project
status: tree
created: 2026-07-19
updated: 2026-07-26
related_progress:
  - "[[Research Loop - Implementation Plan]]"
  - "[[20_Progress/Internship/Building System/Runs/Phases Run]]"
  - "[[System - Build Log]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
tags:
  - internship
  - automation
  - system-design
next: "The 2026-07-26 code (persona config, CS-relevance gate, priority classification, dossier template v2, contact-research widening) is committed and pushed — confirmed live via gh api. Next: verify it's actually firing correctly against a fresh hourly run, and implement the dossier count-limit spec (still not in code)."
---
# Internship Research Loop — Source of Truth
==The complete, closed statement of what this system is built to do — target scope, current form, in one place.== This is not a build report — [[System - Build Log]] carries the full dated history of every session, what shipped, what's still uncommitted, and why each decision landed where it did. Read that note for *how we got here*; read this note for *what's true about the finished shape right now*.
## What This System Is
Two halves, deliberately different in rigor. **Discovery** is a GitHub Actions workflow (`gupta-builds/internship-research-loop`) that polls eight internship-listing sources hourly, filters through a zero-Claude/Anthropic-LLM deterministic gate, and writes survivors into `10_Areas/Career/Internships/List/Dossiers/` — mechanical, unattended, cheap by design. **Promotion onward** is entirely manual, human-judgment-driven, and stays that way on purpose: a dossier becoming a Program note, a Program note turning into real outreach, an outreach turning into a submitted application — none of that is automated, none of it should be.
## The End Goal, Stated Plainly
A real Summer 2027, Winter 2027 (Dec-Jan), or lower-priority Spring 2027 SWE/AI internship, open in the US and OPT-eligible, reaches this vault within an hour of going live anywhere it's discoverable — already carrying enough real content that deciding whether to pursue it takes 60 seconds, not a webpage visit. **A dossier landing in `List/Dossiers/` is not the finish line.** The finish line is a submitted application, and the loop only earns its cost once dossiers are actually promoted through [[30_Order/Workflows/Internship Pipeline]] into real Program notes, real contact research, and real outreach. The success metric is applications submitted per week — not dossiers written, not tests passing, not folders looking tidy.
## The Four Hard Gates — What Has To Be True Before A Dossier Exists
All four share one design principle, applied consistently since the very first rule (`locations_allow`, Phase 2): **permissive by default, exclude only on an explicit negative signal.** A false exclusion silently loses a real opportunity with nothing to show for it; a false inclusion costs one human screening read. That asymmetry is why every rule below errs toward keeping, not discarding, when a signal is ambiguous.
1. **Timing** — `terms: ["Summer 2027", "Winter 2027", "Spring 2027"]` in `core/profile.yaml`. Summer 2027 and Winter 2027 (genuinely Dec 2026-Jan 2027, not the full "Winter" label bucket) are equally high priority; Spring 2027 is wanted but explicitly lower-weighted (`terms_weight`), never a second pass/fail gate.
2. **Location** — United States. An affirmative US signal always passes; an affirmative foreign signal always rejects; anything ambiguous (no data, "Remote," "Multiple Locations") passes.
3. **OPT eligibility** — checked per posting, not per company (the same company can differ role-to-role — proven directly by the 2026-07-19 dossier audit finding Palantir's US Government role citizenship-gated while its Commercial role wasn't). OPT ≠ H-1B sponsorship; "no visa sponsorship" alone is never an exclusion signal. Excluded only on an explicit citizenship/US-person requirement, a security-clearance requirement, or an explicit "OPT/CPT not accepted" statement.
4. **CS/software relevance — added 2026-07-26.** A listing must be genuinely computer science / software engineering at its core, checked *after* the three criteria above, before a dossier is ever written. Adjacent fields (hardware, robotics, astrophysics, space, firmware) are not auto-excluded — they pass only if the specific posting's real content shows genuine software/CS relevance the candidate is suited for (grounded in `Main Resume.md` and `Engineer Edge Roadmap.md`, not guessed). Anything with no software content at all (financial/risk analyst, tax, sports-performance analytics, pure trading-strategy research) is rejected outright and does not land anywhere — not even `Other`.
## Priority Classification — Where A Surviving Dossier Lands
Everything that clears all four gates gets sorted into exactly one subfolder under `List/Dossiers/`, with a short callout at the top citing the real signal that drove the call — never a numeric "Priority N" label; the folder itself is the label:
- **`1 - AI & ML/`** — LLM, RAG, agents, ML infrastructure, applied AI, deep learning signals.
- **`2 - Fullstack/`** — product/frontend/backend/systems engineering, no AI/finance-specific signal.
- **`3 - CyS & Finance/`** — security engineering, or software engineering inside a finance/trading firm.
- **`Other/`** — genuine software engineering that fits none of the three niches above. Same research rigor applies here as anywhere else — this is not a lesser bucket, it exists because "real but not a stated priority" is a legitimate, common case (defense contractors, industrial/embedded software, general enterprise SWE).
`Viewed/` sits alongside these four as a human triage bin (seen, not used) — it is never a pipeline write target.
## Resource Limits — Designed 2026-07-26, Not Yet Implemented In Code
To force real review discipline rather than passive accumulation: **201 total files** in `List/Dossiers/` (excluding `Viewed/`) at maximum — 50 per priority folder, plus the one `Dossiers-to-Create.md` directive note sitting at the root. **Per push, at most ~10 new dossiers** — roughly 3 AI/ML, 3 Fullstack, 3 CyS & Finance, 1 Other; these numbers are a starting point, meant to be tuned against real data, not fixed constants. **Warning stages at 150, 170, 190, and 200** total files, so the system flags itself well before the cap forces a hard decision. **Resource exhaustion** (a source running dry of new eligible postings) gets logged in `10_Areas/Career/Internships/List/Resources` (per-resource usage tracker) with the planned alternative named in `[[20_Progress/Internship/Building System/Research Loop - Resources]]` (the main resource list). **Confirmed still not implemented** as of 2026-07-26 — `run_pipeline.py:66` still reads the original `MAX_NEW_WRITES_PER_RUN = 18`, checked directly against live code, not assumed — see [[System - Build Log]]'s Open section.
## The Promotion Pipeline — Dossier To Submitted Application
Full step-by-step reasoning lives in the new detailed workflow note (`30_Order/Workflows/`, in progress); the short version:
```
  ```
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/Programs/Considering/Software Engineering Intern - Appian.md`
- `Bash` — `cd /home/anant_gupta/projects/work/internship-research-loop
grep -n "MAX_NEW_WRITES_PER_RUN" run_pipeline.py
echo "=== core/identity.py cross_source_key ===" && cat core/identity.py
echo "=== profile.yaml degrees_allow ===" && grep -n "degrees" core/profile.yaml
echo "=== core/relevance.py current stage1 patterns ===" && grep -n "_STAGE1_REJECT_RE" -A 8 core/relevance.py
echo "=== core/classify.py CYS_FINANCE_RE ===" && grep -n "_CYS_FINANCE_RE" -A 5 core/classify.py`
  ```
66:MAX_NEW_WRITES_PER_RUN = 18
282:    this_run, deferred = _prioritize_and_cap(new_listings, MAX_NEW_WRITES_PER_RUN)
=== core/identity.py cross_source_key ===
"""Layer 3 — stable dedup keys for a Listing.

Both remaining sources carry a stable upstream id, so the uid is simply
source:raw_id. (The content-hash fallback existed only for zapplyjobs,
removed as a source 2026-07-18.)

cross_source_key() is the secondary dedup identity: the same program listed
by two different sources gets two different uids but one company+title key.
"""
import re


def compute_uid(listing) -> str:
    if not listing.raw_id:
        raise ValueError(f"listing from {listing.source} has no upstream id: {listing.company!r}")
    return f"{listing.source}:{listing.raw_id}"


def cross_source_key(company: str, title: str) -> str:
    # Punctuation-insensitive: "Intern Co-op" and "Intern/Co-op" are the same
    # posting (real Marmon dup that slipped past a whitespace-only key,
    # caught in the 2026-07-18 dossier audit).
    norm = lambda s: re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return f"{norm(company)}|{norm(title)}"
=== profile.yaml degrees_allow ===
47:# 592, ("PhD",) 586, empty 4676 — fetched 2026-07-18). Permissive: empty degrees
49:degrees_allow: ["Bachelor's"]
=== core/relevance.py current stage1 patterns ===
46:_STAGE1_REJECT_RE = re.compile(
47-    r"\b(financial analyst|risk analyst|performance analyst"
48-    r"|tax (associate|preparer|accountant)"
49-    r"|investor relations"
50-    r"|sports performance (analyst|analytics)|academy performance (analyst|analysis)"
51-    r"|human resources intern|hr intern|marketing intern|business development intern)\b",
52-    re.I,
53-)
54-
--
59:    return bool(_STAGE1_REJECT_RE.search(f"{title} {raw_text}"))
60-
61-
62-# Adjacent-field company/title hint — NOT a reject signal on its own (Jane
63-# Street "Hardware Engineer (FPGA/ASIC) Intern" and Bosch/Magna's automotive
64-# ML roles all pass real content checks below). Only postings that hit this
65-# hint need their fetched content checked at all; everything else already
66-# cleared stage 1 and passes through unconditionally.
[REDACTED] = re.compile(
=== core/classify.py CYS_FINANCE_RE ===
35:_CYS_FINANCE_RE = re.compile(
36-    r"\b(security engineer|cybersecurity|application security|appsec"
37-    r"|penetration test|infosec|threat|vulnerability|quant(itative)? developer"
38-    r"|quantitative (research|trading)|trading systems?|fintech|risk engine"
39-    r"|payments? (engineer|infrastructure)|blockchain|crypto|defi)\b", re.I,
40-)
--
54:    for bucket, pattern in (("AI/ML", _AI_ML_RE), ("CyS & Finance", _CYS_FINANCE_RE), ("Fullstack", _FULLSTACK_RE)):
55-        m = pattern.search(haystack)
56-        if m:
57-            return bucket, m.group(0)
58-    return "Other", ""
59-
  ```
- `Write` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Internship Notes Standard.md`
  ```
---
type: evergreen
status: sprout
created: 2026-07-29
updated: 2026-07-29
tags:
  - internship
  - standard
  - automation
notes:
  - "[[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]]"
  - "[[20_Progress/Internship/Building System/Source of Truth]]"
  - "[[20_Progress/Internship/Building System/System - Build Log]]"
next: "Referenced by 'Prompt 4/5' in [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]] — the dossier-improvement build should conform to this, not re-derive it."
---
# Internship Notes Standard
==Was an empty stub until 2026-07-29 despite being cited by [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]] and every dossier-writing code path — this is the first real content.== Written after a live audit found dossier notes structurally consistent (writer.py's template is applied uniformly) but substantively broken in four ways: unreadable pasted content, zero interlinking (notes float with no MOC/company connection), no distinction between "current" and "removed" dossiers, and a resource-limit spec (see [[20_Progress/Internship/Building System/Source of Truth]]) that exists on paper but not in code. This standard is the contract; the build that makes code match it is tracked in [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]].

## Scope
Applies to every note `gupta-builds/internship-research-loop` writes into `10_Areas/Career/Internships/List/Dossiers/` (including `Viewed/`). Does not govern Program/Contact/Tracker notes — those have their own templates (`30_Order/Templates/Career/`) and are written by `/promote-dossier`, a separate human-consent step.

## 1. Frontmatter — required fields
Every dossier carries exactly the fields `vault_writer/writer.py`'s `build_frontmatter()` produces, in this order: `company, title, url, source, terms, locations, target_year, date_posted, date_found, matched_reason, status, next, tags`. Fail-closed, same as everywhere else in this codebase (`vault_writer/validate.py`'s `REQUIRED_FRONTMATTER_FIELDS`) — a field is present even when `null`/`[]`, never omitted.

**New requirement, 2026-07-29 — `notes:` interlink field.** Every dossier must carry a `notes:` list (the same convention every other evergreen/MOC-style note in this vault already uses — see `Dossiers MOC.md`, `Source of Truth.md`, `System - Build Log.md`) containing:
- **Always:** `"[[10_Areas/Career/Internships/List/Dossiers MOC]]"` — a dossier that doesn't point back to the MOC is exactly the "floating note" problem this rule exists to close.
- **If this dossier is a removal** (moved to `Viewed/` — see §4): also `"[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]"`, appended, never replacing the first link — a removed dossier is still a dossier that was once live, its MOC membership is historical fact, not something removal erases.

**Same-company clustering.** No per-company hub note exists anywhere in this vault (Program notes carry a plain `company:` string, not a link — checked directly against the real `Programs/Considering/Software Engineering Intern - Appian.md` note, 2026-07-29) and creating N-1 backfill edits every time a new same-company dossier lands is exactly the kind of accumulating maintenance cost this codebase's zero-LLM/deterministic ethos avoids elsewhere. **Use a tag, not a link list**: add `company/<slugified-company-name>` to the existing `tags:` array (e.g. `company/appian`, `company/aquatic-capital-management` — same slugification rule as filenames: lowercase, spaces to hyphens, strip `\/:*?"<>|`). Obsidian's tag pane and a `FROM #company/x` Dataview query both cluster same-company dossiers for free, with no write-time lookup of "what else exists for this company" and no risk of a stale link list. If a real need for direct company-to-company wikilinks surfaces later (not hypothetical — an actual workflow that needs it), revisit; don't build the link-list version preemptively.

## 2. Body content — readable, structured, not a raw scrape dump
Currently every dossier pastes `extract_content()`'s output verbatim under `## Posting (fetched <date>)` — real, observed problems as of 2026-07-29: repeated boilerplate (Conagra's "About Us" paragraph appears twice, verbatim, in the same note), UI chrome mixed into body text (`locationsChicago, Illinois` / `time typeFull time` / `job requisition id...` run together with no structure), and zero section structure (a wall of text, not scannable). This is a real defect, not cosmetic — the whole point of Phase 6 pasting real content was to let a 60-second read replace a page visit; unstructured noise defeats that.

**Fix stays zero-LLM** (see [[../../CLAUDE.md|internship-research-loop CLAUDE.md]] in the repo — `ingestion/posting_page.py`'s `extract_content()` is in the unattended path, ships hourly, no exception). The fix is a better deterministic content-structuring pass, not a summarizer:
- **Dedupe repeated paragraphs.** A paragraph (roughly: a blank-line-delimited block) that appears twice verbatim in the same fetch is boilerplate, not content — keep the first occurrence, drop the rest. Cheap, deterministic, no false-positive risk on genuinely short/simple postings (nothing to dedupe if nothing repeats).
- **Split the known ATS-chrome key:value run-ons** (`locations`, `time type`, `posted on`, `job requisition id`, `time left to apply`) onto their own lines before the free-text body starts, instead of leaving them jammed against the first sentence of real content.
- **Section headings, where the source text actually has them** (most real postings already write `Responsibilities` / `Qualifications` / `Requirements` / `Benefits` / `Compensation` as their own line or bolded phrase) — preserve them as real markdown `###` headings instead of flattening everything to plain paragraphs. Do not invent section boundaries the source text doesn't have; a posting with no internal structure stays one block, described as-is, not force-split.
- **Strip known non-content chrome** already partially handled (nav links, "apply now" buttons) — extend to the patterns found live: "Read More" truncation markers, repeated "Follow Us" / social-link lists, and — the real, distinct Google Careers bug (2026-07-26 audit, `[[20_Progress/Internship/Building System/Runs/Claude Code Prompts]]` Task E) — an entire unrelated search-results-listing page preceding the real posting on some ATS platforms. That's an extraction-target bug (wrong page/wrong `waitFor`), not a formatting one; fix at the fetch layer, not by trying to filter listing-page noise out after the fact.

## 3. Company & degree facts — structured, not just prose
Mirrors the "Backfill" rule already proven necessary for Program notes (`.claude/skills/promote-dossier/reference/note-templates.md` in the repo, added after the real Appian run found facts written into prose but never backfilled into frontmatter): if a dossier's own posting content states a concrete class-year, degree-level, or citizenship/OPT signal, that fact must be checked against structured filter behavior, not left to silently pass on missing-data permissiveness. Concretely: a PhD-only posting (real example, Optiver "Quantitative Research Intern, PhD," Greenhouse — no structured degree field, so `degrees_eligible()`'s missing-data permissiveness waved it through) should be caught by a content-level degree check, the same shape as the existing OPT content check (`opt_exclusion()` in `ingestion/posting_page.py`) — permissive by default, reject only on an explicit "PhD required"/"PhD only"/"doctoral candidates only" signal, never on "PhD preferred" or a degree merely being listed among several acceptable ones.

## 4. Removal — move, don't delete; mark, don't erase
`recheck.py` currently deletes a closed-posting dossier outright (`Path(r["path"]).unlink()`). **Changing, 2026-07-29**: a removed dossier moves to `10_Areas/Career/Internships/List/Dossiers/Viewed/` instead of being deleted — the posting closing is real information (a signal about that company's hiring cadence, evidence for why a later duplicate should be rejected, a record of what this pipeline actually saw), and deleting it outright throws that away for no benefit `git log` doesn't already partially provide less usably.
- On move: append `"[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]"` to `notes:` (see §1) — the original Dossiers MOC link and any `company/<slug>` tag stay, unchanged. A removed dossier's history (it was once live, it was in bucket X, it was for company Y) is real and shouldn't disappear because the posting itself closed.
- Add a `removed_date` and `removed_reason` field to the frontmatter at move time (mirrors `recheck.py`'s own existing `reason` string — `"absent from live feed"` or `"active: false upstream"` — already computed, just not currently persisted anywhere once the file is gone).
- `status:` should reflect this too — set to `removed` (currently every dossier's `status` is a static `unreviewed`; this is the first real transition the field will ever see, and it existing unused until now is itself evidence this was always the intended design, not a new field to invent).
- `state/dossier_uids.json` (the uid→path manifest `vault_writer/writer.py` maintains) must be updated to the new post-move path, not left pointing at a file that no longer exists there — a stale manifest entry breaks the next `write_dossier()` idempotency check for that uid.
- `Viewed/` is a **human triage bin**, never a pipeline write target for new dossiers (per [[20_Progress/Internship/Building System/Source of Truth]]) — only `recheck.py`'s removal path writes here, and only by moving an existing file, never creating a new one directly.

## 5. Resource limits — a notification, not a silent hard stop
Per [[20_Progress/Internship/Building System/Source of Truth]] and [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]]: 50 files per priority bucket, 201 total (`List/Dossiers/` excluding `Viewed/`), designed 2026-07-26, still not in code as of this writing. **Clarified 2026-07-29**: hitting a bucket's threshold is a **notification**, surfaced in two places — the vault side (a visible warning on `Dossiers MOC.md` / the Tracker dashboard, so a human opening the vault sees it without reading logs) and the codebase side (a run-log field, and a filed GitHub issue on first crossing — not a hard refusal to write). The point is forcing a human review decision to happen, not silently discarding a real, currently-open posting the same way an exclusion gate would. See [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]] for the exact build spec.

## Done When
- Every dossier's `notes:` field resolves (Dossiers MOC, plus Removed Dossiers MOC for anything in `Viewed/`) — no broken/missing links.
- A same-company second dossier shares its `company/<slug>` tag with the first, verifiable via Obsidian's tag search.
- A spot-read of five random dossiers shows no duplicated paragraphs and no jammed-together UI-chrome lines.
- A bucket crossing 50 shows up on `Dossiers MOC.md` without opening `logs/runs.jsonl`.
- A closed posting's dossier is findable in `Viewed/`, not gone.

  ```
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers MOC.md`
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers MOC.md`
  ```diff
  - # Dossiers — Map of Content
==Everything currently in `List/Dossiers/`, live, by priority folder.== See [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]] for the gate that gets a posting here at all. Nothing here is hand-edited into existence — this note only reads what the loop already wrote.
## 1 — AI & ML
  + # Dossiers — Map of Content
==Everything currently in `List/Dossiers/`, live, by priority folder.== See [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]] for the gate that gets a posting here at all. Nothing here is hand-edited into existence — this note only reads what the loop already wrote.
## ⚠️ Capacity Notification
Live-computed, not code-maintained — this section reads the real folder counts every time this note renders, so a bucket crossing its threshold shows up here without anyone having to push a change. See [[30_Order/Standards/Internship Notes Standard]] §5: crossing 50 is a notification, never a silent write-refusal.
```dataviewjs
const buckets = ["1 - AI & ML", "2 - Fullstack", "3 - CyS & Finance", "Other"];
const root = "10_Areas/Career/Internships/List/Dossiers";
const rows = buckets.map(b => {
  const count = dv.pages(`"${root}/${b}"`).length;
  const flag = count >= 50 ? "🔴 AT/OVER CAP (50)" : count >= 40 ? "🟡 approaching (40+)" : "🟢 ok";
  return [b, count, flag];
});
const total = rows.reduce((sum, r) => sum + r[1], 0);
dv.table(["Bucket", "Count", "Status"], rows);
dv.paragraph(`**Total (excl. Viewed/): ${total} / 201.** Design: [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]].`);
```
## 1 — AI & ML
  ```
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md`
  ```diff
  - ## Prompt 4 — Count-Limit Throttle + Four Real Bugs Found In A Live-Data Audit
```
You are working in gupta-builds/internship-research-loop. Context: Prompts 1-3 already shipped (core/relevance.py, core/classify.py, the priority-folder routing in vault_writer/writer.py, the /promote-dossier skill) — all confirmed live on master. This prompt covers a new count-limit feature plus four real, evidence-based bugs found by manually auditing every dossier the live pipeline actually wrote since Prompts 1-3 shipped — not hypothetical, each one is a real posting that was fetched and misclassified for real. Fixture files for all four are named below; use the real content, don't write synthetic test data.
  + ## Prompt 4 — Revised 2026-07-29, Never Executed
**Written 2026-07-26, still zero code commits against it as of 2026-07-29** — confirmed directly (`git log` shows only "Update state + logs"/"Recheck log" entries since). A follow-up live-dossier audit run 2026-07-29 (94→127→141 dossiers accumulated in that window, entirely through the same unfixed gate) found the *same four bug classes recurring* on new real postings, plus **one new bug class** (a degree-requirement gap, real example: Optiver's PhD-only posting), and the user separately specified four vault-side requirements not in the original scope (interlinking, move-not-delete on removal, readable structured content, and reframing the count-limit as a notification rather than a hard write-refusal). `30_Order/Standards/Internship Notes Standard.md` (empty stub until 2026-07-29) now has real content defining all of this — read it before starting, it's the contract this whole prompt implements. Tasks A-E below are the original bugs, revised with the new recurring evidence; Tasks F-I are new.
```
You are working in gupta-builds/internship-research-loop. Context: Prompts 1-3 already shipped (core/relevance.py, core/classify.py, the priority-folder routing in vault_writer/writer.py, the /promote-dossier skill) — all confirmed live on master. This prompt was originally written 2026-07-26 and never executed (confirmed via git log — zero commits against it). A follow-up live audit on 2026-07-29 found the same bug classes recurring on new real postings plus one new bug class, and the user specified additional vault-side requirements. Read `30_Order/Standards/Internship Notes Standard.md` in the Jarvis vault before starting — it's the real, concrete contract for dossier notes (frontmatter, body structure, interlinking, removal handling, resource limits) that this whole prompt implements; it did not exist (empty file) until this revision. This prompt covers nine tasks — five real, evidence-based bugs (A-E, A also carries a design revision) plus four new requirements (F-I). Fixture files/real examples are named throughout; use the real content, don't write synthetic test data.
  ```
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md`
  ```diff
  - ## Task A — Dossier count-limit throttle (new)
Currently `run_pipeline.py:66` has `MAX_NEW_WRITES_PER_RUN = 18` with no per-bucket split and no ceiling on total accumulated dossiers. Replace with:
1. A hard cap of 201 total files across `10_Areas/Career/Internships/List/Dossiers/` excluding `Viewed/` — 50 per priority bucket (`1 - AI & ML`, `2 - Fullstack`, `3 - CyS & Finance`, `Other`) plus the one `Dossiers-to-Create.md` directive note at the root (50*4+1=201). Before writing, count existing files in the vault checkout per bucket; refuse to write into a bucket already at 50, logging why in the run record rather than silently dropping — a full bucket should surface, not vanish.
2. A per-run write budget, still capped at roughly 10 total but split by bucket: something like 3 AI/ML, 3 Fullstack, 3 CyS & Finance, 1 Other — implement this as a tunable dict, not hardcoded magic numbers spread through the function, since these numbers are explicitly meant to be adjusted over time based on real data.
3. Warning stages: when the total count (again excluding Viewed/) crosses 150, 170, 190, or 200, the run record should carry an explicit `warning` field naming which threshold was crossed. Surface this via a filed GitHub issue only at 190 and 200 (150/170 are informational-only in the run log, not worth an issue) — reuse the existing `file_github_issue` pattern already in run_pipeline.py, don't build a second notification path.
4. Keep the existing most-recently-posted-first prioritization within each bucket's per-run allocation — don't replace that logic, just scope it per-bucket instead of globally.
Tests: fixture-based, covering a bucket at exactly 49/50/51, the total at 200/201, and the per-bucket run-budget split actually respecting bucket boundaries (a bucket with 0 eligible candidates this run shouldn't consume another bucket's slots).
  + ## Task A — Dossier count-limit, as a NOTIFICATION not a hard write-refusal (revised 2026-07-29)
Currently `run_pipeline.py:66` has `MAX_NEW_WRITES_PER_RUN = 18` with no per-bucket split and no ceiling on total accumulated dossiers — still true, checked directly 2026-07-29. **Live counts right now, checked 2026-07-29: `1 - AI & ML` 53, `2 - Fullstack` 21, `3 - CyS & Finance` 54, `Other` 11 — two buckets are already past the original 50 design number, so this is not theoretical anymore.** Original design (`Dossiers-to-Create.md`, `Source of Truth.md`) said "refuse to write into a bucket already at 50" — **the user explicitly overrode that framing**: this is a notification mechanism, not a silent gate that drops a real eligible posting the way an exclusion rule does (that asymmetry — a false exclusion loses an opportunity for nothing, a false inclusion costs one screening read — is this codebase's founding design principle everywhere else; a hard-refusal cap violates it for no reason, since the actual scarce resource is human review attention, not vault storage). Implement:
1. A per-bucket count check before writing (still count real files in the vault checkout per bucket, same mechanism originally planned) — but do **not** refuse the write when a bucket is at/over 50. Keep writing; a full bucket is a signal to review more urgently, not a reason to lose a real posting.
2. A per-run write budget, still capped at roughly 10 total but split by bucket: something like 3 AI/ML, 3 Fullstack, 3 CyS & Finance, 1 Other — implement as a tunable dict, not hardcoded magic numbers spread through the function; this pacing exists to protect Firecrawl budget and review throughput, independent of the notification question above.
3. Run-record field: when a bucket's post-write count is >= 50, the run record carries an explicit `bucket_at_capacity` list naming which bucket(s). File a GitHub issue the **first time** a given bucket crosses 50 (track "already notified" per bucket in `state/` so it doesn't refile every run — reuse the existing `file_github_issue` pattern, don't build a second notification path) and again if the *global* total (excluding `Viewed/`) crosses 190 or 200 (150/170 stay informational-only in the run log). Since `1 - AI & ML` and `3 - CyS & Finance` are already over 50 as of this writing, the very first run after this ships should file both bucket-crossing issues immediately if the "already notified" state starts empty — expected, not a bug.
4. Do **not** touch `10_Areas/Career/Internships/List/Dossiers MOC.md` in the vault — a live `dataviewjs` capacity table was already added there directly 2026-07-29 (reads real folder counts at render time, no code needs to maintain it). Task A only needs the codebase-side run-log/issue half described above.
5. Keep the existing most-recently-posted-first prioritization within each bucket's per-run allocation — don't replace that logic, just scope it per-bucket instead of globally.
Tests: fixture-based, covering a bucket at exactly 49/50/51 (assert the write still happens at 50/51, only the notification fires), the global total at 189/190/200/201, the per-bucket run-budget split respecting bucket boundaries (a bucket with 0 eligible candidates this run shouldn't consume another bucket's slots), and the "notify once per bucket" state actually suppressing a second issue on a subsequent run where the bucket is still >= 50.
  ```
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md`
  ```diff
  - ## Task B — CS-relevance gate: Product Management roles slip through (real bug)
`core/relevance.py`'s `_STAGE1_REJECT_RE` has no pattern for product/program management roles. Real example, live-fetched 2026-07-26: Databricks "Product Management Intern (Summer 2027)" (AIJobs source) — the actual role is explicitly PM work ("you will learn how to be a successful PM," "own your project end-to-end — design, build, launch, and iterate on feedback" from a PM's perspective, not an engineer's) despite listing "computer science" as an acceptable major. It passed both stage 1 and stage 2 and got classified AI/ML purely because "Machine Learning" appears in a list of Databricks' internal team names, not because the role does ML work. Add a pattern to `_STAGE1_REJECT_RE` catching "product management intern," "product manager intern," "program management intern," "technical program manager intern" (word-bounded, same style as the existing patterns) so these reject before ever reaching classification. Verify against the real Databricks fixture (content below) that this doesn't also reject genuine engineering roles that happen to mention "product" (e.g. "product engineer," "product-focused software engineer" should still pass — check this distinction explicitly in a test, don't just add a blunt "product" keyword).
  + ## Task B — CS-relevance gate: Product/rotational/business-analyst roles slip through (real bug, recurring)
`core/relevance.py`'s `_STAGE1_REJECT_RE` has no pattern for product/program management OR business-rotational-program roles — confirmed as a recurring bug class, not a one-off:
- **Databricks** "Product Management Intern (Summer 2027)" (AIJobs source, found 2026-07-26) — the actual role is explicitly PM work ("you will learn how to be a successful PM," "own your project end-to-end — design, build, launch, and iterate on feedback" from a PM's perspective, not an engineer's) despite listing "computer science" as an acceptable major. Passed both stages, classified AI/ML purely because "Machine Learning" appears in a list of Databricks' internal team names, not because the role does ML work.
- **Conagra Brands** "Demand Science Rotational Analyst" (SimplifyJobs, found 2026-07-27, still live in the vault as of this writing at `List/Dossiers/Other/Demand Science Rotational Analyst - Conagra Brands.md`) — a 2-year business rotational program across "Behavioral Science, Demand Forecasting, Data Science, Predictive Science, Demand Planning, Advanced Analytics" with zero programming/software content anywhere in the real posting text; its own stated requirement is "a general understanding of business, financial concepts, and theory behind processes." Passed both stages and landed in `Other` purely because it cleared the CS-relevance gate on no real signal at all (there is no positive software signal in this posting — it should have been rejected by stage 1 or 2, not merely miscategorized).
Add patterns to `_STAGE1_REJECT_RE` catching (word-bounded, same style as existing patterns): "product management intern," "product manager intern," "program management intern," "technical program manager intern," and separately "rotational (analyst|program)," "demand (planning|science) (analyst|rotational)," "business analyst intern" — verify against both real fixtures (Databricks and Conagra dossier files, read them directly from the vault rather than re-fetching) that genuine engineering roles which happen to mention "product" or "rotational" in passing still pass (e.g. "product engineer," "product-focused software engineer," a software-engineering-track rotational program that names actual engineering rotations) — check this distinction explicitly in a test, don't just add blunt keywords.
  ```
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md`
  ```diff
  - ## Task D — Cross-source dedup misses company-name variants (real bug)
Two real, confirmed duplicate pairs slipped past `cross_source_key()`'s dedup check because the two sources spelled the company name differently:
- "Aquatic" (vanshb03, Greenhouse token `aquaticcapitalmanagement`) vs "Aquatic Capital Management" (SimplifyJobs) — same company, same role ("Software Engineer Intern"), same Chicago Greenhouse posting in substance.
- Google's BS-track Summer 2027 SWE intern posting reached the vault twice: once via vanshb03 as `title: "Software Engineering Intern"` (already correctly filed), once via Freehire as `title: "Software Engineering Intern, BS, Summer 2027"` — confirmed the exact same job by comparing the numeric ID embedded in both URLs (`.../jobs/results/85564713261245126`), which was identical, only the URL slug and title string differed.
`cross_source_key()` currently keys on normalized company+title, which breaks when either string varies across sources for the same real posting. Fix: for company-name variants, either (a) maintain a small known-alias map for companies confirmed to appear under multiple names across sources (start with `aquatic` → `aquaticcapitalmanagement`, checked live), or (b) prefer matching on a normalized ATS-derived identity (e.g. extract the Greenhouse/Ashby/Workday job ID or numeric ID embedded in the URL, when present, as a stronger identity signal than title text) before falling back to company+title. Prefer (b) if it's not a large change — it's the more general fix and would have caught the Google case too, which (a) alone would not.
  + ## Task D — Cross-source dedup misses company-name AND title-string variants (real bug, recurring — four confirmed pairs now)
`cross_source_key()` (`core/identity.py`) keys on normalized company+title, which breaks whenever either string varies across sources for the same real posting. Confirmed recurring, not a one-off — four real duplicate incidents now, two from the original 2026-07-26 audit, two more found 2026-07-29:
- **Aquatic** (vanshb03, Greenhouse token `aquaticcapitalmanagement`) vs **Aquatic Capital Management** (SimplifyJobs) — same company, same role ("Software Engineer Intern"), same Chicago Greenhouse posting in substance. Company-name variant.
- **Google** BS-track Summer 2027 SWE intern reached the vault twice: vanshb03 (`title: "Software Engineering Intern"`) and Freehire (`title: "Software Engineering Intern, BS, Summer 2027"`) — confirmed the exact same job via the identical numeric ID embedded in both URLs (`.../jobs/results/85564713261245126`). Title-string variant, same underlying job ID.
- **Virtu Financial** — a genuine *triple* duplicate, confirmed 2026-07-29: three separate dossiers ("2027 Internship - Software Engineer," "Software Engineer Intern - Software Engineer," "Software Engineer Intern") all point to the exact same URL (`greenhouse.io/virtu/jobs/8624410002`), sourced via Greenhouse/zshah101/vanshb03 with a different title string each time. Same Greenhouse job ID present in all three URLs — this is the strongest evidence yet that a URL/job-ID-based identity check would have caught every one of these four incidents, not just some.
- **Palantir** "Intel" role — confirmed 2026-07-29, a duplicate across two different *buckets*: the same Lever job ID, sourced via SimplifyJobs (landed in `1 - AI & ML`) and zshah101 (landed in `2 - Fullstack`) — same posting classified two different ways depending on which source's copy happened to get matched and classified first. This is a distinct failure mode from the other three (the dossiers aren't just duplicated, they disagree with each other about the posting's own classification) — worth a specific regression test, not just a dedup-count assertion.
Fix: prefer matching on a normalized ATS-derived identity — extract the Greenhouse/Ashby/Lever/Workday job ID or numeric ID embedded in the URL, when present, as a stronger identity signal than company+title text, falling back to the existing normalized-company+title key only when no such ID can be extracted (e.g. sources with no discernible job ID in their URL). This is the more general fix and would have caught all four real incidents above (the original company-name-alias-map idea floated 2026-07-26 would only have caught Aquatic). For the Palantir cross-bucket case specifically: once URL/job-ID matching identifies the duplicate, the write gate should keep the first-source-in-`SOURCES`-order copy (existing tie-break rule, already documented in `validate.py`'s `check_cross_source_duplicate` docstring) — don't add a second, different tie-break rule for the cross-bucket case, the existing one already resolves it correctly once dedup actually catches it.
  ```
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md`
  ```diff
  - Fix the extraction; add a regression fixture from the real content captured in this session's audit (both Google dossier files, as they exist right now in the vault, are the real broken-output fixtures — read them directly rather than re-fetching, to guarantee the test reproduces the exact real failure).

## Verification
Run the full test suite, report the exact pass count. Report Tasks A-E individually — for B, C, and D specifically, re-run the real fixture case (Databricks, Mosaic, Aquatic/Google) through the fixed code and confirm the expected outcome (reject, reject, correctly-deduped-or-merged) rather than just asserting the regex looks right.
```
  + Fix the extraction; add a regression fixture from the real content captured in this session's audit (both Google dossier files, as they exist right now in the vault, are the real broken-output fixtures — read them directly rather than re-fetching, to guarantee the test reproduces the exact real failure).

## Task F — Degree-requirement content check (new bug class, 2026-07-29)
Real example: **Optiver** "Quantitative Research Intern, PhD" (Greenhouse) — this is the literal same posting manually deleted from the vault once already (matched by Greenhouse job ID `8451781002`), and it resurfaced. Two distinct problems, fix both:
1. **The gate is structurally blind to degree requirements on 5 of this pipeline's 8 sources.** `core/filter.py`'s `degrees_eligible()` only checks a source's own structured `degrees` field, and is permissive (passes) when that field is empty — correct behavior for genuinely unstated cases, but Greenhouse (and most ATS-direct sources) never carry a structured degree field at all, so a PhD-only posting always passes this check regardless of its real content. Add a content-level check, same shape and same permissive-by-default posture as the existing `opt_exclusion()` check in `ingestion/posting_page.py` (runs on fetched posting content, after the write gate's cheap checks, same point OPT is checked): reject only on an explicit "PhD required," "PhD only," "doctoral candidates only," or equivalent phrasing — never on "PhD preferred," never on a degree merely appearing in a list of several acceptable ones (e.g. "Bachelor's, Master's, or PhD" must still pass). Build the pattern from the real Optiver text; check it against the real Bachelor's/Master's-eligible fixtures already in the test suite to confirm zero new false rejections.
2. **A prior manual deletion taught the system nothing** — there is no feedback path from "a human rejected this" back into the gate, so the same wrong match came right back. **Do not build a feedback-loop mechanism for this now** — `20_Progress/Internship/Building System/Research Loop - Improvement Plan.md`'s Priority 4 already covers this exact gap and is deliberately gated on Priority 1 (a real, human-reviewed Applying-note rejection) happening first; that hasn't happened yet, and building the mechanism ahead of real rejection data to design it against would be exactly the kind of speculative-first building this codebase's own history has repeatedly found wasteful. Task F's actual, sufficient fix is #1 above — a real content-level gate that would have caught Optiver honestly the first time, making the "it came back" complaint moot going forward without needing a memory-of-past-rejections system at all.

## Task G — Dossier interlinking (new, per `30_Order/Standards/Internship Notes Standard.md` §1)
Read the standard doc in the vault first — it's the real, concrete spec (written 2026-07-29, previously an empty stub). Implement in `vault_writer/writer.py`'s `build_frontmatter()`:
1. Add a `notes:` list field (YAML list of wikilink strings) to every dossier's frontmatter, always containing `"[[10_Areas/Career/Internships/List/Dossiers MOC]]"`.
2. Add a `company/<slug>` tag to the existing `tags:` list — same slugification as `dossier_filename()`'s existing sanitization (lowercase, spaces→hyphens, strip `\/:*?"<>|`). This is the same-company clustering mechanism (a tag, not a maintained link list — the standard doc explains why: no per-company hub note exists in this vault, and backfilling N-1 existing dossiers on every new same-company arrival is exactly the kind of accumulating write-time cost this codebase avoids everywhere else).
Tests: a dossier's rendered frontmatter contains both the MOC link and a correctly-slugified company tag; two dossiers for the same company (varying company-string casing/whitespace) produce the identical tag.

## Task H — recheck.py: move to Viewed/, don't delete (new, per Standard §4)
`recheck.py` currently does `Path(r["path"]).unlink()` on a closed posting — replace with a move to `10_Areas/Career/Internships/List/Dossiers/Viewed/` (create the folder if absent). On move:
1. Append `"[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]"` to the dossier's existing `notes:` list (from Task G) — don't replace the MOC/company links already there, a removed dossier's history is still real.
2. Add `removed_date` (today) and `removed_reason` (the existing `reason` string `recheck.py` already computes — `"absent from live feed"` or `"active: false upstream"` — currently discarded once the file's deleted) to frontmatter.
3. Set `status: removed` (every dossier's `status` has been a static `unreviewed` until now — this is the field's first real transition, not a new field being invented).
4. Update `state/dossier_uids.json` (via `vault_writer/writer.py`'s existing `load_dossier_uids`/`save_dossier_uids`) to the new post-move relative path — a stale manifest entry pointing at a file no longer at that path breaks the next `write_dossier()` idempotency check for that uid.
5. `recheck.py`'s existing mass-deletion brake (currently named for delete counts) should apply identically to move counts — same protective logic, don't weaken it just because the operation changed from delete to move.
Tests: a recheck run against a fixture with one closed posting ends with the file present in `Viewed/` (not gone), frontmatter carries all four new/changed fields, and `dossier_uids.json` reflects the new path.

## Task I — Readable, structured dossier body content (new, per Standard §2)
Stay zero-LLM — this is a better deterministic content-structuring pass in `ingestion/posting_page.py`'s `extract_content()`, not a summarizer, per this repo's own hard rule (see the repo's `CLAUDE.md`). Real, observed defects as of 2026-07-29 to fix:
1. **Duplicate-paragraph stripping**: the Conagra fixture (`List/Dossiers/Other/Demand Science Rotational Analyst - Conagra Brands.md`, read it directly) has its entire "About Us" paragraph appearing twice, verbatim. Detect a paragraph (blank-line-delimited block) repeated verbatim later in the same fetch and drop the repeat, keeping the first occurrence.
2. **ATS-chrome line-splitting**: patterns like `locationsChicago, Illinois`, `time typeFull time`, `job requisition idReq-039400` (real, from the same Conagra fixture) are UI labels jammed against their values with no separator — split known label prefixes (`locations`, `time type`, `posted on`, `job requisition id`, `time left to apply`) onto their own line before the free-text body.
3. **Preserve real section structure**: where the source text already states section names (`Responsibilities`, `Qualifications`, `Requirements`, `Benefits`, `Compensation` — bolded or on their own line in the real fetched markdown, check the Appian/Manhattan Associates/Conagra fixtures for the actual shape), render them as `###` headings instead of flattening to one block. Don't invent section boundaries a posting's own text doesn't have.
4. **Strip additional known chrome**: "Read More" truncation markers, repeated "Follow Us"/social-link lists (real example: the Manhattan Associates fixture ends with a duplicated LinkedIn/X/Facebook block).
Tests: fixture-based against the real Conagra and Manhattan Associates dossier content (read directly from the vault, don't re-fetch) — assert no duplicated paragraph survives, assert chrome lines are split, assert a posting with real stated section headers renders them as `###` headings, assert a posting with no internal structure at all stays as one clean block (no invented sections).

## Verification
Run the full test suite, report the exact pass count. Report Tasks A-I individually. For B, C, D, and F specifically, re-run the real fixture cases (Databricks, Conagra, Mosaic, Aquatic/Google/Virtu/Palantir, Optiver) through the fixed code and confirm the expected outcome (reject, reject, reject, correctly-deduped-or-merged, reject) rather than just asserting the regex/logic looks right. For G and H, show the actual rendered frontmatter of a real test dossier before/after. For I, show a real before/after diff of the Conagra fixture's body content. State plainly which tasks were actually run against real data vs. only reviewed for correctness — don't claim a task works if its real fixture case was never actually exercised.
```
  ```
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md`
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md`
  ```diff
  - created: 2026-07-26
updated: 2026-07-26
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
tags:
  - internship
  - automation
  - prompts
next: "Run Prompt 4 against gupta-builds/internship-research-loop, then wipe this file and write the next batch."
---
  + created: 2026-07-26
updated: 2026-07-29
related_progress:
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
tags:
  - internship
  - automation
  - prompts
next: "Run the revised Prompt 4 (Tasks A-I) against gupta-builds/internship-research-loop — needs read access to the real vault (Firecrawl-fetched fixtures live there, not in the repo) to pull the Conagra/Manhattan Associates/Optiver/Virtu/Palantir real content named throughout. Then wipe this file and write the next batch."
---
  ```
- `Read` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/System - Build Log.md`
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/System - Build Log.md`
  ```diff
  - created: 2026-07-16
updated: 2026-07-26
related_progress:
  - "[[Internships Hub]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
tags:
  - internship
  - career
  - system-design
next: "Get Prompt 1-3's code (persona config, CS-relevance gate, priority classification, dossier template v2, contact-research widening, skills/agents) actually committed and pushed — none of it is live yet, see the 2026-07-26 entry."
---
  + created: 2026-07-16
updated: 2026-07-29
related_progress:
  - "[[Internships Hub]]"
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[30_Order/Standards/Internship Notes Standard]]"
tags:
  - internship
  - career
  - system-design
next: "Run the revised Prompt 4 (Tasks A-I) in [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]] against gupta-builds/internship-research-loop — still not executed as of 2026-07-29, see that day's entry below."
---
  ```
- `Edit` — `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/System - Build Log.md`
  ```diff
  - ## Open, Prioritized — Re-Verified Directly Against Live Code (2026-07-26)
1. **`recheck.py`'s `FEEDS` gap — fixed.** Confirmed directly: `FEEDS` now covers 7 entries (SimplifyJobs, JGCL, vanshb03, zshah101, Greenhouse, Ashby, AIJobs). Freehire is the one source still absent from this dict — check whether that's a deliberate exclusion (its data shape may not support the same per-uid closure check) or a real remaining gap.
2. **Dossier count-limit spec — still not implemented.** Confirmed directly: `run_pipeline.py:66` still reads `MAX_NEW_WRITES_PER_RUN = 18`, unchanged from the original backlog-throttle value. No 50-per-folder cap, no 150/170/190/200 warning stages, no 3/3/3/1-style per-push split exist in the live code. This is the next real build item, not yet touched by the 07:xx commits.
3. **Confirm the live code actually works against a real fresh dossier**, not just that it exists on `master` — check the next hourly `run.yml` output directly, or run `loop-verifier`.
4. Resume/cover-letter/interview-prep depth — foundation laid (templates exist), explicitly deferred as future work per this session's own scoping.
  + ## Open, Prioritized — Re-Verified Directly Against Live Code (2026-07-26)
1. **`recheck.py`'s `FEEDS` gap — fixed.** Confirmed directly: `FEEDS` now covers 7 entries (SimplifyJobs, JGCL, vanshb03, zshah101, Greenhouse, Ashby, AIJobs). Freehire is the one source still absent from this dict — check whether that's a deliberate exclusion (its data shape may not support the same per-uid closure check) or a real remaining gap.
2. **Dossier count-limit spec — still not implemented.** Confirmed directly: `run_pipeline.py:66` still reads `MAX_NEW_WRITES_PER_RUN = 18`, unchanged from the original backlog-throttle value. No 50-per-folder cap, no 150/170/190/200 warning stages, no 3/3/3/1-style per-push split exist in the live code. This is the next real build item, not yet touched by the 07:xx commits.
3. **Confirm the live code actually works against a real fresh dossier**, not just that it exists on `master` — check the next hourly `run.yml` output directly, or run `loop-verifier`.
4. Resume/cover-letter/interview-prep depth — foundation laid (templates exist), explicitly deferred as future work per this session's own scoping.
## 2026-07-29 — Prompt 4 Confirmed Still Never Run; Live Audit Finds Four Bugs Recurring Plus One New; Standard Written; Prompt Revised
Classification/routing code (`core/classify.py`, `core/relevance.py`, priority-folder writing) confirmed genuinely live and working since 2026-07-26 — real vault check via direct filesystem read (`/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis`, not MCP, which was disconnected this session), dossiers correctly sorted into `1 - AI & ML` (53), `2 - Fullstack` (21), `3 - CyS & Finance` (54), `Other` (11) — 139 recursive, 1 flat legacy note remaining. **Prompt 4, written 2026-07-26, confirmed still never executed** — zero commits against it (`git log` shows only routine "Update state + logs"/"Recheck log" entries). A fresh live-dossier audit (reported by a separate session, independently spot-checked here against the real vault and repo) found:
- All four of Prompt 4's original bugs (Databricks PM misclassification, Mosaic "threat" false-positive, Aquatic/Google dedup misses, Google careers-page extraction bug) still unfixed, as expected since nothing shipped.
- **The same two bug classes recurring on new postings since 2026-07-26**: Conagra Brands "Demand Science Rotational Analyst" (business rotational program, zero software content, same class as Databricks — `_STAGE1_REJECT_RE` has no rotational/business-analyst pattern); Virtu Financial triple-duplicate and Palantir cross-bucket duplicate (same `cross_source_key()` gap as Aquatic/Google, now with a same Greenhouse/Lever job ID present across all variant URLs — strong evidence a URL/job-ID-based identity check is the right general fix).
- **One new bug class**: Optiver's PhD-only Greenhouse posting resurfaced after a prior manual deletion — `degrees_eligible()` is structurally blind on any source (5 of 8) with no structured degree field; no content-level degree check exists, unlike OPT which already has one at that same layer.
- **User specified four additional requirements**, none in original scope: (1) dossiers must interlink to `List/Dossiers MOC` and cluster by company (chose a `company/<slug>` tag over a maintained link list — no per-company hub note exists anywhere in this vault, and a link list would need backfilling on every new same-company arrival); (2) `recheck.py` should move closed-posting dossiers to `Viewed/` instead of deleting them, keeping their MOC/company links and adding a link to `Viewed/Removed Dossiers MOC`; (3) dossier body content should be genuinely readable (real defects found: Conagra's "About Us" paragraph duplicated verbatim, ATS-chrome jammed against values with no line breaks) — fix stays zero-LLM, a better deterministic structuring pass, not a summarizer; (4) the count-limit (§ above) is a **notification**, not a hard write-refusal — a full bucket should surface via a vault dashboard notification and a codebase-side run-log/issue, never silently drop a real eligible posting, consistent with this codebase's founding permissive-by-default asymmetry.
**Done this session, directly, vault-side (not code — these don't need a Claude Code session against the repo):** [[30_Order/Standards/Internship Notes Standard]] written for the first time (was an empty stub despite being cited everywhere); a live `dataviewjs` capacity table added to [[10_Areas/Career/Internships/List/Dossiers MOC]] (reads real folder counts at render time — the vault-side half of the notification requirement, done, no code needed); [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]]'s Prompt 4 revised in place (kept, not wiped, since it was never executed) — Tasks A/B/D updated with the new recurring evidence, Tasks F (degree check), G (interlinking), H (move-not-delete), I (readable content) added new.
**Not done this session, deliberately**: no repo code touched — this was a research/verification/planning pass per explicit instruction, followed by writing the next prompt. Niche-specific/FAANG-Fortune100/YC-backed targeting (raised in the same audit that surfaced these bugs) is explicitly sequenced *after* Prompt 4 ships and one clean cycle is observed — pointing a wider intake funnel at an unfixed classification/dedup/degree-gate layer would make every bug above worse, not better.
  ```

## Actions Taken
- Files created: /home/anant_gupta/projects/work/internship-research-loop/.claude/agents/contact-researcher.md, /home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/reference/note-templates.md, /home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/SKILL.md, /home/anant_gupta/projects/work/internship-research-loop/.claude/agents/loop-verifier.md, /home/anant_gupta/projects/work/internship-research-loop/.claude/skills/review-loop-change/SKILL.md, /home/anant_gupta/projects/work/internship-research-loop/.claude/settings.json, /home/anant_gupta/projects/work/internship-research-loop/CLAUDE.md, /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/30_Order/Standards/Internship Notes Standard.md
- Files modified: /home/anant_gupta/projects/work/internship-research-loop/.claude/agents/contact-researcher.md, /home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/reference/note-templates.md, /home/anant_gupta/projects/work/internship-research-loop/.claude/skills/promote-dossier/SKILL.md, /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/10_Areas/Career/Internships/List/Dossiers MOC.md, /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/Runs/Claude Code Prompts.md, /mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Building System/System - Build Log.md
- Files deleted: (none)
- Commands run: echo "=== repo root ===" && ls -la && echo "=== core/ ===" && ls -la core/ 2>/dev/null && echo "=== priority.py exists? ===" && test -f core/priority.py && echo YES || echo NO && echo "=== enrich.py ===" && find . -iname "enrich.py" && echo "=== git log ===" && git log --oneline -20, echo "=== search for priority anywhere ===" && grep -rl "priority" --include="*.py" . | grep -v .venv | grep -v __pycache__
echo "=== jarvis-checkout dir ===" && ls -la jarvis-checkout/
echo "=== is jarvis-checkout a git repo / submodule? ===" && cat .gitmodules 2>/dev/null; git -C jarvis-checkout status 2>&1 | head -5
echo "=== search repo for any Jarvis vault path references ===" && grep -rn "Jarvis" --include="*.py" --include="*.yaml" --include="*.md" . | grep -v .venv | grep -v __pycache__ | head -30, echo "=== jarvis-checkout remote ===" && git -C jarvis-checkout remote -v
echo "=== jarvis-checkout full status ===" && git -C jarvis-checkout status
echo "=== jarvis-checkout top-level dirs ===" && ls jarvis-checkout/ 2>/dev/null; find jarvis-checkout -maxdepth 1 2>/dev/null
echo "=== .gitignore mentions jarvis-checkout? ===" && grep -n "jarvis" .gitignore -i, echo "=== run_pipeline.py priority context ===" && grep -n -i "priority" run_pipeline.py
echo "=== enrich.py content ===" && cat enrich.py | head -60
echo "=== search for Programs/Serious Considering Contacts Tracker ===" && grep -rn -i "Programs/Serious\|Programs/Considering\|Contacts/Each\|Tracker/Each\|Each One" . --include="*.py" --include="*.md" --include="*.yaml" 2>/dev/null | grep -v .venv, echo "=== git log ===" && git log --oneline -10 && echo "=== git status ===" && git status && echo "=== core/ ===" && ls -la core/ && echo "=== priority.py? ===" && test -f core/priority.py && echo YES || echo NO, echo "=== jarvis-checkout ===" && ls -la jarvis-checkout/ && find jarvis-checkout -maxdepth 3 2>/dev/null
echo "=== git diff stat ===" && git diff --stat HEAD, echo "=== core/classify.py ===" && cat core/classify.py
echo "=== core/relevance.py ===" && cat core/relevance.py, git diff HEAD -- enrich.py
echo "=====VAULT_WRITER TEMPLATE====="
git diff HEAD -- vault_writer/templates/dossier.md.j2
echo "=====VAULT_WRITER WRITER====="
git diff HEAD -- vault_writer/writer.py, echo "=== does repo already have CLAUDE.md? ===" && find . -iname "CLAUDE.md" -not -path "./.venv/*"
echo "=== .claude dir ===" && ls -la .claude/
echo "=== profile.yaml diff ===" && git diff HEAD -- core/profile.yaml
echo "=== .github workflows ===" && ls .github/workflows/ 2>/dev/null && find .github -type f, cat .claude/settings.local.json
echo "=== run tests ==="
source .venv/bin/activate 2>/dev/null; python -m pytest -q 2>&1 | tail -20, gh repo view gupta-builds/internship-research-loop --json name,defaultBranchRef 2>&1 | head -5
gh api user -q .login 2>&1, ls state/ logs/ && echo "=== seen_ids sample ===" && head -c 300 state/seen_ids.json && echo && echo "=== runs.jsonl tail ===" && tail -3 logs/runs.jsonl 2>/dev/null
echo "=== workflows ===" && cat .github/workflows/run.yml, cat enrich.py
echo "=====VALIDATE====="
cat vault_writer/validate.py, find ~/.claude/skills -maxdepth 2 -iname "SKILL.md" | head -5
echo "---"
cat ~/.claude/skills/graphify/SKILL.md 2>/dev/null | head -40
echo "=== any local project skill examples elsewhere on disk? ==="
find / -maxdepth 6 -path "*/.claude/skills/*/SKILL.md" 2>/dev/null | grep -v "^/home/anant_gupta/.claude/skills" | head -10, find ~/.claude/agents -maxdepth 1 -iname "*.md" 2>/dev/null | head -5
find / -maxdepth 8 -path "*/.claude/agents/*.md" 2>/dev/null | grep -v "^/home/anant_gupta/.claude/agents" | head -10
echo "=== check plugin agents for example frontmatter ==="
find / -path "*agents*" -iname "*.md" 2>/dev/null | grep -iv "node_modules\|/.venv/\|/.git/" | grep -i "code-reviewer\|explore" | head -10, find /home/anant_gupta -maxdepth 10 -path "*/.claude/agents/*.md" 2>/dev/null | head -20, mkdir -p .claude/agents .claude/skills/promote-dossier/reference .claude/skills/review-loop-change, cat .github/workflows/recheck.yml
echo "=====test.yml====="
cat .github/workflows/test.yml
echo "=== state/dossier_uids.json exists? ===" && ls state/, cat ~/.claude/settings.json 2>/dev/null | head -60
echo "=== any other settings.json examples with permissions block ==="
find /home/anant_gupta/projects -maxdepth 4 -path "*/.claude/settings.json" 2>/dev/null | head -5, test -f /home/anant_gupta/projects/work/internship-research-loop/.claude/settings.json && echo EXISTS || echo MISSING, python3 -m json.tool .claude/settings.json > /dev/null && echo "valid JSON", cat README.md, python -m pytest -q 2>&1 | tail -5, source .venv/bin/activate && python -m pytest -q 2>&1 | tail -5, cd /home/anant_gupta/projects/work/internship-research-loop
git fetch origin 2>&1
echo "=== local vs origin/master ==="
git log --oneline -5 origin/master
echo "=== current branch status ==="
git status
echo "=== is local master behind/ahead of origin ==="
git rev-list --left-right --count origin/master...HEAD, cd /home/anant_gupta/projects/work/internship-research-loop
git diff --stat HEAD origin/master
echo "=== do incoming commits touch any file I have modified locally? ==="
comm -12 <(git diff --stat HEAD origin/master --name-only | sort) <(git status --porcelain | awk '{print $2}' | sort), cd /home/anant_gupta/projects/work/internship-research-loop
git diff HEAD --stat -- ingestion/ vault_writer/ tests/test_writer.py tests/test_filter.py
echo "=== ingestion/freehire.py head ==="
head -20 ingestion/freehire.py, cd /home/anant_gupta/projects/work/internship-research-loop
git pull --ff-only origin master
echo "=== post-pull status ==="
git status --short | head -5
git log --oneline -3, cd /home/anant_gupta/projects/work/internship-research-loop
git add core/filter.py core/profile.yaml core/classify.py core/relevance.py \
  enrich.py \
  ingestion/normalize.py ingestion/posting_page.py ingestion/sources.py ingestion/freehire.py \
  recheck.py run_pipeline.py \
  vault_writer/templates/dossier.md.j2 vault_writer/validate.py vault_writer/writer.py \
  tests/fixtures/josegael.json tests/fixtures/simplifyjobs.json tests/fixtures/vanshb03.json tests/fixtures/zshah101.json \
  tests/fixtures/freehire.json tests/fixtures/posting_ashby_ctgt.md \
  tests/test_enrich.py tests/test_filter.py tests/test_posting_page.py tests/test_recheck.py \
  tests/test_run_pipeline.py tests/test_sources.py tests/test_writer.py tests/test_classify.py tests/test_relevance.py tests/test_freehire.py
git status --short, cd /home/anant_gupta/projects/work/internship-research-loop
git commit -m "$(cat <<'EOF'
Priority-bucket classification, CS-relevance gate, widened contact research

Adds core/classify.py (Layer 2.5b, zero-LLM keyword bucketing into AI/ML,
CyS & Finance, Fullstack, Other) and core/relevance.py (Layer 2.5, two-stage
CS/software-relevance gate: cheap title-only reject before fetch, content
-confirmed adjacent-field check after). vault_writer/writer.py and the
dossier template now sort writes into priority-bucket subfolders under
List/Dossiers/, drop the unused uid/category/promoted frontmatter fields in
favor of next (matching the vault's own note convention), and add a
dossier_uids.json manifest for idempotent re-writes and recheck.py's
removal-checking.

Widens enrich.py's contact search to recruiter/university-recruiting queries
and LinkedIn search-snippet hits (site:linkedin.com, snippet text only —
never scrapes or logs into linkedin.com, per its own hard line).

Adds ingestion/freehire.py as an 8th discovery source (scoped to companies
with no reachable Greenhouse/Ashby/Lever token) and wires Greenhouse/Ashby/
AIJobs into recheck.py's removal checks.

258/258 tests passing.
EOF
)"
git log --oneline -3, cd /home/anant_gupta/projects/work/internship-research-loop
source .venv/bin/activate && python -m pytest -q 2>&1 | tail -3
git add .claude/ CLAUDE.md
git status --short, cd /home/anant_gupta/projects/work/internship-research-loop
git commit -m "$(cat <<'EOF'
Add promote-dossier skill, contact-researcher/loop-verifier agents, review-loop-change skill

.claude/skills/promote-dossier/ — turns one List/Dossiers entry into a Program
note + Contacts/Each One note + Tracker/Each One note (Internship Pipeline.md
Step 3), human-consent-gated before any write. Templates copied verbatim from
the vault's own Program Template.md/Contact Template.md; Tracker/Each One has
no pre-existing vault template so its shape is authored from the pipeline
doc's own field description. Requires the Jarvis vault present in the same
working environment (git checkout sibling to this repo, or the jarvis MCP
tools) — documented explicitly rather than assumed, per this being the first
interactive (human-in-the-loop) writer this pipeline has ever had, distinct
from run_pipeline.py/recheck.py's non-interactive scoped-PAT writes.

.claude/agents/contact-researcher.md — exploratory subagent invoked by
promote-dossier's Step 3, using enrich.py's widened search primitives
(recruiter/university-recruiting search, GitHub org members, engineering
blog bylines, LinkedIn search-snippets). Never fabricates a contact; reports
"nothing found" honestly.

.claude/agents/loop-verifier.md — standalone pipeline health check (tests,
scheduled-run history via gh api, vault-vs-run-log dossier counts,
seen_ids/vault divergence, auto-filed issues), the automated version of this
project's prior manual audits (2026-07-19, 2026-07-25).

.claude/skills/review-loop-change/ — checks a diff against this repo's four
established conventions (zero-LLM unattended path, permissive-by-default
filtering, fail-closed write-gate ordering, cited-real-data rule comments)
before it ships. Built as a skill rather than an agent — reasoning is in the
skill file's own "why a skill" section.

.claude/settings.json — pytest/safe-git-reads/gh-reads allowed without
prompting; git push and gh secret modification explicitly require
confirmation every time (permissions.ask), never silently allowed or denied.

CLAUDE.md — documents the three note-template contracts (required fields,
always present even as null) and the explicit agent-vs-script judgment call
for each of contact research / promotion / verification / review.

Verified live against a real dossier (Appian — Software Engineering Intern):
promote-dossier run end-to-end including the write step, contact-researcher
found real sourced contacts, and a real gap this surfaced (structured
frontmatter fields left null while the same fact was already narrated in
body prose — eligible_classes, Tracker's date_created) is fixed in this
commit, not left for later.

258/258 tests passing (no pipeline code touched by this commit).
EOF
)"
git log --oneline -5, cd /home/anant_gupta/projects/work/internship-research-loop
git push origin master
git log --oneline -5 origin/master 2>&1 || git fetch origin && git log --oneline -5 origin/master, cat /home/anant_gupta/projects/work/internship-research-loop/grade_resume.py | head -25
echo "=== jarvis-checkout populated now? ==="
ls -la /home/anant_gupta/projects/work/internship-research-loop/jarvis-checkout/ 2>/dev/null
echo "=== check /mnt/d for a Jarvis vault ==="
ls /mnt/d/Users/_Anant/ 2>/dev/null
find /mnt/d -maxdepth 3 -iname "*jarvis*" 2>/dev/null
echo "=== check /mnt for other drives ==="
ls /mnt/ 2>/dev/null, echo "=== does the literal DEFAULT_RESUME path exist? ==="
ls -la "/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Internship/Resumes/" 2>&1
echo "=== what's actually in /mnt/d/Users/_Anant/10_Areas/ ==="
ls "/mnt/d/Users/_Anant/10_Areas/" 2>&1
echo "=== search for a folder literally named Jarvis anywhere under /mnt/d ==="
find /mnt/d -maxdepth 5 -iname "Jarvis" -type d 2>/dev/null
echo "=== does /mnt/d/Users/_Anant/10_Areas/Career/Internships exist (the vault path used throughout this repo)? ==="
ls "/mnt/d/Users/_Anant/10_Areas/Career/Internships/" 2>&1 | head -20, JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== vault root ===" && ls "$JARVIS"
echo "=== 30_Order/Standards ===" && find "$JARVIS/30_Order" -iname "*standard*" 2>/dev/null
echo "=== 20_Progress/Internship/Building System ===" && ls "$JARVIS/20_Progress/Internship/Building System/" 2>/dev/null
echo "=== Runs dir ===" && find "$JARVIS" -maxdepth 4 -iname "Runs" -type d 2>/dev/null
find "$JARVIS" -iname "*Claude Code Prompts*" 2>/dev/null
echo "=== Dossiers dir ===" && ls "$JARVIS/10_Areas/Career/Internships/List/Dossiers/" | head -30
echo "=== count dossiers ===" && ls "$JARVIS/10_Areas/Career/Internships/List/Dossiers/" | grep -c "\.md$"
echo "=== is there a Viewed subfolder already? ===" && ls "$JARVIS/10_Areas/Career/Internships/List/Dossiers/Viewed/" 2>&1
echo "=== is there a Dossiers MOC already? ===" && find "$JARVIS/10_Areas/Career/Internships" -iname "*MOC*" 2>/dev/null, JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== recursive dossier count per bucket ==="
for d in "1 - AI & ML" "2 - Fullstack" "3 - CyS & Finance" "Other"; do
  echo "$d: $(find "$JARVIS/10_Areas/Career/Internships/List/Dossiers/$d" -maxdepth 1 -iname "*.md" 2>/dev/null | wc -l)"
done
echo "Viewed: $(find "$JARVIS/10_Areas/Career/Internships/List/Dossiers/Viewed" -maxdepth 1 -iname "*.md" 2>/dev/null | wc -l)"
echo "flat root: $(find "$JARVIS/10_Areas/Career/Internships/List/Dossiers" -maxdepth 1 -iname "*.md" 2>/dev/null | wc -l)"
echo "TOTAL recursive: $(find "$JARVIS/10_Areas/Career/Internships/List/Dossiers" -iname "*.md" 2>/dev/null | wc -l)", JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== sample dossiers from each bucket (filenames) ==="
find "$JARVIS/10_Areas/Career/Internships/List/Dossiers/1 - AI & ML" -iname "*.md" | head -5
echo "---"
find "$JARVIS/10_Areas/Career/Internships/List/Dossiers/Other" -iname "*.md" | head -5
echo "=== the one flat-root dossier still there ==="
find "$JARVIS/10_Areas/Career/Internships/List/Dossiers" -maxdepth 1 -iname "*.md", JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== Internship Notes Standard.md ===" && wc -c "$JARVIS/30_Order/Standards/Internship Notes Standard.md" && ls -la "$JARVIS/30_Order/Standards/Internship Notes Standard.md"
echo "=== Removed Dossiers MOC.md ===" && wc -c "$JARVIS/10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC.md"
echo "=== Dossiers-to-Create.md ===" && wc -l "$JARVIS/10_Areas/Career/Internships/List/Dossiers-to-Create.md"
cat "$JARVIS/10_Areas/Career/Internships/List/Dossiers-to-Create.md", JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
cat "$JARVIS/10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create.md", JARVIS="/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis"
echo "=== Programs MOC frontmatter ===" && head -20 "$JARVIS/10_Areas/Career/Internships/Programs/Programs MOC.md"
echo "=== Contacts MOC frontmatter ===" && head -20 "$JARVIS/10_Areas/Career/Internships/Contacts/Contacts MOC.md"
echo "=== a real Program note frontmatter (Appian, since it was actually promoted) ===" && find "$JARVIS/10_Areas/Career/Internships/Programs" -iname "*ppian*"
echo "=== Source of Truth (head) ===" && head -40 "$JARVIS/20_Progress/Internship/Building System/Source of Truth.md", cd /home/anant_gupta/projects/work/internship-research-loop
grep -n "MAX_NEW_WRITES_PER_RUN" run_pipeline.py
echo "=== core/identity.py cross_source_key ===" && cat core/identity.py
echo "=== profile.yaml degrees_allow ===" && grep -n "degrees" core/profile.yaml
echo "=== core/relevance.py current stage1 patterns ===" && grep -n "_STAGE1_REJECT_RE" -A 8 core/relevance.py
echo "=== core/classify.py CYS_FINANCE_RE ===" && grep -n "_CYS_FINANCE_RE" -A 5 core/classify.py
- Tool call tally: Agent (2), AskUserQuestion (2), Bash (43), Edit (16), mcp__jarvis__vault_list (11), mcp__jarvis__vault_read (10), mcp__jarvis__vault_write (5), mcp__jarvis-fs__list_allowed_directories (1), Read (22), Skill (1), TaskCreate (6), TaskUpdate (12), ToolSearch (4), Write (8)

