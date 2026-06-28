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

## Q1 — f(x) = 0.05x + 0.3, 3 ≤ x ≤ 5

**(a) Graph:** f(3) = 0.45, f(5) = 0.55 — line goes up left to right. **4th graph** (begins at (3, 0.45), ends at (5, 0.55)).

**Verify area:**
∫₃⁵ (0.05x + 0.3) dx = [0.025x² + 0.3x]₃⁵ = 2.125 − **1.125** = **1** ✓

**(b)** P(X ≤ 4) = ∫₃⁴ (0.05x + 0.3) dx = [0.025x² + 0.3x]₃⁴ = 1.6 − 1.125 = **0.475**
P(X ≤ 4) **= P(X < 4)** (continuous distribution, point mass = 0)

**(c)**
P(3.5 ≤ X ≤ 4.5) = [0.025x² + 0.3x]₃.₅⁴·⁵ = 1.85625 − 1.35625 = **0.5000**
P(4.5 < X) = 2.125 − 1.85625 = **0.2688**

---

## Q2 — Uniform A = −6, B = 6; f(x) = 1/12

**(a)** P(X < 0) = 6/12 = **0.50**
**(b)** P(−3 < X < 3) = 6/12 = **0.50**
**(c)** P(−3 ≤ X ≤ 5) = 8/12 = **0.67**
**(d)** P(k < X < k+4) = 4/12 = **0.33**

---

## Q3 — Tutorial: Uniform A = −9, B = 9; f(x) = 1/18 (0 pts)

**(a)** P(X < 0) = **0.5**
**(b)** P(−4.5 < X < 4.5) = 9/18 = **0.5**
**(c)** P(−6 ≤ X ≤ 8) = 14/18 = **0.78**
**(d)** P(k < X < k+4) = 4/18 = **0.22**

---

## Q4 — f(x) = kx², 0 ≤ x ≤ 2

**(a) k:** ∫₀² kx² dx = k(8/3) = 1 → k = **0.375**
Graph: curve from (0,0) to (2, 1.5) becoming steeper — **2nd graph**.

**(b)** P(X ≤ 1) = (1/8)(1³) = **0.125**

**(c)** P(0.5 ≤ X ≤ 1.75): (1/8)[x³]₀.₅¹·⁷⁵ = (1/8)(5.359375 − 0.125) = **0.6543**

**(d)** P(X ≥ 1.75): (1/8)[8 − 5.359375] = **0.3301**

---

## Q5 — Uniform A = 0.20, B = 4.25

**(a)** f(x) = 1/(4.05) = **0.247** for 0.20 < x < 4.25, **0** otherwise. **1st graph**.

**(b)** P(X > 2) = (4.25 − 2)/4.05 = 2.25/4.05 = **0.556**

**(c)** Mean = 2.225; P(|X − 2.225| ≤ 2) = P(0.225 ≤ X ≤ 4.225) = 4.000/4.05 = **0.988**

**(d)** P(a < X < a+3) = 3/4.05 = **0.741**

---

## Q6 — f(x) = 0.55e^{−0.55(x−1)}, x ≥ 1

**(a)**
P(X ≤ 7) = 1 − e^{−3.3} = 1 − 0.03688 = **0.963**
P(X > 7) = e^{−3.3} = **0.037**

**(b)** P(3 ≤ X ≤ 7) = e^{−1.1} − e^{−3.3} = 0.33287 − 0.03688 = **0.296**
# Section 4.2

## Q1 — F(x) = x²/16 for 0 ≤ x < 4

**(a)** P(X ≤ 3) = 9/16 = **0.5625**

**(b)** P(2.5 ≤ X ≤ 3) = F(3) − F(2.5) = 9/16 − 6.25/16 = 2.75/16 = **0.1719**

**(c)** P(X > 3.5) = 1 − F(3.5) = 1 − 12.25/16 = **0.2344**

**(d)** Median: x²/16 = 0.5 → x² = 8 → x = 2√2 = **2.8284**

**(e)** f(x) = x/8 for 0 ≤ x < 4, 0 otherwise.

**(f)** E(X) = ∫₀⁴ x²/8 dx = [x³/24]₀⁴ = 64/24 = **8/3 ≈ 2.6667**

**(g)** E(X²) = ∫₀⁴ x³/8 dx = 256/32 = 8
V(X) = 8 − (8/3)² = 8 − 64/9 = **8/9 ≈ 0.8889**
σ_X = √(8/9) = 2√2/3 ≈ **0.9428**

**(h)** E[X²] = **8**

---

## Q2 — Tutorial: F(x) = x²/49 (0 pts)

**(a)** P(X ≤ 5) = 25/49 = **0.5102**
**(b)** P(4.5 ≤ X ≤ 5) = 25/49 − 20.25/49 = **0.0969**
**(c)** P(X > 5.5) = 1 − 30.25/49 = **0.3827**
**(d)** Median: x²/49 = 0.5 → x = 7/√2 = **4.9497**
**(e)** f(x) = 2x/49 = x/24.5 for 0 ≤ x < 7
**(f)** E(X) = ∫₀⁷ 2x²/49 dx = [2x³/147]₀⁷ = 686/147 = **14/3 ≈ 4.6667**
**(g)** E(X²) = 49/2; V(X) = 49/2 − 196/9 = **49/18 ≈ 2.7222**; σ_X ≈ **1.6499**
**(h)** E[X²] = ∫₀⁷ 2x³/49 dx = [x⁴/98]₀⁷ = 2401/98 = **24.5**

