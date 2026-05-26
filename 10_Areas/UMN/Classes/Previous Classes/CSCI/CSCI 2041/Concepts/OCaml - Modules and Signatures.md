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
  - "[[OCaml - Association Lists]]"
  - "[[OCaml - Scanners and Tokens]]"
  - "[[OCaml - Recursive Descent Parsing]]"
---

# OCaml - Modules and Signatures

## One-Line Answer
A module groups implementation; a signature says what outside code is allowed to see. Everything not in the signature is hidden.

## 30-Second Explanation
Lab 8: `module type Associaty = sig ... end` + `module Association : Associaty = struct ... end`. Same pattern repeats for scanner, parser, evaluator, printer, and REPL. The signature is the public contract; the struct is the machinery. If a name isn't in the signature, outside code can't use it.

## Key Examples
- Lab 8: `Association.make`, `put`, `get`, `delete` are public. Internal list representation is hidden.
- Project 2: `Parserish` exposes `Can'tParse`, `initialize`, `nextThing`. Token state, `nextToken`, `nextThings` stay hidden.
- Textbook: Hickey Ch. 11-12.

```ocaml
module type Parserish =
sig
  exception Can'tParse of string ;;
  val initialize : string -> unit ;;
  val nextThing : unit -> thing ;;
end ;;

module Parser : Parserish =
struct
  (* hidden state and helpers live here *)
end ;;
```

## Definition
- Module: named collection of types, values, exceptions.
- Signature: interface constraining which components are externally visible.
- `module M : S = struct ... end`: `M` satisfies `S`, outside code sees only what `S` exposes.

## Contrast With
- **Plain files**: every top-level name can become visible without an explicit interface.
- **[[OCaml - Algebraic Data Types and Structural Recursion]]**: ADTs define data shapes; modules decide which shapes/functions are public.
- **[[OCaml - Recursive Descent Parsing]]**: parser logic is hidden behind `Parserish`.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 8]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 9]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 10]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[Week - 13]], [[Week - 15]].
- Labs: Lab 8 (`lab8.ml`, `tests8.ml`), Lab 11, Lab 12.
- Projects: [[Project - 2 Lisp Parser|Project - 2 Lisp Parser]].
- Textbook: Hickey Ch. 11-12.

## Common Mistakes
- Putting a helper in the signature — accidentally making it public.
- Forgetting to expose an exception that callers must catch.
- Thinking the signature is "just documentation" — it actually controls visibility and type checking.
- Exposing representation details that make later changes impossible.

## Diagnostic Questions
- What can outside code do with `Association`?
- Which names does `Parserish` expose?
- Why should `nextThings` stay hidden?
- How do signatures prepare the interpreter for scanner/parser/printer/evaluator separation?

## Flashcards
#cards/CSCI2041
- What does a module signature define::The public interface — which types, values, and exceptions are visible outside.
- What does `module M : S` do::Constrains `M` to expose only what signature `S` declares.
- What does `Parserish` expose::`Can'tParse`, `initialize`, and `nextThing` — nothing else.
- Why hide parser helpers::Outside code should use the parser contract, not its internal cursor logic.
- What's the difference between signature and documentation::A signature is enforced by the compiler — it controls what's accessible, not just what's described.
