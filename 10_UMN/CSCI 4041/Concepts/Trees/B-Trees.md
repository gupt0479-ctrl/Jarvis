---
type: concept
course: CSCI 4041
status: tree
mastery (1/10): 4
created: 2026-02-25
updated: 2026-04-16
topics:
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
  - "[[10_UMN/CSCI 4041/Textbook/Chapter - 18]]"
related:
  - "[[AVL Trees]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/Elementary Data Structures]]"
  - "[[10_UMN/CSCI 4041/Week - 6|Week - 6]]"
---
# [[B-Trees]]
## MOC
- [[10_UMN/CSCI 4041/Week - 6#Jupyter Notebook Explanations|Week - 6]]
- [[10_UMN/CSCI 4041/Textbook/Chapter - 18#18.1 Definition of B-Trees|Chapter - 18 - Definition of B-Trees]]
- [[10_UMN/CSCI 4041/Textbook/Chapter - 18#18.3 Deletion|Chapter - 18 - Deletion]]
- [[10_UMN/CSCI 4041/Concepts/Trees/AVL Trees#Complexity + Tradeoffs|AVL Trees - Complexity + Tradeoffs]]

## Definition
- **B-tree** is a balanced multiway search tree designed for secondary storage.
- **Minimum degree t** controls how many keys and children each node may contain.
- **All leaves are at the same depth**, so the structure is height-balanced.
- **Main design goal** is to minimize expensive page accesses by keeping height very small.

## Core Ideas (Textbook)
### Secondary-Storage Motivation
- Disk and page access dominate cost when the structure does not fit in RAM.
- A B-tree node is intended to match a disk page.
- High branching factor reduces height dramatically.
- The right complexity measure is often "number of page reads" rather than CPU instructions.

### Node Constraints
- Every non-root node has between `t - 1` and `2t - 1` keys.
- Every internal non-root node has between `t` and `2t` children.
- The root is allowed to be smaller.
- A full node has exactly `2t - 1` keys.

### Search / Insert / Delete
- Search scans keys in the current node, then follows one child interval.
- Insert is top-down and pre-splits full nodes.
- Delete ensures the next child on the descent path is safe before recursing into it.
- Root split is the only way height increases.

## Core Ideas (Lecture + Ch18_B-Tree.ipynb)
### Python Node Shape
- `keys` list
- `children` list
- `leaf` boolean
- `n` current key count
- tree-level parameter `t`

This is the lecture's concrete equivalent of the textbook record fields.

### Inorder-Style Traversal
```python
def traverse(node):
    for i in range(node.n):
        if not node.leaf:
            traverse(node.children[i])
        print(node.keys[i])
    if not node.leaf:
        traverse(node.children[node.n])
```

This code is worth studying because it makes the search-tree ordering visible. Each child lives between two adjacent keys.

### Insert Strategy
- if the root is full, split it before descending
- before descending into a child, split that child if it is full
- this guarantees that insertion always reaches a non-full leaf

The lecture emphasized that this is the opposite feel of BST insertion. The structure is proactively repaired on the way down.

### Bayer and McCreight Notes
- designed for indexed files on disk
- guaranteed at least 50% page utilization
- operations are logarithmic in base k, the effective branching factor
- catenation = merge
- underflow = redistribution case
- height grows only when the root splits

## Proof / Reasoning Toolkit
### Height-Bound Checklist
1. Start with the sparsest legal B-tree.
2. Count how many nodes must appear at each depth.
3. Convert node count to key count.
4. Solve for h to get the logarithmic height bound.

### Insert-Reasoning Checklist
1. Never descend into a full node.
2. If a child is full, split it first.
3. Continue only after the child interval is safe.
4. Use "root split is the only height increase" as a sanity check.

### Delete-Reasoning Checklist
1. Decide whether the target key is in the current node.
2. If not, make sure the target child has enough keys before descending.
3. Borrow if a sibling has spare keys.
4. Merge only when necessary.

## Complexity + Tradeoffs
| Operation | Disk Accesses | Main Reason |
| --- | --- | --- |
| Search | $O(\log_t n)$ | very small height |
| Insert | $O(\log_t n)$ | one descent with occasional splits |
| Delete | $O(\log_t n)$ | one descent with borrow/merge repairs |

Compared with balanced binary trees, B-trees use more work per node but far fewer levels.

## Canonical Examples (Max 5)
### 1. t = 2 Special Case
- Each non-root node has 1 to 3 keys.
- Each internal non-root node has 2 to 4 children.
- This is the familiar 2-3-4 tree case.

### 2. Root Split
- Root is full.
- Create a new root.
- Split the old root into two children.
- Height increases by exactly 1.

### 3. Search Interval Logic
- Compare the target against the ordered keys in one node.
- Descend into the unique child interval that can still contain it.
- Same search-tree idea as BST, just with many keys per node.

### 4. Merge / Catenation
- Two minimum-size siblings plus a separator key are combined into one node.
- This may force a repair upward if the parent loses too many keys.

### 5. Height Intuition
- Large page size means huge branching factor.
- Huge branching factor means tiny height.
- Tiny height means very few disk reads.

## Practice Map
- Trace B-tree insertion by hand
- Trace B-tree deletion borrow/merge cases by hand
- Compare B-tree and AVL search paths conceptually
- Explain why databases like high branching factors
- Reconstruct a B-tree from a sequence of insertions for small t

## Mini-test
1. Why is minimum degree t the most important B-tree parameter?
2. Why is pre-splitting full children so helpful during insertion?
3. What is the only event that increases B-tree height?
4. Why do B-trees outperform balanced binary trees on secondary storage?
5. What is catenation in the original paper's terminology?

## Flashcards
#cards/CSCI4041
1. B-tree leaf-depth property::All leaves are at the same depth.
2. Non-root key range::Between `t - 1` and `2t - 1` keys.
3. When does B-tree height increase::Only when the root splits.
4. Why do B-trees reduce disk I/O::They store many keys per node, reducing height.
5. What is a full node::A node with exactly `2t - 1` keys.
6. Insert invariant::Never descend into a full node.
7. Catenation meaning::Merge two siblings together with the separator key from the parent.
