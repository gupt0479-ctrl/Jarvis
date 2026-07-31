---
type: input
input_kind: ai-conversation
source_app: cowork
source_os: windows
title: "Provide me solutions for the sections 3.4, and 3.5 for the"
started_at: 2026-06-17T17:20:31
ended_at: 2026-06-17T17:49:46
exported_at: 2026-07-31T21:03:35
duration_minutes: 29.3
project: 2026-06
session_id: ad41cd49-b023-4bf5-bc83-8206db472468
status: raw
turn_count: 2
tools_used:
  mcp__jarvis-fs__list_directory: 6
  mcp__jarvis-fs__read_file: 1
  mcp__jarvis-fs__search_files: 2
  mcp__workspace__bash: 4
  Read: 1
  ToolSearch: 1
tokens:
  input: 41
  output: 174455
  cache_creation: 111116
  cache_read: 1629266
  total: 1914878
cost_usd: 3.772424
model:
  - "claude-sonnet-4-6"
files_touched:
  - "C:\\Users\\Anant Gupta\\AppData\\Roaming\\Claude\\local-agent-mode-sessions\\a3ddc74f-5d7e-42cc-b2f0-e2fdb16f754d\\9f8878c6-5e85-4313-8450-e158b8949926\\local_02036b59-8885-4e36-8965-d6ce68d98bee\\.claude\\projects\\C--Users-Anant-Gupta-AppData-Roaming-Claude-local-agent-mode-sessions-a3ddc74f-5d7e-42cc-b2f0-e2fdb16f754d-9f8878c6-5e85-4313-8450-e158b8949926-local-02036b59-8885-4e36-8965-d6ce68d98bee-outputs\\ad41cd49-b023-4bf5-bc83-8206db472468\\tool-results\\toolu_01SSMq3Q1P3yHEKnUf56cfUZ.txt"
tags:
  - input
  - ai-conversation
  - cowork
  - windows
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

### Tool Calls