---

## Q3 — F(x) = 1/2 + (3/56)(6x − x³/3) for −2 ≤ x < 2

**(a)** P(X < 0) = F(0) = 1/2 = **0.5**

**(b)** P(−1 < X < 1) = F(1) − F(−1) = 45/56 − 11/56 = 34/56 = **0.6071**

**(c)** F(1.2) = 0.5 + (3/56)(7.2 − 0.576) = 0.5 + 0.3549 = 0.8549
P(1.2 < X) = 1 − 0.8549 = **0.1451**

**(d)** f(x) = (3/56)(6 − x²) for −2 ≤ x < 2, 0 otherwise.

**(e)** Median: F(μ̃) = 0.5 → (3/56)(6μ̃ − μ̃³/3) = 0 → μ̃ = **0**

---

## Q4 — Time headway: f(x) = k/x⁶, x > 1 (0 pts)

**(a)** ∫₁^∞ k/x⁶ dx = k/5 = 1 → **k = 5**

**(b)** F(x) = 1 − 1/x⁵ for x > 1, **0** for x ≤ 1

**(c)** P(X > 2) = 1/32 = **0.0313**
P(2 < X < 3) = 1/32 − 1/243 = **0.0271**

**(d)** E(X) = 5∫₁^∞ x⁻⁵ dx = 5/4 = **1.25**
V(X) = 5/3 − 25/16 = 5/48; σ = √(5/48) = **0.323**

**(e)** P(|X − 1.25| ≤ 0.323):
Lower bound = 1.25 − 0.323 = 0.927 < 1, so use 1.
Upper = 1.25 + 0.323 = 1.573
P = 1 − 1/(1.573)⁵ = 1 − 0.1039 = **0.896**

---

## Q5 — f(x) = 42x⁵(1−x), 0 < x < 1

**(a) PDF Graph:** peaks at x = 5/6 ≈ 0.833, f(0.833) ≈ 2.81 — **4th PDF graph**.

**CDF:** F(x) = 7x⁶ − 6x⁷ for 0 ≤ x ≤ 1 — **4th CDF graph** (passes through (0.83, 0.67)).

**(b)** F(0.7) = 7(0.7)⁶ − 6(0.7)⁷ = 7(0.117649) − 6(0.082354) = 0.823543 − 0.494126 = **0.3294**

**(c)** F(0.45) = 7(0.45)⁶ − 6(0.45)⁷ = 0.058126 − 0.022420 = 0.035706
P(0.45 < X ≤ 0.7) = 0.3294 − 0.0357 = **0.2937**
P(0.45 ≤ X ≤ 0.7) = **0.2937** (continuous)

**(d) 75th percentile:** Solve 7x⁶ − 6x⁷ = 0.75 numerically:
F(0.862) ≈ 0.7499 → x ≈ **0.8620**

**(e)** E(X) = 42∫₀¹(x⁶ − x⁷) dx = 42(1/7 − 1/8) = 42/56 = **3/4 = 0.7500**
E(X²) = 42(1/8 − 1/9) = 42/72 = 7/12
V(X) = 7/12 − 9/16 = 1/48; σ_X = 1/√48 = **0.1443**

**(f)** P(|X − 0.75| > 0.1443):
μ − σ = 0.6057, μ + σ = 0.8943
F(0.6057) ≈ 0.1661, F(0.8943) ≈ 0.8366
P = 0.1661 + (1 − 0.8366) = **0.3296**

---

## Q6 — Hard limiter: X ~ U(−1, 1), Y = clipped at ±0.5

**(a)** P(Y = 0.5) = P(X > 0.5) = 0.5/2 = **0.25**

**(b)** F_Y(y):
- 0 for y < −0.5
- **(y + 0.5)/2 + 0.25 = 0.5 + y/2** for −0.5 ≤ y < 0.5 → i.e., F(y) = 0.5 + y/2
- 1 for y ≥ 0.5

**4th graph**: jumps from 0 to 0.25 at y = −0.5, linear to 0.75 at y = 0.5, jumps to 1.

---

## Q7 — Circular region R, f(r) = (3/4)[1−(7−r)²], 6 ≤ r ≤ 8

E[πR²] = π · E[R²]

Let u = r − 7:
E[R²] = (3/4)∫₋₁¹(u+7)²(1−u²) du = (3/4)∫₋₁¹(−u⁴ − 48u² + 49) du [odd terms = 0]
= (3/4) × 2[−1/5 − 16 + 49] = (3/4)(2)(32.8) = (3/4)(65.6) = 49.2

E[Area] = 49.2π = **154.57 m²**

---

