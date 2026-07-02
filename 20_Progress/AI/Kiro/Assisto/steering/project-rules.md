---
inclusion: auto
---

# Assisto Website — Project Rules

## Repository Layout

- **Landing page** (`src/app/page.js`, `src/components/*`): Static marketing site. Strapi CMS is gone permanently. Do not add API fetches to external services.
- **Assisto Spend** (future `src/app/(spend)/spend/...`): Enterprise spend workflow module. All new product work goes here.
- **Docs**: `docs/assisto-spend/` (canonical build plans), `docs/assisto-spend/agent-build/` (compact contracts), `docs/research/` (background only).
- **Agent context**: `.agent/` (Codex legacy context, still valid reference), `.kiro/` (active Kiro workspace).

## Git Conventions

- **Primary remote**: `origin` → GitHub (`gupta-builds/assisto-website`, private)
- **Backup remote**: `azure` → Azure DevOps (legacy, read-only reference)
- **Main working branch**: `Anant`
- **Feature branches**: `feature/<name>` off `Anant`
- **Spend implementation**: `feature/assisto-spend-<phase>` per build plan
- Never force-push `Anant` without explicit approval.
- Keep PRs small and phase-scoped per `docs/assisto-spend/agent-build/`.

## Tech Stack

- Next.js 15 App Router, React 19, Tailwind CSS 4, JavaScript (landing), TypeScript (spend module)
- Supabase Postgres + Storage (partially configured, NOT implementation-ready until migration recovery)
- Validation: Zod (after dependency phase)
- No Strapi, no external CMS, no Lovable code

## Protected Paths (Do Not Edit Unless Explicitly Scoped)

- `src/app/page.js`, `src/app/layout.js`, `src/app/globals.css`
- Existing `src/components/**`
- `public/**`
- `package.json`, lockfiles, config files (outside dependency phase)
- `supabase/**` (outside approved database phase)
- `.env*` values (never print, never commit)

## Safety Rules

- Do not commit `.env` files or secrets.
- Do not modify landing page files during spend work unless explicitly scoped.
- Do not add files > 90 MB to git (use `.gitignore` or LFS).
- `*:Zone.Identifier` files are ignored via `.gitignore`.
- Backend correctness before UI polish.
- No product code until specs are approved.

## Build & Run

- `npm run dev` — local dev server (turbopack)
- `npm run build` — production build (must pass before push)
- `npm run lint` — next lint (verify compatibility before relying on it)
- Landing page must render without errors even with no backend.

## Read Order for Assisto-Spend Work

1. `AGENTS.md`
2. `.kiro/steering/` (auto-included)
3. `.kiro/specs/assisto-spend-backend/` (active spec)
4. Relevant canonical docs under `docs/assisto-spend/`
5. Relevant contracts under `docs/assisto-spend/agent-build/`
