---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - theming
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Dark Mode Toggle
> Source of truth derived from [[10 - Codebase Reality & Confusion Clearance]] Part 3. File: `src/components/HeaderScrolling.tsx` (~lines 167–170). Theme infra: `src/components/ThemeProvider.tsx`.

## Current state
The "Dark" pill in the header is a **decorative `<div>`** — Moon icon + the word "Dark" — with no `onClick`, no `useTheme()`, no state. It is a cosmetic status indicator, not a control. Meanwhile `ThemeProvider` is correctly wired (`next-themes`, `attribute="class"`, `defaultTheme="dark"`, `enableSystem`) — the switching infrastructure exists; the pill just isn't connected.

## Why full light mode is out of scope
The whole design system assumes the near-black canvas (`#05040A`). Every `cosmic-card`, `float-btn`, `section-kicker`, `section-backdrop`, `orbit-chip` token is defined **only inside the `.dark { }` block** in `src/app/globals.css`. There is no `.light` palette. Real light mode would require: a full light palette for every cosmic-card variant (translucent surfaces vanish on white), the Three.js background adapting star/planet colours (muted violet looks muddy on light), and every `text-white/*` / `border-white/*` utility rethought. That is a design-system rewrite — explicitly deferred per [[00 - Frontend Overhaul — Build Plan]] (Anant: "no idea what light mode would look like").

## The decision: make it a real, dark-only control (≈10 min)
Convert the `<div>` to a semantically-correct `<button>` that owns `useTheme()` but is a deliberate no-op until light mode is designed. This gives correct semantics (screen-reader role=button) and an honest affordance without committing to the rewrite.

```tsx
'use client'
import { useTheme } from 'next-themes'
// HeaderScrolling is already a client component
const { theme } = useTheme()

<button
  type="button"
  onClick={() => {/* light mode not yet designed — wire setTheme('light') here later */}}
  aria-label="Color theme — dark mode active (light mode coming soon)"
  className="float-btn ml-auto hidden shrink-0 items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1.5 text-xs text-white/50 md:flex cursor-default"
>
  <Moon className="h-3.5 w-3.5" />
  <span className="hidden sm:inline">Dark</span>
</button>
```
`cursor-default` keeps it from feeling clickable since it's a no-op. When light mode is later designed, wire `setTheme('light')` into `onClick` and swap the icon on `theme`.

**Acceptable alternative:** leave it a `<div>` but add `role="status"` + `aria-label="Color theme: dark"` so it's a correct status indicator. Either is minutes of work.

## Must also be STATIC (2026-06-13)
The pill currently **drifts/wobbles** in the header — a `useSpaceFloat`/continuous-drift was applied. **Remove it.** A header control must not wander. Hover-lift is fine; idle motion is not. Full detail in [[14 - Global Fixes — Header & Section Spacing]] §1.

## Done conditions
- The header theme pill is semantically correct (button-with-aria, or status-div-with-aria), keyboard-reachable, and **does not drift** (static in the header).
- No light-mode palette work; `setTheme('light')` left as a documented future hook.