## Q8 — Temperature: μ = 135°C, σ = 4°C → °F = 1.8°C + 32

Mean °F = 1.8(135) + 32 = **275°F**
SD °F = 1.8(4) = **7.2°F**

---

# Section 4.3

## Q1 — Standard Normal Probabilities (4.3.028)

Let Z ~ N(0,1):

**(a)** P(0 ≤ Z ≤ 2.21) = Φ(2.21) − 0.5 = **0.4864**

**(b)** P(0 ≤ Z ≤ 2) = Φ(2) − 0.5 = **0.4772**

**(c)** P(−2.70 ≤ Z ≤ 0) = 0.5 − Φ(−2.70) = **0.4965**

**(d)** P(−2.70 ≤ Z ≤ 2.70) = 2Φ(2.70) − 1 = **0.9931**

**(e)** P(Z ≤ 1.26) = Φ(1.26) = **0.8962**

**(f)** P(−1.45 ≤ Z) = Φ(1.45) = **0.9265**

**(g)** P(−1.70 ≤ Z ≤ 2.00) = Φ(2.00) − Φ(−1.70) = **0.9327**

**(h)** P(1.26 ≤ Z ≤ 2.50) = Φ(2.50) − Φ(1.26) = **0.0976**

**(i)** P(1.70 ≤ Z) = 1 − Φ(1.70) = **0.0446**

**(j)** P(|Z| ≤ 2.50) = 2Φ(2.50) − 1 = **0.9876**

---

## Q2 — Find constant c (4.3.029)

**(a)** Φ(c) = 0.9854 → **c = 2.18**

**(b)** P(0 ≤ Z ≤ c) = 0.2939 → Φ(c) = 0.7939 → **c = 0.82**

**(c)** P(c ≤ Z) = 0.1335 → Φ(c) = 0.8665 → **c = 1.11**

**(d)** P(−c ≤ Z ≤ c) = 0.6528 → Φ(c) = 0.8264 → **c = 0.94**

**(e)** P(c ≤ |Z|) = 0.0128 → 1−Φ(c) = 0.0064 → Φ(c) = 0.9936 → **c = 2.49**

---

## Q3 — Standard Normal Percentiles (4.3.030)

**(a)** 81st: **0.88**

**(b)** 19th: **−0.88**

**(c)** 76th: **0.71**

**(d)** 24th: **−0.71**

**(e)** 16th: **−0.99**

---

## Q4 — z_α values (4.3.031)

z_α = Φ⁻¹(1−α):

**(a)** α = 0.0067 → **z = 2.47**

**(b)** α = 0.15 → **z = 1.04**

**(c)** α = 0.698 → **z = −0.52**

---

## Q5 — Moped speeds: μ = 46.7 km/h, σ = 1.75 km/h (4.3.033)

**(a)** P(X ≤ 50) = Φ((50−46.7)/1.75) = Φ(1.886) = **0.9703**

**(b)** P(X ≥ 48) = 1 − Φ((48−46.7)/1.75) = 1 − Φ(0.743) = **0.2288**

**(c)** P(|X − μ| ≤ 1.5σ) = P(|Z| ≤ 1.5) = 2Φ(1.5) − 1 = **0.8664**

---

## Q6 — Blood chloride: μ = 109, σ = 5 (4.3.037)

**(a)**
- P(X = 110) = **0** (continuous distribution)
- P(X < 110) = Φ((110−109)/5) = Φ(0.20) = **0.5793**
- P(X ≤ 110) = **0.5793**

**(b)** P(|X − 109| > 5) = P(|Z| > 1) = 2(1−Φ(1)) = **0.3173**
**No**, this probability does **not** depend on μ and σ — it depends only on the number of standard deviations (1 SD here), and will always equal 0.3173.

**(c)** Most extreme 0.8% → each tail = 0.4%:
- Lower: 109 + 5·Φ⁻¹(0.004) = **95.74** mmol/L
- Upper: 109 + 5·Φ⁻¹(0.996) = **122.26** mmol/L

---

## Q7 — A36 steel yield strength: μ = 45, σ = 5.5 ksi (4.3.040)

**(a)**
- P(X ≤ 38) = Φ((38−45)/5.5) = Φ(−1.273) = **0.1016**
- P(X > 65) = 1 − Φ((65−45)/5.5) = 1 − Φ(3.636) = **0.0001**

**(b)** "Strongest 75%" cutoff = 25th percentile = 45 + 5.5·Φ⁻¹(0.25) = **41.290 ksi**

---

## Q8 — Vehicle speed on bridge (4.3.043)

Given: P(X < 39.18) = 0.05, P(X > 73.22) = 0.10

Setting up the system:
- (39.18 − μ)/σ = −1.6449
- (73.22 − μ)/σ = 1.2816

**(a)** σ = (73.22 − 39.18)/(1.2816 + 1.6449) = **11.632 m/h**; μ = 39.18 + 1.6449(11.632) = **58.313 m/h**

**(b)** P(50 ≤ X ≤ 65) = Φ((65−58.313)/11.632) − Φ((50−58.313)/11.632) = **0.4799**

