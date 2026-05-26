---
type: class
status: archived
created: 2025-10-09
updated: 2025-10-11
area:
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Week - 1 & 2]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Week - 3|Week - 3]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Week - 4|Week - 4]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Week - 5]]"
tags:
  - "#class"
next: "[[Final]]"
---
[[Quiz]]
[[Vector Class]]
[[Matrix Tools]]
[[Complexity]]
# Cheat sheet
## [[Midterm]]
### Midterm Practice - 1
1. Slicing notation (most compact): Let $x_{0:n-1}​$ denote $[x_0,\dots,x_{n-2}]$ and $x_{1:n}$​ denote $[x_1,\dots,x_{n-1}]$. Then 
		$\boxed{\,d = x_{1:n} - x_{0:n-1}\,}$​ ​In code (NumPy style): `d = x[1:] - x[:-1]`.
2. 3. There are **two different ways** to define "nearest" between vectors:
	1. **Euclidean distance (L2 norm)** →  
    $∥x−y∥$: how far apart the two points are in space.  
    Measures _absolute proximity_.
	2. **Angle (cosine similarity)** →  
	    $$\cos(\theta) = \dfrac{x \cdot y}{\|x\|\|y\|}$$                how aligned the two vectors are.  
	    Measures _directional similarity_ (regardless of magnitude).
	3. For unit vectors, the **Euclidean distance** and **angle** give the same ranking of closeness.
3. 4. k-means divides users into **k groups (clusters)** whose members have similar listening patterns. Each cluster c has a **centroid**
$$\vec\mu_c = \text{mean of all } \vec p_i \text{ in cluster }$$which contains values between 0 and 1 representing how popular each song is _within that cluster_
4. 5. In **k-NN**, you look for _similar users_ directly.
- In **k-means**, you look for _similar groups of users_ and use their average behavior.

| \| Aspect                \| k-Nearest Neighbors                                           \| k-Means Clustering                                                       \|<br>\| --------------------- \| ------------------------------------------------------------- \| ------------------------------------------------------------------------ \|<br>\| **Similarity notion** \| Finds the k most similar individual users                     \| Groups all users into k clusters                                         \|<br>\| **Computation time**  \| Must recompute neighbors for every user → slower for large N  \| Pre-computes clusters once → faster for new users                        \|<br>\| **Personalization**   \| Highly individualized (based on unique neighbors)             \| More generalized (everyone in same cluster gets similar recommendations) \|<br>\| **Prediction source** \| Average of the 100 nearest users’ playlists                   \| Average (centroid) of the cluster                                        \|<br>\| **When to use**       \| When dataset smaller or you want fine-grained personalization \| When dataset large and you want scalable, grouped recommendations        \| |     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
5. **k-means group representative matrix**.
	- AAA has **k rows** and **n columns**.
	- Each row = centroid (average playlist vector) of one cluster of users.
	- So $A_{g j}​$ = fraction (or mean) of users in cluster g
### Midterm practice - 2
1. 

---

## Complexity (Chapter wise)
### Chapter - 1 & 2 
- **Vector Addition (length $n$):** $n$ flops.
- **Scalar-Vector Multiplication (length $n$):** $n$ flops.
- **Inner Product (length $n$):** $2n$ flops ($n$ multiplications and $n$ additions).
The textbook also notes that the memory storage requirement for an $n$-vector is typically $8n$ bytes.
### Chapter - 6 
In complexity analysis, operations are counted in floating point operations (flops). For an $m \times n$ matrix $A$:
- Matrix addition ($A+B$) or scalar multiplication ($\alpha A$): $mn$ flops.
- Matrix transposition ($A^T$): 0 flops (only copying time).
- Matrix-vector multiplication ($Ax$): $2mn$ flops.
- Matrix storage: $8mn$ bytes. Sparse matrix storage requires approximately $16 \text{nnz}(A)$ bytes.
---

## [[Midterm Notes(1)]]

---
## 🔹 Chapter 10 – Matrix–Matrix Products

### 1. Definition

If A is m×n times n×n and BBB is n×pn \times pn×p:

