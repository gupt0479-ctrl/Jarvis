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
  - "[[OCaml - Environments and Closures]]"
  - "[[OCaml - Interpreter Primitives and Special Forms]]"
  - "[[OCaml - Lisp Thing Representation]]"
---

# OCaml - Lisp Evaluator

## One-Line Answer
The evaluator maps a Lisp `thing` to its value by dispatching on constructor shape: look up symbols, apply closures/primitives for calls, return everything else as-is.

## 30-Second Explanation
`evaluating thing env` is the dispatcher. A `Symbol` is looked up. A `Cons (func, args)` is a call: evaluate `func`, then either run a `Primitive howTo` or `apply` a `Closure`. Numbers, `Nil`, closures, and primitives evaluate to themselves.

## OCaml Shape
```ocaml
let rec evaluating thing env =
  match thing with
  | Cons (func, args) ->
      (match evaluating func env with
       | Closure (pars, body, bodyEnv) -> apply pars args env body bodyEnv
       | Primitive howTo -> howTo args env
       | _ -> oops "Closure or primitive expected")
  | Symbol name -> lookup env name
  | _ -> thing
```

## Mental Model
- Atom? Return it or look it up.
- List? Treat as a call.
- Function position must become `Primitive` or `Closure`.
- Arguments? Evaluation depends on the function's rules (primitives decide their own).

## Contrast With
- **[[OCaml - Recursive Descent Parsing]]**: parser builds structure; evaluator gives structure meaning.
- **[[OCaml - Lisp Printer]]**: printer displays values; evaluator computes them.
- **[[OCaml - Interpreter Primitives and Special Forms]]**: primitives supply built-in meanings; evaluator dispatches to them.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13]], [[Week - 15]].
- Labs: Lab 11 (`lab11.ml`, `tests11.ml`), Lab 12 (`lab12.ml`).
- Textbook: Hickey Ch. 3, Ch. 4, Ch. 6, Ch. 9, Ch. 11-12.

## Common Mistakes
- Evaluating all arguments before checking primitive behavior (breaks `and`, `or`, `if`, `quote`).
- Treating every `Cons` as a list literal instead of a function call.
- Forgetting local-before-global lookup order.
- Not raising an error when function position is not a closure or primitive.
- Evaluating closure body in the caller's environment instead of the closure's saved environment.

## Diagnostic Questions
- What does a `Number` evaluate to? (itself)
- What does a `Symbol` evaluate to? (whatever the environment says)
- What happens when function position evaluates to `Primitive howTo`? (call `howTo args env`)
- What happens when function position evaluates to `Closure`? (call `apply`)
- Why does `(1 2)` fail? (1 evaluates to `Number 1`, which is neither `Primitive` nor `Closure`)

## Flashcards
#cards/CSCI2041
- What is the evaluator dispatcher called::`evaluating`.
- What does a symbol evaluation do::Looks up the symbol's binding in the environment (local first, then global).
- What does a `Cons` mean to the evaluator::A function call — evaluate the first element, apply it to the rest.
- What two function-like values can be applied::`Primitive` and `Closure`.
- What evaluates to itself::`Number`, `Nil`, `Closure`, and `Primitive`.
