---
type: evergreen
status: sprout
created: 2026-08-28
updated: 2026-08-28
tags:
  - internship
  - humanizer
  - system
notes:
  - "[[20_Progress/Internship/Building System/Resume Alteration]]"
  - "[[20_Progress/Internship/Building System/Cover Letter Alteration]]"
  - "[[30_Order/Standards/Humanized Writing Standard]]"
next: Design the real global humanizer agent/skill/command system (also used for
  networking) as separate work — this note only commits to the minimal interface
  resume/cover-letter drafting needs from it now.
---
# Humanizer
==Interface-only note.== A global humanizer system — an agent, skills, and commands that keep AI-assisted writing sounding like one consistent professional human across resumes, cover letters, and networking messages — is planned separately and is a larger build than this session's scope. This note commits only to the minimal contract [[20_Progress/Internship/Building System/Resume Alteration]] and [[20_Progress/Internship/Building System/Cover Letter Alteration]] need from it *now*, so those two systems aren't blocked waiting on the full global build. When the global system exists, it should implement or extend this contract, not conflict with it.

## The Contract
**Input:** a drafted resume content plan or cover-letter draft, plus context (the target JD, the role, which evidence source each claim traces to).
**Output:** a pass/fail verdict, plus, on fail, specific line-level flags — the exact phrase, which pattern it violates (see [[30_Order/Standards/Humanized Writing Standard]] for the checklist), and a suggested fix. **The Humanizer never silently rewrites** — it flags, the drafting agent or the human applies the fix, and the revised draft goes through the gate again. This mirrors `contact-researcher`'s own rule in the internship-research-loop repo ("never present a guess as a finding") applied to tone instead of factual accuracy: a system that quietly rewrites your words for you is a different, larger trust problem than one that tells you exactly what reads wrong and lets you decide.

## Where This Gate Sits
Every resume content plan and every cover-letter draft passes through this gate **after** human approval of the content plan and **before** any DOCX is written or overwritten — see the `humanize` step in [[30_Order/Workflows/Application Document Preparation]]. A plan can be factually correct (every claim evidence-backed, per the Resume/Cover Letter Alteration evidence rule) and still fail here for *sounding* wrong — generic, inflated, or obviously AI-written. Evidence correctness and tone correctness are checked separately on purpose: conflating them risks either loosening the evidence rule to fix a tone problem, or loosening tone standards to preserve a fact that was phrased badly.

## What's In Scope Here vs. Not
**In scope for this note and [[30_Order/Standards/Humanized Writing Standard]]:** the specific checklist resume/cover-letter drafts get checked against, and the pass/fail/flag contract above.
**Explicitly out of scope, deferred to the global build:**
- The actual agent/skill/command implementation ("I have this planned out already just need to implement it correctly globally" — stated directly in the discovery session for this note).
- Networking-message humanization — the same touch applies there, but that's the global system's job once it exists, not something this internship-specific note re-implements.
- Any research/voice-matching component (using examples of the user's own writing to match personal voice) — a global-system feature, not required for the minimal pass/fail contract above to function.

## Interfaces
- [[30_Order/Standards/Humanized Writing Standard]] — the actual checklist (prohibited patterns, required checks) this gate runs.
- [[20_Progress/Internship/Building System/Resume Alteration]] / [[20_Progress/Internship/Building System/Cover Letter Alteration]] — the two systems that call this gate before writing a file.
- [[30_Order/Workflows/Application Document Preparation]] — where in the sequence this gate runs.
