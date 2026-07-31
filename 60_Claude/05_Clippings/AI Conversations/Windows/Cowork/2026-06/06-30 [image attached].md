---
type: input
input_kind: ai-conversation
source_app: cowork
source_os: windows
title: "[image attached]"
started_at: 2026-06-30T01:32:35
ended_at: 2026-06-30T01:35:48
exported_at: 2026-07-31T21:04:06
duration_minutes: 3.2
project: 2026-06
session_id: fcb32183-30d5-4356-8e48-9e3ed564f22b
status: raw
turn_count: 3
tools_used:
  mcp__jarvis-fs__list_directory: 1
  mcp__jarvis-fs__read_file: 1
  mcp__workspace__bash: 2
  TaskCreate: 1
  TaskUpdate: 2
  ToolSearch: 2
tokens:
  input: 26
  output: 20146
  cache_creation: 145563
  cache_read: 705546
  total: 871281
cost_usd: 1.38731
model:
  - "claude-sonnet-4-6"
files_touched: []
tags:
  - input
  - ai-conversation
  - cowork
  - windows
---

# [image attached]

## You

[image attached]

[image attached]

[image attached]

Solve every question in `20_Progress/Degree/MATH 2230/Quiz/Practice Quiz -2`. Read the quiz file first. For each question: show the key step(s) and the final answer. Prioritize correctness above all. Keep explanations minimal — one or two lines of reasoning per part, then the answer. Run all arithmetic in Python to verify before responding. Do not narrate your process; deliver all answers in one response.

## You

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]

[Image: original 1700x2200, displayed at 1545x2000. Multiply coordinates by 1.10 to map to original image.]

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

### Tool Calls

