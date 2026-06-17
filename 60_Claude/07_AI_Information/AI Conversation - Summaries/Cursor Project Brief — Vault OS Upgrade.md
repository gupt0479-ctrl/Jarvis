---
type: evergreen
status: sprout
created: 2026-05-31
updated: 2026-05-31
tags:
  - system
  - ai-agents
  - cursor
  - project-brief
notes:
  - "[[AI_CONTEXT]]"
  - "[[Vault Rules — Complete AI Ruleset]]"
  - "[[Note Writing System — Audit and Roadmap (2026-05-31)]]"
---
# Cursor Project Brief — Vault OS Upgrade

==This is a complete, self-contained brief for Cursor Opus 4.8. Read every section before touching a single file. The goal is to build an operating system that any AI agent can use correctly 3 months from now, starting cold.==

---

## Who You Are Working With

Anant Gupta is a learning developer building toward technical independence — agentic AI, ML pipelines, full-stack apps, trading systems, UROP research at UMN, and coursework. He uses this Obsidian vault, called **Jarvis**, as his primary operating system for all work. Every project, note, learning trail, career artifact, and system doc lives here.

He is working with multiple AI tools simultaneously: Claude (via Cowork/MCP), Cursor (you), Kiro, and Obsidian Copilot. All of them need to write notes that are consistent with each other and with his standards. That consistency currently does not exist, which is the problem you are solving.

---

## Your Available Tools

- **Obsidian MCP** (`obsidian-mcp-server` on `http://127.0.0.1:27123`) — read vault notes, search vault, write notes. Use this for all vault reads and writes.
- **Context7** — fetch current documentation for libraries, frameworks, and tools by slug. Primary tool for researching plugin features.
- **Playwright** — browser automation for fetching pages Context7 doesn't cover. Use for GitHub READMEs, plugin docs sites, or any page requiring JavaScript rendering.
- **GitHub connection** (fine-grained token) — access plugin repositories directly if needed.
- **Standard filesystem** — direct read/write to `D:\Users\_Anant\10_Areas\Documents\Jarvis\` (the vault root).

---

## Orientation — Read These Files First, In This Order

Before doing any work, read these files in full. Do not skip any.

1. `AGENTS.md` — root behavioral rules and write contract
2. `60_Claude/07_AI_Information/Vault Rules — Complete AI Ruleset.md` — the governing ruleset (all 14 parts)
3. `60_Claude/07_AI_Information/Note Writing System — Audit and Roadmap (2026-05-31).md` — the full audit of what went wrong and what gaps remain
4. `HUMAN_WRITING.md` — the voice and writing quality standard
5. `60_Claude/07_AI_Information/Jarvis Writing and Formatting.md` — Obsidian-specific formatting rules
6. `60_Claude/07_AI_Information/Plugins.md` — current plugin operating summary
7. `40_Resources/Obsidian/Plugins/00 Plugin Reference Index.md` — plugin workflow map
8. `40_Resources/Obsidian/Plugins/Plugin Gaps Recommendations and Verification.md` — what is unresolved and risky
9. `AI_CONTEXT.md` — live state manifest
10. `00_Dashboard.md` — current control panel

After reading, read 3–5 real vault notes from `10_Areas/UMN/Previous Classes/` to anchor your understanding of what a well-formatted Jarvis note actually looks like in practice. These are the gold standard. The instruction files describe what they do; the real notes show it.

---

## The Problem — Specifically

This is not a vague "improve the system" brief. These are the named gaps from the post-session audit. Build against these.

### Gap 1: Plugin docs exist but have no depth

Every file in `40_Resources/Obsidian/Plugins/` was written on 2026-05-15 with `status: sprout`. They document plugin features at the level of a README summary. They do not answer:
- What does this plugin do at a mechanistic level in this vault?
- What are the exact settings configured right now?
- How does this plugin integrate with the others (e.g., SR + Dataview, Templater + QuickAdd)?
- What should an AI agent specifically write or not write because of this plugin?
- What are the failure modes?
- What are real examples from actual vault notes?

An agent reading `Spaced Repetition and Learning Loops.md` today gets config values and generic rules. It does not get: "the MGMT 3001 notes demonstrate this exact pattern — here is what a complete flashcard section looks like and why." That concreteness is missing everywhere.

### Gap 2: .cursor/rules is almost empty

`.cursor/rules/` has two files:
- `workspace-context.mdc` — 8 lines saying "read AGENTS.md"
- `human-writing.mdc` — 8 lines saying "read HUMAN_WRITING.md"

This is not a ruleset. Cursor has no rules governing: where to write notes, what frontmatter schema to use, what blank lines rule applies, which plugins to invoke for which note types, what security constraints exist, or what the routing table is. Every session Cursor starts cold with zero behavioral guidance beyond "go read some files."

The `.cursor/rules/` directory should enforce behavior automatically, not delegate it to file-reading that may or may not happen.

### Gap 3: No "why" document

There is no document that answers the foundational questions: Why does Anant write notes at all? What makes a note worth writing versus not writing? What is the use case this note serves 3 months from now? Who is the reader of this note (future-Anant, a future AI agent, a flashcard review session)?

Without this, AI agents write notes that are technically formatted but philosophically wrong — captures without a retrieval path, summaries without a use case, structure without purpose.

### Gap 4: Templates are empty shells

Every template in `30_Order/Templates/` needs to be rewritten. Current state:
- `Clipping Distill Template.md` — 5 headings with zero guidance under any of them. Missing `## Full Content`, `## Flashcards`, Tasks format
- `Week Template.md` — has section names but no content guidance. Does not teach the `## Lecture-to-textbook synthesis` pattern that appears in every good MGMT 3001 note
- `Concept Template.md` — has `mastery (1/10): 0` which is invalid YAML
- `For Evergreen.md` and `For Progress.md` — frontmatter only, no body
- `Textbook Template.md` — one heading: `# Chapter - `. That is the entire file.

