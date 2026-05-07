---
type: class
status: archived
created: 2025-11-13
updated: 2025-11-14
area:
  - "[[Main Examples]]"
  - "[[Material]]"
  - "[[Finals]]"
tags:
  - "#class"
  - "#Homework"
  - "#Textbook"
  - "#Discussion"
next: "[[Chapter - 7]]"
---
# #Textbook Textbook & Videos
## 6.1
### Counting Rules
1. **The Product Rule (When Things Happen in Sequence)**:
	- **What it is**: When you have a procedure with multiple steps, multiply the number of options for each step  
	- **Formula**: If you have n₁ ways for step 1, n₂ ways for step 2, etc., then total ways = n₁ × n₂ × n₃...  
	- **Example**: Getting dressed with 4 t-shirts and 3 pairs of shorts = 4 × 3 = 12 different outfits  
	- **Key point**: Use this when tasks happen one after another (sequence matters!)
2. **Tree Diagrams (Visual Way to See All Outcomes)**:
	- **What it is**: A branching diagram that shows every possible outcome visually  
	- **When to use**: Best used with product rule situations to actually see what the outcomes are  
	- **How to make one**:
		- Start with branches for first choice (4 branches for 4 t-shirts)
		- From each branch, make new branches for next choice (3 branches for 3 shorts from each t-shirt)
		- Follow each path to list all outcomes (t-shirt 1 + shorts 1, t-shirt 1 + shorts 2, etc.)  
		- **Critical step**: Actually count/list all the final outcomes - students always forget this!  
		- **Result**: Should match your product rule calculation (12 total outfits)
3. **The Sum Rule (When You Have "OR" Choices)**:
	- **What it is**: When you can do a task in one way OR another way (not both) 
	- **Formula**: n₁ + n₂ + n₃... ways total  
	- **Keyword**: "OR" - this tells you to add, not multiply  
	- **Example**: Beach vacation choices - 37 international beaches OR 14 domestic beaches = 37 + 14 = 51 total choices  
	- **Math notation**: |A₁ ∪ A₂ ∪ A₃...| = |A₁| + |A₂| + |A₃|... (when sets don't overlap)
4. **The Subtraction Rule (Inclusion-Exclusion Principle)**
	- **What it is**: When your "OR" choices overlap, you have to subtract the overlap to avoid double-counting  
	- **Formula**: n₁ + n₂ - (number of overlapping ways)  
	- **Why needed**: If something gets counted in both groups, you counted it twice!  
	- **Complex example**: 7-bit strings that start with 1 OR end with 000
		- Start with 1: First bit = 1, other 6 bits can be anything = 2⁶ = 64 ways
		- End with 000: Last 3 bits = 000, first 4 bits can be anything = 2⁴ = 16 ways
		- Overlap: Start with 1 AND end with 000 = 1___000, middle 3 bits can be anything = 2³ = 8 ways
		- **Answer**: 64 + 16 - 8 = 72 total ways  
		- **Key insight**: The 8 overlapping cases were counted in both the "start with 1" group AND the "end with 000" group.
5. **The Division Rule (When Multiple Arrangements Are "The Same")**
	- **What it is**: When different arrangements should be considered identical, divide by the number of "equivalent" arrangements  
	- **Formula**: n ÷ d ways (where n = total arrangements, d = number of equivalent arrangements per group)  
	- **Tricky example**: Seating 6 people around a circular table
		- Normal calculation: 6! = 720 ways to arrange 6 people
		- **But**: Rotating everyone one seat clockwise gives the "same" seating (same neighbors)
		- Person A could sit in position 1, 2, 3, 4, 5, or 6 and it's the "same" if everyone else rotates too
		- So 6 different arrangements are actually identical
		- **Answer**: 6! ÷ 6 = 720 ÷ 6 = 120 unique circular seatings.  
    - **Why this works**: Each unique seating gets counted 6 times (once for each starting position), so divide by 6. 
### Key Things to Remember for the Exam:
- **Product rule**: Multiply when things happen in sequence (AND situations)  
- **Sum rule**: Add when you have separate choices (OR situations with no overlap)  
- **Subtraction rule**: Add then subtract overlap (OR situations with overlap)  
- **Division rule**: Divide when multiple arrangements count as "the same".
## 6.3
### Permutations and Combinations
**Permutations** = Order MATTERS (like race positions - 1st place ≠ 3rd place!)  
**Combinations** = Order DOESN'T matter (like poker cards - doesn't matter if you get the King first or last).
1. **Permutations**: $$P(n,k) or (nPk) = \frac{n!}{(n-k)!}$$
	- n = total objects you have  
	- k = how many you're choosing  
	- Some calculators use "R" instead of "K" - same thing!
	- How It Works: Example: 3 objects (A, B, C), choosing 2 at a time. 
		- Possible arrangements: AB, AC, BA, BC, CA, CB = **6 total**  
		- Using counting rules: 3 choices for first spot × 2 choices for second spot = 6  
		- Using formula: P(3,2) = 3!/(3-2)! = 6/1 = 6 ✓
	- Why the Formula Works: n! = n × (n-1) × (n-2) × ... × (n-k+1) × (n-k) × ... × 2 × 1  
		- (n-k)! = (n-k) × (n-k-1) × ... × 2 × 1  
		- When you divide, everything from (n-k) down cancels out. You're left with: n × (n-1) × (n-2) × ... × (n-k+1)  
		- This is exactly the counting rule method.
