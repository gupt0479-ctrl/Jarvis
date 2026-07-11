---
type: research
status: sprout
created: 2026-06-25
updated: 2026-06-25
related_progress:
  - "[[AI Market Analyzer - Strategy Engine]]"
  - "[[Trading with Ai]]"
  - "[[RESEARCH]]"
tags:
  - trading
  - ai
  - ml
  - kronos
  - foundation-model
  - research
track:
  - trading
  - ai
---

# Research — Kronos Foundation Model Deep Dive (2026-06-25)

**CRITICAL CORRECTION FIRST:** The previous session summary incorrectly identified Kronos as "Amazon's zero-shot time-series forecasting model." That is **Amazon Chronos** — a different model entirely. The model linked in our vault (shiyu-coder/Kronos on GitHub) is a separate academic work from Tsinghua University, published on arXiv August 2, 2025, accepted at AAAI 2026. Do not conflate the two.

- **Amazon Chronos** — zero-shot time series forecasting, general-purpose, uses text tokenization on numerical series, released 2024, bolt. language-model approach
- **Kronos** (shiyu-coder) — financial-specific, K-line (OHLCV candlestick) data only, specialized tokenizer, trained on 12B candles from 45 global exchanges, published arXiv 2508.02739

---

## What Kronos Actually Is

Kronos is the first open-source foundation model specifically for financial K-line sequences. "K-line" is the Japanese/Chinese candlestick term for OHLCV bars. The model is trained exclusively on financial market data — not on general time series — which is why it's relevant to our project specifically.

**Paper:** "Kronos: A Foundation Model for the Language of Financial Markets"  
**Authors:** Yu Shi, Zongliang Fu, Shuo Chen, Bohan Zhao, Wei Xu, Changshui Zhang, Jian Li (Tsinghua + others)  
**arXiv:** 2508.02739 | Submitted 2025-08-02 | Accepted AAAI 2026  
**GitHub:** https://github.com/shiyu-coder/Kronos  
**HuggingFace:** https://huggingface.co/NeoQuasar/Kronos-base  
**License:** MIT

---

## Architecture

Two-stage design:

**Stage 1 — Specialized Tokenizer**  
Converts continuous multi-dimensional OHLCV data into hierarchical discrete tokens. This is the key departure from generic time series models: the tokenizer is designed specifically for financial market structure — it preserves both price dynamics (OHLC relationships) and trade activity patterns (volume). The tokenizer comes in two variants:
- `Kronos-Tokenizer-2k` — for Kronos-mini (longer context)
- `Kronos-Tokenizer-base` — for Kronos-small and Kronos-base

**Stage 2 — Autoregressive Transformer**  
Decoder-only architecture pretrained with an autoregressive objective over the discrete K-line tokens. This is similar in spirit to GPT (predict the next token) but operating on financial bars rather than text.

**Training corpus:** 12 billion K-line records from 45 global exchanges across all major asset classes (equities, futures, forex, crypto). The breadth of the training set is what enables zero-shot generalization — the model has likely seen market regimes, sectors, and dynamics we haven't explicitly shown it.

---

## Model Zoo

| Variant | Parameters | Context Window | Tokenizer |
|---|---|---|---|
| Kronos-mini | 4.1M | 2048 bars | Kronos-Tokenizer-2k |
| Kronos-small | 24.7M | 512 bars | Kronos-Tokenizer-base |
| Kronos-base | 102.3M | 512 bars | Kronos-Tokenizer-base |
| Kronos-large | 499.2M | — | — (not yet released) |

**For V1 use:** Kronos-small (24.7M params, 512-bar context) is the right balance. Small enough to run locally without a GPU, large enough to have meaningful capacity, and the 512-bar context covers ~2 years of daily data which is our target lookback.

At 512 trading days ≈ 2.0 years at daily resolution (NYSE is open ~252 days/year). This is sufficient to see multiple macro regimes in our OHLCV data.

---

## What "Zero-Shot" Actually Means Here

Zero-shot means: you give the model K-line history for a symbol it has never seen before, and it generates a forecast *without any fine-tuning on that symbol's data*. The foundation model generalizes from its training distribution to new assets.

**What zero-shot does NOT mean:**
- "No data required" — you still need a lookback window of real OHLCV data (up to 512 bars)
- "Always right" — zero-shot performance varies by asset class; results on US large-cap daily data may differ from the paper's benchmark results, which span global markets
- "No validation required" — you must evaluate Kronos's RankIC on your specific universe before trusting it as a strategy input

