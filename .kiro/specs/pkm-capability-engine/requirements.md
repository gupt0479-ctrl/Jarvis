# Requirements Document

## Introduction

The PKM Capability Engine transforms the Jarvis Obsidian vault from a well-organized note archive into a compounding knowledge system. It extends the existing vault schema with capability-tracking fields, introduces structured templates for concept enrichment, builds per-track operational dashboards (Field OS, Depth Ladders, Question Banks), creates an evidence-first output system, and adds global analytics dashboards — all while preserving the current vault structure, plugin reality, and AI working agreements.

The system covers five ambition tracks (AI, Systems, Algorithms, Career, Trading) and treats `10_UMN/` primarily as a feeder layer. Broad restructuring of `10_UMN/` is out of scope, but selective enrichment of flagship concept notes or creation of distilled mirror notes is allowed when it strengthens long-term understanding in one or more tracks.

## Glossary

- **Vault**: The Obsidian-based personal knowledge management system named Jarvis
- **Capability_Engine**: The complete system of schema extensions, templates, dashboards, and workflows defined in this specification
- **Track**: One of five long-term ambition domains: `ai`, `systems`, `algorithms`, `career`, `trading`
- **Concept_Note**: A Markdown note with `type: concept` frontmatter representing a durable, enrichable piece of knowledge
- **Output_Note**: A Markdown note with `type: output` frontmatter representing a portfolio artifact, interview story, demo spec, or similar deliverable
- **Synthesis_Note**: A Markdown note with `type: evergreen` and tag `synthesis` that bridges concepts across two or more tracks
- **Question_Note**: A Markdown note with `type: thought` and tag `question` representing a durable question that persists across sessions
- **Field_OS**: A per-track Dataview dashboard serving as the track control center
- **Depth_Ladder**: A per-track curated board listing core concepts, refresher sequences, and drill queues
- **Question_Bank**: A per-track board organizing open questions, misconceptions, oral exam prompts, debugging drills, and build prompts
- **Mastery_Level**: A text enum (`novice`, `familiar`, `proficient`, `expert`) indicating concept proficiency
- **Drill_Interval**: An integer representing the number of days between scheduled reviews of a concept
- **Mastery_Multiplier**: A numeric factor applied to drill intervals based on mastery level
- **Deep_Dive_Template**: The Templater template used to create enriched concept notes with structured sections
- **Base_File**: An Obsidian `.base` file providing editable database-like views over Markdown notes
- **Dataview_Dashboard**: A Markdown file using Dataview queries to display live analytics
- **Canonical_Schema**: The set of frontmatter properties defined in `Vault Operating System.md`
- **Clipping**: A raw web capture stored in `60_Claude/05_Clippings/`
- **Source_Summary**: A source-grounded summary stored in `60_Claude/30_Source_Summaries/`
- **Growth_Rule**: The staged enrichment policy: `seed` → `sprout` → `tree` with defined section requirements at each stage
- **Output_Gate**: The validation rule requiring at least one qualifying condition before an output note is created
- **Weekly_Synthesis**: A periodic review note summarizing enrichment activity, overdue drills, unresolved questions, and synthesis candidates
- **Explanation_Ladder**: A multi-resolution explanation block that compresses a concept into one-sentence, short-form, and teach-back versions
- **Misconception_Log**: A section or board entry recording common wrong beliefs and their corrections
- **Contrast_Pair**: A comparison between adjacent or easily confused concepts used to improve discrimination and transfer
- **Transfer_Drill**: A prompt requiring the concept to be applied in a new context, debugging situation, or build task
- **Understanding_Proof**: Concrete evidence that a concept can be explained, distinguished, applied, and used in an artifact

## Requirements

### Requirement 1: Schema Extension

**User Story:** As a vault owner, I want the existing frontmatter schema extended with capability-tracking fields, so that every concept note can carry track, mastery, drill, and evidence metadata without breaking existing notes.

#### Acceptance Criteria

