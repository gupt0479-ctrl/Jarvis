---
type: evergreen
status: active
created: 2026-07-26
tags:
  - internship
  - process
  - automation
notes:
  - "[[20_Progress/Internship/Building System/Research Loop - Source of Truth]]"
  - "[[20_Progress/Internship/Building System/Research Loop - Improvement Plan]]"
  - "[[10_Areas/Career/Internships/List/Dossiers/Dossiers MOC]]"
next: "See [[20_Progress/Internship/Building System/Claude Code Prompts]] for the priority-classification build that sorts these into subfolders."
---
# Dossiers — How Notes Get Created Here
==Nothing in this folder is hand-created, ever.== Every file here is written by `gupta-builds/internship-research-loop` (GitHub Actions, hourly, six live sources as of 2026-07-25). This note exists so the gate is legible without reading the codebase — what has to be true about a posting before it lands here, and how it gets sorted once it does.
## The Gate, In Order
1. **Eligibility** — US location (permissive: no data or ambiguous strings pass, only an affirmative foreign signal rejects), OPT-compatible (excluded only on an explicit citizenship/clearance/no-OPT signal, never a guessed allowlist), Bachelor's-eligible (permissive on missing data), and timing (Summer 2027 and Winter 2027 weighted equally high, Spring 2027 wanted but lower-weight — see [[20_Progress/Internship/Building System/Research Loop - Source of Truth]] for the full three-criteria history).
2. **CS/software relevance** — a new hard rule: the posting has to be genuinely software engineering at its core. Adjacent fields (hardware, robotics, astrophysics, space, firmware) aren't auto-excluded, but they only pass if the specific posting's content shows real software/CS relevance a real fit — not just adjacency. Anything that isn't software engineering at all (analyst, risk, tax, sports-performance-analytics roles) is rejected outright, before it reaches step 3 — it does not land in `Other` either.
3. **Priority classification** — every survivor gets sorted into exactly one subfolder: `1 - AI & ML/`, `2 - Fullstack/`, `3 - CyS & Finance/`, or `Other/` (real software engineering that just isn't one of the three named niches — same research rigor applies to `Other`, it is not a lesser bucket). Each dossier carries a short callout at the top stating which real signal from the posting drove the classification — never a numeric "Priority N" label; the folder location already encodes the category.
## What Does Not Belong Here
A lead you found yourself — career fair, LinkedIn, a referral — never becomes a dossier. It goes straight into `Programs/Considering/` (or `Serious/`) per [[30_Order/Workflows/Internship Pipeline]] Step 1, skipping this folder entirely.
## Status During Migration
The priority-subfolder sort (step 3) is a pending codebase change — see [[20_Progress/Internship/Building System/Claude Code Prompts]] Prompt 2, Task A-C. Until that runs, dossiers still sit flat at this folder's root rather than inside the four subfolders; [[10_Areas/Career/Internships/List/Dossiers/Dossiers MOC]] surfaces both states so nothing gets lost in the gap.
