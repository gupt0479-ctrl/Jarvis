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
  - "[[14 - Global Fixes — Header & Section Spacing]]"
next: "Refinement pass — Phase R0 (static header + section spacing) then R1 (schema: color/summary/coverImage/visibility/logo + content). See [[03 - Per-Phase Build Prompts]]."
---
# Frontend Overhaul — Build Plan
> **STATUS 2026-06-13: the build largely RAN — this is now a REFINEMENT pass.** The original 7-phase build executed; the capability graph, R3F education blobs, R3F projects carousel, achievements rail, centered headers, and project summaries all render (per screenshots). Claude Code's `[[BUILD-STATUS]]` "nothing built" table is wrong; what's real is its `## UI Fixes` list (items 1–14) plus the two global header/spacing fixes. The refinement prompts are the **R-phases** in [[03 - Per-Phase Build Prompts]]. Two earlier-note corrections from the graphify codebase map: **Projects and Education are R3F** (drei `Float` + `@react-spring/web` / `MeshDistortMaterial`), not Framer Motion; and **a per-skill `color` field is now ADDED** to Sanity (reversing the old "no color" rule) to drive the dot site-wide.

Spine note for the portfolio's **frontend** rebuild. Sibling of [[00 - Nextgen Chatbot — Build Plan]] (the AI agent) — same two-machine model, same "design in the vault, build in WSL" discipline. This note owns *what we are changing and why*; each section's *how* is its own note. The raw brief is `[[Portfolio]]` → "UI Enhancement" (items 1–24); these notes are the **decided** form.

> **READ FIRST: [[10 - Codebase Reality & Confusion Clearance]].** Claude Code (Sonnet 4.6) verified every claim against the live repo. It is the **codebase source of truth** and it corrected several assumptions the original notes made. Notes 01–09 have been reconciled to it (2026-06-12). When a note and note 10 disagree, **note 10 wins** — it read the actual files.

## The two theses (unchanged, but mechanism corrected by note 10)
1. **One motion language.** "In space / wiggles in its padding / comet-card" = **one new `useSpaceFloat` hook** + the **already-existing `CometCard`** (4 variants: default/dark/subtle/ghost) + **one extracted `SpaceRail`**. Not nine animations. See [[01 - Motion System & Comet Cards]].
2. **One data source.** Everything renders from Sanity. But the schema is **already rich and mostly correct** — `skill` has `category`/`proficiency`/`percentage`/`tone`, colour is **derived from `category`** (no `color` field, do not add one), there is **no `skillCategory` doc**, and the reference fields are **`technologies[]`** (experience/project) vs **`skills[]`** (certification) — *do not rename them*. See [[02 - Sanity as Single Source of Truth]]. Real content in [[09 - Sanity Content Spec]].

## Scope of this rebuild (updated with note 10's three added topics)
In scope: Experience, Projects carousel, Skills graph, Education flowchart, Certifications, Achievements, Blog, Contact, Footer, the motion + Sanity layers, **plus** the three components note 10 documented — [[11 - ObsidianBackground Enhancement]] (Bloom/additive/chromatic polish), [[13 - Dark Mode Toggle]] (make the dead pill a real dark-only button), and [[12 - Orby Friction Fixes]] (speech-cloud clamp, scroll recal, mobile overlap). Plus the flagged **CSP header in `next.config.ts`** (see [[02 - Commands, Hooks & CSP Fix]]).

Out of scope (per Anant + note 10): Hero / About / floating terminal (done by Kiro — do not touch); **light mode** palette (deferred — the toggle becomes a dark-only button only); Orby's 3D model / persona voice / chat-nav pipeline (the `nextgen-chatbot/` folder owns Orby's brain); the chatbot layer (`src/app/api/`, `src/lib/chat-*`).

## Hard "do not" list (from note 10 Part 8)
No git commits, no Vercel/remote pushes (Anant owns both). **pnpm only** (no npm/yarn). No `tailwind.config.ts` (Tailwind v4 is CSS-first — tokens in `globals.css`). Never hand-edit `src/sanity/types/index.ts` (run `pnpm typegen`). Don't rename `technologies[]`→`skills[]`. **Do ADD `skill.color`** (preset palette — reversed 2026-06-13, drives the dot site-wide except the Skills section). Don't touch `OrbyCanvas.tsx`, `src/app/api/`, or `src/lib/chat-*`. Don't create `src/pages/` (App Router). Biome is the only linter/formatter. Invent no GitHub/live/credential URLs — leave empty and flag.

