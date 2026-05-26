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

# OCaml - If Normalization and Tautology Checking

- The if-based tautology checker rewrites propositions into `If` form, normalizes nested tests, substitutes truth values, and checks whether the result simplifies to `T`.

## 30-Second Explanation
- `Labs/Practice/iffyTaut.ml` represents propositions with `T`, `F`, `V of string`, and `If`. Boolean connectives are encoded using `If`. `makeIf`, `normalize`, `substitute`, and `isTautology` implement the simplification/checking pipeline. `Labs/Practice/tautology.ml` is the brute-force contrast.

## Teach It To A Beginner
- The source first says: instead of keeping separate `And`, `Or`, `Not`, `Imply`, and `Equiv` constructors, encode them as if-then-else. Once everything is in `If` form, the checker can apply a smaller set of rewrite rules.
- `makeIf` is a smart constructor. It simplifies obvious cases while building: `If (T, alpha, beta)` becomes `alpha`, `If (F, alpha, beta)` becomes `beta`, and `If (pi, T, F)` becomes `pi`.

```ocaml
type proposition =
  If of proposition * proposition * proposition
| F
| T
| V of string ;;

let makeIf pi alpha beta =
  match (pi, alpha, beta) with
  | (pi, T, F) -> pi
  | (T, alpha, _) -> alpha
  | (F, _, beta) -> beta
  | _ -> If (pi, alpha, beta) ;;
```

## Definition
- If-normal form: a proposition represented and simplified through nested `If` expressions.
- Smart constructor: a function that builds a value while enforcing simplification rules.
- Tautology: a proposition true under every assignment of its variables.

## Mental Model
- Encode: translate connectives into `If`.
- Normalize: move nested tests out of test position.
- Substitute: replace a chosen variable/test with `T` or `F`.
- Simplify: recursively remove redundant structure.
- Check: tautology iff the simplified normalized proposition is `T`.

## Contrast With
- Brute force in `tautology.ml`: generate all truth assignments, evaluate, and require every result true.
- [[OCaml - Algebraic Data Types and Structural Recursion]]: both approaches recurse over ADTs; if-normalization is a more symbolic transformation.
- [[OCaml - Continuation Passing]]: brute-force `tautology.ml` uses continuation-like generators; `iffyTaut.ml` transforms propositions directly.

## Where It Appears
- Weekly notes: [[Week - 13]], [[Week - 14]], [[Week - 15]].
- Labs/practice: `Labs/Practice/iffyTaut.ml`, `Labs/Practice/tautology.ml`.
- Projects: no project requirement, but it reuses ADT transformation patterns from Project 1 and the interpreter.
- Textbook: Hickey Ch. 3, Ch. 4, Ch. 5, Ch. 6.

## Common Mistakes
- Forgetting that connectives are encoded as `If`, not separate constructors in `iffyTaut.ml`.
- Implementing `makeIf` as a blind constructor with no simplification.
- Substituting non-variable propositions as if they were variables.
- Confusing symbolic simplification with brute-force truth-table generation.

## Diagnostic Questions
- How does `iffyTaut.ml` encode `not alpha`?
- What simplifications does `makeIf` perform?
- What does `normalize` do when the test position is another `If`?
- How is `isEquivalent` defined in the source?

## Mini-Test
- [ ] Encode `a && b` using `If`.
- [ ] Simplify `makeIf T alpha beta`.
- [ ] Explain how brute-force tautology differs from if-normal tautology.

## Flashcards
#cards/CSCI2041
- What constructors represent if-based propositions::`If`, `F`, `T`, and `V`.
- How is negation encoded::`If (alpha, F, T)`.
- What is `makeIf`::A smart constructor for simplified if propositions.
- What does `substitute` replace::A variable proposition with `T` or `F`.
- What does `isTautology` ultimately compare against::`T`.
