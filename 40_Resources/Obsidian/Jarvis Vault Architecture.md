---
type: evergreen
status: tree
created: 2026-05-30
updated: 2026-05-31
tags:
  - evergreen
  - system
  - obsidian
  - architecture
notes:
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[AGENTS]]"
  - "[[CLAUDE.md]]"
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[60_Claude/40_Project_Briefs/Vault-Audit-2026-05-29]]"
  - "[[00_Dashboard]]"
next: "Build the missing pieces: 30_Order writing-workflow docs + a 07_AI_Information vault map, then reference both from CLAUDE.md / AGENTS.md / HUMAN_WRITING.md"
---

# Jarvis Vault Architecture

This note defines what every folder in Jarvis is for, what goes in it, who is allowed to write to it, and how a note moves from raw capture to durable knowledge. It is the placement source of truth. When this note and the folder tree disagree, fix one of them on purpose — never let an agent guess.

Read it before writing anything into the vault. It is the answer to the failure that created it: an agent that doesn't know the architecture will invent a folder, and one bad guess at the root pollutes the whole system.

We are early. Most folders are still thin. The point of writing the architecture *now*, before the vault fills up, is so the structure shapes the content instead of the content forcing a messy structure later. Define first, then fill — and never fill with slop (see [[HUMAN_WRITING]]).

---

## The mental model: six layers

Jarvis is not a pile of folders. It is six layers, each answering one question. Every folder belongs to exactly one layer. If you can name the layer, you know where a note goes.

| Layer | Folder | The question it answers | Who owns it |
|---|---|---|---|
| **Identity** | `10_Areas/` | Who am I and what are my domains? | You. AI patches by heading only. |
| **Execution** | `20_Progress/` | What am I actively doing right now? | You + AI, working notes with next actions. |
| **Rules** | `30_Order/` | How are notes written and structured here? | You. AI reads this before writing; edits only when building tooling. |
| **Reference** | `40_Resources/` | What do I need to know or look up to do the work? | You curate. AI proposes, never bulk-dumps. |
| **AI workshop** | `60_Claude/` | Where does AI capture, draft, distill, and coordinate? | Every AI agent, freely. |
| **Dead** | `50_Archive/` | What is done and out of rotation? | Nobody touches it. AI never reads or writes. |

Two cross-cutting pieces sit inside these layers rather than as their own top level:

- **Visual** — `10_Areas/Excalidraw/`: diagrams for any concept, project, or source. Lives under Identity because a diagram belongs to the domain it explains.
- **AI operating memory** — `60_Claude/07_AI_Information/`: how any AI reads this vault, plus the cross-tool conversation and session-log record. The map and memory for agents.

The single most important relationship: **knowledge is born in `60_Claude`, matures there, and is promoted out to Identity / Execution / Reference. `60_Claude` is a workshop, not a warehouse.** That is what stops the vault from splitting into a "human brain" and a separate "AI brain."

---

## The Write Contract

Every agent must follow this, regardless of which tool is driving (Claude Code, Cursor, Kiro, Codex, Cowork, or anything talking only through the Obsidian MCP server). It is short on purpose so it can be pasted into any instruction file.

### Golden rules

1. **Never create a new top-level file or folder at the vault root.** The root holds exactly: `00_Dashboard.md`, `AGENTS.md`, `CLAUDE.md`, `HUMAN_WRITING.md`, and the numbered folders `10_Areas` → `60_Claude`. Adding anything else at root is the single most damaging mistake an agent can make.
2. **When unsure where a note goes, write it to `60_Claude/00_Inbox/`.** A misfiled note in the Inbox is fixed in five seconds. A note in an invented folder is invisible until it causes damage. Unsure is the trigger to use the Inbox, never to invent a location.
3. **Read `30_Order/` before writing.** It holds the templates and the per-folder writing workflow. It is the structural half of [[HUMAN_WRITING]] — that file says how prose should sound, `30_Order` says how a note should be shaped and filed.
4. **Search before creating.** Look for an existing canonical note and extend it. Most "new" notes should be edits.
5. **Preserve frontmatter and wikilinks. Patch by heading.** Do not rewrite a whole note to change one section.