**(c)** P(X > 70) = 1 − Φ((70−58.313)/11.632) = **0.1575**

---

## Q9 — Parcel weights: μ = 13 lb, σ = 3.7 lb (4.3.047)

99% of parcels weigh at most c − 1 lb → P(X ≤ c − 1) = 0.99

c − 1 = 13 + 3.7·Φ⁻¹(0.99) = 13 + 3.7(2.3263) = 21.6075

**c = 22.6075 lb**

---

## Q10 — Binomial n = 25, Normal Approximation (4.3.053)

Parameters: p = 0.5 → μ=12.5, σ=2.5; p = 0.6 → μ=15, σ=2.4495; p = 0.8 → μ=20, σ=2

**(a) P(15 ≤ X ≤ 20)** — Normal approx: P(14.5 ≤ Normal ≤ 20.5)

| p | Exact | Normal Approx |
|---|-------|---------------|
| 0.5 | 0.2117 | 0.2112 |
| 0.6 | 0.5763 | 0.5685 |
| 0.8 | 0.5738 | 0.5957 |

- p=0.5: approx **less than** exact
- p=0.6: approx **less than** exact
- p=0.8: approx **greater than** exact

**(b) P(X ≤ 15)** — Normal approx: P(Normal ≤ 15.5)

| p | Exact | Normal Approx |
|---|-------|---------------|
| 0.5 | 0.8852 | 0.8849 |
| 0.6 | 0.5754 | 0.5809 |
| 0.8 | 0.0173 | 0.0122 |

- p=0.5: approx **less than** exact
- p=0.6: approx **greater than** exact
- p=0.8: approx **less than** exact

**(c) P(20 ≤ X)** — Normal approx: P(19.5 ≤ Normal)

| p | Exact | Normal Approx |
|---|-------|---------------|
| 0.5 | 0.0020 | 0.0026 |
| 0.6 | 0.0294 | 0.0331 |
| 0.8 | 0.6167 | 0.5987 |

- p=0.5: approx **greater than** exact
- p=0.6: approx **greater than** exact
- p=0.8: approx **less than** exact

---

## Q11 — Steel shafts: n = 200, p = 0.13 (4.3.054)

μ = 26, σ = √(200·0.13·0.87) = 4.7560

**(a)** P(X ≤ 30) ≈ P(Normal ≤ 30.5) = Φ((30.5−26)/4.7560) = Φ(0.946) = **0.8280**

**(b)** P(X < 30) = P(X ≤ 29) ≈ P(Normal ≤ 29.5) = Φ((29.5−26)/4.7560) = Φ(0.736) = **0.7691**

**(c)** P(15 ≤ X ≤ 25) ≈ P(14.5 ≤ Normal ≤ 25.5) = Φ(−0.105) − Φ(−2.415) = **0.4503**

---

# Section 4.4

## Q1 — Exponential λ = 1 (4.4.059)

**(a)** E[X] = 1/λ = **1**

**(b)** SD(X) = 1/λ = **1**

**(c)** P(X ≤ 1) = 1 − e⁻¹ = **0.632**

**(d)** P(3 ≤ X ≤ 5) = e⁻³ − e⁻⁵ = 0.0498 − 0.0067 = **0.043**

---

## Q2 — Exponential mean = 2.675 hours (4.4.061)

λ = 1/2.675; for exponential, μ = σ = 2.675

**(a)**
- P(X ≥ 2) = e^(−2/2.675) = **0.4735**
- P(X ≤ 3) = 1 − e^(−3/2.675) = **0.6742**
- P(2 ≤ X ≤ 3) = e^(−2/2.675) − e^(−3/2.675) = **0.1477**

**(b)**
- P(X > μ + 3σ) = P(X > 4·2.675) = e^(−4) = **0.0183**
- P(X < μ − σ) = P(X < 0) = **0** (exponential has μ = σ, so μ − σ = 0)

---

## Q3 — Tutorial exercise (4.4.061.MI.SA)

*(0 points — skipped)*

---

## Q4 — Gamma: mean = 37.5 ms, SD = 21.6 ms (4.4.065)

Using mean = αβ and SD = β√α:

**(a)** α = (mean/SD)² = (37.5/21.6)² = **α = 3.0141**; β = mean/α = 37.5/3.0141 = **β = 12.4416**

**(b)** P(X > 51) = 1 − F_Gamma(51; 3.0141, 12.4416) = **0.226**

**(c)** P(51 < X < 78) = F(78) − F(51) = **0.175**

---

## Q5 — Gamma: mean = 28 weeks, SD = 14 weeks (4.4.067)

α = (28/14)² = **4**, β = 28/4 = **7** → X ~ Gamma(4, 7)

**(a)** P(14 ≤ X ≤ 28) = F(28) − F(14) = **0.424**

**(b)** P(X ≤ 28) = **0.567** > 0.5, so the **median is less than 28**. Since more than 50% of the probability mass lies below 28, the median (CDF = 0.5) must be to the left of 28. ✓

**(c)** 99th percentile of Gamma(4,7) = **70 weeks**

