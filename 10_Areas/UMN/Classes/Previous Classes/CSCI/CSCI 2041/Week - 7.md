---
type: class
input_kind: lecture
status: sprout
created: 2026-05-08
updated: 2026-05-12
area:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Memoization]]"
  - "[[OCaml - Expression Trees and Equation Solving]]"
  - "[[OCaml - Lazy Evaluation]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 8]]"
---
# Entire Week
## What you must be able to do
- Explain why `c 40 10` is slow (repeated subproblems) and `memyC 40 10` is fast (cached results).
- Use a mutable `Hashtbl` as a cache without confusing mutation with the mathematical recurrence.
- Trace Project 1's `isInside`, `solver`, and `solve` in `Labs/project-1/project.ml`.
- State the inverse rule for each binary constructor (`Add`, `Sub`, `Mul`, `Div`) — both sides.
- Explain the first lazy-list representation in `Labs/lab7.ml`.

## Key ideas (textbook)
- Hickey Ch. 7 `Reference cells and side-effects`: memoization is controlled mutation. The function still represents a recurrence, but stores already-computed results.
- Hickey Ch. 8 `Hash tables`: `Hashtbl` gives the lab a mutable lookup table keyed by `(n, k)`.
- Hickey Ch. 6 `Unions`: Project 1's `expression` type is an ADT with constructors for variables, negation, binary arithmetic, and equality.
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4|Ch. 4]] `Pattern matching`: Project 1 dispatches on the outer constructor. The recursive solver is mostly a pattern matching problem.

## Concepts created / updated today
- [[OCaml - Memoization]]
- [[OCaml - References and Mutation]]
- [[OCaml - Expression Trees and Equation Solving]]
- [[OCaml - Algebraic Data Types and Structural Recursion]]
- [[OCaml - Lazy Evaluation]]

## Lecture
### Week 7 lecture map - project equations, memoization, and delayed tails
Week 7 has three connected threads. Project 1 makes recursive data transformation concrete. Lab 6 shows why repeated recursion can be operationally terrible even when the recurrence is mathematically clean. Lab 7 then sets up delayed computation with `Lazy.t`.

Source anchors:
- `Lecture - 15.txt` announces Project 1 and emphasizes that projects differ from labs: individual work, no supplied test-case safety net, and code read by TAs.
- Project files `Labs/project-1/expression.ml`, `project.ml`, and `modStack.ml` define an equation as a recursive expression tree and solve it by inverse transformations.
- `Lecture - 16.txt` asks whether a function can be automatically memoized. The answer is "yes, sort of," with OCaml's type system limiting how general the version can be.
- `Labs/lab6.ml` is the concrete memoization source: plain `c` recomputes binomial subproblems; `memyC` stores results in a local hash table keyed by `(n, k)`.
- `Lecture - 17.txt` returns to evaluation strategies and sets up lazy lists. It also stresses that Project 1 debugging requires students to invent their own tests.

Read the week as a control-flow story:
1. Project 1: recursively walk an expression tree until the variable is isolated.
2. Memoization: keep the same recurrence but change the execution path by caching completed calls.
3. Lazy lists: delay recursive tails so a list can describe more than it immediately computes.

### Mar 2 — Project 1 and Post-Midterm Transition
Sources: `Lecture - 15.txt`, professor notes `02Mar26/`, `Labs/project-1/expression.ml`, `Labs/project-1/project.ml`, `Labs/solve.txt`.

The lecture starts after the midterm and announces Project 1. The professor stresses that projects are not labs: they count more, must be individual, and do not arrive with a friendly test suite. The practical implication for the note system is that Project 1 should be studied by its data model and transformations, not by memorizing examples.

Project 1 represents equations as recursive trees, not strings:
```ocaml
type expression =
  Var of string | Neg of expression
| Add of expression * expression | Sub of expression * expression
| Mul of expression * expression | Div of expression * expression
| Equ of expression * expression ;;
```

Solving is structural recursion over this tree. `isInside name expr` checks whether the variable occurs anywhere in a subtree. Then `solver name left right` repeatedly peels the outer constructor by applying the inverse operation.

