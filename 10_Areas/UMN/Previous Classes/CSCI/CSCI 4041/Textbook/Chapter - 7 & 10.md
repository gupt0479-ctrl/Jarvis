---
type: class
input_kind: book
status: sprout
created: 2026-02-09
updated: 2026-04-28
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Textbook/Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 4|Week - 4]]"
---
# Chapter 7 - Quicksort
## Summary Links
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 4#Chapter 7 and Chapter 10 - Quicksort, Partitioning, and Elementary Data Structures|Week - 4]]
- [[QuickSort#Definition|QuickSort]]
- [[Elementary Data Structures#Definition|Elementary Data Structures]]

**Chapter 7: Quicksort** describes one of the most practical and efficient sorting algorithms, characterized by an **expected running time of** $Θ(n \lg n)$ on an array of n numbers. Despite a **worst-case running time of** $Θ(n^2)$, its average performance is remarkable because the constant factors hidden in the $Θ(n \lg n)$ notation are small. Furthermore, it has the advantage of *sorting in place*, meaning it requires only a constant amount of additional memory beyond the input array, and it performs well in virtual-memory environments.

## 7.1 Description of Quicksort
Quicksort applies the **divide-and-conquer** method, which involves three characteristic steps for sorting a subarray $A[p:r]$:
1. *Divide:* The algorithm partitions the array $A[p:r]$ into two possibly empty subarrays, $A[p:q-1]$ and $A[q+1:r]$. It ensures that every element in $A[p:q-1]$ is **less than or equal to** $A[q]$ and every element in $A[q+1:r]$ is **greater than** $A[q]$.
2. *Conquer:* The two subarrays are sorted by recursive calls to `QUICKSORT`.
3. *Combine:* Because the subarrays are sorted in place, no work is needed to combine them.

### The Partitioning Procedure
The `PARTITION` procedure is the key to the algorithm. It selects the last element of the subarray, $x=A[r]$, as the **pivot** around which to partition the array. As it runs, it organizes the elements into **four regions**:
- *Tan Region (A[p:i]):* Elements known to be ≤ x.
- *Blue Region (A[i+1:j-1]):* Elements known to be > x.
- *White Region (A[j:r-1]):* Elements with an unknown relationship to x.
- *Yellow Region (A[r]):* The pivot element itself.

The procedure uses a *loop invariant* to maintain correctness. At the start of each iteration:
- If $p \leq k \leq i$, then $A[k] \leq x$.
- If $i+1 \leq k \leq j-1$, then $A[k] > x$.
- If $k=r$, then $A[k]=x$.

The running time of `PARTITION` on a subarray of n elements is $Θ(n)$ because it examines each element exactly once.

### Full 0-Indexed Python Partition Code
The lecture used a direct Python translation that is the cleanest version to study:

```python
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
```

### Lecture Emphasis
The lecture emphasized that the whole algorithm lives inside the partition invariant. If you understand what `i` and `j` mean, quicksort stops feeling mysterious. `j` scans through the unknown region one element at a time, and `i` marks the end of the tan region. An element only joins the tan region when it is found to be `<= x`; otherwise it stays in the blue region. The final swap places the pivot directly to the right of the tan region, which is why the returned index is already the pivot's final sorted position.

## 7.2 Performance of Quicksort
The efficiency of quicksort depends on whether the partitioning is **balanced or unbalanced**, which is determined by the choice of the pivot.

### Worst-Case Partitioning
The worst case occurs when the partitioning routine produces one subarray with **n-1 elements** and one with **0 elements** at every level of recursion. This behavior typically happens when the input array is already sorted or reverse-sorted.
- **Recurrence:** $T(n)=T(n-1)+T(0)+Θ(n)$.
- **Result:** Summing the costs at each level results in an arithmetic series, leading to $Θ(n^2)$.

### Best-Case Partitioning
The best case occurs when `PARTITION` produces two subarrays of roughly equal size, $n/2$.
- **Recurrence:** $T(n)=2T(n/2)+Θ(n)$.
- **Result:** By the master method, this solves to $Θ(n \lg n)$.

> *Balanced Partitioning*
> Quicksort is robust even when the split is not perfectly centered. A **9-to-1 proportional split** still results in $O(n \lg n)$ time. The recursion tree still has height $Θ(\lg n)$, and the total work per level remains $O(n)$.

### Lecture Emphasis
The lecture used the recursion-tree notebook to make the 9:1 split point intuitive. The important fact is not that the tree is perfectly balanced. It is that the larger side still shrinks by a constant factor each time. That keeps the height logarithmic, which is enough for total $O(n \lg n)$ work as long as partitioning stays linear per level.

## 7.3 A Randomized Version of Quicksort
To prevent an oblivious adversary from forcing the worst-case behavior with specific inputs, randomization is used. The `RANDOMIZED-PARTITION` procedure picks a random element from the subarray to serve as the pivot by swapping it with $A[r]$ before partitioning. This ensures that the pivot choice is independent of the input order, resulting in good expected performance for all inputs.

### Median-of-3 and Three-Way Partition
The lecture's modification notebook added two practical refinements:

- **Median-of-3:** choose the pivot as the median of `A[p]`, `A[(p+r)//2]`, and `A[r]`. This improves constants on partially ordered inputs but does not change the asymptotic worst-case bound.
- **Three-way partition:** split the array into `< x`, `= x`, and `> x` regions. This prevents the all-equal-elements degeneration that makes ordinary partition produce repeated 0:n-1 splits.

## 7.4 Analysis of Quicksort
### Worst-Case Analysis
Using the substitution method, it can be proven that $T(n)=O(n^2)$. By guessing $T(n)\leq c n^2$ and accounting for the maximization over split points q, the math demonstrates that the worst-case time is quadratic.

### Expected Running Time Analysis
The lecture framed the proof through three lemmas and one theorem.

1. **Lemma 1:** The running time of randomized quicksort on an input of size n is $O(n + X)$ where X is the number of comparisons made.
2. **Lemma 2:** Two elements $z_i$ and $z_j$ are compared if and only if one of them is chosen as the first pivot from the set $\{z_i, z_{i+1}, \dots, z_j\}$.
3. **Lemma 3:** $\Pr[z_i \text{ is compared to } z_j] = \dfrac{2}{j-i+1}$.

From those lemmas:
- **Total Time:** $O(n+X)$.
- **Expected Comparisons:** $E[X] = \sum_{i<j} \dfrac{2}{j-i+1} = O(n \lg n)$.
- **Theorem 7.4:** The expected running time of randomized quicksort is $O(n \lg n)$.

### Lecture Emphasis
The most important idea here is that no two elements are compared twice. Once one of them becomes a pivot, the pair is separated forever. That is what makes the probability argument manageable and turns a messy recursive process into a clean sum over pairs of elements.

# Chapter - 10 Elementary Data Structures
This chapter covers the representation of **dynamic sets** using simple data structures and pointers. These structures include arrays, matrices, stacks, queues, linked lists, and rooted trees.

## 10.1 Simple Array-Based Data Structures
### 10.1.1 Arrays
An array is stored as a **contiguous sequence of bytes** in memory. If an array starts at address a, each element occupies b bytes, and the first index is s, the address of the i-th element is calculated as:
$$
\text{Address}(A[i]) = a + b(i-s)
$$

> [!IMPORTANT] **Indexing Note:** The textbook primarily uses **1-origin indexing**. Most programming languages use **0-origin indexing**.

### 10.1.2 Matrices
Matrices are typically represented using one-dimensional arrays in row-major or column-major order.
- **Row-major order:** stored row by row.
- **Column-major order:** stored column by column.

### 10.1.3 Stacks and Queues
These are dynamic sets where the element removed is pre-specified by the structure's policy.

1. **Stacks (LIFO)**
	- `PUSH(S, x)`: adds element x to the top.
	- `POP(S)`: removes and returns the most recently added element.
	- Both operations take $O(1)$ time.

2. **Queues (FIFO)**
	- `ENQUEUE(Q, x)`: adds element x to the tail.
	- `DEQUEUE(Q)`: removes the element at the head.
	- The queue wraps around the array, giving a circular implementation.

### Circular Queue Full and Empty Detection
The lecture used the 0-indexed Python version:
- **Empty:** `head == tail`
- **Full:** `(tail + 1) % n == head`

The wasted slot is not an accident. It is what allows the queue to distinguish "completely empty" from "completely full" without needing an extra counter.

### CodingHW3 Extensions
The homework turned the textbook structures into actual variants:

```python
# two stacks in one array
l_top = -1
r_top = n
# overflow when l_top + 1 == r_top
```

- Left stack grows right from index 0.
- Right stack grows left from index `n-1`.
- All push and pop operations remain $O(1)$.

The deque extension added `add_first` and `remove_last` to the circular queue while preserving constant-time operations.

## 10.2 Linked Lists
In a linked list, objects are arranged in a linear order determined by **pointers** rather than array indices.

1. **Structure**
	- **Doubly Linked List:** Each node contains a `key`, `next`, and `prev`.
	- **Singly Linked List:** Nodes have a `next` pointer but no `prev`.
	- **Circular List:** The `prev` of the head points to the tail, and the `next` of the tail points to the head.

2. **Operations**
	- `LIST-SEARCH(L, k)`: $Θ(n)$.
	- `LIST-PREPEND(L, x)`: $O(1)$.
	- `LIST-INSERT(x, y)`: $O(1)$.
	- `LIST-DELETE(L, x)`: $O(1)$ if the pointer to x is already known.

### Sentinels
A **sentinel** (`L.nil`) is a dummy object used to simplify boundary conditions.
- It turns a doubly linked list into a circular one.
- The head is `L.nil.next`.
- The tail is `L.nil.prev`.

### Lecture Emphasis
The linked-list lecture kept returning to the difference between "operation cost when you already have the pointer" and "operation cost when you must first search for the node." That is why list deletion is often described as $O(1)$ but real tasks that first search for the target can still cost $Θ(n)$ overall.

## 10.3 Representing Rooted Trees
Rooted trees are represented by nodes containing keys and pointers to other nodes.

### Binary Trees
Each node x uses three pointers:
1. `x.p`: parent.
2. `x.left`: left child.
3. `x.right`: right child.

### Trees with Unbounded Branching
When a node can have an arbitrary number of children, the **left-child, right-sibling representation** is used:
- `x.left-child`: points to the leftmost child.
- `x.right-sibling`: points to the next sibling.
- Uses $O(n)$ space for any n-node rooted tree.

### BST Traversals and Delete Cases from Lecture
The lecture extended Chapter 10 directly into binary search trees using the week notebooks.

```python
def in_order(T, node):
    if node:
        in_order(T, node.left)
        print(node.key)
        in_order(T, node.right)
```

This traversal is the most important one because it prints a BST in sorted order.

The delete discussion centered on these cases:
1. `z.left == None` -> `transplant(z, z.right)`
2. `z.right == None` -> `transplant(z, z.left)`
3. two children, successor `y = min(z.right)` is the right child
4. two children, successor `y = min(z.right)` is deeper in the right subtree

`TRANSPLANT(u, v)` only rewires the parent-side connection. It does **not** modify `u.left` or `u.right`. That detail matters because it explains why delete logic must explicitly reconnect y's children afterward.

### Non-Recursive Linked-List Reverse
CodingHW3 also added the standard in-place reverse:

```python
prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev, curr = curr, nxt
return prev
```

This is a classic example of pointer manipulation with $Theta(n)$ time and $O(1)$ extra space.

---

## Overview
- Chapters 7 and 10 connect a major sorting algorithm, quicksort, with the elementary data structures used throughout the course.
- In CSCI 4041, quicksort is the main randomized divide-and-conquer sorting example, while stacks, queues, linked lists, and rooted-tree representations become implementation tools for graph and tree algorithms.
- The lecture notebooks emphasize both algorithm mechanics and Python data-structure edge cases.

## Core Definitions
- **Partition:** rearranges a subarray around a pivot so all smaller/equal keys are on one side and larger keys are on the other.
- **Randomized quicksort:** chooses a random pivot to make the expected split behavior independent of the original input order.
- **Stack:** last-in, first-out structure with `push` and `pop`.
- **Queue:** first-in, first-out structure with `enqueue` and `dequeue`.
- **Linked list:** node-based sequence using `next` references, optionally with head/tail sentinels.
- **Rooted tree representation:** stores parent/child/sibling or left/right child pointers depending on tree shape.

## Main Algorithms
- `QUICKSORT(A,p,r)`: recursively partitions and sorts the two sides.
- `PARTITION(A,p,r)`: scans once and maintains regions for keys `<= pivot`, `> pivot`, unknown keys, and pivot.
- `RANDOMIZED-PARTITION`: swaps a random element into pivot position before partitioning.
- Lecture variants include constant-subarray handling and algorithmic modifications from Chapter 7 exercises.
- Chapter 10 implementations include array stack, circular queue, singly linked list, and linked binary tree.

## Correctness Ideas
- Partition correctness is a loop invariant over the four regions of the array.
- Quicksort correctness follows by induction after partition places the pivot in its final sorted position.
- Randomization does not change sortedness; it changes the probability distribution of split quality.
- Stack/queue correctness is about preserving the LIFO/FIFO invariant after each operation.
- Linked-list correctness depends on preserving reachability from `head` and not dropping nodes during pointer rewrites.

## Complexity
- Partition is `Theta(n)` on a subarray of length `n`.
- Quicksort worst case is `Theta(n^2)` when partitions are maximally unbalanced.
- Randomized quicksort expected time is `Theta(n lg n)`.
- Quicksort auxiliary stack space is `O(lg n)` expected for balanced recursion and `O(n)` worst case.
- Stack and queue operations are `O(1)` when overflow/underflow checks and circular indices are handled correctly; linked-list search is `Theta(n)`.

## Lecture Emphasis
- `Lectures/Week - 4/Ch7_QuickSort.ipynb` is the direct implementation of textbook quicksort:

```python
def Partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i = i+1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1
```

- `Ch7_QuickSort(AlgorithmicModifcationExamples).ipynb` adds the exercise-style variants, especially constant-subarray handling.
- `Ch10_Stacks_and_Queues.ipynb` makes overflow/underflow and circular queue wraparound explicit.
- `Ch10_LinkedLists.ipynb` and `Ch10_BinaryTree.ipynb` ground textbook fields in Python node objects.
- `Homework/Coding/CodingHW_3(chapter10-CLRS).ipynb` asks for two stacks in one array, an array deque, and a stack via singly linked list.
- Weekly/concept links: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 4|Week - 4]], [[QuickSort|QuickSort]], [[Elementary Data Structures|Elementary Data Structures]].

## Examples
- Partitioning `[2, 8, 7, 1, 3, 5, 6, 4]` with pivot `4` leaves all values `<=4` left of the pivot and all values `>4` right of it.
- A circular queue must treat index wraparound as part of the representation, not as a special later cleanup step.
- Reversing a singly linked list uses three references: previous, current, and next.

## Connections
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 4|Week - 4]]
- [[QuickSort|QuickSort]]
- [[Elementary Data Structures|Elementary Data Structures]]
- Source homework read: `Homework/Coding/CodingHW_3(chapter10-CLRS).ipynb` and `Homework/Paper/Paper HW - 3 (Ch - 7 & 10).pdf`.
- TODO: source gap - no vault Homework/Paper Homework note exists for direct wikilinking.

## Common Pitfalls
- Confusing quicksort's expected `Theta(n lg n)` with its worst-case `Theta(n^2)`.
- Forgetting that partition places only the pivot in final position.
- Mishandling arrays with many equal keys.
- Letting circular queues use one slot ambiguity without a clear full/empty convention.
- Reversing a linked list without saving `next` before overwriting it.

## Review Checklist
- [ ] Implement partition and state its loop invariant.
- [ ] Explain randomized quicksort's expected-time advantage.
- [ ] Trace stack, queue, deque, and linked-list operations by hand.
- [ ] Explain the pointer updates for linked-list reversal.
- [ ] Identify which data-structure operations are `O(1)` and which are linear.

This is a classic example of pointer manipulation with $Θ(n)$ time and $O(1)$ extra space.
