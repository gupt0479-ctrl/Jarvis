---
type: class
input_kind: plan
status: sprout
created: 2026-05-06
updated: 2026-05-08
area:
  - "[[CSCI 2041 Board]]"
tags:
  - "#class"
  - "#workflow"
next:
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 6]]"
---
# CSCI 2041 Note Production Plan
## Operating Contract
This plan is the production contract for rebuilding CSCI 2041 into Jarvis. The goal is not to make light weekly summaries. The goal is to turn the local course corpus into a dense, source-grounded OCaml knowledge system where concept notes are the durable source of truth and weekly/lab/project notes point back into those concepts.

Source of truth:
- The only factual sources are files inside `D:\Users\_Anant\20_Progress\Classes\CSCI\CSCI 2041`.
- That includes lecture transcripts, professor notes images/HTML, labs/tests, projects, practice files, Kiro project-2 specs, syllabus images, and `Hickey Textbook.pdf`.
- Existing Jarvis notes may be used for style, frontmatter, links, and continuity. They are not the factual authority when they disagree with the local source folder.
- Do not use internet sources for course content.
- Do not invent missing lecture content. If a professor-note page or transcript does not say it, mark it as unresolved or inferred from a lab/test.

Protected notes:
- Do not modify [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 1]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 2]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 3]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 4]], or [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 5]] unless explicitly requested later.
- Later concept notes may link back to headings inside those weeks, but the Week 1-5 files themselves stay frozen for now.

Live output folder:
- The prompt and source `AGENTS.md` mention `50_Archive/UMN/Classes/CSCI 2041`.
- The current linked Jarvis course folder is `10_Areas/Degree/UMN/Classes/CSCI 2041`.
- Write notes in the live folder linked from [[CSCI 2041 Board]] unless Anant asks to relocate the course.

## Depth Standard

Every final note should be very detailed. "Very detailed" means:
- Every mechanism gets a definition, mental model, code shape, example from the source corpus, and failure mode.
- Every lab/project concept states exactly where it is tested, which functions/types matter, and what mistakes the tests would catch.
- Every lecture idea points to the transcript/professor-note date and, when useful, to a specific weekly heading.
- Every textbook idea states the Hickey chapter/section or PDF outline heading that supports it.
- Every concept note contains interlinks to weeks, labs, projects, textbook notes, and nearby concepts.
- No generic "this is important" prose. Write the mechanism, the contrast, the code behavior, and the test implication.

Minimum sections for a major concept note:
- `## 30-Second Explanations`
- `## Source Anchors`
- `## Mechanism`
- `## OCaml Shape`
- `## Lecture Development`
- `## Textbook Support`
- `## Labs / Projects`
- `## Common Mistakes`
- `## Contrast With`
- `## Diagnostic Questions`
- `## Flashcards`

Concept notes are the canonical layer:
- Weekly notes are reading maps and synthesis.
- Lab notes explain what the tests demand.
- Project notes explain the larger artifact.
- Concept notes preserve the durable detail.
- Labs must be linked from the relevant concept notes.
- Projects get their own detailed project/concept notes, and each project also links to one or more core concepts.

## Source Coverage Requirement

Before drafting any final note, read every source row for that target. Do not rely on this plan alone.

For a weekly note:
1. Read all transcript files listed for that week.
2. Inspect all professor note images/HTML folders listed for that week.
3. Read all matching labs/tests/projects/practice files.
4. Read the relevant `Hickey Textbook.pdf` sections, not just existing Jarvis textbook notes.
5. Build a source map inside the weekly note or in temporary working notes before drafting.

For a concept note:
1. Read every weekly source where the concept appears.
2. Read every lab/test/project file that exercises it.
3. Read the textbook chapter/section that formalizes it.
4. Link back to the exact weekly, lab, project, and textbook headings.

For a lab note:
1. Read `labN.ml`.
2. Read `testsN.ml` when present.
3. Read the related lecture transcript and professor notes.
4. Add the lab under `## Labs / Projects` inside every concept it tests.

For a project note:
1. Read every file in the project folder.
2. Read related practice files and specs.
3. Read the lecture arc that announced and developed the project.
4. Create a project concept note and link it to the core concept notes.

## Complete Source Inventory

Top-level:
- `AGENTS.md`: source-folder production rules.
- `Hickey Textbook.pdf`: textbook source, 284 pages.
- `Syllabus/Weekly Schedule - 1.png`: schedule source through Apr 17.
- `Syllabus/Weekly Schedule - 2.png`: schedule source through final exam.

Lecture transcripts:
- `Lectures/Transcripts/Lecture - 1.txt` through `Lectures/Transcripts/Lecture - 40.txt`.
- `Lecture - 29.txt` and `Lecture - 30.txt` have the same SHA-256 hash. Treat `Lecture - 30.txt` as a duplicate of `Lecture - 29.txt` unless later manual inspection proves otherwise.

