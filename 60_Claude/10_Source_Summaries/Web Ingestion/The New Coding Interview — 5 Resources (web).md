---
type: input
status: sprout
created: 2026-06-21
updated: 2026-06-21
tags:
  - summary
notes:
  - "[[40_Resources/CS/Repos]]"
input_kind: web
track: career
source_note: "[[the new coding interview, 5 resources id actually study.md]]"
source_url: https://burly-handstand-0dc.notion.site/the-new-coding-interview-5-resources-id-actually-study-380e3f86338481b89157f4fc2dd5fc17
---
# The New Coding Interview — 5 Resources — Summary

**Source:** `https://burly-handstand-0dc.notion.site/the-new-coding-interview-5-resources-id-actually-study-380e3f86338481b89157f4fc2dd5fc17`
**Ingested:** 2026-06-21
**Pages:** N/A — single Notion page, last updated by the author June 15, 2026

## Source

A **Princeton CS** student's ranked list of 5 resources for interview prep, framed around the claim that the skill being tested at interviews has shifted away from raw LeetCode toward production judgment.

## Key Claims

- **The test moved to the actual job:** LeetCode "isn't dead" but no longer gets you hired alone — interviews now probe debugging, reviewing PRs, writing tests, and catching AI when it's confidently wrong.
- **Judgment is the throughline across all 5 resources:** each one trains the same underlying skill — knowing what to do when the test is broken, the PR is sketchy, or the model is wrong — not 5 unrelated skills.
- **Reps beat reading:** the author explicitly warns against just reading the linked resources; several entries specify a timed drill instead (e.g., 30 minutes on a broken server, no AI allowed).
- **AI-assisted interviews are becoming a real format**, and prompts typed during the interview may be visible to the interviewer — the grading target is judgment, not raw model output.

## Full Content

### 1. SadServers
==Broken Linux boxes, a timer, fix it or fail — "the closest thing to the actual job there is, and almost nobody trains this muscle."== Drill: pick one scenario, 30 minutes, no AI — the panic of a broken prod box is exactly what's being screened for.

### 2. the Testing Trophy by Kent C. Dodds
If you can write strong tests, you actually understand the code — and tests are also how you catch AI when it's confidently wrong. The linked post breaks down what to test and what to skip, so tests stop being written that "prove nothing."

### 3. the Google code review guide
How real engineers actually review a PR. Drill: find a merged PR in a large repo, review the diff blind, then read what the maintainers actually caught — the gap between your list and theirs *is* the study plan.

### 4. MIT Missing Semester — debugging and profiling
Narrowing scope and tracing a bug to its root cause, fast. Named explicitly as "the stuff the CS degree skips and the job assumes you already know."

### 5. HackerRank — AI-assisted interviews
==More companies now let candidates use AI during the interview, then grade judgment instead of raw output — prompts can be visible to the interviewer, so the format itself needs studying, not just the content.==

## Why It Matters

This is a different prep axis than what's already tracked in [[40_Resources/CS/Repos]]'s Jobs section (`tech-interview-handbook`, `coding-interview-university`, `leetcode-companywise-interview-questions`) — those are all algorithmic/LeetCode-style prep. Nothing currently in the vault covers the "judgment under a broken system" axis this source argues is the actual bar now (debugging a live box, reviewing a real diff blind, reasoning about AI-generated output). Directly relevant heading into internship interview season.

## Links Into The Vault

- [[40_Resources/CS/Repos]] — confirmed; Jobs section holds the adjacent algorithmic-prep repos this source explicitly contrasts itself against.
- [[the new coding interview, 5 resources id actually study.md]] — the raw clip this note replaces.
- *(to create)* — no existing vault note tracks SadServers, the Testing Trophy, the Google review guide, or MIT Missing Semester; there is currently no career-resources hub to file them under (matches the known gap: `10_Areas` has no concrete Career hub note yet).

## Open Questions

- [ ] Should SadServers / Testing Trophy / Google review guide / MIT Missing Semester get their own entries somewhere in `40_Resources`, or wait for the `10_Areas/Career` hub note that doesn't exist yet?
- [ ] Worth actually running the SadServers 30-minute drill once, unassisted, as a calibration check before relying on this source's claim that it's the highest-value resource of the 5?

## Flashcards

#cards/career
Per this source, what has the **target of technical interviews shifted toward**, beyond raw LeetCode?::Production judgment — debugging a live system, reviewing PRs, writing meaningful tests, and catching AI when it's confidently wrong.
What is the **drill** prescribed for the Google code-review resource, specifically?::Find a merged PR in a large repo, review the diff blind (before reading any comments), then compare your findings against what the maintainers actually caught — the gap is the study plan.
Why does the source warn against AI assistance specifically during the **SadServers** drill, but frame AI use as expected during **HackerRank**'s new format?::SadServers trains the raw diagnostic instinct for a broken system (the skill itself); HackerRank's AI-assisted format tests judgment *while using* AI, since prompts may be visible to the interviewer — they test two different things, not the same skill twice.
