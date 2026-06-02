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
  - "[[OCaml - Scanners and Tokens]]"
  - "[[OCaml - Mutual Recursion]]"
  - "[[OCaml - Lisp Thing Representation]]"
---

# OCaml - Recursive Descent Parsing

## One-Line Answer
Parser functions mirror the grammar's recursive structure: one function per grammar category, mutually recursive because things contain lists and lists contain things.

## 30-Second Explanation
Lisp grammar is naturally recursive: an expression is an atom or a parenthesized list of expressions. `nextThing` parses one expression. `nextThings` parses list contents. They're mutually recursive. One-token lookahead in `token : Scanner.token ref` decides which branch to take.

```ocaml
let rec nextThings () =
  match !token with
  | Scanner.CloseParenToken -> nextToken (); Nil
  | Scanner.EndToken -> raise (Can'tParse "Ran out of tokens before list was closed.")
  | _ ->
      let first = nextThing () in
      Cons (first, nextThings ())

and nextThing () =
  match !token with
  | Scanner.NumberToken n -> nextToken (); Number n
  | Scanner.OpenParenToken -> nextToken (); nextThings ()
  | Scanner.SymbolToken "nil" -> nextToken (); Nil
  | Scanner.SymbolToken s -> nextToken (); Symbol s
  | Scanner.CloseParenToken -> raise (Can'tParse "Got ) when expecting an expression.")
  | Scanner.EndToken -> raise (Can'tParse "Nothing left to parse.") ;;
```

## Definition
- Recursive descent: top-down parser implemented as mutually recursive functions, one per grammar category.
- Lookahead token: current token used to decide which branch to take.
- **Token invariant**: on entry, `!token` is the first token of the expression to parse. On exit, `!token` is the first token *after* that expression.

## Contrast With
- **[[OCaml - Scanners and Tokens]]**: scanner groups characters into tokens; parser builds nested structure from tokens.
- **[[OCaml - Mutual Recursion]]**: recursive descent often requires `and` because grammar categories reference each other.
- **[[OCaml - Lisp Thing Representation]]**: parser output is a `thing` value.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 10]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13]], [[Week - 15]].
- Labs: Lab 12 (`lab12.ml`).
- Projects: [[Project - 2 Lisp Parser|Project - 2 Lisp Parser]].
- Textbook: Hickey Ch. 4, Ch. 6, Ch. 11-12, Ch. 19.

## Common Mistakes
- Matching `SymbolToken s` before `SymbolToken "nil"` — `nil` gets treated as a regular symbol.
- Forgetting to advance past `OpenParenToken` before calling `nextThings`.
- Forgetting to advance past `CloseParenToken` when ending a list.
- Returning `Nil` on unexpected `EndToken` instead of raising `Can'tParse`.
- Breaking the token invariant — leaving `!token` pointing at the wrong position.

## Diagnostic Questions
- What is the precondition for `nextThing`? (`!token` is the first token of the expression)
- What should `nextThings` do when it sees `CloseParenToken`? (advance and return `Nil`)
- Why is `EndToken` inside a list an error? (list was never closed)
- How does `(a b c)` become `Cons (Symbol "a", Cons (Symbol "b", Cons (Symbol "c", Nil)))`?

## Flashcards
#cards/CSCI2041
- Parser input type::`Scanner.token`.
- Parser output type::`thing`.
- What does `SymbolToken "nil"` become::`Nil`, not `Symbol "nil"`.
- What does `nextThings` build::A right-nested `Cons` chain ending in `Nil`.
- What exception reports parser errors::`Can'tParse of string`.
- What is the parser's token invariant::On entry `!token` is the first token of the expression; on exit it's the first token after.
