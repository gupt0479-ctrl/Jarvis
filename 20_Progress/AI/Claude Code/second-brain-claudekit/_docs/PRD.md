# PRD — second-brain-claudekit

## Problem

Anant runs Claude Code across real, active codebases at once — confirmed tracked in Jarvis's own `20_Progress/AI/Claude Code/MOC.md`: Jarvis (this vault's own `.claude/`), CausalOps, OpsPilot, Resq, The Plan (a personal-life vault), Github ReadMe, Portfolio, Trading View — plus BOOM, a UROP research project tracked separately (`20_Progress/UROP/BOOM Board.md`) that doesn't yet have its own Claude Code setup entry in that MOC. Every week, new Claude Code tooling shows up worth trying: skill libraries (mattpocock-skills, gstack), memory MCPs (gbrain), agent harnesses (ECC), starter kits. Two failure modes are equally real and both have already happened:

1. **Install-and-forget** — a tool gets copied straight into a real project's `.claude/` or the global `~/.claude/` on the strength of a README, then turns out broken, redundant, or wrong for the workflow. `20_Progress/AI/Claude Code/` in the Jarvis vault already shows the cost of this: most project folders there are marked `static` or `stale` in `MOC.md`, and a full raw copy of `~/.claude` (`.claude_windows/`, `.claude_wsl/`) sits in the vault as dead, credential-bearing clutter nobody prunes.
2. **Plan-and-never-run** — the opposite failure, also already documented: `60_Claude/20_Distilled_Notes/Sources - Plan/PDF's Ingestion Implementation.md`'s Claude Code Skills & Repos Matrix, under its literal **"Tier 1: INSTALL NOW (Proven, High-Value)"** table (ECC, mattpocock-skills, gstack, cpr-compress-preserve-resume, context-sync, spec-kit — 6 items), sat unexecuted for weeks after being written, confirmed directly against `.claude/skills/`, `.claude/agents/`, and `~/.claude.json` in the 2026-07-29 execution pass (`60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution.md`, `# Github` section).

    **Correction (2026-08-19):** earlier drafts of this doc mis-cited `GitHub Ingestion Implementation.md` as the Tier-1 list's source — verified false by direct re-read. That file has no table labeled "Tier 1" at all; it has its own, separate, unlabeled **"VS Code + Claude Setup (Priority 1 — Install Today)"** list of only 4 items (ECC, mattpocock-skills, cpr-compress-preserve-resume, context-sync — no gstack, no spec-kit). `00_Execution.md`'s own "sat unexecuted for three weeks" verdict is checked against the 6-item Tier-1 table in `PDF's Ingestion Implementation.md`, not the 4-item Priority-1 list. Both lists are real and both went unexecuted for the same three weeks — they are just two different notes, not one.

Neither a bias toward installing everything nor a bias toward endlessly researching without installing anything solves this. What's missing is a **disciplined middle step**: a place to actually run a tool for real — install it, initialize it, hit its real failure modes — before it's allowed anywhere near a project that matters, and a place to record *why* a decision was made once it is.

## Who this is for

One person: Anant, solo developer, running Claude Code (and Codex, Cursor, Kiro) across multiple real projects and one personal-knowledge vault. Not a team. Not distributed. This repo (`gupta-builds/second-brain-claudekit`) is never installed by anyone else, never versioned for external consumers, never a plugin — see `_docs/Design.md` for why that distinction matters mechanically, not just philosophically.

## What this repo actually is (confirmed 2026-08-09)

**Dual-purpose, not single-purpose.** This repo is:

1. **The external-tool qualification pipeline** — `sandbox/` → `tested-tools/` → promoted (repo-scoped or global), for tooling that comes from *outside* this repo. `_docs/Architecture.md` covers the mechanics.
2. **A Jarvis-enhancer / incubator** — several `sandbox/` clones exist specifically to improve Jarvis's own PKM capability, not to feed some other project: `obsidian-mind`, `obsidian-second-brain`, `gbrain`, `graphify`, `claude-mem`, `agentic-inbox` are the confirmed starting set (per `sandbox/README.md`'s inventory) — an explicitly open-ended list, not closed.

