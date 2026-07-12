---
type: session-recap
status: active
created: 2026-07-12
updated: 2026-07-12
related_progress:
  - "[[Session Findings — AI Brain Hub (2026-07-12)]]"
  - "[[Session Findings — Post Base (2026-07-11)]]"
  - "[[Fable 5 — Read Order (TradingView folder)]]"
tags:
  - trading
  - session
  - ai-brain
  - questionnaire
track:
  - trading
  - ai
next: Human opens PR for feat/phase3-llm-seam; V1.1 proposer / DuckDB
  evidence_cards stay parked
---
# Session Recap — AI Brain Hub Questionnaire (2026-07-12)

==Full Q&A audit trail for this session. Locked decisions SoT: [[Session Findings — AI Brain Hub (2026-07-12)]]. Repo mirror: `Docs/SESSION_RECAP_AI_BRAIN_HUB_2026-07-12.md`.==

## Mission

Design the **AI hub** (thin Analyst + Critic on deterministic packets) for the personal US stocks/ETFs desk (`research_data`), then land **Cursor prereqs** so **Fable 5** can one-shot the LLM seam. Trigger: Phase 2b left `quality_momentum_tilt_top3` **demo_eligible** on tiingo (N=1511) — self-improve work starts from a promotion-grade artifact, not a knowledge dump.

## Verification (human machine, this session)

```text
pytest -q  →  483 passed in ~7 min
analyze-symbol NVDA --quality missing  →  action=INSUFFICIENT_DATA confidence=0.0
```

Post-audit Cursor fix: D5 wired in `scripts/run_quality_momentum_study.py` (`--no-cite-lesson` opt-out); `tests/test_citations_and_projection.py` green.

## Scope correction (before A1)

User's fuller vision (self-improve + sibling PM app + polished UI) = **north star** (`Docs/NORTH_STAR_DESK.md`), **not** V1. V1 = AI hub only. PM/Kalshi parked ([[Postmortem - Stocks-ETFs First, Prediction Markets Second]]). No Streamlit/UI.

---

## Block A — Scope & success bar

### A1 — What is V1?
**Options:** (A) symbol card CLI only (B) analyst+critic on demo_eligible only (C) full proposer (D) A+B (E) A+B+C  
**Lean:** D  
**Answer: D** — Symbol `EvidenceCard` CLI + Analyst/Critic on `quality_momentum_tilt_top3`. Proposer → V1.1 after card eval. No PM. No UI.

### A2 — What closes self-improve in V1?
**Options:** (A) lesson→Citation (B) LLM proposer (C) auto-approve tweaks (D) critic demotion only (E) A+D  
**Lean:** E  
**Answer: E (A+D)** — Journal lessons become `Citation` rows; critic may argue HOLD/DEMOTE; `anant` records every decision. No LLM StrategySpec. No auto-approve.

### A3 — Demo bar
**Options:** (A) offline only (B) one live holding (C) full watchlist (D) A+B+critic artifact (E) UI  
**Lean:** D  
**Answer: D** — Offline Properties + one live holding card + CriticReview. Later **G2 locked live symbol = NVDA** (Phase 2b study already has NVDA +939.09% vs VOO +86.46%).

---

## Block B — Packet contracts

### B1 — Minimum packets
**Answer: D + amendments**
1. Analyst numbers ← **ScorePacket only**; DataEvidencePacket ← **evidence_refs only** (no dual quality blocks).
2. Critic gates ← **GateSummaryProjection** whitelist only (map `oos_sharpe`→`oos_net_sharpe`, `tail_annualized_return`→`mc_p5_return`, `fraction_positive`→`wf_pct_positive`, keep `deflated_sharpe_probability`). Plus PromotionDecision + JournalEntry. Kronos never attached.

### B2 — EvidenceCard schema/storage
**Answer: B** — `cards/models.py` + `schema_version`; write `data/cards/{symbol}_{as_of}_{card_id}.json`; vault YAML = mirror. **CriticReview** separate model. DuckDB `evidence_cards` = **build #2** after live card stable (no migrator in this repo).

### B3 — Number invention
**Answer: D** — NumericAllowlist + critic reject. Floats: round both sides to display precision then compare. Ints: exact. Pin: `FLOAT_DISPLAY_DECIMALS=4`, `CONFIDENCE_DISPLAY_DECIMALS=2`. ε pinned in Property 20 tests.

### B4 — Confidence
**Answer: D** — Cap SoT = `ScorePacket.data_quality.max_confidence`. Critic `confidence_delta ≤ 0`. Final = min(analyst, critic-adjusted, cap).