Professor lecture notes:
- Single file: `Lectures/Notes/21Jan26.jpg`.
- Dated folders: `26Jan26`, `28Jan26`, `30Jan26`, `02Feb26`, `04Feb26`, `06Feb26`, `09Feb26`, `11Feb26`, `13Feb26`, `16Feb26`, `18Feb26`, `20Feb26`, `23Feb26`, `25Feb26`, `02Mar26`, `04Mar26`, `06Mar26`, `16Mar26`, `18Mar26`, `20Mar26`, `23Mar26`, `25Mar26`, `27Mar26`, `30Mar26`, `01Apr26`, `03Apr26`, `06Apr26`, `08Apr26`, `10Apr26`, `13Apr26`, `15Apr26`, `17Apr26`, `20Apr26`, `22Apr26`, `24Apr26`, `27Apr26`, `29Apr26`, `01May26`.
- `Lectures/Notes/30Jan26/friday2041.html` is a professor source and should be read with the Jan 30 lecture.

Professor note page ledger:

| Folder | Files |
|---|---|
| `root` | `21Jan26.jpg` |
| `26Jan26` | `26Jan26a.jpg`, `26Jan26b.jpg`, `26Jan26c.jpg`, `26Jan26d.jpg` |
| `28Jan26` | `28Jan26a.jpg`, `28Jan26b.jpg`, `28Jan26c.jpg` |
| `30Jan26` | `30Jan26a.jpg`, `30Jan26b.jpg`, `30Jan26c.jpg`, `30Jan26d.jpg`, `30Jan26e.jpg`, `friday2041.html` |
| `02Feb26` | `02Feb26a.jpg`, `02Feb26b.jpg`, `02Feb26c.jpg` |
| `04Feb26` | `04Feb26a.jpg`, `04Feb26b.jpg`, `04Feb26c.jpg`, `04Feb26d.jpg` |
| `06Feb26` | `06Feb26a.jpg`, `06Feb26b.jpg`, `06Feb26c.jpg`, `06Feb26d.jpg` |
| `09Feb26` | `09Feb26a.jpg`, `09Feb26b.jpg`, `09Feb26c.jpg`, `09Feb26d.jpg` |
| `11Feb26` | `11Feb26a.jpg`, `11Feb26b.jpg`, `11Feb26c.jpg`, `11Feb26d.jpg` |
| `13Feb26` | `13Feb26a.jpg`, `13Feb26b.jpg`, `13Feb26c.jpg`, `13Feb26d.jpg` |
| `16Feb26` | `16Feb26a.jpg`, `16Feb26b.jpg`, `16Feb26c.jpg`, `16Feb26d.jpg`, `16Feb26e.jpg` |
| `18Feb26` | `18Feb26a.jpg`, `18Feb26b.jpg`, `18Feb26c.jpg`, `18Feb26d.jpg` |
| `20Feb26` | `20Feb26a.jpg`, `20Feb26b.jpg`, `20Feb26c.jpg` |
| `23Feb26` | `23Feb26a.jpg`, `23Feb26b.jpg`, `23Feb26c.jpg`, `23Feb26d.jpg`, `23Feb26e.jpg` |
| `25Feb26` | `25Feb26a.jpg`, `25Feb26b.jpg`, `25Feb26c.jpg`, `25Feb26d.jpg`, `25Feb26e.jpg` |
| `02Mar26` | `02Mar26a.jpg`, `02Mar26b.jpg`, `02Mar26c.jpg`, `02Mar26d.jpg` |
| `04Mar26` | `04Mar26a.jpg`, `04Mar26b.jpg`, `04Mar26c.jpg`, `04Mar26d.jpg` |
| `06Mar26` | `06Mar26a.jpg`, `06Mar26b.jpg`, `06Mar26c.jpg`, `06Mar26d.jpg` |
| `16Mar26` | `16Mar26a.jpg`, `16Mar26b.jpg`, `16Mar26c.jpg` |
| `18Mar26` | `18Mar26a.jpg`, `18Mar26b.jpg`, `18Mar26c.jpg`, `18Mar26d.jpg` |
| `20Mar26` | `20Mar26a.jpg`, `20Mar26b.jpg`, `20Mar26c.jpg`, `20Mar26d.jpg` |
| `23Mar26` | `23Mar26a.jpg`, `23Mar26b.jpg`, `23Mar26c.jpg`, `23Mar26d.jpg`, `23Mar26e.jpg` |
| `25Mar26` | `25Mar26a.jpg`, `25Mar26b.jpg`, `25Mar26c.jpg`, `25Mar26d.jpg`, `25Mar26e.jpg` |
| `27Mar26` | `27Mar26a.jpg`, `27Mar26b.jpg`, `27Mar26c.jpg`, `27Mar26d.jpg` |
| `30Mar26` | `30Mar26a.jpg`, `30Mar26b.jpg`, `30Mar26c.jpg`, `30Mar26d.jpg` |
| `01Apr26` | `01Apr26a.jpg`, `01Apr26b.jpg`, `01Apr26c.jpg` |
| `03Apr26` | `03Apr26a.jpg`, `03Apr26b.jpg`, `03Apr26c.jpg`, `03Apr26d.jpg`, `03Apr26e.jpg` |
| `06Apr26` | `06Apr26a.jpg`, `06Apr26b.jpg`, `06Apr26c.jpg` |
| `08Apr26` | `08Apr26a.jpg`, `08Apr26b.jpg`, `08Apr26c.jpg`, `08Apr26d.jpg` |
| `10Apr26` | `10Apr26a.jpg`, `10Apr26b.jpg`, `10Apr26c.jpg`, `10Apr26d.jpg`, `10Apr26e.jpg` |
| `13Apr26` | `13Apr26a.jpg`, `13Apr26b.jpg`, `13Apr26c.jpg`, `13Apr26d.jpg`, `13Apr26e.jpg` |
| `15Apr26` | `15Apr26a.jpg`, `15Apr26b.jpg`, `15Apr26c.jpg` |
| `17Apr26` | `17Apr26a.jpg`, `17Apr26b.jpg`, `17Apr26c.jpg`, `17Apr26d.jpg` |
| `20Apr26` | `20Apr26a.jpg`, `20Apr26b.jpg`, `20Apr26c.jpg`, `20Apr26d.jpg`, `20Apr26e.jpg` |
| `22Apr26` | `22Apr26a.jpg`, `22Apr26b.jpg`, `22Apr26c.jpg`, `22Apr26d.jpg` |
| `24Apr26` | `24Apr26a.jpg`, `24Apr26b.jpg`, `24Apr26c.jpg` |
| `27Apr26` | `27Apr26a.jpg`, `27Apr26b.jpg`, `27Apr26c.jpg`, `27Apr26d.jpg` |
| `29Apr26` | `29Apr26a.jpg`, `29Apr26b.jpg`, `29Apr26c.jpg` |
| `01May26` | `01May26a.jpg`, `01May26b.jpg`, `01May26c.jpg` |