**(d)** t such that P(X > t) = 0.005 → 99.5th percentile = **77 weeks**

# Section 4.6

## Q1 — Normal Probability Plot, n = 30 (tension readings, 4.6.087)

The plot has 30 points forming a pattern from (−2, 195) to (2, 330); the points are close to the line.

**Answer:** The given probability plot is quite linear, so it is plausible that the tension distribution is normal.

---

## Q2 — Clubhead Velocity Normal Probability Plot, n = 15 (4.6.088.MI.S)

Data sorted ascending paired with given z-percentiles:
(−1.83, 68.9) → (1.83, 92.9) — 15 points.

**(a) Plot:** Third graph — pattern starts at (−1.83, 68.9), goes up and right approximately linearly, ends at (1.83, 92.9).

**(b) Plausibility:** The plot is quite linear. This indicates a normal distribution might be a **good fit** to the population distribution of clubhead velocities for female golfers.

---

## Q3 — Weibull Probability Plot, n = 18 (fracture toughness, 4.6.090.MI)

For Weibull plot: x-axis = ln(−ln(1 − pᵢ)), y-axis = observation.

pᵢ = (i − 0.5)/18 → p₁ = 0.0278, p₁₈ = 0.9722
ln(−ln(1 − 0.0278)) ≈ −3.57;  ln(−ln(1 − 0.9722)) ≈ 1.28

**(a) Plot:** First graph — pattern starts at (≈−3.57, 0.47), goes up and right, ends at (≈1.28, 1.05).

**(b) Comment:** The plot is quite linear. This indicates a Weibull distribution might be a **good fit** to the population distribution of fracture toughness in concrete specimens.

---

## Q4 — Bearing Load Life (million revs), n = 20 (4.6.092.S)

Data: 48, 68.1, 68.1, 90.8, 103.6, 106, 115, 126, 146.6, 229, 240, 240, 278, 278, 289, 289, 370, 385.9, 392, 508

pᵢ = (i − 0.5)/20 → z₁ = Φ⁻¹(0.025) = −1.96, z₂₀ = 1.96

**(a) Normal Probability Plot:**
First graph — pattern goes up and right from (−1.96, 48) to (1.96, 508); points scattered moderately from the line.

Is normality plausible? **No.** The data is right-skewed (large upper-tail values); the plot shows curvature rather than linearity.

**(b) Weibull Probability Plot:**
x-axis = ln(−ln(1 − pᵢ)), y-axis = ln(Load Life).

ln(−ln(1 − 0.025)) ≈ −3.68;  ln(−ln(1 − 0.975)) ≈ 1.31
ln(48) ≈ 3.86;  ln(508) ≈ 6.23

First graph — pattern goes up and right from (−3.68, 3.86) to (1.31, 6.23); points scattered moderately from the line.

Is the Weibull distribution family plausible? **Yes.** The Weibull plot is more linear than the normal plot, consistent with bearing life data following a Weibull distribution.

# Section 5.3

## Q1 — Traffic Lights, X₁,X₂ iid, p(0)=0.4, p(1)=0.2, p(2)=0.4; μ=1, σ²=0.8 (5.3.038.MI)

**(a) PMF of T₀ = X₁ + X₂:**

| t₀ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| p(t₀) | 0.16 | 0.16 | 0.36 | 0.16 | 0.16 |

Derivation: P(0)=(0.4)²=0.16; P(1)=2(0.4)(0.2)=0.16; P(2)=(0.4)²+(0.2)²+(0.4)²=0.36; P(3)=2(0.2)(0.4)=0.16; P(4)=(0.4)²=0.16

**(b)** μ_T₀ = 0(0.16)+1(0.16)+2(0.36)+3(0.16)+4(0.16) = **2** = **2** · μ

**(c)** E[T₀²] = 0+0.16+1.44+1.44+2.56 = 5.60 → σ²_T₀ = 5.60−4 = **1.6** = **2** · σ²

**(d)** With n=4: E[T₀] = 4(1) = **4**; V(T₀) = 4(0.8) = **3.2**

**(e)** T₀ = X₁+X₂+X₃+X₄, max=8, each Xᵢ∈{0,1,2}:
- P(T₀=8) = (0.4)⁴ = **0.0256**
- P(T₀=7) = C(4,1)(0.2)(0.4)³ = 4(0.2)(0.064) = 0.0512
- P(T₀≥7) = 0.0512+0.0256 = **0.0768**

---

## Q2 — Tutorial (0 pts) — skip

---

## Q3 — Packages, p(1)=0.1, p(2)=0.4, p(3)=0.3, p(4)=0.2 (5.3.041)

**(a) PMF of X̄ for n=2:**

| x̄ | 1 | 1.5 | 2 | 2.5 | 3 | 3.5 | 4 |
|---|---|---|---|---|---|---|---|
| P(x̄) | 0.01 | 0.08 | 0.22 | 0.28 | 0.25 | 0.12 | 0.04 |

