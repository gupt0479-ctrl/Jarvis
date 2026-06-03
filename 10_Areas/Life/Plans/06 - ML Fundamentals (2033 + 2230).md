---
type: evergreen
status: active
created: 2026-06-03
updated: 2026-06-03
tags:
  - plan
  - summer
  - ml
  - linear-algebra
notes:
  - "[[00 - Summer Plans Index]]"
  - "[[01 - Daily Operating System]]"
  - "[[CSCI 2033 Board]]"
  - "[[MATH 2230 Board]]"
  - "[[04 - Summer Courses Ops]]"
next: "[[02 - Weekly Operating System]]"
---

# ML Fundamentals (CSCI 2033 + MATH 2230)

The math base for ML, built from two sources: **CSCI 2033 (linear algebra)** relearned from scratch, and **MATH 2230 (probability & statistics)** mined for concept notes as the course runs. This is a **repeatable daily/weekly system**, not a reading list. No half-assed learning — every block names a subtopic, an output, and a done definition.

CSCI 2033 board is archived ([[CSCI 2033 Board]]); concepts/templates live under `10_Areas/UMN/Previous Classes/CSCI/CSCI 2033/` and `30_Order/Templates/Previous Templates/CSCI 2033 Template.md`. Respect `.claude/skills/organize-csci2033.md` safety rules when merging concept notes.

## Daily system — CSCI 2033 (30–45 min)

1. Take the **next subtopic** in the linear-algebra sequence below.
2. Learn it actively: re-derive the rule or work examples — don't just reread.
3. Produce **one vault output**: a rule statement, a worked derivation, OR 3 practice problems solved.
4. Note the **ML connection** in one line (why this matters for ML).

**Done when:** subtopic named + one output committed to a 2033 concept note + ML-connection line written.

**MVP:** 3 practice problems on the current subtopic, ML-connection line, no new note.

### Linear algebra sequence (2033 → ML)

| # | Subtopic | ML connection |
|---|----------|---------------|
| 1 | Vectors, vector operations, dot product | Feature vectors; similarity |
| 2 | Matrices, matrix multiplication | Linear layers; batched ops |
| 3 | Systems of linear equations, Gaussian elimination | Solving for weights; least squares setup |
| 4 | Linear independence, span, basis | Feature redundancy; dimensionality |
| 5 | Rank, null space, column space | Degenerate features; solvability |
| 6 | Determinant & inverse | Invertibility; closed-form solutions |
| 7 | Vector spaces & subspaces | Embedding spaces |
| 8 | Orthogonality, projections | Least squares, OLS regression |
| 9 | Gram-Schmidt / QR | Numerical stability |
| 10 | Eigenvalues & eigenvectors | PCA, spectral methods |
| 11 | Diagonalization | Decorrelation; covariance |
| 12 | SVD | PCA, low-rank approximation, embeddings |

> Sequence is the spine. ~12 subtopics → one per study day ≈ 2.5 weeks of Dubai to a working LA base, then reinforce via problems.

## Weekly system — MATH 2230 → ML concept notes

MATH 2230 is learned for its grade ([[04 - Summer Courses Ops]]) **and** mined for ML. Each week, as the course covers a topic, write **≥1 core concept note** framed for ML — not homework restatement.

| Course topic (as it arrives) | ML concept note to write |
|---|---|
| Probability axioms, conditional prob | Bayes rule → naive Bayes, posterior intuition |
| Random variables, distributions | Gaussian/Bernoulli as model assumptions |
| Expectation & variance | Loss expectations; bias-variance |
| Joint / marginal / covariance | Covariance matrix → PCA, multivariate Gaussian |
| Estimation (MLE) | Maximum likelihood = the training objective |
| Hypothesis testing, confidence intervals | Evaluation, significance of metric gaps |

**Done when:** ≥1 ML-framed concept note created that week, linked from the MATH 2230 MOC.

## How this wires into daily/weekly ops

- **Daily:** the "CSCI 2033 30–45 min" row in [[01 - Daily Operating System]] pulls the next sequence subtopic.
- **Weekly:** [[02 - Weekly Operating System]] checks "≥1 MATH 2230 ML concept note created."
- **Phase:** front-load the 2033 sequence in **Dubai** (build the LA base); 2230 notes accrue across the whole term as the course runs.
