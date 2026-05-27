---
type: class
input_kind: book
status: sprout
created: 2026-02-25
updated: 2026-04-28
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]]"
---
# Chapter - 18 B-trees
## Summary Links
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6#Chapter 13 and Chapter 18 - Balanced Trees, Rotations, and B-Trees|Week - 6]]
- [[B-Trees#Definition|B-Trees]]
- [[AVL Trees#Complexity + Tradeoffs|AVL Trees - Complexity + Tradeoffs]]

B-trees are balanced search trees designed specifically to function efficiently on **secondary storage devices**. They are similar to balanced binary search trees, but use a high **branching factor** to minimize disk I/O operations.

## 18.0 Data Structures on Secondary Storage
Computer memory is hierarchical. Primary memory is fast but limited; secondary storage is slower but large.

- Data on disk is organized into blocks or pages.
- A single `DISK-READ` or `DISK-WRITE` accesses one page.
- The primary optimization goal is to minimize the number of page accesses.

This is the whole reason B-trees exist: reducing height by storing many keys per node reduces disk traffic.

## 18.1 Definition of B-Trees
A B-tree T is a rooted tree where every node x contains multiple keys instead of one.

### Node Attributes
1. `x.n`: number of keys currently in the node
2. `x.keys`: ordered key list
3. `x.children`: child pointers
4. `x.leaf`: boolean leaf marker

### Minimum Degree
For minimum degree $t \geq 2$:
- non-root nodes have at least `t - 1` keys
- non-root internal nodes have at least `t` children
- all nodes have at most `2t - 1` keys and `2t` children

### Height Bound
> [!NOTE] **Theorem 18.1:** For an n-key B-tree of minimum degree t,
> $$
> h \leq \log_t \frac{n+1}{2}.
> $$

With large t, the height becomes extremely small.

### Lecture `btree` Class
The notebook implementation used a class with:
- `keys` list
- `children` list
- `leaf` boolean
- `n` current key count
- tree attribute `t`

That matches the textbook structure but makes the state explicit in Python rather than as CLRS record fields.

## 18.2 Basic Operations
### Search
The search is a multiway version of BST search: scan the ordered keys in the current node, then descend into the unique child interval that could contain the target.

```python
def traverse(node):
    for i in range(node.n):
        if not node.leaf:
            traverse(node.children[i])
        print(node.keys[i])
    if not node.leaf:
        traverse(node.children[node.n])
```

The lecture used this inorder-style traversal because it makes it obvious that a B-tree is still a search tree, not just a page layout trick.

### Insert
Insertion is top-down:
1. if the root is full, split it first
2. descend toward the target leaf
3. split any full child before entering it
4. insert into a guaranteed non-full leaf

The root is the only node whose split can increase the height.

### Lecture Emphasis
The course contrasted B-tree insertion with BST insertion:
- BSTs grow at the bottom
- B-trees may grow at the top
- pre-splitting ensures we never recurse into a full node

That is the major structural difference to remember.

## 18.3 Deletion
Deletion is more complicated because keys may be removed from internal nodes and minimum-degree constraints must stay valid.

### Textbook Cases
1. key is in a leaf -> remove directly
2. key is in an internal node
   - predecessor child has at least t keys
   - successor child has at least t keys
   - both have only `t - 1` keys -> merge
3. key is not in the current node
   - ensure the target child has at least t keys before descending
   - borrow or merge as needed

### Bayer and McCreight (1970) Notes
The lecture and paper summary emphasized the original terminology:
- **catenation** means merge
- **underflow** refers to redistribution rather than a propagating merge
- splitting starts at leaves and may propagate upward
- root split is the only height-increase event
- storage utilization is always at least 50%

The paper also derived an optimal page-size parameter k by balancing disk latency and transfer costs, with practical values around 60-128 in the original IBM setting.

### Lecture Emphasis
The most important idea is not to memorize every delete subcase verbatim. It is to remember the invariant: before descending, ensure the child you are about to recurse into has enough keys so you do not get stuck repairing underflow on the way back up.

---

## Overview
- Chapter 18 covers B-trees, balanced multiway search trees designed to reduce disk/page accesses.
- In CSCI 4041, this chapter connects textbook B-tree invariants to Week 6 code and to the Midterm Multiway Search Tree project option.
- The main conceptual shift from BSTs is that one node stores many ordered keys and has many child intervals.

## Core Definitions
- **Minimum degree `t`:** controls legal node sizes.
- **Full node:** a node with exactly `2t-1` keys.
- **B-tree node:** stores `n`, sorted keys, child pointers, and a leaf flag.
- **B-tree invariants:** all leaves have the same depth; non-root nodes have between `t-1` and `2t-1` keys; internal non-root nodes have between `t` and `2t` children.
- **Page/block motivation:** a node is sized to fit a disk page, so high branching factor lowers the number of page reads.

## Main Algorithms
- `B-TREE-SEARCH`: search within a node, then recurse into one child interval.
- `B-TREE-CREATE`: allocate an empty leaf root.
- `B-TREE-SPLIT-CHILD`: split a full child around its median key.
- `B-TREE-INSERT`: split a full root if necessary, then insert into a non-full node.
- `B-TREE-INSERT-NONFULL`: descend top-down, splitting full children before entering them.
- `B-TREE-DELETE`: preserve enough keys before descent using predecessor/successor replacement, borrowing, or merging.

## Correctness Ideas
- Search correctness follows from the ordered interval property inside each multi-key node.
- Insert correctness depends on never descending into a full node; this guarantees room at the leaf where insertion occurs.
- Root split is the only operation that increases height.
- Delete correctness depends on the strengthened descent invariant: before recursing into a child, ensure it has at least `t` keys when possible.
- Height analysis counts the minimum possible number of keys in a height-`h` B-tree.

## Complexity
- Search, insert, and delete take `O(log_t n)` node visits.
- CPU work per visited node is `O(t)` for linear scan, or `O(lg t)` if keys inside a node are searched by binary search.
- Disk I/O is the real target: high `t` makes height small.
- Space is `Theta(n)` keys plus child pointers; utilization is at least about half full for non-root nodes.

## Lecture Emphasis
- `Lectures/Week - 6/Ch18_B-Tree.ipynb` implements a direct Python version of CLRS Chapter 18 with nested `node` fields `n`, `key`, `c`, and `leaf`.
- The lecture's central bridge is top-down splitting:

```python
if x.c[i].n == 2*self.t - 1:
    self.split(x,i)
    if k > x.key[i]:
        i = i + 1
self.insert_nonfull(x.c[i],k)
```

- The code corresponds to the textbook invariant "do not descend into a full child."
- [[Multiway Search Tree Project|Multiway Search Tree Project]] supports the same multi-key search-tree idea through a 2-3 tree variant and is directly linked to this chapter.
- Weekly/concept links: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]], [[B-Trees|B-Trees]], [[Multiway Search Tree Project|Multiway Search Tree Project]].

## Examples
- For `t=2`, every non-root node has 1 to 3 keys; this is the 2-3-4 tree special case.
- Splitting a full child with keys `[10, 20, 30]` moves `20` up and leaves `[10]` and `[30]` as siblings.
- Search in a node with keys `[20, 50, 80]` descends into one of four intervals: `<20`, `20..50`, `50..80`, or `>80`.

## Connections
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]]
- [[B-Trees|B-Trees]]
- [[Multiway Search Tree Project|Multiway Search Tree Project]]
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13|Chapter - 13]] for binary balanced-tree contrast.
- TODO: source gap - the B-tree lecture code covers search/split/insert strongly; deletion is primarily textbook/PDF-grounded in the notes rather than fully implemented in the lecture notebook.

## Common Pitfalls
- Forgetting the root is allowed to have fewer keys than other nodes.
- Treating a B-tree like a binary tree and following only left/right links.
- Splitting after descent instead of before descent in the CLRS top-down insertion strategy.
- Confusing minimum degree `t` with maximum number of children.
- Memorizing deletion cases without tracking the "child has enough keys before descent" invariant.

## Review Checklist
- [ ] State B-tree node-size and leaf-depth invariants.
- [ ] Trace search through a multi-key node.
- [ ] Implement/simulate split-child and insert-nonfull.
- [ ] Explain why root split is the only height-increase event.
- [ ] Analyze operations in terms of `log_t n` and disk/page accesses.
