---
type: class
input_kind: lecture
status: sprout
created: 2026-03-02
updated: 2026-04-16
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 8|Week - 8]]"
---
# Entire Week
## What you must be able to do
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13#13.1 Properties of Red-Black Trees|Chapter - 13 red-black properties]], [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13#13.3 Insertion|RB insert]], and [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13#13.4 Deletion|RB delete]]: know the 5 properties, black-height idea, `T.nil`, and the high-level fix-up cases for insert/delete.
- [[AVL Trees#Core Ideas (Lecture)|AVL Trees - Core Ideas (Lecture)]], [[AVL Trees#Canonical Examples (Max 5)|AVL Trees - Canonical Examples]], and [[AVL Trees#Proof / Reasoning Toolkit|AVL Trees - Proof / Reasoning Toolkit]]: explain the AVL project implementation, the four rotation triggers, and the validation checks.
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6#Chapter 13 and Chapter 18 - Balanced Trees, Rotations, and B-Trees|Week - 6]] and [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13#AVL Notes Anchored to Chapter 13|Chapter - 13 - AVL notes anchored to Chapter 13]]: connect the red-black chapter invariants to the AVL project's stricter balance condition.
- [[AVL Trees#Practice Map|AVL Trees - Practice Map]]: height-balanced checks, rotations, and validation drills remain open.

## Key ideas (textbook)
- **Red-black trees encode balance indirectly.** Instead of storing subtree heights, they constrain coloring so the height can never grow beyond twice the black-height. That is enough to guarantee logarithmic operations.
- **`T.nil` matters because it simplifies every boundary case.** The sentinel means leaves and the root's parent all behave like ordinary black nodes in the code.
- **Insert and delete fix-ups are case analysis around local violations.** Insert mainly repairs red-red problems. Delete repairs the "extra black" problem created when a black node is removed or moved.
- **AVL trees are a stricter balancing strategy built on the same rotation primitive.** They use height differences directly, so the tree stays more tightly balanced at the cost of more explicit bookkeeping.
- **The project work turns theory into correctness checks.** Once you implement rotations and rebalancing, you need invariants like "parent pointers are consistent" and "stored heights match computed heights" to trust the tree.

## Concepts created / updated today
- [[AVL Trees#Definition|AVL Trees]]
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13#13.4 Deletion|Chapter - 13 - RB delete]]
- [[AVL Trees#Mini-test|AVL Trees - Mini-test]]

## Lecture
### Chapter 13 and AVL Project Notes - Red-Black Trees and AVL Validation
This week had two layers. The textbook layer was red-black trees: 5 properties, black-height, sentinel leaves, insertion fix-up, and the extra-black idea in deletion. The project layer was the AVL tree implementation, which is stricter and easier to debug numerically because every node carries a stored height. The lecture used those two layers together rather than treating them as separate units. Red-black trees explain why rotations are enough to restore balance without rebuilding a tree from scratch, and the AVL project shows how those same rotations look in a concrete Python implementation with direct correctness checks.

The red-black side of the week is about invariants. Property 4 forbids red-red edges, Property 5 equalizes black-height, and `T.nil` lets the code treat missing children as actual black nodes. The lecture's big simplification was to talk about deletion through the "extra black" concept rather than through raw pointer updates. That turns the problem into a local imbalance that can be pushed upward or canceled by recoloring and rotation.

The AVL project side made the invariants computational. The four trigger sequences `[30,20,10]`, `[10,20,30]`, `[30,10,20]`, and `[10,30,20]` are worth memorizing because they map directly onto LL, RR, LR, and RL. But more important than memorizing the sequences is understanding how the project checks itself. The stress-test code does not trust one invariant alone. It checks that inorder traversal is sorted, that every local balance factor is valid, that parent pointers are consistent in both directions, and that the stored height field actually equals the recomputed height. That is the right mental model for debugging a tree implementation: never rely on just one visible symptom.

### Jupyter Notebook Explanations
#### AVLTree.ipynb
This notebook contains the project implementation that extends the `balancedtree` scaffold.

```python
def _balance_factor(x):
    L, R = self.compute_height(x)
    return L - R
```

```python
def _fix_up(x):
    while x:
        self.update_height(x)
        bf = self._balance_factor(x)
        # if |bf| == 2, choose LL/RR/LR/RL rotation case
        x = x.p
```

This is the conceptual heart of the implementation. `_fix_up` walks upward from the mutation site, recomputes local height information, and decides whether a rotation is needed. The repair is local, but the reason we walk upward is that only ancestors of the changed node can have had their subtree height altered.

#### Experiment.ipynb
This notebook supplied the most useful test scenarios.

```python
def insertion_seq(n):
    keys = list(range(1, n + 1))
    result = []
    def pick(arr):
        if not arr:
            return
        mid = len(arr) // 2
        result.append(arr[mid])
        pick(arr[:mid])
        pick(arr[mid + 1:])
    pick(keys)
    return result
```

This sequence creates a nearly ideal insertion order that triggers zero rotations because the tree stays balanced as it grows. The lecture paired that with the ascending and descending worst cases, which trigger repeated RR or LL repairs.

The same notebook also used:
- `random.seed(4041)`
- 600 mixed insert/delete operations
- key space 200
- 60% insert and 40% delete

That stress test is valuable because it checks behavior beyond toy trigger sequences.

#### Red-Black Tree Chapter Context
Even though the AVL project was the visible coding work this week, the chapter context still mattered:
- 5 red-black properties
- black-height
- `T.nil`
- insert fix-up's 3-case structure
- delete fix-up's 4-case structure

Those give the conceptual reason balanced trees can guarantee logarithmic height without storing full subtree metrics at every node.

## Examples worth keeping
- **LL trigger:** `[30,20,10]` -> right rotate at 30.
- **RR trigger:** `[10,20,30]` -> left rotate at 10.
- **LR trigger:** `[30,10,20]` -> left rotate at 10, then right rotate at 30.
- **RL trigger:** `[10,30,20]` -> right rotate at 30, then left rotate at 10.
- **Stress-test checklist:** inorder sorted, AVL balance valid, parent pointers correct, stored heights correct.

## Takeaways (questions to resolve)
- [ ] How does red-black black-height compare to AVL's explicit height difference?
- [ ] Why does the AVL fix-up walk upward from the mutation site?
- [ ] Why is checking parent pointers a separate invariant from checking BST order?
- [ ] What exactly does the extra-black idea mean during red-black deletion?
- [ ] Why do the best-case AVL insert sequences cause zero rotations?

## Flashcards
#cards/CSCI4041
1. Five red-black properties summary::color bit, black root, black NIL leaves, no red-red edge, equal black-height on all root-to-leaf paths.
2. What is black-height::The number of black nodes on a path from a node to a descendant leaf, not counting the node itself.
3. AVL LL trigger sequence::`[30, 20, 10]`.
4. AVL RL repair::Right rotate the right child, then left rotate the imbalanced node.
5. Why does the AVL project store heights::To compute balance factors and detect imbalance directly.
6. What does `check_parent_pointers` verify::That every child points back to the correct parent.
7. Why use `T.nil` in red-black trees::It removes special NIL cases by making missing children act like ordinary black sentinel nodes.
