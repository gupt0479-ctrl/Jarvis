---
name: portfolio-ui-polish
description: Guides UI, layout, and animation for this portfolio. Use when changing styling, sections, 3D background, sidebar, or accessibility.
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Cursor/Portfolio/Setup]]"
---

# Portfolio UI and polish

## Purpose

Keep the portfolio polished, readable, responsive, and visually restrained. Effects must not overpower text or calls to action.

## Use this skill when

- Adjusting layout or spacing
- Editing hero, projects, experience, skills, footer, or sidebar UI
- Modifying 3D/background effects (e.g. ObsidianBackground)
- Tuning motion or responsive behavior
- Improving accessibility or interaction polish

## Instructions

- Use Tailwind and shadcn only. Do not introduce separate CSS files unless the project already uses them.
- Preserve visual hierarchy, contrast, spacing, and readability first.
- Effects, gradients, motion, and 3D visuals must not overpower text or CTAs. See `src/components/three/ObsidianBackground.tsx` for the 3D background.
- Prefer small parameter changes and local component edits over broad redesigns.
- Reuse existing section patterns and shared UI in `src/components/ui/` and section components (e.g. PortfolioContent, HeroContent).
- Preserve mobile usability: `use-mobile` hook uses 768px breakpoint; follow existing `sm:/md:/lg:` patterns.
- Add or maintain semantic HTML, aria labels, focus behavior, and keyboard interaction where relevant. Keep animation restrained and purposeful.

## Relevant files

- Section components in `src/components/sections/`
- Shared UI in `src/components/ui/`
- `src/components/three/ObsidianBackground.tsx` and related visual components
- Layout and sidebar components
- `src/app/globals.css` for theme variables and keyframes