### Where does this note go?

| If the note is…                                                         | Write it to…                                                                                                                          |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| A raw clip, paste, web capture, video or imported source                | `60_Claude/05_Clippings/`                                                                                                             |
| A quick AI output you're not sure how to file                           | `60_Claude/00_Inbox/`                                                                                                                 |
| A summary of one source/raw input                                       | `60_Claude/10_Source_Summaries/`                                                                                                      |
| Reusable distilled knowledge (a concept, not a source)                  | `60_Claude/20_Distilled_Notes/` → promote to `40_Resources/` or `10_Areas/` once stable                                              |
| Stable reference material (guide, cheat sheet, plugin doc, link)        | `40_Resources/` + backlink to its `10_Areas/` domain                                                                                  |
| Work on an active project, internship, research, mentorship             | `20_Progress/` under the matching project folder                                                                                      |
| A canonical fact about a life domain (Career, Trading, Life, UMN, etc.) | `10_Areas/` — patch an existing domain file by heading; do **not** add new top-level files here without explicit instruction          |
| A synthesized project brief with infinite backlinks (relevant only)     | `60_Claude/40_Project_Briefs/` — comes from `20_Progress/` and `10_Areas/`                                                            |
| A reusable output artifact (interview story, portfolio bullet, prompt)  | `60_Claude/35_Outputs/` with `source_concepts:` provenance                                                                            |
| A daily / weekly / monthly review                                       | `60_Claude/50_Reviews/`                                                                                                               |
| A dashboard or index                                                    | `60_Claude/44_Indexes/`                                                                                                               |
| A session log entry                                                     | append to `60_Claude/07_AI_Information/Session Logs/log.md`                                                                           |
| A new template, writing workflow, or CLI tool                           | `30_Order/` — only when the task is explicitly building one                                                                           |
| A visualization for a concept, project, pdf, source, or AI input        | `10_Areas/Excalidraw/`, in an area or project subfolder                                                                               |
| Information about the whole vault for any AI tool                        | `60_Claude/07_AI_Information/` — conversations, logs, what to read, how `60_Claude` works                                            |

### Never write to

- **The vault root** — no new files or folders directly inside it.
- **`50_Archive/`** — never read, never write. Excluded from all AI context unless the task is explicitly archival.
- **`60_Claude/05_Clippings/`** after capture — raw sources are read-only input; never rewrite them in place.
- **`40_Resources/` in bulk** — this is a curated hub (see its contract). Add a single backlinked entry when it is genuinely reference; never flush a batch of AI distillations into it.
- **`.obsidian/`, `.claude/`, `.cursor/`, `.kiro/`, `.codex`, `.git/`** — settings and tooling only, never notes. (`.claude/` skills and agents may be edited only when the task is building tooling, never to store knowledge.)

---

## The 60_Claude flow model

`60_Claude` is the AI workshop. Anything can be dumped in; value is created when a dump is distilled and routed to a concrete home. The flow:

```
capture        05_Clippings (raw source)   ·   00_Inbox (loose AI output)
   ↓ summarize one source
distill        10_Source_Summaries  →  20_Distilled_Notes (working concept drafts)
   ↓ when a concept is stable and reused
promote        10_Areas/  (canonical domain truth)   ·   40_Resources/ (curated reference)   ·   20_Progress/ (active work)
   ↓ when you need a deliverable
produce        35_Outputs (interview story, bullet, prompt — with source_concepts provenance)
```

What legitimately *stays* in `60_Claude` long-term is the operating machinery, not the knowledge: clippings, source summaries, project briefs, the outputs library, reviews, indexes, and the `07_AI_Information` agent layer. A distilled *concept* is a guest in `20_Distilled_Notes` — once it is trustworthy and reused, it belongs in `10_Areas` (if it is identity-level truth) or `40_Resources` (if it is lookup reference).

**The 40_Resources guardrail.** Promotion into `40_Resources` is curated, not automatic. AI proposes a promotion and backlinks it; you decide whether it earns a place in the reference hub. This is the rule that keeps `60_Claude` from "messing up" `40_Resources`: the workshop never empties itself into your library without review.

