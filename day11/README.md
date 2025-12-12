# Day 11: Reactor

## Problem Summary

### Part 1
We need to count the number of distinct paths from a starting node `you` to an ending node `out` in a system of devices described as a Directed Acyclic Graph (DAG).
**Answer:** `636`

### Part 2
We need to count the number of paths from `svr` (server rack) to `out` that explicitly visit *both* `dac` (digital-to-analog converter) and `fft` (fast Fourier transform) nodes.
**Answer:** `509312913844956`

## Solution Approach

### Part 1
- The system is parsed into an adjacency list (graph).
- Since it is a DAG, we use **Depth-First Search (DFS) with Memoization** to count paths efficiently.
- `paths(u, v)` returns the number of ways to reach `v` from `u`.

### Part 2
- A path visiting both `A` and `B` must visit them in a specific topological order.
- We check two linear sequences:
    1. `svr` -> ... -> `dac` -> ... -> `fft` -> ... -> `out`
    2. `svr` -> ... -> `fft` -> ... -> `dac` -> ... -> `out`
- The count for a sequence `A -> B -> C -> D` is `paths(A, B) * paths(B, C) * paths(C, D)`.
- We verify which node comes first topologically (or just calculate both ways; if a path is impossible, the count is 0).

## Files

-   `day11_part1.py`: Part 1 solution.
-   `day11_part2.py`: Part 2 solution.
-   `input.txt`: Puzzle input.

## Usage

```bash
# Part 1
python3 day11_part1.py

# Part 2
python3 day11_part2.py
```
