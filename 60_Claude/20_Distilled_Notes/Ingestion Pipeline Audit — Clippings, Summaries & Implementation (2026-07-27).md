---
type: evergreen
status: sprout
created: 2026-07-27
tags:
  - ingestion
  - audit
  - meta
  - pipeline
notes:
  - "[[GitHub Ingestion Implementation]]"
  - "[[PDF's Ingestion Implementation]]"
  - "[[Web Ingestion Implementation]]"
  - "[[Video Ingestion Implementation]]"
  - "[[Useful Repos - Shortlist]]"
  - "[[How Anant Uses Each Repo]]"
  - "[[Maverick Skills Analysis - Cross-Reference with GitHub Repos]]"
  - "[[Internship Tracking Dashboard — 2027 Calendar, Programs, & Application Pipeline]]"
  - "[[Source Summaries Board]]"
  - "[[60_Claude/05_Clippings/Clippings board]]"
next: "Decide the orphan/duplicate queue below, then rebuild GitHub Ingestion Implementation.md against what's actually installed"
---

# Ingestion Pipeline Audit — Clippings, Summaries & Implementation (2026-07-27)

Full read-through of every file in `60_Claude/05_Clippings/`, `60_Claude/10_Source_Summaries/`, and `60_Claude/20_Distilled_Notes/Sources - Plan/`, cross-referenced file-by-file. Goal: know exactly what survived the pipeline, what stalled, what was never touched, and what was *planned in prose but never actually built* — that last category turned out to be the biggest problem, bigger than any missing ingestion.

## The pipeline model

Every source is supposed to move through three stages:

1. **Capture** — raw file lands in `05_Clippings/` (PDF, web scrape, or GitHub repo entry in `40_Resources/CS/Repos`)
2. **Summary** — `/ingest-clipping` produces a structured note in `10_Source_Summaries/`
3. **Distill** — a `20_Distilled_Notes/Sources - Plan/` note pulls the summary into an actual decision or build plan

A source can legitimately stop at stage 1 (skipped, off-topic) or stage 2 (reference material, not actionable). The problem worth flagging is a source that reaches stage 3 — gets a concrete "build this" verdict — and then nothing happens. That's the real gap, and it's the dominant finding below.

## Track summary

| Track | Raw captured | Summarized | Reached a Sources-Plan note | Verdict |
|---|---|---|---|---|
| PDFs | 28 | 28 (29 files, one dupe) | 22 | Best-run track. Nearly 100% summarized, 79% distilled. |
| Web | 25 | 17 | 8 | Half the summaries never went anywhere. |
| GitHub | ~95 repos | ~89 | ~35 named in the implementation note | Fully triaged, but **zero installs verified** — see "The execution gap" below. |
| Video | 0 | 0 | 0 (implementation file exists and is empty) | Dead. Scaffolding only. |
| AI Conversations | ~86 | — (no Source Summary folder exists for this type) | — (no Sources-Plan note) | Out of scope — different pipeline, see note at bottom. |

## Track 1 — PDFs (best-run pipeline)

All 28 raw PDFs in `05_Clippings/PDFs/` have a corresponding source summary. The 2026-07-03/07-04 Fable ingestion log (`60_Claude/07_AI_Information/Session Logs/log.md`, entries `fable-p4-high`, `fable-p4-mediumlow`, `fable-pass2`) confirms every PDF was processed across three signal tiers (high/medium/low), and the giant `PDF's Ingestion Implementation.md` (2,651 lines) threads 22 of them into five concrete tracks: Career (6 PDFs), Trading Bot (5), Jarvis Vault (1), Outreach (1, shared with Career), Finance/student-discounts (1), plus standalone sections for GitNexus, CodeRabbit, model distillation, and DeepThinksFinance competitive analysis.

**Six PDFs were summarized but never distilled into any track** — reviewed, captured in full, then dropped:

