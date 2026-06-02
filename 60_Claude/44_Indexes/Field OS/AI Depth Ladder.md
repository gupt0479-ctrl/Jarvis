---
type: evergreen
status: tree
tags:
  - dashboard
  - capability
  - depth-ladder
created: 2026-04-25
updated: 2026-04-25
notes:
  - "[[AI Field OS]]"
  - "[[AI Question Bank]]"
  - "[[BOOM Board]]"
---
# AI Depth Ladder

Modeled after the [[BOOM Board]]. Curated sequences for reviewing AI concepts at different depths. Refresher lists are hand-picked — Dataview only surfaces the drill queue.

## Core Concepts

These are the load-bearing ideas. If you can't explain these, the rest doesn't hold.

- [[MCPs]]
- [[Gen AI Roadmap]]
- [[AI Workflow]]
- [[Claude Code]]
- [[Cursor AI]]
- [[Ollama]]

## Compare and Discriminate

Adjacent concepts that are easy to confuse. Review these in pairs, not isolation.

| Concept A | Concept B | What to clarify |
|---|---|---|
| RAG (retrieval-augmented generation) | Fine-tuning | RAG adds context at query time; fine-tuning changes model weights. RAG fails when retrieval is bad, fine-tuning fails when data is bad. |
| MCP (Model Context Protocol) | Function calling | MCP is a transport protocol for tool discovery; function calling is the model's interface to invoke tools. MCP wraps function calling. |
| Prompt engineering | Agent orchestration | Prompt engineering shapes a single completion; agent orchestration chains multiple completions with tool use and state. |

## 30-Minute Refresher

1. [[Gen AI Roadmap]]
2. [[MCPs]]
3. [[AI Workflow]]

## 2-Hour Technical Refresher

1. [[Gen AI Roadmap]]
2. [[MCPs]]
3. [[Claude Code]]
4. [[AI Workflow]]
5. [[Cursor AI]]
6. [[Ollama]]

## Deep Relearning Pass

Start at [[Gen AI Roadmap]], then work through each concept note in `40_Resources/CS/AI/` in order. Revisit [[Gen AI Day - 1]] and [[Gen AI Day - 2]] for the original meeting context.

## Overdue Drills

```dataview
TABLE mastery_level, difficulty, next_drill, drill_interval
FROM ""
WHERE type = "concept" AND contains(track, "ai") AND next_drill AND next_drill < date(today)
SORT next_drill ASC
```

## All Tracked AI Concepts

```dataview
TABLE mastery_level, difficulty, status, next_drill
FROM ""
WHERE type = "concept" AND contains(track, "ai")
SORT file.name ASC
```
