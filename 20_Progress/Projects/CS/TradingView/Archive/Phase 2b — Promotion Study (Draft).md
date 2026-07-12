---
type: project
status: '"archived"'
created: 2026-07-11
updated: '"2026-07-12"'
related_progress:
  - "[[Session Findings — Post Base (2026-07-11)]]"
  - "[[Phase 2 — Strategy Pack Landed (2026-07-11)]]"
  - "[[History Depth Blocker — Massive Starter Required]]"
tags:
  - trading
  - phase2b
  - fable-5
track:
  - trading
  - ai
next: Answer Phase 2b questionnaire → write final Fable one-shot prompt after deepen
---
# Phase 2b — Promotion Study (Draft)
> [!NOTE] Superseded 2026-07-12
> This draft's plan ran and landed: 4/4 gates passed on real Tiingo history, `demo_eligible`. See `Docs/PHASE2B_PROMOTION_STUDY_2026-07-11.md` in the repo and [[Phase 2 — Strategy Pack Landed (2026-07-11)]]. Kept for the audit trail, not deleted.

==Hardest remaining desk-proof task. Do not run Fable until history depth is unblocked.==

## One-sentence goal
Same production quality+momentum pack on deep DuckDB history → all four gates at unchanged literature defaults → human promotion by `anant` → demo-eligible → historical replay journal vs VOO with real trade count, costs, and drawdown.

## Why this is the hardest task
Phase 2 proved the *module* and the *fail-closed* path. The desk-is-real bar is **gated replay + journal vs VOO**. That requires enough real history for default WF (not synthetic), honest gate outcomes, and a journal artifact that could survive a portfolio review.

## Preconditions (all required)
1. [[History Depth Blocker — Massive Starter Required]] cleared (DuckDB ≥ ~1135 sessions/symbol)
2. Phase 2 pack merged or available on the working branch
3. Fundamentals usable for equities across the window (one source per symbol)
4. Gate constants untouched
5. Offline `pytest -q` green

## In scope (draft — finalize after questionnaire)
- Deepen verification + study run via existing scripts
- `--record-decision --approver anant` only if all four gates pass
- Honest report if gates fail on deep history (still a valid research outcome)
- Docs/vault update with measured numbers only
- PR to `main` when green

## Out of scope
New strategy invention; Kronos RankIC; analyst/critic agents; Streamlit/UI; full orchestration CLI; PM; loosening gates; paid-history purchase inside the agent (human upgrades Massive)

## Model plan (July quota)
- Deepen + fundamentals refresh + Cursor plumbing: **Composer / Sonnet-class in Cursor** (not Fable)
- Phase 2b one-shot after deepen: **Fable 5** (Claude Code or Cursor) — reserve monthly quota for this
- Do not burn Fable on notes/graphify/ingest

## Open questions
See repo `AGENTS.md` Phase 2b checklist + locked A–E (2026-07-11). **Currently RED** until Massive/Tiingo clears V1 and SEC clears V5. Final Fable implementation prompt deferred until go/no-go green (and Claude Code weekly limit resets).
