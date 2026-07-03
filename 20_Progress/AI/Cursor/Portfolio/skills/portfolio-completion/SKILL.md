---
name: portfolio-completion
description: Checklist and wiring for finishing this portfolio. Use when completing the site, adding missing sections, or fixing known gaps.
---

# Portfolio completion

## Purpose

Checklist of known gaps and section wiring so "finish the portfolio" is actionable. Use when completing the site or fixing known gaps.

## Completion checklist

1. **Contact anchor** — Add `id="contact"` to the footer/contact block so the nav "Contact" link scrolls correctly.
2. **Footer content** — Wire Footer email and social links from profile (PROFILE_QUERY) or a single source of truth; remove hardcoded placeholders (e.g. anant@example.com, placeholder social URLs).
3. **About section** — Integrate AboutSection into PortfolioContent (e.g. after Hero or before Projects) or remove the component if not needed.
4. **Layout cleanup** — Remove duplicate SidebarInset in root layout (`src/app/layout.tsx`); keep one.
5. **Site settings (optional)** — Optionally use SITE_SETTINGS_QUERY for metadata, footer text, or section subtitles.

## Section order

Hero → [About] → Projects → Experience → Skills → Footer.

## After making changes

- Run lint, typecheck, and build.
- Summarize what changed by file.
- Suggest manual QA for nav scrolling, contact scroll target, footer links, and responsive behavior.

## Audit (before code changes)

When auditing what is left to finish:

- Identify which checklist items are already solved and which remain open.
- For each open item, name the likely files involved (e.g. PortfolioContent, Footer, layout.tsx, AboutSection).
- Prefer existing content sources and existing components.
- After proposing fixes, recommend verification steps for navigation, footer links, responsive layout, and build health.

## Relevant files

- `src/components/PortfolioContent.tsx`
- `src/components/Footer.tsx`
- `src/app/layout.tsx`
- `src/components/sections/AboutSection.tsx`
