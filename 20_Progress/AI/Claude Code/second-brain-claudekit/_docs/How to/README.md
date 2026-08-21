# How to — this repo's own pipeline, for a cold read

Second-brain-claudekit's version of Jarvis's Toolkit "How to Use X" pattern (`_docs/Jarvis.md`'s description of `20_Progress/Projects/AI Use/Claude Kit/Toolkit/`) — written 2026-08-19 so a future session, or Anant, can pick up this repo's real, current operating state without re-deriving it from `_docs/Architecture.md`, `_docs/Design.md`, and every dated amendment in between.

| Doc | Answers |
|---|---|
| [`review-system.md`](review-system.md) | How Jarvis's own review system actually works today, and what (if anything) this repo's pipeline activity should feed into it. |
| [`conversation-capture.md`](conversation-capture.md) | What state this repo's session-capture pipeline is actually in right now — not what it was designed to be. |
| [`using-staged-artifacts.md`](using-staged-artifacts.md) | How `agents/`, `commands/`, `hooks/`, `skills/`, `instructions/` staging and promotion actually work, post-2026-08-19 Phase 1 resolution. |
| [`tests-and-promotion.md`](tests-and-promotion.md) | How `tests/` gates a promotion decision, and how that connects to `_docs/Promotion-Criteria.md` and `60_Claude/Qualification-Checklist.md`. |

These are written from `_docs/Jarvis.md` and `_docs/Gaps.md` (both current as of 2026-08-19) — cited throughout rather than re-researched. Where this repo's own state changed *during* this session (conversation-capture, most notably), the doc says so explicitly with a real citation, not a guess.
