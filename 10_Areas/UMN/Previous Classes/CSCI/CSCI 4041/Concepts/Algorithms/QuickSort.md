---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 5
created: 2026-02-16
topics:
  - "[[DSA]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Concepts/Introduction to Algorithms]]"
  - "[[Chapter - 7 & 10]]"
related:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 4|Week - 4]]"
  - "[[Sorting Algorithms]]"
  - "[[Divide and Conquer]]"
---
# [[QuickSort]]
## MOC
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 4#Jupyter Notebook Explanations|Week - 4]]
- [[Chapter - 7 & 10#7.1 Description of Quicksort|Chapter - 7 & 10 - Quicksort]]
- [[Sorting Algorithms#Core Ideas (Lecture)|Sorting Algorithms - Core Ideas (Lecture)]]
- [[Divide and Conquer#Proof / Reasoning Toolkit|Divide and Conquer - Proof / Reasoning Toolkit]]

## Definition
- **Quicksort** is an in-place divide-and-conquer sorting algorithm that partitions a subarray around a pivot and then recursively sorts the two sides.
- **Partition** is the linear-time routine that rearranges the subarray so all values `<= pivot` are on the left and all values `> pivot` are on the right.
- **Expected runtime** is $Θ(n \lg n)$ under randomized pivot selection, while the worst case is $Θ(n^2)$.
- **No combine step** is needed because partitioning leaves the pivot directly in its final sorted position.

## Core Ideas (Textbook)
### 7.1 Algorithm Structure
- Quicksort follows divide, conquer, and implicit combine.
- Divide is the partition pass; conquer is the two recursive calls.
- Once partition returns q, the pivot is already correct and never moves again.
- That is why the full algorithm can be reduced mentally to "repeated partitioning."

### 7.2 Performance Cases
- Worst case happens when partition always gives a 0:n-1 split.
- Best case happens when partition always gives a near 1:1 split.
- Even strongly unbalanced but proportional splits like 9:1 still keep the tree height logarithmic.
- The dominant cost is linear partition work times the number of recursion levels.

### 7.3 Randomization
- Randomization breaks the dependency between input order and pivot choice.
- An oblivious adversary can choose the input but cannot force every pivot to be bad.
- This does not remove the worst case from possibility; it makes the expected case good on every input.

### 7.4 Expected Analysis
- Runtime is bounded by $O(n + X)$ where X counts comparisons.
- The proof shifts from recursive calls to element pairs $z_i, z_j$.
- A pair is compared exactly when one is the first pivot chosen from the interval of ranks between them.
- Summing those pairwise probabilities gives the harmonic-series bound and expected $Θ(n \lg n)$ comparisons.

## Core Ideas (Lecture)
### Full 0-Indexed Partition Code
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

What this code is doing:
1. `x = A[r]` chooses the pivot as the last item.
2. `i = p - 1` means the tan region starts empty.
3. `j` scans left to right across the unknown region.
4. When `A[j] <= x`, the tan region expands by one and the current element is swapped into it.
5. When `A[j] > x`, the element stays in the blue region without any special code.
6. The final swap places the pivot immediately after the tan region, so that returned position is final.

### Four Regions / Loop Invariant
The lecture visualization used four color-coded regions:

| Region | Indices | Meaning |
| --- | --- | --- |
| Tan | `p..i` | values `<= x` |
| Blue | `i+1..j-1` | values `> x` |
| White | `j..r-1` | not examined yet |
| Yellow | `r` | pivot |

This invariant is the source of the correctness proof, not just a picture.

### Expected-Case Lemmas
The lecture's proof outline was:
1. **Lemma 1:** runtime is $O(n+X)$.
2. **Lemma 2:** $z_i$ and $z_j$ are compared if and only if one of them is the first pivot chosen from the set $\{z_i, \dots, z_j\}$.
3. **Lemma 3:** $\Pr[z_i \text{ compared to } z_j] = 2/(j-i+1)$.
4. Therefore $E[X] = O(n \lg n)$ and so expected runtime is $O(n \lg n)$.

The critical intuition is that once one of the two elements is chosen as pivot, the pair can never be compared again.

### Notebook Modifications
#### Median-of-3
- Pivot = median of `A[p]`, `A[(p+r)//2]`, `A[r]`.
- Useful on partially ordered data because it reduces the chance of choosing an extreme pivot.
- Improves constants but does not change the formal worst-case bound.

#### Three-Way Partition
- Splits elements into `< x`, `= x`, and `> x`.
- This is the fix for all-equal inputs, where ordinary partition degenerates badly.
- The lecture treated this as a practical correction for a real weakness in the textbook routine.

## Proof / Reasoning Toolkit
### Partition Loop-Invariant Checklist
1. State the four regions before the loop body executes.
2. Explain what happens when the current value is `<= pivot`.
3. Explain what happens when the current value is `> pivot`.
4. Use the final pivot swap to conclude that the pivot is in its final position.

### Expected-Analysis Checklist
1. Replace "runtime" with "number of comparisons."
2. Sort the input conceptually into order statistics $z_1 < z_2 < \dots < z_n$.
3. Ask when a specific pair can first meet.
4. Sum pairwise comparison probabilities, not recursion costs directly.

### Recursion-Tree Checklist
1. Identify the largest subproblem shrink factor.
2. Show that the height is still logarithmic if the larger side shrinks by a constant factor.
3. Multiply linear work per level by the tree height.

## Complexity + Tradeoffs
| Variant | Time | Extra Space | Main Tradeoff |
| --- | --- | --- | --- |
| Standard quicksort | Best/avg $Θ(n \lg n)$, worst $Θ(n^2)$ | $O(\lg n)$ avg recursion stack | In-place and fast constants, but pivot-sensitive |
| Randomized quicksort | Expected $Θ(n \lg n)$ | $O(\lg n)$ avg recursion stack | Stronger expected guarantee |
| Median-of-3 quicksort | Same asymptotic bounds | Same | Better practical pivot quality |
| Three-way quicksort | Handles equal keys better | Same | Extra partition logic for better duplicate behavior |

## Canonical Examples (Max 5)
### 1. Partition Trace
- Input: `[3,7,8,5,2,1,9,5,4]`, pivot `4`.
- After one partition pass: `[3,2,1,4,7,8,5,9,5]`.
- Common mistake: forgetting that this is only one partition step, not the final fully sorted array.

### 2. Already Sorted Worst Case
- Pivot always chosen as the largest value.
- Produces a 0:n-1 split at every call.
- Recurrence becomes $T(n)=T(n-1)+Θ(n)$.

### 3. 9:1 Split Still Works
- Larger side still shrinks by a constant factor each level.
- Height stays $Θ(\lg n)$.
- Total level cost stays linear.

### 4. All Equal Elements
- Standard partition keeps moving every item into the left side.
- That repeats a nearly full-size recursive call each time.
- Three-way partition fixes this by grouping equal values in the middle.

### 5. Randomized Pivot Story
- Same bad input can behave very differently depending on pivot choice.
- Randomization makes input order stop controlling the pivot sequence.
- This is why quicksort is usually analyzed by expectation instead of worst-case-only intuition.

## Practice Map
- Kth Largest Element in an Array
- Sort Colors / Dutch National Flag
- Quickselect-style partition problems
- Course Schedule style topological sort only as a contrast: it is also linear partitioning of structure, but not a sorting algorithm
- Any "implement sort an array" task where you compare quicksort against merge sort
- CodingHW_3(chapter10-CLRS).ipynb: two stacks in one array, deque, linked-stack/queue, list reversal (Ch 7 & 10 combined)
- Paper HW - 3 (Ch - 7 & 10).pdf: written problems on quicksort partitioning and data structure invariants

## Mini-test
1. Why does partition return the pivot's final index rather than a temporary split point?
2. What do `i` and `j` each mean during the partition loop?
3. Why can no pair of elements be compared twice in randomized quicksort?
4. Why does a 9:1 split still give $O(n \lg n)$?
5. What specific weakness is fixed by three-way partition?

## Flashcards
#cards/CSCI4041
1. What is the pivot in the lecture partition code::The last element `A[r]`.
2. What does the tan region contain::Elements known to be `<= pivot`.
3. Quicksort worst-case recurrence::$T(n)=T(n-1)+Θ(n)$.
4. Why is randomized quicksort expected $Θ(n \lg n)$::Because the expected number of pairwise comparisons is $O(n \lg n)$.
5. Comparison probability formula::$\Pr[z_i \text{ compared to } z_j] = 2/(j-i+1)$.
6. Why is there no combine step in quicksort::Partition already places the pivot in its final position and the recursive calls sort the two sides in place.
7. What does three-way partition improve::Performance on inputs with many equal keys.
