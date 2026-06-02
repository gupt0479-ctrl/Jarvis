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

# OCaml - Interpreter Primitives and Special Forms

- A primitive is built into the evaluator as an OCaml function; a special form controls whether and when its arguments are evaluated.

## 30-Second Explanation
- Lab 11 stores built-ins as `Primitive of (thing -> environment -> thing)`. Arithmetic and relation helpers evaluate their arguments normally. But `and`, `or`, `if`, `quote`, `define`, `lambda`, `imply`, and `let` have special rules, so their primitive functions receive raw argument structure and decide what to evaluate.

## Teach It To A Beginner
- In ordinary function calls, you might expect every argument to be evaluated first. Lisp special forms break that expectation. `quote` returns its argument without evaluation. `if` evaluates only the selected branch. `and` and `or` short-circuit. `lambda` does not evaluate its parameter list or body immediately.
- This is why a primitive function receives both `args` and `env`. It needs the raw Lisp argument list and the environment to evaluate the pieces it chooses.

```ocaml
primitive "or"
  (fun args env ->
    let rec oring args =
      match args with
      | Nil -> Nil
      | Cons (arg, Nil) -> evaluating arg env
      | Cons (arg, args) ->
          let value = evaluating arg env in
          if value = Nil then oring args else value
      | _ -> oops "OR expected zero or more arguments"
    in
    oring args) ;;
```

## Definition
- Primitive: a built-in Lisp operation represented by an OCaml function inside `Primitive`.
- Special form: an operation whose arguments are not all evaluated before the operation runs.
- Short-circuit evaluation: stopping argument evaluation once the result is determined.

## Mental Model
- Arithmetic primitive: evaluate both numbers, compute.
- Relation primitive: evaluate both numbers, return `t` or `Nil`.
- `quote`: evaluate nothing inside.
- `if`: evaluate test, then one branch.
- `and`/`or`/`imply`: evaluate left to right and may stop early.

## Contrast With
- [[OCaml - Lisp Evaluator]]: evaluator dispatches; primitives implement built-in behavior.
- [[OCaml - Higher-Order Functions]]: primitive builders are higher-order helpers.
- User closures: closures use `apply`; primitives run their stored OCaml function.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[Week - 15]].
- Labs: [[Lab - 11 Lisp Evaluator]], [[Lab - 12 Lisp Integration]].
- Projects: Project 2 parser creates input structures that these primitives later evaluate.
- Textbook: Hickey Ch. 3, Ch. 4, Ch. 9.

## Common Mistakes
- Evaluating both branches of `if`.
- Evaluating the argument to `quote`.
- Making `and`, `or`, or `imply` evaluate after the answer is already determined.
- Forgetting arity/type error cases in primitive functions.

## Diagnostic Questions
- Why does `Primitive howTo` receive raw `args`?
- Why should `(imply nil (/ 0 0))` return `t` instead of dividing by zero?
- What does `makeArithmetic` abstract?
- What does `makeRelation` abstract?

## Mini-Test
- [ ] Trace `(and t nil (/ 0 0))`.
- [ ] Trace `(or nil (quote a) (/ 0 0))`.
- [ ] Explain why `lambda` is not an ordinary arithmetic-style primitive.

## Flashcards
#cards/CSCI2041
- What does `Primitive` contain::An OCaml function from args and environment to `thing`.
- Which primitive prevents evaluation of its argument::`quote`.
- Which primitive mutates global environment::`define`.
- Why do `and` and `or` short-circuit::Their result may be known before all arguments are evaluated.
- What does `makeRelation` return::A comparison primitive.
