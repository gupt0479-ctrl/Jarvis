---
type: concept
course: AI
status: seed
mastery (1/10): 2
created: 2026-03-07
updated: 2026-07-27
topics:
  - "[[MCPs]]"
  - "[[AI Workflow]]"
related:
  - "[[Gen AI Meeting]]"
tags:
  - concept
track:
  - ai
prerequisites:
  - "[[MCPs]]"
used_in: []
evidence:
  - "[[60_Claude/45_Outputs/Plan-First Coding Prompt]]"
difficulty: 3
mastery_level: novice
mastery_score: null
last_drilled: 2026-04-25
next_drill: 2026-05-05
drill_interval: 10
---
# Cursor Workflow Notes
## Resources
- https://www.builder.io/blog/cursor-tips
- [Cursor Rules Link](https://dotcursorrules.com/)
- [Everything about cursor](https://cursor.directory/)
- 
## Important correction
- In Cursor and the broader tooling ecosystem, **MCP means Model Context Protocol**, not “Master Control Program.” MCP is the open standard used to connect AI tools like Cursor to external systems, tools, and data sources.
# 1. What changed between the two videos  
## Video 1 (older workflow, around 2025): main emphasis  
- Cursor is the primary AI editor.  
- The workflow starts with **UI exploration first**, before backend or schema work.  
- The creator uses:  
  - competitor research  
  - screenshots  
  - AI prototyping tools
  - Cursor chat + Supabase MCP for backend/system design  
- Heavy emphasis on:  
  - **keeping work in one chat**  
  - **asking follow-up questions first**
  - **breaking features into smaller steps**  
  - using **Cursor rules** to improve consistency  
- Cursor is treated as the main implementation environment.  
## Video 2 (newer workflow, Jan 2026): main emphasis  
- Cursor is still important, but used more selectively:  
  - primarily for **tab completion**  
  - sometimes for agentic coding with different models  
- Claude Code becomes the main agent for large implementation work.  
- Cursor is now used more as a **multi-model control surface**:  
  - ===GPT-5.2 Codex for long-running refactors===
  - ==Gemini 3 Pro for UI / design taste==
  - ==Composer 1 for faster edits==
- More emphasis on:  
  - **plan first, then execute**  
  - **parallel agents**  
  - **Git worktrees**
  - feature-specific documentation files that keep context current  
  - stronger separation between planning, UI system, and execution  
- The creator also points out newer Cursor capabilities he is not fully using yet:  
  - built-in browser interaction
  - debug mode
  - review / bug tools
  - more agent features
### Practical takeaway  
The newer workflow is less about “let Cursor do everything” and more about:  
- use the right model for the right task  
- keep planning explicit
- use parallel isolated branches
- keep persistent context docs inside the repo  
- avoid one-shot feature generation
# 2. Core lessons that stayed consistent across both videos  
## A. UI-first still matters  
Across both videos, the creator starts by understanding:  
- what the product should feel like  
- what good competitors are doing  
- what patterns should be copied, adapted, or avoided  
This remains one of the most useful points:  
- **do not start by asking the agent to build a vague product**  
- first define:  
  - UX flow  
  - visual direction  
  - important screens  
  - quality bar  
  - constraints  
## B. Images are strong context  
Both workflows use screenshots heavily:  
- screenshots of competitors  
- screenshots of UI bugs  
- screenshots of desired layouts  
This lines up with Cursor’s current browser and agent capabilities, which are built around a more visual workflow for testing apps, editing layouts, auditing accessibility, and converting designs into code.
## C. Smaller scoped tasks beat giant prompts  
The old video says:  
- do not ask for too much at once  
- stay in one chat for one feature  
The new video pushes this further:  
- avoid one-shotting large features  
- build piece by piece  
- let the model write code, but keep architectural control yourself  
This matches Cursor’s current agent guidance: plan first, research the codebase, ask clarifying questions, then build.
## D. Persistent project context is critical  
Older workflow:
- use Cursor rules  
Newer workflow:  
- keep feature documentation files up to date  
- use docs as source of truth  
- reduce repeated file-tagging and restating context  
This maps well to Cursor’s modern context system:  
- **Rules**  
- **AGENTS.md**  
- **Skills**  
- **Commands**
- **MCP servers** 
# 3. Best interpretation of Cursor in 2026  
## Cursor is no longer just “an editor with chat”  
Cursor now has a broader operating model:
- **Tab** for fast inline completion
- **Agent** for multi-file coding tasks  
- **Plan Mode** for upfront reasoning before edits  
- **Browser tools** for testing and visual edits  
- **Debug Mode** for finding root causes  
- **Bugbot** for PR review and autofix  
- **Cloud Agents / Automations** for longer-running or recurring work  
- **MCP integration** for external tools and data  
- **Rules / Skills / AGENTS.md / Commands** for durable workflow behavior.  
## Best current framing  
Use Cursor as a **repo-aware agent platform** with these layers:  
1. **Planning layer**  
   - Plan Mode  
   - PRD / spec / AGENTS.md  
   - rules and commands  
1. **Execution layer**  
   - Agent mode  
   - terminal  
   - codebase search  
   - browser tools  
   - MCP tools  
1. **Verification layer**  
   - tests  
   - lint / typecheck  
   - Debug Mode  
   - Bugbot  
1. **Scale layer**  
   - subagents  
   - cloud agents  
   - automations  
   - worktrees  
# 4. Current Cursor features that matter most beyond the videos 
## 4.1 Plan Mode is now a first-class default  
Cursor’s official guidance strongly favors planning before coding.  
Plan Mode:  
- researches relevant files  
- asks clarifying questions  
- creates a detailed implementation plan  
- waits for approval before building  
Shortcut:  
- `Shift+Tab` rotates agent modes, including Plan Mode.
### Why this matters for your workflow  
This supports the creator’s newer “plan first” habit and is the best default for:  
- PRD-driven development  
- repo changes touching multiple files  
- debugging unclear failures  
- migrations  
- auth or schema changes  
## 4.2 Rules are more structured now  
Cursor’s current docs support:  
- `.md`  
- `.mdc`  
`.mdc` adds frontmatter such as:  
- descriptions  
- globs  
- more targeted rule application
There is also support for **AGENTS.md** in the project root as a simpler alternative for agent instructions.  
### Practical meaning  
The older “just make a big .cursorrules file” idea is no longer the best pattern.  
Better pattern:  
- use **AGENTS.md** for high-level repo behavior  
- use **focused rules** for architecture, testing, style, or specific folders  
- use **skills** for reusable specialized behavior  
- use **commands** for repeated workflows
## 4.3 Browser tools are now a serious part of UI work  
Cursor’s browser tool can:  
- test applications  
- visually edit layouts and styles  
- audit accessibility  
- convert designs into code
### Why this matters  
This directly strengthens the screenshot-heavy UI workflow from both videos.  
Instead of:  
- screenshot → describe bug → retry  
You can now often do:  
- run app  
- inspect visually  
- direct the agent against the actual rendered page  
- use the browser tool alongside screenshots and component code  
## 4.4 Debug Mode formalizes root-cause-first debugging  
Cursor’s Debug Mode is built for hard-to-reproduce bugs and focuses on root-cause analysis before code changes.
### Why this matters  
This matches the newer video’s preference for:  
- avoid blind one-shots  
- reason before changing code  
- handle bugs in a narrower, more surgical way  
## 4.5 Bugbot adds a code review layer  
Bugbot reviews pull requests for:  
- bugs  
- security issues  
- code quality issues  
It can also be configured with autofix flows tied to cloud agents.
### Why this matters  
This is one of the cleanest “new since the old video” additions:  
- older workflow focused on building  
- newer Cursor can now also review and catch issues after implementation  
## 4.6 Cloud Agents, subagents, and automations are the newest scale features 
Current Cursor docs describe:  
- **Cloud Agents** for continuous coding assistance  
- **Subagents** as specialized assistants with their own context windows that can help break down work and preserve main-thread context
- **Automations** that run on schedules or external triggers and can use configured MCPs and models in a cloud sandbox
### Why this matters  
This is the clearest current extension of the video’s “parallel agents + worktrees” idea.  
Modern version:  
- Git worktrees for branch isolation  
- Cursor subagents / cloud agents for task separation  
- automations for recurring agent tasks  
# 6. Best codebase pattern for using Cursor with MCP  
## Recommended repo structure  
```text  
project-root/  
  .cursor/  
    rules/  
  docs/  
    prd/  
    decisions/  
    architecture/  
    debugging/  
  AGENTS.md  
  README.md
```
## What goes where
### `AGENTS.md`
Use for:
- product context
- architecture boundaries
- stack assumptions
- testing expectations
- “do not break these contracts”
Cursor docs describe `AGENTS.md` as a simple project-root file for agent instructions.
### `.cursor/rules/`
Use for narrow, targeted persistent rules such as:
- frontend rules
- backend rules
- migration rules
- test-writing rules
- accessibility rules
Cursor supports `.md` and `.mdc`, with `.mdc` useful when you want descriptions and glob-based targeting.
### `docs/prd/`
Use for:
- feature PRDs
- acceptance criteria
- scoped implementation notes
- edge cases
- “what success looks like”
### `docs/architecture/`
Use for:
- schema notes
- integration maps
- feature ownership
- data flow diagrams
- important invariants
### `docs/debugging/`
Use for:
- recurring errors
- previous root causes
- verified fixes
- logs and failure patterns
# 7. Best practical workflow, updated for 2026
## Phase 1 — Define before coding
1. Capture screenshots of:
    - competitors
    - desired patterns
    - existing UI bugs
2. Write a PRD or feature brief.
3. Decide:
    - scope
    - non-goals
    - affected systems
    - acceptance criteria
4. Attach or reference:
    - PRD
    - screenshots
    - design notes
    - relevant schema or API context
### Best default in Cursor
Open Agent and start in **Plan Mode**. Cursor recommends planning first, and Plan Mode is specifically built for codebase research and implementation planning before edits.
## Phase 2 — Build in small units
Preferred order:
1. shell / route / component skeleton
2. data contract
3. core logic
4. UI wiring
5. edge-case handling
6. tests
7. polish
### Do not do this
- one-shot the entire feature
- ask for broad refactors without a plan
- switch chats constantly for one feature unless context has become polluted
## Phase 3 — Use visuals during UI work
Use:
- screenshots
- browser tool
- exact component references
- “before / after” descriptions
- explicit design constraints
Browser support now makes Cursor stronger for visual iteration than in the older workflow.
## Phase 4 — Verify aggressively
After each meaningful code change:
- run lint
- run typecheck
- run targeted tests
- manually verify UI
- use Debug Mode for confusing failures
- use Bugbot for PR review before merge
## Phase 5 — Scale with isolation
For parallel work:
- Git worktrees for branch isolation
- subagents for task separation
- cloud agents for longer-running jobs
- automations for recurring workflows
# 8. Clear comparison: old video advice vs best current advice
## Still correct from the older video
- do UI exploration first
- gather screenshots
- use competitor references
- keep context rich
- break work into small steps
- ask clarifying questions
- use MCP for schema-aware backend work
- avoid resetting chat context too often
## Updated by the newer video
- Cursor is not just a chat editor anymore
- use **plan-first execution**
- use different models for different task types
- parallel work benefits from worktrees and isolated environments
- maintain repo-local docs that keep context current
- stop trying to one-shot large features
## Updated further by current Cursor docs
- Plan Mode is now a built-in primary workflow
- Rules are more structured with `.md` / `.mdc`
- `AGENTS.md` is officially supported
- browser, debug, bugbot, cloud agents, subagents, and automations are now practical parts of the stack
- MCP config and security guidance are more mature than what many older videos show
# 9. Recommended model/task split inside Cursor
This section comes from the newer video’s usage pattern, adapted into a reusable system.
## Use a fast model when you need flow
Good for:
- quick edits
- small bug fixes
- iterative UI polish
- keeping momentum high
## Use a stronger slower model when you need depth
Good for:
- large refactors
- architecture-heavy changes
- cross-cutting fixes
- migrations
## Use a visually strong model for UI direction
Good for:
- layout refinement
- design language extraction
- “make this screen cleaner”
- screenshot-guided improvements
## Best process
- start in plan mode
- select model based on task shape
- keep the scope narrow
- verify every step
# 10. Rules, skills, commands, and MCP — when to use which
## Rules
Use for:
- durable project behavior
- coding conventions
- folder-specific expectations
- testing and review expectations
Rules can be `.md` or `.mdc`; `.mdc` supports frontmatter and globs.
## AGENTS.md
Use for:
- repo-wide instructions in one simple markdown file
- project overview
- architecture map
- “always remember” guidance
## Skills
Use for:
- specialized reusable behaviors
- portable capabilities
- multi-step workflows the agent may invoke when relevant
## Commands
Use for:
- repeatable slash-command workflows
- common prompts
- routine project actions like `/ship-prd` or `/debug-ui`
## MCP
Use for:
- live access to tools or external systems
- DB schema inspection
- issue trackers
- GitHub
- filesystems
- design APIs
- browser-use style tooling
# 11. Practical implementation notes for your own codebase
## 11.1 Start with the minimum viable Cursor setup
### Step 1
Create:
- `AGENTS.md`
- `docs/prd/`
- `.cursor/rules/`
### Step 2
Add one or two focused rules first:
- coding standards
- testing rules
- no-large-refactor rule
### Step 3
Connect only the MCP servers you truly need first:
- filesystem
- database/schema
- GitHub
- maybe one design/doc server
### Step 4
Use Plan Mode for all work that touches:
- auth
- schema
- deployment
- state management
- routing
- more than 3 files
### Step 5
Adopt browser/debug tools only where they clearly help:
- browser for visual/UI work
- Debug Mode for unclear failures
- Bugbot for PR review
## 11.2 Good initial MCP targets
Most useful first servers:
1. filesystem
2. GitHub
3. database or schema source
4. docs / knowledge base
5. browser-related tooling if your app is UI-heavy
## 11.3 Good project habits
- Keep feature docs current after merges.
- Record accepted architecture decisions.
- Put verified debugging notes in repo docs.
- Keep agent instructions short, concrete, and testable.
- Use worktrees for parallel tasks instead of mixing unrelated edits in one branch.
# 12. Example prompts that fit the current Cursor workflow
## A. Plan-first implementation prompt
```
Read @docs/prd/<feature>.md and @AGENTS.md.  
  
Do not edit code yet.  
First:  
1. Identify the files likely affected.  
2. Ask any clarifying questions needed.  
3. Produce a concrete implementation plan with ordered steps.  
4. Call out risks, unknowns, and any contracts that must remain unchanged.  
  
After I approve the plan, implement the smallest safe diff.
```
## B. UI refinement prompt
```
Use the attached screenshots plus the current implementation.  
  
Goal:  
Match the visual direction more closely without changing core behavior.  
  
Constraints:  
- preserve layout intent  
- improve spacing, hierarchy, and consistency  
- do not refactor unrelated code  
- list the exact files you plan to change first
```
## C. Debug prompt
```
Use Debug Mode thinking.  
  
Problem:  
[paste bug]  
  
Expected behavior:  
[paste expected behavior]  
  
First:  
1. propose likely root causes  
2. identify the smallest set of files to inspect  
3. explain the most probable fix  
4. only then implement the fix  
5. finish with verification steps
```
## D. MCP-backed schema prompt
```
Use the configured database MCP to inspect the existing schema.  
  
I need to add:  
[feature]  
  
First:  
1. summarize the current relevant tables and relationships  
2. propose the smallest schema changes needed  
3. identify migration and rollback concerns  
4. wait for approval before changing application code
```
# 13. Example rule patterns
## Example `AGENTS.md`
```
# Project Agent Guide  

## Product  
This repository contains the main application for [product name].  
  
## Priorities  
1. Correctness  
2. Small diffs  
3. Preserve existing architecture  
4. Clear tests and verification  
  
## Defaults  
- Plan before coding for any task touching multiple files.  
- Ask for clarification when requirements are ambiguous.  
- Prefer the smallest safe change.  
- Keep UI accessible and responsive.  
- Do not invent APIs, fields, or environment variables.  
  
## Verification  
Always finish by listing:  
- lint command  
- typecheck command  
- relevant test command  
- manual verification steps
```
## Example focused rule (`.mdc` style)
```
---  
description: Frontend implementation guardrails  
globs:  
  - "src/components/**"  
  - "src/app/**"  
---  
  
- Preserve existing component APIs unless required.  
- Prefer composition over rewriting large files.  
- Keep accessibility intact.  
- When changing UI, explain why the change improves hierarchy or usability.  
- Avoid unrelated styling churn.
```
These patterns align with Cursor’s current support for `.md` / `.mdc` rules and project-level instruction files like `AGENTS.md`.
# 14. Example MCP config pattern
> Use this as a **shape reference**, not as a copy-paste final config. Verify the exact configuration path and workflow in your installed Cursor version. Current docs emphasize managing MCP in Settings and using environment variables for secrets.
```json
{  
  "mcpServers": {  
    "github": {  
      "command": "npx",  
      "args": ["-y", "@modelcontextprotocol/server-github"],  
      "env": {  
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"  
      }  
    },  
    "filesystem": {  
      "command": "npx",  
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]  
    }  
  }  
}
```
## MCP config rules of thumb
- use environment variables for secrets
- start with as few servers as possible
- confirm each server works before adding the next
- prefer local stdio servers first
- document why each server exists
- remove servers you no longer use
# 15. Recommended “best possible” Cursor workflow for a serious codebase
## The modern stack
### Context layer
- `AGENTS.md`
- `.cursor/rules/`
- PRDs
- architecture notes
- debugging notes
### Access layer
- MCP servers for live external context
- terminal tools
- browser tools
### Execution layer
- Plan Mode
- Agent mode
- model selection by task type
- subagents for separation
### Validation layer
- typed code
- linting
- tests
- Debug Mode
- Bugbot
### Scale layer
- Git worktrees
- Cloud Agents
- automations
This overall setup matches Cursor’s current documented product shape much better than the older “chat + rules + MCP” mental model alone.
# 16. Final distilled guidance
## What the old video got right
- UI-first exploration
- screenshots as context
- MCP for backend/system design
- ask follow-up questions
- smaller prompts
- keep context rich
## What the newer video added
- model specialization
- plan-first execution
- feature docs as living context
- parallel work with isolated branches
- strong warning against one-shot feature generation
## What current Cursor adds on top
- Plan Mode as a primary workflow
- browser-based UI iteration
- Debug Mode
- Bugbot
- subagents
- cloud agents
- automations
- stronger rules and instruction systems
- more mature MCP handling and security guidance
## Best simple rule
For any non-trivial task in Cursor:
1. define the scope
2. attach the right context
3. use Plan Mode
4. implement the smallest safe diff
5. verify immediately
6. capture the result back into repo docs# Cursor Workflow Notes

---

## Deep Dive

### One-Sentence Version

Cursor is a repo-aware agent platform with five layers — context (rules, AGENTS.md, PRDs), access (MCP, terminal, browser), execution (Plan Mode, Agent mode, model selection), validation (tests, Debug Mode, Bugbot), and scale (subagents, cloud agents, worktrees) — and the most important habit is planning before coding.

### What It Is

Cursor evolved from "VS Code with AI chat" into a multi-layer development platform. The key architectural insight: it's not one tool, it's a stack.

**Context layer**: AGENTS.md for repo-wide instructions, `.cursor/rules/` for folder-specific conventions, PRDs and architecture docs for feature context. The model reads these before acting.

**Access layer**: MCP servers for external systems (database schemas, GitHub, filesystem), terminal for commands, browser tools for visual testing.

**Execution layer**: Plan Mode (research → clarify → plan → approve → implement), Agent mode for multi-file edits, model selection by task type (fast model for flow, strong model for depth, visual model for UI).

**Validation layer**: lint, typecheck, tests, Debug Mode for root-cause analysis, Bugbot for PR review.

**Scale layer**: Git worktrees for branch isolation, subagents for task separation, cloud agents for long-running jobs, automations for recurring workflows.

### Why It Matters

- The shift from "chat editor" to "agent platform" means the workflow changes fundamentally. You don't type prompts into a chat — you set up context, select a mode, and let the agent plan before it touches code.
- Plan Mode is the single most important feature for non-trivial work. Without it, the agent guesses at file structure and makes cascading changes. With it, the agent researches the codebase, asks clarifying questions, and proposes a plan you approve.
- MCP integration means Cursor can inspect live database schemas, read GitHub issues, and test in a browser — all without leaving the editor. This is what makes it more than autocomplete.

### Real Example

From the distilled workflow notes: building a feature in Cursor now follows this sequence — (1) write a PRD in `docs/prd/`, (2) open Agent in Plan Mode, (3) reference the PRD with `@docs/prd/feature.md`, (4) let the agent research affected files and propose a plan, (5) approve the plan, (6) implement the smallest safe diff, (7) run lint + typecheck + tests, (8) use Debug Mode if something breaks, (9) use Bugbot for PR review.

The older workflow (paste code into chat, ask for changes) still works for trivial edits but fails for anything touching auth, schema, or multiple files.

### Contrast With

**Cursor vs. Claude Code**: Claude Code is a terminal-first agent — you run it from the command line and it operates on your repo through file reads/writes. Cursor wraps the agent in a GUI with visual tools (browser, debug, bugbot). Claude Code is better for large refactors where you want the agent to run autonomously. Cursor is better when you need visual feedback, incremental control, and multi-model switching.

**Cursor vs. GitHub Copilot**: Copilot is primarily an autocomplete engine — it predicts the next line based on surrounding code. Cursor's Agent mode can plan multi-file changes, run terminal commands, and use MCP tools. Copilot is faster for inline completions; Cursor is more capable for architectural work.

### Source Anchors

- Cursor official docs — Plan Mode, Rules, AGENTS.md, MCP, Debug Mode, Bugbot, Cloud Agents
- Two workflow videos analyzed in this note (older 2025 workflow vs newer 2026 workflow)
- [[MCPs]] — MCP protocol that Cursor uses for external tool access
- [[AI Workflow]] — daily workflow plan showing Cursor in the coding lane
