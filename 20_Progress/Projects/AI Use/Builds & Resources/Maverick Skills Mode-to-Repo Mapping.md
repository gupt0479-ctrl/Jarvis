---
type: evergreen
status: sprout
created: 2026-07-29
updated: 2026-07-29
tags:
  - evergreen
  - ai
  - claude-code
notes:
  - "[[Maverick Skills Analysis - Cross-Reference with GitHub Repos]]"
  - "[[40_Resources/CS/Repos]]"
next:
---
# Maverick Skills Mode-to-Repo Mapping
## Why This Exists
[[Maverick Skills Analysis - Cross-Reference with GitHub Repos]] maps all 100 of Maverick's prompt shortcuts against real Claude Code repos and skills — a different layer than [[PDF's Ingestion Implementation#Claude Code Skills & Repos: Implement vs. Knowledge Matrix - REVIEW|the Claude Code Skills & Repos Matrix]], which decides repo-by-repo confidence tier. This note is the condensed reference table for the *other* direction: given a Maverick-style prompt mode, which installed skill already covers it — use it before writing a custom skill, so a capability doesn't get rebuilt that a Tier-1 install (ECC, mattpocock-skills, gstack) already provides.
## The Five High-Impact Bundles
| Bundle | Maverick Modes | What Covers It | Status (2026-07-29) |
|---|---|---|---|
| **Pressure Testing** | /premortem, /redteam, /blindspots, INVERT | `/challenge` (`.claude/skills/challenge.md`) | ✅ Built (PDF pass) |
| **Deep Analysis** | PARETO, WARGAME, /swot, LEVERAGE | `/strategy` (`.claude/skills/strategy.md`) | ✅ Built (this pass) |
| **Writing Quality** | /ghost, /rephrase, /polish, /punch | `anti-slop-editor` agent + gstack "eng review" (gstack queued, not yet installed) | ⚠️ Partial — anti-slop-editor built, gstack still queued |
| **Code Quality** | /code, /refactor, /test, /debug, ARCHITECTURE | gstack + mattpocock-skills + spec-kit | ⚠️ Queued, not yet installed (see [[40_Resources/CS/Repos]]) |
| **Learning & Skill Building** | /teachme, /eli5, /drill, GAPFINDER, /mentor | `learning-agent` (in vault) + mattpocock-skills | ⚠️ Partial — learning-agent built, mattpocock-skills still queued |
## Category Verdicts (Full Detail in Source Note)
- **Writing & Style** — 60% already have repos; 40% composited from anti-slop-editor + gstack; 0% need new custom skills.
- **Artifacts & Creation** — 90% have direct repos (Claude Code native tools, Excalidraw); 10% light composition.
- **Thinking & Reasoning** — 70% already covered (Claude native thinking, gstack, mattpocock); 30% were the `/challenge` gap, now closed.
- **Learning & Mastery** — 80% covered; 20% are learning-agent improvements, already planned.
- **Analysis & Strategy** — 50% covered via GSD + gstack; 50% were the `/strategy` gap, now closed.
- **Creative & Content** — 80% covered by agency-agents (queued); 20% low priority, not content-marketing focused.
- **Coding & Technical** — 100% covered by existing/queued repos (gstack, spec-kit, Claude native).
- **Research & Deep Dives** — 70% covered (Applied ML, research-distiller agent); 30% light composition.
- **Power Commands** — 100% covered — CPR (`/preserve`/`/compress`/`/resume`) is Jarvis-only per [[How Anant Uses Each Repo]]'s status marker; gbrain supersedes the memsearch/context-sync half.
## What This Changes Now That Both Gaps Are Closed
[[Maverick Skills Analysis - Cross-Reference with GitHub Repos]]'s own two flagged custom-skill gaps were `/challenge` and `/strategy` — both are now real files in `.claude/skills/`. The remaining Maverick-mode gaps in the table above (`/mirror` style transfer, `/speedrun` accelerated learning) are explicitly flagged **Medium priority, deferrable** in the source note — not queued for this pass.
## How To Use This Table
Before writing any new custom skill: check whether the capability already falls under an existing bundle above. If it's Writing Quality, Code Quality, or Learning & Skill Building and the underlying repo (gstack, mattpocock-skills) is still queued rather than installed, the fix is to finish that install — not to write a parallel custom skill that duplicates what the queued repo already provides once it lands.
## Evidence
- [[Maverick Skills Analysis - Cross-Reference with GitHub Repos]] — the full 100-mode breakdown this note condenses
- `.claude/skills/challenge.md`, `.claude/skills/strategy.md` — the two gaps this table confirms are now closed (skill files, not indexed as vault notes)
- [[40_Resources/CS/Repos]] — real install status for gstack, mattpocock-skills, spec-kit referenced above
- [[How Anant Uses Each Repo]] — cross-referenced, not duplicated, per [[00_Execution]]
