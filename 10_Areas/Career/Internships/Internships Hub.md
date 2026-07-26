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
next: "Get the 2026-07-26 code committed and pushed — see System - Build Log."
---
# Internships Hub
==The status page for the whole loop — is it actually working, what's broken, what's lacking, what's the habit score, is the rulebook actually being followed.== [[30_Order/Workflows/Internship Pipeline]] is the operating procedure; [[System - Build Log]] is the full history; this note is the current-state dashboard for the questions that matter most right now.
## Is It Working?
**Discovery: yes, verified repeatedly by fresh sessions with no stake in the claims.** Six sources, four hard gates, priority classification — independently re-checked, not just self-reported. **Promotion onward: proven once, manually.** The Appian promotion (2026-07-26) is the first time this pipeline has ever gone from dossier to real Program + Contact + Tracker notes — six days after that gap was first named. One real promotion is evidence the design works, not evidence the loop runs itself yet.
## What's Broken Right Now
> [!IMPORTANT]
> **Nothing from the 2026-07-26 build session is live.** `core/classify.py`, `core/relevance.py`, the priority-folder routing, the dossier template v2, the widened contact research — all built, tested, sitting uncommitted. The hourly automation is still running the pre-this-session code. New dossiers landing this hour are still flat, old-format, unclassified.
- `recheck.py`'s `FEEDS` dict only covers 2 of 6 live sources — dossiers from the other four aren't being closure-checked daily right now.
- The dossier count-limit spec (201 cap, per-push throttle, warning stages) is designed, documented, **not implemented in code**.
- `Habit Tracker.md` doesn't exist yet in usable form — no score to report here until it's built.
## What's Lacking
Resume/cover-letter/interview-prep depth beyond the existing templates — deliberately deferred, foundation laid, not yet built out. Contact discovery stays real-but-shallow by design (public sources only, no LinkedIn scraping) — a genuine ceiling, not a bug to fix later.
## Rules & Regulations — Actually Being Followed?
The four hard gates (timing, US location, OPT, CS/software relevance) and the permissive-by-default design principle are consistently applied everywhere they've been checked — independent audits on 2026-07-19 and 2026-07-25 both confirmed this directly against live code, not claims. The manual dossier reorg (2026-07-26) applied the same rules by hand where the code doesn't exist yet — 25 of 117 processed dossiers were discarded on the CS-relevance gate or as exact duplicates, which is the rule actually biting, not just being stated.
## Habit Tracker Score
Not yet trackable — see [[Habit Tracker]], still a design stub as of 2026-07-26.
## The One Real Blocker
Get the uncommitted code pushed. Everything else — the count limits, the recheck fix, further source additions — is downstream of that one action and shouldn't be worked on ahead of it.
