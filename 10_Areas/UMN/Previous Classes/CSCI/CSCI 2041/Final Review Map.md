---
type: class
input_kind: review
status: sprout
created: 2026-05-08
updated: 2026-05-09
area:
  - "[[CSCI 2041 Board]]"
tags:
  - "#class"
  - "#review"
next:
---
# CSCI 2041 Final Review Map
This map is organized for the open-notes final: what I need to be able to reproduce on paper, explain under time pressure, and trace through code. Use it with [[CSCI 2041 Board]], [[Week - 15]], and the concept notes under `Concepts/`.
## Core OCaml Skills
- *Pattern matching*: be able to read constructor matches, tuple matches, multi-value matches, and parameter-list patterns. Drill [[OCaml - Algebraic Data Types and Structural Recursion]], [[OCaml - Lisp Thing Representation]], and [[OCaml - If Normalization and Tautology Checking]].
- *Recursion*: know ordinary structural recursion, tail recursion with an internal helper, mutual recursion with `and`, and recursive traversal of trees/lists. Drill [[OCaml - Tail Recursion and Internal Helpers]], [[OCaml - Mutual Recursion]], [[OCaml - Recursive Descent Parsing]], and [[OCaml - Lisp Printer]].
- *Exceptions*: create an exception with payloads, raise it, and catch it with `try ... with`. Drill [[OCaml - Exceptions and Error Boundaries]].
- *Higher-order functions*: recognize functions as stored values, callbacks, primitive builders, and continuations. Drill [[OCaml - Higher-Order Functions]] and [[OCaml - Continuation Passing]].
- *Types and ADTs*: define recursive types with `and`; explain why `thing` and `environment` are mutually recursive. Drill [[OCaml - Lisp Thing Representation]], [[OCaml - Environments and Closures]], and [[OCaml - Algebraic Data Types and Structural Recursion]].
- *Lazy evaluation*: explain the idea, closure-simulated laziness from [[OCaml - Streams]], and OCaml `Lazy.t`, `lazy`, and `force` from [[OCaml - Lazy Evaluation]].
- *Modules*: define a module, a signature/module type, and use `module M : S` to hide internals. Drill [[OCaml - Modules and Signatures]], [[OCaml - Scanners and Tokens]], and [[OCaml - Recursive Descent Parsing]].
- *Mathematical transformations to OCaml*: translate rewrite rules into pattern matching and smart constructors. Drill [[OCaml - If Normalization and Tautology Checking]] and [[OCaml - Expression Trees and Equation Solving]].
- *Interpreter architecture*: know scanner -> parser -> printer/evaluator -> REPL. Drill [[OCaml - Lisp Integration and REPL]], [[OCaml - Lisp Evaluator]], and [[OCaml - Interpreter Primitives and Special Forms]].
## Week-by-Week Study Path
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 6]]: streams, functions inside data, closure/object-style behavior. Be able to write `makeStream`, `first`, `rest`, and `take`.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 7]]: memoization, Project 1 expression solving, first lazy-list setup. Be able to explain cached recursion and structural equation inversion.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 8]]: lazy lists, eager vs lazy evaluation, modules/signatures, association module. Be able to hide module internals with a signature.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 9]]: Lisp `thing`, `Cons`, `Nil`, structural recursion over Lisp data. Be able to represent Lisp lists as OCaml values.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 10]]: scanner and parser. Be able to explain tokens, current-token state, `nextThing`, and `nextThings`.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 11]]: Project 2 parser, Lisp printer, evaluator primitives, short-circuit behavior. Be able to trace `car`, `cdr`, `cons`, `and`, `or`, and `makeRelation`.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 12]]: environments, `define`, `lambda`, closures, and `apply`. This is the highest priority interpreter week.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13]]: metaprogramming/macros, final Lisp integration, REPL scaffold, start of if-based tautology.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 14]]: if-normalized tautology checker and CPS permutation example. Be able to explain `makeIf`, `normalize`, `substitute`, and continuation callbacks.
- [[Week - 15]]: final review. Use it as the route map for mutual recursion vs internal helpers and the full interpreter pipeline.
## Lab Skills
- [[Lab - 5 Streams]]: tests [[OCaml - Streams]] and [[OCaml - Higher-Order Functions]]. Reproduce `odds`, `trim`, `scale`, `sum`, and explain why `take` terminates on an infinite stream.
- [[Lab - 6 Memoization]]: tests [[OCaml - Memoization]] and [[OCaml - References and Mutation]]. Explain why `c 40 10` is slow and `memyC 40 10` is fast.
- [[Lab - 7 Lazy Lists]]: tests [[OCaml - Lazy Evaluation]]. Reproduce `LazyNode`, `lazyHead`, `lazyTail`, `lazyTake`, and know when `force` runs.
- [[Lab - 8 Association Module]]: tests [[OCaml - Modules and Signatures]], [[OCaml - Association Lists]], and [[OCaml - Exceptions and Error Boundaries]]. Explain `make`, `put`, `get`, `delete`, and `NoSuchKey`.
- [[Lab - 9 Lisp Data Recursion]]: tests [[OCaml - Lisp Thing Representation]], [[OCaml - Lisp Lists and Cons]], and [[OCaml - Algebraic Data Types and Structural Recursion]]. Trace `every`, `substitute`, and `questyEqual`.
- [[Lab - 10 Lisp Printer]]: tests [[OCaml - Lisp Printer]] and [[OCaml - Mutual Recursion]]. Print `Nil`, atoms, closures/primitives, and nested proper lists exactly.
- [[Lab - 11 Lisp Evaluator]]: tests [[OCaml - Lisp Evaluator]], [[OCaml - Environments and Closures]], and [[OCaml - Interpreter Primitives and Special Forms]]. Highest priority lab for the final.
- [[Lab - 12 Lisp Integration]]: tests [[OCaml - Lisp Integration and REPL]], modules, scanner/parser/printer/evaluator integration, and command-line REPL structure.

