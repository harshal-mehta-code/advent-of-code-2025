#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 2: Gift Shop
Find invalid product IDs (numbers that are a sequence repeated twice).
"""

def is_invalid_id(num):
    """
    Check if a number is invalid (a sequence repeated twice).
    Examples: 11 (1 twice), 6464 (64 twice), 123123 (123 twice)
    """
    s = str(num)
    length = len(s)
    
    # Must have even length to be repeatable
    if length % 2 != 0:
        return False
    
    # Check if first half equals second half
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half

def solve_gift_shop(input_file):
    """
    Find all invalid IDs in the given ranges and sum them.
    """
    # Read the input
    with open(input_file, 'r') as f:
        content = f.read().strip()
    
    # Parse the ranges
    ranges = []
    for range_str in content.split(','):
        range_str = range_str.strip()
        if range_str:
            start, end = map(int, range_str.split('-'))
            ranges.append((start, end))
    
    # Find all invalid IDs
    total = 0
    invalid_count = 0
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total += num
                invalid_count += 1
    
    return total, invalid_count

if __name__ == "__main__":
    answer, count = solve_gift_shop("day2_input1.txt")
    print(f"Total invalid IDs found: {count}")
    print(f"Sum of all invalid IDs: {answer}")
