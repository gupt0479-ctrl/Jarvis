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
The manual reorganization (2026-07-26) sorted the 117 dossiers that had accumulated flat into the four priority subfolders by hand, applying the same rules the codebase is supposed to enforce going forward — **that was a one-time catch-up, not a standing fix**. The classification/routing code (`core/relevance.py`, `core/classify.py`, folder-routing in `vault_writer/writer.py`) is built and tested but not committed to the repo as of 2026-07-26 — see [[System - Build Log]]. Until it's pushed, every new dossier the hourly automation writes still lands flat at this folder's root with the old frontmatter shape, undoing the sort a little more each hour. [[Dossiers MOC]] surfaces both states (sorted and flat) so nothing gets lost in the gap.
