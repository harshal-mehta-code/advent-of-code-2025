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

### Part 2
We need to connect all junction boxes into a single circuit (Minimum Spanning Tree).
- Connect closest components until only 1 component remains.
- Find the product of the X-coordinates of the last connected pair.
- Answer: **3767453340**

## Files

- `day8_input.txt` - Puzzle input (3D coordinates)
- `day8_solution.py` - Part 1 solution
- `day8_part2_solution.py` - Part 2 solution
- `test_day8.py` - Test script for Part 1
- `test_day8_part2.py` - Test script for Part 2

## Running the Solutions

```bash
# Part 1
python3 day8_solution.py

# Part 2
python3 day8_part2_solution.py

# Test with example
python3 test_day8.py
python3 test_day8_part2.py
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

**Part 2:**
1. Parse input points.
2. Generate and sort all edges by distance.
3. Use **Kruskal's Algorithm** (Union-Find) to build the Minimum Spanning Tree.
4. Track the number of connected components.
5. Identify the edge that reduces the component count to 1.
6. Return the product of the X-coordinates of that edge's endpoints.