1. THE Capability_Engine SHALL add the following frontmatter fields to the Canonical_Schema: `track`, `prerequisites`, `used_in`, `evidence`, `difficulty`, `mastery_level`, `mastery_score`, `last_drilled`, `next_drill`, `drill_interval`, `question_kind`, `question_status`, `output_kind`, `source_concepts`, `concepts`, `tracks`
2. WHEN new capability fields are added THEN THE Capability_Engine SHALL preserve all existing Canonical_Schema fields without modification
3. THE Capability_Engine SHALL use `mastery_level` for the text progression enum and SHALL NOT reuse the existing `mastery` property name
4. WHEN a `mastery_level` value is set THEN THE Capability_Engine SHALL accept only values from the set: `novice`, `familiar`, `proficient`, `expert`
5. WHEN a `track` value is set THEN THE Capability_Engine SHALL accept only values from the set: `ai`, `systems`, `algorithms`, `career`, `trading`
6. WHEN a `difficulty` value is set THEN THE Capability_Engine SHALL accept only integer values in the range 1 to 5
7. WHEN an `output_kind` value is set THEN THE Capability_Engine SHALL accept only values from the set: `portfolio-bullet`, `blog-draft`, `interview-story`, `demo-spec`, `project-brief`, `reusable-prompt`
8. WHEN a `question_kind` value is set THEN THE Capability_Engine SHALL accept only values from the set: `open`, `misconception`, `oral-exam`, `debugging`, `build`
9. WHEN a `question_status` value is set THEN THE Capability_Engine SHALL accept only values from the set: `open`, `active`, `resolved`
10. THE Capability_Engine SHALL register all new property names and types in `.obsidian/types.json`

### Requirement 2: Note Archetypes and Templates

**User Story:** As a vault owner, I want structured templates for each note archetype (concept, output, question, synthesis), so that new notes are created with correct frontmatter and consistent section structure.

#### Acceptance Criteria

1. THE Capability_Engine SHALL provide a Deep_Dive_Template at `30_Order/Templates/Capability/Deep Dive Template.md` containing sections: What It Is, Why It Matters, Mental Model, Formal Model, Real Example, Implementation, Failure Modes, Interview Angle, Related Projects, Drill Cards, Next Drill
2. THE Capability_Engine SHALL provide an Output_Template at `30_Order/Templates/Capability/Output Template.md` with frontmatter fields `type: output`, `output_kind`, `source_concepts`, and `track`
3. THE Capability_Engine SHALL provide a Synthesis_Template at `30_Order/Templates/Capability/Synthesis Template.md` with frontmatter fields `type: evergreen`, tag `synthesis`, `concepts`, and `tracks`
4. THE Capability_Engine SHALL provide a Question_Bank_Template, Field_OS_Template, Depth_Ladder_Template, and Clipping_Distill_Template under `30_Order/Templates/Capability/`
5. WHEN a Deep_Dive_Template is instantiated THEN THE Capability_Engine SHALL set `status: seed` and `mastery_level: novice` as defaults
6. THE Capability_Engine SHALL include an Explanation_Ladder in the Deep_Dive_Template with sections for at least: one-sentence version, 30-second version, and teach-it-to-a-beginner version
7. THE Capability_Engine SHALL include sections for `Contrast With`, `Diagnostic Questions`, and `Source Anchors` in the Deep_Dive_Template

### Requirement 3: Growth Rule Enforcement

**User Story:** As a vault owner, I want concept notes to follow a staged enrichment policy, so that notes grow incrementally from seed to tree without requiring all sections immediately.

#### Acceptance Criteria

1. WHEN a Concept_Note has `status: seed` THEN THE Capability_Engine SHALL require at minimum the sections: What It Is, Why It Matters, and one Real Example
2. WHEN a Concept_Note has `status: sprout` THEN THE Capability_Engine SHALL require the seed sections plus: Mental Model, Implementation, and one Failure Mode
3. WHEN a Concept_Note has `status: tree` THEN THE Capability_Engine SHALL require all sprout sections plus: Formal Model, Interview Angle, Related Projects, Drill Cards, and at least one entry in the `evidence` field
4. WHEN a Concept_Note has `status: seed` THEN THE Capability_Engine SHALL also require a one-sentence explanation and at least one Source Anchor
5. WHEN a Concept_Note has `status: sprout` THEN THE Capability_Engine SHALL also require one Contrast_Pair and at least two Diagnostic Questions
6. WHEN a Concept_Note has `status: tree` THEN THE Capability_Engine SHALL also require a teach-it-to-a-beginner explanation and at least one Understanding_Proof

### Requirement 4: Drill Scheduling

**User Story:** As a vault owner, I want an automated drill scheduling system based on difficulty and mastery, so that I review concepts at optimal intervals without depending on the Spaced Repetition plugin.

