---
type: ai
status: sprout
created: 2026-06-07
tags:
  - "#ai"
  - jarvis
  - prompt
related:
  - "[[Jarvis OS — North Star]]"
---
# North Star — Execution Prompt
Paste the block below as the opening message of a fresh Cowork session in the Jarvis project. Model: Sonnet 4.6, high effort.

---

You are running a long convergence session on the Jarvis vault. Your job is to **execute the plan in `60_Claude/07_AI_Information/Jarvis OS — North Star.md`** — specifically Move 1 (collapse the instruction layer), Move 2 (finish the templates), Move 3 (build the one execution dashboard), and the skill/agent file-format cleanup described in Part 5.1–5.2. This is a multi-hour task. Do not rush, do not stop early, and do not declare done until the verification gate in every phase passes.

## What this task is and is not
- This is a **fix-what-exists** task. **Do not add new features, new MCP tools, new Python, new subsystems, or new top-level files.** Parts of the North Star that describe building MCP verbs, a semantic index, scheduled tasks, or new automation are **out of scope** — skip them and note them as deferred.
- Focus the cleanup on the **`60_Claude/` and `.claude/` folders** plus the four root files (`AGENTS.md`, `CLAUDE.md`, `HUMAN_WRITING.md`, and the dashboard). Make these clean, non-redundant, and internally consistent.
- The North Star itself may be partly outdated. When you find that reality has moved past it (a file already merged, a path already changed, a rule already fixed), **update the North Star to match reality** and record the correction in your worklog. Treat the plan as a guide to revise, not gospel.

## Hard guardrails (violating any of these is a failure)
1. **Conservative deletion.** Delete only content that is genuinely redundant (a rule that exists verbatim or near-verbatim in another file) or demonstrably dead (a broken link, a stale `next:`, a reference to a renamed path). When you remove a rule, it must already live in its single authority file, and you replace the removed copy with a one-line pointer. **If you are unsure whether something is redundant, keep it and flag it in the worklog — do not delete.**
2. **Never lose unique content.** Before deleting or merging a file, confirm every unique fact in it has a home in the surviving authority file. If a file has unique content, move that content first, verify it landed, then remove the duplicate.
3. **Preserve frontmatter and wikilinks** on every note you touch. Patch by heading; do not rewrite whole notes unless the note is a pure duplicate being merged out.
4. **Respect `status: tree` notes.** Several instruction files are `tree`. You may edit them per the North Star's Part 4 verdicts, but for any large structural change to a `tree` note, make the change, then immediately read it back and confirm nothing unique was lost.
5. **Do not touch** `50_Archive/`, `60_Claude/05_Clippings/` (raw sources), `.obsidian/`, `.git/`, or anything outside the vault. Do not write to the vault root (no new files there). Do not create files under WSL/UNC paths.
6. **All vault reads and writes go through the `jarvis` MCP server** (the Obsidian bridge), so Obsidian stays in sync. Use filesystem tools only for read-only inspection if the MCP is insufficient.
7. **One change at a time, verified.** After each edit, read back the changed section and confirm it is correct before moving on. Do not batch many blind edits.

## Method (follow in order)