Labs:
- `Labs/hello.ml`
- `Labs/lab1.ml` through `Labs/lab12.ml`
- `Labs/tests1.ml` through `Labs/tests11.ml`
- There is no `Labs/tests12.ml` in the current source folder.
- `Labs/solve.txt`

Projects:
- `Labs/project-1/expression.ml`
- `Labs/project-1/modStack.ml`
- `Labs/project-1/project.ml`
- `Labs/project-2/factorial.lsp`
- `Labs/project-2/project2.ml`
- `Labs/project-2/run_test.ml`
- `Labs/project-2/scanner.ml`
- `Labs/project-2/test_integration.ml`
- `Labs/project-2/test_property1.ml`
- `Labs/project-2/test_property2.ml`
- `Labs/project-2/test_property3.ml`
- `Labs/project-2/testParser.ml`
- `Labs/project-2/thing.png`

Practice:
- `Labs/Practice/factorial.lsp`
- `Labs/Practice/iffyTaut.ml`
- `Labs/Practice/modStack.ml`
- `Labs/Practice/modularMacros.pdf`
- `Labs/Practice/permute.ml`
- `Labs/Practice/scanner.ml`
- `Labs/Practice/tautology.ml`
- `Labs/Practice/testParser.ml`

Generated/spec support inside source folder:
- `Labs/.kiro/specs/lisp-parser-module/.config.kiro`
- `Labs/.kiro/specs/lisp-parser-module/requirements.md`
- `Labs/.kiro/specs/lisp-parser-module/design.md`
- `Labs/.kiro/specs/lisp-parser-module/tasks.md`
- `Labs/.vscode/settings.json`

Use generated/spec support as source material because it is in the corpus, but if it conflicts with professor assignment files, tests, or transcripts, record the conflict and prefer the professor/course file.

## Textbook Coverage

Use `Hickey Textbook.pdf` directly. Existing Jarvis textbook notes are useful, but the PDF is the source.

PDF outline anchors already verified:
- Ch. 1 `Introduction`: functional vs imperative languages.
- Ch. 2 `Simple Expressions`: primitive types, top-level expressions, type system, compiling.
- Ch. 3 `Variables and Functions`: functions, scoping, recursion, higher-order functions, labeled parameters.
- Ch. 4 `Basic pattern matching`: match, patterns, incomplete matches, patterns everywhere.
- Ch. 5 `Tuples, lists, and polymorphism`: polymorphism, tuples, lists, tail recursion.
- Ch. 6 `Unions`: ADTs, binary trees, ordered trees, built-in unions.
- Ch. 7 `Reference cells and side-effects`: refs, pure functional programming, queues, doubly-linked lists, memoization, graphs.
- Ch. 8 `Records, Arrays, and String`: records, arrays, strings, hash tables.
- Ch. 9 `Exceptions`: defining/raising/handling exceptions, standard exceptions.
- Ch. 10 `Input and Output`: channels, buffers, `Printf`, `Scanf`.
- Ch. 11 `Files, Compilation Units, and Programs`: single files, compilers, interfaces, debugging.
- Ch. 12 `The OCaml Module System`: structures, signatures, modules, recursive modules, include, abstraction.
- Ch. 13 `Functors`: module reuse and higher-order functors.
- Ch. 14 `Objects`: encapsulation, functional update, object factories, imperative objects, self, subtyping.
- Ch. 19 `Syntax`: lexemes, names, expressions, patterns, type definitions, module expressions.

