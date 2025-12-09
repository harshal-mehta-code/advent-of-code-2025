# Day 6: Trash Compactor

## Problem Summary

### Part 1
Solve "Cephalopod math" problems on a horizontally unrolled worksheet.
- Input is a grid of characters.
- Problems are separated by empty columns.
- Inside a block, numbers are arranged horizontally (standard rows), but the operator is in the last row.
- Answer: **6295830249262**

### Part 2
Solve the same worksheet using actual "Cephalopod math" rules.
- Problems are still blocks separated by empty columns.
- Numbers are written **vertically** in columns (top-to-bottom).
- Operator is still in the bottom row.
- Answer: **9194682052782**

## Files

- `day6_input.txt` - Puzzle input (math worksheet grid)
- `day6_solution.py` - Part 1 solution
- `day6_part2_solution.py` - Part 2 solution

## Running the Solutions

```bash
# Part 1
python3 day6_solution.py

# Part 2
python3 day6_part2_solution.py
```

## Algorithm

**Part 1:**
1. Parse the grid and pad lines.
2. Identify empty columns to split the grid into problem blocks.
3. For each block, extract numbers from rows (excluding operator row) and the operator from the last row.
4. Calculate result (`+` or `*`) and sum to Grand Total.

**Part 2:**
1. Same grid splitting.
2. For each block, iterate columns right-to-left.
3. Concatenate characters top-to-bottom in each column to form numbers.
4. Extract operator from last row.
5. Calculate result and sum.
