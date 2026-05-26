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

# OCaml - Mutual Recursion

- Mutual recursion defines functions together because they call each other.

## 30-Second Explanation
- The final review asks about mutually recursive functions versus embedded helpers. Lab 10's printer shows the real course pattern: `printThing`, `printingThing`, and `printingThings` are defined with `and` because thing-printing and list-printing call each other.

## Teach It To A Beginner
- OCaml needs to know about recursive names when the functions are defined. `let rec f ... and g ...` binds them as a group, so `f` can call `g` and `g` can call `f`.
- Lab 10 needs this because a Lisp `thing` may be a list, and a Lisp list contains more `thing` values. Printing a thing can require printing a list; printing a list can require printing a thing.
- Textbook connection: Hickey Ch. 3 covers recursive and mutually recursive functions.

```ocaml
let rec printThing thing =
  printingThing thing;
  printf "\n"

and printingThing thing =
  match thing with
  | Cons (_, _) as things ->
      printf "(";
      printingThings things;
      printf ")"
  | Nil -> printf "nil"
  | Number n -> printf "%i" n

and printingThings things =
  match things with
  | Nil -> ()
  | Cons (first, rest) ->
      printingThing first;
      printingThings rest
  | _ -> failwith "printingThings expected a proper list" ;;
```

## Definition
- Mutually recursive functions are functions in the same recursive binding group where at least one function calls another in the group.
- OCaml uses `and` to define these functions together.

## Mental Model
- Single recursion: one loop path.
- Mutual recursion: two or more functions hand work back and forth.
- Course pattern: one function handles an outer syntactic category; another handles a nested syntactic category.

## Contrast With
- [[OCaml - Tail Recursion and Internal Helpers]]: a helper inside a function can use outer variables but does not require another top-level recursive peer.
- [[OCaml - Recursive Descent Parsing]]: `nextThing` and `nextThings` are mutually recursive because things contain lists and lists contain things.
- Plain helper functions: if the helper is called only one direction, `and` may not be needed.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 10]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[Week - 15]].
- Labs: [[Lab - 10 Lisp Printer]], [[Lab - 12 Lisp Integration]].
- Projects: [[Project - 2 Lisp Parser]] uses `nextThings` and `nextThing`.
- Textbook: Hickey Ch. 3.

## Common Mistakes
- Forgetting `and`, causing an unbound function error.
- Using mutual recursion when a nested helper would be clearer.
- Making both functions too broad; each should own a distinct shape.
- Forgetting a base case in one member of the recursive group.

## Diagnostic Questions
- Why can `printingThing` and `printingThings` not be independent?
- What does `and` do in an OCaml `let rec` group?
- Why are `nextThing` and `nextThings` mutual in the parser?
- Which base cases stop the Lab 10 printer?

## Mini-Test
- [ ] Write `even` and `odd` as mutually recursive functions.
- [ ] Explain the call chain for printing `(a (b c))`.
- [ ] Identify whether a recursive pair should be mutual or nested-helper style.

## Flashcards
#cards/CSCI2041
- What keyword connects mutually recursive OCaml functions::`and`.
- Why does Lab 10 need mutual recursion::Things can be lists, and lists contain things.
- What is the parser mutual-recursion pair::`nextThing` and `nextThings`.
- What is the main danger of missing a base case::Infinite recursion or failure on valid input.
- What week reviews this distinction explicitly::[[Week - 15]].
