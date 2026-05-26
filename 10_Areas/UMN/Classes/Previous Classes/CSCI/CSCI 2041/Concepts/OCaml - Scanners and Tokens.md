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

# OCaml - Scanners and Tokens

- A scanner reads characters and groups them into tokens so the parser can work with meaningful units.

## 30-Second Explanation
- `Labs/Practice/scanner.ml` and `Labs/project-2/scanner.ml` define `Scannerish` and `Scanner`. The scanner exposes `initialize : string -> unit` and `nextToken : unit -> token`. Internally it tracks the input channel and current character with refs, skips whitespace/comments, and returns tokens such as `OpenParenToken`, `NumberToken 42`, or `SymbolToken "define"`.

## Teach It To A Beginner
- Parsing Lisp directly from characters would mix too many jobs. The scanner does the first cleanup pass: parentheses become parenthesis tokens, digits become number tokens when possible, everything else becomes a symbol token, and end of file becomes `EndToken`.
- The parser should not care whether the number came from characters `'1'`, `'2'`, `'3'`. It should receive `NumberToken 123`.
- Textbook connection: Hickey Ch. 10 supports file input, Ch. 11-12 support module organization, and Ch. 19 supports syntax/scanning.

```ocaml
type token =
  CloseParenToken
| EndToken
| NumberToken of int
| OpenParenToken
| SymbolToken of string ;;
```

## Definition
- Scanner: a lexical analyzer that reads characters from an input source and returns tokens.
- Token: a typed value representing a lexical unit such as an open parenthesis, close parenthesis, number, symbol, or end marker.

## Mental Model
- Characters: raw stream from file.
- Tokens: cleaned-up chunks.
- Parser: consumes tokens, not characters.
- Current-character ref: the scanner's one-character lookahead state.

## Contrast With
- [[OCaml - Recursive Descent Parsing]]: scanning produces tokens; parsing gives tokens structure.
- [[OCaml - Lisp Thing Representation]]: tokens are not Lisp values yet.
- String splitting: the scanner has special cases for comments, parentheses, numbers, and EOF.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 10]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[Week - 13]], [[Week - 15]].
- Labs: [[Lab - 12 Lisp Integration]] includes scanner code.
- Projects: [[Project - 2 Lisp Parser]] depends on `scanner.ml`.
- Textbook: Hickey Ch. 10, Ch. 11, Ch. 12, Ch. 19.

## Common Mistakes
- Consuming one character too many or too few.
- Forgetting to skip whitespace before returning a token.
- Treating `-` as always a number instead of trying `int_of_string` and falling back to symbol.
- Not turning EOF into a stable `EndToken`.

## Diagnostic Questions
- What are the five token constructors?
- Why does the scanner keep `ch` as a ref?
- What does `nextComment` skip?
- Why does `nextNumberToken` sometimes return `SymbolToken chars`?

## Mini-Test
- [ ] Tokenize `(define x -3)` by hand.
- [ ] Explain what `nextToken` should return at EOF.
- [ ] Identify the scanner's public interface.

## Flashcards
#cards/CSCI2041
- What does the scanner read::Characters from a file.
- What does the scanner return::Tokens.
- What token represents end of file::`EndToken`.
- What token represents `(`::`OpenParenToken`.
- Why are scanner helpers hidden::Only initialization and token production belong in the public API.
