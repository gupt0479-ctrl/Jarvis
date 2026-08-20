---
type: evergreen
status: sprout
created: 2026-08-20
updated: 2026-08-20
tags:
  - system
  - standards
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Log]]"
  - "[[20_Progress/AI/Claude Code/Write Log]]"
  - "[[60_Claude/07_AI_Information/Session Logs/log]]"
  - "[[30_Order/Standards/Review Standard]]"
---
# Log Standard
==A log is a real, ongoing, dateable stream of events — not a one-time note wearing a log's frontmatter. Before creating one, name who is responsible for making entries land, the same way this vault already names a responsible mechanism for sync and capture.==
This is the content and lifecycle standard for append-only logs in this vault (`## [YYYY-MM-DD] tag | title` entries, oldest-preserved, newest-first or newest-last by the file's own stated convention) — [[60_Claude/07_AI_Information/Session Logs/log|the main Session Log]], [[20_Progress/Projects/AI Use/Claude Kit/Log|Claude Kit/Log.md]], and any future log this vault creates. It governs a different question than [[30_Order/Standards/Review Standard|Review Standard]]: Review Standard says what a periodic *review* of a log must contain; this Standard says when a *log itself* is worth creating, when to extend one instead, and how to keep it from going silent without anyone noticing.
## Why this Standard exists
Written 2026-08-20, the first time this vault's actual logging reliability was checked systematically rather than assumed. Two real problems found in one pass: `Write Log.md` duplicated `Claude Kit/Log.md`'s exact heading convention and much of its subject matter, created without checking whether the job already had a home — then sat silent for 21 days because nothing was ever wired to write to it. `Session Logs Board.md` queried a folder that never existed, broken from the day it was created, never fixed because it had zero real dependents to force the question. Both are the same underlying mistake at different stages: creating a log-shaped note without first checking whether it duplicates an existing one, and without naming who or what keeps it fed.
## What makes a log worth creating
A log earns its own file when it tracks a **real, ongoing, dateable stream of events** distinct enough from every existing log's actual scope (not just its stated scope) to survive a direct side-by-side comparison. Concretely: could a new entry in this log be mistaken for an entry that belongs in an existing log, by someone who has both open? If yes, it doesn't earn a new file — extend the existing one, even if the existing one's original scope statement doesn't quite cover it. A log's *written* scope is not the same as its *earned* scope; earned scope is whatever it turns out to actually be used for once real entries accumulate.
> [!WARNING]
> Creating a new log because an existing one's stated scope feels slightly too narrow, without checking whether extending its stated scope is cheaper than maintaining a second file. `Write Log.md` existed because "structural changes to the whole Claude Code layer" felt broader than "second-brain-claudekit's tool-pipeline stages" — in practice, every real entry that landed anywhere landed in the narrower log, and the broader one went unused. The felt-need for a wider scope didn't turn into real, separate content.
## When to prefer extending an existing log over creating a new one
Default to extending. Creating a new log is justified only when an existing log's entries would become noticeably harder to scan or use if the new content were mixed in — real volume or real subject-mismatch, not a hypothetical one. The worked example: [[20_Progress/Projects/AI Use/Claude Kit/Log|Claude Kit/Log.md]] earned its own file because second-brain-claudekit's tool-qualification-stage activity (sandbox → tested-tools → promoted decisions) is dense and specialized enough that mixing it into [[60_Claude/07_AI_Information/Session Logs/log|the main Session Log]] would bury it — the same reasoning [[20_Progress/Projects/AI Use/Claude Kit/Tool Map|Tool Map.md]] earned its own file instead of being a section in some other note. `Write Log.md` did not clear that bar — its actual entries (5, all one day) never demonstrated enough distinct volume to justify a second file, and extending `Claude Kit/Log.md`'s own stated scope by one sentence would have cost nothing.
## The core lesson: prefer automated or scheduled triggers over pure memory
Every log in this vault that stayed reliably fed did so because something other than memory fed it, or because a human explicitly owns feeding it and has kept doing so. Every log that went silent did so because it depended on someone remembering, with no name attached to that responsibility. Before creating or continuing to maintain a log, answer one question explicitly and write the answer into the log's own header:
- **Is there a mechanism that writes to this log without a human remembering?** Name it — a hook, a scheduled script, a skill's own logging step (`/export-ai-session`'s Tool log row, `sync-all.sh`'s `_All-Projects-Sync-Log.md` line). If yes, that mechanism's actual reliability is what matters, not its existence — verify it's still firing, the same way this vault's conversation-capture and sync mechanisms get spot-checked against real evidence, not trusted from their own past success.
- **If no mechanism exists, who is the named human (or agent, explicitly directed) responsible for remembering?** Write that name or role into the log's header, not left implicit. A log with no mechanism and no named owner is the `Write Log.md` failure mode waiting to happen again — it will go silent, not might.
> [!WARNING]
> Writing "manual, session discipline" as the trigger without naming who. `Write Log.md`'s header said its entries came from "direct session discipline" and never said whose — that vagueness is exactly what let 21 days pass without anyone treating it as their job.
## Per-Entry Standard
- Heading format: `## [YYYY-MM-DD] tag | title`, one line, matched exactly across every log in this vault — not reinvented per file.
- Entries are append-only: never edited or removed after being written, corrections land in a new dated entry that references the one being corrected, not a silent rewrite of history.
- An entry states what was verified true, not what was assumed or reported by another source without independent confirmation, per this vault's general "verify before write" discipline (`AGENTS.md`).
## Done Conditions
- The log's own header names its trigger mechanism or its responsible human/agent, explicitly — never left implicit.
- Before creating a new log, an explicit check against every existing log's *actual* (not just stated) scope is recorded somewhere findable — a sentence is enough, but it must exist.
- No `---` in the body; zero blank lines except after a callout; no duplicate frontmatter keys — same house rules as every other note type in this vault.
- A log found silent for longer than its own stated cadence gets investigated for root cause (broken mechanism vs. lapsed habit) before either being fixed or retired — never left ambiguous.
## Gold Standard Example
[[20_Progress/Projects/AI Use/Claude Kit/Log|Claude Kit/Log.md]] — real, dense, dated entries since 2026-07-29, each citing what was actually verified, each linking the notes it updated. [[20_Progress/AI/Claude Code/Write Log|Write Log.md]] (retired 2026-08-20) is the paired negative example worth reading alongside it — same heading format, same general subject area, no named trigger, silent for 21 days, folded into the Gold Standard Example above once that root cause was found.
