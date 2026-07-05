---
name: portfolio-content-cms
description: Guides content and CMS changes for this portfolio. Use when editing Sanity schemas, queries, types, or content-driven components (profile, projects, experience, skills, navigation, footer).
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Cursor/Portfolio/Setup]]"
---

# Portfolio content and CMS

## Purpose

Keep CMS-backed changes consistent with existing Sanity schemas, queries, and generated types. Do not invent fields or content contracts.

## Use this skill when

- Editing schema files in `src/sanity/schemaTypes/`
- Editing `src/sanity/lib/queries.ts`
- Changing rendered content that depends on Sanity data
- Wiring footer/contact/profile content
- Changing site settings usage

## Instructions

- Use existing queries in `src/sanity/lib/queries.ts` and types from `src/sanity/types`. Do not add new schema fields or query fields without listing affected files first.
- Do not invent schema fields, query fields, slugs, references, or content contracts.
- Before expanding a schema or query, list the affected files and UI consumers.
- Prefer reusing existing content sources before introducing new ones.
- For footer/contact, prefer profile `email` and `socialLinks` (already in PROFILE_QUERY) or existing `contact`/`siteSettings` schemas if extending usage.
- Keep types aligned with query usage. Preserve optional-field safety in UI rendering.

## Relevant files

- `src/sanity/lib/queries.ts`
- `src/sanity/types/`
- Schema files for profile, projects, experience, skills, site settings in `src/sanity/schemaTypes/`
- Content-driven sections and Footer component
