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

# OCaml - Macros and Metaprogramming

- Metaprogramming is programming about program structure; macros transform code-shaped data before ordinary evaluation.

## 30-Second Explanation
- Week 13 introduces macros after the interpreter arc because the class has already built code-as-data machinery. `Labs/Practice/modularMacros.pdf` is the source anchor named in the map, and the weekly note ties it to `thing` representation, parser output, and evaluator behavior.

## Teach It To A Beginner
- A normal function usually works with evaluated argument values. A macro works with expression structure. This is natural in Lisp because Lisp code is already represented as list-shaped data.
- The course reason for placing macros here is important: once scanner/parser/evaluator exist, it becomes possible to discuss changing program structure before evaluation.

## Definition
- Metaprogramming: writing programs that inspect, generate, or transform programs.
- Macro: a code transformation mechanism that operates on expression structure rather than ordinary evaluated argument values.

## Mental Model
- Function: receives values.
- Special form: controls argument evaluation.
- Macro: receives code shape and returns replacement code shape.
- Lisp makes this natural because code and data share list structure.

## Contrast With
- [[OCaml - Interpreter Primitives and Special Forms]]: special forms are built-in evaluator behavior; macros rewrite expressions.
- [[OCaml - Lisp Thing Representation]]: macros depend on code being represented as data.
- [[OCaml - Recursive Descent Parsing]]: parser creates the expression structures a macro can transform.

## Where It Appears
- Weekly notes: [[Week - 13]], [[Week - 15]].
- Labs/practice: `Labs/Practice/modularMacros.pdf`.
- Projects: no direct project submission in the source map, but the idea extends the Project 2 interpreter architecture.
- Textbook: Hickey Ch. 19 syntax, Ch. 11-12 modules, Ch. 3 functions.

## Common Mistakes
- Describing macros as just ordinary functions.
- Forgetting that macro arguments are code/expression structure.
- Trying to understand macros before understanding `thing` representation.
- Treating Week 13 macros as isolated rather than as a consequence of the interpreter pipeline.

## Diagnostic Questions
- Why do macros fit naturally after Lisp parsing?
- What does a macro operate on that a normal function usually does not?
- How does the `thing` type make code-as-data possible?
- Why is Hickey Ch. 19 relevant here?

## Mini-Test
- [ ] Explain the difference between a function and a macro in one sentence.
- [ ] Identify which interpreter stage produces structures a macro could transform.
- [ ] Describe why Lisp list syntax helps metaprogramming.

## Flashcards
#cards/CSCI2041
- What is metaprogramming::Programming that manipulates program structure.
- What does a macro transform::Code-shaped expression data.
- Why are macros natural in Lisp::Lisp code is represented as data/list structure.
- What week introduces macros::[[Week - 13]].
- What source file anchors the macro topic::`Labs/Practice/modularMacros.pdf`.
