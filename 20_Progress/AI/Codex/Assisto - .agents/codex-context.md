# Codex Context

## Repo Snapshot

- Repo: `gupta-builds/assisto-website`
- Current branch observed during setup planning: `feature/assisto-spend-docs`
- Primary remote: `origin` on GitHub
- Backup remote: `azure` on Azure DevOps
- Current app: marketing landing page
- Planned product: Assisto-Spend internal workflow module under `/spend`

## Stack

- Next.js `15.4.4`
- React `19`
- App Router under `src/app`
- Landing page uses JavaScript
- Tailwind CSS 4, CSS modules, Framer Motion, lucide/react-icons
- `shadcn-ui` CLI dependency exists, but no local shadcn component system is verified

## Current App Shape

Current visible app files include:

- `src/app/page.js`
- `src/app/layout.js`
- `src/app/globals.css`
- existing marketing components under `src/components/**`
- assets under `public/**`

These are protected during Assisto-Spend work unless explicitly scoped.

## Known Env Names

Env file names exist: `.env`, `.env.local`.

Known variable names only:

- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`
- `NEXT_PUBLIC_API_BASE_URL`

Never print, copy, summarize, or commit env values.

## Supabase State

- Local config: `supabase/config.toml`
- Linked project ref: `tmhsadkglxbhbffsnokh`
- Project name: `Assisto`
- Region: `ap-northeast-1`
- Postgres: 17
- Remote schema: 28 public RLS-enabled tables reported in active docs
- Remote migrations: 4 reported in active docs
- Local `supabase/migrations/`: absent during planning
- Generated DB types: absent
- App Supabase helpers: absent
- Auth middleware: absent
- `auth.users`: empty in active docs
- `public.users`: demo users in active docs
- Storage: exists remotely; bucket name/privacy/policies still need audit

Backend verdict: remote DB is usable after review and local migration recovery, but not production-ready.

## Backend-First Gate

Before deep implementation:

1. Freeze/read-only snapshot remote state.
2. Decide migration source recovery or reviewed rebuild.
3. Review schema, enums, indexes, triggers, policies, and storage.
4. Define auth mapping and service-role boundary.
5. Define RLS and server guard strategy.
6. Define workflow/audit enforcement.
7. Define storage/OCR backend flow.
8. Separate deterministic demo data from production data.
9. Plan report queries, CSV allow-lists, and indexes.

Stop if a task requires backend writes or schema work while migration source-of-truth drift is unresolved.

## Codex Lane

Kiro owns backend-heavy execution unless the user explicitly reassigns it. Codex owns:

- independent review of Kiro backend output
- schema/security/workflow gap detection
- docs/spec alignment
- UI route/component implementation after backend contracts are stable
- tests, QA, demo validation, and final integration review

Codex does not own remote Supabase mutation, migration recovery, RLS implementation, backend workflow engine implementation, storage bucket policy changes, or backend source-of-truth decisions by default.

## Dirty Worktree Warning

The repo may contain unrelated existing changes, including component moves and active docs edits. Do not revert or restage unrelated changes.
