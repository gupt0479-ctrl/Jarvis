---
type: class
input_kind: project
status: sprout
created: 2026-04-27
updated: 2026-04-27
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Concepts/Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Project"
related:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Midterm Project|Midterm Project]]"
  - "[[AVL Trees|AVL Trees]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 7|Week - 7]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13|Chapter - 13]]"
---
# AVL Tree Project
## Overview
This was the user's chosen midterm project option. The project implements an AVL tree by extending a `balancedtree` scaffold, adding height-based rebalancing with the four standard rotation cases (LL, RR, LR, RL). The implementation includes insertion, deletion, and a stress-test validation suite that checks inorder order, AVL balance factors, parent pointer consistency, and stored-height correctness.
## Source Files
- `Midterm_Project/AVL Tree/AVLTree.ipynb` — main implementation extending the balanced tree scaffold
- `Midterm_Project/AVL Tree/Experiment.ipynb` — stress tests with 600 mixed insert/delete operations, trigger sequences, and validation checks
- `Midterm_Project/AVL Tree/Ch12_BinarySearchTree.ipynb` — BST foundation code
- `Midterm_Project/AVL Tree/Ch13_BalancedSearchTrees.ipynb` — balanced tree scaffold and rotation primitives
- `Midterm_Project/AVL Tree/CSCI 4041 Midterm Project - Balanced Tree Report.pdf` — project report
## Reference Papers
- `AVL-tree(original).pdf` — Adelson-Velsky and Landis original 1962 paper
- `AVL tree paper.pdf` — supplementary AVL reference
- `ArtofComputerProgrammingVol3-BalancedTreesMultiwayTrees.pdf` — Knuth's treatment of balanced trees
- `DataStructuresandAlgorithmsinPython-Chapter11.pdf` — Python-oriented AVL reference
## Key Algorithms and Data Structures
- **AVL Tree**: height-balanced BST where every node's left and right subtree heights differ by at most 1
- **Rotations**: left rotate, right rotate, and the four trigger cases:
  - LL: `[30, 20, 10]` → right rotate at 30
  - RR: `[10, 20, 30]` → left rotate at 10
  - LR: `[30, 10, 20]` → left rotate at 10, then right rotate at 30
  - RL: `[10, 30, 20]` → right rotate at 30, then left rotate at 10
- **Fix-up walk**: after insert or delete, walk upward from the mutation site, recompute heights, and rotate where `|balance factor| == 2`
- **Validation suite**: inorder sorted check, AVL balance check, parent pointer check, stored height vs computed height check
## Concept Links
- [[AVL Trees|AVL Trees]] — full concept note with textbook theory and lecture code
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]] — balanced trees, rotations, B-Trees lecture
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 7|Week - 7]] — red-black trees and AVL project work
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 13|Chapter - 13]] — red-black trees (rotation primitives shared with AVL)
## Complexity
| Operation | Average | Worst |
|---|---|---|
| Search | $O(\log n)$ | $O(\log n)$ |
| Insert | $O(\log n)$ | $O(\log n)$ |
| Delete | $O(\log n)$ | $O(\log n)$ |
| Space | $O(n)$ | $O(n)$ |

AVL trees are more tightly balanced than red-black trees (height $\leq 1.44 \log_2(n+2)$), so lookups are faster in practice, but insertions and deletions may require more rotations.