Key probabilities: P(1)=(0.1)²=0.01; P(1.5)=2(0.1)(0.4)=0.08; P(2)=2(0.1)(0.3)+(0.4)²=0.22; P(2.5)=2(0.1)(0.2)+2(0.4)(0.3)=0.28; P(3)=2(0.4)(0.2)+(0.3)²=0.25; P(3.5)=2(0.3)(0.2)=0.12; P(4)=(0.2)²=0.04

**(b)** P(X̄ ≤ 2.5) = 0.01+0.08+0.22+0.28 = **0.59**

**(c) Distribution of R = sample range, n=2:**

| R | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P(R) | 0.30 | 0.44 | 0.22 | 0.04 |

R=0: (1,1)+(2,2)+(3,3)+(4,4) = 0.01+0.16+0.09+0.04 = 0.30
R=1: 2[(0.1)(0.4)+(0.4)(0.3)+(0.3)(0.2)] = 2(0.22) = 0.44
R=2: 2[(0.1)(0.3)+(0.4)(0.2)] = 2(0.11) = 0.22
R=3: 2(0.1)(0.2) = 0.04

**(d) P(X̄ ≤ 1.5) for n=4:**

Sum ≤ 6 (since X̄≤1.5 → ΣXᵢ≤6, min=4):
- Sum=4: (1,1,1,1) → (0.1)⁴ = 0.0001
- Sum=5: C(4,1)(0.1)³(0.4) = 0.0016
- Sum=6: C(4,2)(0.1)²(0.4)² + C(4,1)(0.1)³(0.3) = 0.0096+0.0012 = 0.0108

P(X̄ ≤ 1.5) = 0.0001+0.0016+0.0108 = **0.0125**

---

## Q4 — Salary Sampling Distribution (5.3.042)

Employees: 1→26.7, 2→30.6, 3→27.2, 4→30.6, 5→22.8, 6→26.7 (k$)
Population μ = 164.6/6 = 27.433̄

**(a) Sampling distribution of X̄, n=2 without replacement (C(6,2)=15 equally likely pairs):**

| x̄ | 24.75 | 25.00 | 26.70 | 26.95 | 28.65 | 28.90 | 30.60 |
|---|---|---|---|---|---|---|---|
| p(x̄) | 2/15 | 1/15 | 3/15 | 2/15 | 4/15 | 2/15 | 1/15 |

Pairs → means: (1,5)&(5,6)→24.75; (3,5)→25.00; (1,6)&(2,5)&(4,5)→26.70; (1,3)&(3,6)→26.95; (1,2)&(1,4)&(2,6)&(4,6)→28.65; (2,3)&(3,4)→28.90; (2,4)→30.60

**(b) One office selected (prob 1/3 each); X̄ = average of the two employees:**

Office 1: (26.7+30.6)/2=28.65; Office 2: (27.2+30.6)/2=28.90; Office 3: (22.8+26.7)/2=24.75

| x̄ | 24.75 | 28.65 | 28.90 |
|---|---|---|---|
| p(x̄) | 1/3 | 1/3 | 1/3 |

**(c)** E(X̄) from (a) = 411.50/15 = 27.433̄ = **equal to** μ; E(X̄) from (b) = 82.30/3 = 27.433̄ = **equal to** μ.

---

# Section 5.4

## Q1 — Young's Modulus, μ=70, σ=1.6 GPa (5.4.046)

**(a) n=16:** E(X̄) = **70 GPa**; σ_X̄ = 1.6/√16 = **0.4 GPa**

**(b) n=256:** E(X̄) = **70 GPa**; σ_X̄ = 1.6/√256 = **0.1 GPa**

**(c)** X is more likely to be within 1 GPa of the mean in **part (b)**. This is due to the **decreased variability** of X̄ that comes with a larger sample size.

---

## Q2 — Waist Circumference, n=277, x̄=86.3 cm (5.4.048.S)

Percentiles given: 5th=69.6, 25th=75.2, 50th=81.3, 75th=95.4, 95th=116.4

**(a) Normality:** Mean(86.3) >> Median(81.3); upper spread: 95.4−81.3=14.1 vs lower: 81.3−75.2=6.1.

Since the mean and median are substantially different, and the difference in the distance between the median and the upper quartile and the distance between the median and the lower quartile is relatively large, it **does not seem plausible** that waist size is at least approximately normal.

Shape conjecture: The upper percentiles stretch much farther than the lower percentiles. Therefore, we might suspect a **right-skewed distribution**.

**(b) μ=85, σ=15:** σ_X̄ = 15/√277 = 0.9012; Z = (86.3−85)/0.9012 = 1.4424
P(X̄ ≥ 86.3) = 1 − Φ(1.4424) = **0.0746**

**(c) μ=81:** Z = (86.3−81)/0.9012 = 5.881 → P(X̄ ≥ 86.3) ≈ **0.0000**

No, 81 cm is **not** a reasonable value for μ since if the population mean waist size is 81 cm, there would be almost no chance of observing a sample mean waist size of 86.3 cm (or higher) in a random sample of 277 men.

---

## Q3 — Grading Time, n=43, μ=5 min, σ=4 min (5.4.049.S)

