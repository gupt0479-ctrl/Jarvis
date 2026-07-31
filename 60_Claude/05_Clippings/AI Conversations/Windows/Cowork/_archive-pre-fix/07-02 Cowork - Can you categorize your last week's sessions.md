---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "Can you categorize your last week's sessions"
started_at: 2026-07-02T02:24:10
ended_at: 2026-07-02T02:27:13
project: Cowork
status: raw
session_id: 50f3f67b-1959-4d77-aa4a-61e893763214
tags:
  - input
  - ai-conversation
  - claude-code
---

# Can you categorize your last week's sessions

## You

Can you categorize your last week's sessions? Are any of those Sonnet 4.6 tasks actually Haiku-level? That's often where people find their biggest savings.

## Claude

Here's the breakdown from your last ~38 Cowork sessions (no timestamps or per-session model field exist in this tool, so "last week" here means the most-recent chunk of the session list, and complexity is inferred from content, not verified billing).

**Categories:** coursework/homework (HIST 1103, MATH 2230, Devore Stats, MIT quiz), coding/dev (portfolio, Orby, hackathon projects), vault/knowledge-management ops (Jarvis restructuring, audits), content drafting (LinkedIn, TradingView), admin/logistics.

**Clearest Haiku-downgrade candidates:**

The MATH 2230 / Devore Statistics homework sessions (6+ of them) are pure formula-plug-in probability computation, verified with a Python arithmetic check, output as answer tables — no design judgment. HIST 1103 Quiz 1 and the MIT compliance quiz are closed-book answers matched directly from source text. HIST 1103 final exam and the "big assignment" session were mostly footnote-count verification and word-trimming once the essay existed — checklist work. Two troubleshooting sessions (Claude setup config, Portfolio Claude Code ECC execution) were diagnosing known environment limitations (WSL path, Cursor crash) and producing boilerplate fixes.

**Keep on Sonnet:** anything touching the portfolio/Orby/HiveMind codebase (architecture decisions, OAuth/webhook design, bug root-causing), the Jarvis vault restructuring and audit sessions (multi-file judgment calls), and the HIST 1103 practice-assignment feedback session (real diagnostic reasoning, not templated).

Rough split: roughly a third of sessions look like clean Haiku candidates — mostly the recurring homework and quiz sessions, which is also where the volume is, so that's likely where the real savings sit if you're paying per-session model tier somewhere. The coding/dev and vault-ops sessions justify Sonnet.

One honest gap: I can't confirm which model actually ran each of these — Cowork doesn't expose that field to me. If you're tracking this through usage/billing data somewhere (Anthropic console, a specific dashboard), that'd give a real answer instead of this task-complexity inference.

*Tools used: ToolSearch, mcp__session_info__list_sessions, mcp__session_info__read_transcript, mcp__jarvis__vault_read, mcp__workspace__bash, Agent*


