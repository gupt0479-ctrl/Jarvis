---
type: evergreen
status: tree
created: 2026-04-24
updated: 2026-04-24
tags:
  - evergreen
  - system
  - capability
notes:
  - "[[Vault Operating System]]"
  - "[[Track Definitions]]"
  - "[[Metadata Extension Guide]]"
---

# Capability Engine Guide

The Capability Engine adds tracking, drilling, and output generation to Jarvis. It does not replace the existing vault structure — it layers capability metadata on top of it so concept notes can carry mastery state, drill schedules, and evidence links.

## The Core Loop

```
source → summary → concept → drill → project usage → output → evidence
```

A note that cannot enter this loop stays as a source summary. Only notes with real reuse potential get promoted to tracked concepts.

## Tracks

Five tracks organize all capability work:

| Track | What it covers |
|---|---|
| `ai` | ML, agents, MCP, prompts, AI evaluation |
| `systems` | Backend, Rust, observability, Kafka, Docker, MongoDB |
| `algorithms` | DSA, complexity, OCaml, algorithmic reasoning |
| `career` | Portfolio, interviews, mentorship, career strategy |
| `trading` | Markets, trading tools, quantitative workflows |

Full definitions with vault-grounded sources: [[Track Definitions]]

## Growth Rule

Concept notes grow in stages. You do not fill every section on day one.

- **Seed**: What It Is + Why It Matters + one Real Example + one-sentence explanation + one Source Anchor
- **Sprout**: adds Mental Model + Implementation + one Failure Mode + one Contrast Pair + two Diagnostic Questions
- **Tree**: adds Formal Model + Interview Angle + Related Projects + Drill Cards + evidence + teach-back explanation + Understanding Proof

A note stays at its current stage until the required sections are filled. This prevents blank-section bloat.

## Drill Scheduling

Each tracked concept carries `difficulty`, `mastery_level`, `drill_interval`, `last_drilled`, and `next_drill`.

Formula:
```
next_drill = last_drilled + clamp(round(drill_interval × mastery_multiplier), 3, 180)
```

Default intervals by difficulty: 1→21d, 2→14d, 3→10d, 4→7d, 5→5d.
Multipliers: novice=1.0, familiar=1.25, proficient=1.6, expert=2.0.

This does not depend on the Spaced Repetition plugin. It works purely from frontmatter fields.

## Output Gate

Outputs (interview stories, portfolio bullets, demos) require at least one of:
- A source concept with `mastery_level ≥ familiar`
- A linked project under `used_in`
- A linked artifact under `evidence`

No gate, no output. This prevents writing stories about things you cannot actually demonstrate.

## Where Things Live

### Global Dashboards (Dataview)

- [[Capability Dashboard]] — tracked concept count, mastery distribution, overdue drills, missing evidence
- [[Question Dashboard]] — open questions by track, unresolved misconceptions, debugging backlog
- [[Proof Dashboard]] — outputs by track, concepts with no evidence, in-progress artifacts

### Per-Track Boards

Each track gets three boards under `60_Claude/60_Indexes/Field OS/`:

| Board | What it does |
|---|---|
| Field OS | Control center — summary, drills, progress, questions, outputs, synthesis |
| Depth Ladder | Curated refresher sequences + drill queues (modeled on [[BOOM Board]]) |
| Question Bank | Open questions, misconceptions, oral-exam prompts, debugging drills, build prompts |

Links:
- [[AI Field OS]] · [[Systems Field OS]] · [[Algorithms Field OS]] · [[Career Field OS]] · [[Trading Field OS]]

### Editable Registries (Base files)

- `Capability Registry.base` — sort/edit tracked concepts by difficulty, mastery, next drill
- `Question Triage.base` — filter durable questions by track, kind, status
- `Output Pipeline.base` — track output status and kind

Dataview is read-only. Base files let you edit metadata from a table view without opening individual notes.

## Templates

All under `30_Order/Templates/Capability/`:

- [[Deep Dive Template]] — enriched concept note with growth-rule sections
- [[Output Template]] — output artifact (story, bullet, demo, brief, prompt)
- [[Synthesis Template]] — cross-track bridging note
- [[Question Bank Template]] · [[Field OS Template]] · [[Depth Ladder Template]] · [[Clipping Distill Template]]

## AI Roles

Five prompt roles for enrichment. These are portable patterns, not hardcoded to any specific tool.

| Role | What it adds |
|---|---|
| [[AI Roles — Teacher]] | Explanations, mental models, formal models |
| [[AI Roles — Examiner]] | Drill cards, oral-exam prompts, misconception checks |
| [[AI Roles — Builder]] | Implementations, projects, demo specs, output candidates |
| [[AI Roles — Connector]] | Prerequisites, used_in links, synthesis candidates |
| [[AI Roles — Critic]] | Flags weak explanations, missing evidence, hand-wavy outputs |

## Key References

- [[Vault Operating System]] — canonical schema contract
- [[Track Definitions]] — track scopes and primary sources
- [[Metadata Extension Guide]] — all capability fields, allowed values, usage rules
- [[00_Dashboard]] — vault control panel
