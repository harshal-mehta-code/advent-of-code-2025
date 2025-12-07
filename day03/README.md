# Day 3: Lobby

## Problem Summary

### Part 1
Find the maximum joltage from each battery bank by selecting exactly 2 batteries.

- Each bank is a sequence of digits (1-9)
- Select 2 batteries to form a 2-digit number
- Cannot rearrange batteries (must maintain order)
- Find the maximum possible 2-digit number for each bank
- Answer: **16812**

### Part 2
Find the maximum joltage from each battery bank by selecting exactly 12 batteries.

- Same setup as Part 1
- Now select 12 batteries to form a 12-digit number
- Use greedy algorithm to find lexicographically largest subsequence
- Answer: **166345822896410**

## Files

- `day3_input1.txt` - Puzzle input (200 battery banks)
- `day3_solution.py` - Part 1 solution
- `day3_part2_solution.py` - Part 2 solution
- `test_day3.py` - Test script for Part 1 with example
- `test_day3_part2.py` - Test script for Part 2 with example
- `debug_part2.py` - Debug script used during development

## Running the Solutions

```bash
# Part 1
python3 day3_solution.py

# Part 2
python3 day3_part2_solution.py

# Test with examples
python3 test_day3.py
python3 test_day3_part2.py
```

## Algorithm

**Part 1:** Try all pairs of positions (i, j) where i < j, form the 2-digit number, and find the maximum.

**Part 2:** Greedy algorithm that builds the 12-digit number from left to right:
- For each digit position, select the largest available digit
- Ensure enough positions remain to complete the 12-digit number
- Time complexity: O(n*k) where n is bank length and k=12