Templates are the single most important quality control mechanism. An agent without a good template invents structure. Every invented structure is a source of inconsistency.

### Gap 5: Plugin integration is not wired into workflows

The workflows in `30_Order/Workflows/` describe note moves at an abstract level (Clippings → Source Summaries → Distilled Notes). They do not say: at this step, run Excalidraw if the source has diagrams. At this step, add flashcards using `#cards/[track]`. At this step, write LaTeX for any mathematical expression. At this step, create a Dataview query if the output should be tracked.

Plugin integration is currently documented as a separate concern. It needs to be embedded in the workflows themselves.

---

## The Deliverables — Ordered by Priority

### Priority 1: Deep Plugin Reference Notes

**Location:** `40_Resources/Obsidian/Plugins/` (update existing files, do not create new ones unless a plugin has no file)

**For each plugin**, write a note that contains:

1. **What it does — mechanism, not feature list.** One sentence that says exactly what problem this plugin solves in this vault. "Templater prevents agents from inventing frontmatter by providing pre-built note structures for each folder." Not: "Templater is a powerful template plugin."

2. **Exact current settings.** Read the plugin's `data.json` from `.obsidian/plugins/[plugin-name]/data.json`. Document every setting that affects agent behavior. Skip cosmetic settings. For sensitive plugins (Copilot, Local REST API, QuickAdd AI), name that a secrets field exists but do not expose its value.

3. **Integration map.** How does this plugin interact with the others? Write this as: "Plugin A produces X, which Plugin B reads as Y." Example: "Spaced Repetition reads bold and highlight markers that Jarvis Writing and Formatting defines — every `**term**` in a `#cards`-tagged section becomes a cloze automatically. This is why bold is not general emphasis here."

4. **Agent rules — specific actions.** Not "use this plugin when helpful." Instead: "When creating a PDF source summary note, always end with `## Flashcards #cards/[track]`. When writing a concept with mathematical notation, always use `$...$` inline. When a note should appear in a dashboard, always use the exact frontmatter field the Dataview query reads."

5. **Failure modes.** What happens when an agent uses this plugin wrong? Name the failure. "If you use `**bold**` for general emphasis in a `#cards` section, every bolded word creates an unwanted cloze card. SR will surface junk in review." This is more useful than a rule in isolation.

6. **Gold standard example.** Link to one or two real vault notes that use this plugin correctly. Not invented examples. Read actual notes from `10_Areas/UMN/`, `60_Claude/`, or `40_Resources/` to find real usage. The MGMT 3001 week notes and textbook chapters are the best source.

7. **Verified open state.** Confirm what is still unknown or unresolved and name it explicitly. Do not leave "needs verification" as a vague flag — say what question it is waiting on.

