---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "There were a lot of questions in that specified file, solve"
started_at: 2026-07-23T22:56:26
ended_at: 2026-07-24T23:17:15
project: Cowork
status: raw
session_id: f8c024e1-ae75-49a0-99b5-a81b13136b5c
tags:
  - input
  - ai-conversation
  - claude-code
---

# There were a lot of questions in that specified file, solve

## Claude

**Q1 — 90% CI for mean difference (After − Before), n=10, paired t**

d = −2, 7, −3, 0, 9, 4, −5, 3, 4, 11 → d̄ = 2.8, sd = 5.287, sd/√n = 1.672
t₀.₀₅,₉ = 1.833 → E = 1.833(1.672) = 3.065

**μd = 2.8 ± 3.065 → (−0.265, 5.865)**

**Q2 — χ² test of independence, α = 0.05**

H₀: attitude toward jokes independent of grade. df = (3−1)(2−1) = 2, χ²crit = 5.991

Expected (row total × col total / 200):

| | Funny | Not Funny |
|---|---|---|
|A/B|24.7|51.3|
|C/D|27.3|56.7|
|F/W|13.0|27.0|

χ² components: 0.068, 0.033 / 0.501, 0.241 / 1.923, 0.926

χ² = 3.693, df=2, p = 0.158

**χ² = 3.693 < 5.991 → fail to reject H₀. Not enough evidence that attitude toward jokes is related to grade.**

*Tools used: mcp__workspace__bash*

## You

There were a lot of questions in that specified file, solve all the questions correctly. The last 2 questions have been provided as images Refer to the note for all the questions and the images are for help(formulas). The last 2 questions are also images that have been provided to you already. The first question is 2., solve each of them correctly.

## Claude

**Q2 — Two-sample t (Welch), fixed vs floating platen**

H0: μ1−μ2=0, Ha: μ1−μ2≠0

se=√(25²/10+41²/10)=15.19, t=(808−757)/15.19=**3.4**, df≈14.9, **P-value=0.004**

Conclusion: Reject H0 — sufficient evidence the difference is non-zero.

Agree with author? **No**, the difference is significant.

Assumptions: both distributions approximately normal; data randomly sampled. (Not: equal variances, equal means, equal distributions.)

**Q3 — 99% CI, 7-day vs 28-day strength (large sample, z)**

diff = 26.93−36.76 = −9.83, se=√(4.81²/69+6.49²/74)=0.951, z₀.₀₀₅=2.576, E=2.45

**CI: (−12.28, −7.38) N/mm²**

Interpretation: with 99% confidence, the true difference falls between these values.

**Q4 — Cushing's disease, paired**

(a) μD=0 implies the average time difference is **0 months**, which is **unlikely** — diagnosis can't precede symptom onset.

(b) μD=μonset−μdiagnosis. H0: μD = −25, Ha: μD < −25

d̄=−38.87, sd=23.17, se=5.98, **t=−2.32**, df=14, **P-value=0.0181**

Conclusion: Reject H0 — data suggest diagnosis happens on average more than 25 months after onset.

**Q5 — Regression, axial strength on cube strength**

(a) **ŷ = −31.4660 + 0.9842x**. Slope: a one MPa increase in cube strength → increase in predicted axial strength equal to the slope.

(b) **r² = 0.6178** — proportion of observed variation in axial strength that CAN be attributed to its linear relationship with cube strength.

(c) SSE=367.80, **s = 6.780 MPa** — model predictions typically differ from actual axial strength by an amount within one error standard deviation.

**Q6 — Correlation test, hydrogen content vs porosity (r=0.433, n=14)**

(a) H0: ρ=0, Ha: ρ≠0

t = 0.433√12/√(1−0.433²) = **1.66**, df=12, **P-value=0.122**

Conclusion: Fail to reject H0 — data doesn't suggest ρ differs significantly from 0.

(b) r²×100 = **18.7%**

**Q7 — GOF test, homicides by season (α=0.01)**

H0: p1=p2=p3=p4=0.25, Ha: at least one pi≠0.25

exp=339.5 each, **χ²=4.73**, df=3 → **P-value > 0.10**

Conclusion: Fail to reject H0 — no evidence of a seasonal relationship.

**Q8 — Homogeneity test, foot asymmetry by gender (α=0.05)**

H0: p1i=p2i for i=1,2,3, Ha: at least one p1i≠p2i

Expected: Men (15.43, 11.65, 12.91), Women (33.57, 25.35, 28.09)

**χ²=39.553**, df=2 → **P-value < 0.005**

Conclusion: Reject H0 — strong evidence gender affects foot asymmetry.

**Q9 — Chi-square independence, jokes vs grade (image, α=0.05)**

Expected: (24.7, 51.3)/(27.3, 56.7)/(13.0, 27.0); **χ²=3.693**, df=2, crit=5.991