### Phase 0 — Orient and plan (do not skip)
- Read `60_Claude/07_AI_Information/Jarvis OS — North Star.md` in full. It is your spec.
- Read the four root files and every file named in the **Part 4 audit table**.
- Create a TODO list mirroring Move 1's Part 4 verdicts (one task per file: keep / merge / cut / fix), then Move 2 (one task per template named in the 2026-05-31 audit), then Move 3 (the dashboard), then Part 5.1–5.2 (skill and agent file-format cleanup).
- Start a running **worklog** note at `60_Claude/07_AI_Information/Session Logs/Convergence Worklog 2026-06-XX.md` (use today's date). Append to it continuously: every file touched, every rule moved, every deletion with its justification, every place the North Star was wrong and how you corrected it. This is your audit trail and the raw material for the final change note.

### Phase 1 — Move 1: collapse the instruction layer
Execute the Part 4 audit table verdict by verdict. The end state you are driving toward: **one authority per fact, cold-start reading under ~400 lines, and no rule living in two files.**
- Establish the single **formatting authority** by merging `Jarvis Writing and Formatting` with `Vault Rules — Complete AI Ruleset` Parts 3–9 (they are ~80% the same). One formatting spec, not two. The other becomes a pointer or is cut once its unique content has moved.
- Merge orientation (`Vault Map` + the unique parts of `Agent Operating Guide`) into one short orientation file; narrow `AI_CONTEXT` to the live-state manifest only.
- Shrink `AGENTS.md` and `CLAUDE.md` to one-screen contracts that point at the North Star, the formatting authority, and `Jarvis Vault Architecture`. Remove the folder-role and routing tables that duplicate `Jarvis Vault Architecture`.
- Demote `Vault Operating System` to its property-schema table only.
- After each merge: verify the surviving file holds all unique content, fix inbound wikilinks that pointed at the removed copy, and update the worklog.
- **Verification gate:** open any two instruction files and confirm no sentence is true in both. Re-read the North Star's Part 4 and confirm every verdict is executed or consciously deferred with a logged reason.

### Phase 2 — Move 2: finish the templates
Work the template list in the 2026-05-31 audit (`Note Writing System — Audit and Roadmap`). For each shell template (`For Evergreen`, `For Progress`, `Textbook Template`, `Deep Dive Template`, `Concept Template` — fix its invalid `mastery (1/10)` YAML — and `Clipping Distill Template`): add a one-line description under every heading, one short block of real example content, inline plugin hooks (flashcards, Tasks for open questions, math where relevant), and link one existing gold-standard note (the MGMT 3001 week notes are the standard for course notes). Read each finished template back and confirm an agent could produce a vault-standard note from it without inventing structure.

### Phase 3 — Move 3: the one execution dashboard
Make `00_Dashboard.md` the single daily surface: active focus this week, in-motion notes (`20_Progress/` with a `next:`), the triage queue (inbox + clippings awaiting processing), and the decay list (orphans, stale notes, projects missing `next:`). Prefer live Dataview/Bases queries over hand-maintained lists. Use only plugins already installed. Do not invent new boards — consolidate existing ones into this single pane and leave pointers from any board you fold in.

### Phase 4 — Part 5.1–5.2: skill and agent file-format cleanup (no new code)
For the existing skills in `.claude/skills/` and agents in `.claude/agents/`: convert the `**Description:**` / `**Purpose:**` prose headers into proper YAML frontmatter (`name` in lowercase-hyphen gerund form, third-person `description` saying what it does and when). Tighten any skill body over 500 lines by moving deep detail into a sibling `reference.md` linked one level deep. **Do not write new Python, do not create `scripts/` directories, do not add new skills or agents.** This phase is formatting and structure only — making what exists spec-compliant and consistent.

### Phase 5 — Final change note (required)
Write a detailed note at `60_Claude/50_Reviews/North Star Convergence — Change Report 2026-06-XX.md` covering, in prose with tables where they help:
- **What changed** — every file edited, merged, or shrunk, and what its role is now.
- **What improved** — concretely (e.g. "cold-start reading dropped from ~X to ~Y lines", "formatting rules now live in one file instead of five", "N templates went from shells to instructive").
- **What was deleted** — a complete ledger: every removed file or rule, where its content now lives, and the one-line justification. This list must let a reader undo any deletion if they disagree.
- **What the North Star got wrong** — every place reality had moved past the plan and how you corrected the plan.
- **What was deferred** — everything out of scope (MCP wiring, semantic index, scheduled tasks, new automation) so the next session knows where to pick up.
- Append a continuity entry to `60_Claude/07_AI_Information/Session Logs/log.md`.

## Pacing
Take the full time this needs — likely well over an hour. Do not collapse phases. If you finish a phase early, re-verify it before advancing. The success criterion is not speed; it is that the `60_Claude/` and `.claude/` layers are clean, non-redundant, internally consistent, and that nothing unique was lost. When everything is done and verified, give a short summary and stop.
