---
type: concept
course: CSCI 2041
status: sprout
mastery (1/10): 0
created: 2026-05-08
updated: 2026-05-09
topics:
  - "[[CSCI 2041 Board]]"
related:
  - "[[OCaml - Streams]]"
  - "[[OCaml - Interpreter Primitives and Special Forms]]"
  - "[[OCaml - Continuation Passing]]"
---

# OCaml - Higher-Order Functions

## One-Line Answer
A higher-order function takes a function as an argument, returns a function, or stores a function inside data.

## 30-Second Explanation
Week 6 onward uses functions as data constantly: streams store a `next` function; `Primitive` stores an OCaml function inside a Lisp value; `makeArithmetic` and `makeRelation` build primitive functions from operators; generators call continuations. Hickey Ch. 3 is the root source.

```ocaml
let makeRelation op message =
  fun args env ->
    match args with
    | Cons (left, Cons (right, Nil)) ->
        (* evaluate both, then apply op *)
        if op left right then Symbol "t" else Nil
    | _ -> raise (Failure message) ;;
```

## Definition
- A higher-order function is a function whose inputs or outputs include functions.
- A first-class function is a function that can be bound, passed, returned, or stored like any other value.

## Mental Model
- Function as button: ordinary call.
- Function as part: stream stores `next`.
- Function as recipe factory: `makeArithmetic` and `makeRelation` return new primitive functions.
- Function as callback: `time`, `generatePairs`, `indexes`, and `permute` call a function supplied by the caller.

## Contrast With
- [[OCaml - Continuation Passing]]: CPS is a particular higher-order style where the extra function means "what to do next."
- [[OCaml - Interpreter Primitives and Special Forms]]: interpreter primitives are higher-order data in the `Primitive` constructor.
- Plain recursion: recursion calls itself; higher-order code receives or returns behavior.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 6]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 7]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 14]], [[Week - 15]].
- Labs: Lab 5 (streams), Lab 6 (memoization), Lab 11 (evaluator primitives).
- Projects: Project 2 indirectly through `Primitive` in shared `thing`.
- Textbook: Hickey Ch. 3.

## Common Mistakes
- Calling a function too early instead of passing it.
- Forgetting that `Primitive howTo` wraps an OCaml function, not a Lisp expression.
- Duplicating primitive implementations instead of using a builder like `makeRelation`.
- Confusing a function argument with an already-computed value.

## Diagnostic Questions
- Where is a function stored in Lab 5 streams?
- What does `Primitive of (thing -> environment -> thing)` mean?
- Why are `makeArithmetic` and `makeRelation` higher-order helpers?

## Flashcards
#cards/CSCI2041
- What is a higher-order function::A function that takes or returns a function.
- Where does Lab 5 store a function::Inside the stream pair as `next`.
- What does `Primitive` store::An OCaml function from arguments and environment to a Lisp value.
- Why is `makeRelation` higher-order::It takes an OCaml comparison operator and returns a complete primitive function.