**Plugin research method for each plugin:**
- Step 1: Read the plugin's `data.json` for exact settings
- Step 2: Use Context7 to fetch the plugin's documentation (try by npm package name or GitHub repo slug)
- Step 3: If Context7 doesn't have it, use Playwright to fetch the GitHub README or official docs site
- Step 4: Read 2–3 real vault notes that use the plugin to understand actual usage patterns
- Step 5: Write the doc — mechanism first, settings second, integration third, rules fourth, failure modes fifth, example sixth

**Plugins to cover** (all need updating; prioritize these first):

High-impact, currently underused:
1. **QuickAdd** — installed, 0 choices configured, hotkey exists; needs a proposed capture menu
2. **Excalidraw** — installed, lazy-loaded; needs diagram integration pattern for PDF workflow
3. **Canvas** — core plugin, zero usage documented anywhere
4. **Spaced Repetition** — configured but bold/highlight cloze interaction with agent formatting is underdocumented
5. **Omnisearch** — PDF indexing disabled, Text Extractor decision needed

Active and needs more depth:
6. **Dataview** — good start; needs canonical query patterns for each dashboard type in this vault
7. **Tasks** — configured; needs the emoji format documented with complete examples, due/priority conventions
8. **Templater** — configured; needs the folder → template map documented with agent behavior for each case
9. **Periodic Notes** — configured; needs the review note structure and what happens to the output
10. **Kanban** — used for habits; needs lane naming conventions and card-to-note linking pattern

Supporting plugins:
11. **Latex Suite** — snippets likely exist but are undocumented; research default snippets + recommend vault-specific ones
12. **Hover Editor** — configured; needs the "write headings and first lines for good hover previews" rule with examples
13. **Copilot** — sensitive; document autonomy settings, memory location, and agent constraints without exposing keys
14. **Git** — configured with auto-push; document the dirty worktree risk and when agents should not trigger commits
15. **Local REST API** — insecure server enabled; document security posture and when agents should use MCP vs filesystem

### Priority 2: Note Philosophy — The Why

**Location:** `60_Claude/07_AI_Information/Why We Write Notes.md` (new file)

**This document answers the questions every future AI agent needs to answer before writing a note:**

**Section 1 — The Use Case Test**
A note is worth writing only if it passes one of these tests:
- Future retrieval: "Will future-Anant search for this and need it to appear?"
- Transfer: "Does this mechanism show up in a different context (course → interview, project → portfolio)?"
- Review: "Is this a concept worth practicing via spaced repetition?"
- Decision support: "Is this a decision I will revisit, and does the note capture why I chose what I chose?"
- Action: "Is this a task, next step, or open question that must be tracked?"

If a piece of information fails all five tests, it stays in `05_Clippings/` as raw source and does not become a note.

**Section 2 — The Reader Model**
Every note has a specific intended reader. Write for that reader, not for the feeling of having captured something.

The readers in this vault, and what each needs:
- **Future-Anant (3 months):** needs the mechanism, not the summary. Needs to know what he was confused about, what he understood, and what he still doesn't know.
- **Future AI agent:** needs structured frontmatter, verified wikilinks, plugin-compatible syntax, and concrete examples it can pattern-match against.
- **Spaced Repetition:** needs one well-formed question per card, mechanism-based answers, not label trivia.
- **Dataview:** needs clean, consistent frontmatter fields that match what the dashboard queries.
- **Obsidian graph:** needs meaningful wikilinks that reflect actual relationships, not reflexive linking.

**Section 3 — Note Types and Their Purpose**
For each note type in this vault, explain: what question does this note answer? What does it produce? When does an agent create it vs extend an existing one?

| Note type | Question it answers | When to create | When to extend |
|---|---|---|---|
| Source summary (`input`) | What did this source say, and what's worth keeping? | Once per source, when the source is worth keeping | Never — source summaries are fixed captures |
| Distilled note (`evergreen`) | What is the mechanism behind this concept? | When the concept recurs across multiple sources or contexts | When new evidence, examples, or contrasts arrive |
| Project note (`project`) | What is the current state and next action for this work? | When a project starts | At every meaningful milestone |
| Concept note (`concept`) | What does this term mean, how does it work, what's the failure mode? | When a concept recurs in coursework and will appear again | When mastery grows or examples accumulate |
| Flashcard set | What do I need to be able to recall on demand? | Only after distillation; never from raw source | When new cards are stronger than old ones |
| Review note (`review`) | What happened this week, what must change? | Periodically via Periodic Notes | Never — new review each time |

