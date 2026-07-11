---
type: concept
status: active
created: 2026-06-14
updated: 2026-06-14
tags:
  - portfolio
  - frontend
  - prompt
  - ui-polish
notes:
  - "[[BUILD-STATUS]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[14 - Global Fixes — Header & Section Spacing]]"
---
# UI Polish Sprint — Sidebar Shift, Gaps, Comet Reduction, Skill Buttons

> Claude Code prompt for 4 isolated visual fixes. Run in one session. Start at repo root. Run `pnpm typecheck` before closing.

---

## Context you must read first

Before touching anything, read these files in full:
- `src/components/ObsidianBackgroundCanvas.tsx` — understand the sidebar-aware shift already implemented and the `sidebarOpen` prop path
- `src/app/globals.css` — understand `.section-backdrop`, `--section-pad-y` (if it exists), section spacing tokens
- `src/components/ui/comet-card.tsx` — understand the 4 variants (`default`, `dark`, `subtle`, `ghost`) and what props control tilt sensitivity and drift
- `src/components/sections/BlogSection.tsx` and `src/components/BlogFeed.tsx` — understand how CometCard is used on each blog card
- `src/components/ContactPanel.tsx` — understand how CometCard wraps the contact section
- `src/components/sections/SkillsSectionClient.tsx` — understand the category filter pill markup and its current CSS classes

Do not touch `OrbyCanvas.tsx`. Do not touch the Three.js physics in `ObsidianBackgroundCanvas.tsx` (the sphere/ring/starfield math). Only touch layout/transform behavior for the sidebar shift.

---

## Fix 1 — Sidebar: background and all content move together; sphere stays centered

**Problem:** When the portfolio lab sidebar opens, the background canvas shifts its right edge but the sphere visual center does not move to stay centered in the remaining viewport. The result is that the sphere drifts toward the left side of the visible area, and the main content does not compress symmetrically around the new center. The user expects: everything on the page (background + content) shifts left uniformly when the sidebar opens, so the sphere always appears centered in whatever space is visible.

**What already exists:** `ObsidianBackgroundCanvas.tsx` already accepts a `sidebarOpen` prop and shifts its right edge `448px` left with a `cubic-bezier` transition. The sidebar is `w-[448px]`. The main content wrapper (find it — it is likely in `src/app/(portfolio)/layout.tsx` or `src/components/PortfolioContent.tsx` or the root `page.tsx`) may or may not already shift.

**What to do:**

1. **Read `src/app/(portfolio)/page.tsx` and `src/app/(portfolio)/layout.tsx`** to find how `sidebarOpen` state is passed to child components and what wraps the main content area.

2. **Identify the main page content wrapper** — the div/section that wraps all portfolio sections below the hero. This is the container that needs to shift left when the sidebar opens.

3. **Apply a matching left-shift on the main content wrapper.** When `sidebarOpen === true`, add `translateX(-224px)` (half the sidebar width = 224px) to the main content wrapper with the same transition timing as the canvas (`cubic-bezier(0.4, 0, 0.2, 1)` duration `300ms`). This centers the content in the remaining space.

4. **In `ObsidianBackgroundCanvas.tsx`**, confirm the canvas itself also shifts so the sphere center point (which is computed relative to canvas center) moves left by `224px` when sidebar opens. The existing right-edge shift already does part of this — verify that the canvas width is reduced by 448px AND the canvas is not offset from its left edge, so the sphere's center naturally lands at the midpoint of the narrowed canvas.
   - If the current implementation only clips the right edge without shifting the sphere center: change the approach to `width: sidebarOpen ? 'calc(100vw - 448px)' : '100vw'` on the canvas container, with `transition: width 300ms cubic-bezier(0.4, 0, 0.2, 1)`. The sphere, computed at `canvas.width / 2`, will then always sit at center of visible area.

5. **The header** (`HeaderScrolling.tsx`) should also compress or shift so its content stays within the non-sidebar zone. Verify the header does not overlap the sidebar.

6. **Test at 1280px and 1440px viewport widths** with sidebar open/closed. The sphere must be visually centered in the non-sidebar zone at both widths.

**Do not change:** sphere radius, particle counts, physics parameters, the `448px` sidebar width constant, or any animation in `OrbyCanvas.tsx`.

---

## Fix 2 — Reduce the gap between Education and Certifications sections

**Problem:** There is too much vertical space between the Education section and the Certifications section. The gap is larger than between any other consecutive sections on the page.

**What to do:**

1. **Find the section wrappers** for `EducationSection` and `CertificationsSection` — read `src/components/sections/EducationSection.tsx` and `src/components/sections/CertificationsSection.tsx`. Note the `py-*` or `mt-*` / `pt-*` classes on the outermost `<section>` or container div.

