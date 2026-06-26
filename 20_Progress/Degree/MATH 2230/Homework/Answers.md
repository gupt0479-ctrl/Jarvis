---
type: class
input_kind: homework
status: seed
created:
updated:
area:
  - "[[Weekly Board]]"
tags:
  - "#class"
  - "#Homework"
next:
---
# Overview
## Requirements
- 
## Work log
- 
## Concepts used
- [[Concept - ...]]
- [[Concept - ...]]
# Section 3.6

## Q1 — Poisson μ = 1 (pipeline failures)

**(a)** P(X ≤ 5) = e⁻¹(1 + 1 + ½ + 1/6 + 1/24 + 1/120) = e⁻¹ · 2.71667 = **0.999**

**(b)** PMF: P(X = 1) = e⁻¹ · 1¹/1! = e⁻¹ = **0.368**
Table: P(X ≤ 1) − P(X ≤ 0) = **0.368**

**(c)** P(1 ≤ X ≤ 3) = P(1) + P(2) + P(3) = 0.368 + 0.184 + 0.061 = **0.613**

**(d)** μ = 1, σ = 1. P(X > μ + σ) = P(X > 2) = 1 − P(X ≤ 2) = 1 − 0.920 = **0.080**

---

## Q2 — Poisson μ = 20 (drivers)

Using recursion p(k) = p(k−1) · 20/k, e⁻²⁰ ≈ 2.0612 × 10⁻⁹.

**(a)** P(X ≤ 13) = **0.066**

**(b)** P(X > 24) = 1 − P(X ≤ 24) = 1 − 0.843 = **0.157**

**(c)**
- P(13 ≤ X ≤ 24) = P(X ≤ 24) − P(X ≤ 12) = 0.843 − 0.039 = **0.804**
- P(13 < X < 24) = P(X ≤ 23) − P(X ≤ 13) = 0.787 − 0.066 = **0.721**

**(d)** σ = √20 ≈ 4.472; within 2σ → 12 ≤ X ≤ 28.
P(12 ≤ X ≤ 28) = P(X ≤ 28) − P(X ≤ 11) = 0.966 − 0.021 = **0.944**

---

## Q3 — Poisson approximation (colon cancer gene, n = 2500, p = 1/500)

μ = np = 2500 · (1/500) = **5**

**(a)** P(4 ≤ X ≤ 10) = P(X ≤ 10) − P(X ≤ 3) = 0.986 − 0.265 = **0.721**

**(b)** P(X ≥ 10) = 1 − P(X ≤ 9) = 1 − 0.968 = **0.032**

---

## Q4 — Poisson process α = 8/hr, μ = 8t

**(a)** 1-hour period (μ = 8):
- P(X = 8) = e⁻⁸ · 8⁸/8! = **0.140**
- P(X ≥ 8) = 1 − P(X ≤ 7) = 1 − 0.453 = **0.547**
- P(X ≥ 14) = 1 − P(X ≤ 13) = 1 − 0.966 = **0.034**

**(b)** 75-min period = 1.25 hr → μ = 8 · 1.25 = 10
- Expected value = **10**
- Standard deviation = √10 = **3.162**

**(c)** 2.5-hr period → μ = 8 · 2.5 = 20
- P(X ≥ 27) = 1 − P(X ≤ 26) = 1 − 0.922 = **0.078**
- P(X ≤ 15) = **0.157**

---

## Q5 — Towing service α = 4/hr

**(a)** 5-hr period → μ = 20. P(X = 14) = e⁻²⁰ · 20¹⁴/14! = **0.039**

**(b)** 30-min break → μ = 2. P(X = 0) = e⁻² = **0.135**

**(c)** Expected calls = μ = 4 · 0.5 = **2**

---

## Q6 — Structural loads (mean time between = 0.4 yr, so α = 2.5/yr)

**(a)** Expected loads in 4 yr = 2.5 · 4 = **10 loads**

**(b)** μ = 10. P(X > 12) = 1 − P(X ≤ 12) = 1 − 0.792 = **0.208**

**(c)** P(X = 0 in period t) = e^{−2.5t} ≤ 0.3
→ t ≥ −ln(0.3)/2.5 = 1.20397/2.5 = **0.4816 yr**

---

## Q7 — Trees, 2D Poisson α = 40 trees/acre

**(a)** Quarter-acre → μ = 40 · 0.25 = 10.
P(X ≤ 12) = **0.792**

**(b)** E[trees in 70,000 acres] = 40 · 70,000 = **2,800,000 trees**

**(c)** Circle r = 0.1 mi → Area = π(0.1)² = 0.01π mi² = 0.01π · 640 = 6.4π acres.
μ = 40 · 6.4π = 256π

$$p(x) = \frac{e^{-256\pi}(256\pi)^x}{x!}, \quad x = 0, 1, 2, \ldots$$
# Section 4.1
