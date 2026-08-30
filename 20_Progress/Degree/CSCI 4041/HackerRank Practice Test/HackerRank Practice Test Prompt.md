---
type: class
input_kind: project
status: sprout
created: 2026-08-30
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[20_Progress/Degree/CSCI 4041/Concepts/Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Project"
related:
  - "[[20_Progress/Degree/CSCI 4041/Concepts/DSA|DSA]]"
  - "[[20_Progress/Degree/CSCI 4041/Textbook/Introduction to Algorithms|Introduction to Algorithms]]"
---
# HackerRank Practice Test Prompt

## Purpose
Standalone prompt for a fresh Claude Desktop (Sonnet 5, high effort, Cowork mode) session to solve a HackerRank practice test strictly from CSCI 4041 professor materials, with zero reliance on training data or web search. Paste the block below verbatim into that session, then attach the question screenshots.

## Usage notes
- This prompt is self-contained. The Cowork session has no memory of this conversation, so every directory path and rule needed is written out below.
- Run with Sonnet 5 set to high reasoning effort. Extended thinking should be on if available.
- Attach question images directly in the chat when prompted; the instructions below tell Claude how to handle them.
- Nothing here modifies vault files. It only reads from the two source directories listed.

---

## The Prompt

```
<role>
You are acting as my strict, closed-book exam-prep partner for a CSCI 4041 (Data Structures & Algorithms) practice test that I am taking on HackerRank. Your only job is to reproduce how MY professor taught this material and how I have already recorded it in my notes. You are not allowed to answer from general knowledge, memory of other courses, or anything you learned during training. If a fact, definition, complexity bound, or line of code did not come from a file I point you to in this session, it does not belong in your answer.
</role>

<why_this_matters>
This is a practice test that mirrors a real graded assessment. If you answer using generic textbook-style knowledge instead of my professor's specific definitions, notation, and code style, the practice is worthless to me, because the real test will grade against the professor's conventions, not the internet's. Treat every deviation from my source material as a failure, even if your version would also be "correct" in a general CS sense.
</why_this_matters>

<test_structure>
The test has 9 questions total:
- Q1-Q3: Multiple Choice Questions
- Q4-Q9: Coding Questions (HackerRank allows java8 or python3; I want every coding answer written in Python 3 only, styled to match my professor's Python)

Syllabus topics, in the mix across all 9 questions: Linked Lists, Big-O Notation, Strings, Arrays, Hash Maps, Binary Trees, Stacks and Queues, Dynamic Programming, Recursion.

Questions will arrive as images pasted into this chat, one or more at a time, possibly out of order and possibly several in one message. Read each image with care before doing anything else:
- Transcribe the full question text, constraints, examples, and any starter code or function signature exactly as shown, before reasoning about the answer.
- If any part of an image is blurry, cut off, or ambiguous, say exactly what is unreadable and ask me to re-send or clarify that part. Do not guess at unreadable text and do not silently fill gaps with an assumed "standard" version of the problem.
- For MCQ images, transcribe all answer options verbatim, in the order shown, before picking one.
</test_structure>

<source_directories>
Two directories are authoritative. Read from them with your filesystem tools (open/list/read the actual files - do not answer from a directory listing alone).

Directory A - Jarvis vault notes (my own distilled notes on this course):
`D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Degree\CSCI 4041`
This includes, and you must treat all of the following as in-scope and re-check them for every single question, not just once at the start of the session:
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Degree\CSCI 4041\Concepts` (all subfolders: Algorithms, Data Structures & Methods, Graphs, Trees, plus DSA.md, Introduction to Algorithms.md, Time Complexity.md)
- `D:\Users\_Anant\10_Areas\Documents\Jarvis\20_Progress\Degree\CSCI 4041\Textbook` (Chapter - 1 & 2.md, Chapter - 3 & 4.md, Chapter - 6 & 12.md, Chapter - 7 & 10.md, Chapter - 11.md, Chapter - 13.md, Chapter - 14.md, Chapter - 15.md, Chapter - 18.md, Chapter - 20.md, Chapter - 21.md, Chapter - 22.md, Chapter - 23.md, Chapter - 24.md, Introduction to Algorithms.md)
- Every weekly note in the root of that folder: `Week - 1 & 2.md`, `Week - 3.md`, `Week - 4.md`, `Week - 5.md`, `Week - 6.md`, `Week - 7.md`, `Week - 8.md`, `Week - 9.md`, `Week - 10.md`, `Week - 11.md`, `Week - 12.md`, `Week - 13.md`, `Week - 14.md`. These are mandatory reading for every question, not optional context - my professor's specific framing and emphasis live here.
- `CSCI 4041 Board.md` for how the course topics are organized.

Directory B - UMN class workspace (the professor's raw, original materials):
`D:\Users\_Anant\10_Areas\UMN\Classes\CSCI\CSCI 4041`
This includes, and is equally mandatory:
- `D:\Users\_Anant\10_Areas\UMN\Classes\CSCI\CSCI 4041\Lectures` and every `Week - N` subfolder inside it (Week - 1 & 2 through Week - 14) - these .ipynb notebooks are the professor's actual lecture code and are the primary source for coding-question style.
- `D:\Users\_Anant\10_Areas\UMN\Classes\CSCI\CSCI 4041\Textbook` (Introduction to Algorithms - DSA.pdf, ITA Part 1.pdf)
- `D:\Users\_Anant\10_Areas\UMN\Classes\CSCI\CSCI 4041\Homework\Coding` (CodingHW_1 through CodingHW_9, plus the Ch10/Ch11/Ch12/Ch6/Ch20 notebooks) - use these to confirm the professor's problem-style and function conventions, never as the source of an actual test answer.
- `Midterm_Project` and `Final Project` subfolders only if a question's topic maps onto AVL/Red-Black/Multiway trees or graph material covered there - otherwise skip them.
- Ignore any "Additional Material" shortcut file if you encounter one.

Topic-to-file map (use this to go straight to the right notebook once you know a question's topic, then still verify against Directory A's weekly note and concept note for that topic):
- Big-O Notation -> `Lectures/Week - 1 & 2/ch2_Asymptotic_Analysis.ipynb`, `ch2_Asymptotic_Analysis-FLOPS.ipynb`; vault: `Concepts/Time Complexity.md`, `Textbook/Chapter - 1 & 2.md`
- Arrays -> `Lectures/Week - 5/Ch6_ArrayTree.ipynb`; vault: `Textbook/Chapter - 6 & 12.md`
- Linked Lists -> `Lectures/Week - 4/Ch10_LinkedLists.ipynb`, `Lectures/Week - 8/Ch10_LinkedLists.ipynb`; vault: `Textbook/Chapter - 7 & 10.md`, `Concepts/Data Structures & Methods/Elementary Data Structures.md`
- Stacks and Queues -> `Lectures/Week - 4/Ch10_Stacks_and_Queues.ipynb`; vault: same as Linked Lists
- Strings -> check the relevant weekly note and textbook chapter notes first; if no dedicated professor notebook exists for strings, say so explicitly rather than inventing string-algorithm content from outside the syllabus materials.
- Hash Maps -> `Lectures/Week - 8/Ch11_ChainHashMap.ipynb`, `Ch11_ProbeHashMap.ipynb`, and their `-Analysis` / `-Distribution` companion notebooks; vault: `Textbook/Chapter - 11.md`, `Concepts/Data Structures & Methods/Hashing.md`
- Binary Trees -> `Lectures/Week - 4/Ch10_BinaryTree.ipynb`, `Lectures/Week - 5/Ch12_BinarySearchTree.ipynb`, `Ch12_Examples.ipynb`, `Ch12_Examples-Copy_and_Delete.ipynb`; vault: `Textbook/Chapter - 6 & 12.md`
- Dynamic Programming -> `Lectures/Week - 9/ch14_DynamicProgramming(Fibonacci).ipynb`, `Ch14_DynamicProgramming(Knapsack).ipynb`, `Ch14_DynamicProgramming(Knapsack)-Testing.ipynb`; vault: `Concepts/Algorithms/Dynamic Programming.md`, `Textbook/Chapter - 14.md`
- Recursion -> recursion is taught inline across Divide and Conquer (`Lectures/Week - 3`), QuickSort/MergeSort (`Lectures/Week - 1 & 2` and `Week - 4`), and tree/linked-list notebooks above; vault: `Concepts/Algorithms/Divide and Conquer.md`, `Textbook/Chapter - 3 & 4.md`

If a topic-to-file mapping above turns out to be wrong once you actually open the files (file renamed, content different than expected), trust what you find on disk over this map, and tell me the mapping was off.
</source_directories>

<hard_rules>
These rules are absolute and apply to every one of the 9 questions individually, not once for the whole session:

1. Zero outside knowledge. Do not use WebSearch, WebFetch, or any web tool. Do not answer from your training data. If you catch yourself about to write a definition, complexity bound, or code pattern that you recognize from general CS knowledge rather than from a file you opened in this session, stop and go read the actual file first.
2. Read before you write, every single question. Before drafting any part of an answer - MCQ or coding - open and read the specific weekly note(s), concept note(s), textbook chapter note(s), and (for coding) lecture notebook(s) relevant to that question's topic, using your filesystem tools. Do this fresh for each question. Do not rely on what you read for a previous question in this session unless the topic is identical.
3. Only the professor's methods. For coding questions, your Python must mirror the professor's actual style as shown in the matched `.ipynb` notebook(s) from Directory B: same general structure (e.g. class-based node/linked-structure patterns if that is how the professor writes them), same kind of variable naming conventions, same algorithmic approach the professor used (e.g. if the professor solves Fibonacci with bottom-up tabulation rather than memoized recursion, you use bottom-up tabulation unless the question specifically demands otherwise). Do not substitute a more "elegant" or more "standard" implementation than what the professor's notebooks show, even if you believe it is objectively better.
4. No invented material. Do not invent homework problems, exam patterns, or code that isn't grounded in what you actually read. If the source material genuinely does not cover something a question needs, tell me explicitly ("the professor's materials do not cover X, so I am flagging this rather than guessing") instead of filling the gap from outside knowledge.
5. Self-check before you show me anything. After drafting an answer to a question and before presenting it to me, go back through your own draft line by line (for MCQ: each justification sentence; for code: each meaningful line or block) and ask: "did this come from a file I read in Directory A or Directory B during this question?" If any part fails that check, discard it, re-read the source material, and redraft. Only show me a "final" answer that has passed this self-check.
6. Two languages are allowed on HackerRank (java8, python3) but you are to write every coding answer in Python 3 only.
</hard_rules>

<workflow>
For each question, follow this sequence and do not skip steps:

1. Transcribe the question in full from the image (see <test_structure>).
2. Identify the syllabus topic(s) the question touches.
3. Read the relevant files from Directory A (weekly note + concept note + textbook chapter note for that topic) and, for coding questions, Directory B (the matched lecture notebook(s), and the relevant Homework/Coding notebook if it helps confirm style).
4. Draft the answer:
   - MCQ: pick one option, and write the justification using only definitions/complexity facts found in the files you just read. Reference which note the justification came from.
   - Coding: write the Python solution styled after the matched professor notebook. Include the professor-style approach explicitly (e.g. name which notebook's pattern you followed).
5. Run the self-check from <hard_rules> rule 5 on your own draft before showing it to me.
6. If the self-check fails on any part, go back to step 3 for that part specifically. Do not present a partially-unverified answer.
7. Present the final answer using the format in <output_format>.
</workflow>

<output_format>
For every question, respond with exactly these sections, in this order:

**Q<N> - <topic>**

**Question (as transcribed):** the full transcribed question/prompt/options.

**Answer:** the MCQ letter, or the full Python code block for coding questions.

**Reasoning:** for MCQ, the justification in a few sentences. For coding, a short walkthrough of the approach and its complexity.

**Provenance:** a short list stating exactly which files you opened for this question and what you took from each - e.g. "Read `Week - 8.md` for hash map framing (background only); read `Lectures/Week - 8/Ch11_ChainHashMap.ipynb` and copied the professor's `_hash_utility` bucket structure and separate-chaining insert pattern directly; the `find` method here is newly written by me but follows the same node-list traversal style used in that notebook's `find`." Be specific about what was read, what was copied near-verbatim, what was adapted, and what you wrote yourself using only the patterns you observed (never claim something was "the professor's method" unless you can point to the exact file and cell/section).
**Self-check result:** one line confirming the self-check in <hard_rules> rule 5 passed, or noting what you had to redo.

After all 9 questions are answered, give me a short summary table: question number, topic, answer/one-line result, and self-check status (passed clean / passed after one redo / flagged as uncovered by source material).
</output_format>

<final_reminder>
Take your time. This is worth doing slowly and correctly rather than fast. If at any point you are unsure whether something came from the source material or from your own general knowledge, treat it as general knowledge and go re-read the files. I would rather you tell me "the notes don't cover this" than give me an answer that isn't actually grounded in my professor's materials.
</final_reminder>
```
