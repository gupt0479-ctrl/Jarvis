---
type: evergreen
status: tree
created: 2026-05-31
updated: 2026-05-31
tags:
  - system
  - ai-agents
  - rules
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[Jarvis Writing and Formatting]]"
  - "[[Agent Operating Guide]]"
---
# Vault Rules — Complete AI Ruleset
==This is the governing specification for all AI behavior in Jarvis. Any platform — Claude, Kiro, Cursor, Copilot, or any future tool — that writes notes in this vault must read and enforce every rule here before touching a single file.==
This document states rules as positive specifications. For the history behind each rule, see [[Note Writing System — Audit and Roadmap (2026-05-31)]].
## Part 1 — Mandatory Pre-Flight
Before creating, editing, or organizing any note, complete these actions in order. There are no exceptions.
### Read Order on Any Cold Start
Read in this sequence:
1. `60_Claude/07_AI_Information/Vault Map.md` — orientation
2. **This file** — the governing ruleset
3. `AGENTS.md` — Write Contract and routing table
4. `40_Resources/Obsidian/Jarvis Vault Architecture.md` — placement source of truth
5. The matching workflow in `30_Order/Workflows/` for the task type
6. `HUMAN_WRITING.md` — voice and prose standard
7. `60_Claude/07_AI_Information/Jarvis Writing and Formatting.md` — Obsidian formatting rules
8. `AI_CONTEXT.md` — live state manifest and domain entry points
9. `00_Dashboard.md` — current control panel
10. Tail of `60_Claude/07_AI_Information/Session Logs/log.md` — recent work
Do not skip steps. Do not assume context from a prior session without reading the session log.
### Analyze the Vault Before Writing
==Read 3–5 existing vault notes in the same category or domain before writing any new note.==
An agent that writes without analyzing real vault notes invents conventions that do not match. The formatting standards below were derived from real notes. Real notes are always the ground truth.
- PDF ingestion task → read an existing note from `60_Claude/10_Source_Summaries/PDF Ingestion/`
- Course note task → read 2–3 notes from the relevant course folder under `10_Areas/UMN/`
- Evergreen note task → read 2–3 notes from `60_Claude/20_Distilled_Notes/` or `40_Resources/`
- Project note task → read the existing project brief or board from `20_Progress/`
**Read the Standards doc for this note type.** For the note type you are creating, check the routing table in `AGENTS.md` for its Standards doc. If one exists in `30_Order/Standards/`, read it before writing a single line of the note.
### Search Before Creating
Use `Grep` or `Glob` to find an existing canonical note before creating a new one. Prefer extending a canonical note over creating a duplicate. Write to `60_Claude/00_Inbox/` if the correct destination is unclear.
## Part 2 — Note Placement
Every note belongs to exactly one folder. Use the routing table in `AGENTS.md` as the authority.