**The recurring rule:** inspect the outer constructor, decide which side contains the variable, apply the inverse to the other side. Example: `Add (a, b) = right` and variable is in `a` → rewrite as `a = Sub (right, b)`.

`Labs/solve.txt` shows the same algorithm in Lisp. This confirms Project 1 is part of the course's larger theme: represent programs/data as trees, transform them recursively.

### Mar 4 — Memoization
Sources: `Lecture - 16.txt`, professor notes `04Mar26/`, `Labs/lab6.ml`, `Labs/tests6.ml`, Hickey Ch. 7.

The lecture question is: can we automatically memoize a function? The answer is "yes, sort of." OCaml's type system makes a completely general memoizer awkward, but the lab's binomial example is enough to show the mechanism. The cache is operational; it changes how much work the recurrence does, not what recurrence is being computed.

Plain binomial coefficients:
```ocaml
let rec c n k =
  if k = 0 || k = n then 1
  else c (n - 1) (k - 1) + c (n - 1) k ;;
```

Mathematically simple, computationally wasteful. Same `c n k` values appear repeatedly in the recursion tree.

`memyC` fixes this: create a table, check first, store after computing. The recurrence stays identical — only the operational path changes.

**Common mistake:** thinking memoization changes the answer. If a memoized function returns a different value than the plain recurrence, the cache key or stored value is wrong.

### Mar 6 — Lazy-List Setup
Sources: `Lecture - 17.txt`, professor notes `06Mar26/`, `Labs/lab7.ml`, `Labs/tests7.ml`.

The lecture returns to evaluation strategies and reminds students that Project 1 requires self-made tests. This is a recurring course habit: if the code manipulates recursive structures, the student is responsible for testing shallow cases, deep nested cases, and error cases.

```ocaml
type 'a lazyList =
  LazyEmpty |
  LazyNode of 'a * 'a lazyList Lazy.t ;;
```

The tail is not an ordinary list — it's delayed. `lazyTail` must force that delayed value before returning it. A lazy list is not "a normal list that is large." It's a list whose tail computation is suspended until demanded.

## Labs / Projects
### Lab 6 — Memoized Binomial Coefficients
Source: `Labs/lab6.ml` | Tests: `Labs/tests6.ml`

Tests plain `c` against memoized `memyC`. Cache keyed by `(n, k)` using `Hashtbl`. Tests compare timing for `c 40 10` vs `memyC 40 10`.

Concepts: [[OCaml - Memoization]], [[OCaml - References and Mutation]]

### Project 1 — Equation Solver
See: [[Project - 1 Equation Solver|Project - 1 Equation Solver]]

Uses ADTs, pattern matching, recursion, exceptions, and expression transformation.

## Examples worth keeping
- `isInside name (Add (l, r)) = isInside name l || isInside name r` — structural search.
- `Add (a, b)` solving rule: variable in `a` → `a = Sub (right, b)`.
- `c n k` — simple recurrence with repeated subproblems.
- `memyC` — same recurrence + mutable table.
- `LazyNode (head, lazy tail)` — lazy list node shape.

## Takeaways (questions to resolve)
- [ ] What is the cache key in `memyC`? (`(n, k)` pair)
- [ ] Why does memoization preserve the recurrence's answer?
- [ ] Which Project 1 constructors are unary vs binary?
- [ ] How does `isInside` decide which side to solve?
- [ ] When does a lazy-list tail actually get computed? (when `Lazy.force` is called)

## Flashcards
#cards/CSCI2041
- What does memoization store::Previously computed results keyed by input, so repeated calls return cached values instead of recomputing.
- Why is plain recursive `c 40 10` slow::The recursion tree recomputes the same `(n, k)` subproblems exponentially many times.
- What does `isInside` do in Project 1::Structural recursion checking whether `Var name` appears anywhere inside an expression tree.
- What is the inverse rule for `Add (a, b) = right` when variable is in `a`::`a = Sub (right, b)`.
- What is delayed in `LazyNode`::The tail — it's wrapped in `Lazy.t` and only computed when forced.
