---
type: concept
status: active
updated: 2026-09-05
tags: [portfolio, frontend, ui-fixes, logo, footer, branding]
notes:
  - "[[UI Fixes]]"
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-design]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[frontend-ui-fixes-index]]"
---

# UI Fix 06 — Logo & Footer

> **Status:** open (footer sizing is a real, small gap; the "glow when Lab open" premise did not survive a repo check — see below)
> **Ledger:** [[UI Fixes]] §5 | **Tasks:** 6.1, 6.2
> **2026-09-05 correction pass:** re-verified line-by-line against the live repo on `post-frontend`. Most of this note (the glyph asset, the fallback, the favicon sync) was already accurate. One load-bearing claim was not: there is no in-page component whose glow differs when the Lab sidebar is open vs closed, because the liquid-metal "A" (`HeaderLogo`) is **only rendered in `Footer.tsx`** — not in the header, not in the Lab panel. Same correction applied to [[frontend-ui-fixes-design]] Fix 8 and [[frontend-ui-fixes-tasks]] Tasks 6.1–6.2.

## Purpose

The calligraphic-A glyph asset (`logoGlyphPath.ts`) is solid and already shared correctly between its three renderers. What's left is real but narrower than previously scoped: size the footer instance to match the footer text, and get a real repro (or drop) on the "glow when Lab open" complaint before anyone touches shader code chasing a bug that may not exist in the current tree.

## Current code (re-verified 2026-09-05)

| File | What exists today |
|---|---|
| `src/lib/logoGlyphPath.ts` | Confirmed: `LOGO_GLYPH_SVG_PATH`, `LOGO_GLYPH_VIEWBOX = 236`. Single source of truth, comment explicitly says do not hand-edit — regenerate from trace. |
| `src/app/icon.svg` | Confirmed: favicon, viewBox `0 0 236 236`, comment states it's hand-synced from `logoGlyphPath.ts`. |
| `src/components/three/HeaderLogo.tsx` | Confirmed: feature-detects WebGL2 once client-side, renders `HeaderLogoFallback` underneath always, cross-fades in `HeaderLogoCanvas` on top when supported + ready. Takes exactly one prop: `show: boolean`. |
| `src/components/three/HeaderLogoCanvas.tsx` | Confirmed: R3F canvas, `LiquidMetalMaterial`, orthographic camera, `useAnimationGate({ show })`, `useLogoTexture` for the rasterized texture (**not** `logoTexture.ts` as previously guessed — the real file is `src/hooks/useLogoTexture.ts`). Fixed 32×32 CSS px footprint (`CANVAS_CSS_PX = 32`). |
| `src/hooks/useAnimationGate.ts` | Confirmed: `paused = documentHidden \|\| show === false`. This is a hard animation pause/resume (stops the R3F frameloop), **not** an intensity, brightness, or bloom control. No glow-strength logic lives here. |
| `src/components/three/HeaderLogoFallback.tsx` | Confirmed: static SVG using the same path/viewBox, same fixed 32×32 footprint (`FALLBACK_CSS_PX = 32`), violet→cyan gradient fill. |
| `src/components/Footer.tsx` | Confirmed: `<HeaderLogo show={true} />` at line 43, immediately left of "Anant's Hub" text, inside a `flex items-center gap-2` column-1 cell of a 3-column grid. **`show={true}` is a hardcoded literal — it is never tied to any sidebar/open state.** |
| `src/components/HeaderScrolling.tsx` | **Does not render `HeaderLogo` at all.** The header wordmark (lines 145 and 205, desktop bar + mobile sheet) is plain text: `Anant<span className="text-violet-400">.</span>` — no shader, no glow, no shadow, no conditional class tied to `open`/sidebar state. |
| `src/components/lab/PortfolioLab.tsx` | **Does not render `HeaderLogo` or any brand mark.** Its header (~line 282) is just a `// portfolio lab` kicker line, a description, and a close button. |
| `src/components/SidebarToggle.tsx` | The floating flask-icon button that opens the Lab (`aria-label="Open Portfolio Lab"`) has a permanent `animate-[pulse-glow_3s_ease-in-out_infinite]` class — this **is** a real, always-on glow, but it's on the flask FAB, not on any "A" glyph, and it doesn't turn on/off with the sidebar (it just slides left when open). Do not confuse this with the logo complaint. |

### What this means for "glow mismatch when Lab open"

`HeaderLogo` exists in exactly **one** place in the render tree: the footer. It never appears in the header or the Lab panel today, and its one caller (`Footer.tsx`) passes a hardcoded `show={true}` regardless of sidebar state. There is no code path anywhere that changes a logo's glow/brightness based on the Lab being open or closed.

**2026-09-05 follow-up — user confirmed:** this is about the actual **browser tab favicon** (`src/app/icon.svg`), not any in-page component.

