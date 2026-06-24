---
type: class
status: archived
created: 2025-10-04
updated: 2025-10-16
area:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 2033/Week - 1 & 2]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 2033/Week - 3|Week - 3]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 2033/Week - 4|Week - 4]]"
tags:
  - "#class"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 2033/Midterm - 1]]"
---
# Quizzes Solutions
## Chapter - 2
1. Each arithmetic operation (`*`, `+`) **creates a new Vector object** using the constructor:
	- `3*e1` → calls `__rmul__`, which calls `Vector(self.data)` once → **1 constructor call**
	- `(-2)*e2` → same → **1 more constructor call**
	- `4*e3` → same → **1 more constructor call**
Now the additions:
	- `(3*e1) + (-2)*e2` → calls `__add__`, which again calls `Vector(self.data)` inside → **1 more constructor call**
	- Then you add `+ 4*e3` → another `__add__` → **1 more constructor call**
**Total constructor calls:** `3 (from scalar multiplications) + 2 (from additions) = 5 constructor calls`
**Concept**: Each arithmetic operation (`*`, `+`) creates new `Vector` objects → leading to multiple constructor calls and memory usage. This helps you understand **computational efficiency** when chaining vector operations.
2. Multiplying a vector by a scalar **scales** its magnitude (length) without changing its direction (except when α is negative, which reverses direction).
- q5. Linear combinations like av⃗+bw⃗a\vec{v} + b\vec{w}av+bw represent **combined effects** of multiple cost (or force, or velocity) components. Each coefficient acts as a scaling factor on its vector’s contribution.
## Chapter - 3
1. [[50_Archive/Previous Classes/CSCI/CSCI 2033/Week - 1 & 2#Regression Model]] - A linear regression model predicts an output variable $\hat{y}$ as a **linear combination** of input features:
- $x_1, x_2, \dots$: input features (e.g., total area, number of beds).
- $\beta_1, \beta_2, \dots$: coefficients (showing how sensitive $\hat{y}$ is to each feature).
- $v$: intercept term (baseline prediction).
Each coefficient $\beta_i$ represents **the expected change in $\hat{y}$** for a 1-unit increase in $x_i$, **holding all other variables constant**.
> The model parameter $\beta_1 = 148.73$ represents the amount the regression model price prediction $\hat{y}$ increases when the number of beds increases.
**Answer:** ❌ False
**Reasoning:** $\beta_1$ corresponds to the first feature $x_1$ — **total area**, not number of beds. Therefore, $\beta_1 = 148.73$ means that when the **area** increases by 1 unit (keeping number of beds fixed), the predicted price increases by 148.73 units.

1. Problem 3
> The model parameter $\beta_2 = -18.85$ represents the amount the regression model price prediction $\hat{y}$ decreases when the number of beds increases.
**Answer:** ✅ True
**Reasoning:** $\beta_2$ corresponds to $x_2$, the **number of beds**. Since $\beta_2$ is **negative**, it means: Increasing the number of beds (while keeping total area fixed) **reduces** the predicted sale price. So, the predicted price decreases by 18.85 units for each additional bed, assuming the house area remains the same.
## Chapter - 4 
