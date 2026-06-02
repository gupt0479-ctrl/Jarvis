---
type: class
input_kind: lecture
status: sprout
created: 2026-05-08
updated: 2026-05-12
area:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Scanners and Tokens]]"
  - "[[OCaml - Recursive Descent Parsing]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 11]]"
---
# Entire Week
## What you must be able to do
- Explain the scanner/parser pipeline: characters → tokens → `thing` values.
- Trace the scanner's mutable input state in `scanner.ml`.
- Identify the token constructors used by the Lisp scanner.
- Explain why parser functions use one-token lookahead.
- Write the recursive descent shape for `nextThing` and `nextThings`.
- Explain why `nil` parses to `Nil`, not `Symbol "nil"`.
- Explain how parenthesized Lisp lists become nested `Cons` chains.

## Key ideas (textbook)
- Hickey Ch. 10 `Input and Output`: scanner reads from input channels, manages end-of-file.
- Hickey Ch. 11-12: scanner and parser are module-shaped pieces with small public interfaces.
- Hickey Ch. 19 `Syntax`: scanning separates lexemes/tokens from later syntactic structure.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4|Ch. 4]] and Hickey Ch. 6: parser output is built through pattern matching and recursive union constructors.

## Concepts created / updated today
- [[OCaml - Scanners and Tokens]]
- [[OCaml - Recursive Descent Parsing]]

## Lecture
### Week 10 lecture map - scanner to parser to `thing`
Week 10 turns "Lisp code is data" into a concrete input pipeline. The scanner consumes characters and produces tokens. The parser consumes tokens and produces `thing` values. The important exam skill is to explain why those two stages are separate.

Source anchors:
- `Lecture - 24.txt` begins the code for reading Lisp expressions. This is scanner territory: character input, comments, whitespace, parentheses, numbers, and symbols.
- `Lecture - 25.txt` continues scanner helper mechanics. Each helper consumes exactly the characters that belong to one token and leaves the scanner ready for the next token.
- `Lecture - 26.txt` develops the parser and recursive descent structure. The parser operates on tokens, not characters, because syntactic structure should not also have to classify raw input.
- `Labs/project-2/scanner.ml` defines the scanner module and `token` constructors.
- `Labs/project-2/project2.ml` defines `Parserish`, `Parser`, `initialize`, `nextThing`, `nextThings`, and the `Can'tParse` boundary.

The core invariant for the parser:
- Before `nextThing` starts, the lookahead token is the first token of one Lisp expression.
- After `nextThing` returns, the lookahead token is the first token after that expression.
- `nextThings` handles the inside of a parenthesized list and stops when it sees `CloseParenToken`.

### Mar 30 — Reading Lisp Expressions (Scanner)
Sources: `Lecture - 24.txt`, professor notes `30Mar26/`, `Labs/Practice/scanner.ml`, `Labs/project-2/scanner.ml`.

The lecture defines a token as a meaningful sequence of characters from a program. A real compiler or interpreter does not want the whole system to reason about individual characters; the scanner does that once, then the rest of the interpreter works with token values.

The scanner is stage one. It reads characters from a file and returns token values:
```ocaml
type token =
  CloseParenToken |
  EndToken |
  NumberToken of int |
  OpenParenToken |
  SymbolToken of string ;;
```

Scanner keeps mutable state:
```ocaml
let input = ref stdin ;;
let ch = ref ' ' ;;
```

This isn't the point of the course by itself — it's used because scanning is naturally sequential: read a character, classify it, advance, repeat. One of the places where OCaml code intentionally uses references to model a moving cursor.

### Apr 1 — Scanner Helpers
Sources: `Lecture - 25.txt`, professor notes `01Apr26/`, `Labs/Practice/scanner.ml`.

The lecture's scanner convention is precise: every helper starts with `ch` positioned at the first character of its token, consumes all characters belonging to that token, leaves `ch` at the first character after the token, and returns a token constructor. That convention is why the dispatcher can stay simple.

