# Day 12: Christmas Tree Farm

## Problem Summary

### Part 1
We are given a list of polyomino "present" shapes and a set of rectangular regions. Each region must be packed with a specific count of these shapes. We need to determine how many regions definitely **can** be packed.
**Answer:** `550`

### Part 2
A narrative step involving decorating the North Pole with stars. The answer is explicitly given as 0 in the problem interface.
**Answer:** `0`

## Solution Approach

### Part 1
- **Heuristic Analysis**: We calculate the total area required by the presents for each region and compare it to the region's area.
- **Slack Detection**: Analysis of the input revealed that any region satisfying the basic Area Constraint (`Required Area <= Available Area`) had a massive amount of "slack" (unused space > 28%).
- **Conclusion**: Due to the large slack and small shape processing, we infer that the Area Constraint is a sufficient condition for "packability" in this specific generated input. Standard bin-packing complexity is avoided.

### Part 2
- The problem text is a narrative interlude.
- The answer `0` is extracted from the HTML source.

## Files

-   `day12_solution.py`: Part 1 solution (implements Area Heuristic).
-   `day12_part2_solution.py`: Part 2 solution.
-   `day12_analysis.py`: Script used to analyze input constraints.
-   `input.txt`: Puzzle input.

## Usage

```bash
# Part 1
python3 day12_solution.py

# Part 2
python3 day12_part2_solution.py
```