**Section 4 — The Compression Hierarchy**
Raw source → Source summary → Distilled note → Flashcard. Each step compresses further and serves a different purpose. An agent that jumps directly from raw source to flashcards skips the compression steps that make the cards meaningful.

**Section 5 — What Makes a Note Fail**
Name the failure modes concretely, derived from the audit:
- Note that captures everything but compresses nothing → unusable; user still needs to open the source
- Note with no wikilinks → invisible; Dataview and backlinks don't surface it
- Note with vague frontmatter → not queryable; dashboards miss it
- Note that sounds finished but carries partial understanding → fake confidence; misleads the reviewer
- Note with no flashcards → not retained; all the distillation work is wasted
- Note written without reading existing vault notes → invented conventions; inconsistent with the system

### Priority 3: .cursor/rules Enrichment

**Location:** `.cursor/rules/` (update existing + create new rule files)

Cursor MDC rule files support `alwaysApply: true` (applied to every chat) and `glob` patterns (applied when matching files are in context). Use both modes strategically.

**File 1: `workspace-context.mdc`** (update existing — expand from 8 lines)

Keep `alwaysApply: true`. Expand to include:
- The folder structure at a glance: what each of the 6 numbered folders is for
- The write contract: golden rules in list form (no vault root files, unsure → Inbox, search before creating)
- The routing table: most common note types and where they go
- Live state sources: where to check for current state (Dashboard, session log)
- When to stop and ask vs when to proceed

**File 2: `human-writing.mdc`** (update existing — expand from 8 lines)

Keep `alwaysApply: true`. Expand to include:
- The core test verbatim: delete any sentence that could appear in a productivity blog unchanged
- The 8 things a section must do (define, explain, show mechanism, contrast, give example, failure mode, show usage, state uncertainty)
- The anti-slop rules: mechanism > vibes, real context > generic examples, contrast > isolated summary, plain language > inflation
- The banned words list with substitution guidance
- The blank lines rule: `headerspace.css` handles spacing; zero blank lines except after callout

**File 3: `vault-behavior.mdc`** (new file, `alwaysApply: true`)

The behavioral rules that govern every action:
- Pre-flight checklist: what to read before writing
- Placement decisions: the routing table in compact form
- Frontmatter schema: canonical fields only, no invented keys, no duplicate keys, wikilinks verified before writing
- Quality gate: the 16-point checklist in compact form (reference the full version in Vault Rules)
- Safety constraints: never touch 50_Archive, 05_Clippings, .obsidian, .cursor, .claude, .git. Never expose plugin credentials. Never create vault root files.
- Session close: always append to session log after meaningful work

**File 4: `note-creation.mdc`** (new file, glob: `**/*.md`)

Applied when any markdown file is in context:
- Frontmatter schema with all valid field values
- Blank lines rule enforced with the specific violations to check
- Formatting markers: `==highlight==` one per section, `**bold**` on named concepts, `*italic:*` on sub-labels
- Plugin integration at creation time: which plugins fire on which note types (Templater, SR, Tasks, Dataview)
- Template matching: which template to use for which folder

**File 5: `plugin-rules.mdc`** (new file, `alwaysApply: true`)

A compact decision table: when to use each plugin and what the exact syntax is.
- Use Dataview when the list should stay current from metadata
- Use Tasks when there is a real action with a due date or review state
- Use Kanban when work has lanes and status cards
- Use Excalidraw when spatial layout explains the concept (arrows, flows, system diagrams)
- Use SR flashcards only after the concept is understood and distilled
- Use LaTeX for any mathematical expression
- Use Templater-matching frontmatter for every note created outside Obsidian

### Priority 4: Template Enrichment

**Location:** `30_Order/Templates/` (update existing files only — do not create new template names)

**For each template**, the update must contain:
1. Complete frontmatter with every canonical field and a comment explaining valid values
2. A one-line description under each heading: "This section contains X. Aim for Y sentences/bullets."
3. Example content for the most important sections (commented out with `<!-- example: ... -->` or as placeholder text the user removes)
4. Formatting reminders inline: where to use highlights, bold, callouts, Tasks, flashcards
5. Plugin integration: the specific plugin syntax that belongs in each section

Templates to update, in priority order:

