---
type: class
input_kind: lecture
status: sprout
created: 2026-05-08
updated: 2026-05-12
area:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Mutual Recursion]]"
  - "[[OCaml - Tail Recursion and Internal Helpers]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[Final Review Map]]"
---
# Entire Week
## What you must be able to do
- Distinguish mutually recursive functions from internal helper functions.
- Explain why `let rec ... and ...` is needed when functions call each other.
- Explain when an internal helper inherits unchanged arguments from scope.
- Review the interpreter pipeline end to end: scanner → parser → printer → evaluator → REPL.
- Reproduce core mechanisms from memory: ADT traversal, module signatures, recursive descent, environment lookup, closure application, memoization, lazy-list forcing.

## Key ideas (textbook)
- Hickey Ch. 3: `and` binds functions together so they can call each other.
- Hickey Ch. 3 scoping: internal helpers see values in the enclosing function.
- Hickey Ch. 11-12: final interpreter review depends on file/module organization.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4|Ch. 4]] and Hickey Ch. 6: almost every final structure uses pattern matching over ADTs.

## Concepts created / updated today
- [[OCaml - Mutual Recursion]]
- [[OCaml - Tail Recursion and Internal Helpers]]

## Lecture
### Week 15 lecture map - final review by code patterns
Week 15 is a review session, not a new-content week. The transcript starts from a student question about mutually recursive functions versus internal helpers, which is a useful final-exam distinction because both patterns use local definitions but solve different problems.

Source anchors:
- `Lecture - 40.txt` is the only source for this week; no `04May26/` professor-note folder was found in the source corpus.
- The first review question contrasts mutually recursive functions with an internal helper.
- The transcript names the realistic interpreter example: `evaluating` and `apply` call each other, so they require mutual recursion.
- Earlier labs/projects supply the memory targets: stream helpers, memoized recursion, lazy forcing, module signatures, scanner/parser, printer, evaluator environments, closures, and CPS generation.

Final review organization:
1. `let rec f ... and g ...` is for functions that call each other.
2. `let rec helper ... in ...` is for a helper whose changing argument is smaller but whose fixed context comes from the outer function.
3. Interpreter mutual recursion matters most in `evaluating` / `apply` and parser `nextThing` / `nextThings`.
4. Internal helpers matter in searches, traversals, environment lookup, and accumulator-style recursion.

### May 4 — Final Review
Sources: `Lecture - 40.txt` (no `04May26/` notes folder found).

The first review question is about mutually recursive functions versus an internal helper. Mutually recursive functions are two or more peer functions that call each other, so OCaml must define them together with `and`. Internal helpers are nested functions used because the outer function supplies stable context.

The realistic examples are from the interpreter and parser. `evaluating` and `apply` need mutual recursion because evaluating a function call may apply a closure, and applying a closure evaluates the body. `nextThing` and `nextThings` need mutual recursion because a thing may be a list, and a list contains more things.

Review session, not new material. The transcript opens with a question about mutually recursive functions vs internal helpers. Worth preserving because the two patterns look similar in code but serve different purposes.

**Mutual recursion** — two or more functions call each other. Must be defined together:
```ocaml
let rec even n =
  n = 0 || odd (n - 1)
and odd n =
  n <> 0 && even (n - 1) ;;
```

`even` must know about `odd` and vice versa, so definitions are tied with `and`.

**Internal helper** — function defined inside another function, usually because it needs access to unchanged values from outer scope:
```ocaml
let contains target things =
  let rec looping things =
    match things with
    | [] -> false
    | first :: rest -> first = target || looping rest
  in looping things ;;
```

`looping` doesn't need mutual recursion with `contains`. It uses `target` from the enclosing scope. This pattern appeared early and keeps returning in labs where one argument stays fixed across recursive calls.

### Final Exam Synthesis

Organize by what you can *write from memory*, not by topic names.

**Core mechanisms:**
- Recursive ADT traversal: BSTs, expression solving, Lisp `thing`, tautology propositions.
- Tail recursion and helpers: list processing, performance-sensitive recursion.
- Memoization: `memyC` avoiding repeated binomial subproblems.
- Lazy evaluation: lazy lists with delayed tails forced later.
- Module signatures: `Association`, scanner/parser/printer/evaluator.
- Recursive descent: Project 2 turning token streams into `thing` values.
- Lisp evaluation: symbol lookup, primitive dispatch, closure creation, `apply`.
- CPS: generators/permutation-style examples, tautology generation.

**The interpreter arc (biggest integration target):**
1. Scanner reads characters → returns tokens.
2. Parser reads tokens → returns `thing`.
3. Printer turns `thing` → visible Lisp syntax.
4. Evaluator maps `thing` → value using environments, primitives, closures.
5. REPL repeats read, evaluate, print.

## Labs / Projects
- Review all labs (5-12) and both projects before the final.
- High-priority source files: `lab6.ml`, `lab7.ml`, `lab8.ml`, `lab9.ml`, `lab10.ml`, `lab11.ml`, `lab12.ml`, `project-1/project.ml`, `project-2/project2.ml`, `project-2/scanner.ml`.

## Examples worth keeping
- `let rec f ... and g ...` — mutually recursive definitions.
- `let rec helper ... in helper ...` — internal helper pattern.
- `Closure (pars, body, env)` — interpreter closure.
- `applying pars args (envPut name (evaluating arg argsEnv) bodyEnv)` — closure application.
- `nextThing` / `nextThings` — parser mutual recursion.

## Takeaways (questions to resolve)
- [ ] When do I need `and` for mutual recursion?
- [ ] When should I use an internal helper instead?
- [ ] Can I trace scanner → parser → evaluator → printer?
- [ ] Can I explain closure application without hand-waving environment behavior?
- [ ] Which lab tests expose each major concept?

## Flashcards
#cards/CSCI2041
- What is mutual recursion::Two or more functions defined together because they call each other.
- What keyword connects mutually recursive OCaml functions::`and` — ties the definitions so each can see the other.
- Why use an internal helper::To keep fixed outer arguments in scope while recursing over changing ones — avoids passing them explicitly.
- What are the interpreter pipeline stages::Scanner → parser → evaluator → printer → REPL.
- When do you need `and` vs an internal helper::`and` when functions call *each other*. Internal helper when one function needs access to the outer function's unchanged arguments.