**When zero-shot fails:** The model may underperform on assets or market regimes underrepresented in its training data. US large-cap stocks during unusual macro regimes (e.g., COVID 2020, rate-hike 2022) are in the training distribution, but the model doesn't know about events after its data cutoff.

**Fine-tuning option:** Kronos supports fine-tuning on a target asset's historical data. For V1, zero-shot is the starting point. Fine-tuning becomes worth it only if we validate that zero-shot is directionally useful but not calibrated correctly for our specific 10-symbol universe.

---

## Input/Output Format

**Input:**

```python
import pandas as pd

# x_df: historical OHLCV bars for the lookback window
# columns required: 'open', 'high', 'low', 'close'
# columns optional: 'volume', 'amount' (amount = price × volume)
x_df = df.loc[:lookback-1, ['open', 'high', 'low', 'close', 'volume', 'amount']]

# x_timestamp: the dates/times for the lookback bars
x_timestamp = df.loc[:lookback-1, 'timestamps']

# y_timestamp: the future dates we want to forecast
y_timestamp = df.loc[lookback:lookback+pred_len-1, 'timestamps']
```

Our `PriceReadAPI.get_price_frame()` already returns a pandas DataFrame with all the required columns. The mapping is direct — the `daily_ohlcv` table has `open`, `high`, `low`, `close`, `volume`, `adjusted_close`. We'd use `adjusted_close` as `close` and derive `amount` as `close × volume`.

**Key parameters:**
- `pred_len`: prediction horizon in bars (days, for daily data). Use 5 for 1-week ahead, 20 for ~1-month ahead.
- `T` (temperature, default 1.0): controls forecast diversity. Higher = wider probability spread.
- `top_p` (default 0.9): nucleus sampling. Controls which token sequences are sampled.
- `sample_count`: number of forecast paths to generate. More paths = better uncertainty estimate.

**Output:**

```python
# Returns a pandas DataFrame indexed by y_timestamp
# Columns: ['open', 'high', 'low', 'close', 'volume', 'amount']
# Each row is the model's forecast for that future bar
forecast_df = predictor.predict(x_df, x_timestamp, y_timestamp, T=1.0, top_p=0.9, sample_count=20)
```

With `sample_count=20`, you get 20 independent forecast paths. The spread across these paths is the model's implicit uncertainty estimate. A wide spread (e.g., close ranging from -5% to +8% at day 20) signals high uncertainty and should cap evidence card confidence accordingly.

---

## Evaluation Metrics

**RankIC (Rank Information Coefficient):** Spearman rank correlation between the model's predicted returns and the actual realized returns, computed cross-sectionally at each time step and averaged. This is the standard metric for cross-asset forecasting quality in quantitative finance.

- RankIC = 0: model has no ranking ability (equivalent to random)
- RankIC > 0.05: economically meaningful (industry standard threshold)
- RankIC > 0.10: strong signal in quant finance

Kronos achieves 93% better RankIC than the leading prior TSFM (time series foundation model) and 87% better than the best non-pretrained baseline on the paper's benchmarks. **Important caveat:** benchmark results are across global markets and asset classes, not specifically on US large-cap daily data for 10 symbols.

**MAE for volatility forecasting:** Kronos achieves 9% lower MAE vs. baseline on volatility forecasting. Volatility forecasting is a side benefit — the model's uncertainty across sample paths gives an implicit volatility estimate.

**Generative fidelity:** 22% improvement in synthetic K-line generation. Not directly relevant for V1, but useful for future data augmentation if we want to stress-test strategies on synthetic regimes.

---

## Concrete Integration Plan for V1

### Phase A: Validation First (Before Using as Evidence Input)

Before trusting Kronos output in evidence cards, validate it on our actual universe:

1. Pull 3 years of daily OHLCV for all 10 V1 symbols from DuckDB via `PriceReadAPI`
2. Split: train period (first 2 years), test period (last 1 year)
3. Run Kronos zero-shot forecasts with a rolling 512-bar context window, advancing by 20 bars at a time
4. Compute RankIC: at each step, rank the 10 symbols by predicted 20-day return; compare to actual 20-day return rank
5. Report average RankIC across the test period with a standard error
6. Decision threshold: if RankIC < 0.03, Kronos is not adding signal on this universe and should not influence evidence card confidence

### Phase B: Integration Architecture