**`Clipping Distill Template.md`** — the most-used template. Must match the source ingestion structure in Part 9 of Vault Rules exactly:
- Frontmatter: `type: input`, `status: sprout`, `input_kind:`, `track:`, `source_note:`, `source_url:`
- `## Source` — one sentence: what it is, who produced it, stated purpose
- `## Key Claims` — bullets with `**bold**` on the key concept in each bullet
- `## Full Content` — `###` subheadings from source's actual section titles. This is where the complete extraction goes.
- `## Why It Matters` — connection to active vault work; no padding
- `## Links Into The Vault` — verified wikilinks; stubs labeled `(to create)`
- `## Open Questions` — `- [ ]` Tasks format only
- `## Flashcards` — `#cards/[track]`, 3–5 minimum, mechanisms not labels

**`Week Template.md`** — for MGMT, CSCI, and all future courses. Must teach the synthesis pattern:
- Add `## Lecture-to-textbook synthesis` as a named section with: ==definition anchor==, `*Mechanism:*` label, lecture example, textbook connection with wikilinks, `> [!WARNING]` and `> [!SUMMARY]` callouts
- Add content guidance under every heading
- Remove the existing vague structure; replace with what the real MGMT 3001 notes demonstrate

**`Concept Template.md`** — fix the invalid YAML and add capability fields:
- Remove `mastery (1/10): 0` (invalid YAML — parentheses in key name)
- Add `track:`, `prerequisites:`, `used_in:`, `evidence:` to frontmatter
- Add `## One-Line Answer` section with instruction
- Add `## Mechanism` section: how it works, not just what it is
- Add `## Failure Modes / Misconceptions` section
- Add `## Evidence From This Vault` section: links to notes where this concept appeared
- Fix flashcard section: add `#cards/[track]` tag and formatting instructions

**`For Evergreen.md`** — add actual body structure:
- `## Core Claim` — the single most important thing this note establishes
- `## Mechanism` — how it works
- `## Why This Matters Here` — connection to active work in Jarvis
- `## Failure Modes` — where this breaks or gets confused
- `## Evidence` — sources and vault notes that support this
- `## Related` — wikilinks to nearby concepts

**`For Progress.md`** — add project body structure:
- `## Goal` — one sentence
- `## Current State` — what is true right now
- `## Next Action` — the single next step (also in `next:` frontmatter)
- `## Open Questions` — Tasks format
- `## Log` — dated entries appended over time, not rewritten

**`Textbook Template.md`** — expand from a single heading:
- Same structure as Clipping Distill but with `input_kind: textbook`
- `## Chapter Summary` — one-paragraph compression
- `## Key Concepts` — bold each concept, link to existing concept notes
- `## Examples Worth Keeping` — real worked examples from the chapter
- `## Connections` — how this chapter connects to lectures, projects, or other resources
- `## Flashcards` — required at the end

---

## Execution Method — Step by Step

### How to Research Plugins

For each plugin in Priority 1:

```
Step 1 — Read data.json
Read .obsidian/plugins/[plugin-name]/data.json
Note: config sections, enabled features, security-sensitive fields
Do not copy credential values

Step 2 — Fetch documentation
Try: context7.resolve_library_id with the plugin's npm name or GitHub repo name
If found: context7.get_library_docs for the relevant sections
If not found: use Playwright to navigate to the plugin's GitHub README

Step 3 — Read real vault usage
Find 2–3 actual vault notes that use this plugin
The MGMT 3001 notes are the best source for SR/formatting/Templates
60_Claude/10_Source_Summaries/ for ingestion workflow
40_Resources/ for Dataview and reference structure

Step 4 — Write the doc
Lead with the mechanism sentence
Then settings (from data.json)
Then integration map (plugin A → plugin B relationships)
Then agent rules (specific actions, not vague guidance)
Then failure modes (named errors)
Then example (link to a real vault note)
Then open questions (what is still unresolved, as a specific question)
```

### How to Write Rule Files

For each `.cursor/rules/` MDC file:

```
Requirement: alwaysApply: true for behavioral rules
Requirement: glob pattern for file-type-specific rules
Content: rules in positive form (what to do, not just what not to do)
Format: use tables where decision logic is binary; use numbered steps where order matters
Length: long enough to be complete, short enough to be read every session
Test: could a cold-start Cursor agent follow this file without reading any other doc?
```

