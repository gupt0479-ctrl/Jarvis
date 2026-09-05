---
type: concept
status: active
updated: 2026-09-05
tags: [portfolio, frontend, ui-fixes, about, telemetry]
notes:
  - "[[UI Fixes]]"
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-design]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[frontend-ui-fixes-index]]"
  - "[[ui-fix-02-about-section]]"
---

# UI Fix 03 — About Telemetry (2 Cards, Glow Only)

> **Status:** open — **SUPERSEDES July 4-card accordion spec**
> **Ledger:** [[UI Fixes]] §2 | **Task:** 3.3
> **2026-09-05 verification pass:** re-checked against `src/components/AboutTelemetry.tsx` and `src/sanity/schemaTypes/profile.ts` on `post-frontend`. This note was accurate — every line number and symbol below matched the live file. Only additions: the exact removal list and one existing-convention note worth preserving.

## Purpose

Replace expandable stat cards with **two Sanity-editable KPI cards** that respond to click with a **subtle whole-card glow only** — no dropdown, no graph, no layout shift.

## Current code (re-verified 2026-09-05 — accurate)

| File | Confirmed current behavior |
|---|---|
| `src/components/AboutTelemetry.tsx` (164 lines) | Renders up to **4** cards: `(stats ?? []).filter(...).slice(0, 4)` at line 135. |
| `TelemetryCard` (same file, lines 54–120) | `<button aria-expanded={isOpen}>` at lines 72–116 toggles an `AnimatePresence` accordion (lines 98–115) revealing `<TelemetryDetail>`. |
| `src/components/TelemetryDetail.tsx` | Exists, imported at line 6, renders the mini graph + summary on expand. |
| `AboutSectionClient.tsx` | Passes `skills` and `projects` into `AboutTelemetry`, used **only** to derive `graphPoints` (`skillPercentagePoints` / `projectCategoryCounts`, lines 28–41) — confirmed not used for anything else in this file, so they're safe to drop once the graph goes. |
| `src/sanity/schemaTypes/profile.ts` | `stats[]` array starts at line 159: `label` (required), `value` (required), `summary` (optional). **No `order` field** — confirmed. |

**Existing convention worth preserving (comment at lines 10–12 of `AboutTelemetry.tsx`):** *"Icons are picked by index from this ring — no keyword matching, no canonical fixed slots, no hardcoded fallbacks."* `STAT_ICONS[i % STAT_ICONS.length]` already implements this. Keep that pattern for the 2-card version — don't introduce label-matching logic to pick icons.

**July spec (superseded):** click → expand → `TelemetryDetail` graph. **Do not implement or preserve this.**

## Target cards (exact content — Sanity authoring, not code)

| Card | Value | Label | Icon (by index, per existing convention) |
|---|---|---|---|
| 1 | `Ongoing always (5+)` | Side Quests | `STAT_ICONS[0]` (`Layers`) |
| 2 | `100%` | Eager to Learn | `STAT_ICONS[1]` (`Cpu`) |

**Remove from UI:** any other stats entries ("Coding Experience", "Technologies Mastered", or whatever else is currently authored beyond these 2) — this is a `.slice(0, 2)` change in code plus a Studio content cleanup, not a code-only fix.

## Sanity schema (confirmed, no change needed)

`profile.stats[]` in `profile.ts` (line 159 onward): `label` (string, required), `value` (string, required), `summary` (string, optional — **no longer displayed**, fine to leave unused in schema, do not delete the field itself).

