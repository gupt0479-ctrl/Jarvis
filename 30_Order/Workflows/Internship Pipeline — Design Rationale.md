---
type: evergreen
status: sprout
created: 2026-07-26
tags:
  - system
  - workflow
  - internship
  - career
notes:
  - "[[30_Order/Workflows/Internship Pipeline]]"
  - "[[20_Progress/Internship/Building System/System - Build Log]]"
  - "[[Source of Truth]]"
next:
---
# Internship Pipeline — Design Rationale
==Why each piece of [[30_Order/Workflows/Internship Pipeline]] is shaped the way it is, and exactly what has to be true for a real internship to move from one stage to the next.== The Pipeline note is the lean operating procedure — what to do. This note is *why*, and *under what condition each transition actually fires*. Read this when a step feels arbitrary or when deciding whether to bend a rule.
## Why A Dossier Looks The Way It Does
A dossier exists to make a 60-second decision possible without visiting the actual posting. That's the entire design constraint behind every choice in it:
- **It's auto-generated, never hand-typed** — because the whole value of discovery is speed (within an hour of a posting going live) and volume (eight sources, hourly). A human writing dossiers by hand could never match either, so the loop does it, and a human only ever reads and judges.
- **Four hard gates before it exists at all** (timing, US location, OPT, CS/software relevance) — each one answers a yes/no question that would otherwise cost a real webpage visit to resolve. They're permissive by default on purpose: a false exclusion silently deletes a real opportunity with nothing to show for it, while a false inclusion just costs one extra human read. That asymmetry is why every one of these rules errs toward keeping when a signal is ambiguous, not toward a stricter, cleaner-looking filter.
- **Priority-folder classification, not a frontmatter number** — because the folder itself is the fact you actually use day to day (which pile am I looking at right now), and a number in the text would be redundant the moment the file is already sitting in the right place. The classification is deterministic and keyword-based, not an LLM call, because this step runs unattended, hourly, forever — spending a model call on every candidate scales badly and isn't needed for a decision this mechanical.
- **`Other` is a real bucket, not a dumping ground** — because "real software engineering that isn't one of my three named interests" is a genuinely common, legitimate case (a defense contractor, an industrial-embedded role), and treating it as lesser would just mean good candidates get ignored by habit rather than by judgment.
## Why Program Notes Are Written The Way They Are
- **Split from Applying (Areas vs. Progress)** — because a Program note that also carries live status gets rewritten every time you hear back, which defeats the entire point of it being durable reference. The research (comp, eligibility, deadlines, traps) doesn't change once it's true; the funnel stage changes constantly. Mixing them meant the "stable" file was never actually stable.
- **Serious and Considering are the same template, same depth** — because the difference between them is timing/preference, not how much a role deserves to be understood. Writing Considering thinner would mean the note is worse exactly when you go back to actually decide, weeks later, whether it's worth pursuing — the opposite of when you'd want it to be good.
- **Company Information section, written to sound informed, not just accurate** — because the actual test of this note isn't "did I record the facts," it's "could I have a real, specific conversation with this company using only what's written here." A generic paragraph about a company passes an accuracy test and fails the actual point.
## Why Contacts Are Company-Level, With Three Folders
One contact note per internship, not per person, because the unit of work is "who do I know or can find for this specific role" — a single internship might surface three real names, and tracking them as three separate files would scatter the one thing you actually need together: who to reach out to, in what order, for this specific goal.
- **`Ongoing/`** — something is actively moving. Default location.
- **`Come Back/`** — nothing is moving *right now*, but there's a specific, named reason to revisit (a portal that opens later, a "let's talk after you've applied" from the recruiter). This folder exists because "nothing to do" and "something to do, just not yet" are different states, and collapsing them into one loses the reason to ever come back.
- **`Ended/`** — the thread is actually closed, either with a real answer or after a reasonable follow-up window passed with silence. Not a failure marker.
## Why Tracker Exists Separately From Applying
Two different questions, both real, both needed: **"where does this stand, at a glance, across dates"** (Tracker — the timeline) versus **"what's actually going on right now, what do I do next, what would I say in a meeting"** (Applying — the narrative). A single note trying to answer both ends up bad at one of them — either a wall of dates with no story, or a story with no fast-scan structure. Tracker is created first, at commit time, because a timeline should start the moment you commit to something, not once you're already deep into it.
## Why Job & Company Is Its Own, Later Step
Program-note research answers "should I pursue this." Job & Company research answers "how do I sound genuinely informed in an actual conversation about this specific role." Those are different depths of work, and doing the second one for every Considering-folder program would waste real hours on roles that never go anywhere — so it's deliberately gated on "actually ready to apply," not created automatically alongside the Program note.
## The Conditions For Each Real Transition
| From → To | Condition that actually fires it |
| --- | --- |
| Dossier → Screened | You've explicitly weighed goal-push + personal fit against [[10_Areas/Career/Engineer Edge Roadmap]] — not "it looked interesting for a second." |
| Screened → Committed | The fit test passed. Contact-reachability and pay never block this step either way. |
| Committed → Contacted | A real contact was actually found by the `contact-researcher` agent — an empty result is a valid, honest outcome that doesn't block anything else. |
| Considering/Serious → Ended | An application was **actually submitted** — not decided, not drafted, submitted. |
| Ended (no Applying note) → Discarded | Automatic, by rule — no Applying note means it never really left the research phase, regardless of what the folder name implies. |
| Any stage → Job & Company created | You are concretely about to apply, not merely still considering it. |
| Applying → Result | A real outcome — offer, rejection, or withdrawal — not a guess about how it's probably going. |
## Why Nothing Past Discovery Is Automated, On Purpose
Every step from Screen onward requires a human judgment call this project has deliberately kept out of code: is this actually worth my time, does this person actually matter, does this company actually deserve the deep dive. The `/promote-dossier` skill exists to make the mechanical part of Step 3 (writing three cross-linked notes correctly) fast — it still asks for explicit consent before writing anything, because the judgment itself was never the slow part worth automating.
