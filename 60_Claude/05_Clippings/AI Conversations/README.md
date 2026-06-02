---
type: dashboard
status: tree
created: 2026-05-29
updated: 2026-05-29
tags:
  - clippings
  - ai-conversations
  - readme
notes:
  - "[[60_Claude/07_AI_Information/AI Conversations/README]]"
  - "[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]"
---
# AI Conversations — Raw Archive
This folder is the raw archive for exported LLM conversation transcripts (Claude Code, Claude web, Codex, Cursor, Kiro, ChatGPT, Ollama, future tools).
## Rules
- **Files dropped here are immutable.** Read-only, never rewritten in place.
- Distillation outputs go to `60_Claude/30_Source_Summaries/AI Conversations/`.
- Promotion to durable knowledge (concept notes, project briefs, outputs) requires a manual decision after distillation — not automatic.
## File Naming
```
MM-DD {source-app} - {slugified title}.md
```
Examples:
- `05-29 Claude Code Vault - Audit session.md`
- `05-29 Chatgpt Rag Architecture - Discussion.md`
## Required Frontmatter (Minimum)
```yaml
---
type: input
input_kind: ai-conversation
source_app: claude-code | claude-web | codex | cursor | kiro | chatgpt | ollama | other
title: human-readable conversation title
started_at: YYYY-MM-DDTHH:MM:SS
ended_at: YYYY-MM-DDTHH:MM:SS
project: optional project name
status: raw
tags:
  - #input
  - #...
---
```
## Distillation Workflow
1. Drop raw transcript here with the frontmatter above.
2. Run `/ingest-clipping "60_Claude/05_Clippings/AI Conversations/your-file.md"` or invoke the `research-distiller` agent.
3. Distilled summary lands in `60_Claude/30_Source_Summaries/AI Conversations/` with provenance back here.
4. Promotion to durable knowledge is a separate manual step.
## Related
- [[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]] — defines the conversation memory workstream.
- [[60_Claude/40_Project_Briefs/Jarvis Multi-Agent PKM Plan]] — earlier design for the conversation registry schema.
- [[60_Claude/40_Project_Briefs/Vault-Audit-2026-05-29]] — flags this folder's prior absence as the highest-impact Month 1 fix.
