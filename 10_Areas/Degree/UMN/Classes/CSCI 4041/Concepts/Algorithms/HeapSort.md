---
type: concept
course: CSCI 4041
status: seed
mastery (1/10): 0
created: 2026-02-19
topics:
  - "[[Chapter - 6 & 12]]"
  - "[[Introduction to Algorithms]]"
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
related:
  - "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 5|Week - 5]]"
  - "[[Sorting Algorithms]]"
  - "[[Elementary Data Structures]]"
---
# [[HeapSort]]
## MOC
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 5#Jupyter Notebook Explanations|Week - 5]]
- [[Chapter - 6 & 12#Chapter - 6 Heapsort|Chapter - 6 & 12 - Heapsort]]
- [[Sorting Algorithms#Complexity + Tradeoffs|Sorting Algorithms - Complexity + Tradeoffs]]
- [[Elementary Data Structures#Definition|Elementary Data Structures]]

## Definition
- **Heap** means an array interpreted as a nearly complete binary tree.
- **Max-heap** means every parent key is at least as large as its children.
- **Heapsort** builds a max-heap and then repeatedly removes the root into the sorted tail.
- **Priority queue** uses the heap to support fast repeated access to the current maximum or minimum.

## Core Ideas (Textbook)
### Heap Structure
- The shape property is what makes the index formulas work.
- The heap property gives only parent-child order, not full sorted order.
- That weaker invariant is enough for priority queue operations and heapsort.
- The root of a max-heap is always the maximum.

### Heapify and Build
- `MAX-HEAPIFY` repairs one local violation by pushing a bad value downward.
- `BUILD-MAX-HEAP` works bottom-up because leaves are already heaps.
- The linear-time build proof comes from counting node heights, not just counting calls.
- This is one of the standard examples where worst-case-per-call times are too loose for total cost.

### Heapsort and Priority Queues
- Heapsort is in-place and worst-case $O(n \lg n)$.
- It is not stable because swaps move equal keys past one another.
- Priority queue operations are balanced: no operation is constant except reading the maximum.
- Heaps are the compromise structure when we care about repeated best-element access but do not need full sorted traversal all the time.

## Core Ideas (Lecture)
### 0-Indexed Heap Arithmetic
```python
left(i) = 2*i + 1
right(i) = 2*i + 2
parent(i) = (i - 1) // 2
```

The lecture treated this as the key translation from tree to array. If these formulas are automatic, most heap code becomes readable immediately.

### `increase_key` and `extract_max`
```python
def increase_key(i, key):
    A[i] = key
    while i > 0 and A[(i - 1) // 2] < A[i]:
        A[i], A[(i - 1) // 2] = A[(i - 1) // 2], A[i]
        i = (i - 1) // 2
```

```python
def extract_max():
    m = A[0]
    A[0] = A[heap_size - 1]
    heap_size -= 1
    max_heapify(0)
    return m
```

These two routines are the cleanest way to remember directional repair:
- bigger key -> may need to move up
- root replacement with unknown key -> may need to move down

### `arraytree` and `heappriorityqueue`
- `arraytree` stores `A`, `size`, and `capacity`.
- `add_left` and `add_right` compute child slots directly.
- `heappriorityqueue` subclasses that structure and adds heap-specific repair operations.
- The plotting support in the notebook matters because it helps connect the array to the conceptual tree picture.

### CodingHW4 Variants
#### Min-Heap Priority Queue
- Reverse all comparison directions.
- `extract_min` removes the root.
- `decrease_key` bubbles upward instead of downward.

#### Max-Heap Decrease-Key
- Decreasing a key in a max-heap can only create a violation with children.
- That means the repair path is downward, not upward.

#### Heap Delete
- Raise the target to `∞`.
- Bubble it to the root with increase-key.
- Remove it using extract-max.

#### k-Way Merge
- Heap stores `(value, list_index, element_index)`.
- After extracting the smallest current value, push the next value from the same list.
- Total cost is $O(n \lg k)$ because the heap never grows beyond k elements.

## Proof / Reasoning Toolkit
### `BUILD-MAX-HEAP` Linear-Time Checklist
1. Group nodes by height.
2. Count how many nodes can appear at each height.
3. Multiply "nodes at height h" by "heapify cost O(h)."
4. Use the convergent series $\sum h/2^h$ to finish the bound.

### Direction-of-Repair Checklist
1. Ask whether the changed key got bigger or smaller.
2. Ask whether the possible violation is with ancestors or descendants.
3. Repair only along that one possible path.

### Heap/Tree Translation Checklist
1. Decide whether you are working in 1-indexed or 0-indexed form.
2. Translate parent/child formulas once.
3. Keep the formulas consistent across every routine.

## Complexity + Tradeoffs
| Operation / Structure | Time | Why |
| --- | --- | --- |
| `MAX-HEAPIFY` | $O(\lg n)$ | follows one root-to-leaf path |
| `BUILD-MAX-HEAP` | $O(n)$ | most nodes are shallow |
| Heapsort | $O(n \lg n)$ | build once, then n-1 heap repairs |
| `MAXIMUM` | $O(1)$ | root lookup |
| `EXTRACT-MAX` | $O(\lg n)$ | root replacement plus downward repair |
| `INCREASE-KEY` | $O(\lg n)$ | upward bubbling |

## Canonical Examples (Max 5)
### 1. Array-to-Tree Mapping
- Index 0 is the root.
- Index 1 is the left child of the root.
- Index 2 is the right child of the root.
- This is the mental map behind every heap operation.

### 2. Why Build-Heap Is Not $O(n \lg n)$
- There are many leaves and almost-leaves.
- Only a few nodes are near the root with large repair cost.
- The weighted sum of heights is linear.

### 3. Extract-Max
- Save the root.
- Move the last element to index 0.
- Heapify downward until the max-heap property returns.

### 4. Max-Heap Delete
- Inflate target to infinity.
- Bubble it upward.
- Remove it as though it were the root.

### 5. k-Way Merge
- Keep only one frontier element per list in the heap.
- This is the reason the logarithmic factor depends on k, not on the total number of elements.

## Practice Map
- Kth Largest Element
- Top K Frequent Elements
- Merge k Sorted Lists
- Find Median from Data Stream
- Any priority-queue simulation problem where repeated best-choice extraction matters

## Mini-test
1. Why does a heap not need full sorted order to support extract-max efficiently?
2. Why is `BUILD-MAX-HEAP` linear?
3. What determines whether heap repair goes up or down?
4. Why does k-way merge use a heap of size k instead of n?
5. Why is heapsort not stable?

## Flashcards
#cards/CSCI4041
1. 0-index heap parent formula::`(i - 1) // 2`.
2. Root of a max-heap::Always the maximum element.
3. `MAX-HEAPIFY` direction::Downward.
4. `INCREASE-KEY` direction in a max-heap::Upward.
5. `BUILD-MAX-HEAP` runtime::$O(n)$.
6. Heapsort stability::Not stable.
7. k-way merge runtime::$O(n \lg k)$.