---

## Top-level folder contracts

Each folder is defined the same way: its job, what belongs, what does not, who writes, the workflow that moves notes through it, where it stands today, and the open questions.

### Root files

**Job:** the fixed entry points every tool and human starts from.

**Belongs:** `00_Dashboard.md`, `AGENTS.md`, `CLAUDE.md`, `HUMAN_WRITING.md`. Nothing else. Dotfolders (`.claude`, `.obsidian`, `.git`, `.cursor`, `.kiro`, `.codex`) are tooling, not vault content.

**Who writes:** you, and AI only when explicitly editing one of those four contract files.

**State today:** clean. `Random.md` was moved out to `40_Resources`; the root is frozen and matches the contract. This is the win from the last pass — protect it with golden rule #1.

### 10_Areas — identity layer

**Job:** the source of truth for who you are and what you are working toward. The map you would hand someone to explain your life in ten minutes. It should be small and link-dense: a hub per domain that points *out* to the active work in `20_Progress` and the reference in `40_Resources`, rather than holding all the detail itself.

**Belongs:** one or two canonical notes per domain — currently `Career/`, `Trading/`, `Life/`, `UMN/`. Plus two cross-cutting residents: `Excalidraw/` (visual layer) and, for now, the coursework dump.

**What does not belong:** active build work (that is Execution — the AI Market Analyzer specs correctly moved to `20_Progress/Projects/CS/TradingView/`), and raw AI output.

**Who writes:** you, freely. AI patches existing domain notes by heading and never adds new top-level files here without explicit instruction.

**Workflow — and the honest gap:** there is currently *no concrete identity note* here. The folder holds a `UMN/` coursework tree, a generic `Notes/` folder, an `Excalidraw/` folder, `Trading/`, and `Links.md` — but not a single "this is my Career / my Trading thesis / my operating principles" hub. The intended workflow: each domain gets one canonical hub note (`type: evergreen`, `status: tree`) that states the durable truth of that domain and links to the live work and resources. Everything else in the domain folder is subordinate to that hub.

**Open questions:**
- **What is the actual workflow for this folder?** Undecided, and you flagged it. Recommendation: treat `10_Areas` as hubs only. Write four hub notes (Career, Trading, Life, UMN) first; let them link out. Judge success by whether the hub explains the domain without you opening anything else.
- **`Notes/` vs `UMN/` overlap.** `10_Areas/Notes/` (the coursework that moved out of `30_Order`) and `10_Areas/UMN/` both look like course material. Decide one home for coursework so they don't compete.
- **`Trading/` leftover.** The build specs moved to `20_Progress`; confirm what remains in `10_Areas/Trading/` is a thin identity hub, not orphaned project files.

### 20_Progress — execution layer

**Job:** everything actively in motion. If you are pushing on it this term, it lives here with a next action.

**Belongs:** in-progress projects, internship tracking, mentorship, research (UROP/BOOM), degree planning, hackathons. Current shape: `Degree/`, `Internship/`, `Mentorship Program/`, `Projects/` (which holds `AI Second Brain/`, `CS/` incl. the migrated `TradingView/` build, `UROP/`, `Extra/`, and the boards).

**What does not belong:** finished work (→ `50_Archive`), pure reference (→ `40_Resources`), or identity-level truth (→ `10_Areas`).

**Who writes:** AI writes concrete project notes here, drawn from `60_Claude/40_Project_Briefs/` and `60_Claude/20_Distilled_Notes/`. Every `type: project` note carries a `next:` so the dashboard can surface stalls.

**Workflow:** a project starts as a brief in `60_Claude/40_Project_Briefs/`, becomes a live project note here with a `next:`, accrues working notes, and ends archived. `UROP/` is the model — deep, structured, with a learning ladder, mocks, logs, and briefs.

**State and gap:** this is the most operating-system-like folder, but you are right that it is incomplete. It does not yet hold a note for *every* active thread. Target: a one-line audit — can you name something you are working on that has no note in `20_Progress`? If yes, that thread is invisible to the system. The folder becomes an OS only when every active commitment has a tracked note with a next action.

### 30_Order — rules and machinery layer