Textbook notes to create later:
- [[Textbook/Chapter - 7 & 8]]
- [[Textbook/Chapter - 13 & 14]]
- [[Textbook/Chapter - 19]]

## Transcript And Professor Notes Crosswalk

The mapping below is the working production map. It is based on transcript opening topics, professor-note folders, and syllabus dates. The only hard exception is the duplicate transcript file.

| Week | Dates | Transcript files | Professor notes | Lecture headings to preserve |
|---|---|---|---|---|
| [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 6]] | Feb 23, Feb 25, Feb 27 midterm | `Lecture - 13.txt`, `Lecture - 14.txt` | `23Feb26/`, `25Feb26/` | Streams; functions as parts of objects; object simulation with closures; midterm boundary |
| [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 7]] | Mar 2, Mar 4, Mar 6 | `Lecture - 15.txt`, `Lecture - 16.txt`, `Lecture - 17.txt` | `02Mar26/`, `04Mar26/`, `06Mar26/` | Project 1 announcement; memoization; mutable state/references; lazy-list setup |
| spring break | Mar 9-13 | none | none | No class |
| [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 8]] | Mar 16, Mar 18, Mar 20 | `Lecture - 18.txt`, `Lecture - 19.txt`, `Lecture - 20.txt` | `16Mar26/`, `18Mar26/`, `20Mar26/` | Lazy lists; eager vs lazy evaluation; modules; signatures |
| [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 9]] | Mar 23, Mar 25, Mar 27 | `Lecture - 21.txt`, `Lecture - 22.txt`, `Lecture - 23.txt` | `23Mar26/`, `25Mar26/`, `27Mar26/` | Finish modules; Lisp examples; Lisp interpreter design |
| [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 10]] | Mar 30, Apr 1, Apr 3 | `Lecture - 24.txt`, `Lecture - 25.txt`, `Lecture - 26.txt` | `30Mar26/`, `01Apr26/`, `03Apr26/` | Scanner; helper functions for scanner; parser syntax diagram; evaluator start |
| [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 11]] | Apr 6, Apr 8, Apr 10 | `Lecture - 27.txt`, `Lecture - 28.txt`, `Lecture - 29.txt`; `Lecture - 30.txt` duplicate | `06Apr26/`, `08Apr26/`, `10Apr26/` | Project 2 parser; Lisp printer lab; evaluator primitives; `and`, `or`, `car`, `cdr`, `cons`; higher-order primitive builders |
| [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 12]] | Apr 13, Apr 15, Apr 17 | `Lecture - 31.txt`, `Lecture - 32.txt`, `Lecture - 33.txt` | `13Apr26/`, `15Apr26/`, `17Apr26/` | Finish primitives; `define`; `lambda`; user functions; `apply`; evaluator walkthrough; compiler |
| [[Week - 13]] | Apr 20, Apr 22, Apr 24 | `Lecture - 34.txt`, `Lecture - 35.txt`, `Lecture - 36.txt` | `20Apr26/`, `22Apr26/`, `24Apr26/` | Metaprogramming; macros; final lab integration; special-topic tautology checker |
| [[Week - 14]] | Apr 27, Apr 29, May 1 | `Lecture - 37.txt`, `Lecture - 38.txt`, `Lecture - 39.txt` | `27Apr26/`, `29Apr26/`, `01May26/` | If-based tautology checker; rules 6-11; `makeIf`; `normalize`; `substitute`; `isTautology`; CPS example |
| [[Week - 15 Final Review]] | May 4 | `Lecture - 40.txt` | no `04May26/` notes folder found | Review questions; mutual recursion vs internal helper; final exam synthesis |

## Week Production Details

### [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 6]]

Primary sources:
- `Lecture - 13.txt`
- `Lecture - 14.txt`
- `Lectures/Notes/23Feb26/*`
- `Lectures/Notes/25Feb26/*`
- `Labs/lab5.ml`
- `Labs/tests5.ml`
- `Hickey Textbook.pdf` Ch. 3 and Ch. 14

Content to capture:
- Streams are data objects containing a current value, state, and a next function.
- A stream imitates an infinite series without materializing it all at once.
- Functions are first-class values that can live inside data structures.
- The lab code's stream helpers: `makeStream`, `first`, `rest`, `take`.
- Lab-specific operations: `odds`, `trim`, `scale`, `sum`.
- Object simulation through closures from lecture 14.

