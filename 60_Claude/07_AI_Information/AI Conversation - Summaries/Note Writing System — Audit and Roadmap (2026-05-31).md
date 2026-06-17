---
type: evergreen
status: sprout
created: 2026-05-31
updated: 2026-05-31
tags:
  - evergreen
  - system
  - writing
  - ai-agents
notes:
  - "[[Jarvis Writing and Formatting]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
  - "[[40_Resources/Obsidian/Plugins/00 Plugin Reference Index]]"
  - "[[60_Claude/07_AI_Information/Plugins]]"
---
# Note Writing System — Audit and Roadmap (2026-05-31)
==This document is the single source of truth about the current state of AI note-writing in this vault — what was built, what failed, what was fixed, and what must be built next.==
Written for any future Claude session. Read it before writing a single note. Every gap listed here represents a class of error that has already been made and must not be repeated.
## What This Document Is
A post-session audit covering ~5 days (2026-05-27 to 2026-05-31) of work on the PDF ingestion workflow, formatting instruction files, plugin integration, and template system. Cross-referenced with the full session log from `60_Claude/07_AI_Information/Session Logs/log.md`.
The vault is early. The architecture is sound. The instruction layer is not — it is full of empty headings, missing templates, and rules so vague that an agent reading them will produce mediocre notes. This document closes that gap.
## Session Timeline — What Was Done
**Day 1 (2026-05-31 morning):** Rewrote `/ingest-clipping` skill and `research-distiller` agent. Fixed broken folder paths (`30_Source_Summaries/` → `10_Source_Summaries/`, wrong session log path). Added `pypdf` Python extraction for PDFs on Windows (no `pdftoppm`). Created first trial ingest: `Quant Foundations (PDF).md`.
**Trial ingest round 1 failure:** Note had duplicate `notes:` key in frontmatter, 6 broken wikilinks to non-existent files, `---` horizontal rules between every section, blank lines everywhere, thin content that missed most of the PDF.
**Day 1 (2026-05-31 afternoon, round 2):** Rewrote the note. Fixed frontmatter. Removed `---` separators. Added source structure as `###` headings. Still: no ==highlights==, no `**bold**` on named concepts, no callouts, no *italic* labels, no flashcards, no math, no Tasks.
**Round 2 failure:** User showed the corrected note. Every line of content had no formatting. The note looked like plain prose. The vault's actual notes use =, `**`, `*`, and callouts throughout. The agent had not analyzed the vault's own notes before writing.
**Day 1 (2026-05-31 evening, round 3):** Analyzed MGMT 3001 notes. Derived the exact formatting pattern from real vault notes. Rewrote note with all formatting applied. Updated skill, agent, `Jarvis Writing and Formatting.md`, `HUMAN_WRITING.md`, `Spaced Repetition and Learning Loops.md`. Added blank lines rule, math notation requirement, flashcards section, Tasks for open questions.
**Round 3 failure:** Still had blank lines between sections. User pointed out: "no blank lines in my document, none." The zero-blank-line rule was not yet in the skill quality checklist at that point. Fixed.
**Final state:** All instruction files updated. Formatting rules codified. Quality checklist has 15 items. Templates: not yet touched.
## Mistakes Made — Named Precisely
These are not "areas for improvement." They are specific errors that degraded note quality. Every future agent should know them by name.
### 1. Writing before analyzing the vault
The agent wrote the Quant Foundations note before reading actual vault notes. It invented formatting conventions. The MGMT 3001 notes had the answers. **Rule: read 3–5 existing vault notes in the same category before writing any new note.**
### 2. Duplicate YAML key
`notes:` appeared twice in frontmatter. YAML takes the last value silently. The first block was lost. **Rule: scan frontmatter for duplicate keys before saving. One key, one value.**
### 3. Wikilinks to non-existent files
Linked to `[[20_Progress/Trading]]`, `[[Jane Street]]`, `[[Bayes' theorem]]`, `[[Expectation]]`, `[[Optimal Stopping]]` — none existed. Broke metadata. **Rule: verify every wikilink with Grep before writing. Unverified links go in the body only, labeled `(to create)`.**
### 4. `---` horizontal rules in the body
Used `---` between every section as a visual separator. `---` is YAML frontmatter terminator syntax. It does not mean "separator" in Obsidian note body. **Rule: `---` appears once, after the frontmatter, never in the body.**
### 5. Blank lines everywhere
Added blank lines: after `---`, between heading and content, between list items, between sections. The `headerspace.css` CSS snippet renders visual spacing for headings. Blank lines are not decoration — they are formatting errors in this vault. **Rule: zero blank lines except one after a callout/blockquote before prose.**
### 6. Thin content
Summarized instead of captured. The Quant Foundations PDF had 12 pages. The first note captured maybe 40% of the actual content. **Rule: every line in the source must appear in the note in some form. The note replaces the source — the user should never need to open the PDF again.**
### 7. No formatting markers
Wrote entirely plain prose. The vault uses =, `**`, `*`, and callouts for a reason: they are semantic markers that also feed the Spaced Repetition system. Bold and highlight clozes are ON. Every `**bold**` in a `#cards` section becomes an SR cloze automatically. Writing plain prose throws away the vault's learning infrastructure. **Rule: every named concept gets `**bold**` on introduction. Every major section gets one ==definition anchor==. Sub-category labels get `*italics*`.**
### 8. No flashcards section
MGMT 3001 notes all end with `## Flashcards #cards/MGMT`. PDF ingestion notes should end with `## Flashcards #cards/[track]`. Cards test mechanisms and contrasts, not acronym definitions. The Quant Foundations note went through 3 rewrites without a single flashcard. **Rule: every PDF ingestion note ends with `## Flashcards` section.**
### 9. No math notation
The Quant Foundations PDF is a quant/math document. Used `$E[X]$`, `$P(A|B)$` nowhere. Wrote "Expected value" when `$E[X]$` is the correct form. LaTeX Suite is installed and active. **Rule: any mathematical notation from the source uses LaTeX inline or display math.**
### 10. No Tasks format for open questions
`## Open Questions` section used prose paragraphs. The Tasks plugin is configured and active. Open questions are pending actions. **Rule: `## Open Questions` uses `- [ ]` Tasks format, not prose.**
### 11. Wrong `source_note` format
First wrote `source_note: "[[60_Claude/05_Clippings/PDFs/Quant Foundations]]"` (path, no extension). Correct is `source_note: "[[Quant Foundations.pdf]]"` (filename with extension). **Rule: `source_note` is the filename with extension, shortest unique form.**
### 12. Included `source_status: externally-sourced`
This field is not used in the vault's current note schema. It clutters frontmatter. **Rule: do not include `source_status` in PDF ingestion notes unless the workflow document explicitly requires it.**
## What Was Fixed — Concrete Changes Made
### Instruction files updated
- `HUMAN_WRITING.md` — added `## Vault Formatting Rules` section with blank lines rule and pointer to `[[Jarvis Writing and Formatting]]`
- `60_Claude/07_AI_Information/Jarvis Writing and Formatting.md` — added `## Blank Lines Rule`, `## Formatting Markers` (with SR cloze awareness), `## Callouts` (full type list), `## PDF and Source Ingestion Notes` (math, Tasks, flashcards)
- `40_Resources/Obsidian/Plugins/Spaced Repetition and Learning Loops.md` — added `## Deck Naming`, `## PDF Ingestion Note Structure`, bold/highlight cloze warning in Agent Rules
- `.claude/skills/ingest-clipping.md` — rewrote from scratch; added pypdf extraction, source type routing, spacing rules, math notation step, updated template with Tasks/Flashcards, 15-item quality checklist
- `.claude/agents/research-distiller.md` — same rewrites; added math notation, step 5b, updated template, 15-item quality checklist
### What the quality checklist now catches
1. Duplicate frontmatter keys
2. Broken `notes:` wikilinks
3. `---` in body
4. Blank line between heading and content
5. Blank lines between list items
6. Extra blank lines anywhere except after callout/blockquote
7. Missing ==highlight== anchors
8. Missing `**bold**` on named concepts
9. Missing `*italic*` sub-category labels
10. Missing callouts for emphasis/warnings/tips
11. Space-indented vs tab-indented numbered items
12. Missing math notation
13. `## Open Questions` not in Tasks format
14. Missing `## Flashcards` section
15. Content density check
## Template Audit — Current State and Gaps
This is the most critical remaining gap. **Templates are the ground truth for note structure. Agents without good templates invent structure. This is where quality control breaks down.**
### Templates that exist but are shells
**`Clipping Distill Template.md`** — 5 headings (`## Source`, `## Key Claims`, `## Why It Matters`, `## Links Into The Vault`, `## Open Questions`) with zero content guidance under any of them. Missing: `## Full Content`, `## Flashcards`, Tasks format for Open Questions, frontmatter that matches the actual PDF ingestion schema.
**`For Evergreen.md`** — frontmatter only. No body at all. An agent reading this learns nothing about what to write in an evergreen note.
**`For Progress.md`** — frontmatter only. Same problem.
**`Textbook Template.md`** — one heading: `# Chapter - `. That is the entire template.
**`Week Template.md`** — has the right sections but no guidance. `## Lecture` is empty. The MGMT 3001 notes show the actual rich pattern (`## Lecture-to-textbook synthesis` with ==definition anchor==, `*Mechanism:*`, concept links, callouts) but the template doesn't teach it.
**`Concept Template.md`** — uses `mastery (1/10): 0` which is invalid YAML (parentheses in key name). Missing `track:`, `prerequisites:`, `used_in:`, `evidence:` from the vault's capability schema.
**`Deep Dive Template.md`** — 13 section headings, all empty. No example content. An agent reading `## Teach It To A Beginner` has no idea what to put there without examples.
### Templates missing entirely
- PDF source summary (`60_Claude/10_Source_Summaries/PDF Ingestion/`) — no Templater folder template assigned
- Web source summary (`60_Claude/10_Source_Summaries/Web Ingestion/`) — no template
- Video source summary (`60_Claude/10_Source_Summaries/Video Ingestion/`) — no template
- Distilled note (`60_Claude/20_Distilled_Notes/`) — no template (Templater maps `For Evergreen.md` but it's a shell)
- Project brief (`60_Claude/40_Project_Briefs/`) — no template
- Review notes (`60_Claude/50_Reviews/`) — uses `Better Week.md` from Headway Templates but those are daily/weekly reviews, not source review notes
### What a good template must contain
1. **Frontmatter block** — every canonical field with correct syntax, no invented fields
2. **Section heading** with a one-line description of what the section contains
3. **Example content** (commented out or as placeholder) showing what rich content looks like
4. **Formatting reminders** — where to use =, `**`, `*`, callouts
5. **Plugin integration** — flashcard syntax at the bottom, Tasks format in Open Questions, math placeholder if relevant
## Plugin Gaps — What Is Not Being Used
### Plugins being used correctly
- `> [!NOTE]`, `> [!TIP]`, `> [!WARNING]`, `> [!QUESTION]`, `> [!SUMMARY]` — callouts, integrated ✓
- `**bold**` cloze — integrated into formatting rules ✓
- ==highlight== cloze — integrated into formatting rules ✓
- `::` flashcard separator — integrated into template ✓
- `- [ ]` Tasks format — integrated into Open Questions ✓
- `$...$` math — integrated into PDF workflow ✓
### Plugins not being used
**Canvas** — zero usage in any note or workflow. Canvas is for spatial maps: source-concept relationship maps, multi-note comparison layouts, concept dependency graphs. Every complex PDF could have a Canvas map linking its concepts. Not mentioned in any template or workflow document.
**Excalidraw** — referenced in `Jarvis Writing and Formatting.md` but not integrated into PDF ingestion workflow. PDFs frequently contain diagrams, flowcharts, frameworks. Currently: the diagram is described in text. Should be: recreate the diagram in Excalidraw, embed with `![[diagram.excalidraw]]`, link back from the note. No template has an Excalidraw embed placeholder.
**QuickAdd** — installed, not configured. QuickAdd is the one-keystroke note capture tool. Without QuickAdd configured, every note creation requires manual frontmatter. The vault has Templater folder templates but no QuickAdd capture menu. This means the user cannot create a new PDF summary note with correct frontmatter from mobile or without thinking about structure.
**Bases** — enabled but no usage patterns documented. Bases can query vault data like Dataview but with a different query model. No notes document what Bases is good for in this vault vs Dataview.
**Hover Editor** — configured (300ms delay, 400×340px) but no guidance on how to write link text and headings to maximize hover preview quality. Good hover previews require the first non-heading line of a note to be a useful summary.
**Latex Suite snippets** — active but undocumented custom snippets. The Quant Foundations note should use `$\mathbb{E}[X]$`, `$P(A \mid B)$` with proper LaTeX. The current rules say "use LaTeX" but don't document which snippets are available.
**Omnisearch** — enabled but PDF indexing is disabled. The 18 PDFs in `05_Clippings/PDFs/` are not searchable by Omnisearch. Either enable PDF indexing (requires Text Extractor plugin) or document that PDF search requires the manual extraction workflow.
**File Explorer++ pinning** — pins are configured for boards and dashboards but not for source summary folders. The `60_Claude/10_Source_Summaries/PDF Ingestion/` folder is not pinned, so it is not in the user's quick navigation.
## What Is Still Missing
### 1. Templates rewritten to be instructive
Priority: **critical**. Every template needs: description under each heading, example content, formatting reminders, flashcard section, Tasks format. The `Clipping Distill Template.md` must match the actual PDF ingestion note structure documented in `ingest-clipping.md`.
### 2. The `## Lecture-to-textbook synthesis` pattern documented
The MGMT 3001 notes end with a synthesis section that follows a strict pattern: ==definition anchor==, `*Mechanism:*`, lecture/scenario example, textbook connection with wikilinks, concept links, then `> [!WARNING]` and `> [!SUMMARY]` callouts. This pattern appears in every good week note. It is not documented in any instruction file. Every agent writing course notes will miss it.
### 3. Note maturity standards defined
What does a `status: seed` note look like vs `status: sprout` vs `status: tree`? There are 223 notes in the enrichment queue. Nobody (human or agent) knows what "enriched" means in concrete terms per note type. The `Jarvis Enrichment Template.md` exists but the standards are vague.
### 4. One completed example note per type
The best instruction is a concrete example. Every note type (PDF summary, concept, week note, textbook chapter, output, project brief) needs one canonical "gold standard" example linked from its template. Right now, the MGMT 3001 notes are the gold standard but they are never referenced from the templates.
### 5. Dataview boards for each source type
`10_Source_Summaries/PDF Ingestion/` has no Dataview board. The user cannot see all ingested PDFs at a glance with their status. Same for Web, Video, AI Conversations. The `Source Summaries Board.md` queries `60_Claude/30_Source_Summaries` (old path) — it's broken.
### 6. Canvas + Excalidraw integrated into PDF workflow
PDFs with frameworks, flowcharts, or concept maps should produce an Excalidraw note. The ingest skill should say: "if source has diagrams, create `[Source Name] - Diagrams.excalidraw` in `10_Areas/Excalidraw/` and embed with `![[...]]`."
### 7. QuickAdd capture menu configured
5–6 capture actions: PDF summary, web clip, distilled note, project note, quick thought, flashcard candidate. Each drops the note in the right folder with complete frontmatter. Without this, note creation is manual and error-prone on mobile.
### 8. Source Summaries Board repaired
`60_Claude/10_Source_Summaries/Source Summaries Board.md` queries `60_Claude/30_Source_Summaries` (old path, doesn't exist). Fix: update to query all four subfolders of `10_Source_Summaries/`.
### 9. Math standards for technical notes
LaTeX Suite snippets are undocumented. Before writing any math-heavy note, the agent should know: what snippets are active? What is the preferred LaTeX notation for probability ($P$, $\mathbb{P}$?), expectation ($E$, $\mathbb{E}$?), sets, functions? Until this is documented, every math note will be inconsistent.
## Definitive Formatting Rules — The Complete List
*For any AI agent writing in this vault:*
**Frontmatter:**
- No duplicate keys. One instance of every field.
- `source_note` for PDFs: `"[[Filename.pdf]]"` (filename with extension, no path)
- Do not include `source_status` unless the specific workflow requires it
- Every wikilink in `notes:` verified with Grep before writing
**Blank lines (the most-violated rule):**
- `headerspace.css` handles visual spacing. Do not add blank lines for visual breathing room.
- Zero blank lines: between `---` and title, between heading and content, between list items, between sections
- One blank line only: after a callout (`> [!X]`) or blockquote (`> `) before following prose
**Formatting markers:**
- ==text== — ONE per major section. The single most important definitional claim. Creates SR cloze. Do not scatter.
- `**text**` — named concepts on introduction, category labels, key contrast words, named entities. Creates SR cloze in `#cards` sections. Use deliberately.
- `*label:*` — sub-category intro labels only: *Mechanism:*, *Interview value:*, *Core Python Skills:*, *Utilitarianism:*. Not a cloze.
- `> [!NOTE]` — critical statement. `> [!TIP]` — practical advice. `> [!WARNING]` — failure mode. `> [!QUESTION]` — interview emphasis. `> [!SUMMARY]` — section summary.
- Numbered items: `1. **Title**` then tab-indented sub-content (not space-indented)
**Plugin integration:**
- Math: `$E[X]$`, `$P(A|B)$` for any notation. `$$...$$` for display equations.
- Tasks: `## Open Questions` uses `- [ ]` format
- Flashcards: `## Flashcards` at end of every PDF/source note. `#cards/[track]` deck. `question::answer` single-line or multiline with `?`. 3–5 cards minimum. Test mechanisms and contrasts, not labels.
- Wikilinks: shortest unique filename. Verify existence before writing.
**What `---` means:**
- After frontmatter: end of YAML block. Exactly once per file.
- In the body: nothing. Do not use it. It will look like a horizontal rule in reading view but it is semantically wrong and confusing.
## Build Priorities — Ordered
*What must be done to reach "notes written as I wish" state:*
1. **Rewrite Clipping Distill Template** — match the actual PDF ingestion structure: `## Full Content` with `###` subheadings, `## Open Questions` as Tasks, `## Flashcards` with `#cards/[track]`. This is the most-used template.
2. **Write a Week Template that teaches** — add the `## Lecture-to-textbook synthesis` section with ==definition anchor==, `*Mechanism:*`, callouts. Add content guidance under every heading. Link to a gold standard example note.
3. **Rewrite For Evergreen.md and For Progress.md** — add actual body sections, not just frontmatter
4. **Fix Concept Template** — remove `mastery (1/10): 0` (invalid YAML), add `track:`, `prerequisites:`, `used_in:`, `evidence:` capability fields
5. **Repair Source Summaries Board** — fix Dataview query from `30_Source_Summaries` to `10_Source_Summaries`
6. **Configure QuickAdd** — 5-item capture menu for the main note types
7. **Integrate Excalidraw into PDF workflow** — when source has diagrams, create `.excalidraw` file and embed
8. **Document the synthesis pattern** — add `## Lecture-to-textbook synthesis` as a named pattern in `Jarvis Writing and Formatting.md`
9. **Document math notation standards** — which LaTeX notation for probability, expectation, sets
10. **One gold standard example per note type** — link from each template
## What "Complete Control" Requires
The user's stated goal: complete control of each word written in the vault. This requires:
- **Templates that are instructive, not empty** — every heading has a one-line description of what goes there and how much
- **Formatting rules embedded in templates** — not just in a separate instruction document
- **Quality checklist that every agent runs** — the 15-point checklist in `ingest-clipping.md` is the starting point; it needs to exist in every skill and agent that writes notes
- **Gold standard examples** — one fully-populated example per note type that an agent can pattern-match against
- **Plugin integration in every workflow** — not as afterthought documentation but as required steps in the skill
The gap between "notes written by an agent" and "notes that match the vault's standard" is not a knowledge gap — it is a documentation gap. The vault's own notes already demonstrate the correct standard. The instruction layer needs to point at those notes and say: this is what you must produce.
## Sources Read This Session
- `60_Claude/07_AI_Information/Session Logs/log.md` — full history
- `10_Areas/UMN/Previous Classes/Minor/MGMT 3001/Week - 4.md`, `Week - 9.md`
- `10_Areas/UMN/Previous Classes/Minor/MGMT 3001/Textbook/Chapter - 3.md`, `Chapter - 5.md`, `Chapter - 6.md`
- `30_Order/Templates/` — all 32 templates
- `40_Resources/Obsidian/Plugins/` — all 12 plugin reference notes
- `60_Claude/07_AI_Information/Jarvis Writing and Formatting.md`
- `HUMAN_WRITING.md`, `AGENTS.md`, `CLAUDE.md`
- `60_Claude/05_Clippings/PDFs/Quant Foundations.pdf` — trial ingest source
