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
  - "[[Capability Engine Guide]]"
  - "[[Vault Operating System]]"
  - "[[Track Definitions]]"
---

# Metadata Extension Guide

All capability fields added to the Jarvis schema. These are additive — they extend the [[Vault Operating System|Canonical Schema]] without touching existing properties.

All property names and types are registered in `.obsidian/types.json`.

---

## `track`

- **Type**: list
- **Allowed**: `ai`, `systems`, `algorithms`, `career`, `trading`
- **Used on**: concept notes, question notes, output notes
- **Required**: yes, for any note entering the capability system

Assigns a note to one or more tracks. See [[Track Definitions]] for what each track covers and where its source material lives.

```yaml
track:
  - ai
  - systems
```

## `prerequisites`

- **Type**: list (wikilinks)
- **Used on**: concept notes
- **Required**: no

Concepts that should be understood first. Used by the Connector role and Depth Ladders to build learning sequences.

```yaml
prerequisites:
  - "[[Binary Search Trees]]"
  - "[[Big-O Notation]]"
```

## `used_in`

- **Type**: list (wikilinks)
- **Used on**: concept notes
- **Required**: no

Projects, boards, briefs, or implementations where this concept is applied. Satisfies one leg of the output gate — if a concept has a `used_in` link, it can generate outputs.

```yaml
used_in:
  - "[[UROP Project]]"
```

## `evidence`

- **Type**: list (wikilinks)
- **Used on**: concept notes
- **Required**: yes for `status: tree`

Outputs, demos, writeups, or briefs that prove understanding. When you create an output from a concept, add the output here. This is how the Proof Dashboard knows which concepts have real backing.

```yaml
evidence:
  - "[[Observability Interview Story]]"
```

## `difficulty`

- **Type**: number (integer 1–5)
- **Used on**: concept notes
- **Required**: yes for tracked concepts

Determines the default drill interval:

| Difficulty | Interval |
|---|---|
| 1 | 21 days |
| 2 | 14 days |
| 3 | 10 days |
| 4 | 7 days |
| 5 | 5 days |

Higher difficulty = shorter default interval = more frequent review.

## `mastery_level`

- **Type**: text
- **Allowed**: `novice`, `familiar`, `proficient`, `expert`
- **Used on**: concept notes
- **Required**: yes for tracked concepts

Current capability stage. Intentionally separate from the legacy `mastery` numeric field — Obsidian property types are global by name, and `mastery` is already typed as a number in `.obsidian/types.json`. Do not reuse it.

Mastery level determines the drill multiplier:

| Level | Multiplier | What it means |
|---|---|---|
| `novice` | 1.0 | You recognize the concept but cannot explain it reliably |
| `familiar` | 1.25 | You can explain it and give an example |
| `proficient` | 1.6 | You can apply it, debug with it, and contrast it |
| `expert` | 2.0 | You can teach it, build with it, and prove understanding |

## `mastery_score`

- **Type**: number (integer 1–10)
- **Used on**: concept notes
- **Required**: no

Optional finer-grained confidence score alongside the text-based `mastery_level`.

## `last_drilled`

- **Type**: date
- **Used on**: concept notes
- **Required**: no (set when a drill occurs)

Date of the most recent active review. Updating this triggers recomputation of `next_drill`.

## `next_drill`

- **Type**: date
- **Used on**: concept notes
- **Required**: no (computed)

Next scheduled review date:

```
next_drill = last_drilled + clamp(round(drill_interval × mastery_multiplier), 3, 180)
```

Minimum 3 days, maximum 180 days. This works without the Spaced Repetition plugin — it is pure frontmatter math.

## `drill_interval`

- **Type**: number (integer, days)
- **Used on**: concept notes
- **Required**: yes for tracked concepts

Days between reviews. Defaults come from `difficulty`. Editable via the Capability Registry base file.

## `question_kind`

- **Type**: text
- **Allowed**: `open`, `misconception`, `oral-exam`, `debugging`, `build`
- **Used on**: question notes (`type: thought`, tag `question`)
- **Required**: yes for durable question notes

| Kind | What it is |
|---|---|
| `open` | Unresolved question that persists across sessions |
| `misconception` | Wrong belief that needs correction — store both the wrong version and the fix |
| `oral-exam` | Prompt for verbal explanation practice |
| `debugging` | Prompt requiring diagnosis of a broken scenario |
| `build` | Prompt requiring construction or implementation |

## `question_status`

- **Type**: text
- **Allowed**: `open`, `active`, `resolved`
- **Used on**: question notes
- **Required**: yes for durable question notes

| Status | What it means |
|---|---|
| `open` | Not yet being worked on |
| `active` | Currently under investigation |
| `resolved` | Answered — kept for reference |

## `output_kind`

- **Type**: text
- **Allowed**: `portfolio-bullet`, `blog-draft`, `interview-story`, `demo-spec`, `project-brief`, `reusable-prompt`
- **Used on**: output notes (`type: output`)
- **Required**: yes for output notes

| Kind | When to use |
|---|---|
| `portfolio-bullet` | Concept demonstrated in a real project or implementation |
| `blog-draft` | Concept is teachable and you have something non-obvious to say |
| `interview-story` | Concept has a concrete problem-action-result narrative |
| `demo-spec` | Concept can become a working proof artifact |
| `project-brief` | Knowledge should become an execution plan |
| `reusable-prompt` | Concept works best as an agent workflow or instruction pattern |

## `source_concepts`

- **Type**: list (wikilinks)
- **Used on**: output notes
- **Required**: yes for output notes

The concept notes that feed this output. Every output must trace back to at least one source concept — this is how the output gate enforces provenance.

```yaml
source_concepts:
  - "[[Observability and Tracing]]"
```

## `concepts`

- **Type**: list (wikilinks)
- **Used on**: synthesis notes (`type: evergreen`, tag `synthesis`)
- **Required**: yes (minimum 2)

Concept notes being bridged. A valid synthesis must link at least two concepts from at least two distinct tracks.

```yaml
concepts:
  - "[[Rust Ownership]]"
  - "[[OCaml - Pattern Matching]]"
```

## `tracks`

- **Type**: list
- **Allowed**: `ai`, `systems`, `algorithms`, `career`, `trading`
- **Used on**: synthesis notes
- **Required**: yes (minimum 2 distinct values)

The tracks bridged by a synthesis note. Must contain at least two distinct values.

```yaml
tracks:
  - systems
  - algorithms
```

---

## Fields by Note Archetype

| Archetype | Key fields |
|---|---|
| Concept (`type: concept`) | `track`, `difficulty`, `mastery_level`, `drill_interval`, `prerequisites`, `used_in`, `evidence` |
| Output (`type: output`) | `track`, `output_kind`, `source_concepts` |
| Question (`type: thought`, tag `question`) | `track`, `question_kind`, `question_status` |
| Synthesis (`type: evergreen`, tag `synthesis`) | `concepts`, `tracks` |

---

## Relationship to Existing Schema

All capability fields are additive. Existing canonical properties are unchanged:

`type`, `status`, `created`, `updated`, `tags`, `notes`, `next`, `area`, `related_progress`, `source_url`, `input_kind`, `thought_kind`, `deadline`, `reviewed`

Full schema contract: [[Vault Operating System]]
