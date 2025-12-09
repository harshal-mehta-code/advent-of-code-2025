# Day 7: Laboratories

## Problem Summary

### Part 1
A tachyon beam travels down through a manifold.
- Starts at `S`.
- Moves downward.
- If it hits a splitter `^`, it stops, and two new beams start from the left and right, moving downward.
- Beams pass through empty space `.`.
- Goal: Count the number of splitters activated.
- Answer: **1566**

## Files

- `day7_input.txt` - Puzzle input (tachyon manifold diagram)
- `day7_part1_solution.py` - Part 1 solution
- `test_day7.py` - Test script for Part 1 with example

## Running the Solutions

```bash
# Part 1
python3 day7_solution.py

# Test with example
python3 test_day7.py
```

## Algorithm

**Part 1:**
1. Parse the grid. Find `S`.
2. Use a Queue for BFS to trace beams.
3. Queue stores `(row, col)` of beam HEADS.
4. Process queue:
   - Move beam downwards from head.
   - If `^` encountered:
     - Mark as visited (count it).
     - Queue new heads at `(r, c-1)` and `(r, c+1)`.
     - Stop tracing current beam.
5. Return count of unique splitters hit.