There is a named, longer-horizon third phase — **Jarvis's own setup becoming self-improving**, using this repo's evidence as the input — but it is strictly sequenced and evidence-gated, not something either purpose above builds toward automatically: the qualification pipeline has to run solidly for a real stretch of time, enough proven, tested, dated decisions have to accumulate as real evidence, and *only then* does anything about what specifically gets automated get decided. Nothing here assumes what "self-improving" will concretely mean before that evidence exists. See `_docs/Design.md` for the full statement of this sequencing and its non-negotiable logging requirement.

## What "solved" looks like

- **Every tool sitting in a rigid folder** (`.claude/skills/`, `.claude/commands/`, or the real global `~/.claude/`) **has a documented reason it's there** — traceable to a real test, not a README summary. `_docs/Promotion-Criteria.md` defines what "documented reason" means concretely.
- **Nothing gets promoted without having been run for real first** — installed, initialized, exercised against its actual failure modes (per `_docs/Architecture.md`'s pipeline). GBrain clearing this bar (`bun install` → `gbrain init --pglite --no-embedding` → `doctor` reporting 80/100 health, a real PGLite database at `~/.gbrain/`) is the proof this works when followed; gstack failing at a real Playwright Chromium launch check is proof the bar catches real blockers instead of hiding them.
- **Anything that actually crosses into Jarvis's real `.claude/` meets Jarvis's own build standard at that point** — the directory-shaped skill format, full agent frontmatter, and defined hook lifecycle `Jarvis OS — North Star.md` Part 5 already specifies for Jarvis's native tooling. This repo's own pipeline mechanics don't need that shape internally (see `_docs/Design.md`) — Jarvis's bar applies at the moment of promotion into Jarvis, not before.
- **Every decision has a matching record in Jarvis**, not just in this repo — `_docs/Jarvis.md` defines the manual ritual, and `20_Progress/Projects/AI Use/Claude Kit/` is where it lives.
- **The gap between "planned" and "executed" stays visible and small.** The multi-week gap documented above should not recur — every tool that clears the sandbox stage gets a same-session (or explicitly flagged, dated) decision, not an indefinite one.

## Non-goals

- This is not a shareable starter kit release, despite its shape (`.claude/`, `commands/`, `60_Claude/Templates/`, `60_Claude/vault-rules/`) resembling one — see `_docs/Design.md`.
- This is not a general-purpose package manager or automated CI pipeline for skill installation. The qualification step is manual and deliberately slow.
- This does not track every starred GitHub repo — `40_Resources/CS/Repos.md` in the Jarvis vault already does that job as a discovery/triage layer. This repo and its Jarvis-side tracking (`20_Progress/Projects/AI Use/Claude Kit/`) only start once a repo is actually cloned into `sandbox/`.
- This does not decide global-vs-project-scoped promotion by itself for tools bound for the real global `~/.claude/`. That decision, and the actual install, happens in a separate session working directly at the Windows home directory, then gets replicated to the WSL home directory — see `_docs/Design.md`.
- This does not keep its own copy of tool-by-tool pipeline state. `20_Progress/Projects/AI Use/Claude Kit/Tool Map.md` in Jarvis is the sole source of truth for that — see below.

## Current state

Tracked live in Jarvis, not duplicated here: **`20_Progress/Projects/AI Use/Claude Kit/Tool Map.md`** is the one authoritative, per-tool record of pipeline stage, blockers, and verdicts — updated the same session anything changes. Keeping a second "current state" table in this file was tried and it drifted stale (the version this file carried through 2026-08-08 was already behind `Tool Map.md`'s real content by the time it was checked on 2026-08-09) — exactly the failure `Jarvis OS — North Star.md`'s "one fact, one home" rule exists to prevent. Read `Tool Map.md` for what's actually true right now.

Full background: Jarvis vault, `60_Claude/10_Source_Summaries/Github Ingestion/Claude Kit Implementation.md` and `60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution.md`'s `# Github` section.