Concept notes to create/update:
- [[OCaml - Streams]]
- [[OCaml - Functions as Data]]
- [[OCaml - Objects with Functions as Parts]]
- [[OCaml - Let bindings, Scope & Closures]]

Lab/project notes:
- [[Lab - 5 Streams]]

Required backlinks:
- [[OCaml - Streams]] links to [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 6#Lecture]], [[Lab - 5 Streams]], `lab5.ml`, `tests5.ml`, and Hickey Ch. 14.
- [[Lab - 5 Streams]] links back to [[OCaml - Streams]] and [[OCaml - Functions as Data]].

### [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 7]]

Primary sources:
- `Lecture - 15.txt`
- `Lecture - 16.txt`
- `Lecture - 17.txt`
- `Lectures/Notes/02Mar26/*`
- `Lectures/Notes/04Mar26/*`
- `Lectures/Notes/06Mar26/*`
- `Labs/lab6.ml`
- `Labs/tests6.ml`
- `Labs/lab7.ml`
- `Labs/tests7.ml`
- `Labs/project-1/expression.ml`
- `Labs/project-1/modStack.ml`
- `Labs/project-1/project.ml`
- `Labs/solve.txt`
- `Hickey Textbook.pdf` Ch. 7 and Ch. 8

Content to capture:
- Project 1 solves equations by recursively moving the unknown variable toward isolation.
- `expression` ADT constructors: `Var`, `Neg`, `Add`, `Div`, `Equ`, `Mul`, `Sub`.
- `isInside` controls which side of an expression is recursively solved.
- `solver` implements inverse-operation rules for each constructor.
- `solve.txt` gives a Lisp version of the same algebraic solving idea and should be cross-linked with Project 1.
- Memoization changes repeated recursive computation into lookup after the first computation.
- `lab6.ml` compares plain `c` with `memyC` using `Hashtbl`.
- `lab7.ml` introduces lazy-list representation with delayed tails.

Concept notes to create/update:
- [[OCaml - Memoization]]
- [[OCaml - Reference Cells and Side Effects]]
- [[OCaml - Hash Tables]]
- [[OCaml - Equation Solver Project]]
- [[OCaml - Algebraic Data Types]]
- [[OCaml - Lazy Lists]]

Lab/project notes:
- [[Lab - 6 Memoization]]
- [[Lab - 7 Lazy Lists]]
- [[Project - 1 Equation Solver]]

Required backlinks:
- [[Project - 1 Equation Solver]] links to [[OCaml - Algebraic Data Types]], [[OCaml - Pattern Matching]], and [[OCaml - Equation Solver Project]].
- [[OCaml - Memoization]] links to [[Lab - 6 Memoization]] and Hickey Ch. 7 `Memoization`.
- [[OCaml - Lazy Lists]] links to [[Lab - 7 Lazy Lists]] and [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 8]] if Week 8 contains the fuller lazy-evaluation explanation.

### [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 8]]

Primary sources:
- `Lecture - 18.txt`
- `Lecture - 19.txt`
- `Lecture - 20.txt`
- `Lectures/Notes/16Mar26/*`
- `Lectures/Notes/18Mar26/*`
- `Lectures/Notes/20Mar26/*`
- `Labs/lab7.ml`
- `Labs/tests7.ml`
- `Labs/lab8.ml`
- `Labs/tests8.ml`
- `Hickey Textbook.pdf` Ch. 11 and Ch. 12

Content to capture:
- Eager vs lazy evaluation: when computation happens, what is stored, and when forcing occurs.
- Lazy lists as a source-backed concrete data structure, not a generic laziness summary.
- Modules and signatures as API boundaries.
- `module type Associaty` hides representation and exposes `make`, `put`, `get`, `delete`.
- `Association.NoSuchKey` and how exceptions appear through the module API.

Concept notes to create/update:
- [[OCaml - Lazy Evaluation]]
- [[OCaml - Lazy Lists]]
- [[OCaml - Modules and Signatures]]
- [[OCaml - Association Lists]]
- [[OCaml - Exceptions]]

Lab/project notes:
- [[Lab - 8 Association Module]]

Required backlinks:
- [[OCaml - Modules and Signatures]] links to [[Lab - 8 Association Module]], Hickey Ch. 11, and Hickey Ch. 12.
- [[OCaml - Association Lists]] links to earlier association-list lecture material and later Lisp environments.

### [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 9]]

Primary sources:
- `Lecture - 21.txt`
- `Lecture - 22.txt`
- `Lecture - 23.txt`
- `Lectures/Notes/23Mar26/*`
- `Lectures/Notes/25Mar26/*`
- `Lectures/Notes/27Mar26/*`
- `Labs/lab9.ml`
- `Labs/tests9.ml`
- `Hickey Textbook.pdf` Ch. 5, Ch. 6, Ch. 11, Ch. 12

