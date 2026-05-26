---
type: class
input_kind: lecture
status: sprout
created: 2026-05-08
updated: 2026-05-12
area:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Macros and Metaprogramming]]"
  - "[[OCaml - Lisp Integration and REPL]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[Week - 14]]"
---
# Entire Week
## What you must be able to do
- Explain metaprogramming as programs manipulating program structure.
- Explain what a macro adds to the Lisp interpreter (transforms expression structure *before* evaluation).
- Identify the integration points in `Labs/lab12.ml`.
- Explain how scanner, parser, printer, evaluator, and REPL fit together.
- Explain the role of `Parsish`, `Printish`, and `Lispish` signatures.
- Connect macros to the idea that Lisp code is data.

## Key ideas (textbook)
- Hickey Ch. 19 `Syntax`: macros and parsers both depend on treating program text/structure as data.
- Hickey Ch. 11-12: Lab 12's final integration is a module organization problem.
- Hickey Ch. 3 and Ch. 6: metaprogramming relies on functions and recursive data representations.

## Concepts created / updated today
- [[OCaml - Macros and Metaprogramming]]
- [[OCaml - Lisp Integration and REPL]]
- [[OCaml - If Normalization and Tautology Checking]]

## Lecture
### Week 13 lecture map - macros, integration, and the return of tautology
Week 13 finishes the planned interpreter arc and opens the special-topic ending. The connecting idea is that code can be represented as data, transformed, and then interpreted.

Source anchors:
- `Lecture - 34.txt` defines metaprogramming as programming about programming, specifically programs that make additional code for themselves.
- The same lecture introduces Lisp macros after higher-order primitive builders: both are ways to make code produce behavior, but macros transform expression structure before ordinary evaluation.
- `Lecture - 35.txt` continues macros and lines up the final lab.
- `Labs/lab12.ml` states that most code has already been written and only selected placeholders remain: `Parsish`, `Parser`, `Printish`, `Printer`, `Lispish`, and `Lisp`.
- `Lecture - 36.txt` starts the special-topic tautology checker. It returns to a problem from earlier in the course but uses an if-based representation instead of brute-force truth assignments.

The week should feel like one architecture diagram:
1. Scanner reads characters into tokens.
2. Parser turns tokens into `thing`.
3. Printer turns `thing` back into readable Lisp.
4. Evaluator turns expressions into values.
5. REPL repeats that pipeline over input files.
6. Macros and if-based tautology checking both depend on treating program/logical structure as recursive data.

### Apr 20 — Metaprogramming and Macros
Sources: `Lecture - 34.txt`, professor notes `20Apr26/`, `Labs/Practice/modularMacros.pdf`.

The lecture explicitly says the scheduled course topics are almost finished and introduces metaprogramming as the last scheduled topic. In this course, metaprogramming means programs that make or transform additional code for themselves. The Lisp interpreter makes this natural because code is already represented as recursive data.

The macro material also adds one more primitive idea: `list`, which builds a Lisp list of evaluated arguments. That primitive becomes useful when a macro needs to construct expression structure.

"Meta" = "about." Metaprogramming = programming about programming. In this course: extending Lisp so programs can make or transform additional code.

Macros fit naturally after the interpreter because the course already built machinery to represent code as data. If Lisp expressions are `thing` values, a macro can transform one `thing` structure into another *before* ordinary evaluation.

**Key distinction:** a function receives *evaluated* arguments (unless it's a special primitive). A macro works on *expression structure*. That's the difference.

### Apr 22 — Final Lab Integration
Sources: `Lecture - 35.txt`, professor notes `22Apr26/`, `Labs/lab12.ml`.

Lab 12 says the student has already written most of the required code in earlier labs and projects. The new work is integration: fill module signatures and modules so the scanner, parser, printer, evaluator, and command-line REPL connect.

The source file is also a compact review of the whole interpreter. Its comments restate the meaning of `Closure`, `Cons`, `Nil`, `Number`, `Primitive`, `Symbol`, and `environment`, then place each later module behind a signature.

`lab12.ml` is the map of the final interpreter architecture. It includes most evaluator and scanner code and leaves placeholders for:
- `Parsish` / `Parser`
- `Printish` / `Printer`
- `Lispish` / `Lisp`

The important mechanism is explicit boundaries. Each module has a public interface and internal helpers. The pipeline:
1. Scanner → tokens
2. Parser → `thing`
3. Evaluator → value
4. Printer → visible output
5. REPL → repeat over command-line files

### Apr 24 — Special Topic: Tautology Returns
Sources: `Lecture - 36.txt`, professor notes `24Apr26/`, `Labs/Practice/iffyTaut.ml`.

The lecture marks the move into "special topics." The earlier tautology checker generated all possible assignments and ran in exponential time. The new approach is a small automatic theorem prover: represent propositions as if-expressions, normalize them, simplify them, and see whether the result is `T`.

The important change is representation. Instead of many constructors for logical connectives, the source uses `If of proposition * proposition * proposition` plus `T`, `F`, and variables.

Planned course topics mostly complete. Returns to tautology checking through a different representation:
```ocaml
type proposition =
  T | F | V of string | If of proposition * proposition * proposition ;;
```

Bridge into Week 14. No longer brute-forcing every truth assignment — now transforming proposition structure, normalizing conditionals, substituting truth values, checking simplified forms.

## Labs / Projects
### Lab 12 — Lisp Integration
Source: `Labs/lab12.ml` | Tests: none found in source corpus.

Wires the interpreter pipeline through module boundaries. Not testing one new function — testing that all pieces connect.

Concepts: [[OCaml - Lisp Integration and REPL]], [[OCaml - Modules and Signatures]], [[OCaml - Scanners and Tokens]], [[OCaml - Lisp Evaluator]]

## Examples worth keeping
- `Lisp.repl ()` — the big-finish call at the end of `lab12.ml`.
- `Parser` and `Printer` placeholders — visible integration tasks.
- Macro distinction: function evaluates arguments; macro transforms expression structure.
- `If (pi, alpha, beta)` — if-based proposition node.

## Takeaways (questions to resolve)
- [ ] What makes metaprogramming different from ordinary programming? (operates on program structure)
- [ ] Why do macros fit naturally in Lisp? (code is already data)
- [ ] What modules does Lab 12 integrate?
- [ ] What's the difference between parser output and evaluator output? (`thing` vs evaluated `thing`)

## Flashcards
#cards/CSCI2041
- What is metaprogramming in this course::Programs manipulating or generating program structure — code that makes code.
- Why are macros natural in Lisp::Lisp code is represented as `thing` data structures, so transforming code is just transforming data.
- What modules does Lab 12 integrate::Scanner, parser, printer, evaluator, and REPL — the full interpreter pipeline.
- What does a REPL do::Read (parse), evaluate, print, loop — repeatedly over input expressions.
- How is a macro different from a function::A function receives evaluated arguments; a macro transforms unevaluated expression structure before evaluation happens.