```
PriceReadAPI.get_price_frame(symbol, n_bars=512, require_usable=True)
  → [OHLCVRecord × 512]
  → convert to pandas DataFrame (OHLC + volume)
  → KronosPredictor.predict(x_df, x_ts, y_ts, sample_count=20)
  → KronosForecastResult:
      median_forecast_df      # central tendency
      path_df_list            # 20 sample paths
      implied_volatility      # std of 20-day return across paths
      implied_direction       # sign of median 20-day return
      forecast_confidence     # RankIC from validation phase
```

**Key integration constraint:** Kronos sits in the pipeline AFTER `DataQualityAuditor`. Only `USABLE` status records should be fed into Kronos. If quality status is `PARTIAL`, `STALE`, or worse, do not call Kronos — instead surface `INSUFFICIENT_DATA` directly.

```python
# Pseudocode for integration guard
if quality_report.status != QualityStatus.USABLE:
    return KronosForecastResult(status=QualityStatus.INSUFFICIENT_DATA)
```

### Phase C: Evidence Card Integration

Kronos output becomes *one input* to the Technical Analyst agent, not the final verdict. The evidence card should represent Kronos as:

```json
{
  "source": "kronos_small_zero_shot",
  "claim": "Model forecasts a median +2.3% return for MSFT over the next 20 trading days, with high path variance (10th–90th percentile range: -1.8% to +6.1%).",
  "confidence": 0.55,
  "data_as_of": "2026-06-25",
  "model_rankic_on_universe": 0.07,
  "caveat": "Zero-shot model. Forecast uncertainty is high. Do not treat as directional signal in isolation."
}
```

**⚠️ Guardrail flags:**
1. Kronos forecasts close prices, not action labels. The system must convert a price forecast to an evidence claim, never to a direct BUY/SELL recommendation.
2. Confidence in the evidence card must be *bounded by the model's validated RankIC on our universe*. If RankIC < 0.03, Kronos evidence card confidence = 0 or drops to INSUFFICIENT_DATA.
3. Wide path variance (e.g., interquartile range > 5% over 20 days) must trigger a confidence reduction and an explicit "high uncertainty" flag in the evidence card.
4. Kronos output should never appear in evidence without the `model_rankic_on_universe` field populated. This prevents the system from surfacing untested model predictions.

---

## Installation

```bash
# From the repository root (WSL dev environment, not Cowork):
git clone https://github.com/shiyu-coder/Kronos.git
cd Kronos
pip install -r requirements.txt

# Load tokenizer and model:
from tokenizer.KronosTokenizer import KronosTokenizer
from model.kronos import Kronos as KronosModel

tokenizer = KronosTokenizer.from_pretrained("NeoQuasar/Kronos-Tokenizer-base")
model = KronosModel.from_pretrained("NeoQuasar/Kronos-small")
```

Note: the HuggingFace model cards are hosted under `NeoQuasar/` namespace. The canonical GitHub repo is `shiyu-coder/Kronos`.

---

## Open Questions for Next Pass

1. **Inference cost:** What is the wall-clock time to run Kronos-small on 10 symbols with 512-bar context and sample_count=20 on a laptop CPU? Need to benchmark before committing to daily inference in the pipeline.
2. **Data cutoff:** What is the latest data in Kronos's training set? If it's 2024 or earlier, post-cutoff market regime (2025-2026) is technically out-of-distribution.
3. **Sector calibration:** Does RankIC on our universe degrade significantly for ETFs (VOO, VTI, SPY, QQQ) vs. individual stocks? ETF price action is more index-driven and less company-specific.
4. **Amount column:** Our `daily_ohlcv` schema stores `volume` but not `amount` (price × volume = dollar volume). We'd need to derive this. Verify whether `amount` is required or optional for Kronos inference.

---

## Source Index

| Source | URL | Supports |
|---|---|---|
| Kronos arXiv paper (2508.02739) | https://arxiv.org/abs/2508.02739 | Primary source. Architecture, training data, benchmark results (RankIC +93% vs leading TSFM). |
| Kronos GitHub repository | https://github.com/shiyu-coder/Kronos | Code, model zoo, installation instructions, input/output format. |
| Kronos-base on HuggingFace | https://huggingface.co/NeoQuasar/Kronos-base | Model card with usage examples and tokenizer references. |
| Kronos demo site | https://shiyu-coder.github.io/Kronos-demo/ | Interactive demo of forecast outputs. |
| Kronos blog deep-dive | https://blog.arkin-dev.com/kronos-foundation-model-financial-markets-2026-04-10/ | Community explanation of architecture and zero-shot capabilities. |
| HuggingFace paper page | https://huggingface.co/papers/2508.02739 | Paper summary page confirming AAAI 2026 acceptance. |
