---
type: concept
status: active
updated: 2026-09-05
tags: [portfolio, frontend, ui-fixes, about, gsap]
notes:
  - "[[UI Fixes]]"
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-design]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[frontend-ui-fixes-index]]"
  - "[[ui-fix-03-about-telemetry]]"
---

# UI Fix 02 — About Section (Pinned Scroll + Summary)

> **Status:** open (no ScrollTrigger pin; bio expand button-only — both confirmed live 2026-09-05)
> **Ledger:** [[UI Fixes]] §2 | **Tasks:** 3.0–3.2, 3.4
> **2026-09-05 verification pass:** re-checked every claim below against `AboutSection.tsx`, `AboutSectionClient.tsx`, `Providers.tsx`, `package.json` on `post-frontend`. Unlike [[ui-fix-01-hero-background]], this note had no phantom symbols — it was already close to correct. One real finding: **the GSAP ScrollSmoother-vs-native open question is already answered by existing code** (see below) — treat it as resolved, not open.

## Purpose

Transform About from a scroll-through prose block into a **cinematic pinned moment**: short summary + 2 stat cards, scroll-driven summary transform, mesmerizing background scatter, and click-anywhere bio expand.

## Current code (re-verified 2026-09-05)

| File | Confirmed behavior |
|---|---|
| `src/components/sections/AboutSection.tsx` | Server component. `ABOUT_QUERY` fetches `aboutSummary`, `fullBio`, `stats` from the profile singleton. **`id="about"` is already on the `<section>`** (line 37) — nothing to add there, just don't remove it. |
| `src/components/sections/AboutSectionClient.tsx` (168 lines) | `expanded` state (line 94). Toggle is **button-only**: the "Read full bio"/"Show less" `<button>` at lines 137–151 is the *sole* `onClick` in the file — confirmed no click handler on the `CometCard` wrapper (line 104) or the prose `<div>` (line 105). |
| `src/sanity/schemaTypes/profile.ts` | `aboutSummary` field exists (line ~86, "3–4 sentence collapsed-state summary"). `stats[]` array at line 159 with `label`/`value`/`summary` (required/required/optional) — confirmed, no `order` field exists. |
| `src/components/Providers.tsx` | **`gsap.registerPlugin(ScrollTrigger)` already runs here, and `lenis.on("scroll", ScrollTrigger.update)` already wires Lenis (the site's scroll driver) to ScrollTrigger.** This answers design doc Open Question 6: the project already uses native Lenis scroll + ScrollTrigger, not ScrollSmoother — that decision is made, don't re-litigate it in the pin implementation. |
| `src/components/ui/split-heading.tsx` | Also registers `useGSAP` + `ScrollTrigger` + `SplitText` (for a scroll-triggered text-reveal-on-enter effect on section headings, no pin/scrub). Confirms `@gsap/react`'s `useGSAP` is the established pattern in this repo — use it for the new pin too, don't reach for raw `useEffect` + manual ScrollTrigger cleanup. |
| `package.json` | `gsap ^3.15.0` and `@gsap/react ^2.1.2` **confirmed installed** — no `pnpm add` needed. |
| Any `about-pin.ts` / `useSectionPin` hook | **Confirmed does not exist yet** (grepped `src/` for both names) — this is genuinely new code, not a rename/extend of something existing. |
| Background | No sync with About scroll — confirmed, `background:mode` CustomEvent system doesn't exist yet (see [[ui-fix-01-hero-background]] — it's explicitly out of scope for that task too, so don't expect it to land before this one). |

## Target behavior

### Scroll pin (GSAP ScrollTrigger)
- Trigger: user scrolls past hero into `#about` (id already present — just target it, don't add it).
- Pin duration: ~**1 viewport height** (`pin: true`, `scrub: 1`, `anticipatePin: 1`).
- Use `@gsap/react`'s `useGSAP` with cleanup on unmount — same pattern as `split-heading.tsx`, not a bespoke one.
- Scroll source is already Lenis, already synced to `ScrollTrigger.update` in `Providers.tsx` — a plain `ScrollTrigger.create(...)` inside `useGSAP` picks this up automatically. Do not add a second Lenis instance, do not add ScrollSmoother, do not add a manual scroll listener.

### Timeline beats (scroll-scrubbed progress 0→1)

| Progress | DOM state | Background |
|---|---|---|
| 0.0–0.4 | `aboutSummary` visible + 2 telemetry cards | `about-pin` high-amplitude scatter |
| 0.4–0.8 | Summary morph / second summary text | scatter continues, slower reform |
| 0.8–1.0 | Hold or subtle hint toward full bio | fade to `idle` |

**Open question (still genuinely open, not code-resolvable):** Beat 2 content — second Sanity field vs. derived Portable Text block. Default if unspecified: use the second paragraph of `fullBio` (`profile.fullBio[1]`) rather than adding a new schema field, since `fullBio` is already fetched and no `aboutSummary2` field exists today.

### Click-anywhere bio expand (orthogonal to pin)
- Click **anywhere** on the About card surface OR description text toggles `expanded` — currently only the button at line 139 does this (`onClick={() => setExpanded((v) => !v)}`).
- Add the same handler to the `CometCard`/prose wrapper; keep the button as a secondary, visually-labeled affordance (don't remove it — it's the only visible affordance a non-hovering/keyboard user has that expansion is possible).
- Reuse the exact `AnimatePresence` / `height: "auto"` / `duration: 0.3` pattern already in this file (lines 117–133) for consistency — don't introduce a second animation approach.
- `aria-expanded` stays on whichever element is the primary interactive target.

### Layout
- Collapsed About (summary + 2 cards) should fit ~1 viewport at 375px and 1440px — this is a visual QA check, not a code claim to verify statically.
- Section kicker `// scan report` / "A quick system scan." — unchanged, already correct in `AboutSection.tsx`.

## Files to create/modify

| File | Action |
|---|---|
| `src/lib/gsap/about-pin.ts` (new) | ScrollTrigger pin setup, following `split-heading.tsx`'s `useGSAP` pattern |
| `src/components/sections/AboutSectionClient.tsx` | Pin ref, click-anywhere expand (extend existing `onClick`, don't duplicate state) |
| `src/components/sections/AboutSection.tsx` | No change expected — `#about` id already present |
| `src/components/three/ObsidianBackgroundCanvas.tsx` | `background:mode` listener — **separate task (3.4), not this one** |

## Sanity content

- `profile.aboutSummary` — populate 3–4 sentences for Beat 1 (schema already supports this).
- Beat 2: no new field needed by default (see Open Question above) — only add `aboutSummary2` if the default (`fullBio[1]`) is rejected during review.
- Stats: only 2 cards — see [[ui-fix-03-about-telemetry]].

## Accessibility

- Pin must not trap keyboard focus.
- Reduced motion (`prefers-reduced-motion`): skip the pin entirely, render `aboutSummary` + 2 cards in normal document flow immediately — this repo already has a `useReducedMotion`-style pattern in `ObsidianBackgroundCanvas.tsx`; check for a shared hook before writing a new media-query listener.
- Click-anywhere target: keep the explicit button visible for users who wouldn't discover click-anywhere; don't rely on it as the only affordance.

## Acceptance criteria

- [ ] Scroll into About: section pins ~1 viewport, using the existing Lenis+ScrollTrigger wiring (no new scroll library)
- [ ] Scroll scrub changes summary beat
- [ ] Clicking anywhere on the bio card (not just the button) expands it
- [ ] Existing button-only toggle still works (regression check)
- [ ] Reduced motion: static layout, no pin, no scroll-lock
- [ ] No layout jump on unpin
- [ ] `pnpm typecheck && pnpm lint` pass

## Implementation prompt

> Single autonomous session (Claude Sonnet 5 in Cursor). Front-loaded so no follow-up turn is needed.

```
Read ui-fix-02-about-section.md in full first. Confirmed facts you can rely on without re-verifying: gsap and @gsap/react are already installed (package.json); gsap.registerPlugin(ScrollTrigger) and Lenis→ScrollTrigger.update wiring already exist in src/components/Providers.tsx; useGSAP is already used for a scroll-triggered effect in src/components/ui/split-heading.tsx (copy that pattern, not a new one); #about id already exists on the section in AboutSection.tsx; no about-pin.ts or useSectionPin hook exists yet — you are creating it new, not renaming/extending something.

TASK:
1. Create src/lib/gsap/about-pin.ts (or a hook, matching whatever split-heading.tsx's pattern actually is once you read it) that pins #about for ~1 viewport height using ScrollTrigger (pin: true, scrub: 1, anticipatePin: 1), driven by useGSAP with cleanup on unmount.
2. Wire a 0→1 scroll-scrubbed timeline with two beats: 0.0–0.4 shows aboutSummary + the 2 telemetry cards (see ui-fix-03-about-telemetry for that half — do not implement telemetry changes here, they're a separate task); 0.4–0.8 transitions to a second summary state using profile.fullBio[1] if no second summary field exists (do not add a new Sanity field for this unless fullBio has fewer than 2 blocks).
3. In AboutSectionClient.tsx, extend the EXISTING expanded state (line 94, do not add a second state) so clicking anywhere on the CometCard/prose wrapper also toggles it, in addition to the existing button at line 139. Do not change the button's own behavior.
4. Dispatch a background:mode CustomEvent with detail about-pin at pin start and idle at pin end — this is a stub for a listener that doesn't exist yet (Task 3.4), so it's fine if nothing currently consumes it; do not build the ObsidianBackgroundCanvas.tsx listener side in this task.
5. prefers-reduced-motion: skip the pin entirely (check how ObsidianBackgroundCanvas.tsx detects it and reuse the same approach if there's a shared hook — grep for useReducedMotion or matchMedia before writing a new listener).

CONSTRAINTS:
- Do not add ScrollSmoother, a second scroll library, or a manual scroll event listener — Lenis + ScrollTrigger is already wired and sufficient.
- Do not touch AboutTelemetry.tsx or TelemetryDetail.tsx in this task (separate task, ui-fix-03-about-telemetry).
- Do not remove the existing "Read full bio" button or its aria-expanded attribute.
- Kill every ScrollTrigger instance you create on unmount — this is a long page with other sections; leaking triggers breaks other scroll behavior.

VERIFY and report each explicitly:
(a) Scrolling into About pins the section for approximately one viewport height, not more/less.
(b) Clicking the bio card body (not the button) expands it; clicking the button still works too.
(c) Reduced motion: no pin occurs, summary + cards render immediately in normal flow.
(d) No duplicate ScrollTrigger registration warnings in the console.
(e) Other sections' scroll behavior (e.g. the split-heading reveal effect) is unaffected.
Run pnpm typecheck && pnpm lint and paste the output. Do not deploy, do not commit.
```

## Dependencies

- Task 3.0 (GSAP research) — largely already answered by this note's Providers.tsx/split-heading.tsx findings; treat 3.0 as a quick confirmation read, not fresh research.
- Task 1.1 (Sanity content: `aboutSummary` populated)
- Task 2.1 + 3.4 (background scatter modes) — this task only dispatches the event, doesn't consume it
- [[ui-fix-03-about-telemetry]] (2-card layout renders inside Beat 1, but is a separate implementation task)

## Risks

- Multiple ScrollTriggers on a long page — kill on unmount, and be aware `split-heading.tsx` already registers its own per-heading triggers; don't assume yours is the only one active.
- `backdrop-filter` on `.cosmic-card` during pin — test GPU cost on mobile.
- Pin + expanded bio height — expanding the full bio during an active pin may exceed the pinned viewport; either allow internal scroll or force an early unpin when expanded is true. Decide and document which, don't leave it ambiguous in the diff.
