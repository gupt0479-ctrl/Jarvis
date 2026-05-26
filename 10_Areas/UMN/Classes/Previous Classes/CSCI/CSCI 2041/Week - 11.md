---
type: class
input_kind: lecture
status: sprout
created: 2026-05-08
updated: 2026-05-12
area:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Lisp Printer]]"
  - "[[OCaml - Interpreter Primitives and Special Forms]]"
  - "[[OCaml - Mutual Recursion]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 12]]"
---
# Entire Week
## What you must be able to do
- Explain what Project 2 asks the parser to do.
- Trace mutually recursive printer functions (`printThing`, `printingThing`, `printingThings`).
- Explain evaluator primitives as OCaml functions wrapped in `Primitive`.
- Explain how `and` and `or` short-circuit.
- Explain `car`, `cdr`, `cons` on `Cons` structures.
- Explain why higher-order helper builders (`makeRelation`, `makeArithmetic`) remove repeated code.

## Key ideas (textbook)
- Hickey Ch. 3: primitive builders are higher-order functions — they return functions sharing an argument-checking pattern.
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4|Ch. 4]]: printers and primitives dispatch on `thing` constructors.
- Hickey Ch. 9: evaluator/printer errors reported through exceptions.
- Hickey Ch. 11-12: printer, parser, scanner, evaluator are separate module-shaped pieces.

## Concepts created / updated today
- [[OCaml - Lisp Printer]]
- [[OCaml - Interpreter Primitives and Special Forms]]
- [[OCaml - Higher-Order Functions]]
- [[OCaml - Mutual Recursion]]

## Lecture
### Week 11 lecture map - printing and primitive evaluation
Week 11 builds two interpreter pieces that point in opposite directions. Lab 10 prints `thing` values back into Lisp-like output. The evaluator lectures start turning `thing` expressions into values by dispatching to primitives and closures.

Source anchors:
- `Lecture - 27.txt` connects Project 2 to Lab 10: after parsing Lisp expressions into internal `thing` values, the course needs a printer for those values.
- `Labs/lab10.ml` uses three mutually recursive functions: `printThing`, `printingThing`, and `printingThings`. A `thing` can be a list, and a list contains more things.
- `Lecture - 28.txt` begins evaluator primitives. A primitive is an OCaml function wrapped as a Lisp value, with access to the unevaluated argument list and environment.
- `Lecture - 29.txt` and the duplicate `Lecture - 30.txt` cover `cdr`, `cons`, numeric predicates, and higher-order builders that avoid repeated primitive code.
- `Labs/lab11.ml` gives the concrete evaluator implementation for `Primitive`, `makeArithmetic`, `makeRelation`, `primitive`, `and`, `or`, `car`, `cdr`, `cons`, and related forms.

The final-exam distinction:
- Ordinary arithmetic and relation primitives evaluate their arguments before operating.
- Special forms such as `and`, `or`, `if`, `quote`, `define`, and `lambda` cannot simply evaluate everything first.
- That is why `Primitive of (thing -> environment -> thing)` receives the raw argument list and environment.

### Apr 6 — Project 2 and Printing Lisp Expressions
Sources: `Lecture - 27.txt`, professor notes `06Apr26/`, `Labs/lab10.ml`, `Labs/tests10.ml`.

The lecture announces Project 2 as code that reads Lisp expressions and returns internal form, using the scanner already provided on Canvas. Lab 10 is paired with that project: if Project 2 reads external Lisp syntax into `thing`, Lab 10 prints internal `thing` values back out.

The printer is a source-grounded mutual-recursion example. `printingThing` knows how to print one `thing`; `printingThings` knows how to print the sequence inside a proper Lisp list. They need each other because lists contain things and things may themselves be lists.

Project 2 announced as parser work. Lab 10 is the opposite direction: printing `thing` → visible output.

Lab 10 uses mutual recursion:
```ocaml
let rec printThing thing =
  printingThing thing; printf "\n"
and printingThing thing = ...
and printingThings things = ...
```

`printingThing` handles one object. `printingThings` handles the inside of a list. They call each other because a list contains things, and a thing may itself be a list.

**Common mistake:** printing `Cons` as an OCaml pair. The course wants Lisp notation — proper `Cons` chain prints inside parentheses with spaces between elements.

### Apr 8 — Evaluator Primitives
Sources: `Lecture - 28.txt`, professor notes `08Apr26/`, `Labs/lab11.ml`.

