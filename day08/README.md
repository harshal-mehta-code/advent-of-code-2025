# Day 8: Playground

## Problem Summary

### Part 1
The Elves are connecting electrical junction boxes in a 3D space.
- Connections are made between "closest" pairs of boxes (Euclidean distance).
- We make the **1000** shortest possible connections.
- Connecting boxes merges them into the same circuit.
- Goal: Calculate component sizes (number of boxes in each circuit).
- Result: Multiply the sizes of the **three largest** circuits.
- Answer: **67488**

## Files

- `day8_input.txt` - Puzzle input (3D coordinates of junction boxes)
- `day8_solution.py` - Part 1 solution script
- `test_day8.py` - Test script with example case

## Running the Solutions

```bash
# Part 1
python3 day8_solution.py

# Test with example
python3 test_day8.py
```

## Algorithm

**Part 1:**
1. Parse input points `(x, y, z)`.
2. Generate all pairwise connections and their squared distances.
3. Sort connections by distance ascending.
4. Select the top 1000 connections.
5. Use **Union-Find** data structure to merge components.
6. Calculate sizes of all disjoint sets.
7. Sort sizes descending and multiply the top 3.