Content to capture:
- Lisp is represented with OCaml data constructors, not strings.
- `thing` type from lab9: `Nil`, `Number`, `Symbol`, `Cons`.
- `every` tests predicates over lists of `thing`.
- `substitute` recursively replaces old things with new things inside nested structures.
- `questyEqual` defines course-specific structural equality.
- This week begins the interpreter arc. It should prepare links into scanner/parser/evaluator notes.

Concept notes to create/update:
- [[OCaml - Lisp Thing Representation]]
- [[OCaml - Recursive Data]]
- [[OCaml - Structural Recursion]]
- [[OCaml - Lisp Lists]]

Lab/project notes:
- [[Lab - 9 Lisp Data Recursion]]

Required backlinks:
- [[OCaml - Lisp Thing Representation]] becomes a core concept for [[Project - 2 Lisp Parser]], [[Lab - 10 Lisp Printer]], [[Lab - 11 Lisp Evaluator]], and [[Lab - 12 Lisp Integration]].

### [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 10]]

Primary sources:
- `Lecture - 24.txt`
- `Lecture - 25.txt`
- `Lecture - 26.txt`
- `Lectures/Notes/30Mar26/*`
- `Lectures/Notes/01Apr26/*`
- `Lectures/Notes/03Apr26/*`
- `Labs/Practice/scanner.ml`
- `Labs/Practice/testParser.ml`
- `Labs/project-2/scanner.ml`
- `Labs/project-2/project2.ml`
- `Labs/.kiro/specs/lisp-parser-module/requirements.md`
- `Labs/.kiro/specs/lisp-parser-module/design.md`
- `Labs/.kiro/specs/lisp-parser-module/tasks.md`
- `Hickey Textbook.pdf` Ch. 10, Ch. 11, Ch. 12, Ch. 19

Content to capture:
- Scanner reads characters and produces tokens.
- Token constructors: `CloseParenToken`, `EndToken`, `NumberToken`, `OpenParenToken`, `SymbolToken`.
- Scanner state is held in refs: input channel and current char.
- Parser reads tokens and produces `thing` values.
- Parser interface from Kiro spec: `Can'tParse`, `initialize`, `nextThing`.
- Recursive descent shape: `nextThing` and `nextThings`.
- `nil` is parsed as `Nil`, not `Symbol "nil"`.
- Parenthesized lists become right-nested `Cons` chains ending in `Nil`.

Concept notes to create/update:
- [[OCaml - Scanners]]
- [[OCaml - Tokens]]
- [[OCaml - Recursive Descent Parsing]]
- [[OCaml - Lisp Parser]]
- [[OCaml - Input and Output]]

Lab/project notes:
- [[Project - 2 Lisp Parser]]

Required backlinks:
- [[Project - 2 Lisp Parser]] links to [[OCaml - Scanners]], [[OCaml - Recursive Descent Parsing]], [[OCaml - Lisp Thing Representation]], and [[OCaml - Modules and Signatures]].
- [[OCaml - Recursive Descent Parsing]] links to Kiro requirements/design/tasks, professor parser syntax diagram, `project2.ml`, and `testParser.ml`.

### [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 11]]

Primary sources:
- `Lecture - 27.txt`
- `Lecture - 28.txt`
- `Lecture - 29.txt`
- `Lecture - 30.txt` as duplicate check only
- `Lectures/Notes/06Apr26/*`
- `Lectures/Notes/08Apr26/*`
- `Lectures/Notes/10Apr26/*`
- `Labs/lab10.ml`
- `Labs/tests10.ml`
- `Labs/project-2/*`
- `Hickey Textbook.pdf` Ch. 3, Ch. 4, Ch. 9, Ch. 10, Ch. 11, Ch. 12

Content to capture:
- Project 2 is announced as parser work based on the scanner.
- Lab 10 prints Lisp `thing` values.
- Printer uses mutual recursion: `printThing`, `printingThing`, `printingThings`.
- Evaluator primitives must check argument count, evaluate arguments when appropriate, and raise errors for wrong shapes.
- `and` and `or` are short-circuit primitives.
- `car`, `cdr`, `cons` operate on `Cons` and `Nil` representations.
- Higher-order helper builders reduce repeated primitive code, especially arithmetic and relation makers.

Concept notes to create/update:
- [[OCaml - Lisp Printer]]
- [[OCaml - Interpreter Primitives]]
- [[OCaml - Short-Circuit Evaluation]]
- [[OCaml - Higher-Order Helpers]]
- [[OCaml - Mutual Recursion]]

Lab/project notes:
- [[Lab - 10 Lisp Printer]]
- Update [[Project - 2 Lisp Parser]]

