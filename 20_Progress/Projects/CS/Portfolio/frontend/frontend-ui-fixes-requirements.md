---
type: concept
status: active
created: 2026-07-11
updated: 2026-09-05
tags:
  - portfolio
  - frontend
  - ui-fixes
  - requirements
notes:
  - "[[frontend-ui-fixes-design]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[UI Fixes]]"
  - "[[BUILD-STATUS]]"
---

# Frontend UI Fixes — Requirements

> **Updated:** 2026-09-05 from localhost walkthrough + screenshots.
> Human ground truth: [[UI Fixes]] § Current Localhost Walkthrough.
> Companion docs: [[frontend-ui-fixes-design]], [[frontend-ui-fixes-tasks]].
> Every file path below was verified against the live repo on branch with liquid-glass + GSAP additions.

## Document History

| Date | Change |
|---|---|
| 2026-07-11 | Initial requirements from dictated notes |
| 2026-09-05 | **Major revision** — pinned GSAP sections, 2-card glow telemetry, 3D volumetric scatter, education spring/rope, logo/footer, Lab input centering. Supersedes July telemetry accordion + education-only stagger |

## Glossary

| Term | Meaning |
|---|---|
| Pin / lock-screen | GSAP ScrollTrigger pins a section for one viewport while scroll drives internal animation |
| Volumetric scatter | R3F particles displace in XYZ depth, not a flat 2D ripple |
| Glow-only card | Click triggers whole-card border/shadow glow — no expand, no graph |
| Blast radius | Sphere click hit area in `ObsidianBackgroundCanvas.tsx` (`PLANET_RADIUS * 1.1`) |
| Rope connector | Education path rendered as flexible bent curve, not rigid straight line |

---

## Executive Summary

The portfolio's next UI pass elevates **scroll choreography** over incremental polish. Three sections (About, Projects, Education) get **pinned cinematic moments** driven by GSAP ScrollTrigger, synchronized with the existing R3F background. The hero sphere click becomes truly **3D volumetric**. About telemetry shrinks from 4 expandable cards to **2 Sanity-editable glow cards**. Logo/tab/footer branding is unified. Portfolio Lab input text must **vertically center** when short.

July-era fixes (terminal removal, scatter-intro, line-clamps, skills graph, Orby, dark mode, deploy sync) remain valid where not superseded — see Fix Area 9.

---

## Fix Area 0 — Pre-Flight: Deployment Sync

**Status:** open

Compare local `git rev-parse HEAD` against latest production deployment SHA. Record: in-sync / out-of-sync / unable-to-verify. If out-of-sync, flag as blocking prerequisite.

---

## Fix Area 1 — Hero & Background Particle System

**Components:** `HeroContent.tsx`, `ProfileImage.tsx`, `ObsidianBackgroundCanvas.tsx`, `PortfolioContent.tsx`

### Problem (Sep 2026)
1. Sphere click effect reads **2D** despite 3D particle background — needs **volumetric scatter/reform** (particles fly outward in depth, then reconnect).
2. Profile image was fixed from moving but must remain **fully static** after entrance — zero ambient drift.
3. Profile card hover overlay (Open Portfolio Lab / Close tab) has visible gap on **left and bottom borders** — must cover entire image.
4. Load-in scatter exists (partial) but lacks convincing depth; click scatter should share visual language.

### Success Criteria
- Click inside blast radius triggers XYZ scatter with depth-based scale/opacity falloff, then spring reform to rest positions.
- Profile image: no motion after mount; comet sweep (if kept) is one-shot only.
- Hover overlay covers 100% of image bounds including rounded corners.
- `prefers-reduced-motion`: sphere renders formed, click scatter skipped.

### Content Dependencies
None.

---

## Fix Area 2 — About Section (Pinned Scroll + Summary + 2 Cards)

**Components:** `AboutSection.tsx`, `AboutSectionClient.tsx`, `AboutTelemetry.tsx`, `ObsidianBackgroundCanvas.tsx`

### Problem (Sep 2026)
1. About has no **pinned scroll moment** — user scrolls through prose without a cinematic pause.
2. Bio expands only via "Read full bio" button — must expand on **click anywhere** on card/description.
3. Four telemetry cards exist; only **two** should remain.
4. July spec required click-to-expand graphs — **SUPERSEDED**. Cards should **glow only**.