`nextToken` is the dispatcher. Checks current character, chooses the helper:
- `nextCloseParenToken`, `nextOpenParenToken`
- `nextComment` (semicolons)
- `nextEndToken`
- `nextNumberToken`, `nextSymbolToken`

Whitespace and comments are skipped. Digits and `-` may start number tokens, but if accumulated characters don't parse as an integer, scanner returns a symbol token.

**Mistake to watch:** consuming too much or too little input. Every helper must leave the scanner positioned at the first character *after* the token it just returned.

### Apr 3 — Parser and Recursive Descent
Sources: `Lecture - 26.txt`, professor notes `03Apr26/`, `Labs/project-2/project2.ml`.

The parser is described as a function that reads a Lisp expression and returns the internal form. The syntax diagram named `thing` has alternatives for parenthesized lists, numbers, and symbols. Parentheses delimit lists, but the parser's output is not parentheses; it is nested `Cons` and `Nil`.

The parser reads tokens and produces `thing` values. Recursive descent shape:

```ocaml
let rec nextThings () =
  match !token with
  | CloseParenToken -> nextToken (); Nil
  | EndToken -> raise (Can'tParse "...")
  | _ -> let first = nextThing () in Cons (first, nextThings ())

and nextThing () =
  match !token with
  | NumberToken n -> nextToken (); Number n
  | SymbolToken "nil" -> nextToken (); Nil
  | SymbolToken s -> nextToken (); Symbol s
  | OpenParenToken -> nextToken (); nextThings ()
  | CloseParenToken | EndToken -> raise (Can'tParse "...")
```

**The key invariant:** when a parser function starts, `token` is the first token of the expression it will parse. When it returns, `token` is the first token *after* that expression. This invariant is what lets the parser read a whole file expression by expression.

**`SymbolToken "nil"` → `Nil`**: special case. Not `Symbol "nil"`.

**`(a b c)`** becomes `Cons (Symbol "a", Cons (Symbol "b", Cons (Symbol "c", Nil)))`.

## Labs / Projects
### Project 2 — Lisp Parser
See: [[Project - 2 Lisp Parser|Project - 2 Lisp Parser]]

Uses `Labs/project-2/scanner.ml`, `project2.ml`, `testParser.ml`, and property tests.

## Examples worth keeping
- Token constructors: `OpenParenToken`, `CloseParenToken`, `EndToken`, `NumberToken`, `SymbolToken`.
- `SymbolToken "nil" -> Nil` — special parser case.
- `(a b c)` → `Cons (Symbol "a", Cons (Symbol "b", Cons (Symbol "c", Nil)))`.
- `nextThings` stops when it sees `CloseParenToken`.
- End of input inside a list → parser error.

## Takeaways (questions to resolve)
- [ ] What problem does the scanner solve before parsing begins? (characters → tokens)
- [ ] What token does `nil` become, and what `thing` does it become? (`SymbolToken "nil"` → `Nil`)
- [ ] What invariant does the parser maintain about `token`?
- [ ] Why are `nextThing` and `nextThings` mutually recursive?
- [ ] What error should happen if a list reaches `EndToken` before `CloseParenToken`?

## Flashcards
#cards/CSCI2041
- Scanner output type::`token` — one of `CloseParenToken`, `EndToken`, `NumberToken of int`, `OpenParenToken`, `SymbolToken of string`.
- Parser output type::`thing` — the same ADT used by the evaluator and printer.
- What does `SymbolToken "nil"` parse to::`Nil`, not `Symbol "nil"`. Special case in the parser.
- What does `nextThings` build::A right-nested `Cons` chain ending in `Nil` — one `Cons` per element until `CloseParenToken`.
- What is the parser's token invariant::On entry, `!token` is the first token of the expression to parse. On exit, `!token` is the first token after that expression.
- What is recursive descent parsing::Parsing by functions that mirror the grammar's recursive structure — each grammar rule becomes a function.