- `Generative AI Mastermind Pre-Reads (PDF)` — no track references it
- `AI Mastermind Workbook Links (PDF)` — same mastermind program, same gap
- `Junior Year Extracurriculars List (PDF)` — irrelevant to a college sophomore's actual timeline; likely safe to archive
- `Find Startup Ideas with Reddit & AI (PDF)` — orthogonal to every active project; low-cost to skip
- `AI Generalist Roadmap — Outskill (PDF)` (raw file: `Road Map.pdf`) — a generalist roadmap that never got compared against the Pivot Guide's roadmap already driving the Career track; worth 15 minutes to check for contradictions, then archive
- `TRIBE v2 — Foundation Model for In-Silico Neuroscience (PDF)` — flagged **high-signal** in the original ingestion pass, yet touches nothing else in the vault (no BOOM link, no trading link, no course link). Either this was mis-triaged as high-signal, or there's a reason it matters that never got written down. Worth a direct question to the user rather than a guess.

**One structural duplicate:** `Ultimate Guide to Winning Hackathons (PDF).md` exists both in `10_Source_Summaries/PDF Ingestion/Read/` and directly in `10_Source_Summaries/PDF Ingestion/` (root). The 07-04 log shows it was initially skipped, then re-ingested in the same-day `fable-pass2` pass — the second pass wrote to root instead of `Read/`. Diff the two, keep one, delete the other.

**One filing inconsistency (not a duplicate):** `MavGPT AI Resume & Job Search Guide (PDF).md` sits at `PDF Ingestion/` root while all 26 other summaries live in `PDF Ingestion/Read/`. Move it in for consistency.

## Track 2 — Web (half-orphaned)

25 raw clippings in `05_Clippings/Web/` (including the `Security/` subfolder), 17 source summaries, 8 of those 17 reached a distilled note.

**Reached implementation** (8): `The Agent-Ready Roadmap`, `NextWork — Automate Your AI Second Brain`, `Naive — Agent Primitives API` (all three feed `Web Ingestion Implementation.md`); `Hall of Hacks — Winning Hackathon Archive` and `4 Ways to Make Money with the Hermes Agent` (feed their own named distilled notes); `2027 Internship Calendar`, `Fintech Early Programs That Pay`, `Underclassmen Internship List` (feed `Internship Tracking Dashboard`).

**Summarized but orphaned** (9): `The New Coding Interview — 5 Resources`, `Gurwinder — Substack Index`, `Claude Council — Path A Prompt`, `The Hidden Operating System Behind Every Income Ceiling`, `The Output Audit`, `AI Engineering from Scratch`, `Relevance AI — AI Agents for Sales & GTM`, `AI Engineer Roadmap — roadmap.sh`, `GitOps Resource List (mis-titled clips)`. None of these are bad captures — several (Gurwinder, the two Dustin Weiss essays, the coding-interview list) are genuinely reusable — they just never got carried into a track note. This is the single largest pocket of "reviewed once, never touched again" material in the vault.

**Never summarized at all** (8 of the 25 raw clippings): three `Maverick AI Resource Hub` clippings (1/2/3) — correctly skipped, `Clippings board.md` confirms they're byte-duplicates of the Maverick and MavGPT PDFs already ingested, no action needed; `Magic Fretboard` — off-topic, correctly skipped; `App Privacy Policy Generator`, `Compliance Solutions for Websites, Apps and Organizations`, `All-in-One Data Privacy Compliance Solution` — a cluster of three privacy-compliance tool pages, only the first is named in the board's skip log, the other two were never logged either way; two clippings both titled `Where teams and agents work together` (`.md` and `.md` `1`) — one of these appears to be the actual source behind the mistitled `GitOps Resource List (mis-titled clips)` summary, the other was never opened. Worth a quick check of the original URL to confirm what this source actually is before deciding whether it's worth a real title and a real summary.

