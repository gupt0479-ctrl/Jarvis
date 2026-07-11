---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - orby
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[04 - Orby Integration]]"
---
# Orby Friction Fixes
> Source of truth derived from [[10 - Codebase Reality & Confusion Clearance]] Part 4. This note covers **only the small frontend frictions** to fix during this sprint. Orby's behaviour, the 3D model, the persona voice, and the chat-navigation wiring are **not** redesigned here — the deep Orby plan lives in the chatbot folder ([[04 - Orby Integration]] in `nextgen-chatbot/`). **Do not touch `OrbyCanvas.tsx`.**

## What Orby already is (context, not work)
A fully-implemented autonomous floating astronaut companion (NOT the chatbot — the chatbot is the Lab sidebar `PortfolioLab.tsx`). Files in `src/components/orby/`: `Orby.tsx` (RAF loop writes transforms directly — zero React re-renders for position), `OrbyCanvas.tsx` (live R3F astronaut, not a sprite — out of scope), `OrbySpeechCloud.tsx` (typewriter speech), `OrbyArrow.tsx`, `useOrbyState.ts` (11-state machine), `useTypedText.ts`.
- Position: RAF writes `wrapperRef.style.transform`; React state only for speech/state. Canvas 88px desktop / 64px mobile. `z-40` (under the `z-50` header). Hidden when `innerHeight<560 && innerWidth<400`.
- 11 states: intro → pointing → roaming → section-comment → exitingLeft → goodbye → departingLeft → returningRight, plus `chat-nav-home`/`chat-nav-arrival` (chat `navigate` tool via a `window` `CustomEvent('orby:navigate', {detail:{sectionId, orbyMessage}})`) and `reducedMotion`.
- Section speech fires for **`projects`, `blog`, `contact` only** — a deliberate calibration, not a gap.

## The three frictions to fix this sprint
1. **Speech-cloud right-edge clamping.** `OrbySpeechCloud.tsx` is `min-w-[200px] max-w-[300px]`, positioned `left-1/2 -translate-x-1/2` relative to Orby's wrapper, with **no viewport-edge clamping**. At Orby's home position (far right), the cloud can clip off-screen on narrow viewports. `positionAbove` flips above/below but does no horizontal clamp. **Fix:** clamp the cloud's X into `[8, vw - cloudWidth - 8]` in the RAF/cloud-position logic so it never clips the right (or left) edge.
2. **Section-timing recalibration.** After sections are rebuilt with new heights, the scroll thresholds in `useOrbyState.ts` that fire `section-comment` for projects/blog/contact may trigger at the wrong visual moment. **Re-verify and adjust thresholds** once section heights settle (do this near the end, after the section rebuilds).
3. **Mobile overlap check.** On ~375px phones, verify Orby doesn't overlap the Lab toggle button or hero content distractingly. The `tooSmall` guard (560×400) may not catch all cases — add a small offset or guard if it does.

## Sequencing
Friction (1) is independent — do anytime. Frictions (2) and (3) depend on the section rebuilds being done, so they run **after** the per-section work (this is Phase 5 in the corrected order, [[00 - Frontend Overhaul — Build Plan]]).

## Done conditions
- Speech cloud never clips the viewport edge at any Orby position/width.
- section-comment triggers fire at the right scroll moment for the rebuilt projects/blog/contact heights.
- No distracting Orby overlap on 375px mobile.
- Untouched: `OrbyCanvas.tsx` model, persona voice, new section copy, the chat-nav pipeline (chatbot folder owns it).