## Project Skills
- [[Project - 1 Equation Solver|Project - 1 Equation Solver]]: proves I understand [[OCaml - Expression Trees and Equation Solving]], ADTs, pattern matching, recursive tree search, inverse transformations, and exception boundaries. Be able to explain `isInside`, `solver`, and `solve`.
- [[Project - 2 Lisp Parser|Project - 2 Lisp Parser]]: proves I understand [[OCaml - Scanners and Tokens]], [[OCaml - Recursive Descent Parsing]], [[OCaml - Lisp Thing Representation]], module signatures, one-token lookahead, and proper `Cons` list construction.

## Concepts To Drill
- Must be automatic: [[OCaml - Exceptions and Error Boundaries]], [[OCaml - Mutual Recursion]], [[OCaml - Lisp Thing Representation]], [[OCaml - Scanners and Tokens]], [[OCaml - Recursive Descent Parsing]], [[OCaml - Lisp Evaluator]], [[OCaml - Environments and Closures]], [[OCaml - Interpreter Primitives and Special Forms]].
- Likely weak areas: `try ... with`, exceptions carrying strings, `match` over two values, parameter-list pattern matching, scanner helper details (`open_in`, `input_char`, `Char.escaped` or `String.make`, `int_of_string`, `^`), why `!global` enables mutually recursive Lisp functions, and how `apply` separates `argsEnv` from `bodyEnv`.
- Paper-note priorities: print the `thing` type, the scanner token type, the evaluator dispatcher, `apply`, `makeRelation`, and the parser `nextThing`/`nextThings` skeleton.
- Cumulative data-structure review: use earlier notes for big O, sorting, rational numbers, stacks, queues, binary trees, BSTs, and linked lists. From Week 6 onward, the most relevant links are [[OCaml - Association Lists]], [[OCaml - Algebraic Data Types and Structural Recursion]], and [[OCaml - Tail Recursion and Internal Helpers]].

## Code Patterns To Reproduce From Memory

### Exceptions
```ocaml
exception Can'tParse of string ;;

raise (Can'tParse "Unexpected token") ;;

try
  Parser.nextThing ()
with
| Parser.Can'tParse message -> Nil ;;
```

### Mutual Recursion
```ocaml
let rec even n =
  n = 0 || odd (n - 1)
and odd n =
  n <> 0 && even (n - 1) ;;
```

### Mutually Recursive Types
```ocaml
type thing =
  Closure of thing * thing * environment
| Cons of thing * thing
| Nil
| Number of int
| Primitive of (thing -> environment -> thing)
| Symbol of string
and environment = (string * thing) list ;;
```

### Match With Two Values
```ocaml
match (pars, args) with
| (Nil, Nil) -> evaluating body bodyEnv
| (Nil, Cons (_, _)) -> oops "More arguments than parameters"
| (Cons (_, _), Nil) -> oops "Fewer arguments than parameters"
| (Cons (Symbol name, pars), Cons (arg, args)) ->
    applying pars args (envPut name (evaluating arg argsEnv) bodyEnv)
| _ -> oops "Bad application" ;;
```

### Pattern Matching In Parameters
```ocaml
let first ((this, state), next) =
  this ;;
```

### Printing
```ocaml
Printf.printf "%s %i\n" name count ;;
```

### Lazy Evaluation
```ocaml
open Lazy ;;

type 'a lazyList =
  LazyEmpty
| LazyNode of 'a Lazy.t * 'a lazyList Lazy.t ;;

let lazyHead list =
  match list with
  | LazyEmpty -> raise LazyListError
 | LazyNode (head, _) -> force head ;;
```

### Module Type Hiding
```ocaml
module type Parserish =
sig
  exception Can'tParse of string ;;
  val initialize : string -> unit ;;
  val nextThing : unit -> thing ;;
end ;;

module Parser : Parserish =
struct
  let token = ref Scanner.EndToken ;;
  (* helpers hidden here *)
end ;;
```

### Scanner Token Shape
```ocaml
type token =
  CloseParenToken
| EndToken
| NumberToken of int
| OpenParenToken
| SymbolToken of string ;;
```

