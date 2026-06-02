---
type: project
status: active
created: 2026-05-28
updated: 2026-05-28
tags:
  - claude
  - ai-workflow
  - optimization
  - learning-system
notes:
  - "[[CLAUDE.md]]"
  - "[[AI_CONTEXT]]"
  - "[[40_Resources/Obsidian/Claude Pro Workflow]]"
  - "[[40_Resources/CS/AI/Skills/Github Skills]]"
  - "[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]"
---
# Claude Optimization Master Setup

> Full vault audit + external link analysis done 2026-05-28 via Cowork session. This note replaces scattered AI Workflow docs as the canonical Claude setup guide.

## What I Found In The Vault

### Solid Foundation (Keep, Don't Rebuild)

- `CLAUDE.md`, `AI_CONTEXT.md`, `AGENTS.md`, `HUMAN_WRITING.md` — the context spine works
- Skills layer: `/ops`, `/ingest-clipping`, `/distill-note`, `/trace-topic`, `/context`, `/closeday`, `/weekly-review` — already in `.claude/skills/`
- Agents: `research-distiller`, `vault-curator`, `career-operator`, `anti-slop-editor`
- Capability Engine: AI/Trading/Systems/Algorithms/Career Field OS boards, drills, proof dashboards
- `jarvis_ops.py` CLI: health, context, projects, links, report commands
- MCP connections active: `obsidian-jarvis` (Local REST API), `context7`, `playwright`, `openaiDeveloperDocs`
- Knowledge Enrichment queue: 223 candidate notes waiting, infrastructure already built
- `Claude Pro Workflow.md` (created 2026-05-26) is the current canonical workflow doc

### Outdated, Don't Follow

- `40_Resources/CS/AI/AI Workflow.md` — GPT-generated March 2026, assumes ChatGPT Pro as primary. Claude wasn't the main tool yet. Ignore the tool hierarchy and budget math.
- `40_Resources/CS/AI/MCPs.md` — March 2026, mostly about Cursor not Claude. MCP section is conceptually fine but setup details are stale.

### Best Recent Analysis In The Vault

`40_Resources/CS/AI/Skills/Github Skills.md` — created May 2026, already a thorough comparison of the four key repos. Treat it as source of truth for the GitHub skills decision. The vault already knows what's good; it just hasn't installed any of it.

---

## What To Set Up Now (Priority Order)

### 1. Install mattpocock/skills (30 seconds, highest ROI)

108k GitHub stars. Works with Claude Code, Codex, Cursor, Windsurf.

```bash
npx skills@latest add mattpocock/skills
```

Pick: `Claude Code`. Select `/setup-matt-pocock-skills` during install and run it first.

**Why it matters:** Fixes the three most common AI coding failure modes — misalignment before building, code that doesn't work without feedback loops, and architecture that degrades. The skills are small and composable, not a ceremony.

**Which to use and when:**

| Skill | When |
|---|---|
| `/grill-me` | Any new idea or feature before planning |
| `/grill-with-docs` | Any real codebase feature — grills you + builds CONTEXT.md |
| `/caveman` | Whenever a session gets expensive. Cuts token usage ~75% |
| `/tdd` | Before letting Claude make a large code change |
| `/diagnose` | Before speculative bug fixes |
| `/handoff` | Before ending a long session or switching tools |
| `/to-prd` | After a planning conversation — turn it into a doc |
| `/to-issues` | After PRD — break into vertical slice tasks |
| `/zoom-out` | When Claude is stuck in one file, missing the full picture |
| `/improve-codebase-architecture` | After many AI changes, things feel tangled |
| `/prototype` | Hackathon/idea validation before committing to architecture |

Run this in every active project repo (IssueDesk, OpsPilot, Resq, any BOOM work). The `/grill-with-docs` + `/tdd` + `/handoff` trio is the most important.

### 2. Create CONTEXT.md For Each Active Project

This is the "shared language" file. Without it, Claude wastes tokens re-explaining domain terms every session. With it, variables, functions, and plans use the same vocabulary as conversations.

`/grill-with-docs` builds it automatically during a planning session. After the first session, keep it open in Claude's context.

Location: project root or `.claude/CONTEXT.md`.

