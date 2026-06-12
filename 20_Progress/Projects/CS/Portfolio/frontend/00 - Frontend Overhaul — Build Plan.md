---
type: project
status: active
created: 2026-06-12
updated: 2026-06-12
tags:
  - progress
  - portfolio
  - frontend
related_progress:
  - "[[Portfolio]]"
  - "[[00 - Nextgen Chatbot — Build Plan]]"
notes:
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[01 - Motion System & Comet Cards]]"
  - "[[02 - Sanity as Single Source of Truth]]"
  - "[[03 - Experience Section]]"
  - "[[04 - Projects Carousel]]"
  - "[[05 - Skills Capability Graph]]"
  - "[[06 - Education Flowchart]]"
  - "[[07 - Certifications & Achievements]]"
  - "[[08 - Blog, Contact & Footer]]"
  - "[[09 - Sanity Content Spec]]"
  - "[[11 - ObsidianBackground Enhancement]]"
  - "[[12 - Orby Friction Fixes]]"
  - "[[13 - Dark Mode Toggle]]"
next: "Phase 0 — real content + the two small schema touches (summary, education logo). See [[03 - Per-Phase Build Prompts]]."
---
# Frontend Overhaul — Build Plan
Spine note for the portfolio's **frontend** rebuild. Sibling of [[00 - Nextgen Chatbot — Build Plan]] (the AI agent) — same two-machine model, same "design in the vault, build in WSL" discipline. This note owns *what we are changing and why*; each section's *how* is its own note. The raw brief is `[[Portfolio]]` → "UI Enhancement" (items 1–24); these notes are the **decided** form.

> **READ FIRST: [[10 - Codebase Reality & Confusion Clearance]].** Claude Code (Sonnet 4.6) verified every claim against the live repo. It is the **codebase source of truth** and it corrected several assumptions the original notes made. Notes 01–09 have been reconciled to it (2026-06-12). When a note and note 10 disagree, **note 10 wins** — it read the actual files.

## The two theses (unchanged, but mechanism corrected by note 10)
1. **One motion language.** "In space / wiggles in its padding / comet-card" = **one new `useSpaceFloat` hook** + the **already-existing `CometCard`** (4 variants: default/dark/subtle/ghost) + **one extracted `SpaceRail`**. Not nine animations. See [[01 - Motion System & Comet Cards]].
2. **One data source.** Everything renders from Sanity. But the schema is **already rich and mostly correct** — `skill` has `category`/`proficiency`/`percentage`/`tone`, colour is **derived from `category`** (no `color` field, do not add one), there is **no `skillCategory` doc**, and the reference fields are **`technologies[]`** (experience/project) vs **`skills[]`** (certification) — *do not rename them*. See [[02 - Sanity as Single Source of Truth]]. Real content in [[09 - Sanity Content Spec]].

## Scope of this rebuild (updated with note 10's three added topics)
In scope: Experience, Projects carousel, Skills graph, Education flowchart, Certifications, Achievements, Blog, Contact, Footer, the motion + Sanity layers, **plus** the three components note 10 documented — [[11 - ObsidianBackground Enhancement]] (Bloom/additive/chromatic polish), [[13 - Dark Mode Toggle]] (make the dead pill a real dark-only button), and [[12 - Orby Friction Fixes]] (speech-cloud clamp, scroll recal, mobile overlap). Plus the flagged **CSP header in `next.config.ts`** (see [[02 - Commands, Hooks & CSP Fix]]).

Out of scope (per Anant + note 10): Hero / About / floating terminal (done by Kiro — do not touch); **light mode** palette (deferred — the toggle becomes a dark-only button only); Orby's 3D model / persona voice / chat-nav pipeline (the `nextgen-chatbot/` folder owns Orby's brain); the chatbot layer (`src/app/api/`, `src/lib/chat-*`).

