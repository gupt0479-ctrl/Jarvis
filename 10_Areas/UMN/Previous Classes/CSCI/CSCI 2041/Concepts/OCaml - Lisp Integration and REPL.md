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

# OCaml - Lisp Integration and REPL

- The final Lisp interpreter integrates scanner, parser, evaluator, printer, and a loop that runs them over input files.

## 30-Second Explanation
- `Labs/lab12.ml` is the integration scaffold. It includes the shared `thing` type, an evaluator, a scanner, and placeholders for `Parsish`, `Parser`, `Printish`, `Printer`, `Lispish`, and `Lisp`. The final call is `Lisp.repl ()`, making the architecture explicit: read, evaluate, print, loop.

## Teach It To A Beginner
- The interpreter is not one magic function. It is a pipeline:
- Scanner reads characters and returns tokens.
- Parser reads tokens and returns `thing`.
- Evaluator computes a `thing` value.
- Printer displays the value.
- REPL repeats that process for expressions in command-line files.
- Textbook connection: Hickey Ch. 11 and Ch. 12 support this as a module/program organization problem.

## Definition
- REPL: read-evaluate-print-loop.
- Integration scaffold: source file that assembles separately learned components into one executable interpreter flow.
- Public module interfaces: `Evaluatish`, `Scannerish`, `Parsish`, `Printish`, and `Lispish`.

## Mental Model
- `Scanner.nextToken`: raw input to tokens.
- `Parser.nextThing`: tokens to tree.
- `Evaluator.evaluate`: tree to value.
- `Printer.printThing`: value to output.
- `Lisp.repl`: orchestration.

## Contrast With
- Individual lab notes: Lab 12 is about joining earlier pieces, not inventing every component from scratch.
- [[OCaml - Modules and Signatures]]: integration depends on module boundaries.
- [[OCaml - Lisp Evaluator]]: evaluator is one stage; REPL coordinates all stages.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13]], [[Week - 15]].
- Labs: [[Lab - 12 Lisp Integration]].
- Projects: [[Project - 2 Lisp Parser]] provides a parser component for this architecture.
- Textbook: Hickey Ch. 10, Ch. 11, Ch. 12.

## Common Mistakes
- Treating Lab 12 as just copy-paste instead of interface matching.
- Forgetting that each module exposes only its signature.
- Printing unevaluated expressions when the REPL should print evaluated results.
- Failing to handle end-of-input cleanly when reading multiple files/expressions.

## Diagnostic Questions
- What are the five interpreter stages?
- Which module owns file-to-token behavior?
- Which module owns token-to-thing behavior?
- What does `Lisp.repl ()` orchestrate?

## Mini-Test
- [ ] Draw the pipeline for evaluating `(+ 2 2)`.
- [ ] Explain what `commandArguments etc` contributes.
- [ ] Identify which Lab 12 placeholders correspond to earlier labs/projects.

## Flashcards
#cards/CSCI2041
- What does REPL stand for::Read-evaluate-print-loop.
- What does scanner produce::Tokens.
- What does parser produce::`thing` values.
- What does evaluator produce::A Lisp value, also represented as `thing`.
- What does printer consume::A `thing` value.
