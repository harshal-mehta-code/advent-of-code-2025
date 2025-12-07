# Day 4: Printing Department

## Problem Summary

### Part 1
Count how many rolls of paper can be accessed by forklifts.

- Grid of rolls (`@`) and empty spaces (`.`)
- A roll is accessible if it has **fewer than 4** rolls in the 8 adjacent positions (including diagonals)
- Answer: **1604**

### Part 2
Iteratively remove accessible rolls until no more can be removed.

- Remove all accessible rolls simultaneously
- After removal, some previously inaccessible rolls may become accessible
- Repeat until no more rolls can be removed
- Count total rolls removed
- Answer: **9397**

## Files

- `day4_input1.txt` - Puzzle input (140×140 grid)
- `day4_solution.py` - Part 1 solution
- `day4_part2_solution.py` - Part 2 solution
- `test_day4.py` - Test script for Part 1 with example
- `test_day4_part2.py` - Test script for Part 2 with example

## Running the Solutions

```bash
# Part 1
python3 day4_solution.py

# Part 2
python3 day4_part2_solution.py

# Test with examples
python3 test_day4.py
python3 test_day4_part2.py
```

## Algorithm

**Part 1:** 
- Iterate through each cell in the grid
- For each `@`, count adjacent `@` symbols in all 8 directions
- If count < 4, the roll is accessible
- Time complexity: O(rows × cols)

**Part 2:**
- Repeatedly find all accessible rolls and remove them simultaneously
- Continue until no accessible rolls remain
- Time complexity: O(iterations × rows × cols)
- In practice, iterations is small (9 for the example, likely similar for the input)