What goes in it: domain terms (not definitions of what `async` means — definitions of what a "claim," "queue event," or "pipeline stage" means *in this specific project*), key architectural decisions, and what not to change.

### 3. Set Up Conversation Capture (Week 1 of the Three-Month Plan, Still Unstarted)

**The biggest compounding loss right now:** every session disappears. The Three-Month Research Engine plan designed the full architecture. Week 2 hasn't been built.

Start simple — don't build the full SQLite registry yet:

```
60_Claude/05_Clippings/AI Conversations/
60_Claude/30_Source_Summaries/AI Conversations/
```

Create these two folders. At the end of any significant session, ask Claude: `Summarize this session as a conversation note. Include: decisions made, things tried, open questions, related notes.` Save output to `30_Source_Summaries/AI Conversations/YYYY-MM-DD-topic.md`.

This is the highest-leverage week 1 action from the Three-Month plan. It starts the memory compounding loop.

### 4. Set Up A Morning Context Pack Start

The `/ops morning-start` skill already exists. Run it at the start of each Claude session:

```
/ops morning-start
```

What it does: pulls current projects, open tasks, enrichment candidates, session log tail, and surfaces the top 3 triage items. 3-4 minute investment, saves 15+ minutes of re-orientation per session.

For Cowork specifically: start every session by asking Claude to read the context pack (the Claude Pro Workflow doc already has the exact prompt).

### 5. Schedule A Weekly Review (Cowork Scheduled Task)

The vault has `/weekly-review` skill and `60_Claude/50_Reviews/` already. But the review isn't automated.

Use Cowork scheduled tasks: every Sunday at 7 PM, trigger a session that:
1. Runs `/ops health-check`
2. Runs `/weekly-review`
3. Enriches 5 notes from the queue
4. Distills any captured conversations

Ask me to set this up if you want it automated.

---

## For Learning Literally Anything

The infrastructure for this is already built. The workflow just needs to be activated.

### The Learning Loop That Already Exists

1. **Find the topic** → search vault for existing notes
2. **Run `/trace-topic "topic"`** → maps what you know, what's prerequisite, what's missing
3. **Pull sources** → add to `60_Claude/05_Clippings/`
4. **Run `/ingest-clipping "filename.md"`** → creates source summary, enriches related notes, adds backlinks
5. **Enrich the concept note** → use the Jarvis Enrichment Template (definition + mechanism + example + contrast + failure modes + drills)
6. **Create drills** → add flashcard-style questions, schedule with `next_drill` field
7. **Build proof** → link to a project that uses the concept under `used_in`

### Activated Learning Tracks

From the AI Field OS already in the vault:

- **AI agents** → `60_Claude/60_Indexes/Field OS/AI Field OS.md`
- **Trading/finance** → `60_Claude/60_Indexes/Field OS/Trading Field OS.md`
- **Systems** → `60_Claude/60_Indexes/Field OS/Systems Field OS.md`
- **Algorithms** → `60_Claude/60_Indexes/Field OS/Algorithms Field OS.md`
- **Career** → `60_Claude/60_Indexes/Field OS/Career Field OS.md`

Each Field OS has an enrichment queue, proof layer, and drill set. They're ready to run.

### Best External Learning Resources (From Link Audit)

These are the links in the vault worth prioritizing right now:

**AI agents + agentic workflows:**
- HuggingFace Agents Course (free, structured): `https://huggingface.co/learn/agents-course/`
- LangChain Deep Agents with LangGraph: `https://academy.langchain.com/courses/deep-agents-with-langgraph`
- Google ADK Codelabs (hands-on, free): `https://codelabs.developers.google.com/onramp/instructions`

**Full-stack AI app building:**
- Matt Pocock's aihero.dev (the skills author): `https://www.aihero.dev/`
- FullStack Open (free, complete): `https://fullstackopen.com/en/`
- LangChain Academy — broader path available

**Structured learning (free):**
- Google Skills AI catalog: `https://www.skills.google/catalog`
- NVIDIA AI essentials: `https://www.nvidia.com/en-us/learn/ai-learning-essentials/`

**Worth tracking as a course not a bookmark:**
- Algoverse AI research program (apply): `https://algoverseairesearch.org/research`

