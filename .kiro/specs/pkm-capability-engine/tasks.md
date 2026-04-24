# Implementation Plan: PKM Capability Engine

## Overview

This plan implements the Capability Engine for the Jarvis vault in four phases, building on the already-completed Phase 0 (schema hardening — `types.json`, `Vault Operating System.md`, and all 7 templates are in place). All work uses Obsidian MCP tools to create and modify vault files. The implementation follows the design's phased migration: control surfaces first, then flagship note enrichment, then output generation, then weekly cadence.

## Tasks

- [x] 1. Create guide and reference documents under `40_Resources/Capability/`
  - [x] 1.1 Create `40_Resources/Capability/Capability Engine Guide.md`
    - Overview of the capability engine, how it works, and how to use it
    - Link to Track Definitions, Vault Operating System, and all dashboards
    - _Requirements: 13.2, 16.1_
  - [x] 1.2 Create `40_Resources/Capability/Track Definitions.md`
    - Define all five tracks (`ai`, `systems`, `algorithms`, `career`, `trading`) with primary sources, scope, and examples grounded in the actual vault
    - _Requirements: 1.5, 13.2_
  - [x] 1.3 Create `40_Resources/Capability/Metadata Extension Guide.md`
    - Document all capability extension fields, allowed values, and usage rules
    - Reference the Canonical Schema in Vault Operating System
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 13.2_

- [x] 2. Create global Dataview dashboards
  - [x] 2.1 Create `60_Claude/60_Indexes/Capability Dashboard.md`
    - Dataview queries for: global count of tracked concepts, mastery distribution, overdue drills, recently enriched notes, notes missing evidence
    - _Requirements: 10.1, 10.4_
  - [x] 2.2 Create `60_Claude/60_Indexes/Question Dashboard.md`
    - Dataview queries for: open durable questions by track, unresolved misconceptions, debugging prompts backlog
    - _Requirements: 10.2, 10.4, 19.4_
  - [x] 2.3 Create `60_Claude/60_Indexes/Proof Dashboard.md`
    - Dataview queries for: outputs produced by track, concepts with no evidence, in-progress interview stories / portfolio bullets / demos
    - _Requirements: 10.3, 10.4_

- [x] 3. Create per-track Field OS dashboards
  - [x] 3.1 Create `60_Claude/60_Indexes/Field OS/AI Field OS.md`
    - Sections: capability summary, overdue drills, recent progress, open questions, outputs produced, synthesis notes, links to AI Depth Ladder and AI Question Bank
    - All sections powered by Dataview queries filtered on `track` contains `ai`
    - _Requirements: 7.1, 7.2, 7.3_
  - [x] 3.2 Create `60_Claude/60_Indexes/Field OS/Systems Field OS.md`
    - Same structure as AI Field OS, filtered on `track` contains `systems`
    - _Requirements: 7.1, 7.2, 7.3_
  - [x] 3.3 Create `60_Claude/60_Indexes/Field OS/Algorithms Field OS.md`
    - Same structure, filtered on `track` contains `algorithms`
    - _Requirements: 7.1, 7.2, 7.3_
  - [x] 3.4 Create `60_Claude/60_Indexes/Field OS/Career Field OS.md`
    - Same structure, filtered on `track` contains `career`
    - _Requirements: 7.1, 7.2, 7.3_
  - [x] 3.5 Create `60_Claude/60_Indexes/Field OS/Trading Field OS.md`
    - Same structure, filtered on `track` contains `trading`
    - _Requirements: 7.1, 7.2, 7.3_