## Hard "do not" list (from note 10 Part 8)
No git commits, no Vercel/remote pushes (Anant owns both). **pnpm only** (no npm/yarn). No `tailwind.config.ts` (Tailwind v4 is CSS-first — tokens in `globals.css`). Never hand-edit `src/sanity/types/index.ts` (run `pnpm typegen`). Don't rename `technologies[]`→`skills[]`. Don't re-add `color` to `skill`. Don't touch `OrbyCanvas.tsx`, `src/app/api/`, or `src/lib/chat-*`. Don't create `src/pages/` (App Router). Biome is the only linter/formatter. Invent no GitHub/live/credential URLs — leave empty and flag.

## Corrected phase order (mirrors note 10 Part 7)
The original phase order had errors. Use this:
- **Phase 0 — Real content + 2 small schema touches.** Delete fake certs; push real projects/experience/skills ([[09 - Sanity Content Spec]]) with `githubUrl` resolved via `mcp__github__search_repositories`; **add `summary` to project** and **`logo` to `EDUCATION_QUERY`**; `pnpm typegen` → `pnpm typecheck`. No renames.
- **Phase 1 — Motion primitives.** Build `useSpaceFloat`; confirm `CometCard` (4 variants) is the single hover surface; extract `SpaceRail`. Unblocks every section.
- **Phase 2 — Header theme pill (10 min).** [[13 - Dark Mode Toggle]] — `<div>`→`<button>` + `useTheme()`, dark-only.
- **Phase 3 — ObsidianBackground.** [[11 - ObsidianBackground Enhancement]] — postprocessing via `three-artist`; perf-guard mobile.
- **Phase 4 — Section rebuilds:** Experience (render Portable Text `description` + expand) → Projects (centre header, `summary`, enhance Framer slider) → Skills (add the capability graph on the working pill grid + 7 effects) → Education (centre header, blobs already done, living pulse) → Certifications (delete fakes, out-links) → Achievements (kicker + rail outside box) → Blog (read `BlogFeed` TODO first) → Contact (frame-not-fill; read `ContactPanel` first) → Footer (compact, translucent).
- **Phase 5 — Orby friction.** [[12 - Orby Friction Fixes]] — after heights settle.
- **Phase 6 — CSP header.** Add CSP to `next.config.ts` (it already has HSTS/X-CTO/X-Frame/Referrer/Permissions — only CSP missing); run **report-only first**. See [[02 - Commands, Hooks & CSP Fix]].

## Two-machine rule
Repo in WSL (`/home/anant_gupta/projects/hub/portfolio/`, `Chatbot` branch merging to `main` before a `frontend` branch). Build there (`cd repo` → `claude`); this vault is the playbook. Claude Code reads notes by direct file read at `/mnt/d/.../frontend/` (preferred) or jarvis MCP (fallback). Don't edit repo files from Cowork.

## Note index
- [[10 - Codebase Reality & Confusion Clearance]] — **the codebase source of truth; read first.**
- [[01 - Motion System & Comet Cards]] · [[02 - Sanity as Single Source of Truth]] · [[03 - Experience Section]] · [[04 - Projects Carousel]] · [[05 - Skills Capability Graph]] · [[06 - Education Flowchart]] · [[07 - Certifications & Achievements]] · [[08 - Blog, Contact & Footer]] · [[09 - Sanity Content Spec]] · [[11 - ObsidianBackground Enhancement]] · [[12 - Orby Friction Fixes]] · [[13 - Dark Mode Toggle]].
- Build kit (how Claude Code executes): [[00 - Frontend Build Kit — Index]].

## Current State
Planning, reconciled to verified codebase reality. No code. Build kit in `claude-code-setup/`.

## Next Action
Phase 0 from [[03 - Per-Phase Build Prompts]].

## Log
- **2026-06-12:** Built the kit, then reconciled all notes to [[10 - Codebase Reality & Confusion Clearance]] (Claude Code's verified codebase read). Corrected the Sanity model (no skillCategory/color; technologies[] vs skills[]; githubUrl; percentage/proficiency), reframed Skills/Education as augmentations not rescues, fixed phase order, added the three missing-component notes (background, Orby fixes, dark mode), and decisions: enhance the Framer carousel (not R3F), add a `summary` field to project.