**Decision needed before coding (pick one, don't leave ambiguous in the diff):** add an `order` field to the schema, or just hardcode `.slice(0, 2)` and rely on Studio-side content cleanup to keep only 2 entries. Given no `order` field exists today and adding one is a schema migration, default to `.slice(0, 2)` unless the review explicitly asks for `order`.

## Target behavior

### Render
- Grid: `grid-cols-2 gap-4` (2 cards only) — same grid class already in use at line 143, just fed fewer items.
- Each card: keep `CometCard variant="subtle"` wrapper, value + label + the existing static sparkline bars (`SPARKLINE_BARS`, lines 16–22) — no change needed there.
- Icons: `STAT_ICONS[0]` and `STAT_ICONS[1]` only, via the existing index-based selection.

### Click interaction (replaces the accordion)
```tsx
const [glowingIndex, setGlowingIndex] = useState<number | null>(null);

const handleClick = (i: number) => {
  setGlowingIndex(i);
  setTimeout(() => setGlowingIndex(null), 500); // 300–600ms
};
```

Glow styling (apply conditionally, not via a new component):
```
ring-2 ring-violet-400/50
shadow-[0_0_24px_rgba(167,139,250,0.35)]
transition-all duration-500 ease-out
```

- **No** `AnimatePresence` expand, **no** height change, **no** `TelemetryDetail` render.
- Replace `aria-expanded` accordion semantics with `aria-pressed` during the glow window, or omit ARIA state entirely and treat it as a decorative visual-only interaction (glow doesn't change page semantics or content).

### Props cleanup
- Remove `skills`, `projects` props and the `skillPercentagePoints`/`projectCategoryCounts` functions from `AboutTelemetry.tsx` — confirmed unused once the graph is gone.
- Remove the `TelemetryDetail` import and its usage.
- Update the `AboutSectionClient.tsx` call site (currently passes `skills={skills} projects={projects}`, lines ~161–162) to drop those two props — but check whether `AboutSectionClient` still needs `skills`/`projects` for anything else in that file before deleting its own props/fetch; if not used elsewhere, remove them there too rather than leaving dead props threaded through.

## Visual reference

- Current: 4-card grid, accordion-expand-to-graph. Target: 2-card row, glow-only, sitting under the summary during the About pin (see [[ui-fix-02-about-section]] Beat 1).

## Files to modify

1. `src/components/AboutTelemetry.tsx` — primary rewrite (drop accordion state, drop graph derivation, add glow state)
2. `src/components/sections/AboutSectionClient.tsx` — drop `skills`/`projects` pass-through if unused elsewhere in that file
3. `src/components/TelemetryDetail.tsx` — leave on disk but unreferenced (delete in a separate cleanup pass, not this task — don't delete files as a side effect of an unrelated task)

## Do NOT

- Implement any accordion / mutually-exclusive expand behavior.
- Derive graphs from `SKILLS_QUERY` / `PROJECTS_QUERY` data.
- Show `stats[].summary` text anywhere.
- Add label-based/keyword-matching icon selection — keep the existing index-based convention.
- Delete `TelemetryDetail.tsx` as part of this task.

## Accessibility

- Cards remain `<button type="button">` for keyboard access.
- Glow is visual-only feedback; either use `aria-pressed` briefly or treat as purely decorative — don't leave a stale `aria-expanded` on an element that no longer expands anything.
- Sparkline bars stay decorative (no `role="img"` needed, no data claim being made).

## Acceptance criteria

- [ ] Exactly 2 cards render
- [ ] Values/labels editable from Sanity `profile.stats[]`
- [ ] Click → glow 300–600ms, zero height/layout change
- [ ] `TelemetryDetail` no longer rendered in the DOM
- [ ] `skills`/`projects` props removed from `AboutTelemetry` (unless still needed elsewhere)
- [ ] Layout stable at 375px
- [ ] `pnpm typecheck && pnpm lint` pass

## Implementation prompt

> Single autonomous session (Claude Sonnet 5 in Cursor). Front-loaded so no follow-up turn is needed.

```
Read ui-fix-03-about-telemetry.md in full first. This supersedes the July 4-card accordion spec — do not implement expand/graph behavior even if you find references to it elsewhere (e.g. an older prompt in frontend-ui-fixes-tasks.md).

Confirmed facts (verified against the live file, don't re-derive): src/components/AboutTelemetry.tsx currently slices to 4 stats (line 135) and each TelemetryCard is a button with aria-expanded that reveals TelemetryDetail via AnimatePresence (lines 72–116). skills/projects props exist only to build graphPoints for that graph (lines 28–41) — nothing else in the file uses them. The icon-selection convention is explicitly index-based (STAT_ICONS[i % STAT_ICONS.length], comment at lines 10–12) — preserve this, do not switch to label matching.

TASK:
1. In AboutTelemetry.tsx: change the slice from 4 to 2. Remove expandedIndex state, the AnimatePresence/TelemetryDetail block, the TelemetryDetail import, skillPercentagePoints, projectCategoryCounts, and the skills/projects props and their SKILLS_QUERYResult/PROJECTS_QUERYResult type imports.
2. Add glowingIndex state. On card click, set it and clear it via setTimeout after 500ms. Apply ring-2 ring-violet-400/50 and shadow-[0_0_24px_rgba(167,139,250,0.35)] (transition-all duration-500 ease-out) conditionally when a card's index matches glowingIndex. Do not add any height-changing content.
3. Update the button's ARIA: remove aria-expanded (nothing expands anymore); either add aria-pressed tied to the glow state or omit ARIA state entirely if you judge it purely decorative — pick one and be consistent.
4. In AboutSectionClient.tsx: remove the skills/projects props passed to AboutTelemetry. If skills/projects are not used for anything else in that file after this change, remove them from that file's own props/fetch too rather than leaving dead code — check first, don't assume.
5. Leave TelemetryDetail.tsx on disk, unreferenced. Do not delete the file in this task.

CONSTRAINTS:
- Do not touch the pin/scroll work in ui-fix-02-about-section.md — that's a separate task.
- Keep the existing grid-cols-2 gap-4 grid class and the existing SPARKLINE_BARS rendering unchanged.
- Do not add a new component file for the glow — it's a small conditional className change on the existing TelemetryCard.

VERIFY and report each explicitly:
(a) Exactly 2 cards render, values/labels reflect Sanity content.
(b) Clicking a card produces a visible glow for ~300–600ms with zero layout shift (screenshot or measured height before/after).
(c) TelemetryDetail is not imported or rendered anywhere in AboutTelemetry.tsx.
(d) No unused-import or unused-prop lint warnings for skills/projects/TelemetryDetail-related code.
Run pnpm typecheck && pnpm lint and paste the output. Do not deploy, do not commit.
```

## Dependencies

- Task 1.1 (Sanity: exactly 2 stats authored in Studio)
- Runs alongside [[ui-fix-02-about-section]] pin work — the 2-card grid renders inside that pin's Beat 1, but this is a separable code change and can land independently.

## Migration note

Studio: delete or unpublish extra `stats[]` entries beyond the 2 target ones so the `.slice(0, 2)` isn't silently hiding authored content someone expects to see.