The evaluator lecture continues the bottom-up construction from Week 10. The global environment is a mutable reference because primitives and definitions are installed over time. Initially the global environment binds `nil` and `t`; then the helper `primitive` adds built-in functions by binding names to `Primitive howTo` values.

A primitive receives the raw Lisp argument list and the current environment. This is deliberate: some primitives must choose whether to evaluate arguments at all. `quote` evaluates none, `if` evaluates only one branch, `and` and `or` short-circuit.

A primitive in the evaluator:
```ocaml
Primitive of (thing -> environment -> thing)
```

The primitive receives *unevaluated* argument structure and an environment. It decides which arguments to evaluate and in what order. That's why `and`, `or`, `if`, `quote` are special — they have non-standard evaluation rules.

- **`and`**: evaluates left to right, stops at `Nil`.
- **`or`**: evaluates left to right, stops at first non-`Nil`.
- If these evaluated all arguments first, they wouldn't short-circuit.

### Apr 10 — `car`, `cdr`, `cons`, and Higher-Order Builders
Sources: `Lecture - 29.txt` (`Lecture - 30.txt` is duplicate by hash), professor notes `10Apr26/`, `Labs/lab11.ml`.

The professor's reason for higher-order primitive builders is boredom avoidance, but the mechanism is serious. Numeric relation primitives all have the same control flow: evaluate two arguments, require numbers, apply an OCaml comparison, and return `t` or `nil`. `makeRelation` captures the shared control flow and takes only the changing comparison operator and error message as arguments.

The list primitives are direct structural operations on `Cons`: `car` extracts the first field, `cdr` extracts the second field, and `cons` constructs a new `Cons`. The evaluator must still validate that the evaluated value has the right shape.

Many numeric predicates share the same shape: evaluate two arguments, require numbers, apply an OCaml operator, return `t` or `Nil`. That's why `makeRelation` exists:

```ocaml
let makeRelation op message =
  fun args env ->
    match args with
    | Cons (left, Cons (right, Nil)) ->
        let left = evaluating left env in
        let right = evaluating right env in
        (match (left, right) with
         | (Number left, Number right) ->
             if op left right then tee else Nil
         | _ -> oops message)
    | _ -> oops message ;;
```

Captures the repeated argument-checking pattern. Then `<`, `<=`, `<>`, `>`, `>=` are installed by passing different OCaml comparison functions.

**List primitives:**
- `car` — first element of nonempty `Cons`.
- `cdr` — rest of nonempty `Cons`.
- `cons` — builds `Cons (first, rest)`.

## Labs / Projects
### Lab 10 — Lisp Printer
Source: `Labs/lab10.ml` | Tests: `Labs/tests10.ml`

Tests exact printing for `Nil`, numbers, symbols, closures, primitives, and proper `Cons` lists. Mutual recursion between thing-level and list-level helpers.

Concepts: [[OCaml - Lisp Printer]], [[OCaml - Mutual Recursion]], [[OCaml - Lisp Thing Representation]]

### Project 2 — Lisp Parser
See: [[Project - 2 Lisp Parser|Project - 2 Lisp Parser]]

## Examples worth keeping
- `Closure (_, _, _) -> printf "[Closure]"` — printer doesn't dump environments.
- `Cons (_, _) as things -> printf "("; printingThings things; printf ")"` — list wrapper.
- `and` returns `Nil` immediately when an argument evaluates to `Nil`.
- `or` returns the first non-`Nil` value.
- `makeRelation` — higher-order primitive builder.

## Takeaways (questions to resolve)
- [ ] Why are printer functions mutually recursive?
- [ ] What makes a `Cons` chain print as a parenthesized list?
- [ ] Which primitives must avoid evaluating all arguments? (`and`, `or`, `if`, `quote`, `define`, `lambda`)
- [ ] What repeated pattern does `makeRelation` eliminate?

## Flashcards
#cards/CSCI2041
- Why does the Lisp printer use mutual recursion::Things can contain lists, and lists contain things — each level needs to call the other.
- What does `car` return::The first element of a nonempty `Cons`.
- What does `cdr` return::The rest of a nonempty `Cons`.
- Why are `and` and `or` special primitives::They short-circuit — stop evaluating arguments as soon as the result is determined.
- What does `makeRelation` build::A primitive function that evaluates two numeric arguments, compares them with a given operator, and returns `t` or `Nil`.
- What does `Primitive of (thing -> environment -> thing)` mean::A primitive receives unevaluated arguments and the environment, deciding evaluation order itself.