- `ToolSearch` -- `{"query":"select:mcp__jarvis-fs__read_file,mcp__jarvis-fs__list_directory,mcp__jarvis-fs__search_files","max_results":5}`
- `mcp__jarvis-fs__list_directory` -- `{"path":"20_Progress/Degree/MATH 2230/Homework"}`
- `mcp__jarvis-fs__list_directory` -- `{"path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis"}`
- `mcp__jarvis-fs__search_files` -- `{"path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress","pattern":"*Chapter*3*"}`
- `mcp__jarvis-fs__search_files` -- `{"path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress","pattern":"*MATH*"}`
- `mcp__jarvis-fs__list_directory` -- `{"path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress"}`
- `mcp__jarvis-fs__list_directory` -- `{"path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Degree"}`
- `mcp__jarvis-fs__list_directory` -- `{"path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Degree\\MATH 2230"}`
- `mcp__jarvis-fs__list_directory` -- `{"path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Degree\\MATH 2230\\Homework"}`
- `mcp__jarvis-fs__read_file` -- `{"path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Degree\\MATH 2230\\Homework\\Chapter - 3.md"}`
- `Read` -- `C:\Users\Anant Gupta\AppData\Roaming\Claude\local-agent-mode-sessions\a3ddc74f-5d7e-42cc-b2f0-e2fdb16f754d\9f8878c6-5e85-4313-8450-e158b8949926\local_02036b59-8885-4e36-8965-d6ce68d98bee\.claude\projects\C--Users-Anant-Gupta-AppData-Roaming-Claude-local-agent-mode-sessions-a3ddc74f-5d7e-42cc-b2f0-e2fdb16f754d-9f8878c6-5e85-4313-8450-e158b8949926-local-02036b59-8885-4e36-8965-d6ce68d98bee-outputs\ad41cd49-b023-4bf5-bc83-8206db472468\tool-results\toolu_01SSMq3Q1P3yHEKnUf56cfUZ.txt`
- `mcp__workspace__bash` -- `{"command":"python3 \u003c\u003c \u0027EOF\u0027\nfrom math import comb, factorial\nfrom scipy.stats import binom, hypergeom, nbinom\nimport scipy.stats as stats\n\nprint(\"=== SECTION 3.4 ===\")\nprint(\"\\n--- Q1: Binomial formula ---\")\ndef b(x, n, p):\n    return comb(n,x) * (p**x) * ((1-p)**(n-x))\n\nprint(f\"(a) b(5;8,0.3) = {b(5,8,0.3):.3f}\")\nprint(f\"(b) b(6;8,0.65) = {b(6,8,0.65):.3f}\")\np_c = sum(b(x,7,0.55) for x in range(3,6))\nprint(f\"(c) P(3\u003c=X\u003c=5|n=7,p=0.55) = {p_c:.3f}\")\np_d = 1 - b(0,9,0.15)\nprint(f\"(d) P(X\u003e=1|n=9,p=0.15) = {p_d:.3f}\")\n\nprint(\"\\n--- Q2: X~Bin(15,0.05) ---\")\nn,p = 15, 0.05\nP_le2 = binom.cdf(2,n,p)\nP_lt2 = binom.cdf(1,n,p)\nP_ge3 = 1 - P_le2\nP_1to2 = binom.pmf(1,n,p) + binom.pmf(2,n,p)\nEX = n*p\nsigma = (n*p*(1-p))**0.5\nP_none50 = binom.pmf(0,50,0.05)\nprint(f\"P(X\u003c=2) = {P_le2:.3f}\")\nprint(f\"P(X\u003c2) = {P_lt2:.3f}\")\nprint(f\"P(X\u003e=3) = {P_ge3:.3f}\")\nprint(f\"P(1\u003c=X\u003c=2) = {P_1to2:.3f}\")\nprint(f\"E(X) = {EX:.2f}, sigma = {sigma:.2f}\")\nprint(f\"P(none in 50) = {P_none50:.3f}\")\n\nprint(\"\\n--- Q3: X~Bin(25,0.25) ---\")\nn,p = 25, 0.25\nprint(f\"(a) P(X\u003c=5) = {binom.cdf(5,n,p):.3f}\")\nprint(f\"(b) P(X=5) = {binom.pmf(5,n,p):.3f}\")\nprint(f\"(c) P(X\u003e=5) = {1-binom.cdf(4,n,p):.3f}\")\nprint(f\"(d) P(X\u003e5) = {1-binom.cdf(5,n,p):.3f}\")\n\nprint(\"\\n--- Q4: n=25,p=0.40 ---\")\nn,p = 25, 0.40\nmu = n*p; sig = (n*p*(1-p))**0.5\nprint(f\"E(X) = {mu}\")\nprint(f\"sigma = {sig:.3f}\")\nthreshold = mu + 2*sig\nprint(f\"mu+2sigma = {threshold:.3f}\")\nprint(f\"P(X \u003e {threshold:.3f}) = P(X \u003e= {int(threshold)+1}) = {1-binom.cdf(int(threshold),n,p):.3f}\")\n\nprint(\"\\n--- Q5: n=15,p=0.30 ---\")\nn,p = 15, 0.30\nmu = n*p; sig = (n*p*(1-p))**0.5\nprint(f\"mean={mu}, sigma={sig:.2f}\")\nlo = mu-2*sig; hi = mu+2*sig\nprint(f\"mu-2s={lo:.4f}, mu+2s={hi:.4f}\")\n# |X-mu|\u003e2sigma means X\u003clo or X\u003ehi: X=0 or X\u003e=9\nP_outside = binom.pmf(0,n,p) + (1-binom.cdf(8,n,p))\nprint(f\"P(|X-mu|\u003e2sigma) = {P_outside:.3f}\")\n# all 15 satisfied: 5\u003c=X\u003c=10\nP_all = binom.cdf(10,n,p) - binom.cdf(4,n,p)\nprint(f\"P(5\u003c=X\u003c=10) = {P_all:.3f}\")\n# Revenue: h(X)=60X+1350, E[h(X)]=60*4.5+1350\nEX_5 = n*p\nE_rev = 60*EX_5 + 1350\nprint(f\"E[revenue] = ${E_rev:.0f}\")\n\nprint(\"\\n--- Q6: n=30,p=0.03 ---\")\nn,p = 30, 0.03\nmu = n*p; sig = (n*p*(1-p))**0.5\nprint(f\"(a) P(X=1) = {binom.pmf(1,n,p):.3f}\")\nprint(f\"(b) P(X\u003e=1) = {1-binom.pmf(0,n,p):.3f}\")\nprint(f\"(c) P(X\u003e=2) = {1-binom.cdf(1,n,p):.3f}\")\nlo2 = mu-2*sig; hi2 = mu+2*sig\nprint(f\"(d) mu={mu}, sigma={sig:.4f}, range=[{lo2:.4f},{hi2:.4f}]\")\nP_d = binom.cdf(int(hi2), n, p)  # since lo is negative, lower bound is 0\nprint(f\"P(within 2 SDs) = P(X\u003c=2) = {binom.cdf(2,n,p):.3f}\")\nE_time = n*(p*4.5 + (1-p)*3)\nprint(f\"(e) E[total time]/30 = {E_time/n:.2f} hr per student\")\n\nprint(\"\\n--- Q7: n=25 ---\")\n# (a) P(reject|p=0.6) = P(X\u003c=15|Bin(25,0.6))\np_a = binom.cdf(15, 25, 0.6)\nprint(f\"(a) P(reject|p=0.6) = {p_a:.3f}\")\n# (b) P(not reject|p=0.5) = P(X\u003e=16|Bin(25,0.5))\np_b5 = 1 - binom.cdf(15, 25, 0.5)\n# P(not reject|p=0.4)\np_b4 = 1 - binom.cdf(15, 25, 0.4)\nprint(f\"(b) P(not reject|p=0.5) = {p_b5:.3f}\")\nprint(f\"(b) P(not reject|p=0.4) = {p_b4:.3f}\")\n# (c) New rule: reject if x\u003c=14\np_c_a = binom.cdf(14, 25, 0.6)\np_c_b5 = 1 - binom.cdf(14, 25, 0.5)\np_c_b4 = 1 - binom.cdf(14, 25, 0.4)\nprint(f\"(c) New rule P(reject|p=0.6) = {p_c_a:.3f}\")\nprint(f\"(c) New rule P(not reject|p=0.5) = {p_c_b5:.3f}\")\nprint(f\"(c) New rule P(not reject|p=0.4) = {p_c_b4:.3f}\")\n\nprint(\"\\n--- Q8: Gas station ---\")\nprint(f\"(a) Debit card: mean={100*0.2}, variance={100*0.2*0.8}\")\nprint(f\"(b) Non-cash: mean={100*0.8}, variance={100*0.8*0.2}\")\n\nprint(\"\\n=== SECTION 3.5 ===\")\nprint(\"\\n--- Q1: h(x;6,7,17) ---\")\n# N=17, M=7, n=6\nN,M,n = 17,7,6\nC_N_n = comb(N,n)\nprint(f\"C(17,6) = {C_N_n}\")\nfor x in range(7):\n    if x \u003c= min(M,n) and (n-x) \u003c= (N-M):\n        px = comb(M,x)*comb(N-M,n-x)/C_N_n\n        print(f\"P(X={x}) = {comb(M,x)}*{comb(N-M,n-x)}/{C_N_n} = {px:.4f}\")\n\nP_eq4 = hypergeom.pmf(4, N, M, n)\nP_le4 = hypergeom.cdf(4, N, M, n)\nP_ge4 = 1 - hypergeom.cdf(3, N, M, n)\nprint(f\"P(X=4) = {P_eq4:.4f}\")\nprint(f\"P(X\u003c=4) = {P_le4:.4f}\")\nprint(f\"P(X\u003e=4) = {P_ge4:.4f}\")\nmu_h = n*M/N\nvar_h = n*(M/N)*((N-M)/N)*(N-n)/(N-1)\nprint(f\"mean = {mu_h:.3f}, sigma = {var_h**0.5:.3f}\")\n\nprint(\"\\n--- Q2: h(x;15,35,60) ---\")\nN,M,n = 60,35,15\n# (a) P(X=10)\nprint(f\"(a) P(X=10) = {hypergeom.pmf(10,N,M,n):.4f}\")\n# (b) P(X\u003e=10)\nprint(f\"(b) P(X\u003e=10) = {1-hypergeom.cdf(9,N,M,n):.4f}\")\n# (c) P(X\u003e=10 from second OR X\u003e=10 from first)\n# second section: M=35, first section: N-M=25\n# \"at least 10 from same section\": P(X\u003e=10) + P(25-X\u003c=15-10) = P(X\u003e=10) + P(X\u003c=5)\n# X ~ h(x;15,35,60). At least 10 from second: X\u003e=10. At least 10 from first: 15-X\u003e=10 =\u003e X\u003c=5\nP_ge10 = 1 - hypergeom.cdf(9,N,M,n)\nP_le5 = hypergeom.cdf(5,N,M,n)\nprint(f\"(c) P(\u003e=10 same section) = P(X\u003e=10)+P(X\u003c=5) = {P_ge10+P_le5:.4f}\")\nmu2 = n*M/N\nvar2 = n*(M/N)*((N-M)/N)*(N-n)/(N-1)\nprint(f\"(d) mean={round(mu2)}, sigma={var2**0.5:.3f}\")\n# (e) not among first 15 from second section: 35-X\n# E[35-X] = 35 - E[X], Var same\nprint(f\"(e) mean={round(35-mu2)}, sigma={var2**0.5:.3f}\")\n\nprint(\"\\n--- Q4: h(x;19,12,24) basalt/granite ---\")\n# N=24 total (12 basalt + 12 granite), M=12 granite, n=19 selected\nN,M,n = 24,12,19\n# x ranges from max(0,n-(N-M)) to min(M,n) = max(0,19-12) to min(12,19) = 7 to 12\nprint(\"pmf of granite specimens selected:\")\nmu_q4 = n*M/N\nvar_q4 = n*(M/N)*((N-M)/N)*(N-n)/(N-1)\nfor x in range(max(0,n-(N-M)), min(M,n)+1):\n    px = hypergeom.pmf(x,N,M,n)\n    print(f\"x={x}: {px:.4f}\")\n# (b) all of one type selected\n# All 12 granite: P(X=12)\nP_all_granite = hypergeom.pmf(12,N,M,n)\n# All 12 basalt: that means 19-12=7 granite selected, so X=7\nP_all_basalt = hypergeom.pmf(7,N,M,n)\nprint(f\"(b) P(all granite) = {P_all_granite:.4f}\")\nprint(f\"(b) P(all basalt) = {P_all_basalt:.4f}\")\nprint(f\"(b) P(all of one type) = {P_all_granite+P_all_basalt:.4f}\")\nprint(f\"mean={mu_q4:.4f}, sigma={var_q4**0.5:.4f}\")\n# (c) P within 1 SD of mean\nlo = mu_q4 - var_q4**0.5\nhi = mu_q4 + var_q4**0.5\nlo_int = int(lo)+1 if lo != int(lo) else int(lo)\nhi_int = int(hi)\nprint(f\"mu={mu_q4:.4f}, sigma={var_q4**0.5:.4f}, range: ({lo:.4f},{hi:.4f})\")\nprint(f\"Integer range: {lo_int} to {hi_int}\")\nP_within1 = sum(hypergeom.pmf(x,N,M,n) for x in range(lo_int, hi_int+1))\nprint(f\"(c) P(within 1 SD) = {P_within1:.4f}\")\n\nprint(\"\\n--- Q5: Smog h(x;20,24,60) ---\")\n# (a) pmf h(x;20,24,60)\n# (b) approx by b(x;20,0.4)\n# (c) exact vs approx E(X) and V(X) for 600 firms, 240 violating\nN2,M2,n2 = 600,240,20\nmu_ex = n2*M2/N2\nvar_ex = n2*(M2/N2)*((N2-M2)/N2)*(N2-n2)/(N2-1)\nmu_ap = n2*0.4\nvar_ap = n2*0.4*0.6\nprint(f\"Exact: E(X)={mu_ex:.2f}, V(X)={var_ex:.2f}\")\nprint(f\"Approx binomial: E(X)={mu_ap:.2f}, V(X)={var_ap:.2f}\")\n\nprint(\"\\n--- Q6: Negative Binomial, p=0.2, r=3 prizes ---\")\n# NB: r=3 successes (prizes), p=0.2\n# X = number of failures (boxes without prize) before 3rd prize\n# P(x failures) = C(x+r-1, x) * p^r * (1-p)^x = nb(x;r,p)\nr, p = 3, 0.2\n# (b) P(purchase 5 boxes) = P(4 boxes without prize before 3rd prize) + wait...\n# actually \"purchase x boxes\" means x-r failures + r successes = x boxes total\n# P(purchase 5 boxes) = P(X=2 failures) since 3 prizes in 5 boxes means 2 non-prizes\n# Using NB where X = # failures: P(X=x) = C(x+r-1,r-1)*p^r*(1-p)^x\ndef nb_pmf(x, r, p):\n    return comb(x+r-1, r-1) * (p**r) * ((1-p)**x)\n\nprint(f\"(b) P(purchase 5 boxes) = P(X=2 failures) = {nb_pmf(2,r,p):.4f}\")\n# (c) P(purchase at most 5) = P(X\u003c=2 failures)\nP_atmost5 = sum(nb_pmf(x,r,p) for x in range(3))\nprint(f\"(c) P(at most 5 boxes) = {P_atmost5:.4f}\")\n# (d) E[failures] = r(1-p)/p, E[boxes] = r/p\nE_fail = r*(1-p)/p\nE_boxes = r/p\nprint(f\"(d) E[boxes without prize] = {E_fail:.0f}\")\nprint(f\"(d) E[total boxes] = {E_boxes:.0f}\")\nEOF\n"}`
- `mcp__workspace__bash` -- `{"command":"pip install scipy --break-system-packages -q 2\u003e\u00261 | tail -1"}`
- `mcp__workspace__bash` -- `{"command":"python3 -c \"from scipy.stats import binom; print(\u0027ok\u0027)\""}`
- `mcp__workspace__bash` -- `{"command":"python3 \u003c\u003c \u0027EOF\u0027\nfrom math import comb\nfrom scipy.stats import binom, hypergeom\n\nprint(\"=== SECTION 3.4 ===\")\nprint(\"\\n--- Q1 ---\")\ndef b(x, n, p):\n    return comb(n,x) * (p**x) * ((1-p)**(n-x))\n\nprint(f\"(a) b(5;8,0.3) = {b(5,8,0.3):.3f}\")\nprint(f\"(b) b(6;8,0.65) = {b(6,8,0.65):.3f}\")\np_c = sum(b(x,7,0.55) for x in range(3,6))\nprint(f\"(c) P(3\u003c=X\u003c=5|n=7,p=0.55) = {p_c:.3f}\")\nprint(f\"(d) P(X\u003e=1|n=9,p=0.15) = {1-b(0,9,0.15):.3f}\")\n\nprint(\"\\n--- Q2: Bin(15,0.05) ---\")\nn,p=15,0.05\nprint(f\"P(X\u003c=2)={binom.cdf(2,n,p):.3f}, P(X\u003c2)={binom.cdf(1,n,p):.3f}\")\nprint(f\"P(X\u003e=3)={1-binom.cdf(2,n,p):.3f}\")\nprint(f\"P(1\u003c=X\u003c=2)={binom.pmf(1,n,p)+binom.pmf(2,n,p):.3f}\")\nprint(f\"E(X)={n*p:.2f}, sigma={(n*p*(1-p))**0.5:.2f}\")\nprint(f\"P(none in 50)={binom.pmf(0,50,0.05):.3f}\")\n\nprint(\"\\n--- Q3: Bin(25,0.25) ---\")\nn,p=25,0.25\nprint(f\"(a)P(X\u003c=5)={binom.cdf(5,n,p):.3f}\")\nprint(f\"(b)P(X=5)={binom.pmf(5,n,p):.3f}\")\nprint(f\"(c)P(X\u003e=5)={1-binom.cdf(4,n,p):.3f}\")\nprint(f\"(d)P(X\u003e5)={1-binom.cdf(5,n,p):.3f}\")\n\nprint(\"\\n--- Q4: Bin(25,0.40) ---\")\nn,p=25,0.40; mu=n*p; sig=(n*p*(1-p))**0.5\nprint(f\"E(X)={mu}, sigma={sig:.3f}\")\ncut=mu+2*sig\nprint(f\"mu+2sigma={cut:.3f}, P(X\u003e{int(cut)})={1-binom.cdf(int(cut),n,p):.3f}\")\n\nprint(\"\\n--- Q5: Bin(15,0.30) ---\")\nn,p=15,0.30; mu=n*p; sig=(n*p*(1-p))**0.5\nprint(f\"mean={mu}, sigma={sig:.2f}\")\nlo=mu-2*sig; hi=mu+2*sig\nprint(f\"(b) outside=[X=0 or X\u003e=9]: P={binom.pmf(0,n,p)+(1-binom.cdf(8,n,p)):.3f}\")\nprint(f\"(c) P(5\u003c=X\u003c=10)={binom.cdf(10,n,p)-binom.cdf(4,n,p):.3f}\")\nprint(f\"(d) E[revenue]=60*{n*p}+1350=${60*n*p+1350:.0f}\")\n\nprint(\"\\n--- Q6: Bin(30,0.03) ---\")\nn,p=30,0.03; mu=n*p; sig=(n*p*(1-p))**0.5\nprint(f\"(a) P(X=1)={binom.pmf(1,n,p):.3f}\")\nprint(f\"(b) P(X\u003e=1)={1-binom.pmf(0,n,p):.3f}\")\nprint(f\"(c) P(X\u003e=2)={1-binom.cdf(1,n,p):.3f}\")\nprint(f\"(d) P(within 2SD)=P(0\u003c=X\u003c=2)={binom.cdf(2,n,p):.3f}\")\nprint(f\"(e) avg time={(n*(p*4.5+(1-p)*3))/n:.2f} hr\")\n\nprint(\"\\n--- Q7: n=25 ---\")\nprint(f\"(a) P(reject|p=0.6)=P(X\u003c=15|Bin(25,0.6))={binom.cdf(15,25,0.6):.3f}\")\nprint(f\"(b) P(not reject|p=0.5)={1-binom.cdf(15,25,0.5):.3f}\")\nprint(f\"(b) P(not reject|p=0.4)={1-binom.cdf(15,25,0.4):.3f}\")\nprint(f\"(c) new: P(reject|p=0.6)={binom.cdf(14,25,0.6):.3f}\")\nprint(f\"(c) new: P(not reject|p=0.5)={1-binom.cdf(14,25,0.5):.3f}\")\nprint(f\"(c) new: P(not reject|p=0.4)={1-binom.cdf(14,25,0.4):.3f}\")\n\nprint(\"\\n--- Q8 ---\")\nprint(f\"(a) Debit: mean={100*0.2:.0f}, var={100*0.2*0.8:.0f}\")\nprint(f\"(b) Non-cash: mean={100*0.8:.0f}, var={100*0.8*0.2:.0f}\")\n\nprint(\"\\n=== SECTION 3.5 ===\")\nprint(\"\\n--- Q1: h(x;6,7,17) ---\")\nN,M,n=17,7,6\nprint(f\"P(X=4)={hypergeom.pmf(4,N,M,n):.4f}\")\nprint(f\"P(X\u003c=4)={hypergeom.cdf(4,N,M,n):.4f}\")\nprint(f\"P(X\u003e=4)={1-hypergeom.cdf(3,N,M,n):.4f}\")\nmu=n*M/N; var=n*(M/N)*((N-M)/N)*(N-n)/(N-1)\nprint(f\"mean={mu:.3f}, sigma={var**0.5:.3f}\")\n\nprint(\"\\n--- Q2: h(x;15,35,60) ---\")\nN,M,n=60,35,15\nprint(f\"(a) P(X=10)={hypergeom.pmf(10,N,M,n):.4f}\")\nprint(f\"(b) P(X\u003e=10)={1-hypergeom.cdf(9,N,M,n):.4f}\")\nP_ge10=1-hypergeom.cdf(9,N,M,n)\nP_le5=hypergeom.cdf(5,N,M,n)\nprint(f\"(c) P(\u003e=10 same)={P_ge10+P_le5:.4f}\")\nmu=n*M/N; var=n*(M/N)*((N-M)/N)*(N-n)/(N-1)\nprint(f\"(d) mean={round(mu)}, sigma={var**0.5:.3f}\")\nprint(f\"(e) mean={round(35-mu)}, sigma={var**0.5:.3f}\")\n\nprint(\"\\n--- Q4: h(x;19,12,24) granite ---\")\nN,M,n=24,12,19\nmu=n*M/N; sig=(n*(M/N)*((N-M)/N)*(N-n)/(N-1))**0.5\nprint(f\"Range x={max(0,n-(N-M))} to {min(M,n)}\")\nfor x in range(max(0,n-(N-M)),min(M,n)+1):\n    print(f\"x={x}: p={hypergeom.pmf(x,N,M,n):.4f}\")\nP_allg=hypergeom.pmf(12,N,M,n); P_allb=hypergeom.pmf(7,N,M,n)\nprint(f\"(b) P(all one type)={P_allg+P_allb:.4f}\")\nprint(f\"mean={mu:.4f}, sigma={sig:.4f}\")\nlo=mu-sig; hi=mu+sig\n# integer bounds\nlo_i=int(lo)+1 if lo\u003eint(lo) else int(lo)\nhi_i=int(hi)\nP_w1=sum(hypergeom.pmf(x,N,M,n) for x in range(lo_i,hi_i+1))\nprint(f\"(c) P(within 1 SD of {mu:.4f})=P({lo_i}\u003c=X\u003c={hi_i})={P_w1:.4f}\")\n\nprint(\"\\n--- Q5: ---\")\nprint(\"(a) pmf: h(x;20,24,60)\")\nprint(\"(b) approx: b(x;20,0.4)\")\nN2,M2,n2=600,240,20\nmu_e=n2*M2/N2; v_e=n2*(M2/N2)*((N2-M2)/N2)*(N2-n2)/(N2-1)\nprint(f\"(c) Exact: E(X)={mu_e:.2f}, V(X)={v_e:.2f}\")\nprint(f\"(c) Approx: E(X)={n2*0.4:.2f}, V(X)={n2*0.4*0.6:.2f}\")\n\nprint(\"\\n--- Q6: Negative Binomial r=3, p=0.2 ---\")\nr,p=3,0.2\ndef nb(x,r,p):\n    return comb(x+r-1,r-1)*(p**r)*((1-p)**x)\nprint(f\"(a) pmf: nb(x;3,0.2)\")\nprint(f\"(b) P(buy 5)=P(2 failures)={nb(2,r,p):.4f}\")\nprint(f\"(c) P(at most 5)={sum(nb(x,r,p) for x in range(3)):.4f}\")\nprint(f\"(d) E[non-prize boxes]={r*(1-p)/p:.0f}, E[total boxes]={r/p:.0f}\")\nEOF\n"}`

## Actions Taken

**Files created:**
_None_

**Files modified:**
_None_

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
_None_