2. **Combinations (Order Doesn't Matter!)**: $$C(n,k) or (nCk) = \frac{n!}{[(n-k)! × k!]}$$It's the permutation formula DIVIDED BY k! The k! removes all the redundant arrangements.
- How It Works: Same example: 3 objects (A, B, C), choosing 2 at a time. With permutations we had: AB, AC, BA, BC, CA, CB = 6.
	- But AB = BA, AC = CA, BC = CB when order doesn't matter  
	- So we have only 3 unique combinations: {A,B}, {A,C}, {B,C}  
	- Using formula: C(3,2) = 3!/(1! × 2!) = 6/2 = 3 ✓
- Why We Divide by k!: k! counts all the ways to arrange k objects. 
	- Since we don't care about order, we divide out these redundant arrangements  
	- Example: 2 objects can be arranged 2! = 2 ways, so we divide by 2
- [[Main Examples#PNC Practice Examples|PNC Practice Examples]]
- [[Main Examples#|Counting Rules and Combinatorics Practice]]
#### Calculator Tips:
Look for nPr and nCr buttons on your calculator. Some calculators have these in menus.
- Always double-check by thinking about whether your answer makes sense!
## 6.4
### Binomial Theorem and Pascal's Triangle
**The Problem**: Imagine trying to expand (3x + 2)^100 by hand - you'd be multiplying forever!  
**The Solution**: The binomial theorem gives us a shortcut formula to expand any binomial (two-term expression) raised to any power  
**Why it matters**: Instead of doing endless multiplication, we can find specific coefficients directly.
1. **The Binomial Theorem Formula**:
	- **General form**: $$(x + y)^n = \sum_{j=0}{[n j] × x^{(n-j)} × y^j}$$
	- **What this means**:
		- n choose j($nj$) = binomial coefficient (tells us the number in front of each term)
		- $x^{(n-j)}$ = the first term's power decreases as we go
		- $y^j$ = the second term's power increases as we go
		- We add up all terms from j=0 to j=n
	- Step-by-Step Example: (x + y)^4
		- **Term 1** (j=0): 4 choose 0 × x^4 × y^0 = 1 × x^4 × 1 = x^4  
		- **Term 2** (j=1): 4 choose 1 × x^3 × y^1 = 4 × x^3 × y = 4x^3y  
		- **Term 3** (j=2): 4 choose 2 × x^2 × y^2 = 6 × x^2 × y^2 = 6x^2y^2  
		- **Term 4** (j=3): 4 choose 3 × x^1 × y^3 = 4 × x × y^3 = 4xy^3  
		- **Term 5** (j=4): 4 choose 4 × x^0 × y^4 = 1 × 1 × y^4 = y^4  
		- **Final answer**: x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + y^4
	- *How to Calculate Binomial Coefficients*:
		- **Formula**: n choose k = $$\frac{n!}{(k!(n-k)!)}$$
		- **Examples**:
			- 4 choose 0 = 4!/(0!×4!) = 1
			- 4 choose 1 = 4!/(1!×3!) = 4
			- 4 choose 2 = 4!/(2!×2!) = 6
			- 4 choose 3 = 4!/(3!×1!) = 4
			- 4 choose 4 = 4!/(4!×0!) = 1
		- [[Main Examples#Binomial Theorem and Pascal's Triangle|Real Examples]]
### Pascal's Identity (The Building Block)
**Formula**: (n+1) choose k = (n choose k-1) + (n choose k)  
**What it means**: Any binomial coefficient equals the sum of the two coefficients above it  
**Why it works**: Think of it as choosing k items from n+1 items - either you include a specific item (and choose k-1 from the rest) or you don't include it (and choose all k from the rest)
#### Pascal's Triangle (The Cheat Sheet!)
**What it is**: A triangular arrangement where each number is the sum of the two numbers above it.
**Structure**:
```bash
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
1 5 10 10 5 1
```
**How to use it**: Row n gives you all the coefficients for $(x + y)^n$  
- **Example**: Row 4 gives us 1, 4, 6, 4, 1 - exactly the coefficients we found for $(x + y)^4!$
1. *Building Pascal's Triangle Using Pascal's Identity*:
	- **Row 4**: 1, 4, 6, 4, 1  
	- **Building Row 5**:
		- Start and end with 1
		- 1 + 4 = 5
		- 4 + 6 = 10
		- 6 + 4 = 10
		- 4 + 1 = 5  
	- **Row 5**: 1, 5, 10, 10, 5, 1  
	- **Instant expansion**: $(x + y)^5 = x^5 + 5x^4y + 10x^3y^2 + 10x^2y^3 + 5xy^4 + y^5$
- *Key Patterns to Remember*:
	- **Powers of x**: Start at n and decrease by 1 each term until you reach 0  
	- **Powers of y**: Start at 0 and increase by 1 each term until you reach n  
	- **Coefficients**: Use Pascal's triangle or calculate binomial coefficients  
	- **Total terms**: For (x + y)^n, you get exactly n + 1 terms

---
# #Homework Homework 7


---
# #Discussion Discussion 7


---
