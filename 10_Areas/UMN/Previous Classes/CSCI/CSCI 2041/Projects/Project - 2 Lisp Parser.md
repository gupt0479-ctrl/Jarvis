---
type: class
input_kind: project
status: sprout
created: 2026-05-08
updated: 2026-05-08
area:
  - "[[CSCI 2041 Board]]"
tags:
  - "#class"
  - "#project"
next:
---

# Project - 2 Lisp Parser

## Project Goal
Project 2 tests the scanner/parser boundary in the Lisp interpreter. The goal is to read Lisp source text from a file, turn characters into tokens, and turn those tokens into nested `thing` values.

This is the project version of [[OCaml - Recursive Descent Parsing]], [[OCaml - Scanners and Tokens]], [[OCaml - Lisp Thing Representation]], [[OCaml - Modules and Signatures]], [[OCaml - Mutual Recursion]], and [[OCaml - Exceptions and Error Boundaries]]. It is introduced in [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 10]], continued in [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 11]], and reviewed in [[Week - 15]].

## File Map
- `Labs/project-2/project2.ml`: defines `thing`, `environment`, `Parserish`, an embedded `Scanner` module, and `Parser : Parserish`.
- `Labs/project-2/scanner.ml`: professor-style scanner module using `Scannerish`, `input : in_channel ref`, `ch : char ref`, and character-by-character helpers.
- `Labs/project-2/testParser.ml`: manual parser smoke test for `factorial.lsp`; shows the expected nested `Cons` output.
- `Labs/project-2/test_integration.ml`: integration test comparing parsed factorial output to a hand-written expected `thing`; also checks that another `nextThing` at EOF raises `Parser.Can'tParse`.
- `Labs/project-2/test_property1.ml`: property test that printing a parser-producible `thing` to Lisp syntax and parsing it back preserves structure.
- `Labs/project-2/test_property2.ml`: property test that sequential parsing advances the token correctly across multiple expressions in one file.
- `Labs/project-2/test_property3.ml`: property test that any parsed parenthesized list is a proper `Cons` chain ending in `Nil`.
- `Labs/project-2/factorial.lsp`: Lisp factorial definition used by the manual and integration tests.

Important source distinction: `scanner.ml` is the professor scanner source, but `project2.ml` also defines its own `module Scanner` using a full-file string and `index` ref. The `Parser` inside `project2.ml` refers to the embedded `Scanner` defined immediately above it.

## Data Model
### `thing` and `environment`
```ocaml
type thing =
  Closure of thing * thing * environment |
  Cons of thing * thing |
  Nil |
  Number of int |
  Primitive of (thing -> environment -> thing) |
  Symbol of string
and environment = (string * thing) list ;;
```

The parser produces only:
- `Cons`
- `Nil`
- `Number`
- `Symbol`

`Closure` and `Primitive` are included because this `thing` type belongs to the larger interpreter, but Project 2's parser does not create closures or primitive functions from source text.

### `token`
The token type appears in the embedded scanner in `project2.ml`:

```ocaml
type token =
  EndToken |
  OpenParenToken |
  CloseParenToken |
  NumberToken of int |
  SymbolToken of string ;;
```

The professor scanner in `scanner.ml` uses the same conceptual token set, ordered as `CloseParenToken`, `EndToken`, `NumberToken`, `OpenParenToken`, `SymbolToken`.

### `Parserish`
```ocaml
module type Parserish =
sig
  exception Can'tParse of string ;;
  val initialize : string -> unit ;;
  val nextThing : unit -> thing ;;
end ;;
```

This signature hides parser state and helpers. Outside code can initialize a file, ask for the next parsed `thing`, and catch `Can'tParse`.

## Main Functions
### `Scanner.initialize`
In `project2.ml`, `Scanner.initialize path` opens the file, reads the entire file into a string, resets `index` to `0`, and closes the channel.

```ocaml
let initialize path =
  let ic = open_in path
  in let len = in_channel_length ic
  in input := really_input_string ic len ;
     index := 0 ;
     close_in ic ;;
```

In `scanner.ml`, `initialize` instead opens an input channel and calls `nextChar ()` once to set up the current-character ref.