- [x] 4. Create per-track Depth Ladders
  - [x] 4.1 Create `60_Claude/60_Indexes/Field OS/AI Depth Ladder.md`
    - Modeled after the BOOM Board pattern
    - Curated wikilink sections: core concepts, 30-minute refresher, 2-hour technical refresher, deep relearning pass
    - Dataview sections: overdue drills, all tracked concepts for `ai`
    - Include at least one compare-or-discriminate segment
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_
  - [x] 4.2 Create `60_Claude/60_Indexes/Field OS/Systems Depth Ladder.md`
    - Same structure for `systems` track, seeded with UROP/BOOM concepts
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_
  - [x] 4.3 Create `60_Claude/60_Indexes/Field OS/Algorithms Depth Ladder.md`
    - Same structure for `algorithms` track, seeded with CSCI 4041/2041 concepts
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_
  - [x] 4.4 Create `60_Claude/60_Indexes/Field OS/Career Depth Ladder.md`
    - Same structure for `career` track
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_
  - [x] 4.5 Create `60_Claude/60_Indexes/Field OS/Trading Depth Ladder.md`
    - Same structure for `trading` track
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_

- [x] 5. Create per-track Question Banks
  - [x] 5.1 Create `60_Claude/60_Indexes/Field OS/AI Question Bank.md`
    - Sections: open questions, misconceptions, oral exam prompts, debugging drills, build prompts, resolved learnings
    - Dataview queries filtered by `track` and `question_kind`
    - Prefer board-level entries over separate note files
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 17.1_
  - [x] 5.2 Create `60_Claude/60_Indexes/Field OS/Systems Question Bank.md`
    - Same structure for `systems` track
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 17.1_
  - [x] 5.3 Create `60_Claude/60_Indexes/Field OS/Algorithms Question Bank.md`
    - Same structure for `algorithms` track
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 17.1_
  - [x] 5.4 Create `60_Claude/60_Indexes/Field OS/Career Question Bank.md`
    - Same structure for `career` track
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 17.1_
  - [x] 5.5 Create `60_Claude/60_Indexes/Field OS/Trading Question Bank.md`
    - Same structure for `trading` track
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 17.1_

- [x] 6. Create editable Base registries
  - [x] 6.1 Create `60_Claude/60_Indexes/Bases/Capability Registry.base`
    - Query all notes with `type: concept` and a non-empty `track` field
    - Columns: name, track, difficulty, mastery_level, mastery_score, next_drill, drill_interval, status
    - Editable fields: track, mastery_level, drill_interval
    - Sortable by difficulty, mastery_level, next_drill
    - _Requirements: 11.1_
  - [x] 6.2 Create `60_Claude/60_Indexes/Bases/Question Triage.base`
    - Query all notes with tag `question` and `type: thought`
    - Columns: name, track, question_kind, question_status, created
    - Filterable by track, question_kind, question_status
    - _Requirements: 11.2_
  - [x] 6.3 Create `60_Claude/60_Indexes/Bases/Output Pipeline.base`
    - Query all notes with `type: output`
    - Columns: name, status, output_kind, track, source_concepts, created
    - _Requirements: 11.3_

- [x] 7. Checkpoint — Control surfaces complete
  - Verify all dashboards, Field OS boards, Depth Ladders, Question Banks, and Base files are created and render correctly
  - Ensure all tests pass, ask the user if questions arise.

- [x] 8. Create AI role prompt files
  - [x] 8.1 Create `40_Resources/Capability/AI Roles — Teacher.md`
    - Portable prompt pattern for expanding: What It Is, Why It Matters, Mental Model, Formal Model
    - _Requirements: 15.1, 15.2, 15.7_
  - [x] 8.2 Create `40_Resources/Capability/AI Roles — Examiner.md`
    - Portable prompt pattern for adding: oral exam prompts, drill cards, debugging drills, misconception checks
    - _Requirements: 15.1, 15.3, 15.7_
  - [x] 8.3 Create `40_Resources/Capability/AI Roles — Builder.md`
    - Portable prompt pattern for adding: implementation examples, related projects, demo specs, output candidates
    - _Requirements: 15.1, 15.4, 15.7_
  - [x] 8.4 Create `40_Resources/Capability/AI Roles — Connector.md`
    - Portable prompt pattern for adding: prerequisites, used_in links, synthesis candidates, cross-track links
    - _Requirements: 15.1, 15.5, 15.7_
  - [x] 8.5 Create `40_Resources/Capability/AI Roles — Critic.md`
    - Portable prompt pattern for identifying: weak explanations, missing evidence, hand-wavy outputs, notes with no practical leverage
    - _Requirements: 15.1, 15.6, 15.7_

