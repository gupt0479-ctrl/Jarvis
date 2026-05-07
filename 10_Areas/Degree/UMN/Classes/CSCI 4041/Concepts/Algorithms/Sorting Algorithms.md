---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 4
created: 2026-02-01
topics:
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
  - "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 1 & 2|Week - 1 & 2]]"
  - "[[Introduction to Algorithms]]"
  - "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Textbook/Chapter - 1 & 2]]"
related:
  - "[[Divide and Conquer]]"
  - "[[Time Complexity]]"
---
# [[Sorting Algorithms]]
## MOC
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 1 & 2#Chapter 1 and Chapter 2 - Insertion Sort, Cost Models, and Merge Sort|Week - 1 & 2]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Textbook/Chapter - 1 & 2#2.1 Insertion Sort|Chapter - 1 & 2 - Insertion Sort]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Textbook/Chapter - 1 & 2#2.3 Designing Algorithms|Chapter - 1 & 2 - Merge Sort]]
- [[Divide and Conquer#Definition|Divide and Conquer]]
- [[Time Complexity#Definition|Time Complexity]]

## Definition
- **Sorting problem**: given a sequence of keys, return a permutation of those keys in nondecreasing order.
- **Insertion sort**: an incremental sorting method that maintains a sorted prefix and inserts the next key into that prefix.
- **Merge sort**: a divide-and-conquer sorting method that recursively sorts halves and merges them in linear time.
- **In-place**: uses only `O(1)` extra storage outside the input array.
- **Correctness**: the algorithm halts and produces the required sorted output for every valid input instance.

## Core Ideas (Textbook)
### 2.1 Insertion Sort
- The algorithm keeps the prefix already processed in sorted order and inserts the next key by shifting larger elements to the right.
- The standard proof tool is a loop invariant: before each iteration, the prefix contains the original elements from that region in sorted order.
- The textbook version is in-place, so it uses constant extra space outside the input array.
- Best case occurs on already sorted input, while reverse-sorted input forces the maximum number of shifts and comparisons.

### 2.2 Analyzing Algorithms
- The RAM model treats primitive operations and data accesses as constant-time steps so that growth can be analyzed at the algorithmic level.
- Best case, worst case, and average case are not different algorithms; they are different input arrangements for the same algorithm.
- Insertion sort has `Theta(n)` best case and `Theta(n^2)` average and worst case.
- Asymptotic notation ignores lower-order terms and constant factors to isolate long-run growth.

### 2.3 Designing Algorithms
- Divide-and-conquer splits a problem into smaller instances, solves them recursively, and combines the results.
- Merge sort satisfies `T(n) = 2T(n/2) + Theta(n)`.
- The merge step is linear because every element is copied into the merged output exactly once.
- The recursion tree shows that merge sort runs in `Theta(n lg n)`.

## Core Ideas (Lecture)
### Three insertion-sort variants
Lecture emphasized that [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 1 & 2#Chapter 1 and Chapter 2 - Insertion Sort, Cost Models, and Merge Sort|Week - 1 & 2]] was not about memorizing one code listing. It was about seeing how implementation choices affect cost.
1. **CLRS in-place version**
	- Stores the current key, shifts larger values right, and writes the key into the gap.
	- This is the cleanest version for a loop-invariant proof and for RAM-model reasoning.
2. **`insertion_sort_python`**
	- Replaces explicit shifts with `A.pop(i)` and `A.insert(j+1, key)`.
	- The algorithmic idea remains insertion sort, but middle edits on Python lists are not cheap.
3. **`insertion_sort_Joy`**
	- Builds a separate `sorted_array`.
	- It is easier to read, but it is not in-place and uses `Theta(n)` extra memory.

### `merge_list` from `Ch2_Merge_Sort.ipynb`
This is the exact lecture code for Joy's list-based merge:

```python
def merge_list(A,B):
    """merges lists A and B (assuming they are each in order)"""

    N = len(A)+len(B)
    output = [None for i in range(N)]   # space requirement O( |A| + |B| )

    k = N-1  # location to copy to
    while A and B:
        if A[-1] > B[-1]:               # load output from the back
            key = A.pop()               # remove from A
        else:
            key = B.pop()               # remove from B
        output[k] = key
        k-=1
    ######################## empty A or B when they are the only one left
    while A:
        key = A.pop()
        output[k] = key
        k-=1
    while B:
        key = B.pop()
        output[k] = key
        k-=1

    return output       # reference to new array with combined values
```

Line-by-line explanation:
1. `N = len(A) + len(B)` computes the total output length once so the merge step does not keep growing the list dynamically.
2. `output = [None for i in range(N)]` allocates the output array up front, making the space cost visible.
3. `k = N-1` means the output is filled from right to left instead of left to right.
4. `if A[-1] > B[-1]` compares the largest remaining items because both lists are already sorted.
5. `A.pop()` or `B.pop()` removes that largest remaining element from the end, which is cheap on Python lists.
6. `output[k] = key` writes the chosen element into the current final slot, and `k -= 1` moves the fill pointer left.
7. The final `while A:` and `while B:` loops drain whichever list still has leftovers after one side empties.

### FLOPS / chosen-cost model
The lecture's FLOPS notebook was really a cost-model notebook, not a benchmarking notebook:

```python
def insertion_sort_python_cost(A,n):
    """sorts the array A (in-place) using the insertion sort algorithm from CLRS-ch2"""
    cost = 0

    for i in range(1,n):
        # (Loop Invariant)
        # the elements in positions 0 to i-1 are sorted (start at 1)
        #print(A[:i])

        key = A.pop(i)               # pop current element
        cost += 1       # this is the cost for link-based structures
        #cost += n-i    # this is the cost for array-based structures

        j = i-1
        cost += 1

        while j>=0 and A[j]>key:    # walk back to find insertion point
            j = j-1                 # move back
            cost += 1

        A.insert(j+1,key)           # insert ith element (key) into position j+1
        cost += 1        # this is the cost for link-based -O(1)
        #cost += n-(j+1) # this is the cost for array-based -O(length)

    return A,cost
```

The comments are the lecture's real point. The notebook deliberately separates a link-based interpretation from an array-based interpretation so the same high-level algorithm can be analyzed under two different concrete data-structure costs.

### Hybrid optimization from `CodingHW_1(chapter2-CLRS).ipynb`
The homework version of coarsened merge sort stops the recursion once the subproblem is small enough:

```python
def merge_coarse(A,n,k=8):
    """sorts the array A using the merge sort algorithm with insertion sort for leaf cases of size less than k"""

    # base cases
    if n < 2:
        return A[:]
    if n <= k:
        return insertion_sort_python(A[:], n)   # sort a copy using insertion sort

    # recursive case
    q = int(n/2)
    L = merge_coarse(A[:q], q, k)        # left half sorted list
    R = merge_coarse(A[q:], n - q, k)    # right half sorted list

    # merge
    return merge_list(L, R)
```

If there are `n/k` insertion-sorted leaves and each leaf costs `Theta(k^2)`, then the leaf work is `Theta(nk)`. The merge phase above those leaves costs `Theta(n lg(n/k))`. So the full hybrid cost is `Theta(nk + n lg(n/k))`, and choosing `k = Theta(lg n)` preserves `Theta(n lg n)`.

## Proof / Reasoning Toolkit
### Loop Invariant Checklist
1. State the property that is true before each loop iteration.
2. Show it is true before the first iteration.
3. Assume it is true at the start of one iteration and prove the loop body preserves it.
4. Use the invariant at termination to conclude correctness.

### Cost-Model Checklist
1. Say what one unit of "cost" means.
2. Identify which operations depend on the data structure rather than just the high-level algorithm.
3. Count the dominant repeated work instead of only describing the code informally.

### Recursion-Tree Checklist
1. Compute the subproblem size at depth `i`.
2. Count how many subproblems appear at that level.
3. Multiply "number of subproblems" by "cost per subproblem."
4. Sum over levels and simplify asymptotically.

### Hybrid Sort Checklist
1. Separate leaf work from merge work.
2. Count how many leaves there are.
3. Express the merge height as `lg(n/k)`.
4. Choose `k` to improve constants without changing the asymptotic rate.

## Complexity + Tradeoffs
| Algorithm / Variant | Time | Extra Space | Main Lecture Point |
| --- | --- | --- | --- |
| CLRS insertion sort | Best `Theta(n)`, worst `Theta(n^2)` | `O(1)` | Best fit for loop invariants and RAM-model analysis |
| `insertion_sort_python` | Still quadratic overall | `O(1)` extra list storage, but expensive middle edits | Data-structure operations change the real cost |
| `insertion_sort_Joy` | Best `Theta(n)`, average/worst `Theta(n^2)` | `Theta(n)` | Simpler structure, but not in-place |
| CLRS merge sort | `Theta(n lg n)` | `Theta(n)` | Classic divide-and-conquer recurrence |
| Joy `merge_sort_list` | `Theta(n lg n)` | `Theta(n)` plus sliced sublists | Python-specific implementation details matter |
| `merge_coarse` | `Theta(nk + n lg(n/k))` | Depends on copied sublists | Small-input tuning can preserve asymptotic optimality |

## Canonical Examples (Max 5)
### 1. Sorting instance `⟨31, 41, 59, 26, 41, 58⟩`
- **Goal:** Turn the input into a nondecreasing permutation.
- **Key steps:** Recognize that insertion sort and merge sort are two different correct algorithms for the same problem.
- **Common mistake:** Confusing the problem specification with one specific implementation.

### 2. CLRS insertion-sort trace on `[22, 48, 33, 12, 42, 8]`
- **Goal:** See the sorted-prefix invariant in action.
- **Key steps:** Save `key`, shift larger entries right, then write `key` once at `j+1`.
- **Common mistake:** Forgetting to store `key` before overwriting array cells.

### 3. `merge_list` on `A=[22,48]`, `B=[12,33]`
- **Goal:** Understand why the output fills from right to left.
- **Key steps:** Compare `48` and `33`, place `48`, then `33`, then `22`, then `12`.
- **Common mistake:** Assuming the merge must start at the front simply because the final array is sorted left to right.

### 4. `SUM-ARRAY` loop invariant
- **Goal:** Practice the initialization-maintenance-termination proof structure.
- **Key steps:** State `sum = sum of first i-1 items`, verify initialization, preserve it, then use termination.
- **Common mistake:** Writing an invariant that is only true after the loop body instead of before each iteration.

### 5. Hybrid merge sort with threshold `k`
- **Goal:** Explain where `Theta(nk + n lg(n/k))` comes from.
- **Key steps:** Count the `n/k` leaves, then count the merge levels above them.
- **Common mistake:** Forgetting that the merge phase starts only after subproblem size reaches `k`, not 1.

## Practice Map
- Implement insertion sort once from scratch using the CLRS shifting pattern.
- Compare a built-in sort against your own insertion sort on small arrays.
- Merge two sorted arrays or lists.
- Practice sorting-based grouping problems such as anagrams.
- Rehearse a three-value partitioning problem as preparation for [[QuickSort#Definition|QuickSort]] later.

## Mini-test
1. Why is the CLRS insertion-sort implementation the cleanest one for a loop-invariant proof?
2. What is the exact lecture point of the commented-out array-based cost lines in `insertion_sort_python_cost`?
3. Why does `merge_list` use `A[-1]` and `B[-1]` instead of the first elements?
4. How do you derive the `lg n + 1` recursion-tree height for merge sort?
5. Why does choosing `k = Theta(lg n)` keep `merge_coarse` asymptotically optimal?

## Flashcards
#cards/CSCI4041
1. Sorting problem::Return a permutation of the input keys in nondecreasing order.
2. Why is CLRS insertion sort in-place::It uses only a constant number of extra variables outside the array.
3. `insertion_sort_python` lecture lesson::The algorithmic idea can stay the same while the concrete operation costs change.
4. Why does `merge_list` pop from the end::End pops on Python lists are cheap and keep the merge step linear.
5. Merge-sort recurrence::`T(n) = 2T(n/2) + Theta(n)`.
6. Hybrid merge-sort formula::`Theta(nk + n lg(n/k))`.
7. What does a loop invariant buy you::A structured proof of initialization, maintenance, and termination.
