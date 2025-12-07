#!/usr/bin/env python3
"""
Test Day 2 solution with the example
"""

def is_invalid_id(num):
    """Check if a number is invalid (a sequence repeated twice)."""
    s = str(num)
    length = len(s)
    
    if length % 2 != 0:
        return False
    
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half

# Test with the example
example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

# Parse ranges
ranges = []
for range_str in example.replace('\n', '').split(','):
    range_str = range_str.strip()
    if range_str:
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))

# Find invalid IDs
total = 0
print("Invalid IDs found:")
for start, end in ranges:
    invalid_in_range = []
    for num in range(start, end + 1):
        if is_invalid_id(num):
            invalid_in_range.append(num)
            total += num
    
    if invalid_in_range:
        print(f"  {start}-{end}: {invalid_in_range}")
    else:
        print(f"  {start}-{end}: none")

print(f"\nTotal sum: {total}")
print(f"Expected: 1227775554")
