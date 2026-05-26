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

# OCaml - Algebraic Data Types and Structural Recursion

- Algebraic data types define the shapes a value can have; structural recursion follows those shapes exactly.

## 30-Second Explanation
- Week 6 onward keeps using constructor-shaped data: Project 1's `expression`, Lab 9's `thing`, Lab 11's expanded `thing`, and Week 14's `proposition`. The correct recursive function almost always has one branch per constructor and recursive calls on the constructor's subparts.

## Teach It To A Beginner
- If the data is a tree, the function should look like a tour of the tree. For `Var`, stop. For `Add (l, r)`, recurse on `l` and `r`. For `Cons (first, rest)`, handle the first item and recurse on the rest. The type tells you the cases you cannot ignore.
- Textbook connection: Hickey Ch. 4 pattern matching and Ch. 6 unions are the backbone.
- Lecture connection: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 7]] uses expression trees for Project 1; [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 9]] uses Lisp data; [[Week - 14]] uses proposition trees.

```ocaml
type expression =
  Var of string
| Neg of expression
| Add of expression * expression
| Div of expression * expression
| Equ of expression * expression
| Mul of expression * expression
| Sub of expression * expression ;;

let rec isInside name expr =
  match expr with
  | Var x -> x = name
  | Neg e -> isInside name e
  | Add (l, r)
  | Sub (l, r)
  | Mul (l, r)
  | Div (l, r)
  | Equ (l, r) -> isInside name l || isInside name r ;;
```

## Definition
- An algebraic data type is a type defined by named constructors, where each constructor may carry zero or more fields.
- Structural recursion is recursion organized by pattern matching on those constructors and recursively processing contained values of the same type.

## Mental Model
- The type definition is a map.
- Each constructor is a road.
- A correct recursive function visits every road that matters and recurses only into same-type substructures.

## Contrast With
- String processing: interpreters in this course turn text into structured values, then recurse over constructors instead of slicing strings.
- [[OCaml - Recursive Descent Parsing]]: parser recursion follows grammar shape; structural recursion follows data shape.
- [[OCaml - Tail Recursion and Internal Helpers]]: structural recursion is about shape; tail recursion is about call position and accumulator design.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 7]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 9]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 10]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[Week - 13]], [[Week - 14]], [[Week - 15]].
- Labs: [[Lab - 9 Lisp Data Recursion]], [[Lab - 10 Lisp Printer]], [[Lab - 11 Lisp Evaluator]], [[Lab - 12 Lisp Integration]].
- Projects: [[Project - 1 Equation Solver]], [[Project - 2 Lisp Parser]].
- Textbook: Hickey Ch. 4 and Ch. 6.

## Common Mistakes
- Missing a constructor case.
- Recursing into only one side of a binary constructor.
- Treating `Cons` like OCaml `::` instead of the course's Lisp constructor.
- Returning `Nil` for an atom in a transformation that should leave atoms unchanged.

## Diagnostic Questions
- What are the constructors of Project 1's `expression` type?
- Which constructors in `thing` are atoms?
- Why does `substitute` need to recurse through both parts of `Cons` if it is a true tree substitution?
- What changes when `thing` gains `Closure` and `Primitive`?

## Mini-Test
- [ ] Write `size_expression : expression -> int`.
- [ ] Write a `contains_symbol` over Lab 9 `thing`.
- [ ] Explain why a missing `Cons` branch breaks most interpreter functions.

## Flashcards
#cards/CSCI2041
- What is an ADT constructor::A named way to build a value of a union type.
- What is structural recursion::Recursion that follows the constructors of the data.
- Which textbook chapters support this concept::Hickey Ch. 4 and Ch. 6.
- What Project 1 function demonstrates structural recursion::`isInside`.
- What later source reuses the same idea::Lisp `thing` and if-based `proposition`.