Fail to reject H0 — no evidence attitude toward jokes is related to grade.

**Q10 — Paired 90% CI, QuizWizards before/after (image)**

d̄=2.8, sd=5.287, se=1.672, t₀.₀₅,₉=1.833

**μd: (−0.265, 5.865)**

All arithmetic verified in Python (scipy.stats). Q1, Q9(written page), Q11 are non-computational (proctoring/acknowledgment/completion screens) — no answer needed.

**Q9 — Paired 90% CI for net difference in test scores (QuizWizards)**

Step 1 — differences, d = After − Before, for each of the 10 students:

| Student | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Before | 90 | 72 | 81 | 63 | 85 | 94 | 70 | 92 | 89 | 76 |
| After | 88 | 79 | 78 | 63 | 94 | 98 | 65 | 95 | 93 | 87 |
| d | −2 | 7 | −3 | 0 | 9 | 4 | −5 | 3 | 4 | 11 |

Step 2 — sample mean of differences: Σd = 28, n = 10 → d̄ = 28/10 = **2.8**

Step 3 — sample SD of differences. Deviations (d − d̄): −4.8, 4.2, −5.8, −2.8, 6.2, 1.2, −7.8, 0.2, 1.2, 8.2
Squared: 23.04, 17.64, 33.64, 7.84, 38.44, 1.44, 60.84, 0.04, 1.44, 67.24 → Σ = 251.6

s_d = √(251.6/9) = √27.956 = **5.287**

Step 4 — standard error: s_d/√n = 5.287/√10 = **1.672**

Step 5 — critical value: 90% CI, df = n−1 = 9, two-tailed α/2 = 0.05 → t₀.₀₅,₉ = **1.833** (from t-table)

Step 6 — margin of error: E = 1.833 × 1.672 = **3.065**

Step 7 — interval: μ_d = d̄ ± E = 2.8 ± 3.065

**90% CI: (−0.265, 5.865)**

Interpretation: We're 90% confident the true mean difference in test scores (after − before) lies between −0.265 and 5.865 points. Since the interval contains 0, the data do not provide strong evidence that the QuizWizards technique produces a real average change in scores.

---

**Q10 — χ² test of independence: joke attitude vs. grade (Mr. Dickie), α = 0.05**

**H — Hypotheses**
H₀: attitude toward the jokes and final grade group are independent
Hₐ: attitude toward the jokes and final grade group are associated

**D — Distribution / decision rule**
Test statistic ~ χ² with df = (rows−1)(cols−1) = (3−1)(2−1) = 2
Critical value at α = 0.05, df = 2: **χ²₀.₀₅,₂ = 5.991**
Decision rule: reject H₀ if χ² > 5.991

Observed:

| | Funny | Not Funny | Row total |
|---|---|---|---|
| A or B | 26 | 50 | 76 |
| C or D | 31 | 53 | 84 |
| F or W | 8 | 32 | 40 |
| Col total | 65 | 135 | **200** |

Expected (row total × col total ÷ 200):

| | Funny | Not Funny |
|---|---|---|
| A or B | 76×65/200 = 24.70 | 76×135/200 = 51.30 |
| C or D | 84×65/200 = 27.30 | 84×135/200 = 56.70 |
| F or W | 40×65/200 = 13.00 | 40×135/200 = 27.00 |

All expected counts ≥ 5, so the χ² approximation is valid.

**T — Test statistic.** χ² components (obs−exp)²/exp:

| | Funny | Not Funny |
|---|---|---|
| A or B | (26−24.7)²/24.7 = 0.068 | (50−51.3)²/51.3 = 0.033 |
| C or D | (31−27.3)²/27.3 = 0.501 | (53−56.7)²/56.7 = 0.241 |
| F or W | (8−13)²/13 = 1.923 | (32−27)²/27 = 0.926 |

Sum: **χ² = 0.068+0.033+0.501+0.241+1.923+0.926 = 3.693**

**V — Verdict / conclusion**
χ² = 3.693 < critical value 5.991 (equivalently P-value ≈ 0.158 > 0.05) → **fail to reject H₀**.

At the 5% significance level, there is not sufficient evidence to conclude that a student's attitude toward Mr. Dickie's jokes is related to their final grade — the data are consistent with independence.

*Tools used: Read, mcp__jarvis__vault_list, mcp__jarvis__vault_read, mcp__workspace__bash*

## You

Prove me with a prompt for a new session to provide short answers for each question but for the written submission answers gives good lengthy answers as given just now. I want the prompt to focus on getting the answer correct and providing me with short solutions based on the formulas uploaded to it.

## Claude

Here's a reusable prompt for a new session.

Drop the quiz file/formula sheet in with this prompt at the start of a new session — it'll give short answers for regular questions and full step-by-step work only for the "written submission" ones.

*Tools used: Write, mcp__cowork__present_files*


