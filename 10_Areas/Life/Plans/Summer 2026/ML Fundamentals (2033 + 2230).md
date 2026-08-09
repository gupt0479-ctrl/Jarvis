---
type: plan
status: active
created: 2026-06-03
updated: 2026-07-27
tags:
  - plan
  - summer
  - ml
  - linear-algebra
  - statistics
notes:
  - "[[00 - Summer Plans Index]]"
  - "[[Daily Operating System]]"
  - "[[ML_Foundations]]"
  - "[[CSCI 2033 Board]]"
  - "[[MATH 2230 Board]]"
  - "[[Stocks Trading AI Hub]]"
  - "[[Final Month Plan (Jul 28 - Sep 1)]]"
next: "[[Final Month Plan (Jul 28 - Sep 1)]]"
---
# ML Fundamentals (CSCI 2033 + MATH 2230)
==CSCI 2033 supplies the linear algebra of ML, MATH 2230 supplies the probability and statistics — together the math base for an ML-engineer path, not a full course replay.== Merged 2026-07-27 with the separate progress tracker — one file, not two.
> [!WARNING]
> **Pace correction, 2026-07-27.** Zero of the 14 units in §3 were touched during Dubai or Bangalore — see §8. With one month left, the original per-unit depth (derive by hand, explain from memory, full active output) is no longer the right bar. §3's table stays as the map of what exists, but its done-definition now means "grasp the core idea + the formula + when to use it," not full derivation-level mastery. **MATH 2230 is complete as of 2026-07-27** — Track B below is historical except its still-owed bridge notes (§5).
## 1. Strategic summary
The spine is curated: only the ML-fundamentals subset of 2033 (sections 1–6 of [[ML_Foundations]]), studied in prerequisite order with no skipped dependencies. PageRank and graph ML (2033's endgame, [[ML_Foundations]] §7) are deferred to a late-summer deep pass, not skimmed now. Where 2033 and 2230 topics overlap, one study block covers both.
## 2. Two-track model
| Track | Source | Role | Cadence |
|-------|--------|------|---------|
| **A — 2033 ML spine** | `Concepts_old/` + [[ML_Foundations]] | Curated, ordered LA→ML sequence | broad pass, §7 |
| **B — 2230 live course** | `MATH 2230 - Calendar` + syllabus | Complete — only the ML bridge notes (§5) remain | historical |
## 3. ML fundamentals spine (2033) — in-scope only
Ordered units, each mapped to a real `Concepts_old/` filename. Prerequisites are explicit. Track completion in §8.
Path prefix: `10_Areas/UMN/Previous Classes/CSCI/CSCI 2033/Concepts_old/`

| #   | ML_Foundations § | Primary vault file(s)                                                                                                   | Prereq | Active output                                 | Done when                          | 2230 bridge                                |
| --- | ---------------- | ----------------------------------------------------------------------------------------------------------------------- | :----: | --------------------------------------------- | ---------------------------------- | ------------------------------------------ |
| 1   | §1               | `Vectors, Linear Functions, and the Regression Model.md`                                                                |   —    | 3 problems: dot product, linear function eval | vector ops from memory             | Descriptive stats, mean                    |
| 2   | §1               | `Norms, Distance, Standard Deviation, and Angles.md`                                                                    |   1    | derive ‖x‖, distance, cosine                  | compute norm/angle by hand         | Variance, std dev                          |
| 3   | §1–2             | `Linear Independence, Bases, Orthonormality, and Matrices.md`                                                           |   1    | check independence; build orthonormal set     | explain span/basis                 | —                                          |
| 4   | §2               | `Geometric Transformations, Graphs, Linear Equations, and the Matrix Class.md` *(LA core only; defer graph subsection)* |   3    | matrix as transform; 2 products               | matrix-vector by hand              | —                                          |
| 5   | §2               | `Linear Systems, Inverses, Pseudo-Inverse, and Polynomial Interpolation.md`                                             |   4    | solve a system; pseudo-inverse meaning        | when inverse exists vs pseudo      | —                                          |
| 6   | §2               | `Matrix–Matrix Products, QR Factorization, and Householder Reflectors.md` *(QR in-scope; PageRank subsection defers)*   |   5    | Gram–Schmidt QR on 3×3                        | QR by hand, why numerically stable | —                                          |
| 7   | §2               | `Vectors, Linear Functions, and the Regression Model.md` + `Least Squares and Feature Engineering.md`                   |   6    | fit least-squares line; min ‖Aβ−b‖²           | regression as projection           | **Estimation, MLE**                        |
| 8   | §2               | `Least Squares and Feature Engineering.md`                                                                              |   7    | add polynomial features; show overfit         | train vs test U-curve              | Bias-variance intuition                    |
| 9   | §3               | `Least Squares Classifiers, Optimization, and Gradient Descent.md`                                                      |   7    | LS classifier, ±1 labels, threshold           | decision boundary = hyperplane     | **Conditional prob, Bayes**                |
| 10  | §5               | `Least Squares Classifiers, Optimization, and Gradient Descent.md`                                                      |   9    | code gradient descent on a loss               | role of step size; SGD vs GD       | **Expectation of loss, variance**          |
| 11  | §6               | `Singular Value Decomposition and Eigenfaces.md`                                                                        |   6    | SVD of small matrix; rank-k approx            | top-k singular vectors meaning     | —                                          |
| 12  | §6               | `Singular Value Decomposition and Eigenfaces.md` + `Matrix_Operations_Reference.md`                                     |   11   | PCA = de-mean + SVD; project to k dims        | PC = variance direction            | **Joint distributions, covariance matrix** |
| 13  | §4               | `Clustering.md`                                                                                                         |   2    | k-means assign→update loop                    | why it converges                   | —                                          |
| 14  | §4               | `Clustering, K-n.md`                                                                                                    | 2, 13  | k-NN classifier; cosine NN                    | parametric vs non-parametric       | —                                          |
Reference on demand: `Matrix_Operations_Reference.md`, `Extra notes/` (`Matrix Tools.md`, `Vector Class.md`, `Jacobi Method.md`, `Complexity.md`). Do not assign a full reread of any `Week - *.md`.
### Explicitly deferred — Endgame (late summer, deep pass not skim)
`Concepts_old/Graphs_and_PageRank.md`, `Concepts_old/The Google PageRank Algorithm.md`, the graph/PageRank subsections inside units 4 and 6, [[ML_Foundations]] §7. **Endgame standard when reached:** implement PageRank power iteration from scratch, adjacency-matrix + random-walk drills, the column-stochastic Google matrix $G=\alpha S+\frac{1-\alpha}{n}J$, then link forward to GNN / Node2Vec. Not attempted this month — locked until units 1–14 have had their broad pass and a future class actually needs the depth.
## 4. 2033 ↔ 2230 bridge table
| 2033 / ML unit | MATH 2230 topic (course week) | Combined study action |
|----------------|-------------------------------|------------------------|
| U1–2 Vectors, norms, distance | Descriptive stats, expectation (Ch 1–3, Wk 1–3) | Compute mean/variance as vector operations |
| U10 Gradient descent / loss | Discrete RVs, expectation & variance (Ch 3, Wk 2–3) | Frame loss as an expectation; bias-variance |
| U9 Classification thresholds | Continuous RVs, distributions, Bayes (Ch 4, Wk 3–4) | Gaussian/Bernoulli as label-noise models |
| U11–12 SVD / PCA | Joint distributions, covariance (Ch 5–6, Wk 4–5) | Covariance matrix → principal components |
| U7 Least squares / regression | Estimation, MLE (Ch 7–8, Wk 5–6) | Show MLE under Gaussian noise = least squares |
| (evaluation) | Hypothesis testing, CIs (Ch 9, Wk 7) | Significance of a metric gap between models |
| U7–8 Regression | Linear regression (Ch 12, Wk 7) | 2230 confirms the regression you built in LA |
| U12 PCA / variance | ANOVA / variance decomposition (Ch 14, Wk 8) | Variance explained per component |
## 5. MATH 2230 ML concept notes — the active backlog
**8 notes owed, 0 written.** Path: `20_Progress/Degree/MATH 2230/Concepts/` (co-located with the course board). Each note, four parts: definition · ML use · link to the 2033 spine unit · one worked example. Write these from what you already learned in the completed live course, cross-linked to the matching row in §4 — this is the one active task this file still owes, now that the course itself is done.
## 6. Vault hygiene
Primary read: `Concepts_old/` (human-refined, the study spine above). `Concepts_new/` (`Week_1_and_2.md` … `Week_11_to_13.md`) is supplemental only — do not assign reading all `Week - *.md`. Any concept-note merge/refine follows `.claude/skills/organize-csci2033.md` (never delete, weekly files append-only) and stays out of scope this month; the one optional pilot merge is a backlog item, not active work.
## 7. Corrected timeline (see [[Final Month Plan (Jul 28 - Sep 1)]])
1. **Broad pass, units 1–14** — one or two sessions per week, core idea + formula + one example, no forced derivation, folded into the daily floor's System Design / AI Knowledge time.
2. **MATH 2230 bridge notes, all 8** (§5) — the real backlog item.
3. **Endgame (PageRank / graph ML)** stays deferred.
## 8. Progress Tracking
### Spine units (Track A — 2033 ML)
| # | Unit | Mastery 0/1 | Date done | Output link |
|---|------|:---:|:---:|---|
| 1 | Data as vectors / linear functions | 0 | | |
| 2 | Norms, distance, std dev, angles | 0 | | |
| 3 | Linear independence, bases, orthonormality | 0 | | |
| 4 | Matrix class & geometric transforms (LA core) | 0 | | |
| 5 | Linear systems, inverses, pseudo-inverse | 0 | | |
| 6 | QR factorization & Householder | 0 | | |
| 7 | Regression → least squares | 0 | | |
| 8 | Feature engineering & overfitting | 0 | | |
| 9 | Least squares classification | 0 | | |
| 10 | Optimization & gradient descent | 0 | | |
| 11 | SVD & eigenfaces | 0 | | |
| 12 | PCA (SVD ↔ covariance) | 0 | | |
| 13 | Clustering (k-means) | 0 | | |
| 14 | k-NN (non-parametric) | 0 | | |
### Endgame queue (locked until §7's broad pass is done)
- [ ] `Graphs_and_PageRank.md`
- [ ] `The Google PageRank Algorithm.md`
- [ ] [[ML_Foundations]] §7 (PageRank → Graph ML)
- [ ] Implement PageRank power iteration from scratch + adjacency/random-walk drills
- [ ] Forward link to GNN / Node2Vec study
### Track B — MATH 2230 ML bridge notes (§5's 8, none written yet)
| Course week | 2230 topic | Bridge note created | Linked 2033 unit |
|---|---|:---:|---|
| Wk 1 (6/1–6/7) | Intro, descriptive stats (Ch 1–2) | | U1–2 |
| Wk 2 (6/8–6/14) | Discrete RVs, expectation (Ch 2.3–3.3) | | U10 |
| Wk 3 (6/15–6/21) | Continuous RVs, distributions (Ch 3.4–4) | | U9 |
| Wk 4 (6/22–6/28) | Joint dists, covariance (Ch 5–6) | | U11–12 |
| Wk 5 (6/29–7/5) | Estimation, MLE (Ch 7–8) | | U7 |
| Wk 6 (7/6–7/12) | (Ch 8, 10.1) | | — |
| Wk 7 (7/13–7/19) | Hypothesis testing, regression (Ch 9, 12) | | U7–8 |
| Wk 8 (7/20–7/24) | ANOVA / variance (Ch 14) | | U12 |
### Backlog
- [ ] Optional pilot: merge one `Concepts_new/` week into its `Concepts_old/` counterpart per `.claude/skills/organize-csci2033.md` (append-only, never delete). Not this month.
