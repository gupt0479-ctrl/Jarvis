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

# OCaml - Lisp Printer

- The Lisp printer turns internal `thing` values back into readable Lisp syntax.

## 30-Second Explanation
- `Labs/lab10.ml` defines `printThing`, `printingThing`, and `printingThings`. The printer must display atoms directly, print proper `Cons` chains with parentheses and spaces, and hide implementation-heavy values like closures and primitives behind `[Closure]` and `[Primitive]`.

## Teach It To A Beginner
- Parser goes from text to `thing`; printer goes from `thing` back to text. It is not enough to print OCaml constructors. The source tests demand Lisp-looking output: `Cons (Symbol "a", Cons (Symbol "b", Nil))` prints as `(a b)`.
- The printer is mutually recursive because lists contain things, and things can themselves be lists.
- Tests in `Labs/tests10.ml` are precise about spaces, newlines, and case.

```ocaml
and printingThings things =
  match things with
  | Nil -> ()
  | Cons (first, Nil) -> printingThing first
  | Cons (first, rest) ->
      printingThing first;
      printf " ";
      printingThings rest
  | _ -> failwith "printingThings expected a proper list" ;;
```

## Definition
- Printer: the component that converts internal interpreter values into visible text.
- Proper list printing: print a `Cons` chain ending in `Nil` as parenthesized elements separated by single spaces.

## Mental Model
- Atom: print itself.
- List: open parenthesis, print elements, close parenthesis.
- Closure/primitive: print a placeholder because their internals are not Lisp surface syntax.

## Contrast With
- [[OCaml - Recursive Descent Parsing]]: parser reads syntax into structure; printer writes structure into syntax.
- [[OCaml - Lisp Thing Representation]]: printer is a consumer of `thing`.
- OCaml `printf "%s"` on constructors: not available for arbitrary ADTs; the course printer defines the display rules.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 13]], [[Week - 15]].
- Labs: [[Lab - 10 Lisp Printer]], [[Lab - 12 Lisp Integration]].
- Projects: [[Project - 2 Lisp Parser]] output can be checked with the Lab 10 printer.
- Textbook: Hickey Ch. 4, Ch. 6, Ch. 11-12.

## Common Mistakes
- Printing extra spaces before `)`.
- Forgetting the newline in `printThing`.
- Printing nested lists without recursive calls to `printingThing`.
- Trying to print improper lists as if they were valid proper lists.

## Diagnostic Questions
- Why does `printingThings` stop on `Nil`?
- What should a `Closure` print as?
- Why does `(a (b c))` require both printer helpers?
- What would the printer output for the factorial definition?

## Mini-Test
- [ ] Print `Cons (Symbol "a", Cons (Symbol "b", Nil))` by hand.
- [ ] Explain why `printingThings` fails on a non-list rest.
- [ ] Write the branch for `Primitive _`.

## Flashcards
#cards/CSCI2041
- What does Lab 10 print for `Nil`::`nil`.
- What does it print for a closure::`[Closure]`.
- What does it print for a primitive::`[Primitive]`.
- Why are printer functions mutually recursive::Things can be lists, and lists contain things.
- What file tests exact printer output::`Labs/tests10.ml`.
