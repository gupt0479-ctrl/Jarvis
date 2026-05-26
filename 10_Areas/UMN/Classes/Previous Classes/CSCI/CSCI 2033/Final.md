---
type: class
status: archived
created: 2025-12-11
updated: 2025-12-12
area:
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Midterm - 1|Midterm - 1]]"
  - "[[Python]]"
  - "[[CSCI 2033 Board]]"
tags:
  - "#class"
next: "[[CSCI 2033 Board]]"
---
Chapters - **6,7,8,10,11,12,13,14**
Weeks 5 end chapter - 6 onwards. Paper homework 5 included
Skim through the textbook using notebooklm and then got through everything that Joy has done(lectures, labs, paper hw, quizzes). 
Create a cheat code of material from each and every single chapter. Understand each and every lab, ow to write equations in python format. how to use numpy in the end. Research numpy a bit.
# Notes
## Chapter 7
This section provides the key formulas related to problem applications within Chapter 7.

|   |   |   |
|---|---|---|
|Concept|Formula|Citation|
|**2D Rotation (Counterclockwise)**|y=Ax, where A=[cosθsinθ​−sinθcosθ​]||
|**Incidence Matrix Entry (**n×m**)**|Aij​=⎩![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.8889em"%20height="0.316em"%20style="width:0.8889em"%20viewBox="0%200%20888.89%20316"%20preserveAspectRatio="xMinYMin"><path%20d="M384%200%20H504%20V316%20H384z%20M384%200%20H504%20V316%20H384z"></path></svg>)⎨![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.8889em"%20height="0.316em"%20style="width:0.8889em"%20viewBox="0%200%20888.89%20316"%20preserveAspectRatio="xMinYMin"><path%20d="M384%200%20H504%20V316%20H384z%20M384%200%20H504%20V316%20H384z"></path></svg>)⎧​1−10​if edge j points to node iif edge j points from node iotherwise​||
|**Flow Conservation (with Sources/Sinks** s**)**|Ax+s=0||
|**Potential Differences (for Node Potentials** v**)**|u=ATv||
|**Dirichlet Energy (Graph Roughness)**|D(v)=∣ATv∣2 (sum of squared potential differences across edges)||
|**1D Convolution (Result** c **is size** n+m−1**)**|ck​=∑i+j=k+1​ai​bj​||
|**Matrix Form of Convolution (Toeplitz Matrix** T(a)**)**|c=T(a)b||
|**Second Difference Operation (Approximate Roughness)**|Δx=Dn−1​Dn​x, where D is the difference matrix.|,|
## Chapter 8
Important Formulas and Concepts from Chapter 8

|                                  |                          |                                                                   |
| -------------------------------- | ------------------------ | ----------------------------------------------------------------- |
| Concept                          | Formula / Representation | Context                                                           |
| **Linear Function**              | f(x)=Ax                  | A is m×n. f satisfies superposition.                              |
| **Affine Function**              | f(x)=Ax+b                | b is the constant offset. Satisfies superposition only if α+β=1.  |
| **Taylor Approximation**         | f^​(x)=f(z)+Df(z)(x−z)   | Affine approximation of f near point z.                           |
| **System of Linear Equations**   | Ax=b                     | A is coefficient matrix, x are variables, b is right-hand side.   |
| **Residual Vector (Regression)** | rd=yd−XTβ−v1             | Vector of prediction errors for N data points.                    |
| **Flow Conservation**            | Af+s=0                   | A is incidence matrix, f is flow vector, s is source/sink vector. |
| **Leontief Model**               | (I−A)x=d                 | x is output level, d is demand, A is input-output matrix.         |
**Analogy:** If we think of a complex, winding river representing a **nonlinear function** f, the **Taylor approximation** is like building a short, straight canal (an affine function) perfectly aligned with the river's current where you are standing (z).
## Chapter 10