### `Scanner.nextToken`
In `project2.ml`, `nextToken` skips whitespace, peeks at the current character, and returns one token:
- end of input -> `EndToken`
- `(` -> `OpenParenToken`
- `)` -> `CloseParenToken`
- otherwise read a symbol-like lexeme, then try `int_of_string`; success gives `NumberToken n`, failure gives `SymbolToken lexeme`

The professor scanner in `scanner.ml` is more detailed: it has helpers for close paren, open paren, comments, EOF, number tokens, symbol tokens, and a dispatcher `nextToken`.

### `Parser.initialize`
`Parser.initialize path` calls `Scanner.initialize path`, then immediately calls `nextToken ()` so `token` holds the first lookahead token before parsing begins.

```ocaml
let initialize path =
  Scanner.initialize path ;
  nextToken () ;;
```

### `nextToken`
Inside `Parser`, `nextToken` is a hidden helper:

```ocaml
let nextToken () =
  token := Scanner.nextToken () ;;
```

It advances the one-token lookahead.

### `nextThing`
`nextThing` parses one Lisp expression from the current token:
- `CloseParenToken`: error, because `)` cannot start an expression.
- `EndToken`: error, because there is no expression left.
- `NumberToken n`: advance and return `Number n`.
- `OpenParenToken`: advance past `(`, then parse a list with `nextThings`.
- `SymbolToken "nil"`: advance and return `Nil`.
- `SymbolToken s`: advance and return `Symbol s`.

`nil` must be checked before the general symbol case, or it will parse incorrectly as `Symbol "nil"`.

### `nextThings`
`nextThings` parses zero or more expressions inside a parenthesized list:
- `CloseParenToken`: advance past `)` and return `Nil`.
- `EndToken`: raise `Can'tParse`, because the list was never closed.
- otherwise: parse one `thing`, recursively parse the rest, and return `Cons (first, rest)`.

```ocaml
let rec nextThings () =
  match ! token
  with Scanner.CloseParenToken ->
         nextToken () ;
         Nil |
       Scanner.EndToken ->
         raise (Can'tParse "Ran out of tokens before list was closed.") |
       _ ->
         let first = nextThing ()
         in Cons (first, nextThings ())
```

### Why `nextThing` and `nextThings` are mutually recursive
They call each other because the grammar is recursive:
- A thing can be a parenthesized list.
- A parenthesized list contains zero or more things.

That is why the source uses:

```ocaml
let rec nextThings () = ...
and nextThing () = ...
```

## Control Flow
1. File contents begin in `factorial.lsp` or another Lisp source file.
2. `Parser.initialize path` initializes `Scanner` and reads the first token.
3. `Parser.nextThing ()` inspects the current lookahead token.
4. Numbers become `Number n`.
5. Symbols become `Symbol s`, except `"nil"` becomes `Nil`.
6. `(` begins a recursive list parse through `nextThings`.
7. `nextThings` builds a nested `Cons` chain until it sees `CloseParenToken`.
8. The final output is a `thing` value representing the Lisp expression.

Pipeline:

```text
file contents -> scanner tokens -> parser lookahead -> nested thing value
```

Example:

```lisp
(a nil 3)
```

parses as:

```ocaml
Cons (Symbol "a",
  Cons (Nil,
    Cons (Number 3, Nil)))
```

## Tests / Expected Behavior
### `testParser.ml`
This is the manual smoke test. It runs:

```ocaml
Parser.initialize "factorial.lsp" ;;
Parser.nextThing () ;;
```

The expected result is the nested `Cons` representation of:

```lisp
(define !
  (lambda (n)
    (if (= n 0)
        1
        (* n (! (- n 1))))))
```

The first part of the expected value begins:

```ocaml
Cons (Symbol "define",
  Cons (Symbol "!",
    Cons (Cons (Symbol "lambda", ...), Nil)))
```

### `test_integration.ml`
This test defines `thingEqual`, builds the full expected factorial `thing`, parses `factorial.lsp`, and prints a pass/fail message based on structural equality. It also calls `Parser.nextThing ()` a second time and expects `Parser.Can'tParse _` at end of file.

### Property test 1: round-trip parsing preserves structure
`test_property1.ml` generates random parser-producible `thing` values using only `Cons`, `Nil`, `Number`, and `Symbol`, prints each one to Lisp syntax, writes it to a temp file, parses it back, and checks structural equality. This validates atom parsing, list parsing, nested parsing, and parenthesis consumption.