#### Acceptance Criteria

1. THE Capability_Engine SHALL compute `next_drill` using the formula: `next_drill = last_drilled + clamp(round(drill_interval × mastery_multiplier), 3, 180)`
2. THE Capability_Engine SHALL assign default `drill_interval` values based on difficulty: difficulty 1 = 21 days, difficulty 2 = 14 days, difficulty 3 = 10 days, difficulty 4 = 7 days, difficulty 5 = 5 days
3. THE Capability_Engine SHALL apply Mastery_Multiplier values: `novice` = 1.0, `familiar` = 1.25, `proficient` = 1.6, `expert` = 2.0
4. WHEN `last_drilled` is updated on a Concept_Note THEN THE Capability_Engine SHALL recompute `next_drill` using the scheduling formula
5. THE Capability_Engine SHALL clamp the computed interval to a minimum of 3 days and a maximum of 180 days
6. WHEN the Spaced Repetition plugin is later enabled THEN THE Capability_Engine SHALL remain compatible by using `#cards` tags and `::` separators inside `## Drill Cards` sections

### Requirement 5: Output System and Gate

**User Story:** As a vault owner, I want an evidence-first output system with a validation gate, so that output notes are only created when backed by real capability evidence.

#### Acceptance Criteria

1. THE Capability_Engine SHALL store Output_Notes in `60_Claude/45_Outputs/`
2. WHEN an Output_Note is created THEN THE Capability_Engine SHALL require at least one of: `mastery_level` of `familiar` or higher on a linked source concept, a linked project under `used_in`, or a linked artifact under `evidence`
3. WHEN an Output_Note is created THEN THE Capability_Engine SHALL require a non-empty `source_concepts` field linking back to the originating Concept_Notes
4. THE Capability_Engine SHALL support the following `output_kind` values: `portfolio-bullet`, `blog-draft`, `interview-story`, `demo-spec`, `project-brief`, `reusable-prompt`
5. WHEN a Concept_Note is linked as a source for an Output_Note THEN THE Capability_Engine SHALL add the Output_Note to the Concept_Note's `evidence` field

### Requirement 6: Cross-Domain Synthesis

**User Story:** As a vault owner, I want synthesis notes that bridge concepts across multiple tracks, so that I can identify and articulate cross-domain transfer and insight.

#### Acceptance Criteria

1. THE Capability_Engine SHALL store Synthesis_Notes in `60_Claude/20_Distilled_Notes/Synthesis/`
2. WHEN a Synthesis_Note is created THEN THE Capability_Engine SHALL require the `concepts` field to contain at least two wikilinks
3. WHEN a Synthesis_Note is created THEN THE Capability_Engine SHALL require the `tracks` field to contain at least two distinct track values
4. IF a Synthesis_Note links concepts from fewer than two tracks THEN THE Capability_Engine SHALL reject the note as invalid synthesis

### Requirement 7: Per-Track Field OS Dashboards

**User Story:** As a vault owner, I want a Field OS dashboard for each track, so that I have a single control center showing capability summary, overdue drills, recent progress, open questions, outputs, and synthesis notes per track.

#### Acceptance Criteria

1. THE Capability_Engine SHALL create a Field_OS dashboard for each of the five tracks at `60_Claude/60_Indexes/Field OS/{Track} Field OS.md`
2. WHEN a Field_OS dashboard is rendered THEN THE Capability_Engine SHALL display: capability summary, overdue drills, recent progress, open questions, outputs produced, synthesis notes touching the track, and links to the track's Depth_Ladder and Question_Bank
3. THE Capability_Engine SHALL implement Field_OS dashboards using Dataview queries filtered by the `track` field

### Requirement 8: Per-Track Depth Ladders

**User Story:** As a vault owner, I want a Depth Ladder for each track modeled after the BOOM Board pattern, so that I have curated refresher sequences and drill queues for each domain.

#### Acceptance Criteria

1. THE Capability_Engine SHALL create a Depth_Ladder for each of the five tracks at `60_Claude/60_Indexes/Field OS/{Track} Depth Ladder.md`
2. WHEN a Depth_Ladder is rendered THEN THE Capability_Engine SHALL display sections for: core concepts, 30-minute refresher, 2-hour technical refresher, deep relearning pass, overdue drills, and all tracked concepts
3. THE Capability_Engine SHALL implement refresher sequences as curated wikilink lists, not auto-generated content
4. THE Capability_Engine SHALL implement the overdue drills and all tracked concepts sections using Dataview queries
5. THE Capability_Engine SHALL include at least one compare-or-discriminate segment in each Depth_Ladder so that adjacent concepts are reviewed in contrast rather than isolation

