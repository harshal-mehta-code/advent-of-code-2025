#!/usr/bin/env python3
"""
Test Day 3 Part 2 solution with the example
"""

def find_max_joltage_part2(bank):
    """Find the maximum joltage by selecting exactly 12 batteries."""
    from itertools import combinations
    
    n = len(bank)
    max_joltage = 0
    
    for positions in combinations(range(n), 12):
        digits = ''.join(bank[pos] for pos in positions)
        joltage = int(digits)
        max_joltage = max(max_joltage, joltage)
    
    return max_joltage

# Test with the example
example_banks = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
]

expected = [
    987654321111,
    811111111119,
    434234234278,
    888911112111
]

print("Testing Part 2 with example:")
total = 0
for i, bank in enumerate(example_banks):
    max_joltage = find_max_joltage_part2(bank)
    print(f"  {bank}: {max_joltage} (expected: {expected[i]})")
    total += max_joltage

print(f"\nTotal: {total}")
print(f"Expected: 3121910778619")
