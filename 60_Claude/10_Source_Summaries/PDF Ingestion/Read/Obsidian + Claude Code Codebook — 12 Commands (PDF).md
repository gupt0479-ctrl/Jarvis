---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[Claude OS]]"
  - "[[CLAUDE.md]]"
source_url: 60_Claude/05_Clippings/PDFs/Obsidian + Claude Commands.pdf
source_note: "[[Obsidian + Claude Commands.pdf]]"
input_kind: pdf
track: ai
---
# The Obsidian + Claude Code Codebook — 12 Commands — Summary
**Source:** `60_Claude/05_Clippings/PDFs/Obsidian + Claude Commands.pdf`
**Ingested:** 2026-07-04
**Pages:** 7
## Source
A codebook by **Vin (Internet Vin)** documenting the 12 custom Claude Code slash-commands he uses to run his Obsidian vault as a personal operating system — Claude Code + Obsidian + **Obsidian CLI** so the agent sees both files and the link graph.
## Key Claims
- ==The governing principle: "the quality of information the agent has entirely determines what it can do for you — if it doesn't know a lot about you, it can't do a lot for you"== (identical to the Jarvis context-pack thesis)
- **You don't code the commands — you ask Claude Code to create them** for you, then refine the prompt
- The connective tissue is **Obsidian CLI**, which lets the agent follow backlinks and trace how an idea evolved, not just read files
- "Start by writing daily — the commands only work if your vault has context"; build one, test, refine, then the next
## Full Content — the 12 commands
1. **/context** — loads full life/work state (projects, preferences, priorities, current focus) at session start.
2. **/today** — pulls calendar + tasks + daily notes into a prioritized daily plan.
3. **/trace** — tracks how a specific idea evolved over time across the vault (timeline + connections).
4. **/connect** — bridges two domains via the link graph, finding unexpected connections.
5. **/ghost** — answers a question in your voice, from your writing and stated beliefs.
6. **/challenge** — pressure-tests your beliefs; finds contradictions and weak assumptions.
7. **/ideas** — scans the vault and generates an idea report (tools to build, people to meet, topics to investigate, things to write).
8. **/graduate** — extracts undeveloped ideas from daily notes into standalone files.
9. **/closeday** — captures what happened and what you learned (counterpart to /today).
10. **/drift** — surfaces loosely-connected recurring ideas with no clear thread ("what your subconscious is circling").
11. **/emerge** — identifies clusters coalescing into something bigger (project/essay/product-ready).
12. **/schedule** — maps stated priorities to actual time blocks, flagging conflicts between what you say matters and how you spend time.
## Why It Matters
This is the **third independent source** (with second-brain-claudekit and the Jarvis skills themselves) converging on nearly the same Obsidian-as-OS command set — which is strong validation that Jarvis is on the right architecture, and it sharpens the gap list already recorded in [[Claude OS]]: Jarvis has strong equivalents for /context, /today (→/startday), /closeday, /trace (→/trace-topic), /connect (→/connect-notes), /graduate (→/distill-note), but is **missing /challenge, /ideas, /drift, /emerge** — the "surface what you can't see yourself" commands. /drift and /emerge are especially interesting because they do cross-note *pattern discovery*, which is exactly what the `jarvis-memory` semantic-search build (North Star 5.4) would enable. The whole codebook reinforces the vault's own principle that context quality caps agent usefulness — the reason the context-pack discipline exists. Concrete next step: adopt /emerge and /challenge (also flagged from claudekit), and note /drift as a semantic-search-dependent future skill.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/Obsidian + Claude Commands.pdf`
- [[Claude OS]] — the skill roster and the /emerge, /challenge, /drift gap list this confirms
- [[CLAUDE.md]] — the Jarvis skill/command registry
- internetvin.com — source author's site
## Open Questions
- [ ] Adopt /emerge and /challenge (confirmed by two sources now) into the Jarvis skill set?
- [ ] Is /drift buildable now (keyword) or does it need jarvis-memory semantic search to be worthwhile?
- [ ] Does the vault use Obsidian CLI, or only the REST-API MCP — would the CLI add backlink-following the MCP lacks?
## Flashcards
#cards/ai
What principle does Internet Vin's codebook share with the Jarvis context-pack design?::"The quality of information the agent has **entirely determines** what it can do for you" — a well-fed vault is the cap on agent usefulness, so context quality is the leverage point.
Which of Vin's 12 commands are genuine gaps in the Jarvis skill set?::**/challenge** (pressure-test beliefs), **/ideas** (grounded idea report), **/drift** (recurring un-threaded themes), **/emerge** (clusters ready to become projects) — the "surface what you can't see yourself" commands.
Why are /drift and /emerge harder to build well than /trace or /connect?::They do cross-note **pattern discovery** (what's coalescing without your noticing), which benefits from semantic search — the `jarvis-memory` build (North Star 5.4) — rather than simple keyword/backlink traversal.