**Job:** how the vault itself works. This is the structural counterpart to [[HUMAN_WRITING]]: that file governs how prose should *sound*; `30_Order` governs how a note should be *shaped, structured, and filed*, plus the tooling that runs the vault. **Every AI agent must read this folder before writing notes.**

**Belongs:** `Templates/` (the note skeletons — Classes, Capability, Metadata, Headway, plus the MOC), `System/` (the `jarvis-cli` and `claude-workflow` hooks), and — once built — a `Workflows/` area documenting how to write into each folder.

**What does not belong:** knowledge, course material, PDFs, attachments. The litmus test: if it is not a template, a writing workflow, or a tool, it does not belong in `30_Order`. (This is now true — the old `30_Order/Notes/` coursework was moved into `10_Areas`.)

**Who writes:** you. AI reads this folder as mandatory input and edits it only when the explicit task is building a template, workflow, or tool.

**Workflow — and the gap:** today `30_Order` has the templates and the CLI, but **not** the written per-folder workflows you want. That is the missing piece. The target: a `30_Order/Workflows/` set that says, concretely, "to write a distilled note, use this template, this frontmatter, file it here, backlink it there" — one short doc per note type. Until that exists, agents only have templates, not the procedure around them. `CLAUDE.md`, `AGENTS.md`, and `HUMAN_WRITING.md` should each point at `30_Order` as required pre-write reading.

### 40_Resources — reference hub

**Job:** your private search engine. This is your Google, YouTube, and knowledge shelf in one place — the guides, concepts, links, tools, and docs you reach for to do the work. Everything in `10_Areas` and `20_Progress` should be able to link *into* here for the resource it needs.

**Belongs:** `Capability/` (AI role definitions, the Capability Engine guide), `CS/` (AI tooling notes, concepts, links, repos), `Obsidian/` (the system docs, including this note and the Vault Operating System). Course reference material can live under the new `UMN/` here. Every entry backlinks to the `10_Areas` domain it serves.

**What does not belong:** raw captures (→ `05_Clippings`), one-off source summaries (→ `10_Source_Summaries`), or active project notes. And critically: **not a dumping ground for AI distillations.**

**Who writes:** you curate. AI may add a single, backlinked reference entry when it is genuinely lookup material, and otherwise *proposes* promotions for your review. The worry that `60_Claude` will mess this folder up is handled by the guardrail in the flow model: nothing bulk-promotes in.

**Where this is heading:** you plan to wire PKM tooling into this layer — NotebookLM over the reference corpus, scheduled tasks that refresh and improve entries, a self-improving agent loop. That only works if the hub stays curated and consistently backlinked. Treat structure here as load-bearing for the tools you are about to add.

**State today:** the most definitive folder. One cleanup note: `Random.md` landed at `40_Resources/` root and should be filed or moved to `00_Inbox`. The outdated `CS/AI/AI Workflow.md` and `CS/AI/MCPs.md` still read as current and should be bannered or refreshed.

### 50_Archive — dead-letter office

**Job:** historical material out of active rotation but not deleted.

**Belongs:** completed courses, finished projects, superseded plans. Currently holds `copilot/`.

**Who writes:** you, during deliberate archival. **AI never reads and never writes here.** The hard exclusion is a feature — it keeps stale content out of AI context.

### 60_Claude — AI workshop and orchestration layer

**Job:** where every AI agent captures, drafts, distills, produces, and coordinates. The one place an agent can write without second-guessing — and the home of the default landing zone (`00_Inbox`). Knowledge flows through it and is promoted out; the operating machinery stays.

**Who writes:** every AI agent, freely.

**Numbering:** the subfolder numbers are intentionally non-sequential (`00, 05, 07, 10, 20, 35, 40, 44, 50`) to leave room for insertion. That is your scheme, not drift — keep it stable so links don't break.

#### 60_Claude subfolder contracts