### Success Criteria
- ScrollTrigger **pins About for ~1 viewport** after leaving hero.
- **Beat 1:** Short summary + 2 stat cards visible.
- **Beat 2:** Summary transforms (scroll-driven) to next summary state.
- During pin: background runs **mesmerizing scatter/reform** (stronger than hero click — attention hook).
- Only 2 cards render: **"Ongoing always (5+)" / Side Quests** and **"100%" / Eager to Learn**.
- Both cards: label + value editable via Sanity `profile.stats[]`.
- Card click: subtle whole-card glow (~300–600ms ease), **no dropdown, no graph, no accordion**.
- Bio expand: entire About card/description area is clickable (button remains but is not sole trigger).
- Collapsed About fits ~1 viewport including 2 cards.

### Content Dependencies
- `profile.aboutSummary` (short summary for Beat 1) — schema may exist; verify + populate.
- `profile.stats[]`: ensure exactly 2 entries authored in Studio OR filter/limit in query to first 2 by order.
- Optional: second summary field for Beat 2 transform — or derive from Portable Text block.

### Accessibility
- Pin must not trap focus; reduced-motion: skip pin, show static layout.
- Glow cards: `<button>` or `role="button"` with `aria-pressed` during glow state.

---

## Fix Area 3 — About Telemetry (2 Cards, Glow Only) — SUPERSEDES July Fix Area 3

**Components:** `AboutTelemetry.tsx`

> **July Fix Area 3 (4-card accordion + mini-graph) is explicitly superseded. Do not implement.**

### Success Criteria
- Render 2-card grid (1×2 on mobile, 2×1 or 2×2 depending on layout — design doc decides).
- Remove `TelemetryDetail.tsx` usage if present.
- Click → CSS/Framer glow on `.cosmic-card` border + shadow; no height change.
- Sanity-editable `label` and `value` per card.

---

## Fix Area 4 — Portfolio Lab Chat Input

**Components:** `ChatInputBar.tsx`, `ChatThread.tsx`, `PortfolioLab.tsx`, `sidebar.tsx`

### Problem (Sep 2026)
1. **Text vertical alignment:** Typed text sits at bottom of input card; must be **vertically centered** when 1 line, top-aligned as textarea grows to 3-line cap.
2. Growable textarea (July) — verify built state.
3. Mobile send button overflow — still needs repro at 320/375/390px.
4. Chat bubble `break-words` for long tokens.

### Success Criteria
- Empty/short input: text vertically centered, left-aligned.
- At 3-line cap: internal scroll, text top-aligned within textarea.
- Enter submits, Shift+Enter newline.
- Character indicator near cap (if not already shipped).
- Mobile: send button fully visible without horizontal scroll/zoom.

---

## Fix Area 5 — Experience Section (Line Clamp)

**Status:** unchanged from July — UI perfect; add line-clamp on collapsed bullets. Content quality out of scope.

**Components:** `ExperienceCard.tsx`

---

## Fix Area 6 — Projects Section (Pinned Cinematic Lock)

**Components:** `ProjectsSlider.tsx`, Projects section wrapper, `ObsidianBackgroundCanvas.tsx`

### Problem (Sep 2026)
July spec focused on auto-play indices 0–2. Sep adds **pinned cinematic section**:
1. Section pins on scroll entry.
2. **Edge/border background effect** — soothing recurring animation on screen periphery during auto-scroll (distinct from About center scatter).
3. Three cards **emerge** from fully translucent → opaque 3D-feeling cards (appear in space, not slide).
4. Side cards drift subtly within bounded region while center card is active.
5. Auto-play first 3 projects still valid; manual nav to all 9 preserved.

### Success Criteria
- ScrollTrigger pin on `#projects` (or equivalent).
- On pin start: cards animate opacity + subtle scale/depth from "in screen" to solid.
- Border effect loops gently during auto-play; pauses on interaction.
- Side cards: constrained parallax/drift (design doc defines bounds).
- `prefers-reduced-motion`: static cards, no auto-play, no pin animation.
- Chat slug navigation remains reliable.

### Open Design Items
- Exact border effect visual (color, speed, shape) — needs mood reference.
- Document's role in card effects — brainstorm in design doc.

---

## Fix Area 7 — Skills & Spacing

**Status:** largely unchanged from July.

- Graph starts 2022, first point ≤ 35.
- Reduce SkillPill + CategoryPill effect variety.
- Tighten Skills↔Education↔Certifications padding.

**Components:** `SkillsCapabilityGraph.tsx`, `SkillsSectionClient.tsx`, `globals.css`, `EducationSection.tsx`

---

## Fix Area 7b — Education (Pinned Spring + Rope + Dot-Sync Deform)

**Components:** `EducationSection.tsx`, `EducationFlowchart.tsx`