For each of these: ingest the course structure as a clipping, run `/ingest-clipping`, let Jarvis create a study plan note. Don't collect more courses — collect one and activate it.

### The Thing That Actually Compounds

The enrichment queue has 223 notes. Each enriched note becomes a faster starting point for the next related learning. The goal is not to read 223 notes — it's to enrich 5-10 per week in the topics you're actively working on.

The Dataview query on `00_Dashboard.md` surfaces the top enrichment candidates automatically. Read it each morning.

---

## Claude-Specific Tips For This Subscription

### Rate-Limit Discipline

From `Claude Pro Workflow.md` — this is already written correctly:

- Use Sonnet for everything normal (notes, coding, implementation, enrichment)
- Use Opus only for: cross-cutting architecture decisions, stuck debugging, planning sessions that require broad synthesis
- Start a new session or `/clear` between unrelated tasks
- Use `/compact` when continuing a task in a long session (preserves key context, removes noise)
- Use `/caveman` (once installed) during expensive sessions — 75% token reduction with no accuracy loss

### What Cowork Mode Is Good For (vs. Claude Code CLI)

| Task | Use |
|---|---|
| Vault maintenance, note editing, enrichment | Cowork (this) |
| Repo coding, running tests, multi-file edits | Claude Code CLI |
| Architecture planning, long brainstorms | Claude Desktop |
| Quick capture on phone | Claude mobile |

Cowork has direct file access to the vault via MCP. It's the right surface for what you're doing.

### Context Pack To Start Every Session

```
Read the Jarvis context pack: AGENTS.md, HUMAN_WRITING.md, 60_Claude/7_AI_Information/AI_CONTEXT.md, 00_Dashboard.md, and the tail of 60_Claude/10_Session_Logs/log.md. Then read the specific notes I'm working on. Do not scan the full vault.
```

### Skills That Already Exist In `.claude/skills/`

Run these by typing the command:

```
/ops morning-start     — start the day, orient Claude
/ops health-check      — vault health report
/context               — load project context pack
/today                 — build today's plan
/ingest-clipping "x"   — process a clipping into the vault
/distill-note          — distill a note into evergreen form
/trace-topic "x"       — map what I know about a topic
/connect-notes         — find orphaned notes that should link
/closeday              — end of day summary + session log
/weekly-review         — weekly review workflow
/lint-claude-layer     — audit the 60_Claude layer for drift
```

These exist. Use them.

---

## The Three Things That Will Make The Biggest Difference

1. **Install mattpocock/skills today.** `npx skills@latest add mattpocock/skills` into any active project. Run `/setup-matt-pocock-skills`. The `/caveman` and `/grill-with-docs` skills alone justify it.

2. **Start conversation capture this week.** Create the two folders. End every significant session with a summary note. This is Month 1 Week 2 of the Three-Month plan and it's the foundation of Jarvis's memory layer.

3. **Run `/ops morning-start` every session.** The Capability Engine, enrichment dashboards, and learning tracks are already wired. They just need to be consulted. One habit surfaces all of it.

The vault is better built than most people's setup. The gap is consistent execution of the system already here.

---

## What To Ignore From The Old Workflow Docs

- The "tool per role" system from `AI Workflow.md` (ChatGPT for X, Claude for Y, Perplexity for Z) — you have Claude Pro now, it handles all of this
- The budget math in `AI Workflow.md` — predates the current subscription
- The Cursor-centric MCP setup in `MCPs.md` — MCP in Jarvis now runs through `.mcp.json` and the `obsidian-jarvis` server, not Cursor settings

The `Claude Pro Workflow.md` (2026-05-26) is the correct current reference. This note supplements it with the concrete actions missing from there.

---

## Next Actions

- [ ] `npx skills@latest add mattpocock/skills` in IssueDesk, OpsPilot, or any active repo
- [ ] Create `60_Claude/05_Clippings/AI Conversations/` and `60_Claude/30_Source_Summaries/AI Conversations/`
- [ ] Run `/ops morning-start` at the start of next session
- [ ] Create `CONTEXT.md` in any active project after next `/grill-with-docs` session
- [ ] Activate one learning track from the AI Field OS (pick: HuggingFace agents or LangChain deep agents)
- [ ] Ask Claude to set up a Sunday 7 PM weekly review scheduled task
