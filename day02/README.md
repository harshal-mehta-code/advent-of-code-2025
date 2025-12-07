# Day 2: Gift Shop

## Problem Summary

### Part 1
Find and sum all "invalid" product IDs in given ranges, where an invalid ID is a number consisting of a sequence of digits repeated **exactly twice**.

- Examples: 11 (1 twice), 6464 (64 twice), 123123 (123 twice)
- No leading zeros allowed (0101 is not valid)
- Answer: **40055209690**

### Part 2
Find and sum all "invalid" product IDs where an invalid ID is a number consisting of a sequence of digits repeated **at least twice**.

- Examples: 
  - 11 (1 twice)
  - 111 (1 three times)
  - 123123123 (123 three times)
  - 1212121212 (12 five times)
- Answer: **50857215650**

## Files

- `day2_input1.txt` - Puzzle input (product ID ranges)
- `day2_solution.py` - Part 1 solution
- `day2_part2_solution.py` - Part 2 solution
- `test_day2.py` - Test script for Part 1 with example
- `test_day2_part2.py` - Test script for Part 2 with example
- `day2_part1.htmll` - Part 1 problem description
- `day2_part2.html` - Part 2 problem description

## Running the Solutions

```bash
# Part 1
python3 day2_solution.py

# Part 2
python3 day2_part2_solution.py

# Test with examples
python3 test_day2.py
python3 test_day2_part2.py
```

## Algorithm

**Part 1:** Check if a number's string representation has even length and the first half equals the second half.

**Part 2:** Try all possible pattern lengths from 1 to half the number's length. If the number can be formed by repeating any pattern at least twice, it's invalid.