### Problem (Sep 2026)
July spec: stagger deform on section entry. **Sep supersedes** with fuller choreography:
1. Section **pins one viewport** on entry.
2. **Spring bounce entry:** Bachelor's bounces up first, then High School, then Middle School.
3. Connectors become **rope** (flexible, bent) not rigid straight lines.
4. Travelling dot delayed **+0.5s** at loop start.
5. Bachelor's deformity **tracks dot**: rigid at rest → gradually deforms as dot leaves → peaks at Middle School level → subtly returns to rigid before dot restarts.
6. Header padding reduced — currently obscures Bachelor's sphere.

### Success Criteria
- Pin + spring sequence plays once per visit (or per scroll-into-view, design decides).
- `MeshDistortMaterial.distort` on Bachelor's blob lerps with dot position along path — not instant snap.
- Rope: quadratic/cubic bezier or physics-based sag between blob centers.
- Header: `section-pad-top-tight` or custom override so sphere clears title block.
- `prefers-reduced-motion`: static layout, final distort values, no spring.

---

## Fix Area 8 — Logo, Footer, Branding

**Components:** Header logo, Lab tab logo, `Footer.tsx`

### Success Criteria
- **No glow difference** between tab open vs closed — same logo rendering both states.
- **A thinner, more cursive** within existing logo system (structure + alignment preserved).
- Footer: fixed logo glyph **leftmost**, left of "Anant's Hub", matching footer text size.

---

## Fix Area 9 — Carry-Forward (July, Still Valid)

| Item | Components | Notes |
|---|---|---|
| HeroTerminal removed | `PortfolioContent.tsx` | Done in code — verify |
| Scatter-intro on load | `ObsidianBackgroundCanvas.tsx` | Partial — deepen 3D |
| Dark mode toggle + light tokens | `HeaderScrolling.tsx`, `globals.css` | Partial |
| Orby radio/wave/idle/walking | `OrbyModel.tsx`, `Orby.tsx` | Partial |
| Footer polish (beyond logo) | `Footer.tsx` | Open |
| CSP enforcement | `next.config.ts` | Verify shipped |

---

## Superseded Requirements (Do Not Implement)

| ID | July requirement | Replaced by |
|---|---|---|
| FIX-3-accordion | 4 telemetry cards, click expand graph | Fix Area 3 glow-only 2 cards |
| FIX-7b-entry-only | Deform stagger on scroll-into-view only | Fix 7b dot-sync + spring pin |
| FIX-6-autoplay-only | Projects auto-play without pin | Fix Area 6 pinned cinematic |

---

## Open Questions

1. About pin: 2 beats or 3 (include full bio reveal inside pin)?
2. Projects border effect visual reference?
3. Education rope: SVG path vs R3F tube geometry vs GSAP morph?
4. Logo source file path for A refinement?
5. Orby speech bubble vertical centering (Contact section) — in or out of scope?
6. GSAP ScrollSmoother vs native scroll + ScrollTrigger pin — research prerequisite (Phase 3).

---

## Verification Commands (for implementation phase)

```bash
pnpm typegen && pnpm typecheck && pnpm lint && pnpm test && pnpm build
```

Manual QA: 320px, 375px, 768px, 1280px, 1440px; `prefers-reduced-motion: reduce`; scroll through About → Projects → Education pin sequence.

---

## Component spec cross-reference

> **Detailed per-component notes:** [[frontend-ui-fixes-index]]

| Fix Area | Component spec | Primary files |
|---|---|---|
| 0 Deploy sync | [[ui-fix-08-carry-forward]] §0.1 | — |
| 1 Hero / background | [[ui-fix-01-hero-background]] | `ObsidianBackgroundCanvas.tsx`, `HeroContent.tsx` |
| 2 About pin + summary | [[ui-fix-02-about-section]] | `AboutSectionClient.tsx`, `about-pin.ts` |
| 3 Telemetry 2-card glow | [[ui-fix-03-about-telemetry]] | `AboutTelemetry.tsx` |
| 4 Lab input | [[ui-fix-07-portfolio-lab]] | `ChatInputBar.tsx` |
| 5 Experience clamp | [[ui-fix-08-carry-forward]] | `ExperienceCard.tsx` |
| 6 Projects pin | [[ui-fix-04-projects-section]] | `ProjectsSlider.tsx` |
| 7 Skills / spacing | [[ui-fix-08-carry-forward]] | `SkillsCapabilityGraph.tsx` |
| 7b Education | [[ui-fix-05-education-section]] | `EducationFlowchart.tsx` |
| 8 Logo / footer | [[ui-fix-06-logo-footer]] | `logoGlyphPath.ts`, `Footer.tsx` |
| 9 Carry-forward | [[ui-fix-08-carry-forward]] | Orby, dark mode, CSP |
