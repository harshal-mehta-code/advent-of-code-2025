# Day 1: Secret Entrance

## Problem Summary

### Part 1
Count how many times a safe dial lands on position 0 after completing each rotation instruction.

- The dial has positions 0-99 in a circle
- Starts at position 50
- Instructions are L (left/decrease) or R (right/increase) followed by a distance
- Answer: **1168**

### Part 2
Count how many times the dial passes through or lands on position 0 during any rotation (including while rotating).

- Same setup as Part 1
- Now count every time the dial crosses 0, not just when it ends on 0
- Answer: **7199**

## Files

- `day1_input.txt` - Puzzle input (4778 rotation instructions)
- `day1_solution.py` - Part 1 solution
- `day1_part2_solution.py` - Part 2 solution
- `test_part2.py` - Test script to verify Part 2 logic with example
- `day1_part2.html` - Downloaded Part 2 problem description

## Running the Solutions

```bash
# Part 1
python3 day1_solution.py

# Part 2
python3 day1_part2_solution.py

# Test Part 2 with example
python3 test_part2.py
```