### Requirement 9: Per-Track Question Banks

**User Story:** As a vault owner, I want a Question Bank for each track, so that I can organize open questions, misconceptions, oral exam prompts, debugging drills, and build prompts per domain.

#### Acceptance Criteria

1. THE Capability_Engine SHALL create a Question_Bank for each of the five tracks at `60_Claude/60_Indexes/Field OS/{Track} Question Bank.md`
2. WHEN a Question_Bank is rendered THEN THE Capability_Engine SHALL display sections for: open questions, misconceptions, oral exam prompts, debugging drills, build prompts, and resolved learnings
3. THE Capability_Engine SHALL use Dataview queries filtered by `track` and `question_kind` to populate Question_Bank sections
4. THE Capability_Engine SHALL prefer board-level entries over separate note files for questions that do not persist across sessions

### Requirement 10: Global Dashboards

**User Story:** As a vault owner, I want global Capability, Question, and Proof dashboards, so that I can see vault-wide analytics on mastery distribution, open questions, and evidence coverage.

#### Acceptance Criteria

1. THE Capability_Engine SHALL create a Capability_Dashboard at `60_Claude/60_Indexes/Capability Dashboard.md` displaying: global count of tracked concepts, mastery distribution, overdue drills, recently enriched notes, and notes missing evidence
2. THE Capability_Engine SHALL create a Question_Dashboard at `60_Claude/60_Indexes/Question Dashboard.md` displaying: open durable questions by track, unresolved misconceptions, and debugging prompts backlog
3. THE Capability_Engine SHALL create a Proof_Dashboard at `60_Claude/60_Indexes/Proof Dashboard.md` displaying: outputs produced by track, concepts with no evidence, and in-progress interview stories, portfolio bullets, and demos
4. THE Capability_Engine SHALL implement all global dashboards using Dataview queries

### Requirement 11: Editable Base Registries

**User Story:** As a vault owner, I want editable `.base` file registries for capabilities, questions, and outputs, so that I can triage and maintain metadata from a table view without editing individual note files.

#### Acceptance Criteria

1. THE Capability_Engine SHALL create a Capability_Registry at `60_Claude/60_Indexes/Bases/Capability Registry.base` for all tracked Concept_Notes, sortable by `difficulty`, `mastery_level`, and `next_drill`, with editable `track`, `mastery_level`, and `drill_interval` fields
2. THE Capability_Engine SHALL create a Question_Triage at `60_Claude/60_Indexes/Bases/Question Triage.base` for durable Question_Notes, filterable by `track`, `question_kind`, and `question_status`
3. THE Capability_Engine SHALL create an Output_Pipeline at `60_Claude/60_Indexes/Bases/Output Pipeline.base` for all Output_Notes, tracking `status`, `output_kind`, and `track`

### Requirement 12: Ingestion Pipeline

**User Story:** As a vault owner, I want a structured three-stage ingestion pipeline for web clippings, so that raw captures flow cleanly from clipping to source summary to durable concept or output.

#### Acceptance Criteria

1. WHEN a raw clipping is captured THEN THE Capability_Engine SHALL store it in `60_Claude/05_Clippings/` with `type: input`, `source_url`, and `track` when obvious
2. THE Capability_Engine SHALL treat all files in `60_Claude/05_Clippings/` as immutable after initial capture
3. WHEN a clipping is distilled THEN THE Capability_Engine SHALL create a source-grounded summary in `60_Claude/30_Source_Summaries/` preserving source lineage and linking to relevant concepts, projects, or track boards
4. WHEN distilled information is reusable THEN THE Capability_Engine SHALL promote it to a durable Concept_Note in `40_Resources/` or `60_Claude/20_Distilled_Notes/`, or to an Output_Note in `60_Claude/45_Outputs/`
5. IF distilled information is not reusable THEN THE Capability_Engine SHALL retain it as a Source_Summary without promotion
6. WHEN distilled information is promoted to a durable Concept_Note THEN THE Capability_Engine SHALL preserve at least one explicit Source Anchor back to the originating Source_Summary or feeder note

### Requirement 13: Information Architecture

