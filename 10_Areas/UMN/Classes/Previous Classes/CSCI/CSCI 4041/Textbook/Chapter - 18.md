---
type: class
input_kind: book
status: sprout
created: 2026-02-25
updated: 2026-04-16
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]]"
---
# Chapter - 18 B-trees
## Summary Links
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 6#Chapter 13 and Chapter 18 - Balanced Trees, Rotations, and B-Trees|Week - 6]]
- [[B-Trees#Definition|B-Trees]]
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Trees/AVL Trees#Complexity + Tradeoffs|AVL Trees - Complexity + Tradeoffs]]

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
