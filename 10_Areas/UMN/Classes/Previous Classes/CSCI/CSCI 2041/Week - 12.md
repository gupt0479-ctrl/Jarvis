---
type: class
input_kind: lecture
status: sprout
created: 2026-05-08
updated: 2026-05-12
area:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Environments and Closures]]"
  - "[[OCaml - Lisp Evaluator]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[Week - 13]]"
---
# Entire Week
## What you must be able to do
- Explain how the evaluator looks up symbols: local environment first, then global.
- Explain how `define` mutates the global environment.
- Explain how `lambda` creates a closure: `Closure (pars, body, env)`.
- Trace `apply`: parameter matching, argument evaluation in caller env, body evaluation in closure env extended with bindings.
- Explain how `areParameters` prevents invalid lambda parameter lists.
- Walk through a small Lisp expression by hand using evaluator rules.

## Key ideas (textbook)
- Hickey Ch. 3 scoping/closures: the evaluator's `Closure (pars, body, env)` is the interpreter version of lexical scoping.
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4|Ch. 4]]: evaluator dispatches by matching `thing` constructors.
- Hickey Ch. 9: evaluator failures use explicit error messages.
- Hickey Ch. 11-12: evaluator is one module in the interpreter architecture.

## Concepts created / updated today
- [[OCaml - Environments and Closures]]
- [[OCaml - Lisp Evaluator]]
- [[OCaml - Interpreter Primitives and Special Forms]]

## Lecture
### Week 12 lecture map - user functions, closures, and `apply`
Week 12 is the center of the Lisp evaluator. Before this week, the language can mostly run built-in behavior. After this week, Lisp users can define functions, save lexical environments, and apply closures.

Source anchors:
- `Lecture - 31.txt` finishes primitive functions and starts user-defined functions through `define`, `lambda`, and the coming `apply`.
- `Lecture - 32.txt` focuses on `apply`: how user-defined functions are called, how environments are handled, how argument counts are checked, and how the body is evaluated.
- `Lecture - 33.txt` walks through a small evaluator execution and then introduces compiler commands for the final lab.
- `Labs/lab11.ml` is the authoritative code source for `global`, `lookup`, `evaluating`, `apply`, `areParameters`, `lambda`, `let`, `is-atom`, and `imply`.

The environment rule to keep exact:
- Symbols are looked up in the local environment first.
- If not found locally, lookup falls back to `!global`.
- `define` mutates `global`, so globally defined functions can see each other.
- `lambda` stores `Closure (pars, body, env)`, where `env` is the defining environment.
- `apply` evaluates arguments in the caller environment (`argsEnv`) but evaluates the body in the closure environment (`bodyEnv`) extended with parameter bindings.

That last rule is the interpreter's version of lexical scoping. If the body used the caller's environment instead, the interpreter would behave like a dynamically scoped language.

### Apr 13 — Finishing Primitives, Starting User Functions
Sources: `Lecture - 31.txt`, professor notes `13Apr26/`, `Labs/lab11.ml`.

The lecture finishes the primitive set by emphasizing cases with important error behavior: division checks for divide-by-zero, `=` only compares nils, numbers, and symbols, and relation primitives expect two numbers. Then the course shifts to the thing programmers actually need: defining their own functions.

`define` is the key side-effecting primitive. It expects a symbol and an expression, evaluates the expression in the current environment, and extends the mutable global environment. The returned value is the symbol itself, matching the source code in `lab11.ml`.

Until `lambda`, the evaluator can only run built-in behavior. `define` and `lambda` make the language programmable.

The global environment is mutable:
```ocaml
let global = ref (envMake ()) ;;
```

`define` changes it by binding a symbol to a value. This is one of the clearest side effects in the interpreter. Lookup has two phases: search local first, then global.

### Apr 15 — `lambda`, Closures, and `apply`
Sources: `Lecture - 32.txt`, professor notes `15Apr26/`, `Labs/lab11.ml`, `Labs/tests11.ml`.

The lecture's two apply questions are the exam questions: how does `apply` handle environments, and how does it make sure there are enough arguments? The code answers both with the same recursive walk over parameter and argument lists.

