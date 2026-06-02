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
  - "[[OCaml - Lisp Evaluator]]"
  - "[[OCaml - References and Mutation]]"
  - "[[OCaml - Interpreter Primitives and Special Forms]]"
---

# OCaml - Environments and Closures

## One-Line Answer
An environment maps names to values; a closure stores parameters, body, and the environment visible when the function was created — that's lexical scoping in the interpreter.

## 30-Second Explanation
`environment = (string * thing) list`. `lambda` builds `Closure (pars, body, env)`. `apply` evaluates arguments in the *caller* environment, binds them into the *closure's* saved environment, then evaluates the body there. If you use the wrong environment, you get dynamic scoping or broken bindings.

## OCaml Shape
```ocaml
(* Closure creation *)
Closure (pars, body, env)

(* Application — the key mechanism *)
let rec applying pars args bodyEnv =
  match (pars, args) with
  | (Nil, Nil) -> evaluating body bodyEnv
  | (Cons (Symbol name, pars), Cons (arg, args)) ->
      applying pars args
        (envPut name (evaluating arg argsEnv) bodyEnv)
  | _ -> oops "Bad application"

(* Lookup order *)
let lookup env name =
  envGet env name (fun () -> envGet (!global) name (fun () -> oops ...))
```

## Mental Model
- **Lookup**: local first → global second → error.
- **`define`**: writes to mutable global.
- **`let`**: extends a local environment for one body.
- **`lambda`**: saves the current environment into a closure.
- **`apply`**: evaluates args in caller env, binds them in closure env, runs body there.

## Contrast With
- **[[OCaml - References and Mutation]]**: global env is mutable (`ref`); local env extension returns a new list (immutable pattern).
- **[[OCaml - Interpreter Primitives and Special Forms]]**: primitives are OCaml functions; closures are user-created Lisp functions.
- **Dynamic scoping**: if body ran in the caller's environment instead of the closure's, that would be dynamic scoping. This course uses lexical.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 12]] (highest priority), [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13]], [[Week - 15]].
- Labs: Lab 11 (`lab11.ml`, `tests11.ml`), Lab 12 (`lab12.ml`).
- Textbook: Hickey Ch. 3 (scoping/closures), Ch. 7 (mutation for `global`).

## Common Mistakes
- Evaluating closure body in the caller environment instead of the closure's saved environment.
- Binding parameters globally instead of locally.
- Evaluating parameter *names* instead of treating them as symbols in `lambda`.
- Forgetting that `!global` enables mutually recursive Lisp functions (both see the shared mutable env).
- Confusing `argsEnv` (where arguments are evaluated) with `bodyEnv` (where body runs).

## Diagnostic Questions
- What does `Closure (pars, body, env)` store?
- Why does `apply` receive both `argsEnv` and `bodyEnv`?
- What does `lookup` search first?
- How does `(let a 1 (let b 2 (+ a b)))` keep both names visible?
- Why does `define` use mutation while `let` doesn't?

## Flashcards
#cards/CSCI2041
- What is an environment in Lab 11::A `(string * thing) list` mapping symbol names to values.
- What does `lookup` search first::The local environment, then global, then error.
- What does `define` mutate::The global environment `!global`.
- What does `lambda` return::`Closure (pars, body, env)` — parameters, body, and the defining environment.
- Where are closure arguments evaluated::The caller's environment (`argsEnv`), not the closure's.
- Why does `!global` enable mutual recursion::Because all defined functions share the same mutable environment, so function A can see function B even if B was defined later.