- [x] 9. Create output and synthesis folder scaffolding
  - [x] 9.1 Create `60_Claude/45_Outputs/` folder with a placeholder index note
    - _Requirements: 5.1, 13.5_
  - [x] 9.2 Create `60_Claude/20_Distilled_Notes/Synthesis/` folder with a placeholder index note
    - _Requirements: 6.1, 13.6_
  - [x] 9.3 Create `60_Claude/50_Reviews/Weekly Synthesis/` folder with a placeholder index note
    - _Requirements: 14.1, 13.7_

- [x] 10. Checkpoint — Infrastructure complete
  - All folders, dashboards, boards, bases, templates, guides, and AI roles are in place
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 11. Enrich flagship concept notes — AI track
  - [x] 11.1 Identify and enrich 5-6 flagship AI concept notes with capability fields and Deep Dive sections
    - Add `track: [ai]`, `difficulty`, `mastery_level: novice`, `drill_interval`, and growth-rule-appropriate sections
    - Target notes in `40_Resources/CS/AI/`, AI workflow notes, MCP/agent notes
    - Follow growth rule: seed requires What It Is, Why It Matters, one Real Example, one-sentence explanation, one Source Anchor
    - Add at least one Contrast_Pair or Contrast With entry per note beyond seed
    - _Requirements: 1.1, 3.1, 3.4, 4.2, 18.2, 19.2, 21.3_

- [x] 12. Enrich flagship concept notes — Systems track
  - [x] 12.1 Identify and enrich 5-6 flagship Systems concept notes with capability fields and Deep Dive sections
    - Target UROP/BOOM notes: Observability, Kafka/Redis, API/Backend, Docker/WSL, MongoDB, Rust patterns
    - Same enrichment pattern as AI track
    - _Requirements: 1.1, 3.1, 3.4, 4.2, 18.2, 19.2, 21.3_

- [x] 13. Enrich flagship concept notes — Algorithms track
  - [x] 13.1 Identify and enrich 5-6 flagship Algorithms concept notes with capability fields and Deep Dive sections
    - Target CSCI 4041/2041 core concepts, OCaml pattern matching, DSA fundamentals
    - Create distilled mirror notes in `40_Resources/` or `60_Claude/20_Distilled_Notes/` when direct modification of `10_UMN/` notes is undesirable
    - _Requirements: 1.1, 3.1, 3.4, 4.2, 18.2, 19.2, 21.3, 21.4_

- [x] 14. Enrich flagship concept notes — Career and Trading tracks
  - [x] 14.1 Identify and enrich 4-5 flagship Career concept notes
    - Target career strategy, portfolio, mentorship, and internship notes under `20_Progress/Career/`
    - _Requirements: 1.1, 3.1, 3.4, 4.2, 18.2, 19.2_
  - [x] 14.2 Identify and enrich 3-4 flagship Trading concept notes
    - Target highest-value trading notes under `40_Resources/Trading/`
    - _Requirements: 1.1, 3.1, 3.4, 4.2, 18.2, 19.2_

- [x] 15. Compute drill schedules for all enriched notes
  - For each enriched concept note, compute `next_drill` using: `next_drill = last_drilled + clamp(round(drill_interval × mastery_multiplier), 3, 180)`
  - Set `last_drilled` to today's date for initial seeding
  - Apply default drill_interval by difficulty and mastery_multiplier by mastery_level
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5_