**User Story:** As a vault owner, I want all new Capability Engine content placed within the existing folder structure, so that no new top-level folders are created and the vault shape is preserved.

#### Acceptance Criteria

1. THE Capability_Engine SHALL place all templates under `30_Order/Templates/Capability/`
2. THE Capability_Engine SHALL place all guide and reference documents under `40_Resources/Capability/`
3. THE Capability_Engine SHALL place all dashboards, depth ladders, question banks, and field OS boards under `60_Claude/60_Indexes/`
4. THE Capability_Engine SHALL place all base files under `60_Claude/60_Indexes/Bases/`
5. THE Capability_Engine SHALL place all output notes under `60_Claude/45_Outputs/`
6. THE Capability_Engine SHALL place all synthesis notes under `60_Claude/20_Distilled_Notes/Synthesis/`
7. THE Capability_Engine SHALL place all weekly synthesis reviews under `60_Claude/50_Reviews/Weekly Synthesis/`
8. THE Capability_Engine SHALL NOT create any new top-level folders

### Requirement 14: Weekly Synthesis Review

**User Story:** As a vault owner, I want a weekly synthesis review note generated automatically, so that I can track enrichment activity, overdue drills, unresolved questions, and synthesis candidates each week.

#### Acceptance Criteria

1. THE Capability_Engine SHALL generate Weekly_Synthesis notes in `60_Claude/50_Reviews/Weekly Synthesis/`
2. WHEN a Weekly_Synthesis is generated THEN THE Capability_Engine SHALL include sections for: concepts enriched this week, overdue drills, unresolved questions, outputs created, and 1-3 synthesis candidates worth pursuing
3. WHEN computing overdue drills THEN THE Capability_Engine SHALL identify all Concept_Notes where `next_drill` is earlier than the current date

### Requirement 15: AI Role Model

**User Story:** As a vault owner, I want five defined AI roles (Teacher, Examiner, Builder, Connector, Critic) as portable prompt patterns, so that concept enrichment follows consistent, role-specific behavior regardless of the AI tool used.

#### Acceptance Criteria

1. THE Capability_Engine SHALL define five AI roles: Teacher, Examiner, Builder, Connector, Critic
2. WHEN the Teacher role enriches a Concept_Note THEN THE Capability_Engine SHALL expand the sections: What It Is, Why It Matters, Mental Model, Formal Model
3. WHEN the Examiner role enriches a Concept_Note THEN THE Capability_Engine SHALL add: oral exam prompts, drill cards, debugging drills, misconception checks
4. WHEN the Builder role enriches a Concept_Note THEN THE Capability_Engine SHALL add: implementation examples, related projects, demo specs, output candidates
5. WHEN the Connector role enriches a Concept_Note THEN THE Capability_Engine SHALL add: prerequisites, used_in links, synthesis candidates, cross-track links
6. WHEN the Critic role reviews a Concept_Note THEN THE Capability_Engine SHALL identify: weak explanations, missing evidence, hand-wavy outputs, notes with no practical leverage
7. THE Capability_Engine SHALL implement AI roles as portable prompt patterns usable across Kiro specs, AGENTS.md, and optional `.claude/skills/` files

### Requirement 16: Migration Phasing

**User Story:** As a vault owner, I want the Capability Engine rolled out in four phases, so that the system is built incrementally without destabilizing the existing vault.

#### Acceptance Criteria

1. WHEN Phase 0 (Schema Hardening) is executed THEN THE Capability_Engine SHALL update `Vault Operating System.md`, update `.obsidian/types.json`, and add all capability templates
2. WHEN Phase 1 (Control Surfaces) is executed THEN THE Capability_Engine SHALL create all dashboards, field OS boards, depth ladders, question banks, and base files
3. WHEN Phase 2 (Seed the Engine) is executed THEN THE Capability_Engine SHALL enrich 20-30 flagship notes across UROP systems, AI workflow, core CS concepts, career, and trading
4. WHEN Phase 3 (Output Pass) is executed THEN THE Capability_Engine SHALL generate interview stories, portfolio bullets, reusable prompts, and project briefs from enriched concepts
5. WHEN Phase 4 (Weekly Cadence) is executed THEN THE Capability_Engine SHALL establish the weekly synthesis review workflow

### Requirement 17: Guardrails and Safety

**User Story:** As a vault owner, I want explicit guardrails against file explosion, metadata drift, output spam, and AI clutter, so that the Capability Engine maintains vault quality over time.