### Property test 2: sequential parsing advances token correctly
`test_property2.ml` generates several random `thing` values, writes all of them to one temp file separated by newlines, initializes the parser once, and calls `nextThing ()` repeatedly. Each parsed result must match the corresponding generated value. This tests the lookahead invariant: after one expression returns, `token` must point at the first token after that expression.

### Property test 3: proper list invariant
`test_property3.ml` generates random parenthesized list expressions containing atoms, parses each one, and checks `isProperList`. The parsed value must be a chain of `Cons` cells whose `cdr` eventually reaches `Nil`.

## Concepts Used
- [[OCaml - Scanners and Tokens]]
- [[OCaml - Recursive Descent Parsing]]
- [[OCaml - Lisp Thing Representation]]
- [[OCaml - Modules and Signatures]]
- [[OCaml - Mutual Recursion]]
- [[OCaml - Exceptions and Error Boundaries]]
- [[OCaml - Algebraic Data Types and Structural Recursion]]
- [[OCaml - Pattern Matching]]
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 10]]
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 11]]
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 12]]
- [[Week - 15]]

## Common Mistakes
- Parsing characters directly in `Parser` instead of consuming scanner tokens.
- Forgetting to initialize the scanner and then read the first token before parsing.
- Matching `SymbolToken s` before `SymbolToken "nil"`.
- Returning `Symbol "nil"` instead of `Nil`.
- Forgetting to advance past `OpenParenToken` before parsing the list body.
- Forgetting to advance past `CloseParenToken` when ending a list.
- Treating `EndToken` inside `nextThings` as an empty list instead of a parse error.
- Forgetting that `nextThing` and `nextThings` must be mutually recursive.
- Building `Cons (first, rest)` incorrectly so lists do not terminate in `Nil`.
- Confusing the professor `scanner.ml` module with the embedded `Scanner` module inside `project2.ml`.

## Representative Code
```ocaml
module type Parserish =
sig
  exception Can'tParse of string ;;
  val initialize : string -> unit ;;
  val nextThing : unit -> thing ;;
end ;;
```

```ocaml
let token = ref Scanner.EndToken ;;

let nextToken () =
  token := Scanner.nextToken () ;;
```

```ocaml
and nextThing () =
  match ! token
  with Scanner.CloseParenToken ->
         raise (Can'tParse "Got ) when expecting an expression.") |
       Scanner.EndToken ->
         raise (Can'tParse "Nothing left to parse.") |
       Scanner.NumberToken n ->
         nextToken () ;
         Number n |
       Scanner.OpenParenToken ->
         nextToken () ;
         nextThings () |
       Scanner.SymbolToken "nil" ->
         nextToken () ;
         Nil |
       Scanner.SymbolToken s ->
         nextToken () ;
         Symbol s ;;
```

```ocaml
let rec thingEqual a b =
  match (a, b)
  with (Nil, Nil) -> true |
       (Number m, Number n) -> m = n |
       (Symbol s, Symbol t) -> s = t |
       (Cons (aHead, aTail), Cons (bHead, bTail)) ->
         thingEqual aHead bHead && thingEqual aTail bTail |
       (_, _) -> false ;;
```

## Study Checklist
- [ ] Can I write the `thing` and `environment` types from memory?
- [ ] Can I explain which `thing` constructors the parser can actually produce?
- [ ] Can I list the token constructors?
- [ ] Can I explain why parser works with tokens, not characters?
- [ ] Can I explain one-token lookahead?
- [ ] Can I trace `Parser.initialize` through the first call to `nextToken`?
- [ ] Can I trace `nextThing` on `NumberToken 3`?
- [ ] Can I trace `nextThing` on `SymbolToken "nil"`?
- [ ] Can I trace `nextThing` on `OpenParenToken`?
- [ ] Can I explain why `nextThings` stops at `CloseParenToken`?
- [ ] Can I explain every `Can'tParse` case?
- [ ] Can I draw the `Cons` chain for `(a nil 3)`?
- [ ] Can I explain what `testParser.ml` expects for `factorial.lsp`?
- [ ] Can I explain the purpose of each property test?
