---
epoch: 1780036543430
modelKey: "gpt-5.2|github-copilot"
topic: "AI Agent Vault Key Files"



tags:
  - copilot-conversation
---

**user**: What are the most important files that an ai agent reads in this vault first?
[Context: Notes: 40_Resources/Obsidian/Jarvis Enrichment Engine.md]
[Timestamp: 2026/05/29 10:35:43]

**ai**: The vault’s **first-read “spine”** for an AI agent is:

- [[AI_CONTEXT]] — the shared cross-tool context manifest that tells agents what the live context sources are and what to read next. It explicitly instructs agents to read `AGENTS.md` and `HUMAN_WRITING.md`, then use the manifest to find the right live sources for the task. [^1]
- [[AGENTS]] — the “Jarvis Agent Guide” with priority files, folder roles, working rules, retrieval rules, and safety boundaries (including not surfacing secrets and keeping raw capture separate from distillation). [^2]
- [[00_Dashboard]] — the “current control panel” / continuity layer for what’s going on right now (active projects, open tasks, inbox/cleanup). It’s repeatedly named as the live state source to consult before making assumptions. [^1]  
- [[log]] (at `60_Claude/10_Session_Logs/log.md`) — the other core continuity layer for recent AI-assisted work and system changes, used alongside the dashboard. [^1]

In addition, the vault defines **agent + workflow specific first-read packs**:

- For “system/vault work” and anything that might restructure notes: [[40_Resources/Obsidian/Vault Operating System.md]] is called out as a key entry point, and the agent reading order in [[AI Automation and Local Interfaces]] includes it early (after context + writing rules). [^1] [^3]
- For Claude-specific workflows: [[CLAUDE]] is named as a priority file for the existing Claude-layer workflow. [^2]

#### Sources
[^1]: [[AI_CONTEXT]]
[^2]: [[AGENTS]]
[^3]: [[AI Automation and Local Interfaces]]
[Timestamp: 2026/05/29 10:36:04]

**user**: These are the most basic files, provide me with a more deeper understand of this vault. What files would it read when given a complex task?
[Context: Notes: 40_Resources/Obsidian/Vault Operating System.md]
[Timestamp: 2026/05/29 10:37:34]

**ai**: For a complex task, the agent should still start with the **spine**, then expand into **task-specific context packs** (live state → system rules → domain entry points → dashboards/indexes → sources/work artifacts). The vault explicitly lays out this reading order and the main “where to look” files. [^1]

## 1) Always-start spine (orientation + continuity)
- `AGENTS.md` (behavioral rules) [^1]
- `HUMAN_WRITING.md` (writing quality rules) [^1]
- [[AI_CONTEXT]] (manifest that tells the agent what the live sources are and what to read next) [^1]
- `00_Dashboard.md` (current control panel: active projects, open tasks, inbox/cleanup queues) [^1]
- `60_Claude/10_Session_Logs/log.md` (recent AI-assisted work + system changes + previous sessions) [^1]

## 2) If the task might change structure: the “operating contract” layer
If the task involves creating notes, restructuring, or making system-level edits, the agent should pull in:
- [[40_Resources/Obsidian/Vault Operating System]] (canonical operating contract: vault purpose, properties/schema, folder logic, default workflows, enrichment rules) [^1]
- `40_Resources/Obsidian/Claude Pro Workflow.md` (Claude-specific operating rules; listed as a canonical shared source) [^1]
- [[CLAUDE]] (Claude-layer operating contract; includes the “context packs, not vault dumps” rule) [^2]

## 3) Task routing: read the right “domain entry points”
Once oriented, the vault expects the agent to switch to the entry points for the task’s domain (instead of scanning everything):

- **System/vault work:**  
  - [[40_Resources/Obsidian/Vault Operating System]]  
  - `AGENTS.md`  
  - `CLAUDE.md` [^1]

- **UROP / systems / backend:**  
  - `20_Progress/UROP/BOOM Board.md`  
  - `20_Progress/UROP/index.md` [^1]

- **Active projects / career work:**  
  - `20_Progress/Projects/Projects Board.md`  
  - relevant notes under `20_Progress/Career/`  
  - relevant notes under `20_Progress/Mentorship Program/` [^1]

- **AI / agents / workflows:**  
  - `40_Resources/Obsidian/Claude Pro Workflow.md`  
  - notes under `40_Resources/CS/AI/`  
  - relevant notes under `60_Claude/30_Source_Summaries/` and `60_Claude/20_Distilled_Notes/` [^1]

- **Coursework:**  
  - relevant notes under `10_UMN/` (feeder layer; selective enrichment / mirrors) [^1]

## 4) Live dashboards/indexes (for complex tasks with many moving parts)
For multi-step or “diagnose + plan + execute” tasks, the manifest names these as live state sources to consult:
- `60_Claude/60_Indexes/Vault Health Dashboard.md` (metadata drift, orphans, stale inbox, projects missing next actions) [^1]
- `60_Claude/60_Indexes/Claude Layer Index.md` (current Claude-layer outputs) [^1]

## 5) “Complex task” reading pattern (practical sequence)
A typical complex-task read sequence in *this* vault looks like:

1. `AGENTS.md` → `HUMAN_WRITING.md` → [[AI_CONTEXT]] (rules + manifest) [^1]  
2. `00_Dashboard.md` + `60_Claude/10_Session_Logs/log.md` (what’s happening now) [^1]  
3. If structure/editing is involved: [[Vault Operating System]] (+ `Claude Pro Workflow` / [[CLAUDE]] as needed) [^1] [^2]  
4. Pull the domain entry-point files for the task (BOOM board, Projects board, AI workflow layer, etc.) [^1]  
5. Use dashboards/indexes (`Vault Health Dashboard`, `Claude Layer Index`) to locate the relevant notes/summaries/outputs efficiently [^1]  
6. Only then: drill into the specific project notes, source summaries, distilled notes, and clippings relevant to the task (while keeping raw clippings read-only unless asked). [^1]

#### Sources
[^1]: [[AI_CONTEXT]]
[^2]: [[CLAUDE]]
[Timestamp: 2026/05/29 10:38:04]