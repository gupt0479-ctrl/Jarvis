---
type: concept
status: active
updated: 2026-09-05
tags: [portfolio, frontend, ui-fixes, carry-forward, skills, orby, dark-mode]
notes:
  - "[[UI Fixes]]"
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[frontend-ui-fixes-index]]"
---

# UI Fix 08 — Carry-Forward (July Items Still Valid)

> **Status:** mixed partial/open
> **Ledger:** [[UI Fixes]] §7 | **Tasks:** Phase 7 + 0.1, 8.1

Items from July 2026 walkthrough **not superseded** by Sep pinned-section work. Implement after or parallel to core component fixes.

---

## 0.1 Deploy sync verification

**Status:** open

Compare `git rev-parse HEAD` vs production Vercel deployment SHA.
Record: in-sync | out-of-sync | unable-to-verify.
**Block all UI work if out-of-sync** without explicit flag.

---

## Experience — line clamp

**Files:** `ExperienceCard.tsx`
**Status:** partial

- UI "perfect" per user; content quality out of scope.
- Add `line-clamp-2` (mobile) / `line-clamp-3` (desktop) on collapsed bullet text spans.
- Expanded Portable Text description: max-height + internal scroll for extreme entries.
- Pattern: clamp inner `<span>`, not parent `<li>` with bullet glyph.

**Task ref:** July 2.x / Phase 7 if not done

---

## Skills — graph + pills + spacing

**Files:** `SkillsCapabilityGraph.tsx`, `SkillsSectionClient.tsx`, `globals.css`, `EducationSection.tsx`, `CertificationsSection.tsx`

| Item | Target |
|---|---|
| Graph years | Start **2022** (shift to 2022–2027, 6 points) |
| 35 cap | `values[0] = Math.min(values[0], 35)` in `buildCurveValues` |
| SkillPill effects | Reduce from 7 → **3** cohesive effects (ring pulse, gradient wash, 3D tilt) |
| CategoryPill effects | Reduce 9+ variants → **2–3**; keep `useSpaceFloat` idle drift |
| Section padding | `section-pad-top-tight` / `section-pad-bottom-tight` on Education/Skills boundaries |

**Task ref:** 7.3 + July 3.7–3.9, 3.12

---

## Dark mode

**Files:** `HeaderScrolling.tsx`, `ThemeProvider.tsx`, `globals.css`

**Status:** partial — toggle may be wired but light tokens incomplete

- `useTheme()` + `setTheme` on header button.
- `:root:not(.dark)` companions for `.cosmic-card`, `.orbit-chip`, `.section-kicker`, `.float-btn`.
- **ObsidianBackgroundCanvas stays dark-only.**
- Full `text-white/*` audit — high risk; flag before shipping light mode.

**Task ref:** 7.4

---

## Orby companion

**Files:** `OrbyModel.tsx`, `Orby.tsx`, `useOrbyIdleCommentary.ts`, `api/orby-comment/route.ts`

| Item | Target |
|---|---|
| Radio prop | Antenna sub-element on radio mesh |
| Wave animation | Deeper arm raise (~-70°) |
| Idle commentary | AI flavor text via `/api/orby-comment`, 45s client cooldown |
| radio-talk pose | During roaming, alternate with idle |
| Walking pose | Leg lift synced to horizontal velocity |
| Ground anchor | Roaming `targetY` oscillates toward `bottomY` |

**Task ref:** 7.5

**Separate issue (open question):** Orby speech bubble text bottom-aligned on Contact — vertical center bubble text?

---

## Footer polish (beyond logo)

**File:** `Footer.tsx`
**Status:** partial — `useSpaceFloat` already on brand/copyright

- User wanted "more eye-pleasing" — optional gradient/iconography pass.
- Logo fix: [[ui-fix-06-logo-footer]]

---

## CSP enforcement

**File:** `next.config.ts`
**Status:** verify shipped (report-only vs enforce)

---

## Chat — break-words

**File:** `ChatThread.tsx`
**Task ref:** 7.2 (also in [[ui-fix-07-portfolio-lab]])

---

## Phase 8 verification gate

```bash
pnpm typegen && pnpm typecheck && pnpm lint && pnpm test && pnpm build
```

Manual QA checklist: see [[frontend-ui-fixes-tasks]] Task 8.1

Breakpoints: 320, 375, 768, 1280, 1440 + `prefers-reduced-motion: reduce`

---

## Implementation prompt (bundle)

```
Work through [[ui-fix-08-carry-forward]] items not yet done.
Prioritize: 7.2 break-words, 7.3 skills graph, 7.1 mobile repro.
Defer full light-mode text audit unless user requests.
Run Phase 8.1 gate before declaring pass complete.
```
