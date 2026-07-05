---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "Session 013235"
started_at: 2026-06-30T01:32:35
ended_at: 2026-06-30T01:35:48
project: Cowork
status: raw
session_id: fcb32183-30d5-4356-8e48-9e3ed564f22b
tags:
  - input
  - ai-conversation
  - claude-code
---

# Session 013235

## Claude

---

## Practice Quiz 2 — Math 2230

---

### Q2 — Binomial, n=10, p=0.6

μ = 6, σ = 1.5492

**(a)** P(X ≥ 5) = **0.834**

**(b)** Within 1 SD means X ∈ [4.45, 7.55] → integers {5,6,7}. P = **0.666**

**(c)** Store has 6 of each. All served iff oversize ≤ 6 AND midsize ≤ 6. Since midsize = 10−X, need 4 ≤ X ≤ 6. P = **0.563**

---

### Q3 — Negative Binomial, r=2, p=0.1 (X = failures before 2nd success)

**(a)** **nb(x; 2, 0.1)**

**(b)** 4 boxes total = 2 failures before 2nd prize. nb(2;2,0.1) = C(3,1)·(0.1)²·(0.9)² = **0.0243**

**(c)** P(X ≤ 2) = P(0)+P(1)+P(2) = 0.01+0.018+0.0243 = **0.0523**

**(d)** E(failures) = r(1−p)/p = **18**; E(total boxes) = **20**

---

### Q4 — Poisson, α=8/hr, μ=8t

**(a)** t=1 hr, μ=8: P(X=8) = **0.140** | P(X≥8) = **0.547** | P(X≥11) = **0.184**

**(b)** t=0.75 hr, μ=6: E(X) = **6**, σ = √6 = **2.4495**

**(c)** t=2.5 hr, μ=20: P(X≥24) = **0.213** | P(X≤13) = **0.066**

---

### Q5 — CDF: F(x) = (x/7)[1 + ln(7/x)], 0<x≤7

**(a)** P(X≤5) = F(5) = (5/7)[1+ln(7/5)] = **0.955**

**(b)** P(5≤X≤6) = F(6)−F(5) = **0.035**

**(c)** f(x) = **ln(7/x) / 7** for 0 < x ≤ 7, 0 otherwise *(differentiate F(x))*

---

### Q6 — Normal, μ=107, σ=2

**(a)** P(X=108) = **0** (continuous); P(X<108) = P(X≤108) = **0.6915**

**(b)** P(|X−107|>2) = P(|Z|>1) = **0.3173**. **No**, this does **not** depend on μ and σ — it's always P(|Z|>1).

**(c)** Bottom 0.3% and top 0.3% → z = ±2.748 → concentrations below **101.50** mmol/L and above **112.50** mmol/L

---

### Q7 — Normal approx to Binomial, n=200, p=0.12

μ=24, σ=4.5957 (with continuity correction)

**(a)** P(X≤30) ≈ P(Z≤(30.5−24)/σ) = **0.9214**

**(b)** P(X<30) ≈ P(Z≤(29.5−24)/σ) = **0.8843**

**(c)** P(15≤X≤25) ≈ P((14.5−24)/σ ≤ Z ≤ (25.5−24)/σ) = **0.6086**

---

### Q8 — Exponential, mean=2.835 hrs

**(a)** P(X≥2) = **0.4939** | P(X≤3) = **0.6529** | P(2≤X≤3) = **0.1468**

**(b)** For exponential, σ=μ=2.835, so mean+4SD = 5×2.835:
P(X > 5·2.835) = e⁻⁵ = **0.0067**
P(X < mean−SD) = P(X < 0) = **0** (exponential has no mass below 0)

---

### Q9 — CLT, μ=50, σ=1.8

**(a)** n=12 (exactly normal): SE=1.8/√12=0.5196; z=(51−50)/0.5196=1.925 → P(X̄≥51) = **0.0271**

**(b)** n=45 (CLT): SE=1.8/√45=0.2683; z=3.727 → P(X̄≥51) ≈ **0.0001**

---

### Q10 (Written) — f(x) = kx³, 0≤x≤2 (X in minutes past the hour)

**(a)** ∫₀²kx³dx = k·(16/4) = 4k = 1 → **k = 1/4**

**(b)** P(X≤1) = (1/4)·(1/4) = **0.0625**

**(c)** 75s = 1.25 min, 105s = 1.75 min. P(1.25≤X≤1.75) = (1/4)·(1.75⁴−1.25⁴)/4 = **0.4336**

**(d)** P(X≥1.75) = (1/4)·(2⁴−1.75⁴)/4 = **0.4138**

---

### Q11 (Written) — Dishwasher soap, X₁,X₂ ∈ {25,40,60}, p={0.2,0.5,0.3}

**(a) Sampling distribution of X̄:**

| x̄ | 25 | 32.5 | 40 | 42.5 | 50 | 60 |
|---|---|---|---|---|---|---|
| p(x̄) | 0.0400 | 0.2000 | 0.2500 | 0.1200 | 0.3000 | 0.0900 |

**(b)** E(X̄) = **43.0000** *(equals population mean: 25·0.2+40·0.5+60·0.3=43)*

**(c) Sampling distribution of s²:**

| s² | 0 | 112.5 | 200 | 612.5 |
|---|---|---|---|---|
| p(s²) | 0.3800 | 0.2000 | 0.3000 | 0.1200 |

**(d)** E(S²) = **156.0000** *(equals population variance — verified)*

*Tools used: ToolSearch, TaskCreate, mcp__jarvis-fs__list_directory, TaskUpdate, mcp__jarvis-fs__read_file, mcp__workspace__bash*