- [x] 16. Checkpoint — Flagship enrichment complete
  - Verify 20-30 notes have `track`, `difficulty`, `mastery_level`, and drill fields
  - Verify Capability Dashboard and Field OS boards show enriched notes
  - Ensure all tests pass, ask the user if questions arise.

- [x] 17. Generate output notes from enriched concepts
  - [x] 17.1 Create 3-4 interview story outputs from UROP/Systems enriched concepts
    - Store in `60_Claude/45_Outputs/` with `type: output`, `output_kind: interview-story`
    - Require `source_concepts` linking back to originating concept notes
    - Validate output gate: linked source concept has `mastery_level >= familiar` or linked project under `used_in`
    - Add output to source concept's `evidence` field
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_
  - [x] 17.2 Create 2-3 portfolio bullet outputs from projects and systems notes
    - `output_kind: portfolio-bullet`, same gate and provenance rules
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_
  - [x] 17.3 Create 2-3 reusable prompt outputs from AI workflow notes
    - `output_kind: reusable-prompt`, same gate and provenance rules
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_
  - [x] 17.4 Create 1-2 project brief outputs from high-signal concept clusters
    - `output_kind: project-brief`, same gate and provenance rules
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

- [x] 18. Create initial synthesis notes
  - [x] 18.1 Create 2-3 synthesis notes bridging concepts across tracks
    - Store in `60_Claude/20_Distilled_Notes/Synthesis/`
    - Each must link at least 2 concepts from at least 2 distinct tracks
    - Use examples from design: Rust ownership vs OCaml immutability, Kafka pipelines vs agent orchestration, observability vs AI evaluation
    - _Requirements: 6.1, 6.2, 6.3, 6.4_

- [x] 19. Checkpoint — Output pass complete
  - Verify at least 10 output notes exist with real provenance
  - Verify Proof Dashboard shows outputs by track
  - Ensure all tests pass, ask the user if questions arise.

- [x] 20. Establish weekly synthesis review workflow
  - [x] 20.1 Create a Weekly Synthesis review template at `30_Order/Templates/Capability/Weekly Synthesis Template.md`
    - Sections: concepts enriched this week, overdue drills, unresolved questions, outputs created, 1-3 synthesis candidates
    - Use Dataview queries where possible for overdue drills and unresolved questions
    - _Requirements: 14.1, 14.2, 14.3_
  - [x] 20.2 Generate the first Weekly Synthesis review note in `60_Claude/50_Reviews/Weekly Synthesis/`
    - Populate with current state: enriched notes, overdue drills, open questions, outputs, synthesis candidates
    - _Requirements: 14.1, 14.2, 14.3_

- [x] 21. Update `00_Dashboard.md` with Capability Engine links
  - Add a new "Capability Engine" section with links to: Capability Dashboard, Proof Dashboard, Question Dashboard, and the five Field OS boards
  - Preserve all existing dashboard content and frontmatter
  - _Requirements: 13.3, 16.2_

- [x] 22. Final checkpoint — Capability Engine complete
  - Verify all five tracks have a functioning Field OS, Depth Ladder, and Question Bank
  - Verify at least 25 notes have track, difficulty, mastery_level, and drill fields
  - Verify at least 10 output notes exist with real provenance
  - Verify weekly synthesis review can identify overdue drills and evidence gaps
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Phase 0 (schema hardening) is already complete — `types.json`, `Vault Operating System.md`, and all 7 templates are in place
- All vault operations use Obsidian MCP tools (`mcp_obsidianVault_*`)
- Existing frontmatter must be preserved on all modified notes
- `10_UMN/` is a feeder layer — prefer creating distilled mirror notes over bulk restructuring
- Files in `60_Claude/05_Clippings/` are immutable after capture
- Checkpoints ensure incremental validation between phases
- Depth Ladders follow the BOOM Board pattern from `20_Progress/UROP/BOOM Board.md`