**Documentation drift found:** `Clippings board.md` lists `Claude Council` as "skipped per signal tiers," but a full summary (`Claude Council — Path A Prompt (web).md`) exists in `10_Source_Summaries/Web Ingestion/`. Either the board is stale (most likely — it wasn't updated after later ingestion passes) or the summary was created from a different source than the board thinks. Low stakes, but the board is supposed to be the map of what's landed where, and right now it's wrong on at least this one entry.

## Track 3 — GitHub (fully triaged, zero installed)

`40_Resources/CS/Repos` holds 95 starred repos across 7 sections. Two master documents already triage effectively all of them with a priority and a concrete action: `Useful Repos - Shortlist.md` (repo-by-repo capability + priority) and `How Anant Uses Each Repo.md` (repo-by-repo "how you'd actually use this today"). `GitHub Ingestion Implementation.md` distills the highest-priority subset into a same-session install order, and `Maverick Skills Analysis - Cross-Reference with GitHub Repos.md` separately cross-maps 100 Maverick prompt-shortcut modes against these same repos, concluding 65% are already covered by installed-or-installable tools and flagging two custom skills — `/challenge` and `/strategy` — as "ship this week, critical path."

This is the most thoroughly *reviewed* track in the vault. It is also the track with the biggest gap between plan and reality, because the plan was never executed:

- `.claude/skills/`, `.claude/agents/`, and `.claude/commands/` contain only Jarvis's own hand-built tooling (context, startday, closeday, trace-topic, connect-notes, distill-note, remove-ai-slop, organize-csci2033, lint-claude-layer, tag-month, weekly-review, ops, the ingesting-clipping and export-ai-session skills, plus the anti-slop-editor / career-operator / learning-agent / research-distiller / vault-curator agents). None of the recommended installs are present: no ECC, no mattpocock-skills, no gstack, no agent-skills-addyosmani, no CPR (`/preserve` `/compress` `/resume`), no context-sync, no obsidian-mind hooks, no graphify, no spec-kit, no claude-code-templates scaffold.
- `~/.claude.json` has no `sequential-thinking`, `context-sync`, `memsearch`, or knowledge-graph MCP server configured — only Jarvis's own servers (`jarvis`, `jarvis-fs`, `the-plan`, `the-plan-fs`), plus `github`, `firecrawl`, `excalidraw-diagram`.
- `/challenge` and `/strategy` — the two skills Maverick Skills Analysis called "critical path, ship this week" — don't exist anywhere in `.claude/`.

Every "Install Order (This Session)" item in `GitHub Ingestion Implementation.md` is still a to-do, three weeks after it was written. This isn't a knowledge gap — the triage is excellent and still correct — it's a pure execution gap.

**Duplicate summaries found:** `AI Starred/PageIndex.md` and `Claude Starred/VectifyAIPageIndex 📑 PageIndex Document Index for Vectorless, Reasoning-based RAG.md` are the same repo, summarized twice under different names in different subfolders. Same for `Claude Starred/tradingview-mcp (github).md` and `Claude Starred/tradingview-mcp - AI-assisted TradingView chart analysis.md` — same repo, two files, same folder. Merge each pair and delete the redundant file.

**Summarized in the per-repo folders but never mentioned in either master triage doc** (true orphans, not skipped-on-purpose): `CL4R1T4S`, `polymarket-mcp-server`, `autoresearch`, `gbrain`, `last30days-skill`, `LLM Council skills`, `obsidian-dashboard`, `devops-projects-notharshha`, `devops-projects-techiescamp`, `openbb`, `prompt-eng-interactive-tutorial`, `developer-roadmap`. None of these are large gaps individually, but `openbb` is worth a second look given it's a full open-source trading/investment research platform and the vault already has a heavy trading track (`Trading Resources Integration`, `Hermes Agent`, `Index Fund Investing`) that never once mentions it.

## Track 4 — Video (dead)

`05_Clippings/Videos/` is empty. `10_Source_Summaries/Video Ingestion/` is empty. `20_Distilled_Notes/Sources - Plan/Video Ingestion Implementation.md` exists as a file but has zero bytes of content. This is the only track where the scaffolding was built (folder structure, routing rules in `ingest-clipping.md`, a named implementation-note slot) and nothing has ever been put into it — not one video, ever. Decide one of two things: either there's a real backlog of video content (YouTube talks, course lectures, conference recordings) waiting to be captured and this is a genuine miss, or there isn't and the empty folder + empty implementation note should be deleted rather than left as clutter that looks like unfinished work every time this folder is opened.

## Out of scope — AI Conversations

`05_Clippings/AI Conversations/` holds ~86 files (Cowork, Claude Code, and Cursor session exports across Windows and WSL). This is a different, fully separate pipeline — automatic capture via a global SessionEnd hook plus the `/export-ai-session` skill — and it has no corresponding folder in `10_Source_Summaries/` and no implementation note in `Sources - Plan/`. It was not reviewed file-by-file here because it doesn't feed the ingestion→summary→distillation pipeline this audit is about; it's a separate archive-and-distill loop. If you want the same kind of audit run against that archive, that's a distinct task — flag it separately rather than folding it into this one.

## The one structural finding worth acting on before any of the above

`Internship Tracking Dashboard — 2027 Calendar, Programs, & Application Pipeline.md` proposes a specific folder shape: `10_Areas/Career/Internships/Programs/` with one file per program and five Dataview queries against that folder. That's not what actually got built. The real system at `10_Areas/Career/Internships/` is more advanced than the plan — a tiered `List/Dossiers/` structure (`1 - AI & ML`, `2 - Fullstack`, `3 - CyS & Finance`, `Other`) holding 140+ individual role dossiers, plus a separate `Tracker/Tracker.md` and `Programs/Programs MOC.md`. The distilled note is now describing a system that doesn't match the one in active use. This is a good sign about the underlying work (it outgrew the plan) and a bad sign about the note (it will mislead anyone who reads it expecting to find `Programs/2026-HRT.md`). Update the distilled note to describe the real structure, or mark it superseded and point to the MOC directly.

## Priority queue

**Fix now (low effort, high clarity payoff):**
1. Deduplicate `Ultimate Guide to Winning Hackathons (PDF)`, `PageIndex` / `VectifyAIPageIndex`, and `tradingview-mcp (github)` / `tradingview-mcp - AI-assisted...`
2. Move `MavGPT AI Resume & Job Search Guide (PDF).md` into `PDF Ingestion/Read/`
3. Correct or delete the stale `Claude Council` skip-note in `Clippings board.md`
4. Update `Internship Tracking Dashboard` to match the real `10_Areas/Career/Internships/` structure, or mark it superseded

**Decide (needs your input, not mine):**
1. What is `TRIBE v2` doing in this vault at all, and was "high-signal" the right call?
2. Is Video ingestion a real backlog or dead scaffolding to delete?
3. Are the two `Where teams and agents work together` web clippings worth a real title and a real look, or safe to discard?
4. Do the three untouched privacy-compliance web clippings matter for the portfolio site (there's a live "agent-readable portfolio" thread in `Web Ingestion Implementation.md` that could plausibly need a privacy policy)?

**Build (this is the actual highest-leverage gap — planning is done, nothing is installed):**
1. Run the `GitHub Ingestion Implementation.md` "Install Order" for real: ECC, mattpocock-skills, CPR, context-sync, claude-code-templates, bumblebee — none of these take more than 10 minutes each and the triage has already been done twice
2. Build `/challenge` and `/strategy` as actual `.claude/commands/` or `.claude/skills/` entries — both were marked critical path in May and still don't exist
3. Decide the `openbb` question and fold it into `Trading Resources Integration` if it clears the bar

**Low priority — safe to leave alone:**
The 9 orphaned Web summaries and 6 orphaned PDF summaries are genuine reference material, correctly captured, just not yet needed by an active track. No action required until a project actually needs them — re-litigating each one now would be busywork against `PDF's Ingestion Implementation.md`'s own Classification Matrix, which already says Reference/Archive sources should be skipped past the distilled-note stage.
