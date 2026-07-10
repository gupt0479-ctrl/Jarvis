---
type: decision-log
status: active
created: 2026-07-10
updated: 2026-07-10
related_progress:
  - "[[RESEARCH]]"
  - "[[Postmortem - Stocks-ETFs First, Prediction Markets Second]]"
  - "[[Year-Ahead Base — Fable 5 Architecture Contract]]"
  - "[[Math-First Map — Existing Code to Factor Brain]]"
  - "[[AI Market Analyzer - Strategy Engine]]"
  - "[[Research - Systematic Equity Strategy Edge (2026-06-25)]]"
  - "[[Research - Kronos Foundation Model Deep Dive (2026-06-25)]]"
tags:
  - trading
  - architecture
  - decision
  - session
track:
  - trading
  - ai
next: "Hand Fable 5 the year-ahead base prompt; Cursor finishes .kiro plumbing next"
---
# Session Findings — Cursor Alignment Pass (2026-07-10)

==This note is the source of truth for what was decided in the Cursor Ask-mode alignment session (2026-07-09 → 2026-07-10) before the Fable 5 year-ahead base build.== Older vault notes remain rich context; when they conflict with this file, **this file wins**.

*Readers:* Fable 5 (immediate), future-Anant reviewing the base of TradingView, any agent that must not re-litigate settled law.

## Goal
Capture every material question, reply, and rejected alternative from the alignment pass so the year-ahead base is built from decisions — not from a beginner vibe or a re-opened debate.

## Session Context
*Repo:* `/home/anant_gupta/projects/hub/tradingview` (`research_data`).
*Vault folder:* `20_Progress/Projects/CS/TradingView/`.
*Mode:* research/alignment only until this note landed; Fable 5 executes the hard slice next; Cursor owns leftover `.kiro` plumbing afterward.
*Repo drift vs Postmortem (2026-06-25):* `quality.py` + `read_api.py` exist; no `evidence.py` / `benchmark.py` / `polygon.py` / `cli.py`; quality tests 7.2–7.4 still open; strategy/agents/journal/UI still absent. Ingestion is partial; the decision loop is still 0% code.

## Settled Before This Session (do not re-open)
- Stocks/ETFs vertical ships completely first; Kalshi/Polymarket is vertical 2 later, separate page/nav/data/risk — see [[Postmortem - Stocks-ETFs First, Prediction Markets Second]].
- V1 advisor/paper path; autonomy ladder level 2 target historically; no autonomous real-money execution.
- Python computes facts/signals; AI synthesizes/debates/explains — never invents numbers.
- Zero-cost-first; US large-cap/ETF universe named in RESEARCH (14 symbols).
- Action vocabulary: `WATCH | HOLD | ACCUMULATE | REDUCE | AVOID | INSUFFICIENT_DATA`.

## Question Bank — Full Record

### A — Product framing: personal edge vs monetize?
*Asked:* RESEARCH says not for sale; newer language sounded like product/money-printing. Is output (a) personal trading edge never sold, or (b) eventual SaaS/portfolio product?
*Reply:* **(a) Personal edge.** Single-user local desk; no auth/multi-tenancy; compliance stays private tool; value = paper→real P&L and journal discipline. Portfolio may *mention* the project as proof-of-work; everything built stays private (repo through deployed app). Only for Anant to use.
*Implication:* No multi-tenant architecture. No public advice surface. Portfolio showcases engineering honesty, not a sold trading product.
*Rejected:* Designing for billing, multi-user auth, or “sell the bot.”

### B — Kalshi/Polymarket timing and shared core?
*Asked:* What does “later” mean? Any Kalshi/Polymarket fields reserved now? Referenced failure modes #1 god-object schema, #2 mislabeled CONTRADICTORY, #5 ledger bleed, #9 premature provider generalization.
*Reply:* **No vertical-2 code until stocks/ETFs paper trading is online and being tested.** **No shared core / placeholders at all for now.** Build stocks paper trading, strategy testing, everything first. No Supabase — mainly Python/DuckDB. Graphify stays a docs/graph side-tool as the repo grows.
*Implication:* Zero PM tables, nullable fields, provider stubs, or “thin shared Asset” abstractions in this phase.
*Rejected:* Parallel PM build; reserving schema “just in case.”