C=AB∈Rm×p,cij=∑k=1naikbkj.C = AB \in \mathbb{R}^{m \times p}, \quad c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}.C=AB∈Rm×p,cij​=k=1∑n​aik​bkj​.

### 2. Three equivalent “views”

1. **Row-by-column** (standard definition).
    
2. **Column view**: each column of CCC is AAA times the corresponding column of BBB:
    
    C=[Ab1  Ab2  ⋯  Abp].C = [A b_1 \; A b_2 \; \cdots \; A b_p].C=[Ab1​Ab2​⋯Abp​].
3. **Outer-product view**: sum of rank-1 matrices
    
    C=∑k=1nakbkT,C = \sum_{k=1}^{n} a_k b_k^T,C=k=1∑n​ak​bkT​,
    
    where aka_kak​ = kkk-th column of AAA and bkTb_k^TbkT​ = kkk-th row of BBB.
    

👉 _Quizzes often ask_:

> “Which of the following represents matrix multiplication correctly?”  
> Answer: the one where inner dimensions match and each entry is a dot product.

---

### 3. Properties

- Associative: (AB)C=A(BC)(AB)C = A(BC)(AB)C=A(BC)
    
- Distributive: A(B+C)=AB+ACA(B + C) = AB + ACA(B+C)=AB+AC
    
- _Not commutative:_ AB≠BAAB \neq BAAB=BA in general.
    
- (AB)T=BTAT(AB)^T = B^T A^T(AB)T=BTAT.
    

### 4. Computational cost

- Matrix–vector multiply: O(n2)O(n^2)O(n2)
    
- Matrix–matrix multiply: O(n3)O(n^3)O(n3) (for dense matrices)
    

---

### 5. Applications (as seen in Lab 6)

- **PageRank:** iterative process xk+1=Pxkx_{k+1} = P x_kxk+1​=Pxk​, with stochastic PPP.  
    Multiple iterations Pkx0P^k x_0Pkx0​ are effectively repeated matrix–vector multiplications.  
    In code, this often appears as:
    
    `x = P @ x`
    
    (which uses matrix–matrix product rules internally).
    

---

## 🔹 Chapter 11 – Householder QR Factorization

### 1. Purpose

To solve least squares Ax≈bAx \approx bAx≈b stably:

A=QR,QTQ=I,R upper triangular.A = QR, \quad Q^T Q = I, \quad R \text{ upper triangular}.A=QR,QTQ=I,R upper triangular.

Then x=R−1QTb.x = R^{-1} Q^T b.x=R−1QTb.

---

### 2. Householder transformation

A **Householder reflector** is:

$H=I−2vvTvTvH = I - 2\frac{vv^T}{v^T v}H=I−2vTvvvT​$

where v∈Rnv \in \mathbb{R}^nv∈Rn (nonzero vector).

- HHH is **orthogonal**: HTH=IH^T H = IHTH=I.
    
- Geometrically: reflection across the hyperplane orthogonal to vvv.
    
- Property: for any xxx, HxHxHx has the same 2-norm as xxx.
    

---

### 3. Using Householder to zero out below a pivot

Goal: for given column aaa of AAA, construct HHH such that

Ha=∥a∥e1H a = \|a\| e_1Ha=∥a∥e1​

(where e1=[1,0,…,0]Te_1 = [1, 0, \dots, 0]^Te1​=[1,0,…,0]T).

Steps (from lecture & Lab 7):

1. a=Ak:m,ka = A_{k:m, k}a=Ak:m,k​ (current column below diagonal)
    
2. Compute α=−sign(a1)∥a∥2\alpha = -\text{sign}(a_1)\|a\|_2α=−sign(a1​)∥a∥2​
    
3. Define v=a−αe1v = a - \alpha e_1v=a−αe1​
    
4. Normalize: v=v/∥v∥2v = v / \|v\|_2v=v/∥v∥2​
    
5. H=I−2vvTH = I - 2vv^TH=I−2vvT
    
6. Apply HHH to the current submatrix of AAA.
    

After finishing all columns, AAA becomes RRR, and QQQ is the product of all reflectors:

Q=H1H2⋯Hn−1.Q = H_1 H_2 \cdots H_{n-1}.Q=H1​H2​⋯Hn−1​.

---

### 4. Comparison: Gram–Schmidt vs. Householder

|Property|Classical GS|Modified GS|Householder|
|---|---|---|---|
|Stability|Poor|Better|Excellent|
|Orthogonality|Approximate|Good|Perfect (up to round-off)|
|Cost|O(2mn2)O(2mn^2)O(2mn2)|O(2mn2)O(2mn^2)O(2mn2)|O(2mn2−2n3/3)O(2mn^2 - 2n^3/3)O(2mn2−2n3/3)|

👉 _Quiz-style question:_

> “Which QR method is most numerically stable?”  
> ✅ **Answer:** Householder QR.

---

### 5. Example (2×2)

Let

A=[111−1].A = \begin{bmatrix} 1 & 1\\ 1 & -1 \end{bmatrix}.A=[11​1−1​].

Compute HHH to zero the lower element of first column:

- a=[1,1]Ta = [1,1]^Ta=[1,1]T, ∥a∥=2\|a\|=\sqrt{2}∥a∥=2​, α=−2\alpha = -\sqrt{2}α=−2​.
    
- v=a−αe1=[1+2,1]Tv = a - \alpha e_1 = [1+\sqrt{2},1]^Tv=a−αe1​=[1+2​,1]T
    
- v=v/∥v∥v=v/\|v\|v=v/∥v∥.
    
- H=I−2vvTH = I - 2vv^TH=I−2vvT.  
    Then HAHAHA yields upper triangular RRR.
    

---

### 6. Lab 7 key formulas

In your notebook, you saw:

`def householder_reflection(a):     v = a.copy()     v[0] = v[0] + np.sign(a[0])*np.linalg.norm(a)     v = v / np.linalg.norm(v)     H = np.eye(len(a)) - 2*np.outer(v,v)     return H`

and for full QR:

`for k in range(n):     Hk = np.eye(m)     Hk[k:,k:] -= 2*np.outer(v,v)     A = Hk @ A     Q = Q @ Hk.T`

---

### 7. Numerical behavior

- QQQ is orthogonal: QTQ=IQ^T Q = IQTQ=I.
    
- RRR is upper-triangular.
    
- Useful for least squares: ATAx=ATbA^T A x = A^T bATAx=ATb can be avoided (better conditioning).
    

---

### 8. Householder vs. PageRank connection

Both use **matrix iteration** ideas:

- PageRank iterates xk+1=Pxkx_{k+1}=Px_kxk+1​=Pxk​ (power iteration).
    
- QR with Householder applies successive **orthogonal transformations** HiH_iHi​ to reduce AAA.
    

---

## ✅ Common quiz-type questions (and correct answers)

|Likely question|Correct concept / answer|
|---|---|
|Which expression defines matrix–matrix product?|Cij=∑kaikbkjC_{ij} = \sum_k a_{ik}b_{kj}Cij​=∑k​aik​bkj​|
|Is AB=BAAB = BAAB=BA?|No (not commutative)|
|What is (AB)T(AB)^T(AB)T?|BTATB^T A^TBTAT|
|What’s a rank-1 update / outer product form?|AB=∑kakbkTAB = \sum_k a_k b_k^TAB=∑k​ak​bkT​|
|What does a Householder reflector do?|Reflects a vector about a plane to zero out entries below pivot|
|Formula for reflector?|H=I−2vvT/(vTv)H = I - 2vv^T/(v^Tv)H=I−2vvT/(vTv)|
|HHH is orthogonal?|Yes, HTH=IH^T H = IHTH=I|
|How is QQQ built?|Product of Householder reflectors|
|Advantage over Gram–Schmidt?|Greater numerical stability|
|What is RRR in QR?|Upper-triangular part of transformed AAA|
|QTQ=IQ^T Q = IQTQ=I?|True|
|Cost of matrix–matrix product?|O(n3)O(n^3)O(n3)|
|To find least-squares solution using QR:|x=R−1QTbx = R^{-1} Q^T bx=R−1QTb|