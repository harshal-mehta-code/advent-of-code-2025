# Day 9: Movie Theater

## Problem Summary

### Part 1
We are given coordinates of red tiles in a grid.
Goal: Find the largest rectangle (by area) that has two red tiles as opposite corners.
Area calculation includes the boundary: `width = |x1 - x2| + 1`, `height = |y1 - y2| + 1`.
Answer: **4781235324**

## Files

- `day9_input.txt` - Puzzle input (coordinates of red tiles)
- `day9_solution.py` - Part 1 solution script
- `test_day9.py` - Test script with example case

## Running the Solutions

```bash
# Part 1
python3 day9_solution.py

# Test with example
python3 test_day9.py
```

## Algorithm

**Part 1:**
1. Parse the input to get a list of `(x, y)` coordinates.
2. Iterate through all unique pairs of points.
3. For each pair, calculate the rectangle area: `(|x1 - x2| + 1) * (|y1 - y2| + 1)`.
4. Return the maximum area found.