| Content type                          | Destination                      |
| ------------------------------------- | -------------------------------- |
| Raw clips, PDFs, imported sources     | `60_Claude/05_Clippings/`        |
| Quick AI output awaiting review       | `60_Claude/00_Inbox/`            |
| Source-grounded summaries             | `60_Claude/10_Source_Summaries/` |
| Durable distilled knowledge           | `60_Claude/20_Distilled_Notes/`  |
| Reusable output artifacts             | `60_Claude/35_Outputs/`          |
| Project briefs                        | `60_Claude/40_Project_Briefs/`   |
| Daily/weekly/monthly reviews          | `60_Claude/50_Reviews/`          |
| Dashboards and indexes                | `60_Claude/44_Indexes/`          |
| Agent/session docs, AI operating docs | `60_Claude/07_AI_Information/`   |
| Active projects, career, UROP         | `20_Progress/`                   |
| Coursework, identity domains          | `10_Areas/`                      |
| Stable guides, concepts, reference    | `40_Resources/`                  |
| Templates, workflows, CLI tools       | `30_Order/`                      |
When unsure: write to `60_Claude/00_Inbox/`. Never invent a folder. Never create files or folders at the vault root.
## Part 3 — Frontmatter Specification
### No Duplicate Keys
Every YAML key appears exactly once. Scan frontmatter before saving. YAML silently takes the last value when a key repeats, discarding the first without warning.
### Canonical Field Set
Use only these fields. Do not invent new keys unless the current schema cannot represent the information:
```yaml
---
type: input
status: sprout
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - summary
notes:
  - "[[Verified Existing Note]]"
source_url: 60_Claude/05_Clippings/PDFs/Filename.pdf
source_note: "[[Filename.pdf]]"
input_kind: pdf
track: ai
next: "[[Next Action Note]]"
---
```
Valid values:
- `type`: `input` | `evergreen` | `concept` | `project` | `thought` | `brainstorm` | `class` | `plan` | `review` | `dashboard` | `index` | `output`
- `status`: `seed` | `sprout` | `tree` | `active` | `paused` | `complete` | `archived`
- `input_kind`: `pdf` | `web` | `video` | `image` | `conversation`
- `track`: `ai` | `systems` | `algorithms` | `career` | `trading` | `general`
### source_note Format
For any source summary note: `source_note: "[[Filename.pdf]]"` — filename with extension, no folder path. Not `[[60_Claude/05_Clippings/PDFs/Filename.pdf]]`. Not `[[Filename]]` (without extension).
### source_status Field
Do not include `source_status` in frontmatter unless the specific workflow document for this note type explicitly requires it. It is not part of the default schema.
### Wikilinks in Frontmatter
Every wikilink in `notes:` must refer to a file that actually exists in the vault. Before writing any wikilink into frontmatter, Grep for the filename to confirm it exists. Broken frontmatter links corrupt metadata silently. Stubs belong only in the note body, labeled `(to create)`, never in frontmatter.
## Part 4 — Blank Lines and Spacing
==The `headerspace.css` CSS snippet handles all visual heading spacing. Any blank line added for visual breathing room is an error.==
**The complete blank line specification:**
- Zero blank lines between `---` (frontmatter close) and the `#` title
- Zero blank lines between any heading (`##`, `###`, `####`) and its first content line
- Zero blank lines between consecutive list items
- Zero blank lines between consecutive sections
- One blank line is permitted: immediately after a callout (`> [!X]`) or blockquote (`> `) before a following paragraph of prose
- `---` in the body is forbidden. `---` is the YAML frontmatter terminator. It appears exactly once per file, after frontmatter, before the title. It never appears anywhere in the note body.
- No trailing blank lines at the end of a file
- No footer comments (`*Ingested by...*`, `*Generated by...*`)
Any blank line that exists for visual rhythm is wrong. If you are tempted to add one for breathing room, do not. The CSS handles it.
## Part 5 — Formatting Markers
These markers carry semantic meaning. They are not decoration. Spaced Repetition bold and highlight clozes are enabled in this vault: every `**bold**` and ==highlight== in a `#cards`-tagged section becomes an automatic cloze card. Use them deliberately.
### ==text== — Highlight Cloze
Use for the **single most important definitional claim** per major section.
- One per major section (`##` heading). Never scattered through bullets.
- This is the anchor sentence — the one line that defines the core truth of the section.
- Good: ==Expectation is the most important object in quant interviews.==
- Good: ==Ethics is about what managers and organizations should do, not merely what they are legally allowed to do.==
- Wrong: three highlights in the same section, a highlight on a list item, highlights on every paragraph.
### **text** — Bold Cloze
Use for every named concept, term, entity, or category when introduced, and for key contrast words.
Bold goes on:
- Named concepts when introduced: `**Expectation**`, `**limit order book**`, `**Diversification**`
- Category labels in lists: `**Stars:**`, `**Legitimate power:**`, `**Tangible resources:**`
- Named entities: `**Jane Street**`, `**Amazon**`, `**NumPy**`, `**pandas**`
- Key contrast words: `**mis-ordered**`, `**do**` vs `**not**`
- Directive action instructions: `**Simulate**`, `**Verify**`, `**Depth beats breadth**`
### *label:* — Italic Sub-Category Label
Use for sub-category intro labels only. Not a cloze.
- `*Mechanism:*`, `*Interview value:*`, `*Core Python Skills:*`, `*The four pillars:*`
- Framework names used as inline labels: `*Utilitarianism:*`, `*Kantianism:*`
- Do not use italics for general emphasis.
### Numbered Items with Indented Sub-Content
When the source has numbered concepts with sub-content:
```
1. **Concept Name**
	Sub-description (tab-indented, not space-indented)
	*Label:* Explanation
	- Sub-bullet
	- Sub-bullet
```
Use tab indentation. Space-indented sub-content under numbered items is wrong.
## Part 6 — Content Density Standard
==Every line in the source must appear in the note in some form. The note replaces the source — the user should never need to open the original again.==
- Map the document structure first: list every heading and subheading before writing anything
- Preserve the source's own section order; use `###` headings with the source's exact section titles verbatim
- Reproduce all numbered steps, frameworks, checklists, and lists in full — do not compress
- If the source has 6 steps, the note has 6 steps. If it has 5 project types with sub-bullets, the note has all 5 with all sub-bullets.
- Every named concept, term, entity, tool, company, and person gets captured
- Every warning, emphasis, or "key insight" marker in the source becomes a callout in the note
- After writing, re-read the note: if opening the original would reveal anything not in the note, the note is incomplete
Summaries that miss content are not complete notes. Partial capture is a failure, not a draft.
## Part 7 — Wikilink Rules
- Use shortest unique filename: `[[BOOM Board]]` not `[[20_Progress/UROP/BOOM Board]]`
- Verify every wikilink exists before writing it — Grep for the filename in the vault
- Stubs belong only in the `## Links Into The Vault` body section, labeled `(to create)`. Never in frontmatter.
- Do not wikilink firm names, book titles, or concept terms unless an actual vault note exists for them
- Use aliases when prose reads better: `[[Long Note Title|short label]]`
- After writing, grep every wikilink you added to confirm it resolves
## Part 8 — Plugin Integration Rules
### Callouts
Use callout syntax when the content needs to change how the reader treats it — not for decoration.
Callout types used in this vault:
- `> [!NOTE]` — key fact, important note, critical statement from the source
- `> [!TIP]` — practical advice or application instruction
- `> [!WARNING]` — failure mode, common mistake, or misconception to avoid
- `> [!QUESTION]` — interview emphasis question or unresolved gap
- `> [!SUMMARY]` — section summary
- `> [!EXAMPLE]` — concrete worked example
After a callout, exactly one blank line before the next paragraph of prose. Do not stack callouts to make the note look designed.
### Tasks
Use Tasks syntax for real actions and open questions, not prose paragraphs.
- `## Open Questions` uses `- [ ]` Tasks format for every item — never prose
- `- [/]` for in-progress, `- [x]` for done, `- [-]` for cancelled
- Add due/scheduled/priority metadata in Tasks emoji format, not Dataview inline fields
- Write tasks only when there is a real concrete action
### Spaced Repetition — Flashcards
Every PDF/source summary note ends with `## Flashcards`. No exceptions.
- Deck tag: `#cards/[track]` where `[track]` matches the note's `track:` frontmatter field
- Single-line card: `question::answer #cards/[track]`
- Multi-line card: question on its own line, `?` on next line, answer, then `#cards/[track]`
- Minimum 3–5 cards per PDF ingestion note
- Test mechanisms, contrasts, and failure modes — not acronym definitions or label trivia
- Cards belong after the concept is explained in the note body, not before
- Do not put cards in templates, archive folders, or raw clippings
> [!WARNING]
> Every `**bold**` term in a `#cards`-tagged section becomes an SR cloze automatically. In flashcard sections, bold only the exact term you want tested, not every noun in the answer.
### Math Notation — LaTeX Suite
Use LaTeX for any mathematical notation from the source. Never spell out formulas in plain prose.
- Inline expressions: `$E[X]$`, `$P(A|B)$`, `$O(n \log n)$`, `$\sigma^2$`
- Display equations (own line): `$$E[X] = \sum x \cdot P(X=x)$$`
- Explain what each equation means in the prose around it
- One worked example is better than five unexplained formulas
- Do not use LaTeX as decoration or to make simple sentences look technical
### Dataview
Use Dataview when a list should stay current from frontmatter metadata.
- Prefer Dataview boards over manually-maintained lists for active projects, stale notes, and task queues
- Keep metadata clean and consistent — Dataview only queries what is in frontmatter
- DataviewJS only when plain Dataview cannot express the query
- Do not manually duplicate lists that Dataview should generate
### Excalidraw
Use Excalidraw when the relationship is spatial: system architecture, feedback loops, dependency graphs, flowcharts, concept maps.
- During PDF ingestion: if the source contains diagrams, frameworks, or flowcharts, create `[Source Name] - Diagrams.excalidraw` in `10_Areas/Excalidraw/` and embed with `![[Source Name - Diagrams.excalidraw]]`
- Always keep searchable text near visual work — future agents need text to find things
- Embed with wikilinks, not image paths
- Do not use Excalidraw as a replacement for a clear text note
- Do not edit compressed drawing data by hand
### Templater
Templater is the active template system (core Templates is disabled).
- Templates folder: `30_Order/Templates`
- When creating notes outside Obsidian, manually follow the same template fields and frontmatter schema
- Match existing frontmatter schema; do not invent new keys
- Folder templates are configured for: `10_UMN`, `20_Progress`, `40_Resources`, `60_Claude/20_Distilled_Notes`, `60_Claude/30_Source_Summaries`, `60_Claude/40_Project_Briefs`
### Kanban
Use Kanban for board-shaped workflows: habit tracking, project stages, triage lanes. Keep card text action-oriented. Link cards to canonical notes when the card represents real project work.
### Git
Do not run Git operations unless the user explicitly asks. Do not modify auto-backup settings. Check status before any commit or push.
## Part 9 — Source Ingestion Rules
### Structure Order for Any Source Note
1. Frontmatter (with `track:` matching subject domain, no duplicate keys, all wikilinks verified)
2. `# Title — Summary` (no blank line after frontmatter close)
3. `**Source:**`, `**Ingested:**`, `**Pages:**` header lines immediately after title
4. `## Source` — one sentence: what it is, who produced it, stated purpose
5. `## Key Claims` — every distinct claim; bold the key word in each bullet
6. `## Full Content` — `###` subheadings using the source's exact section titles verbatim
7. `## Why It Matters` — connection to active vault work; no padding
8. `## Links Into The Vault` — verified wikilinks; stubs labeled `(to create)`
9. `## Open Questions` — `- [ ]` Tasks format
10. `## Flashcards` — `#cards/[track]` cards, 3–5 minimum, mechanisms not labels
### PDF-Specific Rules
- Extract with Python pypdf before writing anything:
```bash
python -c "
import pypdf, sys
sys.stdout.reconfigure(encoding='utf-8')
reader = pypdf.PdfReader(r'FULL_WINDOWS_PATH')
print(f'Total pages: {len(reader.pages)}')
for i, page in enumerate(reader.pages):
    print(f'\n=== Page {i+1} ===')
    print(page.extract_text())
"
```
- For PDFs over 30 pages: batch in groups of 20 pages
- If output is blank or garbled binary: PDF is image-based (scanned) — tell the user, OCR required
- Map every heading and subheading across all pages before writing the note
- `input_kind: pdf`, `source_note: "[[Filename.pdf]]"` (filename + extension, no path)
- Every formula uses LaTeX notation
### Web-Specific Rules
- Use `WebFetch` with `format: "markdown"` for live URLs
- If paywalled: tell the user and ask for pasted content
- `input_kind: web` in frontmatter
### Video-Specific Rules
- Read transcript markdown from `60_Claude/05_Clippings/Videos/`
- `input_kind: video` in frontmatter
## Part 10 — Tool Selection Rules
### Reading Files
| Situation | Tool |
|---|---|
| Any text file or Markdown note | `Read` |
| PDF file | Python pypdf via `Bash` |
| Image file | `Read` (multimodal) |
| Live URL | `WebFetch` |
| Search file contents | `Grep` |
| Find files by pattern | `Glob` |
| Directory listing | `Bash` (ls) |
### Writing Files
| Situation | Tool |
|---|---|
| Patching an existing file by heading | `Edit` (patch only — do not rewrite) |
| Creating a new file | `Write` |
| Full rewrite of an existing file | `Read` first, then `Write` |
### MCP Filesystem Tools
Prefer `Read`, `Edit`, `Write`, `Grep`, `Glob` over `mcp__filesystem__*` equivalents. Use MCP filesystem tools only when the core tools cannot perform the operation. Never use MCP tools to read plugin `data.json` files unless explicitly asked to document plugin settings.
### Subagents
- Use subagents for broad exploration requiring 3+ queries
- `subagent_type: Explore` for finding files without a known path
- `subagent_type: research-distiller` for long technical PDFs requiring section-by-section deep extraction
- Do not spawn subagents for tasks completable inline with 1–2 tool calls
## Part 11 — Skills and Agents
### Skills — When to Use Each
| Skill | Use when |
|---|---|
| `/ingest-clipping` | Processing any single source from `05_Clippings/` |
| `/distill-note` | Converting a source summary into a durable concept note |
| `/remove-ai-slop` | Rewriting a note that sounds AI-generated |
| `/context` | Building a context pack for a complex task |
| `/today` | Morning planning |
| `/trace-topic` | Following a concept across multiple vault notes |
| `/connect-notes` | Finding connections between isolated notes |
| `/closeday` | End-of-day summary and session log |
| `/weekly-review` | Weekly review |
| `/lint-claude-layer` | Auditing the `60_Claude` layer for structure problems |
| `/ops [operation]` | Daily vault operations (morning-start, evening-close, health-check) |
### Agents — When to Use Each
| Agent | Use when |
|---|---|
| `research-distiller` | Long PDF, multiple sources, cross-referencing required |
| `vault-curator` | Links audit, deduplication, structure maintenance |
| `career-operator` | Career notes, internship tracking, portfolio |
| `anti-slop-editor` | Rewriting AI-sounding prose vault-wide |
`/ingest-clipping` (skill) is for standard single-source ingestion. `research-distiller` (agent) is for deep multi-source or complex technical ingestion where cross-referencing is required.
### Hooks
Hooks execute shell commands in response to Claude Code events. They are configured in `.claude/settings.json` under `hooks`. To add or modify automated behaviors ("before each note save check X", "after a session log every run Y"), use the `update-config` skill — do not edit settings files directly. Never disable hooks with `--no-verify` without explicit user instruction.
## Part 12 — Quality Gate
==Run this 16-point checklist before saving any note. Do not save until all answers are correct.==
1. **Duplicate frontmatter keys?** → scan and fix; one key, one value
2. **Every `notes:` wikilink confirmed to exist?** → Grep each one; fix or move to body labeled `(to create)`
3. **`---` anywhere in the body?** → remove; `---` appears only as the frontmatter terminator
4. **Blank line between frontmatter `---` and `#` title?** → remove
5. **Blank line between any heading and its first content line?** → remove
6. **Blank lines between list items?** → remove
7. **Extra blank lines anywhere except after callout/blockquote before prose?** → remove
8. **Every major `##` section has exactly one ==highlight== anchor?** → add the single most important definitional claim
9. **Named concepts, terms, and entities bolded on first introduction?** → add `**bold**`
10. **Sub-category intro labels italicized?** → `*Label:*` on every sub-group intro
11. **Interview emphasis, warnings, and key facts in callouts?** → add where missing
12. **Tab-indented (not space-indented) sub-content under `1. **Title**` items?** → fix
13. **LaTeX notation (`$...$`) for any mathematical expression?** → add if missing
14. **`## Open Questions` in `- [ ]` Tasks format?** → fix if prose
15. **`## Flashcards` section with `#cards/[track]` cards?** → add if missing (PDF/source notes); minimum 3–5; test mechanisms not labels
16. **Does re-reading this note replace opening the original?** → if no, add what's missing
## Part 13 — Safety Rules and Stop Conditions
### Never Do Without Explicit Instruction
- Create a file or folder at the vault root
- Modify `60_Claude/05_Clippings/` — raw sources are read-only after capture
- Read or write anything in `50_Archive/`
- Edit `.obsidian/`, `.claude/`, `.cursor/`, `.kiro/`, `.codex`, `.git/` settings or plugin data files
- Copy API keys, tokens, plugin credentials, or `data.json` secret values into notes
- Run Git commit, push, or pull
- Restructure notes with `status: tree` — propose changes first
- Delete or move notes
- Bulk-dump AI output into `40_Resources/` — curated; one backlinked entry at a time
### Pause and Confirm Before
- Restructuring system docs or template schemas
- Any destructive or hard-to-reverse file operation
- Modifying plugin settings
- Changing vault folder structure
- Converting task formats vault-wide
### When in Doubt
Write to `60_Claude/00_Inbox/`. Make one well-linked note. Do not invent structure. Ask the user.
## Part 14 — Session End Protocol
After any meaningful vault changes, append a concise entry to `60_Claude/07_AI_Information/Session Logs/log.md`.
Format:
```
## [YYYY-MM-DD] [operation] | [title or subject]
- What was created or changed
- Why it matters
- Open questions
- Next action if one exists
```
Update `updated:` in the frontmatter of any note that changed meaningfully. Do not update dashboards just to create activity.
