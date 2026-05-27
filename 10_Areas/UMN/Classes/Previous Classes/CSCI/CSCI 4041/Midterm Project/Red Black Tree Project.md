---
type: class
input_kind: project
status: sprout
created: 2026-04-27
updated: 2026-04-27
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Project"
related:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Midterm Project|Midterm Project]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 7|Week - 7]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13|Chapter - 13]]"
---
# Red Black Tree Project
## Overview
This project option implements a red-black tree variant based on Sedgewick's left-leaning red-black (LLRB) tree formulation. Instead of the full CLRS 4-case insert and delete fix-ups, the LLRB approach restricts red links to lean left, which simplifies the case analysis. The implementation extends the same `balancedtree` scaffold used by the AVL option.
## Source Files
- `Midterm_Project/Red Black Tree/Ch13_DiChromaticTrees.ipynb` — LLRB tree implementation
- `Midterm_Project/Red Black Tree/Ch12_BinarySearchTree.ipynb` — BST foundation code
- `Midterm_Project/Red Black Tree/Left-Leaning_Red-black_Trees(Sedgewick-2008).pdf` — Sedgewick's 2008 LLRB paper
## Reference Papers
- `A_dichromatic_framework_for_balanced_trees.pdf` — Guibas and Sedgewick's original dichromatic framework
- `Sedgewick-Algorithms-Chapter15.pdf` — Sedgewick's textbook treatment
- `Sedgewick-AlgorithmsinC-Chapter15.pdf` — C implementation reference
## Key Algorithms and Data Structures
- **Red-black tree**: BST with color bits enforcing 5 properties that guarantee $O(\log n)$ height
- **Left-leaning invariant**: red links lean left only, reducing the number of fix-up cases
- **5 red-black properties**: color bit, black root, black NIL leaves, no red-red edge, equal black-height on all root-to-leaf paths
- **`T.nil` sentinel**: simplifies boundary cases by making missing children act as ordinary black nodes
- **Insert fix-up**: recolor and rotate to restore the no-red-red-edge property
- **Delete fix-up**: handle the "extra black" problem when a black node is removed
## Concept Links
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 7|Week - 7]] — red-black trees and AVL project lecture
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]] — balanced trees and rotation primitives
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13|Chapter - 13]] — CLRS red-black tree chapter
- [[AVL Trees|AVL Trees]] — comparison: stricter balance, explicit heights
## Complexity
| Operation | Average | Worst |
|---|---|---|
| Search | $O(\log n)$ | $O(\log n)$ |
| Insert | $O(\log n)$ | $O(\log n)$ |
| Delete | $O(\log n)$ | $O(\log n)$ |
| Space | $O(n)$ | $O(n)$ |

Red-black trees allow slightly more imbalance than AVL (height $\leq 2 \log_2(n+1)$), but insertions and deletions tend to require fewer rotations on average.