#### Acceptance Criteria

1. THE Capability_Engine SHALL prefer board-level entries over separate note files for transient questions and prompts
2. THE Capability_Engine SHALL enforce "search before create" for all AI-initiated note creation
3. THE Capability_Engine SHALL prefer enriching existing notes over creating new notes
4. THE Capability_Engine SHALL NOT modify files under `60_Claude/05_Clippings/` after initial capture
5. THE Capability_Engine SHALL NOT create hard dependencies on plugins that are installed but disabled (QuickAdd, Spaced Repetition, Git, Periodic Notes)
6. WHEN an Output_Note is created without meeting the Output_Gate criteria THEN THE Capability_Engine SHALL reject the creation
7. THE Capability_Engine SHALL use the Vault Health Dashboard to surface metadata drift and orphan notes
8. THE Capability_Engine SHALL NOT perform broad structural rewrites inside `10_UMN/`, but MAY selectively enrich flagship notes or create distilled mirror notes when they materially improve long-term understanding

### Requirement 18: Explanation Ladder and Teach-Back

**User Story:** As a vault owner, I want every high-value concept to be expressible at multiple levels of compression, so that I can prove I understand it instead of only recognizing it.

#### Acceptance Criteria

1. THE Capability_Engine SHALL define an Explanation_Ladder for high-value Concept_Notes
2. WHEN a high-value Concept_Note is enriched THEN THE Capability_Engine SHALL include a one-sentence version of the concept
3. WHEN a high-value Concept_Note reaches `status: sprout` or `status: tree` THEN THE Capability_Engine SHALL include a 30-second explanation in plain language
4. WHEN a high-value Concept_Note reaches `status: tree` THEN THE Capability_Engine SHALL include a teach-it-to-a-beginner explanation that avoids relying on undefined jargon

### Requirement 19: Misconceptions and Contrastive Learning

**User Story:** As a vault owner, I want concepts to record misconceptions and nearby confusions, so that I can distinguish similar ideas instead of memorizing shallow summaries.

#### Acceptance Criteria

1. THE Capability_Engine SHALL support a Misconception_Log at either the Concept_Note level or the Question_Bank level
2. WHEN a Concept_Note is enriched beyond `status: seed` THEN THE Capability_Engine SHALL include at least one Contrast_Pair or `Contrast With` entry linking it to a nearby concept
3. WHEN a misconception is recorded THEN THE Capability_Engine SHALL store both the incorrect belief and its corrected explanation
4. THE Capability_Engine SHALL surface unresolved misconceptions in the relevant Question_Bank or Question_Dashboard

### Requirement 20: Transfer Drills and Proof of Understanding

**User Story:** As a vault owner, I want every serious concept to be tested through application, so that the vault measures transfer and execution rather than recognition alone.

#### Acceptance Criteria

1. THE Capability_Engine SHALL support Transfer_Drills for high-value Concept_Notes
2. WHEN a Concept_Note reaches `status: sprout` THEN THE Capability_Engine SHALL include at least one Diagnostic Question or Transfer_Drill
3. WHEN a Concept_Note reaches `status: tree` THEN THE Capability_Engine SHALL include at least one Transfer_Drill requiring debugging, building, comparison, or problem-solving
4. WHEN a Concept_Note is marked as deeply understood THEN THE Capability_Engine SHALL require an Understanding_Proof in the form of at least one of: solved problem, implementation, demo, teach-back artifact, interview story, or linked output

### Requirement 21: Selective Feeder-Layer Enrichment

**User Story:** As a vault owner, I want school notes to remain stable overall while still allowing the most important ones to graduate into the long-term system, so that coursework can compound into durable capability.

#### Acceptance Criteria

1. THE Capability_Engine SHALL treat `10_UMN/` as a feeder layer rather than the primary long-term destination for capability notes
2. THE Capability_Engine SHALL NOT perform bulk restructuring or broad rewriting across `10_UMN/`
3. WHEN a `10_UMN/` note clearly supports a long-term track THEN THE Capability_Engine MAY selectively enrich that note with metadata or understanding sections
4. WHEN direct modification of a feeder note is undesirable THEN THE Capability_Engine SHALL allow creation of a distilled mirror note in `40_Resources/` or `60_Claude/20_Distilled_Notes/` with backlinks to the original feeder note