`areParameters` protects `lambda` before a closure is created. A valid parameter list must be a proper Lisp list of distinct symbols. That is why `(lambda (x x) ...)` and `(lambda (3) ...)` should not produce ordinary closures.

**This is the center of the evaluator.** `lambda` returns a closure:
```ocaml
Closure (pars, body, env)
```

The triple:
- `pars` — parameter list (a `thing` list of symbols).
- `body` — unevaluated body expression.
- `env` — environment visible when the function was created.

`apply` is where function calls happen:
```ocaml
applying pars args (envPut name (evaluating arg argsEnv) bodyEnv)
```

This line *is* lexical scoping inside the interpreter:
- Arguments evaluated in the **caller's** environment (`argsEnv`).
- Body evaluated in the **closure's** environment (`bodyEnv`) extended with parameter bindings.

**Why this matters:** if you evaluate the body in the caller's environment, you get dynamic scoping. The course uses lexical scoping — the function sees what was visible when it was *created*, not when it was *called*.

### Apr 17 — Evaluator Walkthrough
Sources: `Lecture - 33.txt`, professor notes `17Apr26/`, `Labs/tests11.ml`.

The lecture walks through evaluation because the evaluator does many small steps that are easy to blur together. The dispatcher first decides whether the expression is a function call, a symbol lookup, or a self-evaluating value. Function calls then split into primitive calls and closure applications.

The compiler discussion at the end prepares Lab 12. The course moves from using the interpreter interactively to compiling/running a full OCaml file, which matters because the final lab integrates many modules into one program.

Dispatcher rules:
- `Symbol name` → look it up.
- `Cons (func, args)` → evaluate `func`; must become `Closure` or `Primitive`.
- `Primitive howTo` → let the primitive decide evaluation rules.
- `Closure (pars, body, bodyEnv)` → call `apply`.
- Anything else → evaluates to itself.

`tests11.ml` tests forms added near the end: `is-atom`, `imply`, `let`.
- `(let n 1 n)` returns `Number 1`.
- Nested `let` should preserve the right environment chain.
- A wrong implementation that stores every binding globally will fail these tests.

## Labs / Projects
### Lab 11 — Lisp Evaluator
Source: `Labs/lab11.ml` | Tests: `Labs/tests11.ml`

Tests `envGet`, `envPut`, `lookup`, `evaluating`, `apply`, `define`, `lambda`, `and`, `or`, `if`, `quote`, `let`, `is-atom`, `imply`.

**Highest priority lab for the final.** Be able to trace local vs global lookup and why `imply`/`and`/`or` must avoid evaluating every argument eagerly.

Concepts: [[OCaml - Lisp Evaluator]], [[OCaml - Environments and Closures]], [[OCaml - Interpreter Primitives and Special Forms]]

## Examples worth keeping
- `global := envPut name value (!global)` — mutation through `define`.
- `Closure (pars, body, env)` — saved lexical environment.
- `applying pars args (envPut name (evaluating arg argsEnv) bodyEnv)` — the apply mechanism.
- `lookup env name` — local search, then global, then error.

## Takeaways (questions to resolve)
- [ ] What is stored in a Lisp closure? (pars, body, defining env)
- [ ] Why are arguments evaluated in `argsEnv`? (caller's context)
- [ ] Why is the body evaluated in `bodyEnv` extended with parameters? (lexical scoping)
- [ ] What is the lookup order for a symbol? (local → global → error)
- [ ] Which tests would fail if `let` used only the global environment?

## Flashcards
#cards/CSCI2041
- What does `define` mutate::The mutable global environment `!global`.
- What are the three parts of a closure::Parameter list, body, and the defining environment.
- In `apply`, where are arguments evaluated::The calling environment (`argsEnv`) — because arguments belong to the call site.
- In `apply`, where is the body evaluated::The closure's saved environment extended with parameter bindings — this is lexical scoping.
- What does lookup search first::The local environment, then global, then raises an error.
- Why does `!global` enable mutually recursive Lisp functions::Because `define` stores functions in a shared mutable environment that all functions can see, so function A can call function B even if B was defined after A.