### How to Validate a Template

Before saving a template:
1. Does it match the structure in Vault Rules Part 9 (for source notes) or the note type rules?
2. Is the frontmatter schema exactly right — no invented fields, no duplicate keys, valid YAML?
3. Does each section heading have a description line? Does at least one section have example content?
4. Are the plugin integration points marked? (SR flashcards, Tasks format, LaTeX placeholders)
5. If the template is for a note type that has gold standard examples in the vault, does the template match that example's structure?

---

## Quality Standards

### For Plugin Docs

A plugin doc is complete when:
- An AI agent reading only that doc knows exactly how to use the plugin in this vault without reading any other file
- The failure modes section would have prevented the mistakes named in the audit
- The example section links to at least one real vault note, not an invented one
- The settings section matches what is actually in data.json right now

### For .cursor/rules Files

A rule file is complete when:
- Cursor starts a cold session and the rules enforce behavior without the user needing to give instructions
- The routing table is present and unambiguous
- The frontmatter schema is present and complete
- The quality gate is present in compact form
- Security constraints are explicit

### For Templates

A template is complete when:
- An agent creating a note from this template produces a note that passes the 16-point quality gate on the first attempt
- Every heading has a description
- The frontmatter has no invalid YAML and uses only canonical fields
- The flashcard section is present (for source/concept/class notes) with correct syntax
- At least one gold standard example note is linked

### For the Why Document

Complete when:
- A future AI agent reads it and knows whether to write a note for any given piece of information
- The failure modes section names what a note looks like when it fails each test
- The note types table is complete
- Real vault examples are linked throughout

---

## Output Locations Summary

| Deliverable | Location |
|---|---|
| Plugin docs | `40_Resources/Obsidian/Plugins/[existing filename].md` |
| Note philosophy doc | `60_Claude/07_AI_Information/Why We Write Notes.md` |
| Cursor rules | `.cursor/rules/[filename].mdc` |
| Updated templates | `30_Order/Templates/[existing path]/[existing filename].md` |
| Session log entry | `60_Claude/07_AI_Information/Session Logs/log.md` |

---

## What Not to Do

These are the mistakes that the audit named specifically. Do not repeat them.

- **Do not write docs before reading real vault notes.** The MGMT 3001 notes are the ground truth. Read them before writing any instruction file.
- **Do not write vague rules.** "Use Excalidraw when helpful" is not a rule. "When a source contains a diagram, flowchart, or system map, create `[Source] - Diagrams.excalidraw` in `10_Areas/Excalidraw/` and embed with `![[...]]`" is a rule.
- **Do not write blank-line errors.** The headerspace.css snippet handles spacing. Zero blank lines between heading and content. Zero blank lines between sections.
- **Do not invent fields.** Only canonical frontmatter fields. No `source_status` unless the workflow explicitly requires it.
- **Do not write templates with only headings.** A template with a heading and no content guidance teaches nothing. Every heading needs a description or example.
- **Do not leave "needs verification" without a specific question.** Every unresolved item must be a question with a specific answer that can be verified.
- **Do not write AI slop.** Read HUMAN_WRITING.md. Every sentence must carry mechanism, example, contrast, or a real failure mode. Delete any sentence that could appear in a generic productivity guide.

---

## Session Close Protocol

After completing any deliverable:

1. Run the quality gate for that deliverable (listed above)
2. Verify every wikilink you added with a vault search
3. Append to `60_Claude/07_AI_Information/Session Logs/log.md`:

```
## [YYYY-MM-DD] [operation] | [title]
- What was created or changed
- Why it matters
- Open questions
- Next action if one exists
```

4. Update `updated:` in the frontmatter of any note that changed meaningfully

---

## The North Star

Three months from now, a new AI agent starts cold in this vault. It reads the `.cursor/rules/` files. It reads the plugin docs. It reads a template. It writes a note.

That note should be indistinguishable from notes Anant would write himself: correct frontmatter, right folder, right formatting markers, right plugin syntax, right content density, no blank line errors, flashcards that test mechanisms, wikilinks that actually exist.

Everything you build in this session is infrastructure for that agent. Not documentation for its own sake. Not files that say "be good." Infrastructure that makes correct behavior the default and wrong behavior difficult to accidentally produce.

If a piece of documentation could be read and still allow one of the 12 audit mistakes, it is not finished.