---

## Block C — Topology

### C1 — Roles
**Answer: B** — Analyst + Critic only. TradingAgents Trader/PM approve via LLM → forbidden (`validate_human_identity` / `_NON_HUMAN_IDENTITIES`). Tutor + research-proposer swarm deferred (not V1 topology).

### C2 — Orchestration
**Answer: E** — `agents/runner.py` + Typer. **No LangGraph** (fixed 2-call linear path). instructor/pydantic-ai + litellm; fixture provider like `csv_fixture`.

### C3 — Provider
**Answer: E** — Live default Gemini Flash; alt Groq; GitHub Models out (retires 2026-07-30); Azure reserve. Training disclaimer in `.env.example`.

### C4 — LLM path boundary
**Answer: E** — Imports only under `agents/`; sole litellm site = `llm_client.py`. Router: Gemini → Groq → Ollama (rate-limit robustness, not a research daemon).

---

## Block D — Citations / human gate

### D1 — Citation ingest
**Answer: E** — `cite-add` / `cite-from-vault` / `cite-from-journal` outside `agents/`. Stable id = `hash(vault_relpath + content_hash(claims_section))` — **no mtime**. Insert-only store → edit = new row. Empty claims OK at ingest; required at PROPOSED use. Manual cite warns on title/author dup.

### D2 — StrategySpec contract
**Answer: D tightened** — `n_trials` = global `count_tested_specs()` only; **never** `declared_n_trials`. Add `params_delta` + `parent_spec_id` (provenance); `params` fully merged at propose. `resolve_hook` at **propose-time**.

### D3 — Forbidden classes
**Answer: D + structural tests** — Gate params never non-default outside `tests/`; hooks never read universe/symbols/cost-bps from `params`; no `kronos_reserved` under `agents/`. Card/critic ban = BUY/SELL/guaranteed/risk-free (**HOLD legal**).

### D4 — Human UX
**Answer: D** — Typer brain cmds complete; analyze/critique partial until Fable. One-way DB→vault mirror in V1. DB wins.

### D5 — Lesson → citation
**Answer: D** — Inject `on_lesson_journaled` at `PaperEngine._journal` for lesson/exit. Study script supplies closure; `--no-cite-lesson` for synthetic only.

---

## Block E — Eval / cost

### E1 — Offline
**Answer: D** — Properties 20–22; hypothesis on float ε; zero LLM invocations on MISSING/CONTRADICTORY; hallucinated ref_key rejected.

### E2 — Live
**Answer: C** — `scripts/live_ai_card_smoke.py` / `--live`; NVDA; planted false Sharpe must fail; not in default pytest.

### E3 — Secrets
**Answer: C** — Keys in `.env`; no raw OHLCV to model; max_tokens + Router fail-fast; smoke prints pass/fail only.

### E4 — Calibration
**Answer: C + `Thesis.source_card_id`** — No Brier in V1. North-star: Brier needs named binary event + probability (action/confidence ≠ that yet).

---

## Block F — Structure

### F1 — Layout
**Answer: C** — `cards/` (5 files + empty `store.py`); `agents/` (llm_client, assemble, runner, analyst, critic).

### F2 — Docs
**Answer: D** — `PHASE3_AI_BRAIN_{PROBLEM_STATEMENT,SOLUTION_DESIGN,RUNBOOK}.md` + `NORTH_STAR_DESK.md`.

### F3 — Vault
**Executed** — folders Canon / Session Findings / Phases / Research / Archive; moves only; Read Order points here.

---

## Block G — Cursor vs Fable

### G1 — Cursor pack
**Answer: D** — Schemas, assemblers, validators, citation CLI, complete brain Typer, D5 wiring, Properties, Docs, fixture LLM. Analyze happy-path placeholder until Fable.

### G2 — Fable cut
**Answer: C** — litellm.Router + structured bind + prompts + FactorEngine happy path + NVDA smoke + CriticReview + vault mirror. No proposer / DuckDB cards / Tutor.

### G3 — Non-goals + merge
**Answer: C expanded + merge (i)** — Also: no fabrication; no confidence over cap; no intraday/tick/options/futures/crypto/margin/leverage; no LLM outside agents/; no TradingView.com trade-record surface; gate **order** immutable; cost-model edits banned. Human opens PR.

---

## Anti-patterns rejected

Student-toy knowledge dump; LangGraph; TradingAgents LLM-approve topology; declared_n_trials; mtime citation ids; dual quality serialization; applying benchmark HOLD ban to cards; auto-promote; UI-as-desk-is-real.