Checked `icon.svg` directly: it's a flat `linearGradient`-filled path with no `filter`, no `feGaussianBlur`, no `drop-shadow`, no glow of any kind — just a violet-to-cyan gradient fill, same as `HeaderLogoFallback.tsx`. Next.js's `app/icon.svg` file-convention favicon is static; nothing in this repo swaps it based on client-side state (no JS touches `<link rel="icon">`), and browsers don't apply any glow/brightness effect to favicons on their own. So **"glow differs when the Lab tab is open vs closed" cannot be literally true for a favicon** — there is no mechanism, browser-side or app-side, that could make it differ by state.

This leaves two real possibilities:
1. **Not an actual bug** — the gradient favicon was observed at two different moments and misattributed to "Lab open vs closed"; nothing to fix.
2. **A real but different complaint**: the gradient itself just reads as too bright/"glowy" at real favicon size, independent of any state. If that's it, it's a one-line design tweak to the *rendered* favicon (e.g. flatten to a single solid color, or reduce the gradient's contrast) — separate from and much smaller than a "fix the open/closed bug" task, and can ride along with Task 6.1's glyph regeneration if wanted.

**Default: treat as closed, no code change**, unless the user specifically asks for (2) above.

## Target behavior

##### 1. "Glow mismatch" — RESOLVED 2026-09-05: no code path exists, closed by default

Confirmed to be about the static favicon (`icon.svg`), which has no glow/filter and no state-dependence — see the diagnosis above. **No code change** unless the user separately asks to tone down the favicon's gradient brightness on its own merits (option 2 above); that would be a one-line tweak to `icon.svg`'s gradient stops, not a bug fix, and is not included in the implementation prompt below.

### 2. Thinner, more cursive A — accurate, actionable as before
- Edit source: regenerate `LOGO_GLYPH_SVG_PATH` in `logoGlyphPath.ts` from the design trace tool (per its own header comment — do not hand-edit the path data).
- Re-sync downstream: `src/app/icon.svg`, and confirm `useLogoTexture` (the rasterizer `HeaderLogoCanvas` calls) and `HeaderLogoFallback.tsx` need no changes beyond picking up the new `LOGO_GLYPH_SVG_PATH`/`LOGO_GLYPH_VIEWBOX` constants (they already just reference them, so a path-only regeneration should require zero code changes in those two files — verify this stays true).
- Keep `LOGO_GLYPH_VIEWBOX = 236` and both fixed 32px footprints (`CANVAS_CSS_PX`, `FALLBACK_CSS_PX`) unchanged — only the traced path data changes.

### 3. Footer sizing — the one real, well-scoped gap
- `HeaderLogo` takes only a `show` prop today; there is no size override. Both its children hardcode 32×32 CSS px.
- Target: the footer instance should visually match the adjacent `text-sm` "Anant's Hub" label height (roughly `1em`), not a fixed 32px box.
- Smallest fix: wrap the `<HeaderLogo show={true} />` call in `Footer.tsx` in a fixed-size container (e.g. `className="h-[1em] w-[1em]"` on a wrapping `span`) and scale the inner fixed-32px box down with a CSS `transform: scale()` — this avoids threading a new size prop through three files (`HeaderLogo` → `HeaderLogoCanvas`/`HeaderLogoFallback`) for what only the footer needs today. If a real size prop turns out to be needed later (a second non-footer usage appears), that's a separate, bigger change — don't build it speculatively now.

## Files to modify

1. `src/lib/logoGlyphPath.ts` — regenerate `LOGO_GLYPH_SVG_PATH` (thinner/more cursive A). Do not hand-edit the path by guessing coordinates.
2. `src/components/Footer.tsx` — wrap `<HeaderLogo show={true} />` to size it to `~1em` matching the footer text, without touching `HeaderLogo`'s own API.
3. Do NOT touch `HeaderScrolling.tsx`, `SidebarToggle.tsx`, or `PortfolioLab.tsx` for this task — none of them render the glyph, and the "glow" item is blocked on a repro (see above).
4. Do NOT touch `HeaderLogoCanvas.tsx`, `useAnimationGate.ts`, or `liquidMetalMaterial.ts` — no glow/intensity bug was found in them; don't invent a fix for an unconfirmed bug.

## Accessibility (existing contract — unchanged)

- `HeaderLogo`'s wrapper `<span>` is `aria-hidden="true"` — decorative, correct as-is (confirmed in code comments).
- Adjacent visible text ("Anant's Hub" in the footer) supplies the accessible name.
- Do not add `aria-label` to the glyph itself.

## Acceptance criteria

- [ ] `logoGlyphPath.ts`'s traced path reads visibly thinner/more cursive across all three renderers (canvas shader, fallback SVG, favicon)
- [ ] Footer glyph visually matches the height of "Anant's Hub" text (`~1em`), not a fixed oversized 32px box
- [ ] Header and Lab panel are unchanged (they never had this glyph — confirm no regression from touching shared files)
- [ ] Favicon (`icon.svg`) still matches the glyph after regeneration
- [ ] `pnpm typecheck && pnpm lint` pass
- [x] "Glow mismatch when Lab open" resolved: confirmed to be the static favicon, no code path ties it to sidebar state, closed with no change unless a separate gradient-brightness tweak is requested

## Implementation prompt

> Written for a single autonomous coding session (Claude Sonnet 5 in Cursor). This prompt covers only the two confirmed, well-scoped items (glyph shape + footer sizing). The "glow" item was investigated and closed — see CONTEXT — it is deliberately excluded here.

```
Read ui-fix-06-logo-footer.md in full before touching any file. It contains a verified 2026-09-05 correction: the liquid-metal "A" glyph component (HeaderLogo, src/components/three/HeaderLogo.tsx) is rendered ONLY in src/components/Footer.tsx today. It does NOT exist in src/components/HeaderScrolling.tsx (plain text wordmark there) or src/components/lab/PortfolioLab.tsx (no logo there at all).

The "glow differs when Lab tab is open vs closed" complaint was confirmed by the user to be about the static browser-tab favicon (src/app/icon.svg), then investigated and closed: icon.svg has no filter/blur/drop-shadow of any kind (just a flat gradient fill) and nothing in the repo ties it to sidebar/Lab state — favicons are static and can't differ by client-side state without machinery that doesn't exist here. There is nothing to fix for this item. Do not go looking for a glow bug in HeaderLogoCanvas.tsx / useAnimationGate.ts / liquidMetalMaterial.ts — none was found there on inspection, and "fixing" a confirmed-nonexistent bug is out of scope for this task.

TASK — implement exactly these two items, nothing else:

1. Regenerate the glyph to be thinner and more cursive:
   - Edit src/lib/logoGlyphPath.ts's LOGO_GLYPH_SVG_PATH per its own header comment (regenerate from the design trace, do not hand-edit path coordinates by guessing).
   - Keep LOGO_GLYPH_VIEWBOX at 236 and both fixed-footprint constants (CANVAS_CSS_PX, FALLBACK_CSS_PX, both 32) unchanged.
   - Confirm src/app/icon.svg, src/components/three/HeaderLogoFallback.tsx, and the useLogoTexture rasterizer hook (src/hooks/useLogoTexture.ts) need no code changes beyond picking up the new path constant — they already just reference LOGO_GLYPH_SVG_PATH/LOGO_GLYPH_VIEWBOX. If any of them turns out to hardcode geometry independently of those constants, flag that as a separate finding rather than silently duplicating your edit.
   - Manually sync icon.svg's path data to match (its own comment says it's hand-synced, not auto-generated). Do not otherwise change icon.svg's gradient stops or add any filter — that's a separate, not-yet-requested change.

2. Size the footer's logo instance to match its adjacent text:
   - In src/components/Footer.tsx (~line 43), HeaderLogo currently renders at a fixed 32x32 CSS px box with no size prop available.
   - Wrap it in a `~1em`-sized container next to the "Anant's Hub" text (currently text-sm) and scale the inner fixed box down via CSS transform, rather than adding a new size prop to HeaderLogo/HeaderLogoCanvas/HeaderLogoFallback — those three files have no other caller today, so a prop plumbed through all of them for a single call site is unnecessary; do this with a wrapper + CSS transform in Footer.tsx only.
   - Do not change HeaderLogo.tsx's public API (it currently takes only `show: boolean`).

CONSTRAINTS:
- Do not touch HeaderScrolling.tsx, SidebarToggle.tsx, or PortfolioLab.tsx.
- Do not touch HeaderLogoCanvas.tsx, useAnimationGate.ts, or liquidMetalMaterial.ts.
- Do not add a size prop to HeaderLogo/HeaderLogoCanvas/HeaderLogoFallback for this task — solve the footer sizing locally in Footer.tsx.
- Do not touch icon.svg's gradient/color values — only its path data, to match the regenerated glyph.
- No new dependencies.

VERIFY before reporting done, and state the result of each explicitly:
(a) Screenshot or describe the new glyph shape next to the old one — visibly thinner/more cursive, same overall structure.
(b) Footer glyph now reads as roughly the same height as "Anant's Hub" text, not a large fixed box.
(c) Favicon in a browser tab still matches the in-page glyph.
(d) Header and Lab panel render unchanged (no logo appeared there, none was expected to).
Run pnpm typecheck && pnpm lint and paste the output. Do not deploy, do not commit.
```

## Dependencies

- Task 6.2 (footer sizing) does not depend on Task 6.1 (glyph shape) — they can run in either order or in parallel; the old "6.2 depends on 6.1" note was about matching a new visual, not a code dependency.

## Risks

- SVG path edit breaks fill rule (compound path uses nonzero winding) — verify the regenerated path renders solid, not with unexpected holes.
- `icon.svg` is manually synced (per its own comment) — a mismatch between it and `logoGlyphPath.ts` after this edit is a real regression risk; diff them explicitly before calling this done.
