---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "Provide me solutions for the sections 3.4, and 3.5 for the"
started_at: 2026-06-17T17:20:31
ended_at: 2026-06-17T17:49:46
project: Cowork
status: raw
session_id: ad41cd49-b023-4bf5-bc83-8206db472468
tags:
  - input
  - ai-conversation
  - claude-code
---

# Provide me solutions for the sections 3.4, and 3.5 for the

## You

Provide me solutions for the sections 3.4, and 3.5 for the homework: `20_Progress/Degree/MATH 2230/Homework/Chapter - 3`. Everything has been listed in that file. Provide me solutions in a manner that optimizes tokens, be sure of each and every answer and just provide me with the answer. If you are unsure about the answer, refer to the textbook in the MATH 2230 folder. Answer all the questions in order and correctly.

## Claude

All values computed. Here are the complete solutions:

---

## Section 3.4

**Q1 — Binomial probabilities**

(a) b(5; 8, 0.3) = C(8,5)·0.3⁵·0.7³ = **0.047**
(b) b(6; 8, 0.65) = C(8,6)·0.65⁶·0.35² = **0.259**
(c) P(3 ≤ X ≤ 5 | n=7, p=0.55) = **0.745**
(d) P(X ≥ 1 | n=9, p=0.15) = 1 − 0.85⁹ = **0.768**

---

**Q2 — X ~ Bin(15, 0.05)**

(a) P(X ≤ 2) = **0.964**; P(X < 2) = **0.829**
(b) P(X ≥ 3) = **0.036**
(c) P(1 ≤ X ≤ 2) = **0.501**
(d) E(X) = np = **0.75**; σ = √(np(1−p)) = **0.84**
(e) P(X = 0 | n=50, p=0.05) = 0.95⁵⁰ = **0.077**

---

**Q3 — X ~ Bin(25, 0.25), fax calls**

(a) P(X ≤ 5) = **0.378**
(b) P(X = 5) = **0.165**
(c) P(X ≥ 5) = **0.786**
(d) P(X > 5) = **0.622**

---

**Q4 — n=25, p=0.40, fax**

(a) E(X) = **10**
(b) σ = √(25·0.4·0.6) = **2.449**
(c) μ + 2σ = 14.899 → P(X ≥ 15) = **0.034**

---

**Q5 — n=15, p=0.30, new copies**

(a) mean = **4.5**; σ = √(15·0.3·0.7) = **1.77**
(b) P(|X − 4.5| > 2·1.77) = P(X=0) + P(X≥9) = **0.020**
(c) Need 5 ≤ X ≤ 10 (10 new, 10 used in stock): P(5 ≤ X ≤ 10) = **0.484**
(d) h(X) = 150X + 90(15−X) = 60X + 1350; E[revenue] = 60(4.5) + 1350 = **$1620**; rule used: **E(aX + b) = a·E(X) + b**

---

**Q6 — n=30, p=0.03, SAT accommodations**

(a) P(X = 1) = **0.372**
(b) P(X ≥ 1) = **0.599**
(c) P(X ≥ 2) = **0.227**
(d) μ = 0.9, σ = 0.934 → within 2 SDs means X ∈ {0,1,2}: P(X ≤ 2) = **0.940**
(e) E[avg time] = 0.03(4.5) + 0.97(3) = **3.05 hr**

---

**Q7 — n=25, reject p ≥ 0.6 if X ≤ 15**

(a) P(reject | p=0.6) = P(X ≤ 15 | Bin(25, 0.6)) = **0.575**
(b) P(not reject | p=0.5) = P(X ≥ 16 | Bin(25, 0.5)) = **0.115**; P(not reject | p=0.4) = **0.013**
(c) New rule x ≤ 14: P(reject | p=0.6) = **0.414**; P(not reject | p=0.5) = **0.212**; P(not reject | p=0.4) = **0.034**
*(Type I error decreases; Type II errors increase)*

---

**Q8 — Gas station, 100 customers**

(a) Debit (p=0.2): mean = **20**, variance = **16**; reasoning: binomial applies, X = number of customers who use a debit card
(b) Non-cash (p=0.8): mean = **80**, variance = **16**

---

## Section 3.5

**Q1 — 17 individuals, 7 first-timers, 6 assigned: X ~ h(x; 6, 7, 17)**

(a) Distribution: **h(x; 6, 7, 17)** (hypergeometric)

(b) Using C(17,6) = 12,376:

| | |
|---|---|
| P(X = 4) | **0.1273** |
| P(X ≤ 4) | **0.9825** |
| P(X ≥ 4) | **0.1448** |

(c) mean = 6·7/17 = **2.471**; σ = **1.000**

---

**Q2 — 25 + 35 students, first 15 graded: X ~ h(x; 15, 35, 60)**

(a) P(X = 10) = **0.1834**
(b) P(X ≥ 10) = **0.3281**
(c) P(≥10 from same section) = P(X≥10) + P(X≤5) = **0.3532**
(d) mean = **9** projects; σ = **1.668** projects
(e) mean = **26** projects; σ = **1.668** projects

---

**Q4 — 12 basalt + 12 granite, 19 selected: X ~ h(x; 19, 12, 24)**

(a) pmf (x = 7 to 12):

| x | p(x) |
|---|------|
| 7 | 0.0186 |
| 8 | 0.1398 |
| 9 | 0.3416 |
| 10 | 0.3416 |
| 11 | 0.1398 |
| 12 | 0.0186 |

(b) P(all of one type) = P(X=12) + P(X=7) = **0.0373**
(c) μ = 9.5, σ = 1.016 → P(9 ≤ X ≤ 10) = **0.6832**

---

**Q5 — 60 firms, 24 violating, 20 visited**

(a) pmf: **h(x; 20, 24, 60)**
(b) With 600 firms/240 violating, approximate by **b(x; 20, 0.4)**
(c)

| | Exact h(x;20,240,600) | Approx b(x;20,0.4) |
|---|---|---|
| E(X) | **8.00** | **8.00** |
| V(X) | **4.65** | **4.80** |

---

**Q6 — Negative binomial, p=0.2, r=3 prizes**

(a) pmf: **nb(x; 3, 0.2)** where x = number of boxes without the prize
(b) P(purchase 5 boxes) = P(X=2 failures) = C(4,2)·0.2³·0.8² = **0.0307**
(c) P(purchase ≤ 5 boxes) = **0.0579**
(d) E[non-prize boxes] = r(1−p)/p = **12**; E[total boxes] = r/p = **15**

*Tools used: ToolSearch, mcp__jarvis-fs__list_directory, mcp__jarvis-fs__search_files, mcp__jarvis-fs__read_file, Read, mcp__workspace__bash*