- `ToolSearch` -- `{"query":"select:TaskCreate,TaskUpdate","max_results":2}`
- `ToolSearch` -- `{"query":"select:mcp__jarvis-fs__read_file,mcp__jarvis-fs__list_directory","max_results":2}`
- `TaskCreate` -- `{"subject":"Solve Practice Quiz 2 — Math 2230","description":"Read quiz file, run all arithmetic in Python, deliver answers for all questions.","activeForm":"Reading quiz and running calculations"}`
- `mcp__jarvis-fs__list_directory` -- `{"path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Degree\\MATH 2230\\Quiz"}`
- `TaskUpdate` -- `{"taskId":"1","status":"in_progress"}`
- `mcp__jarvis-fs__read_file` -- `{"path":"D:\\Users\\_Anant\\10_Areas\\Documents\\Jarvis\\20_Progress\\Degree\\MATH 2230\\Quiz\\Practice Quiz - 2.md"}`
- `mcp__workspace__bash` -- `{"command":"python3 \u003c\u003c \u0027EOF\u0027\nfrom scipy import stats\nfrom scipy.special import comb\nimport numpy as np\n\nprint(\"=\"*60)\nprint(\"Q2: Binomial n=10, p=0.6\")\nprint(\"=\"*60)\nn, p = 10, 0.6\nrv = stats.binom(n, p)\nmu = n*p; sigma = np.sqrt(n*p*(1-p))\nprint(f\"mu={mu}, sigma={sigma:.6f}\")\n\n# (a) P(X \u003e= 5)\npa = 1 - rv.cdf(4)\nprint(f\"(a) P(X\u003e=5) = {pa:.3f}\")\n\n# (b) within 1 std dev of mean: P(mu-sigma \u003c= X \u003c= mu+sigma)\nlo = mu - sigma; hi = mu + sigma\nprint(f\"  1 sd range: [{lo:.4f}, {hi:.4f}] -\u003e integers [{int(np.ceil(lo))}, {int(np.floor(hi))}]\")\npb = rv.cdf(int(np.floor(hi))) - rv.cdf(int(np.ceil(lo))-1)\nprint(f\"(b) P(within 1 sd) = {pb:.3f}\")\n\n# (c) store has 6 each; need oversize \u003c=6 AND midsize \u003c=6\n# midsize = 10-X, so midsize \u003c=6 means X\u003e=4\n# need 4\u003c=X\u003c=6\npc = rv.cdf(6) - rv.cdf(3)\nprint(f\"(c) P(4\u003c=X\u003c=6) = {pc:.3f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q3: Negative Binomial r=2, p=0.1\")\nprint(\"=\"*60)\n# X = number of failures (boxes without prize) before r=2 successes\nr, p3 = 2, 0.1\n\n# (a) Correct notation: nb(x; 2, 0.1)\nprint(\"(a) nb(x; 2, 0.1)\")\n\n# (b) P(purchase 4 boxes total) = P(3 failures before 2nd success) \n# Because 4 boxes total, 2 successes, so 2 failures =\u003e x=2\n# nb PMF: P(X=x) = C(x+r-1, r-1) * p^r * (1-p)^x\ndef nb_pmf(x, r, p):\n    return comb(x+r-1, r-1, exact=True) * p**r * (1-p)**x\n\npb3 = nb_pmf(2, r, p3)\nprint(f\"(b) P(4 boxes total) = P(X=2 failures) = {pb3:.4f}\")\n\n# (c) P(at most 4 boxes) = P(X\u003c=2 failures)\npc3 = sum(nb_pmf(x, r, p3) for x in range(3))\nprint(f\"(c) P(at most 4 boxes) = P(X\u003c=2) = {pc3:.4f}\")\n\n# (d)\nE_failures = r*(1-p3)/p3\nE_total = E_failures + r\nprint(f\"(d) E(failures without prize) = {E_failures:.1f}, E(total boxes) = {E_total:.1f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q4: Poisson\")\nprint(\"=\"*60)\n# (a) t=1 hr, mu=8\nmu4a = 8\nrv4a = stats.poisson(mu4a)\np_eq8 = rv4a.pmf(8)\np_ge8 = 1 - rv4a.cdf(7)\np_ge11 = 1 - rv4a.cdf(10)\nprint(f\"(a) P(X=8)={p_eq8:.3f}, P(X\u003e=8)={p_ge8:.3f}, P(X\u003e=11)={p_ge11:.3f}\")\n\n# (b) t=45min=0.75hr, mu=6\nmu4b = 8*0.75\nsigma4b = np.sqrt(mu4b)\nprint(f\"(b) E(X)={mu4b:.4f}, sd={sigma4b:.4f}\")\n\n# (c) t=2.5hr, mu=20\nmu4c = 8*2.5\nrv4c = stats.poisson(mu4c)\np_ge24 = 1 - rv4c.cdf(23)\np_le13 = rv4c.cdf(13)\nprint(f\"(c) P(X\u003e=24)={p_ge24:.3f}, P(X\u003c=13)={p_le13:.3f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q5: CDF F(x)=(x/7)[1+ln(7/x)] for 0\u003cx\u003c=7\")\nprint(\"=\"*60)\ndef F5(x):\n    return (x/7)*(1 + np.log(7/x))\n\npa5 = F5(5)\npb5 = F5(6) - F5(5)\nprint(f\"(a) P(X\u003c=5) = F(5) = {pa5:.3f}\")\nprint(f\"(b) P(5\u003c=X\u003c=6) = F(6)-F(5) = {pb5:.3f}\")\nprint(f\"(c) f(x) = ln(7/x)/7  for 0 \u003c x \u003c= 7\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q6: Normal mu=107, sigma=2\")\nprint(\"=\"*60)\nmu6, sigma6 = 107, 2\nrv6 = stats.norm(mu6, sigma6)\np_eq108 = 0  # continuous\np_lt108 = rv6.cdf(108)\np_atmost108 = rv6.cdf(108)\nprint(f\"(a) P(X=108)=0, P(X\u003c108)={p_lt108:.4f}, P(X\u003c=108)={p_atmost108:.4f}\")\n\npb6 = 1 - (rv6.cdf(109) - rv6.cdf(105))  # P(|X-107|\u003e2) = 1-P(105\u003cX\u003c109)\n# Actually: P(|X-mu|\u003esigma) = P(|Z|\u003e1)\npb6 = 2*(1 - stats.norm.cdf(1))\nprint(f\"(b) P(|X-107|\u003e2) = P(|Z|\u003e1) = {pb6:.4f}  -- No, does NOT depend on mu/sigma\")\n\n# (c) most extreme 0.6%: bottom 0.3% and top 0.3%\nz_low = stats.norm.ppf(0.003)\nz_high = stats.norm.ppf(0.997)\nx_low = mu6 + z_low*sigma6\nx_high = mu6 + z_high*sigma6\nprint(f\"(c) Below {x_low:.2f} and above {x_high:.2f} mmol/L\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q7: Normal approx to Binomial n=200, p=0.12\")\nprint(\"=\"*60)\nn7, p7 = 200, 0.12\nmu7 = n7*p7\nsigma7 = np.sqrt(n7*p7*(1-p7))\nprint(f\"mu={mu7}, sigma={sigma7:.6f}\")\n\n# Continuity correction\npa7 = stats.norm.cdf((30.5 - mu7)/sigma7)\npb7 = stats.norm.cdf((29.5 - mu7)/sigma7)\npc7 = stats.norm.cdf((25.5 - mu7)/sigma7) - stats.norm.cdf((14.5 - mu7)/sigma7)\nprint(f\"(a) P(X\u003c=30) approx = {pa7:.4f}\")\nprint(f\"(b) P(X\u003c30) approx = {pb7:.4f}\")\nprint(f\"(c) P(15\u003c=X\u003c=25) approx = {pc7:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q8: Exponential mean=2.835\")\nprint(\"=\"*60)\nmean8 = 2.835\nlam8 = 1/mean8\nrv8 = stats.expon(scale=mean8)\npa8_ge2 = 1 - rv8.cdf(2)\npa8_le3 = rv8.cdf(3)\npa8_bet = rv8.cdf(3) - rv8.cdf(2)\nprint(f\"(a) P(X\u003e=2)={pa8_ge2:.4f}, P(X\u003c=3)={pa8_le3:.4f}, P(2\u003c=X\u003c=3)={pa8_bet:.4f}\")\n\n# (b) mean=2.835, sd=2.835\n# P(X \u003e mean + 4*sd) = P(X \u003e 5*2.835) = e^{-5}\npb8_exceed = np.exp(-5)\n# P(X \u003c mean - 1*sd) = P(X \u003c 0) = 0 since mean-sd=0\npb8_less = 0\nprint(f\"(b) P(X\u003emean+4sd)=e^(-5)={pb8_exceed:.4f}, P(X\u003cmean-sd)=P(X\u003c0)={pb8_less}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q9: CLT, mu=50, sigma=1.8\")\nprint(\"=\"*60)\nmu9, sig9 = 50, 1.8\n# (a) n=12, normal dist\nn9a = 12\nse9a = sig9/np.sqrt(n9a)\npa9 = 1 - stats.norm.cdf((51-mu9)/se9a)\nprint(f\"(a) n=12: P(Xbar\u003e=51) = {pa9:.4f}\")\n\n# (b) n=45, CLT approx\nn9b = 45\nse9b = sig9/np.sqrt(n9b)\npb9 = 1 - stats.norm.cdf((51-mu9)/se9b)\nprint(f\"(b) n=45: P(Xbar\u003e=51) approx = {pb9:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q10 (Written): Professor lecture problem f(x)=kx^3, 0\u003c=x\u003c=2\")\nprint(\"=\"*60)\n# (a) Find k: integral from 0 to 2 of kx^3 dx = 1\n# k * [x^4/4] from 0 to 2 = k * 16/4 = 4k = 1 =\u003e k = 1/4\nk10 = 1/4\nprint(f\"(a) k = {k10}\")\n\n# (b) P(X\u003c=1) = integral 0 to 1 of (1/4)x^3 dx = (1/4)[x^4/4] from 0 to 1 = 1/16\npb10 = k10 * (1**4/4)\nprint(f\"(b) P(X\u003c=1) = {pb10:.4f}\")\n\n# (c) P(75sec \u003c= X \u003c= 105sec) in MINUTES: 75/60=1.25, 105/60=1.75\nlo10 = 75/60; hi10 = 105/60\npc10 = k10*(hi10**4/4 - lo10**4/4)\nprint(f\"(c) P(1.25\u003c=X\u003c=1.75) = {pc10:.4f}\")\n\n# (d) P(X \u003e= 105/60) = P(X \u003e= 1.75)\npd10 = k10*(2**4/4 - (105/60)**4/4)\nprint(f\"(d) P(X\u003e=1.75) = {pd10:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q11 (Written): Dishwasher soap sampling distribution\")\nprint(\"=\"*60)\n# X1, X2 ~ pkg sizes {25, 40, 60} with p={0.2, 0.5, 0.3}\n# xbar = (X1+X2)/2\n# All possible pairs and their probs:\nsizes = [25, 40, 60]\nprobs = [0.2, 0.5, 0.3]\n\nxbar_dist = {}\ns2_dist = {}\nfor i, (x1, p1) in enumerate(zip(sizes, probs)):\n    for j, (x2, p2) in enumerate(zip(sizes, probs)):\n        xb = (x1+x2)/2\n        s2 = ((x1-xb)**2 + (x2-xb)**2)/1  # sample variance with n-1=1\n        prob = p1*p2\n        xbar_dist[xb] = xbar_dist.get(xb, 0) + prob\n        s2_dist[s2] = s2_dist.get(s2, 0) + prob\n\nprint(\"(a) Sampling distribution of Xbar:\")\nfor xb in sorted(xbar_dist):\n    print(f\"  xbar={xb}: p={xbar_dist[xb]:.4f}\")\n\nE_xbar = sum(xb*p for xb,p in xbar_dist.items())\nprint(f\"(b) E(Xbar) = {E_xbar:.4f}\")\n\nprint(\"(c) Sampling distribution of s^2:\")\nfor s2 in sorted(s2_dist):\n    print(f\"  s2={s2}: p={s2_dist[s2]:.4f}\")\n\nE_s2 = sum(s2*p for s2,p in s2_dist.items())\nprint(f\"(d) E(S^2) = {E_s2:.4f}\")\n\n# Verify: population variance\nE_X = sum(x*p for x,p in zip(sizes,probs))\nE_X2 = sum(x**2*p for x,p in zip(sizes,probs))\npop_var = E_X2 - E_X**2\nprint(f\"\\nVerify: pop mean={E_X}, pop var={pop_var:.4f} (E(S^2) should equal pop var)\")\n\nEOF\n"}`
- `mcp__workspace__bash` -- `{"command":"pip install scipy --break-system-packages -q \u0026\u0026 python3 \u003c\u003c \u0027EOF\u0027\nfrom scipy import stats\nfrom scipy.special import comb\nimport numpy as np\n\nprint(\"=\"*60)\nprint(\"Q2: Binomial n=10, p=0.6\")\nn, p = 10, 0.6\nrv = stats.binom(n, p)\nmu = n*p; sigma = np.sqrt(n*p*(1-p))\npa = 1 - rv.cdf(4)\nlo = mu - sigma; hi = mu + sigma\npb = rv.cdf(int(np.floor(hi))) - rv.cdf(int(np.ceil(lo))-1)\npc = rv.cdf(6) - rv.cdf(3)\nprint(f\"mu={mu}, sigma={sigma:.4f}\")\nprint(f\"(a) P(X\u003e=5) = {pa:.3f}\")\nprint(f\"(b) 1-sd range [{lo:.4f},{hi:.4f}] integers [{int(np.ceil(lo))},{int(np.floor(hi))}] P={pb:.3f}\")\nprint(f\"(c) P(4\u003c=X\u003c=6) = {pc:.3f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q3: Negative Binomial r=2, p=0.1\")\nr, p3 = 2, 0.1\ndef nb_pmf(x, r, p):\n    return int(comb(x+r-1, r-1, exact=True)) * p**r * (1-p)**x\npb3 = nb_pmf(2, r, p3)\npc3 = sum(nb_pmf(x, r, p3) for x in range(3))\nE_fail = r*(1-p3)/p3\nE_tot = E_fail + r\nprint(f\"(a) nb(x; 2, 0.1)\")\nprint(f\"(b) P(4 boxes total)=P(X=2 failures)={pb3:.4f}\")\nprint(f\"(c) P(at most 4 boxes)=P(X\u003c=2)={pc3:.4f}\")\nprint(f\"(d) E(failures)={E_fail}, E(total boxes)={E_tot}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q4: Poisson\")\nmu4a = 8\nrv4a = stats.poisson(mu4a)\nprint(f\"(a) P(X=8)={rv4a.pmf(8):.3f}, P(X\u003e=8)={1-rv4a.cdf(7):.3f}, P(X\u003e=11)={1-rv4a.cdf(10):.3f}\")\nmu4b = 8*0.75\nprint(f\"(b) E(X)={mu4b}, sd={np.sqrt(mu4b):.4f}\")\nrv4c = stats.poisson(8*2.5)\nprint(f\"(c) P(X\u003e=24)={1-rv4c.cdf(23):.3f}, P(X\u003c=13)={rv4c.cdf(13):.3f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q5: F(x)=(x/7)[1+ln(7/x)]\")\ndef F5(x): return (x/7)*(1 + np.log(7/x))\npa5 = F5(5); pb5 = F5(6)-F5(5)\nprint(f\"(a) F(5)={pa5:.3f}\")\nprint(f\"(b) F(6)-F(5)={pb5:.3f}\")\nprint(f\"(c) f(x) = ln(7/x)/7  for 0 \u003c x \u003c= 7\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q6: Normal mu=107, sigma=2\")\nrv6 = stats.norm(107, 2)\np108 = rv6.cdf(108)\npb6 = 2*(1-stats.norm.cdf(1))\nz003 = stats.norm.ppf(0.003)\nprint(f\"(a) P(X=108)=0, P(X\u003c108)=P(X\u003c=108)={p108:.4f}\")\nprint(f\"(b) P(|X-107|\u003e2)=P(|Z|\u003e1)={pb6:.4f}  --  No, does NOT depend on mu/sigma\")\nprint(f\"(c) Below {107+z003*2:.2f} and above {107-z003*2:.2f} mmol/L\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q7: Normal approx to Bin n=200, p=0.12\")\nmu7 = 200*0.12; sigma7 = np.sqrt(200*0.12*0.88)\nprint(f\"mu={mu7}, sigma={sigma7:.6f}\")\npa7 = stats.norm.cdf((30.5-mu7)/sigma7)\npb7 = stats.norm.cdf((29.5-mu7)/sigma7)\npc7 = stats.norm.cdf((25.5-mu7)/sigma7)-stats.norm.cdf((14.5-mu7)/sigma7)\nprint(f\"(a) P(X\u003c=30)={pa7:.4f}\")\nprint(f\"(b) P(X\u003c30)={pb7:.4f}\")\nprint(f\"(c) P(15\u003c=X\u003c=25)={pc7:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q8: Exponential mean=2.835\")\nrv8 = stats.expon(scale=2.835)\nprint(f\"(a) P(X\u003e=2)={1-rv8.cdf(2):.4f}, P(X\u003c=3)={rv8.cdf(3):.4f}, P(2\u003c=X\u003c=3)={rv8.cdf(3)-rv8.cdf(2):.4f}\")\nprint(f\"(b) P(X\u003e5*2.835)=e^(-5)={np.exp(-5):.4f}, P(X\u003c0)=0\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q9: CLT mu=50, sigma=1.8\")\nmu9, sig9 = 50, 1.8\npa9 = 1-stats.norm.cdf((51-mu9)/(sig9/np.sqrt(12)))\npb9 = 1-stats.norm.cdf((51-mu9)/(sig9/np.sqrt(45)))\nprint(f\"(a) n=12: P(Xbar\u003e=51)={pa9:.4f}\")\nprint(f\"(b) n=45: P(Xbar\u003e=51)={pb9:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q10: f(x)=kx^3, 0\u003c=x\u003c=2 (X in minutes)\")\nk10 = 1/4\npb10 = k10*(1**4/4)\nlo10=75/60; hi10=105/60\npc10 = k10*(hi10**4/4 - lo10**4/4)\npd10 = k10*(2**4/4 - (105/60)**4/4)\nprint(f\"(a) k={k10}\")\nprint(f\"(b) P(X\u003c=1)={pb10:.4f}\")\nprint(f\"(c) P(1.25\u003c=X\u003c=1.75)={pc10:.4f}\")\nprint(f\"(d) P(X\u003e=1.75)={pd10:.4f}\")\n\nprint()\nprint(\"=\"*60)\nprint(\"Q11: Dishwasher soap sampling distribution\")\nsizes=[25,40,60]; probs=[0.2,0.5,0.3]\nxbar_dist={}; s2_dist={}\nfor x1,p1 in zip(sizes,probs):\n    for x2,p2 in zip(sizes,probs):\n        xb=(x1+x2)/2\n        s2=((x1-xb)**2+(x2-xb)**2)/1\n        pr=p1*p2\n        xbar_dist[xb]=xbar_dist.get(xb,0)+pr\n        s2_dist[s2]=s2_dist.get(s2,0)+pr\n\nprint(\"(a):\")\nfor xb in sorted(xbar_dist): print(f\"  xbar={xb}: p={xbar_dist[xb]:.4f}\")\nE_xb=sum(xb*p for xb,p in xbar_dist.items())\nprint(f\"(b) E(Xbar)={E_xb:.4f}\")\nprint(\"(c):\")\nfor s2 in sorted(s2_dist): print(f\"  s2={s2}: p={s2_dist[s2]:.4f}\")\nE_s2=sum(s2*p for s2,p in s2_dist.items())\nprint(f\"(d) E(S^2)={E_s2:.4f}\")\nE_X=sum(x*p for x,p in zip(sizes,probs))\nE_X2=sum(x**2*p for x,p in zip(sizes,probs))\nprint(f\"Pop variance check: {E_X2-E_X**2:.4f}\")\nEOF\n"}`
- `TaskUpdate` -- `{"taskId":"1","status":"completed"}`

## Actions Taken

**Files created:**
_None_

**Files modified:**
_None_

**Files deleted (heuristic, from Bash commands):**
_None detected_

**Commands run:**
_None_


