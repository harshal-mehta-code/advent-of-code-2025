#!/usr/bin/env python3
"""
Test Day 3 solution with the example
"""

def find_max_joltage(bank):
    """Find the maximum joltage possible from a bank of batteries."""
    max_joltage = 0
    
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage

# Test with the example
example_banks = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
]

print("Testing with example:")
total = 0
for bank in example_banks:
    max_joltage = find_max_joltage(bank)
    print(f"  {bank}: max joltage = {max_joltage}")
    total += max_joltage

print(f"\nTotal: {total}")
print(f"Expected: 357")