T₀ = ΣXᵢ; E[T₀]=215, V[T₀]=43(16)=688, SD=√688=26.2296

**(a) P(T₀ ≤ 250)** (6:50 PM to 11:00 PM = 250 min):
Z = (250−215)/26.2296 = 1.3344 → **P ≈ 0.9090**

**(b) P(T₀ > 260)** (misses sports at 11:10 = 260 min from 6:50):
Z = (260−215)/26.2296 = 1.7157 → P(misses) = 1 − Φ(1.7157) = **0.0431**

---

## Q4 — Mortgage Form, X~N(9,4²), n₁=5 and n₂=6 (5.4.051.S)

P = P(X̄₁ ≤ 11) × P(X̄₂ ≤ 11) (independent days)

Day 1 (n=5): Z = 2/(4/√5) = √5/2 = 1.1180; Φ(1.1180) = 0.8682
Day 2 (n=6): Z = 2/(4/√6) = √6/2 = 1.2247; Φ(1.2247) = 0.8897

P = 0.8682 × 0.8897 = **0.7724**

---

## Q5 — Battery Lifetime, μ=15 hr, σ=1 hr, n=9 (5.4.052.S.MI)

T = ΣXᵢ ~ N(135, 9); SD(T)=3

P(T > t) = 0.05 → t = 135 + 3(1.645) = **139.93 hours**

---

## Q6 — Tutorial (0 pts) — skip

---

## Q7 — Sediment Density, μ=2.66, σ=0.91, n=25 (5.4.054.S)

σ_X̄ = 0.91/5 = 0.182; Z = (3.00−2.66)/0.182 = 1.8681

**(a)**
- P(X̄ ≤ 3.00) = Φ(1.8681) = **0.9691**
- P(2.66 ≤ X̄ ≤ 3.00) = Φ(1.8681) − 0.5 = **0.4691**

**(b)** Need 0.34√n/0.91 ≥ 2.3263 → √n ≥ 6.2263 → n ≥ 38.77 → **n = 39 specimens**

---

## Q8 — Binary Channel, p=0.20, n=1000 (5.4.056.S)

X ~ Bin(1000,0.20); μ=200, σ=√160=12.6491

**(a) P(X ≤ 235):**
Z = (235−200)/12.6491 = 2.7675 → **P ≈ 0.9972**

**(b) D = X₁−X₂; E[D]=0, V[D]=320, SD[D]=√320=17.8885**
P(|D| ≤ 60): Z = 60/17.8885 = 3.3541
P = 2Φ(3.354)−1 = **0.9992**

# Section 6.1

## Q1 — Flexural Strength, n=27 beams (6.1.001)

Σxᵢ = 220.6 (given), Σxᵢ² = 1870.9 (given), n=27

**(a) Mean:** x̄ = 220.6/27 = **8.170 MPa** — estimator: **x̄**

**(b) Median (50th percentile):** Sorted data, 14th value = **7.7 MPa** — estimator: **x̃**

**(c) Standard deviation:**
s² = [1870.9 − (220.6)²/27]/26 = [1870.9 − 1802.384]/26 = 68.516/26 = 2.6352
s = √2.6352 = **1.623 MPa** — estimator: **s**
Interpretation: This estimate describes the **spread** of the data.

**(d) Proportion exceeding 10 MPa:**
Values > 10: {10.7, 11.3, 11.6, 11.8} → 4 out of 27
p̂ = 4/27 = **0.148**

**(e) Coefficient of variation σ/μ:**
ĈV = s/x̄ = 1.623/8.170 = **0.1987** — estimator: **s/x̄**

---

## Q2 — HDL Cholesterol, n=20 (6.1.002.S.MI)

Data: 34,48,51,55,64,50,52,46,87,37,45,34,38,44,38,62,94,36,31,47 → Σxᵢ=993

**(a) Mean:** x̄ = 993/20 = **49.65 mg/dl**

**(b) Median:** Sorted 20 values; average of 10th and 11th = (46+47)/2 = **46.5 mg/dl**

**(c) Standard deviation:**
Σxᵢ² = 54591; s² = [54591 − 993²/20]/19 = 5288.55/19 = 278.344
s = **16.684 mg/dl**

**(d) Proportion with HDL ≥ 60:**
Values ≥ 60: {62, 64, 87, 94} → 4 out of 20
p̂ = 4/20 = **0.20**

---

## Q3 — Tutorial (0 pts) — skip

---

## Q4 — Beams vs Cylinders (6.1.004.MI)

**Beams (m=27):** Σxᵢ=219.4 → x̄=8.126; Σxᵢ²=1859.34 → s₁²=2.9426, s₁=1.715 MPa
**Cylinders (n=20):** Σyᵢ=172.9 → ȳ=8.645; Σyᵢ²=1583.01 → s₂²=4.6468, s₂=2.156 MPa

**(a) Unbiasedness:** E(X̄−Ȳ) = E(X̄)−E(Ȳ) = μ₁−μ₂ (linearity of expectation). Estimate: 8.126−8.645 = **−0.519 MPa**