| Subfolder | Holds | AI behavior |
|---|---|---|
| `00_Inbox/` | loose AI output awaiting filing; **the default landing zone** | write freely; review and route out regularly |
| `05_Clippings/` | raw clips, web captures, videos, imports (`Web/`, `Videos/`, `AI Conversations/`) | write on capture only; never rewrite in place |
| `07_AI_Information/` | the AI operating + memory layer (see below) | the agent's map and memory; patch the docs, append the logs |
| `10_Source_Summaries/` | one summary per source (`Web Ingestion/`, `Video Ingestion/`, `Github Ingestion/`) | write from clippings; one source in, one summary out |
| `20_Distilled_Notes/` | working concept drafts + `Synthesis/` | write; promote stable concepts to `10_Areas`/`40_Resources` |
| `35_Outputs/` | reusable deliverables (stories, bullets, prompts) | write with `source_concepts:` provenance |
| `40_Project_Briefs/` | synthesized project plans | write; feed `20_Progress` |
| `44_Indexes/` | dashboards, indexes, Field OS, `Bases/` | write; prefer Dataview/Bases over hand-maintained tables |
| `50_Reviews/` | daily / weekly / monthly reviews | write on cadence |

#### The distinction that was unclear: Distilled Notes vs Outputs

These felt vague because they were never given a sharp edge. The edge:

- **`20_Distilled_Notes` is knowledge you understand.** Input → understanding. It answers *"what do I actually know about X?"* Examples already present: *Cognitive AI*, *AI-Assisted Trading*, *Career Strategy*, *Rust Ownership vs OCaml Immutability*. The consumer is **you, learning**. It is internal.
- **`35_Outputs` is an artifact you produce for external use.** Understanding → deliverable, with `source_concepts:` pointing back at the distilled notes it came from. It answers *"what can I show, send, or reuse?"* Examples already present: *BOOM Systems Engineering Bullet*, *Plan-First Coding Prompt*, *Rust Type Safety Story*. The consumer is **someone else** — a recruiter, an interviewer, a future prompt.

One-line test: if it teaches *you*, it is distilled; if it is something you hand to *another person or system*, it is an output. Keep both — they have different consumers and the provenance link (`source_concepts:`) is what makes the outputs trustworthy. Do not merge them; do enforce the link.

#### 07_AI_Information — the AI operating and memory layer

This is the folder the previous version of this note ignored, and it is central to your goal of agents that talk to each other and read the vault correctly. **It is how any AI tool learns this specific vault: what is in it, where things live, how to interlink, how `60_Claude` works, and what has happened before.**

**Job:** the agent's map and memory. Two functions:

1. **The map / onboarding.** How to read and write *this* vault. What each folder is (it points here, to the Architecture, and to `30_Order` for the writing rules), how interlinks and frontmatter work, what to read first on a cold start. `AI_CONTEXT.md` is the manifest; `Agent Operating Guide.md` and `Jarvis Writing and Formatting.md` are the operating docs; `Plugins.md` covers the tooling surface.
2. **The memory.** `Session Logs/log.md` is the continuity record appended after every meaningful change. `AI Conversations/` is where cross-tool conversations are captured so one agent can pick up what another did.

**Relationship to `30_Order`:** clean split, no overlap. `30_Order` holds the *rules and machinery* — the templates and the writing workflow. `07_AI_Information` holds the *map and memory* — what's in the vault and what happened — and it *points agents at `30_Order`* when they need the writing procedure. Rules in `30_Order`; orientation and history in `07_AI_Information`.

**Who writes:** AI writes here freely — logs and conversations grow continuously; the operating docs are patched in place.

**Where this is heading:** this becomes the spine that `CLAUDE.md`, `AGENTS.md`, and `HUMAN_WRITING.md` all reference, so every tool — including MCP-only agents — gets the same orientation. It must explain, in detail, how to use `30_Order` to write notes across the vault. Target: a single "read me first" vault map here that any new agent can absorb in five minutes, plus a living conversation/log record that makes the system continuous across tools and sessions.

### Excalidraw — visual layer (under 10_Areas)

**Job:** diagrams and visual thinking for any concept, project, source, or AI input, organized by the area or project they explain. It now lives at `10_Areas/Excalidraw/` because a diagram belongs to the domain it illustrates.

**Who writes:** you, and AI when explicitly generating a diagram. Link every drawing from the note it supports.

