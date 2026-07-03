---
type: input
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - summary
notes:
  - "[[Quant Foundations (PDF)]]"
  - "[[Stocks Trading AI Hub]]"
  - "[[06 - ML Fundamentals (2033 + 2230)]]"
source_url: 60_Claude/05_Clippings/PDFs/MIT QUANT BIBLE pdf.pdf
source_note: "[[MIT QUANT BIBLE pdf.pdf]]"
input_kind: pdf
track: trading
---
# MIT Quant Bible — Summary
**Source:** `60_Claude/05_Clippings/PDFs/MIT QUANT BIBLE pdf.pdf`
**Ingested:** 2026-07-03
**Pages:** 51
## Source
A quant-finance interview-prep guide from the **MIT Sloan Business Club** (contributors: Evan Vogelbaum, Ravi Raghavan, Guang Cui, Kyri Chen, Brian). It maps MIT coursework to the quant pipeline and covers probability, statistics, data-science/regression (built on *Elements of Statistical Learning*), econometrics (built on *Mostly Harmless Econometrics*), quant-research case studies, market-making theory, and a firm-by-firm brainteaser bank. This note captures the structure, all core formulas, and the market-making method in full; the exhaustive per-firm question list stays in the PDF as the drill source.
## Key Claims
- Quant finance is **learnable, not genius-gated** — "as long as you build up familiarity with the math and CS behind quant, and have energy for the field, it's within your reach"; the mystique is a self-fulfilling prophecy
- The **course-road** is explicit: probability (18.600), linear algebra (18.06), econometrics (14.32), discrete math (6.042), algorithms (6.006/6.046), ML (6.034/6.036), statistics (18.650)
- **Linearity of expectation works even for dependent variables** — the single most reusable trick for "complicated expected value" brainteasers
- **Bayes brainteasers exploit base-rate neglect** — the taxi (41% blue not 80%), the librarian-vs-farmer, the 1%-Ebola test (positive → only 50% sick)
- Least squares vs nearest neighbors is a **bias-variance / dimensionality** tradeoff: linear = high bias/low variance/good in high-D; kNN = low bias/high variance/**curse of dimensionality**
- **Ridge (L2) shrinks proportionally; Lasso (L1) zeroes out** — lasso produces sparse models, ridge keeps all variables; lasso is less stable when insignificant correlated variables reorder
- Econometrics' core enemy is **selection bias**; randomization kills it via LLN, and regression only kills it for *observed* controls — leaving **omitted variables bias** ($OVB = \pi_1 \times \gamma$)
- A market-maker's quote balances **three things: theoretical value, last traded price, current position** — and you widen the market with uncertainty and skew it against an informed counterparty
- The last two trades of a good market-making game generate **riskless PNL** by triangulating the counterparty's fair value, independent of the true answer
## Full Content
### 1 Introduction — the field and the course-road
==Quant finance is the intersection of math, CS, and economics — the markets become a playing ground for technical knowledge, a microcosm of the real world boiled to numbers that changes every hour.==
Core MIT classes: 18.600, 18.06, 14.32, 6.042, 6.006/6.046, 6.034/6.036, 18.650. Extra: 18.615 (stochastic processes — the main field of math finance), 6.867 (grad ML), 6.437/6.438 (inference), 18.211 (combinatorics). Books: *Heard on the Street* (Crack), *Elements of Statistical Learning* (Hastie), *A Practical Guide to Quantitative Finance Interviews* (Zhou), *Fifty Challenging Problems in Probability* (Mosteller), *Cracking the Coding Interview*, Natenberg's *Option Volatility and Pricing* (Optiver teaches from it). Firms to apply: Jane Street, Citadel/Citadel Securities, D.E. Shaw, Two Sigma, HRT, Jump, SIG, Optiver, Akuna, IMC, Five Rings, DRW, Virtu, Tower, and more.
### 2 Probability Fundamentals
==Conditional probability $P(A|B) = P(A\cap B)/P(B)$ gives Bayes: $P(A|B) = P(B|A)P(A)/P(B)$, with the evidence expanded by total probability $P(B)=P(B|A)P(A)+P(B|\neg A)P(\neg A)$.==
- Bayes brainteasers (base-rate neglect): blue-taxi = 0.8·0.15 / (0.8·0.15 + 0.2·0.85) ≈ **0.41**; the 1%-Ebola 1%-error test → positive only **50%** sick; 999 fair + 1 double-headed coin, 10 heads → **≈0.5** it's the unfair one.
- **Expectation** $E[X]=\sum xp(x)$; **linearity of expectation holds for dependent variables** — the 10-boys-10-girls adjacent-different-gender line = $19 \cdot \frac{10}{19} = 10$.
- **Variance** $\text{Var}(X)=E[X^2]-E[X]^2$; $\text{Var}(aX+b)=a^2\text{Var}(X)$; for i.i.d., $\text{Var}(\text{avg}) = \sigma^2/n$.
- Distribution table (memorize E and Var): Bernoulli ($p$, $pq$), Binomial ($np$, $npq$), Poisson ($\lambda$, $\lambda$), Geometric ($1/p$, $(1-p)/p^2$), Uniform ($\frac{a+b}{2}$, $\frac{(b-a)^2}{12}$), Normal ($\mu$, $\sigma^2$), Exponential ($1/\lambda$, $1/\lambda^2$). Geometric and exponential are **memoryless**; Poisson is the large-$n$-small-$p$ limit of Binomial.
- **Covariance** $\text{Cov}(X,Y)=E[XY]-E[X]E[Y]$; correlation $\rho = \text{Cov}/\sqrt{\text{Var}(X)\text{Var}(Y)}$. Independent ⟹ uncorrelated, **converse false**.
### 3 Statistics Fundamentals
==Probability starts from known parameters and predicts data; statistics observes data and deduces unknown parameters — the estimator links them via the LLN, the CLT quantifies confidence.==
Framework: treat each data event as an i.i.d. r.v., pick an estimator (often the sample mean), bound confidence via a CLT-derived interval. A level-$(1-\alpha)$ CI: $\hat\theta \pm \frac{\sigma}{\sqrt n} q_{\alpha/2}$; for Bernoulli use the bound $p(1-p)\le \frac14$; generally use Slutsky's theorem to substitute the estimator into the variance.
### 4 Quant Research — Data Science (from ESL)
==Least squares gives $\hat\beta = (X^TX)^{-1}X^Ty$ — the single most important formula to know cold — and the hat matrix $H=X(X^TX)^{-1}X^T$ is the orthogonal projection of $y$ onto the column space of $X$.==
- **Least squares vs kNN:** linear model = high bias / low variance / assumes linearity / efficient in high-D; kNN $\hat Y(x)=\frac1k\sum_{x_i\in N_k(x)}y_i$ = low bias / high variance / no assumptions / effective degrees of freedom $n/k$ / **curse of dimensionality** (distances grow, points hit boundaries → extrapolation). 1-NN is the lowest-bias model possible and the only one with zero training error.
- **Significance:** individual coefficient z-score (t-test) $z_j = \hat\beta_j / (\hat\sigma\sqrt{v_j})$; the $\pm 2\,\text{se}(\hat\beta)$ rule is the ≈95% CI. **F-statistic** tests *groups* of coefficients — three individually insignificant coefficients can be jointly significant.
- **Dimensionality reduction:** stepwise (forward/backward/stagewise, "hard thresholding"), **Ridge** $\hat\beta = (X^TX+\lambda I)^{-1}X^Ty$ (always invertible, proportional shrinkage, shrinks the last principal components via SVD $X=UDV^T$), **Lasso** (L1, no closed form, "soft thresholding," creates sparsity by zeroing coefficients), LAR (greedy, reproduces the lasso path), PCR (truncates last principal components entirely). Lasso/ridge are the $q=1,2$ cases of $L_q$; elastic-net interpolates $q\in(1,2)$.
- **Regression brainteasers:** assumptions = linearity, zero-mean error, low multicollinearity, homoskedasticity, no autocorrelation; regressing $Y$ on $X$ vs $X$ on $Y$ does **not** give $\beta_1 = 1/\beta_2$ (vertical vs horizontal residuals); doubling every data point leaves $\beta$ unchanged; lasso has lower bias / higher variance than ridge.
### 4.6 The Econometrics Perspective (from MHE)
==Without "other things equal," the average causal effect decomposes into (true effect) + (selection bias); randomization drives selection bias to zero by the LLN.==
- **OVB** (omitted variables bias): $\text{OVB} = \beta_{short} - \beta_{long} = \pi_1 \times \gamma$ (relationship of omitted-to-treatment × omitted's effect in the long regression). Claiming no OVB is claiming the long regression has a causal interpretation via the **conditional independence assumption**.
- Regression as causal tool: $Y_i = \alpha + \beta X_i + \gamma A + \epsilon$, OLS minimizes RSS. Bivariate $\beta = \text{Cov}(Y,X)/\text{Var}(X)$. **Regression anatomy:** a multivariate coefficient depends only on the residual of that variable after regressing on all others. $SE(\hat\beta) = \frac{\sigma_\epsilon}{\sqrt n}\cdot\frac1{\sigma_X}$ — want low residual variance, **high input variance**. Heteroskedasticity → robust standard errors (usually close in practice). Population solution $\beta = E[X^TX]^{-1}E[X^TY]$; CEF is the minimum-MSE predictor; ANOVA: $\text{Var}(Y)=\text{Var}(E[Y|X])+E[\text{Var}(Y|X)]$. Saturated regressions (all-discrete inputs, dummies for main effects + interactions) fit the CEF perfectly.
### 5 Quant Research — Case Studies (the method)
==The case-study method: pick the model (regression vs kNN), then reason explicitly through encoding, normalization, correlation/multicollinearity, and interpretation — brainstorming variables and preprocessing iteratively.==
- **Two Sigma NY housing:** multivariate regression; continuous (sqft, year) as-is, discrete (beds/baths), categorical (borough) one-hot; **sqft is lognormal → take the log then normalize**; sqft/beds/baths correlate → use **Spearman rank** (continuous vs ordinal) then ridge/lasso/orthonormalization for multicollinearity.
- **QuantCo opera-house pricing:** kNN makes sense because row/column/section map to real 2D/3D spatial seat value (nearer/better angle); add a distance kernel; convert row to Euclidean distance to stage; add **log(days-to-concert)** (exponential demand), a **scarcity** variable (loss-aversion/FOMO drives back-row prices above the linear fit), and lognormal willingness-to-pay for profit maximization.
- **Two Sigma CitiBikes [advanced]:** open-ended — brainstorm variables first (time-of-day, neighborhood, season, temperature, weather); **cyclical variables** (hour/month) get bucketed + one-hot or trig/spline basis transforms to preserve cyclicality; neighborhood as lat/long with polynomial/spline transforms.
### 6 Quant Trading — Market Making
==A market maker always quotes a two-sided bid@ask; the spread compensates for the risk of being filled on the wrong side, and the three determinants of your quote are theoretical value, last traded price, and current position.==
- **Theoretical value:** tight for known quantities (die roll = 3.5), wide for uncertain ones (ping-pong balls in the Empire State Building). The interviewer wants to see you widen for risk.
- **Current position:** market makers want to be **flat**; if long, skew the market down (e.g. $0.43@0.53$ on a $0.50 asset) to make selling more attractive — giving up edge to cut exposure. Flat ⟹ symmetric quote.
- **Confidence interval** questions (SIG's "windows in your building") test the same instinct — wider with more uncertainty.
- **Realism:** $0@1\text{billion}$ contains the true value but never trades; tightest/fastest markets win the flow.
- **Informational asymmetry:** even knowing the true value, quote the widest market your counterparty will still trade; if you think they'll over-estimate, **skew up** (e.g. 550@600 when you expect them to buy at 600).
- **Trading-game method (Red Sox wins case):** generate theoretical value from data (2018 .667 / 2019 .519 / 2020 .400 → shade to .50 → 81 wins → 76@86 for a 10-wide market); CIs from Binomial-normal ($\sigma=\sqrt{162\cdot0.5\cdot0.5}\approx6.36$, z=0.67 for 50%, 1.64 for 90%). After each trade, **move toward flat** and incorporate the counterparty's revealed valuation; the last trades triangulate their fair value and produce **riskless PNL** (sold 93, bought 84 → +9 on two trades regardless of the true answer). Track position and running PNL by pairing opposite trades ("trader memory").
- **Losing is fine** (Tanzania population case, PNL −$20) — the game tests reaction to trades and market adaptation, not knowledge of the answer.
### 7 Question Bank (index — full brainteasers in the PDF)
Per-firm interview question sets with worked patterns: **Jane Street** (Evan/Brian), **Virtu Financial** (Evan), **Optiver** (Ravi), **Akuna Capital**, **Citadel**, **Hudson River Trading**, **Two Sigma**, **Five Rings**, **SIG** (Ravi), plus a preliminaries section. Use these as the drill deck once the fundamentals above are fluent.
## Why It Matters
This is the map for the quant-internship track that runs alongside Anant's ML coursework and the [[Stocks Trading AI Hub]] project — and the overlap is exact: the probability/expectation/variance and the regression/dimensionality-reduction material *is* [[06 - ML Fundamentals (2033 + 2230)]] and CSCI 2033/MATH 2230, recontextualized. It pairs with [[Quant Foundations (PDF)]] (which is the "how to prepare" strategy layer; this is the "actual content" layer). The market-making section is the most uniquely valuable part — it's not in any course, and the three-determinant quoting method + riskless-PNL triangulation is directly drillable. Honest caveat: the guide targets MIT students recruiting for these specific firms; the course numbers and firm list are MIT-specific, but the math and the interview method transfer to any quant recruiting.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/MIT QUANT BIBLE pdf.pdf`
- [[Quant Foundations (PDF)]] — the strategy/prep companion to this content bible
- [[Stocks Trading AI Hub]] — the trading project this feeds
- [[06 - ML Fundamentals (2033 + 2230)]] — the vault's version of the probability/stats/regression fundamentals here
- [[05 - LeetCode & CSCI 4041]] — several firms (Two Sigma, HRT, Akuna, Belvedere) give coding challenges
- ESL / regression concept notes `(to create)` — ridge/lasso/PCR, bias-variance, curse of dimensionality
## Open Questions
- [ ] Which of the 4041/2033/2230 concepts already have vault notes that could absorb the ESL regression material vs need new ones?
- [ ] Is the market-making game worth building as an interactive drill (interviewer bot quoting/trading against you)?
- [ ] Map the firm question bank to which firms actually recruit non-MIT / international students?
## Flashcards
#cards/trading
Why can you use linearity of expectation on dependent random variables?::Because expectation is **linear regardless of dependence** — $E[X_1+\dots+X_n]=E[X_1]+\dots+E[X_n]$ even when the $X_i$ are dependent, which cracks many "complicated expected value" brainteasers (e.g. adjacent-different-gender pairs = $19\cdot\frac{10}{19}=10$).
What are the three determinants of a market maker's quote?::**Theoretical value** (your estimate, widen with uncertainty), **last traded price** (the market's view vs your model), and **current position** (skew the quote to move back toward flat).
Ridge vs Lasso — what's the key behavioral difference?::**Ridge (L2)** shrinks all coefficients proportionally and keeps them nonzero; **Lasso (L1)** zeroes some coefficients entirely, producing **sparse models** — but lasso is less stable when insignificant correlated variables reorder.
What is the closed form for least-squares regression, and what does the hat matrix do?::$\hat\beta=(X^TX)^{-1}X^Ty$; the hat matrix $H=X(X^TX)^{-1}X^T$ is the **orthogonal projection of $y$ onto the column space of $X$**.
State the omitted-variables-bias formula and what it means.::$\text{OVB}=\beta_{short}-\beta_{long}=\pi_1\times\gamma$ (omitted-to-treatment relationship × omitted's effect in the long regression) — claiming no OVB means claiming your long regression is causal via the conditional independence assumption.
Why does the blue-taxi answer come out to ~41%, not 80%?::**Base-rate neglect** — Bayes weighs the witness's 80% accuracy against the low prior (15% blue): $\frac{0.8\cdot0.15}{0.8\cdot0.15+0.2\cdot0.85}\approx0.41$, so the taxi is more likely green despite the identification.
Why does a good market-making game end in riskless PNL?::The last trades **triangulate the counterparty's fair value** from their buy/sell pattern, letting you sell high and buy low around it (e.g. sold 93, bought 84 → +9) regardless of the true answer.
Why is kNN good in low dimensions but bad in high dimensions?::The **curse of dimensionality** — in high-D, average distances between points grow and points fall on the boundary, so classifying by a nearby training point requires extrapolation instead of interpolation; effective parameters $n/k$.
