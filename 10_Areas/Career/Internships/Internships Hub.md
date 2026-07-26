---
type: evergreen
status: active
created: 2026-07-16
updated: 2026-07-26
tags:
  - evergreen
  - career
  - internship
notes:
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[10_Areas/Career/Internships/README]]"
  - "[[System - Build Log]]"
  - "[[Source of Truth]]"
next: "Confirm the live code fires correctly on a real hourly run, then build the dossier count-limit throttle — see System - Build Log."
---
# Internships Hub
==The status page for the whole loop — is it actually working, what's broken, what's lacking, what's the habit score, is the rulebook actually being followed.== [[30_Order/Workflows/Internship Pipeline]] is the operating procedure; [[System - Build Log]] is the full history; this note is the current-state dashboard for the questions that matter most right now.
## Is It Working?
**Discovery: yes, verified repeatedly by fresh sessions with no stake in the claims.** Six sources, four hard gates, priority classification — independently re-checked, not just self-reported. **Promotion onward: proven once, manually.** The Appian promotion (2026-07-26) is the first time this pipeline has ever gone from dossier to real Program + Contact + Tracker notes — six days after that gap was first named. One real promotion is evidence the design works, not evidence the loop runs itself yet.
## What's Broken Right Now
> [!NOTE]
> **Corrected 2026-07-26.** The 2026-07-26 build (CS-relevance gate, priority classification, dossier template v2, contact-research widening, promote-dossier skill) was uncommitted at first check — reply prompts went out, and it's now confirmed live via direct `gh api` verification: `classify.py`/`relevance.py` exist on `master`, `.claude/agents`/`.claude/skills`/`.claude/settings.json` are live, `recheck.py`'s `FEEDS` dict now covers 7 of 8 sources (Freehire is the one absence — confirm whether that's deliberate). Not yet confirmed: whether the hourly automation has actually produced a fresh, correctly-classified dossier since the push — check the next `run.yml` log directly rather than assuming from the commit history.
- The dossier count-limit spec (201 cap, per-push throttle, warning stages) is designed, documented, **confirmed still not implemented** — `run_pipeline.py:66` unchanged.
- `Habit Tracker.md` doesn't exist yet in usable form — no score to report here until it's built.
## What's Lacking
Resume/cover-letter/interview-prep depth beyond the existing templates — deliberately deferred, foundation laid, not yet built out. Contact discovery stays real-but-shallow by design (public sources only, no LinkedIn scraping) — a genuine ceiling, not a bug to fix later.
## Rules & Regulations — Actually Being Followed?
The four hard gates (timing, US location, OPT, CS/software relevance) and the permissive-by-default design principle are consistently applied everywhere they've been checked — independent audits on 2026-07-19 and 2026-07-25 both confirmed this directly against live code, not claims. The manual dossier reorg (2026-07-26) applied the same rules by hand where the code doesn't exist yet — 25 of 117 processed dossiers were discarded on the CS-relevance gate or as exact duplicates, which is the rule actually biting, not just being stated.
## Habit Tracker Score
[[Habit Tracker]] is built now — a 16-week tick grid plus an auto-computed real-application count. No ticks yet; check back once a week or two of real use has happened.
## The One Real Blocker
The code is pushed now — the real blocker is verifying it actually behaves correctly against a real, unattended hourly run (not just that it compiles and passed tests), and then building the count-limit throttle before the vault's dossier folders silently grow past what a human can actually review.
