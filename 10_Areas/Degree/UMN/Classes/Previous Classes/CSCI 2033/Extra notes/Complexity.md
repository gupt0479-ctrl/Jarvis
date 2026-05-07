---
type: input
input_kind: book
status: sprout
created: 2025-09-25
related_progress:
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 1 & 2]]"
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 6|Week - 6]]"
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Midterm - 1]]"
tags:
  - input
---
# Complexity (Chapter wise)
## Chapter - 1 & 2 
- **Vector Addition (length $n$):** $n$ flops.
- **Scalar-Vector Multiplication (length $n$):** $n$ flops.
- **Inner Product (length $n$):** $2n$ flops ($n$ multiplications and $n$ additions).
The textbook also notes that the memory storage requirement for an $n$-vector is typically $8n$ bytes.
## Chapter - 6 
In complexity analysis, operations are counted in floating point operations (flops). For an $m \times n$ matrix $A$:
- Matrix addition ($A+B$) or scalar multiplication ($\alpha A$): $mn$ flops.
- Matrix transposition ($A^T$): 0 flops (only copying time).
- Matrix-vector multiplication ($Ax$): $2mn$ flops.
- Matrix storage: $8mn$ bytes. Sparse matrix storage requires approximately $16 \text{nnz}(A)$ bytes.
