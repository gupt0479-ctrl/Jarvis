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

# OCaml - References and Mutation

- A reference cell stores a value that can be changed later; the course uses it when the program really has moving state.

## 30-Second Explanation
- Week 6 onward uses mutation in specific places: `Hashtbl.add` updates a memo table in Lab 6, scanner state uses `input` and `ch` refs, the parser keeps a current-token ref, and the evaluator's `global` environment is a ref so `define` can add global bindings. Mutation is not the default style; it appears when the source has a sequential cursor or global language state.

## Teach It To A Beginner
- Most OCaml values in the course are built and passed forward. A ref is different: it is a box. You can read the box with `!box` and replace its contents with `box := new_value`.
- Scanners need a box because reading characters moves through a file. Evaluators need a global box because `(define x 3)` should affect later expressions. Memoization needs a table because later recursive calls should see answers computed earlier.
- Textbook connection: Hickey Ch. 7 is the key chapter for reference cells and side effects.

```ocaml
let input = ref stdin ;;
let ch = ref ' ' ;;

let nextChar () =
  try ch := input_char !input
  with End_of_file -> ch := '\000' ;;
```

## Definition
- A reference cell is a mutable container.
- `ref value` creates a cell.
- `!cell` reads a cell.
- `cell := value` updates a cell.

## Mental Model
- Immutable binding: the name points to a value.
- Reference binding: the name points to a box; the box's contents can change.
- Course rule of thumb: use refs for moving cursors, caches, and persistent interpreter state.

## Contrast With
- [[OCaml - Memoization]]: memoization is one use of mutation through a cache.
- [[OCaml - Environments and Closures]]: most local environments are immutable association lists; only `global` is a ref.
- [[OCaml - Lazy Evaluation]]: laziness may hide computation timing; refs make state changes explicit.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 7]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 10]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[Week - 15]].
- Labs: [[Lab - 6 Memoization]], [[Lab - 11 Lisp Evaluator]], [[Lab - 12 Lisp Integration]].
- Projects: [[Project - 2 Lisp Parser]] uses scanner/parser cursor state.
- Textbook: Hickey Ch. 7.

## Common Mistakes
- Forgetting `!` when reading from a ref.
- Accidentally creating a new ref when the code should update an existing ref.
- Treating the global environment like an ordinary local value.
- Mutating local state where a recursive parameter would be clearer.

## Diagnostic Questions
- Why does `Scanner.nextToken` need to remember `ch`?
- Why is `global` a ref but local environment lists are not?
- What does `global := envPut name value (!global)` do?
- What is the difference between `env` and `!global`?

## Mini-Test
- [ ] Explain each ref in the scanner.
- [ ] Trace how `define` changes the evaluator's global environment.
- [ ] Identify where mutation is necessary versus merely convenient.

## Flashcards
#cards/CSCI2041
- How do you create a ref::`ref value`.
- How do you read a ref::With `!`.
- How do you update a ref::With `:=`.
- Why is scanner state mutable::It tracks a moving position through input.
- Why is the evaluator global environment mutable::`define` must affect later evaluations.