## Refinement phase order (R-phases — see [[03 - Per-Phase Build Prompts]])
The build ran; these are targeted fixes from `[[BUILD-STATUS]]` `## UI Fixes` + the two global fixes.
- **R0 — Global:** static header pill + kill the section-backdrop blank box + unify section padding ([[14 - Global Fixes — Header & Section Spacing]]).
- **R1 — Sanity schema + content:** add `skill.color`, `project.summary`; make `coverImage` optional; remove `project.visibility`; add `logo` to `EDUCATION_QUERY`; push real skills/projects/experience; delete fake certs ([[02 - Sanity as Single Source of Truth]], [[09 - Sanity Content Spec]]).
- **R2 — Experience:** type-chip by location, achievements off gold, click-to-open description ("more"), comet dialed down, Sanity dot colours ([[03 - Experience Section]]).
- **R3 — Projects (R3F):** comet down + Float bounded, side cards decoupled from centre hover, remove case-note (summary only), ≤4 skills ([[04 - Projects Carousel]]).
- **R4 — Skills:** remove count box + "All" button, same-line layout, divergent trajectories, unique effects for mobile/soft-skills/testing, 7 fixed-size skill effects, no colour dot here ([[05 - Skills Capability Graph]]).
- **R5 — Education (R3F):** equal opacity, deformation gradient via `distort`, off-axis layout, single upward travelling pulse, subtle card comet ([[06 - Education Flowchart]]).
- **R6 — Certs + Achievements:** cert comet down + out-links; achievements smaller header, minimal gap, one transparent subtle comet for all three ([[07 - Certifications & Achievements]], [[14 - Global Fixes — Header & Section Spacing]]).
- **R7 — Blog/Contact/Footer:** centre blog header, GitHub bottom-lift (not comet), smaller contact card, edge-aligned compact footer ([[08 - Blog, Contact & Footer]]).
- **R8 — Orby frictions + CSP report-only + a11y (last)** ([[12 - Orby Friction Fixes]], [[02 - Commands, Hooks & CSP Fix]]).

> Deferred (not part of the refinement backlog unless asked): [[11 - ObsidianBackground Enhancement]] (Bloom/postprocessing polish) and full light mode.

## Two-machine rule
Repo in WSL (`/home/anant_gupta/projects/hub/portfolio/`, `Chatbot` branch merging to `main` before a `frontend` branch). Build there (`cd repo` → `claude`); this vault is the playbook. Claude Code reads notes by direct file read at `/mnt/d/.../frontend/` (preferred) or jarvis MCP (fallback). Don't edit repo files from Cowork.

## Note index
- [[10 - Codebase Reality & Confusion Clearance]] — **the codebase source of truth; read first.** Plus the graphify map at `../INDEX`, `../architecture`, `../components`, `../data`.
- [[BUILD-STATUS]] — the refinement backlog (`## UI Fixes` 1–14); ignore its stale "nothing built" table.
- [[01 - Motion System & Comet Cards]] · [[02 - Sanity as Single Source of Truth]] · [[03 - Experience Section]] · [[04 - Projects Carousel]] · [[05 - Skills Capability Graph]] · [[06 - Education Flowchart]] · [[07 - Certifications & Achievements]] · [[08 - Blog, Contact & Footer]] · [[09 - Sanity Content Spec]] · [[11 - ObsidianBackground Enhancement]] · [[12 - Orby Friction Fixes]] · [[13 - Dark Mode Toggle]] · [[14 - Global Fixes — Header & Section Spacing]].
- Build kit (how Claude Code executes): [[00 - Frontend Build Kit — Index]].

## Current State
Build executed; refinement pass defined (R0–R8). Notes reconciled to the graphify codebase map (R3F Projects/Education) + the new UI-fix backlog. Build kit in `claude-code-setup/`.

## Next Action
Phase 0 from [[03 - Per-Phase Build Prompts]].

## Log
- **2026-06-12:** Built the kit, then reconciled all notes to [[10 - Codebase Reality & Confusion Clearance]] (Claude Code's verified codebase read). Corrected the Sanity model (no skillCategory/color; technologies[] vs skills[]; githubUrl; percentage/proficiency), reframed Skills/Education as augmentations not rescues, fixed phase order, added the three missing-component notes (background, Orby fixes, dark mode), and decisions: enhance the Framer carousel (not R3F), add a `summary` field to project.
