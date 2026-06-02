---
type: evergreen
status: sprout
created: 2026-06-01
updated: 2026-06-01
tags:
  - system
  - standards
notes:
  - "[[Clipping Distill Template]]"
  - "[[Capture to Summary]]"
  - "[[Vault Rules — Complete AI Ruleset]]"
  - "[[HUMAN_WRITING]]"
---
# Source Summary Standard
==A source summary captures one source so completely that reopening the original reveals nothing new — it replaces the source, it does not advertise it.==
This is the content standard for any `input` note created from a single source (PDF, web page, video, image, AI conversation). It says what belongs under each heading, how dense each section should be, which plugin syntax applies, and what each section looks like when an agent gets it wrong. The template gives the empty shape; this doc gives the content. The structure here must match [[Vault Rules — Complete AI Ruleset]] Part 9 exactly.
## Maps To
- Template: [[Clipping Distill Template]]
## Used By Workflow
- [[Capture to Summary]] — the create-the-note step reads this doc first.
- `research-distiller` agent and `ingest-clipping` skill point here for the note body.
## Per-Heading Standard
### Frontmatter
`type: input`, `status: sprout`, `created`/`updated` as `YYYY-MM-DD`, `tags: [summary]`. Set `input_kind` to the real source kind (`pdf | web | video | image | conversation`) and `track` to the subject domain (`ai | systems | algorithms | career | trading | general`) — the `track` value becomes the flashcard deck. For source notes set `source_note: "[[Filename.pdf]]"` using the filename **with extension and no folder path**, and `source_url` to the path or live link. Every `notes:` wikilink must point to a file that already exists — Grep first.
> [!WARNING]
> Duplicate `notes:` keys (YAML silently keeps the last), a `source_note` written as a full path or without the extension, or a `track` that does not match the deck you tag in Flashcards. The Quant Foundations note uses `source_note: "[[Quant Foundations.pdf]]"` and `track: trading` feeding `#cards/trading`.
### Title and Source Lines
One H1 with the source's real title plus ` — Summary`, no blank line after frontmatter. Immediately follow with three bold header lines: `**Source:**` (path or URL in backticks), `**Ingested:**` (date), `**Pages:**` (count for PDFs; omit the count for web/video but keep the line meaningful). No highlight here — these are metadata, not a section.
> [!WARNING]
> A blank line between the frontmatter `---` and the title, or prose padding before the header lines. See Quant Foundations lines 15–18 for the exact shape.
### Source
One sentence: what it is, who produced it, its stated purpose. Bold the source type, author, or named firms on first mention. One `==highlight==` is optional here; the real anchor lives in Full Content sections.
*Density:* one to three sentences. No bullet list.
> [!WARNING]
> A multi-paragraph description, or restating the title. Quant Foundations § Source is a single sentence naming the firms (`**Jane Street**`, `**SIG**`, ...) and the four things the source actually teaches.
### Key Claims
Every distinct claim in the source as a bullet, bold the key concept in each. This is the compressed argument of the whole source before the full capture.
*Density:* one bullet per real claim — Quant Foundations carries 12. Do not merge claims to look shorter.
*Plugins:* bold cloze on the key term; this section is not `#cards`-tagged so bold is safe on every named concept.
> [!WARNING]
> Three vague bullets that paraphrase the abstract. If the source makes a contrast (`Top firms do **not** expect... they **do** expect...`), both halves are separate claims.
### Full Content
The complete capture, using `###` subheadings with the source's **exact section titles in source order**. If the source has 8 parts, the note has 8 `###` sections. Reproduce every numbered list, framework, and checklist in full. Each `###` section carries exactly one `==highlight==`: its single most important definitional claim.
*Density:* this is the bulk of the note. A 12-page source becomes a long Full Content section, not a paragraph.
*Plugins:* `1. **Title**` then tab-indented sub-content for numbered concepts; `*Label:*` italic for sub-group intros (`*Focus areas:*`, `*Interview value:*`); callouts for every source emphasis (`> [!NOTE]` key fact, `> [!TIP]` advice, `> [!WARNING]` failure mode, `> [!QUESTION]` interview emphasis); `$...$` LaTeX for any notation, never spelled-out formulas.
> [!WARNING]
> Compressing the source ("Part II covers probability and distributions") instead of reproducing it. Space-indented rather than tab-indented sub-content. A section with no highlight, or three highlights. See Quant Foundations § Full Content: each `### Part` opens with one `==...==` anchor, numbered concepts use tab-indented `*Focus areas:*` blocks, and `> [!NOTE] *Key interview skill:*` carries the emphasis.
### Why It Matters
The connection to active vault work — a named project, course, or concept — and why this source earns a note. No generic importance.
*Density:* two to four sentences. Name the real use.
> [!WARNING]
> Padding like "this is a valuable resource." Quant Foundations § Why It Matters names quant internship applications and points at the 5 buildable Python projects.
### Links Into The Vault
Verified wikilinks only — Grep each before writing. Stubs that do not yet exist go **here**, labeled `(to create)`, never in frontmatter.
*Density:* link the source clipping and every existing concept/project the source touches.
> [!WARNING]
> Wikilinking firm names or book titles that have no vault note. Quant Foundations links only `[[Stocks Trading AI Hub]]` (confirmed) and lists uncreated targets as questions, not as fake links.
### Open Questions
`- [ ]` Tasks format for every item, never prose. Add `📅`/`⏳`/priority emoji where a real date exists.
*Density:* the genuine follow-ups and gaps — typically two to five.
> [!WARNING]
> Writing open questions as a prose paragraph, or inventing questions to fill the section.
### Flashcards
Ends every source note. `#cards/[track]` where `[track]` matches the `track:` frontmatter field. Minimum 3–5 cards. Test mechanisms, contrasts, and failure modes — not acronym or label trivia. Cards come after the concept is explained in the body.
*Plugins:* in a `#cards` section, `**bold**` and `==highlight==` become automatic clozes — bold **only** the exact term you want hidden in review, not every noun.
> [!WARNING]
> Cards built straight from raw source before distillation, label trivia (`RAG stands for::...`), or bolding every word in an answer so the card hides everything.
## Done Conditions
- Reopening the original source would reveal nothing the note does not already contain.
- Structure matches Part 9: frontmatter → title → source lines → Source → Key Claims → Full Content → Why It Matters → Links → Open Questions → Flashcards.
- Every `###` in Full Content uses the source's verbatim title and carries exactly one highlight.
- No duplicate frontmatter keys; every `notes:` link verified; no `---` in the body; no blank lines except one after a callout before prose.
- 3–5+ mechanism-testing flashcards on the correct `#cards/[track]` deck.
- Passes all 16 points of [[Vault Rules — Complete AI Ruleset]] Part 12.
## Gold Standard Example
- [[Quant Foundations (PDF)]] — the reference build: 12 pages captured in source order, one highlight per part, tab-indented numbered concepts, callouts for every emphasis, verified links, and a `#cards/trading` deck.