**(b) V(X̄−Ȳ) = σ₁²/m + σ₂²/n** (correct step — second option).
σ_X̄−Ȳ = √(σ₁²/n₁ + σ₂²/n₂) — third option.
Estimated SE = √(2.9426/27 + 4.6468/20) = √(0.1090+0.2323) = √0.3413 = **0.584 MPa**

**(c) Point estimate of σ₁/σ₂:** s₁/s₂ = 1.715/2.156 = **0.796**

**(d) V(X−Y) for single beam and cylinder:** s₁²+s₂² = 2.9426+4.6468 = **7.59 MPa²**

---

## Q5 — Tutorial (0 pts) — skip

---

## Q6 — Defective Components, n=160, 56 defective (6.1.008)

**(a)** p̂(not defective) = 104/160 = **0.65**

**(b)** P(series system works) = p²; estimate = (0.65)² = **0.4225**

---

## Q7 — Unbiased Estimator, f(x;θ)=0.5(1+θx) (6.1.013)

E(X) = ∫₋₁¹ x·½(1+θx) dx = ½[x²/2 + θx³/3]₋₁¹ = ½[(½+θ/3)−(½−θ/3)] = θ/3

Integrand in blank: **x·½(1+θx)** dx; result = **θ/3**

Therefore: θ = **3μ** (in terms of μ), so θ̂ = 3X̄.
E(θ̂) = 3E(X̄) = 3μ = θ ✓ (unbiased)

---

## Q8 — Jet Fighter Serial Numbers (6.1.014)

**(a)** n=5: {427,262,453,381,207} → max=453, min=207
Estimate = 453−207+1 = **247 planes**

**(b)** The estimate equals the true number if and only if the smallest serial number in the population AND the largest serial number in the population both appear in the sample.

Will estimate ever be larger than true total? **No** — sample range ≤ population range.

Is estimator unbiased? **The estimate is biased. The estimate can never exceed β−α+1.** (It systematically underestimates since the sample max−min ≤ β−α.)

---

# Section 6.2

## Q1 — False Positive Diagnostic Test (6.2.020)

X ~ Bin(n,p); log L(p) = x·ln(p)+(n−x)·ln(1−p)

Setting d/dp = 0: x/p − (n−x)/(1−p) = 0 → p̂ = x/n

**(a)** MLE: **p̂ = X/n**
If n=25, x=6: p̂ = 6/25 = **0.24**

**(b)** Unbiased? E[X/n] = np/n = p → **Yes**

**(c)** MLE of (1−p)⁵ by invariance: (1−p̂)⁵ = (1−0.24)⁵ = (0.76)⁵
= 0.76² × 0.76² × 0.76 = 0.5776 × 0.5776 × 0.76 = 0.3336 × 0.76 = **0.2536**

---

## Q2 — Aptitude Test, f(x;θ)=(θ+1)xᶿ (6.2.022.MI)

Data: 0.99,0.75,0.79,0.65,0.73,0.94,0.92,0.86,0.45,0.90 → X̄=0.798

**(a) Method of Moments:**
E(X) = ∫₀¹ x(θ+1)xᶿ dx = (θ+1)/(θ+2) = X̄
Solving: θ(1−X̄) = 2X̄−1 → **θ̃ = 1/(1−X̄) − 2**

Estimate: 1/(1−0.798)−2 = 1/0.202−2 = 4.950−2 = **2.95**

**(b) MLE:**
log L = n·ln(θ+1) + θ·Σln(xᵢ); setting d/dθ=0: n/(θ+1)+Σln(xᵢ)=0
→ **θ̂ = −n/Σln(Xᵢ) − 1**

Σln(xᵢ) = ln(0.99)+ln(0.75)+ln(0.79)+ln(0.65)+ln(0.73)+ln(0.94)+ln(0.92)+ln(0.86)+ln(0.45)+ln(0.90)
= −0.0101−0.2877−0.2357−0.4308−0.3147−0.0619−0.0834−0.1508−0.7985−0.1054
= −2.4789

θ̂ = −10/(−2.4789)−1 = 4.034−1 = **3.03**

---

## Q3 — Tutorial (0 pts) — skip

---

## Q4 — Spot Welds, n=10, Normal MLE (6.2.025.S)

Data: 388,375,415,358,404,370,409,367,362,389
Σxᵢ=3837; Σxᵢ²=1,476,009

**(a) MLE (normal distribution uses σ̂²=Σ(xᵢ−x̄)²/n):**
μ̂ = 3837/10 = **383.70 psi**
σ̂² = 1476009/10 − (383.70)² = 147600.9−147225.69 = 375.21
σ̂ = √375.21 = **19.37 psi**

**(b) 95th percentile** (= μ+1.645σ by invariance):
383.70+1.645(19.37) = 383.70+31.86 = **415.56 psi**

**(c) MLE of P(X ≤ 400):**
P(X≤400) = Φ((400−μ̂)/σ̂) = Φ((400−383.70)/19.37) = Φ(0.8415)
= Φ(0.84)+0.15·[Φ(0.85)−Φ(0.84)] = 0.7995+0.15(0.0028) = **0.7999**