Required backlinks:
- [[OCaml - Interpreter Primitives]] links to [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 11#Lecture]], [[Lab - 11 Lisp Evaluator]], and later [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 12]].
- [[OCaml - Mutual Recursion]] links to Lab 10 printer and final review's mutual-recursion question.

### [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 12]]

Primary sources:
- `Lecture - 31.txt`
- `Lecture - 32.txt`
- `Lecture - 33.txt`
- `Lectures/Notes/13Apr26/*`
- `Lectures/Notes/15Apr26/*`
- `Lectures/Notes/17Apr26/*`
- `Labs/lab11.ml`
- `Labs/tests11.ml`
- `Labs/project-2/*`
- `Hickey Textbook.pdf` Ch. 3, Ch. 9, Ch. 11, Ch. 12

Content to capture:
- `define` mutates the global environment.
- `lambda` builds a closure with parameter list, body, and defining environment.
- `apply` evaluates arguments in the calling environment and evaluates the body in the closure environment extended with parameter bindings.
- Local environment and global environment lookup order.
- `areParameters` and `isMember` validate lambda parameter lists.
- `let` tests in `tests11.ml` show nested bindings and environment behavior.
- Evaluator walkthrough should be detailed enough to trace a small Lisp expression by hand.

Concept notes to create/update:
- [[OCaml - Environments]]
- [[OCaml - Closures in Interpreters]]
- [[OCaml - Apply in an Interpreter]]
- [[OCaml - Lisp Evaluator]]
- [[OCaml - Global vs Local Environment]]

Lab/project notes:
- [[Lab - 11 Lisp Evaluator]]
- Update [[Project - 2 Lisp Parser]] if parser behavior is referenced.

Required backlinks:
- [[OCaml - Environments]] links to [[OCaml - Association Lists]], [[OCaml - Let bindings, Scope & Closures]], [[Lab - 11 Lisp Evaluator]], and `tests11.ml`.
- [[OCaml - Closures in Interpreters]] links to [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 12#Lecture]] and Hickey Ch. 3 scoping.

### [[Week - 13]]

Primary sources:
- `Lecture - 34.txt`
- `Lecture - 35.txt`
- `Lecture - 36.txt`
- `Lectures/Notes/20Apr26/*`
- `Lectures/Notes/22Apr26/*`
- `Lectures/Notes/24Apr26/*`
- `Labs/lab12.ml`
- `Labs/Practice/modularMacros.pdf`
- `Labs/Practice/iffyTaut.ml`
- `Hickey Textbook.pdf` Ch. 11, Ch. 12, Ch. 19

Content to capture:
- Metaprogramming means programs manipulating or generating program structure.
- Macros are introduced by extending Lisp.
- Lab 12 integrates previous pieces: evaluator, scanner, parser, printer, and REPL.
- `lab12.ml` has explicit placeholders for `Parsish`, `Parser`, `Printish`, `Printer`, `Lispish`, and `Lisp`.
- Special topic tautology work begins again, now through if-normalized propositions.

Concept notes to create/update:
- [[OCaml - Macros and Metaprogramming]]
- [[OCaml - Lisp Integration]]
- [[OCaml - REPL Structure]]
- [[OCaml - If Normalization]]

Lab/project notes:
- [[Lab - 12 Lisp Integration]]

Required backlinks:
- [[Lab - 12 Lisp Integration]] links to all interpreter-arc concepts: scanner, parser, printer, evaluator, environments, modules.
- [[OCaml - Macros and Metaprogramming]] links to `modularMacros.pdf`, Week 13 lectures, and Hickey syntax/module sections.

### [[Week - 14]]

Primary sources:
- `Lecture - 37.txt`
- `Lecture - 38.txt`
- `Lecture - 39.txt`
- `Lectures/Notes/27Apr26/*`
- `Lectures/Notes/29Apr26/*`
- `Lectures/Notes/01May26/*`
- `Labs/Practice/iffyTaut.ml`
- `Labs/Practice/tautology.ml`
- `Labs/Practice/permute.ml`
- `Hickey Textbook.pdf` Ch. 3, Ch. 4, Ch. 5, Ch. 6

Content to capture:
- If-based proposition representation: `T`, `F`, `V`, `If`.
- `makeIf` applies simplification rules while building if expressions.
- `normalize` rewrites nested conditions into a normal form.
- `substitute` replaces variables with truth values.
- `isTautology` reduces tautology checking to simplification/equivalence.
- `isEquivalent` is called out as the mystery to solve.
- Final CPS example should link back to continuations without rewriting Week 5.

Concept notes to create/update:
- [[OCaml - If Normalization]]
- [[OCaml - Tautology Problems]]
- [[OCaml - Structural Equality]]
- [[OCaml - Continuation Passing]]

Lab/project notes:
- no new numbered lab; practice files are concept sources.

Required backlinks:
- [[OCaml - Tautology Problems]] links to [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 5]], [[Week - 14]], `tautology.ml`, `iffyTaut.ml`, and [[OCaml - Continuation Passing]].
- [[OCaml - If Normalization]] links to `makeIf`, `normalize`, `substitute`, and `isTautology` headings in the concept note.

### [[Week - 15 Final Review]]

Primary sources:
- `Lecture - 40.txt`
- All prior week, lab, project, and concept notes after they exist.
- `Hickey Textbook.pdf` sections already mapped above.

Content to capture:
- Final review questions, including mutual recursion vs internal helper.
- Cumulative Lisp evaluator/project expectations.
- What to be able to write from memory:
  - recursive ADT traversal
  - module signature + module implementation
  - scanner token dispatcher
  - parser recursive descent
  - evaluator environment lookup
  - closure application
  - memoized recursion
  - lazy-list forcing

Concept notes to create/update:
- [[OCaml - Mutual Recursion]]
- [[OCaml - Internal Helper Functions]]
- [[Final Review Map]]

## Lab And Project Link Rules

Each lab note should have:
- problem in plain language
- source files read
- function/type signatures
- exact test behavior from `testsN.ml`
- concepts tested
- common wrong solutions
- representative snippet
- what Anant should reproduce without looking

Each concept touched by a lab must include:
- a `## Labs / Projects` section
- a bullet for the lab
- the exact functions or tests that exercise the concept
- link to the lab note and weekly heading

Each project note should have:
- project goal
- file map
- data model
- key functions/control flow
- parser/scanner/test architecture when present
- concepts exercised
- failure modes from tests
- input/output examples
- links to the project concept and core concepts

Project concept rules:
- [[OCaml - Equation Solver Project]] is the project concept for Project 1.
- [[OCaml - Lisp Parser]] is the project concept for Project 2.
- Project 1 must also link to [[OCaml - Algebraic Data Types]], [[OCaml - Pattern Matching]], and [[OCaml - Recursive Data]].
- Project 2 must also link to [[OCaml - Scanners]], [[OCaml - Recursive Descent Parsing]], [[OCaml - Lisp Thing Representation]], and [[OCaml - Modules and Signatures]].

## Interlinking Rules

Strong links are required. Prefer links to headings, not just files.

Examples:
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 6#Lecture]]
- [[Lab - 5 Streams#Test Behavior]]
- [[OCaml - Streams#Labs / Projects]]
- [[Project - 2 Lisp Parser#Recursive Descent]]
- [[OCaml - Lisp Evaluator#Apply]]
- [[Chapter - 11 & 12#Chapter 12 - The OCaml Module System]]

When a heading does not exist yet, create the note with stable headings that future notes can link to.

Each weekly note must link to:
- concept notes created/updated
- lab/project notes
- relevant textbook chapter notes or PDF-derived textbook notes
- practice files when they are source material

Each concept note must link to:
- weeks where the concept appears
- labs/projects that test it
- textbook support
- related concepts

## Proposed Note Creation Order

1. Build [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 6]], [[OCaml - Streams]], [[OCaml - Functions as Data]], and [[Lab - 5 Streams]].
2. Build [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 7]], [[OCaml - Memoization]], [[OCaml - Reference Cells and Side Effects]], [[Project - 1 Equation Solver]], [[OCaml - Equation Solver Project]], [[Lab - 6 Memoization]], and [[Lab - 7 Lazy Lists]].
3. Build [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 8]], [[OCaml - Lazy Evaluation]], [[OCaml - Modules and Signatures]], [[OCaml - Association Lists]], and [[Lab - 8 Association Module]].
4. Build the interpreter arc in order: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 9]], [[OCaml - Lisp Thing Representation]], [[Lab - 9 Lisp Data Recursion]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 10]], [[OCaml - Scanners]], [[OCaml - Recursive Descent Parsing]], [[Project - 2 Lisp Parser]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 11]], [[Lab - 10 Lisp Printer]], [[OCaml - Interpreter Primitives]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 12]], [[Lab - 11 Lisp Evaluator]], [[OCaml - Environments]], [[OCaml - Closures in Interpreters]].
5. Build [[Week - 13]], [[Lab - 12 Lisp Integration]], [[OCaml - Lisp Integration]], and [[OCaml - Macros and Metaprogramming]].
6. Build [[Week - 14]], [[OCaml - If Normalization]], and deepen [[OCaml - Tautology Problems]] without rewriting [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 5]].
7. Build [[Week - 15 Final Review]], [[OCaml - Mutual Recursion]], [[OCaml - Internal Helper Functions]], and [[Final Review Map]].

## Final Quality Check For Every Note

Before saving a final note, answer:
- Which exact source files did this note use?
- Which lecture date/folder did each lecture claim come from?
- Which Hickey textbook section supports the textbook claim?
- Which lab/test/project file exercises the concept?
- What should Anant be able to write from memory?
- What common mistake does the source/test expose?
- Are all major links bidirectional through weekly, lab/project, and concept notes?
- Did the note avoid generic filler?
- Did the note mark uncertainty instead of hiding it?