**State:** thin and underused relative to the visual-thinking ambition in the plugin docs. Target: every significant project or concept that benefits from a picture has one, linked both ways.

---

## What is still messy — open questions

Honest list of what is unresolved as of 2026-05-31. These need your decisions, not silent guesses.

1. **`10_Areas` has no concrete identity notes yet.** The folder's whole purpose — canonical domain hubs — is unbuilt. This is the biggest content gap. Decision: write the four hub notes, or keep deferring?
2. **Coursework has two possible homes** inside `10_Areas`: `Notes/` and `UMN/`. Pick one.
3. **`30_Order` lacks the written workflows.** You want every agent to read `30_Order` and learn how to write in each folder, but only templates and the CLI exist there. The `Workflows/` docs need to be written. Until then "read `30_Order` before writing" only gets an agent halfway.
4. **`40_Resources` promotion policy needs to be enforced, not just stated.** The guardrail is written here; it should also live in `AGENTS.md` and be checked by the curator agent, or `60_Claude` will eventually leak into it.
5. **`20_Progress` is incomplete.** Not every active thread has a note. It is not yet the execution OS you want.
6. **Dashboard may still query `10_UMN`.** `00_Dashboard.md` had Dataview blocks pointing at a non-existent `10_UMN`. Confirm they now point at `10_Areas/UMN` (and wherever coursework finally lands), or the dashboard keeps lying.
7. **Link scatter persists.** `Links.md` exists in several places (`10_Areas/Links.md`, `40_Resources/CS/Links.md`, `20_Progress/Projects/CS/TradingView/Links.md`). Decide one canonical links note per domain.

## Build order — making this real

Cheapest, highest-leverage first. This is about writing the *missing structure*, not moving more files.

**Step 1 — make the rules readable by every agent.** Embed the Write Contract (golden rules + routing table) into `AGENTS.md`, and add "read `30_Order` before writing" to `CLAUDE.md`, `AGENTS.md`, and `HUMAN_WRITING.md`. This closes the exact gap that caused the root-folder incident.

**Step 2 — write the `30_Order/Workflows/` docs.** One short procedure per note type (clipping → summary → distilled → promotion; project brief → progress note; output with provenance). This is what turns templates into a followable method.

**Step 3 — write the `07_AI_Information` vault map.** A single "read me first" note: folder roles in one table, what to read on cold start, interlink and frontmatter conventions, and how to use `30_Order`. Point `AI_CONTEXT.md` at it.

**Step 4 — write the four `10_Areas` hub notes.** Career, Trading, Life, UMN — each a canonical hub that links out. This finally gives the identity layer real content and makes the rest of the model concrete.

**Step 5 — make it self-enforcing.** Have the `vault-curator` agent and the `/lint-claude-layer` skill check this contract every run: flag any root-level non-contract file, anything in `30_Order` that is not a template/workflow/tool, any `10_Areas` file that looks like active project work, any bulk write into `40_Resources`, and any `20_Distilled_Notes` concept stable enough to promote.

## Relationship to the other contract docs

- **This note** — what each folder is for and where any note goes. The folder-placement source of truth.
- [[40_Resources/Obsidian/Vault Operating System]] — the property/frontmatter schema and the capture→distill→review workflows. Its "Folder Logic" section is the older, thinner version of this note; this note supersedes it for placement.
- [[HUMAN_WRITING]] — how prose must sound. The voice half of the writing standard; `30_Order` is the structural half.
- [[AGENTS]] — root behavioral rules; should embed this note's Write Contract verbatim so MCP-only agents inherit it.
- [[CLAUDE.md]] — Claude-specific workflow, skills, and agents.
- [[AI_CONTEXT]] — the manifest that points all tools at the files above; lives in `07_AI_Information`.
- [[60_Claude/40_Project_Briefs/Vault-Audit-2026-05-29]] — the instruction-spine health audit and 3-month build roadmap. Complementary: it audits the instructions and tooling; this note defines the folders.

*Rewritten by Claude (Cowork session) 2026-05-31 to match the reorganized vault. This is the placement contract — when reality and this note disagree, fix one of them deliberately, never silently.*
