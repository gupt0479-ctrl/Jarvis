---
type: concept
course: CSCI 2041
status: sprout
mastery (1/10): 0
created: 2026-05-08
updated: 2026-05-08
topics:
  - "[[CSCI 2041 Board]]"
related:
---
# OCaml - Expression Trees and Equation Solving
- Project 1 solves equations by recursively transforming an expression tree until the target variable is isolated.
## 30-Second Explanation
- `Labs/project-1/expression.ml` defines an `expression` ADT. `project.ml` uses `isInside`, `solver`, and `solve`. The solver does not manipulate strings. It pattern matches on constructors such as `Add`, `Sub`, `Mul`, `Div`, and rewrites the equation using inverse operations.

## Teach It To A Beginner
- An equation is a tree. To solve for `x`, first find which side contains `x`. Then repeatedly look at the outer operation around `x` and move the other part to the opposite side.
- If the left side is `Add (a, b)` and `x` is inside `a`, then `a + b = c` becomes `a = c - b`. That rule is just an expression-tree transformation.
- `Labs/solve.txt` shows the same algorithm in Lisp form, which links Project 1 to the later interpreter material.

```ocaml
| Add (a, b) ->
    if isInside name a then solver name a (Sub (right, b))
    else if isInside name b then solver name b (Sub (right, a))
    else raise (SolvingError "variable not found in either side of addition")
```

## Definition
- Expression tree: an ADT value whose constructors represent variables, unary operations, binary operations, and equations.
- Equation solving by inversion: recursively move operations away from the target variable by applying inverse constructors to the other side.

## Mental Model
- `isInside`: find the target variable.
- `solve`: choose which side of `Equ` to solve.
- `solver`: peel off one outer constructor at a time.
- Error cases: variable absent, variable on both sides, non-equation input, wrong variable.

## Contrast With
- Algebra on strings: this project never edits textual formulas.
- [[OCaml - Algebraic Data Types and Structural Recursion]]: equation solving is a specialized ADT transformation.
- [[OCaml - Lisp Thing Representation]]: both represent symbolic structures; Project 1 uses a domain-specific `expression` type, while Lisp uses `thing`.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 7]], [[Week - 15]].
- Labs: source lives under `Labs/project-1`; no numbered lab note yet.
- Projects: [[Project - 1 Equation Solver]].
- Textbook: Hickey Ch. 4 pattern matching, Ch. 6 unions.

## Common Mistakes
- Searching only one side of a binary expression.
- Forgetting that `Equ` is only valid at the top-level for `solve`, not inside `solver`.
- Moving the wrong expression across the equation.
- Not raising an error when the variable appears on both sides.

## Diagnostic Questions
- What does `isInside` return for `Add (Var "x", Var "y")`?
- What should `solve "x" (Equ (Add (Var "x", Var "b"), Var "c"))` produce?
- Why does division have different rewrite rules depending on whether the variable is in numerator or denominator?
- What does `Labs/solve.txt` confirm about the algorithm?

## Mini-Test
- [ ] Solve `x + b = c` as an expression tree.
- [ ] Solve `a / x = c` as an expression tree.
- [ ] Identify all Project 1 `SolvingError` cases.

## Flashcards
#cards/CSCI2041
- What type represents Project 1 formulas::`expression`.
- What does `isInside` test::Whether a variable occurs in an expression tree.
- What does `solver` repeatedly do::Peels outer operations away from the target variable.
- Why is Project 1 structural recursion::It pattern matches on expression constructors.
- What linked Lisp file shows the same algorithm::`Labs/solve.txt`.
