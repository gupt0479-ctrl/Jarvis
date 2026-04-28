---
type: class
status: archived
created: 2025-10-09
updated: 2025-10-17
area:
  - "[[Main Examples]]"
  - "[[Finals]]"
  - "[[Material]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Homework"
  - "#Discussion"
next: "[[Chapter - 4]]"
---
# #Textbook Textbook & Videos
## 3.1
**What is an Algorithm?**
- A set of specific steps that takes valid input and produces desired output
- Think of it like a recipe - exact instructions to follow
- Computers need these step-by-step instructions because they can't just "look and figure it out" like humans can
- Algorithms can handle much larger amounts of data than humans can process
**Example: Finding Maximum Value in a List of Numbers**
- **Step 1:** Set the first number as your "temporary maximum"
- **Step 2:** Compare the second number to your temporary max
- **Step 3:** If the new number is bigger, make it your new temporary max
- **Step 4:** If it's not bigger, ignore it and move to the next number
- **Step 5:** Repeat steps 2-4 until you've checked all numbers
- **Step 6:** When you're done, your temporary max is the actual maximum!
### Searching Algorithms
**Main purpose**: Find a specific element X in a list of distinct elements OR determine it's not there.
**Output**: Either the location/position of the element we're looking for, or 0 if it's not found  
**Real-world example**: Spell check! It searches through your text, compares words to a dictionary, and puts those red squiggly lines under misspelled words
1. **Linear Search Algorithm**: **How it works:**  
	- Goes through the list one by one from left to right  
	- Checks each element until it finds what you're looking for  
	- Like reading a book page by page until you find the chapter you want
	**Example Professor X gave us:** List: some numbers with 9 in the 7th position. 
	- Computer checks: position 1 (not 9), position 2 (not 9), position 3 (not 9)... keeps going until position 7 (found it!). 
	- **Output**: 7 (because 9 is in the 7th location)
	**Pseudocode breakdown:**  
	- **Procedure name**: linear_search
	- **Inputs**: X (what we're looking for) and a list of distinct integers a₁, a₂, ..., aₙ  
	- **Process**:
		- Start at i = 1 (first position)
		- While i ≤ n AND we haven't found X yet: keep checking next position
		- If i ≤ n when we exit the loop: we found it at position i
		- Otherwise: return 0 (not found)
2. **Binary Search Algorithm**: **Key requirement**: List MUST be in increasing order first!
	- Might need to sort the data before using this algorithm. 
	- Way more efficient than linear search for large lists
	**How it works:** Finds the middle element and compares it to what you're looking for. Eliminates half the list each time based on the comparison. Keeps narrowing down until you find it or determine it's not there.
	**Professor X's example:**
	- Looking for 9 in a sorted list  
	- Left endpoint = position 1, Right endpoint = position 7  
	- Middle = (1+7)/2 = 4, check position 4 (value is 3)  
	- Since 9 > 3, eliminate left half, new range is positions 5-7  
	- Middle = (5+7)/2 = 6, check position 6 (value is 7)  
	- Since 9 > 7, eliminate left half again, now just position 7  
	- Check position 7, find 9! **Output**: 7
	**Pseudocode breakdown:**  
	- **Procedure name**: binary_search  
	- **Inputs**: X and ordered list a₁ through aₙ (increasing order)  
	- **Variables**:
		- i = left endpoint (starts at 1)
		- j = right endpoint (starts at n)  
	- **Process**:
		- While i < j: find middle using floor((i+j)/2)
		- If X > middle value: new left endpoint is middle + 1
		- Otherwise: new right endpoint is middle
		- If X equals a[i]: return i (found it!)
		- Otherwise: return 0 (not found)
- [[Main Examples#Searching Algorithm Practice Problem|Searching Algorithm Practice Problem]]
### Sorting Algorithms
**Definition**: Algorithms that arrange elements in a list into increasing order (numerical, alphabetical, whatever!)  
**Real-world uses**: Large databases, customer numbers, part numbers, prices, phone directories (sorted by last name)  
**Fun fact**: There are over 100 different sorting algorithms in existence! (Don't worry, we're only learning 2 of them 😅)
1. **Bubble Sort Algorithm**: **Basic concept**: Compares adjacent elements and swaps them if they're in wrong order.   
	- **Key feature**: May require several passes through the entire list. 
	- **Think of it like**: Bubbles rising to the surface - bigger numbers "bubble up" to their correct positions.
	- [[Main Examples#Bubble Sort Algorithm Practice|Bubble Sort Algorithm Practice]]
2. **Insertion Sort Algorithm**: **Basic concept**: Starts with second value, asks "is this in the right spot?" and places it correctly.
	- **Key feature**: Builds the sorted list one element at a time  
	- **Think of it like**: Sorting playing cards in your hand - you pick up each card and insert it in the right position.
	- [[Main Examples#Insertion Sort Algorithm Practice problem|Insertion Sort Algorithm Examples]]
### Greedy Algorithms and Optimization
**Definition**: An algorithm that makes the best choice at each step  
**Key point**: YOU (the programmer) decide what "best choice" means for each problem  
**Common uses**: Finding shortest paths, connecting networks with minimal cable, scheduling tasks.
[[Main Examples#Greedy Algorithm Examples|Greedy Algorithm Examples]]
**NOTE**:
- **Proofs**: The mathematical proofs for why these greedy algorithms work are in your textbook - you need to study them!  
- **Optimality**: These algorithms don't just work, they give the BEST possible solution  
- **Key insight**: Greedy doesn't always work for every problem, but when it does, it's often the simplest solution
---