### C — Weekly workflow / charting / app vs TradingView.com?
*Asked:* End-to-end weekly session: where look first, when switch, what app shows that TradingView.com does not.
*Reply:* **App first** — base for strategies under test, AI over those strategies, research hub. Switch to external execution surfaces later when the system says a trade should happen at a time; TradingView.com keeps a record of physical trades **in the future**. Now: paper strategies, stock review, in-app graphs with addable indicators. After strategies + agent are proven, move knowledge into real-life execution via TradingView.com. Want **fast-forward** paper trading. When paper system is built and verified ready for real use → then Kalshi/Polymarket version.
*Follow-up — fast-forward meaning?* Both **(a)** historical replay/backtest at accelerated speed writing journal-as-if-time-passed, and **(b)** live paper book on real calendar with UI review jump-ahead. Not cinema playback — **research verification** on past markets; self-improving. Inspired by “3PO”: brain vault → strategy factory → four tests → demo account.
*Four promotion gates (order fixed):*
1. Out-of-sample screening
2. Monte Carlo
3. Walk-forward
4. Deflated Sharpe
Then demo paper account; later portfolio-of-strategies + risk gauge.
*Follow-up — “trade at specific time”?* Paper engine **auto-enters at computed time once thesis is pre-approved**. Paper is the real test of knowledge. After paper generates usable results → wire real-world practice as instructed from the app. Driver’s seat only after strategies work.
*Rejected:* TradingView.com as the research hub; freeform autonomous paper without thesis pre-approval; starting PM before paper readiness.

### Brain / strategy factory — 1 vs 2 vs 3?
*Asked:* (1) fixed factors only improved by journal/tests; (2) AI proposes specs, human gates code, four tests; (3) full 3PO autonomy.
*Reply:* **Sweet spot of 1 and 2.** Journal + cited research + test results promote/demote fixed factors (momentum, quality/FCF, safety, valuation, ETF baseline). Agent may propose new strategy specs from papers; Python implements; four tests must pass; human gates what gets coded. Verify new strategies only if better for us. Outside tests: Anant decides; AI suggests. **Inside approved paper-test windows:** engine has full power to generate paper P&L (timed auto-entry).
*Rejected:* Fully autonomous strategy invention (3); pure fixed-modules with zero proposal path.

### D — Barebone gap table still current?
*Asked:* Confirm or update RESEARCH Barebone gaps given codebase + new decisions.
*Reply:* Update the table; lead with self-improving test-gated strategy lab + local journal; keep Barebone research as rich but outdated context. Table is a **working differentiator**, not frozen forever — then elevated further (see Ambition Raise).

### Ambition raise — “imbecile student project” revelation
*Said:* Draft was directionally right but the bar felt like a CS junior toy. Missing how serious desks use process/math. Need quant-grade proof on equations, code, UI, brain, tests. Research depth; brain that thinks like a professional personal desk; not a lousy beginner platform. Long-run ambition (compound skill and capital) — notes must hold that bar without claiming guaranteed market profits in product language.
*What we locked as the elevation:*
| Lead | Meaning |
|---|---|
| Quant math is first-class | Every score has formula, inputs, as-of, and a test that can kill it |
| Brain before vibes | Citations + journal + tests drive promote/demote; AI suggests; human gates code |
| Proof over narrative | Four gates before demo paper; nothing “feels good” ships |
| Personal multi-year desk | Private; portfolio shows engineering; P&L proof is paper→real later |
*“Best freaking thing” operationalized as:* strictest promotion + cleanest provenance — not flashiest UI.

### Brain-first sequencing — A / B / C?
*Asked:* Vault-research-only first (A), brain module parallel with `.kiro` data (B), or finish ingestion+factors before brain UI (C)?
*Reply:* **(B)** Brain = software module (research store + citations + promote/demote) **in parallel with** finishing `.kiro` ingestion so tests have real data. Fable 5 gets the hard slice (math, brain, research structure). If remaining `.kiro` tasks are easy plumbing, **Cursor** finishes them next — not Fable 5.

### E / method — factors vs Kronos?
*Asked:* Confirm factor stack; Kronos alongside or out?
*User uncertain;* Cursor decided from notes + session:
- **Primary math = fixed factor stack** (momentum 12-1, quality/FCF, safety/vol, valuation FCF-EV, ETF baseline). TA = context only.
- **Kronos = reserved gated evidence slot only** in Fable 5 — no inference, no promote/demote influence until RankIC validation later (per [[Research - Kronos Foundation Model Deep Dive (2026-06-25)]]).
*Why not alongside now:* proof clarity; open inference-cost/cutoff questions; ingestion/fundamentals incomplete; Strategy Engine already defers Kronos behind RankIC > 0.03.

### Fable 5 deliverable shape
*Asked:* design-only / MVP code / both; fundamentals path; brain contents; one-sentence success.
*Reply:* **Both** design notes in vault **and** real implementation (not a disposable “MVP” framing — durable product base). Fundamentals: **design/ingest minimal SEC + FMP in same handoff.** Brain must include citations, strategy specs proposed+approved, test-run records, promote/demote, paper-journal links — plus the **x-factor closed loop**. Success sentence: **base for TradingView a year from now.**

