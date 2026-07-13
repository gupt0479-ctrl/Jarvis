---
type: project
status: active
created: 2026-07-12
updated: 2026-07-12
related_progress:
  - "[[Session Findings — AI Brain Hub (2026-07-12)]]"
  - "[[Session Recap — AI Brain Hub Questionnaire (2026-07-12)]]"
  - "[[Phase 2 — Strategy Pack Landed (2026-07-11)]]"
tags:
  - trading
  - phase3
  - ai-brain
  - llm
track:
  - trading
  - ai
next: "V1.1 parked: StrategySpec proposer; DuckDB evidence_cards (cards/store.py)"
---
# Phase 3 — AI Brain Hub Landed (2026-07-12)

==Fable 5 completed the Phase 3 one-shot on `feat/phase3-llm-seam`: live structured Analyst/Critic LLM calls bound to `EvidenceCard`/`CriticReview`, evidence-bound prompts, numeric-allowlist fail-closed validation, and an NVDA live smoke. Cursor then polished the desk CLI. **The branch was merged to `main` via PR #4 (commit `c754f00`) during this session** — this closes the last open item in [[Session Findings — AI Brain Hub (2026-07-12)]].==

This note is the **as-built** technical record: what the code actually does, read directly from `src/research_data/agents/`, `src/research_data/cards/`, `scripts/live_ai_card_smoke.py`, and the real card artifacts under `data/cards/` — not the design intent (that's [[Session Findings — AI Brain Hub (2026-07-12)]], which stays the locked-decisions SoT).

## What landed (4 commits, `8c0cf9a`..`0aa1a5a`, merged `c754f00`)

| Commit | What |
|---|---|
| `8c0cf9a` (Cursor) | `cards/` (models, gate_projection, allowlist, validators, writer, empty `store.py`), `agents/` skeleton, `brain/citations.py`, desk CLI skeleton, offline Properties, docs trio |
| `25d5be8` (Fable) | Live `llm_client.py` (litellm.Router + instructor), evidence-bound `analyst.py`/`critic.py` prompts, `runner.py` orchestration, `live_ai_card_smoke.py`, Property 23, 497 tests passing offline |
| `2a51dc6` (Cursor) | `critique-spec` wired through `build_happy_path_bundle` (real FactorEngine data, not synthetic packets), smoke writes vault mirror by default, `--price-source tiingo` CLI default |
| `0aa1a5a` (Cursor) | Doc polish only |

Net diff across the four commits: **~35 files, +3,300/-155 lines** (dominated by `25d5be8`'s 952-line, 14-file change).

## Architecture, as actually implemented

```text
ScorePacket + DataEvidencePacket.evidence_refs
  → assemble_symbol_input() (agents/assemble.py)     — no LLM, builds AnalystInputBundle
  → quality_blocks_llm() gate (E1)                    — MISSING/CONTRADICTORY short-circuits here
  → get_llm_client() (agents/llm_client.py)           — FixtureLLMClient (CI) | LiveLLMClient (live)
  → build_analyst_user_prompt() / build_critic_user_prompt()
  → client.complete_structured(response_model=EvidenceCard | CriticReview)
  → server-side stamping (card_id, max_confidence, data_quality_status, spec_id — NEVER model-authored)
  → validate_evidence_card() / validate_critic_review() (cards/validators.py)
  → one corrective retry on CardValidationError (live only; fixture would just replay the same canned object)
  → write_evidence_card() / write_critic_review() (cards/writer.py) → data/cards/{symbol}_{as_of}_{card_id}.json
  → optional write_vault_mirror() → data/cards/{SYMBOL}_live_mirror.md (one-way, DB wins)
```

### `agents/llm_client.py` — the sole `litellm` import site (C4)

- `LiveLLMClient.__init__` imports `instructor`/`litellm` lazily, so `RESEARCH_DATA_LLM=fixture` (CI default) never pays the import cost — confirmed by reading the constructor: the live imports are inside the branch that only runs when no `structured_create` stub is injected.
- `litellm.Router` deployments are built only for providers whose env key is present (`_build_model_list`): `desk-gemini` (`GEMINI_API_KEY`), `desk-groq` (`GROQ_API_KEY`), `desk-ollama` (`OLLAMA_API_BASE`). Fallback chain is `[{first: rest}]` — Gemini Flash primary, Groq/Ollama fallback, in whatever order keys are present.
- `DEFAULT_MAX_TOKENS = 8192`, not the originally-planned 2048 — bumped because **Gemini 3.x Flash is a reasoning model and spends "thinking" tokens from the same completion budget**, which truncated instructor's JSON mid-object at 2048 (documented lesson in `Docs/fable5_run_memory.md`). Paired with `reasoning_effort="low"` and `litellm.drop_params=True` so Groq/Ollama fallbacks don't 400 on an unsupported sampling param.
- `ROUTER_MAX_FAILURES = 2`: after 2 consecutive failed calls, `LiveLLMClient` refuses further calls for the process lifetime (`LLMClientError`) — fail-fast, not fail-open. Success resets the counter to 0.
- `DEFAULT_GEMINI_MODEL = "gemini/gemini-3.5-flash"` — `gemini-2.0-flash` was retired 2026-06-01; this was reconfirmed live at implement time per the prompt's own instruction, not copied from a possibly-stale `.env.example`.

### `agents/analyst.py` / `agents/critic.py` — evidence-bound prompts

- The analyst system prompt hard-bans `BUY`, `SELL`, `guaranteed`, `risk-free` in prose (HOLD stays legal — this list is **not** `benchmark.py`'s `_EXECUTION_TOKENS`, which also bans HOLD and would be wrong here).
- Numeric discipline is stricter than "don't invent numbers": the prompt bans **digits in prose entirely** except values copied verbatim from a `QUOTABLE_NUMBERS` block the assembler pre-renders at display precision. This closes a real failure mode found during implementation (`fable5_run_memory.md`): models leak digits through indicator names ("the RSI 14") and dates even when told to quote only listed numbers — fixed by banning digits wholesale, naming the indicator-digit trap explicitly, and giving the runner one corrective retry that feeds the exact validator error back. That combination moved live runs from 1/2 pass to consistently green.
- The critic sees **only** the four-key `GateSummaryProjection` (`oos_net_sharpe`, `mc_p5_return`, `wf_pct_positive`, `deflated_sharpe_probability`) plus optionally the card under review's action/confidence/summary — never raw gate `inputs`/`outputs`. `confidence_delta` is Pydantic-constrained `le=0.0` at the model level (`cards/models.py::CriticReview`), not just prompt-enforced.

### `agents/runner.py` — orchestration, and where provenance actually gets stamped

- `run_analyze_symbol`: on the blocked path (`quality_blocks_llm`), it explicitly asserts `client.invocation_count` is unchanged before/after building the deterministic `INSUFFICIENT_DATA` card — this is Property 21's mechanism, not just an output-label check.
- On the happy path, after the LLM returns a card, the runner overwrites `card_id`, `max_confidence`, `data_quality_status`, `confidence` (clamped to the cap), `source_packet_symbol`, `source_packet_as_of`, and `spec_id` server-side via `model_copy(update={...})` — the model's own values for these fields are discarded, confirming B4's "ids are never model-authored" rule in code, not just prompt text.
- **Gap found while reading the real output artifacts** (not in the update dict, so not server-stamped): `EvidenceCard.created_at` and `CriticReview.created_at` are *not* in either update dict. `data/cards/review_a4e924ae-....json` (a real live critic run) has `"created_at": "2023-10-27T12:00:00Z"` — a hallucinated placeholder date the model produced, silently accepted because nothing overrides it. This doesn't violate any guardrail (it's metadata, not evidence prose, and it's not a fabricated market number), but it's a real rough edge worth a one-line fix (`created_at` should join the `update` dict in both `run_analyze_symbol` and `run_critique_spec`) before this ships to anyone who might sort/filter cards by timestamp.

### `cards/` package — no LLM imports, confirmed by grep-shaped tests

- `validators.py::validate_numeric_allowlist` matches floats by rounding both sides to `FLOAT_DISPLAY_DECIMALS=4` (returns/Sharpe/vol) or `CONFIDENCE_DISPLAY_DECIMALS=2` (confidence), then exact-comparing — never substring/string matching, because this repo already renders floats rounded everywhere else (`walk_forward.py`, `cli.py`, `benchmark.py`).
- A real live-run regression is baked into the validator as a named case: **"ranks 3." lexes as float 3.0** (sentence-ending integer + period) but should match the allowlisted int 3 — `validate_numeric_allowlist` explicitly checks `value.is_integer() and allowlist.allows_int(int(value))` as a fallback before rejecting.
- `GateSummaryProjection` (`gate_projection.py`) is a pure rename/extract, confirmed by reading `project_gate_batch`: it reads `TestRunRecord.outputs["oos_sharpe"|"tail_annualized_return"|"fraction_positive"|"deflated_sharpe_probability"]` and republishes under the whitelist names — no recomputation anywhere in the function body.
- `cards/store.py` stays empty (10 lines, reserved comment only) — confirmed still true; DuckDB `evidence_cards` (B2 build #2) has not started.

## Real live artifacts (not fixture output)

`data/cards/` holds actual NVDA cards and reviews from live Gemini runs across 2026-07-11 and 2026-07-12, e.g.:

- `NVDA_2026-07-10_46f18d85....json` — `action=ACCUMULATE confidence=1.0`, citing quality score 76.4700, safety rank 3/14, momentum rank 11/14, P/FCF 102.1619 — every number traces to `ScorePacket` fields (spot-checked: `quality_fcf_score.value`, `safety_score.rank`, `momentum_score.rank`, `valuation.p_fcf`).
- `review_a4e924ae....json` — a live critic **demote** (`confidence_delta=-0.2`) on a card that read `all_passed=true` on the real gate batch, citing `wf_pct_positive=1.0000` as a plausible-overfitting flag — the critic correctly pushed back on a passing gate batch instead of rubber-stamping it, which is exactly B4/D-block's intent (critic may only lower, never raise, and it used that authority here).
- `NVDA_2026-07-12_a547d70e....json` — the blocked path, `action=INSUFFICIENT_DATA confidence=0.0`, `"Analysis blocked: data quality is missing. No LLM call was made"` — proves E1 fires on a real (not synthetic) MISSING packet, not just in a unit test.

## Test status (independently re-verified this session)

```text
source .venv/bin/activate && pytest -q
→ 497 passed in 368.46s (0:06:08)
```

Matches the commit message's claim exactly (497 passed offline, up from the 483 baseline `[[Session Recap — AI Brain Hub Questionnaire (2026-07-12)]]` recorded before Fable's run). New test files: `tests/test_ai_hub_llm_seam.py` (10 tests — prompt shape, fixture happy path, invented-number fail-closed, sentence-ending-integer edge case, critic provenance stamping, planted-Sharpe fail-closed, live-client fail-fast/reset, fixture default), plus 3 new cases in `tests/test_property_ai_hub_cards.py` (Property 23).

## Guardrails verified intact

- `_BANNED_TOKEN_RE` in `cards/validators.py`: `BUY|SELL|BUY NOW|SELL NOW|guaranteed|risk-free`, case-insensitive — HOLD is legal (correctly *not* reusing `benchmark.py`'s stricter `_EXECUTION_TOKENS`).
- E1 fail-closed: `quality_blocks_llm()` gates both `run_analyze_symbol` and `run_critique_spec` before any client call, and both paths assert `invocation_count` didn't move.
- Confidence cap: Pydantic `le=1.0`/`ge=0.0` on both models, plus `validate_confidence_cap` re-checking against `ScorePacket.data_quality.max_confidence` specifically (not just the field bound), plus the runner clamping via `min()` before validation even runs.
- No raw OHLCV ever reaches the model — `score_packet_to_analyst_dict` serializes `ScorePacket` only; the assembler's evidence refs carry table/key/source/timestamps, never bar-level prices.
- `tests/test_ai_hub_security.py` (5 tests, from the Cursor prereq commit) structurally enforces C4 (LLM imports only under `agents/`) and D3 (no non-default gate params outside `tests/`, no hook reading universe/symbols from `params`) via AST/grep-shaped checks, not just convention.

## Deviations / findings vs. the locked design

1. **`created_at` provenance gap** (above) — the only real "ids are never model-authored" exception found by reading live output; not a guardrail violation, just an inconsistency worth a follow-up one-liner.
2. **`.env.example` Gemini alias drift confirmed live**: `gemini-2.0-flash` → `gemini/gemini-3.5-flash`, exactly as the implementer prompt warned would need reconfirmation at run time.
3. **`DEFAULT_MAX_TOKENS` moved from an implicit 2048 assumption to an explicit, documented 8192** — a real correction driven by hitting truncated JSON on a reasoning model, now pinned as a lesson in `Docs/fable5_run_memory.md`.
4. **DuckDB `UUID` → `str` cast bug** in `read_api.py::get_quality_report` — pre-existing since Month 1, only surfaced because the AI hub was the first caller to round-trip a stored quality report through Pydantic's `str` field. Fixed in `25d5be8`.

## PR / branch status (resolved mid-session, 2026-07-12)

`feat/phase3-llm-seam` was merged to `main` via **PR #4, merge commit `c754f00`**, closing the human-in-the-loop step that `Docs/FABLE5_PHASE3_AI_BRAIN_PROMPT.md` explicitly deferred ("Leave green branch. Do not open or merge the PR — human will."). `git branch -a` / `git reflog` confirm: `feat/phase3-llm-seam` → `main` fast-forward-merge lineage is clean, no force-push, no rebase. This is the last open checkbox in [[Session Findings — AI Brain Hub (2026-07-12)]]'s Open Items — see that note for the updated checklist.

## What's still parked (V1.1, explicitly out of scope here)

- StrategySpec proposer (LLM drafts specs) — deferred with the research-proposer swarm.
- DuckDB `evidence_cards` table (`cards/store.py` build #2) — waits until the live card shape has been stable for a while with no breaking field change (per B2's sequencing rule); this session's `created_at` finding is exactly the kind of thing worth fixing *before* that table gets committed, not after.
- Tutor role, multi-agent debate, PM/Kalshi vertical, UI — all still non-goals per G3.

## Companion artifacts from this session

- Knowledge graph refreshed locally: `graphify --update` folded in the 39 changed code files + 15 changed docs (agents/, cards/, Docs/PHASE3_AI_BRAIN_*, fable5_run_memory.md) into the existing 2026-06-25/07-11 graph → repo `graphify-out/` now has 141 communities / 1,747 curated node notes (`graphify-out/jarvis_curated/`) plus the full raw export (`graphify-out/obsidian/`). **Not mirrored into the `60_Claude/40_Project_Briefs/TradingView` vault folder this session** — an earlier attempt to bulk-copy ~1,900 individual files via parallel background agents hit the session's usage limit partway through and was abandoned by explicit instruction; that vault folder was left in a partially-updated, inconsistent state (mix of the 2026-06-25 baseline and a handful of freshly-copied files) and should be treated as stale until a deliberate, smaller-batch sync is run.

## Related

- [[Session Findings — AI Brain Hub (2026-07-12)]] — locked design decisions (A1–G3), the SoT for *why*
- [[Session Recap — AI Brain Hub Questionnaire (2026-07-12)]] — full Q&A transcript
- [[Phase 2 — Strategy Pack Landed (2026-07-11)]] — prior landed-work record, same folder convention
- Repo: `src/research_data/{agents,cards}/`, `scripts/live_ai_card_smoke.py`, `Docs/PHASE3_AI_BRAIN_*.md`, `Docs/fable5_run_memory.md`
