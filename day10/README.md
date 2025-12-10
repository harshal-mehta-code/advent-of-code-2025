# Day 10: Factory

## Problem Summary

### Part 1
We need to configure machines by setting indicator lights (binary) to a target pattern.
Finding the minimum button presses is a linear algebra problem over GF(2).
**Answer:** `491`

### Part 2
We need to configure machines by matching joltage counters (integers) to target values.
Finding the minimum button presses is an Integer Linear Programming problem (minimizing sum of non-negative integers).
**Answer:** `20617`

## Solution Approach

### Part 1
- Modeled as $Ax = b$ in GF(2).
- Solved using Gaussian Elimination.
- Optimized over free variables for minimum Hamming weight.

### Part 2
- Modeled as $Ax = b$ in integers with $x \ge 0$.
- Solved using Gaussian Elimination (fractional arithmetic).
- **Bounding Constraint**: Since $A$ contains only 0s and 1s, each variable $x_j$ is bounded by $\min \{ b_i \mid A_{ij} = 1 \}$. This allows efficiently searching the space of free variables.

## Files

-   `day10_solution.py`: Part 1 solution.
-   `day10_part2_solution.py`: Part 2 solution.
-   `input.txt`: Puzzle input.
-   `test_day10.py`, `test_day10_part2.py`: Unit tests.

## Usage

```bash
# Part 1
python3 day10_solution.py

# Part 2
python3 day10_part2_solution.py
```