2. **Read `src/app/globals.css`** and find `.section-backdrop` and any section spacing utility. If a global `--section-pad-y` token exists, verify Education and Certifications are using it.

3. **Reduce the top padding / margin on `CertificationsSection`** so the gap between Education and Certifications matches the gap between other consecutive sections (e.g., Experience → Projects, Projects → Skills). Do not shrink the internal padding of either section — only the space between them.

4. **If Achievements renders immediately after Certifications** as a subsection: leave its top padding minimal (per the existing note in `14 - Global Fixes`), it reads as one block with Certifications.

5. After the change, scroll through the full page and confirm all inter-section gaps look uniform. If other sections have inconsistent gaps, normalize them to one value now. Document the chosen value in a comment in `globals.css`.

---

## Fix 3 — Reduce comet card and wiggle on blog cards and contact card

**Problem:**
- The "What I Read or Do" section (BlogSection/BlogFeed) has CometCard + wiggle/drift on every card. The cards wiggle too aggressively on cursor movement and the comet is too intense, making the "Visit" button hard to click. 
- The Contact card has the same issue — it is smaller than blog cards so even a little cursor movement shifts it dramatically.

**CometCard primer:** Read `src/components/ui/comet-card.tsx` to understand which props control (a) tilt sensitivity/max tilt angle, (b) comet opacity/size/speed, (c) transition speed. There may be a `maxTilt`, `tiltSensitivity`, `cometIntensity`, or similar prop — identify the exact prop names from the component.

**What to do for blog cards:**

1. **In `src/components/BlogFeed.tsx`** (and/or `src/components/sections/BlogSection.tsx`):
   - Find every `<CometCard>` wrapping a blog card.
   - Reduce tilt max angle to `4°` or less (from whatever it currently is).
   - If there is a sensitivity or parallax multiplier prop, cut it by ~50%.
   - If the comet intensity/opacity is configurable, reduce it by ~40%.
   - The GitHub card is explicitly exempt — it keeps its current effect per product decision. Identify the GitHub card by its distinct left violet rail / solid background and do NOT change its CometCard props.
   - The small resource cards (non-GitHub) are the ones to dial down.

2. **Remove or reduce `useSpaceFloat` / any continuous drift** applied to the non-GitHub blog card wrappers. These cards should not wander on their own — they should be stationary until the user hovers. The wiggle that makes the Visit button hard to click is coming from idle drift, not CometCard tilt. Remove the idle drift entirely from blog cards (except GitHub card which should keep its behavior).

**What to do for contact card:**

1. **In `src/components/ContactPanel.tsx`**:
   - Find the `<CometCard>` wrapping the contact panel.
   - This card is smaller, so sensitivity should be halved relative to blog cards — apply `maxTilt: 3°`, sensitivity at minimum.
   - Remove any `useSpaceFloat` continuous drift from the contact card wrapper.
   - The contact card should only respond to hover, not drift on its own.

**Acceptance:** The user can move cursor over a blog card and click "Visit" without the card drifting away. The effect should feel refined, not absent — there is still a tilt effect on hover, just subtle.

---

## Fix 4 — Skill category buttons: more visible against the background

**Problem:** The skill category filter buttons (AI/ML, Backend, Cloud, Database, etc.) in the Skills section are visually drowned out by the ObsidianBackground — the background is too bright/active and the buttons look washed out.

**What NOT to do:** Do not touch the background. Do not reduce the background's intensity or opacity.

**What to do:**

1. **Read `src/components/sections/SkillsSectionClient.tsx`** and find the category filter pill/button markup. Note the current Tailwind classes (background color, text color, border, padding, font-size).

2. **Make the buttons darker and more opaque:**
   - Increase the background opacity of each button. If they currently use something like `bg-white/10` or `bg-purple-500/20`, increase to at least `bg-white/20` or `bg-neutral-900/70` with a clear border.
   - Add or strengthen the border: `border border-white/30` or `border border-violet-400/40`.
   - If there is a backdrop-blur on the buttons, increase it slightly: `backdrop-blur-sm` → `backdrop-blur-md`.
   - The selected/active category button should be clearly darker still with a stronger border or bg opacity.

3. **Make the buttons slightly larger:**
   - Increase padding from current values to `px-4 py-2` (or equivalent if already using those values, go `px-5 py-2.5`).
   - Increase font size by one step if currently `text-xs` → `text-sm`. If `text-sm`, leave it.

4. **Do not change the hover effects on the buttons** — the existing hover micro-interactions (shimmer, blink cursor, pulse-glow, etc.) are good. Only touch background color, border, size, and opacity of the resting state.

5. **Run `pnpm typecheck` before committing.** No type errors introduced.
