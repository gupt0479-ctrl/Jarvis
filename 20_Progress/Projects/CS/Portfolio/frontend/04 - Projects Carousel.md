---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - projects
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[01 - Motion System & Comet Cards]]"
  - "[[09 - Sanity Content Spec]]"
---
# Projects Carousel
Files: `ProjectsSlider.tsx`. Kicker: `// build log`. This is called out as the single ugliest, weakest section — rebuild it.

## Header (brief item 4)
Move the header **to centre**, like every other section. Today it's left-aligned with `// build log` above it; centre both the kicker, the "Projects" title, and the description. Match the centred pattern used by Skills/Education/Certifications/Contact.

## The three-card space carousel (brief items 4, 7)
A centre card flanked by a left and right peek card.
- **Centre card:** large, dark, readable, *premium before hover*. Gets `CometCard` (reduced tilt) **and** `useSpaceFloat` bounded to its padding — it wanders gently, zero-gravity, never leaving its box.
- **Side cards:** translucent (keep it), each drifting in its **own** padding via `useSpaceFloat`. They do **not** get the comet effect — comet is exclusive to whichever card is centred. Keep them not-too-close / not cramped, clearly separated from the centre.
- **Arrows:** vertically centred beside the main card, not overlapping it. Accessible names; keyboard arrows + swipe still work.

## The transition (brief items 4, 7)
On clicking left/right:
- The chosen side card **glides to centre** with a smooth transition; the old centre card glides out to the opposite side.
- The incoming card **gains** the comet effect as it lands centre; the outgoing card **loses** it.
- Side cards keep their current opacity while wandering — don't flash them opaque.
- **Tether / string-pull:** add a subtle interactive background cue — a particle trail or an elastic "string" that appears to pull the incoming card toward centre on click. Keep it subtle; respect reduced-motion.
- Pagination dots below, styled as glowing orbit dots (keep the `1 / 6` counter).

## Hover behaviour (brief items 7, 10) — depends on Sanity content first
The old "all cards move down on hover" is gone (handled globally in [[01 - Motion System & Comet Cards]]). New behaviour:
- The centre card is never empty before hover — it already shows title, tagline, tech chips, and a small inner "case note" box (a metric / system note).
- On hover it reveals **a detailed summary** (the Sanity `description`) and, below it, the drop-down with **Source (GitHub)** and **View Live** buttons as floating buttons.
- Side cards keep wandering while hovered — they do not freeze even when more content shows.
- The expanded card must **not** become extremely large; cap its height and scroll internally if needed.

## Content + links (brief items 5, 8) — see [[09 - Sanity Content Spec]]
- All filler/"Alex Morgan"/Lovable data is replaced with **real Anant projects** written professionally: OpsPilot, Resq, SafeReach, the nextgen AI portfolio agent, the Jarvis vault system, etc.
- Live demos are mostly broken/undeployed by the user's own account — **do not chase live links.** Each project's `liveUrl` may be empty; when empty, hide "View Live" and let Orby's existing "site may be down, check GitHub" line stand. **`repoUrl` always points to the correct GitHub repo.**
- Skill chips: shared `<SkillChip>` (colour + name only) from `project.skills[]→ref`. Nothing hardcoded.

## Done conditions
- Header centred; three-card space carousel with bounded drift; comet only on centre; smooth tether transition; glowing orbit dots.
- Hover reveals real summary + Source/Live floating buttons without ballooning; side cards keep drifting.
- Every field (title, tagline, summary, chips, repoUrl) from Sanity; real content loaded; broken live links not surfaced.
