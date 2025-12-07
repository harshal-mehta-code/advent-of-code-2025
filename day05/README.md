# Day 5: Cafeteria

## Problem Summary

### Part 1
Count how many available ingredient IDs are fresh (fall within any fresh ID range).

- Input has two sections: fresh ID ranges and available IDs
- Ranges are inclusive and can overlap
- An ID is fresh if it falls in ANY range
- Answer: **782**

### Part 2
Count the total number of unique ingredient IDs considered fresh across all ranges.

- Ignore the available IDs section
- Count all unique IDs covered by the fresh ranges
- Ranges can overlap, so need to merge them
- Answer: **353863745078671**

## Files

- `input.txt` - Puzzle input (~186 ranges, ~1000 available IDs)
- `day5_solution.py` - Part 1 solution
- `day5_part2_solution.py` - Part 2 solution
- `test_day5.py` - Test script for Part 1 with example
- `test_day5_part2.py` - Test script for Part 2 with example

## Running the Solutions

```bash
# Part 1
python3 day5_solution.py

# Part 2
python3 day5_part2_solution.py

# Test with examples
python3 test_day5.py
python3 test_day5_part2.py
```

## Algorithm

**Part 1:** 
- Parse ranges and available IDs
- For each available ID, check if it falls in any range
- Time complexity: O(n × m) where n = available IDs, m = ranges

**Part 2:**
- Parse and sort all ranges
- Merge overlapping/adjacent ranges using interval merging
- Sum the lengths of merged ranges: (end - start + 1) for each
- Time complexity: O(m log m) for sorting ranges
- **Key optimization:** Instead of enumerating ~353 trillion IDs, we calculate the count mathematically after merging ranges