### Parser Skeleton
```ocaml
let rec nextThings () =
  match !token with
  | Scanner.CloseParenToken -> nextToken (); Nil
  | Scanner.EndToken -> raise (Can'tParse "Unclosed list")
  | _ -> let first = nextThing () in Cons (first, nextThings ())

and nextThing () =
  match !token with
  | Scanner.NumberToken n -> nextToken (); Number n
  | Scanner.OpenParenToken -> nextToken (); nextThings ()
  | Scanner.SymbolToken "nil" -> nextToken (); Nil
  | Scanner.SymbolToken s -> nextToken (); Symbol s
  | Scanner.CloseParenToken -> raise (Can'tParse "Unexpected )")
  | Scanner.EndToken -> raise (Can'tParse "No expression") ;;
```

### Evaluator Dispatcher
```ocaml
let rec evaluating thing env =
  match thing with
  | Cons (func, args) ->
      (match evaluating func env with
       | Closure (pars, body, bodyEnv) -> apply pars args env body bodyEnv
       | Primitive howTo -> howTo args env
       | _ -> oops "Closure or primitive expected")
  | Symbol name -> lookup env name
  | _ -> thing ;;
```

### Primitive Builder
```ocaml
let makeRelation op message =
  fun args env ->
    match args with
    | Cons (left, Cons (right, Nil)) ->
        let left = evaluating left env in
        let right = evaluating right env in
        (match (left, right) with
         | (Number left, Number right) ->
             if op left right then tee else Nil
         | _ -> oops message)
    | _ -> oops message ;;
```

### If Transformation Pattern
```ocaml
let makeIf pi alpha beta =
  match (pi, alpha, beta) with
  | (pi, T, F) -> pi
  | (T, alpha, _) -> alpha
  | (F, _, beta) -> beta
  | _ -> If (pi, alpha, beta) ;;
```

## Common Exam Mistakes
- Explaining laziness as "it is faster" instead of saying what is delayed and when `force` happens.
- Saying a signature is documentation only; it is the visible type/interface of a module.
- Forgetting that parser works with tokens because scanner already handled characters.
- Parsing `nil` as `Symbol "nil"` instead of `Nil`.
- Printing `Cons` using OCaml constructor syntax instead of Lisp syntax.
- Evaluating all arguments to `and`, `or`, `if`, `quote`, `define`, or `lambda`.
- Saying a closure has only parameters and body; it also stores an environment.
- Evaluating closure body in the caller environment instead of the closure environment extended with parameter bindings.
- Forgetting that `define` mutates `!global`, while `let` extends a local environment.
- Losing the difference between mutual recursion with `and` and an internal helper function.

## Practice Questions
- [ ] Create, raise, and catch an exception carrying a string.
- [ ] Write a mutually recursive pair of functions with `and`.
- [ ] Define mutually recursive `thing` and `environment` types.
- [ ] Match on two values at once and explain each branch.
- [ ] Explain how pattern matching in `let first ((this, state), next)` works.
- [ ] Explain what `Printf.printf "%s %i\n" name count` prints.
- [ ] Explain closure-simulated laziness in [[OCaml - Streams]].
- [ ] Explain `Lazy.t`, `lazy`, and `force` in [[OCaml - Lazy Evaluation]].
- [ ] Write a module type and a module constrained by it.
- [ ] Translate one if-transformation rule into OCaml pattern matching.
- [ ] Draw the scanner/parser boundary: characters -> tokens -> `thing`.
- [ ] Trace how `nextThing` parses `(a nil 3)`.
- [ ] Print `Cons (Symbol "a", Cons (Symbol "b", Nil))`.
- [ ] Trace evaluator dispatch for `(+ 2 2)`.
- [ ] Trace `apply` for a one-argument closure.
- [ ] Explain why Lisp global environment enables functions to call each other.
- [ ] Explain why `(and nil (/ 0 0))` should not divide by zero.
- [ ] Explain how `primitive "<" (makeRelation (<) "...")` installs a primitive.
- [ ] Explain the REPL pipeline from input file to printed output.
- [ ] Connect one lab or project to every concept in the "must be automatic" list.

## Flashcards
#cards/CSCI2041
- What is the final exam's main interpreter pipeline::Scanner, parser, evaluator, printer, REPL.
- What are the three parts of a Lisp closure::Parameter list, body, and environment.
- Why does the parser use tokens instead of characters::The scanner has already grouped raw characters into meaningful lexical units.
- What does `define` change::The mutable global environment `!global`.
- Which Lisp primitives need not evaluate all arguments::`and`, `define`, `if`, `lambda`, `or`, and `quote`.
- What does `makeRelation` build::A primitive function that evaluates two numeric arguments, compares them, and returns `t` or `Nil`.
- What keyword defines mutually recursive functions or types::`and`.
- What does a module signature hide::Names not exposed in the signature.
- What does `force` do::Demands the value inside an OCaml lazy computation.
- What does a dispatcher do::Chooses behavior by inspecting the shape of the input value.