### Env / design-note target (pre-handoff)
*Design notes:* `20_Progress/Projects/CS/TradingView/` (this folder). Fable 5 refers here first.
*`.env` (gitignored):* `POLYGON_API_KEY`, `FMP_API_KEY`, `SEC_USER_AGENT` (identity string, not a key). Optional later: Tiingo/Alpha Vantage/Anthropic.

## Canonical Differentiator (elevated gap table)
==Lead with test-gated self-improving lab + local journal; quant math first-class; proof over narrative.==
| Priority | Gap | Personal response |
|---|---|---|
| 1 | Research feed without promotion discipline | OOS → Monte Carlo → walk-forward → deflated Sharpe → demo paper only if better for *you* |
| 2 | No owned decision memory | Local journal: thesis, rejects, fills, lessons, citations |
| 3 | Math vs AI prose unclear | Python owns signals/tests/fills; AI proposes/explains |
| 4 | Weak audit trail | Evidence: source, timestamp, missing/stale, quality-capped confidence |
| 5 | Opaque/overfit backtests | Vs VOO; costs; drawdown; trade count; literature defaults |
| 6 | No staged autonomy | Suggest → gate code → pre-approve thesis → timed paper auto-entry → real instructions later → driver’s seat only after proof |
| 7 | Charts/decisions split badly | In-app review + indicators for paper phase; TradingView.com later for real-trade record |
| 8 | Product pressure | Personal-only; no auth/tenancy; never sold |
| 9 | Uncontrolled agents | Explicit agent contracts when agents land |

Barebone remains the closest *UX reference* (structured research, not raw chat). We are not cloning it.

## How the Fable 5 Prompt Avoids the “Student Toy” Failure
> [!WARNING]
> The failure mode is a dashboard that *looks* like a trading app while scores are untested folklore and AI prose substitutes for math.

*Avoidance mechanisms baked into the handoff:*
1. **Hard-slice only** — brain + factor math + fundamentals path + four-gate harness + paper contracts; not CLI cosmetics.
2. **Settled law block** — Fable must not re-open personal-vs-SaaS, PM merge, or Kronos-as-peer-driver.
3. **Math-first** — every factor has formula + as-of + kill-test; TA cannot sole-drive actions.
4. **Promotion wall** — no demo eligibility without all four gates.
5. **Closed-loop brain** — citations and tests change module status; vibes do not.
6. **Out-of-scope wall** — `.kiro` plumbing stays with Cursor so Fable does not burn weekly quota on easy leftovers.
7. **Long-run Fable instructions** — ground progress in tool results; self-verify on an interval; memory file; no early stop from context anxiety.
8. **Guardrails** — no fabrication, no execution language, no broker SDKs, no PM schema creep.

## Confidence Gate (stated at session end)
*Concrete output:* durable year-ahead base (brain + factors + fundamentals + four gates + paper contracts + Kronos reserved) in vault + repo.
*Methods:* personal local Python/DuckDB; Python facts; AI suggestions; human gates code; timed paper auto-entry in approved windows.
*Rejected alternatives:* sell/SaaS; unified PM engine; TradingView.com as hub; full 3PO autonomy; Kronos as co-equal signal now; beginner checklist as edge.
*Unique value:* local test-gated journaled strategy lab with quant-grade promotion — accountability, not Barebone clone.
**Confidence: ~95%.** Gate treated as passed for note-writing and Fable handoff.

## Open Questions
- [x] Fable 5 year-ahead base landed AND Cursor completed `.kiro` 7.2–13 leftovers (2026-07-10; 420 offline tests green — see [[Year-Ahead Base — Fable 5 Architecture Contract]] Current State)
- [ ] Live-data shakeout: run polygon/FMP/SEC clients with real keys, ingest the 14-symbol universe, first real replay study
- [ ] RankIC validation pass before any Kronos inference
- [ ] Re-check shared-core shape only after real paper-journal weeks exist (Postmortem residual risk) — still **no PM code** until paper readiness
- [ ] In-app charting library choice (durable, navigable, not a widget junk drawer)

## Related Notes
- [[Year-Ahead Base — Fable 5 Architecture Contract]] — what Fable 5 must implement
- [[Math-First Map — Existing Code to Factor Brain]] — how existing `research_data` files stay clean under math-first
- [[Postmortem - Stocks-ETFs First, Prediction Markets Second]]
- [[RESEARCH]]
- [[AI Market Analyzer - Strategy Engine]]
