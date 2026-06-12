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
  - "[[01 - Motion System & Comet Cards]]"
  - "[[02 - Sanity as Single Source of Truth]]"
  - "[[03 - Experience Section]]"
  - "[[04 - Projects Carousel]]"
  - "[[05 - Skills Capability Graph]]"
  - "[[06 - Education Flowchart]]"
  - "[[07 - Certifications & Achievements]]"
  - "[[08 - Blog, Contact & Footer]]"
  - "[[09 - Sanity Content Spec]]"
next: "Run Phase 0 (Sanity-as-SoT) from the build kit: [[00 - Frontend Build Kit — Index]]."
---
# Frontend Overhaul — Build Plan
This is the spine note for the portfolio's **visual/frontend** rebuild. It is the sibling of [[00 - Nextgen Chatbot — Build Plan]] (which owns the AI agent) — same two-machine model, same "design in the vault, build in WSL with Claude Code" discipline. This note owns *what we are changing and why*; each section's *how* lives in its own note, linked below. The raw, unstructured brief lives in `[[Portfolio]]` under "UI Enhancement" (sections 1–24); these notes are the **structured, decided** version of it. The notes are the source of truth — Claude Code reads them, it does not re-derive them.

## Goal
Turn a section-by-section "good idea, rough execution" portfolio into one coherent, premium, **space-physics** interface where every surface is driven by Sanity. Done looks like: every card floats and drifts in its own padding, every interactive card uses one shared comet-card primitive, every skill chip across the entire site renders the *same* colour and name pulled from one Sanity `skill` registry, and a recruiter can read every section cleanly with no fake data, no hardcoded content, and no green-on-dark eyesores.

## The two theses that make everything else fall out
Almost every item in the brief is an instance of one of these two ideas. Build the two primitives first and most sections become assembly, not invention.

1. **One motion language.** "Appears to be in space / wiggles in its own padding / comet-card on hover" is repeated for Experience, Projects, Skills categories, Education shapes, Certifications, Blog, Contact, the back-to-top button. That is not nine animations — it is **one** `useSpaceFloat` drift primitive + **one** `CometCard` wrapper, parameterised (drift radius, tilt strength, glow). Defined once in [[01 - Motion System & Comet Cards]], reused everywhere. Respect `prefers-reduced-motion` in the primitive, not in nine places.

2. **One data source.** "Everything on the card should render from Sanity," "skills must not be hardcoded," "colour + name come from the Sanity Skills section," "these are dummy/filler, write real content." That is one rule: **Sanity is the single source of truth, and `skill` is a first-class referenced document, not a string.** Defined in [[02 - Sanity as Single Source of Truth]]; the actual real content to load is [[09 - Sanity Content Spec]].

Everything else is per-section styling on top of those two.

## Scope of this rebuild
In scope: Experience, Projects carousel, Skills capability graph + category/skill interactions, Education flowchart, Certifications, Achievements, Blog ("What I read or do"), Contact card, Footer, and the cross-cutting motion + Sanity layers. Plus the one flagged open item from the chatbot build — **the CSP header in `next.config.ts`** — carried into this kit so it actually ships (see [[02 - Commands, Hooks & CSP Fix]]).

Out of scope, by the user's instruction:
- **Hero + About + floating terminal** — already fixed by Kiro and loved. Do not touch unless a concrete bug or dead code is found. (Brief items 1–3.)
- **Orby** — its own future prompt; lives in the chatbot plan, not here.
- **Light mode / dark-mode toggle** — undesigned; explicitly deferred. The toggle stays but light mode is a no-op task for later.

## Two-machine rule (carried over)
The portfolio repo is in WSL; build it there with Claude Code (`cd repo` → `claude`). This Windows vault is the playbook. Claude Code reads these notes by direct file read at `/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/frontend/` (preferred, zero network) or via the jarvis MCP (fallback). Do not edit repo files from Cowork. Same rule as the chatbot kit.

## Note index
- [[01 - Motion System & Comet Cards]] — the shared `useSpaceFloat` drift + `CometCard` tilt/glow primitive, the timeline rail, reduced-motion. Build first.
- [[02 - Sanity as Single Source of Truth]] — the data contract: `skill` as a referenced doc, what each section must read from Sanity, the no-hardcode rule.
- [[03 - Experience Section]] — timeline rail in space, employment-type chip placement, click-to-expand description, subtle drop-down affordance, Sanity skill chips.
- [[04 - Projects Carousel]] — centred header, three-card space carousel, comet-card only on the centre card, tether-pull transition, hover detail.
- [[05 - Skills Capability Graph]] — the stock-chart multi-trajectory graph (left) + category buttons and per-skill effects (right), the 7 unique skill effects.
- [[06 - Education Flowchart]] — amoeba→circle morph shapes, the living-pulse connector, off-axis flowchart layout.
- [[07 - Certifications & Achievements]] — centred header, Sanity skill chips, out-links only; Achievements as a separated experience-style timeline.
- [[08 - Blog, Contact & Footer]] — comet cards + translucency for Blog, the "frame not fill" Contact card, the compact translucent footer.
- [[09 - Sanity Content Spec]] — the real Anant content (projects, skills registry, experience, certs) to push to Sanity. Nothing fake.

## Current State
Planning. No code. Brief in `[[Portfolio]]` is the raw input; these notes are the decided form. Build kit in the sibling folder `claude-code-setup/`: [[00 - Frontend Build Kit — Index]].

## Next Action
Phase 0 — establish Sanity as source of truth (the `skill` registry + real content) per [[02 - Sanity as Single Source of Truth]] and [[09 - Sanity Content Spec]], because every visual section depends on it. Then build [[01 - Motion System & Comet Cards]] before any section. See [[03 - Per-Phase Build Prompts]].

## Log
- **2026-06-12:** Spun up the frontend overhaul kit mirroring the chatbot kit's structure. Collapsed the 24-item brief into two primitives (motion + Sanity) plus per-section notes. Carried the flagged CSP-header item into this kit. Pulled real project content (OpsPilot, Resq, SafeReach) from the vault for the Sanity spec.
