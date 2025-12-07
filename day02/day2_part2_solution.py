#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 2 Part 2: Gift Shop
Find invalid product IDs (numbers that are a sequence repeated at least twice).
"""

def is_invalid_id_part2(num):
    """
    Check if a number is invalid (a sequence repeated at least twice).
    Examples: 
    - 11 (1 twice)
    - 123123 (123 twice)
    - 123123123 (123 three times)
    - 1212121212 (12 five times)
    """
    s = str(num)
    length = len(s)
    
    # Try all possible pattern lengths (from 1 to length//2)
    # A pattern must repeat at least twice, so max pattern length is length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the string can be made by repeating a pattern of this length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            
            # Check if repeating the pattern gives us the original string
            if pattern * repetitions == s:
                return True
    
    return False

def solve_gift_shop_part2(input_file):
    """
    Find all invalid IDs in the given ranges and sum them (Part 2 rules).
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
            if is_invalid_id_part2(num):
                total += num
                invalid_count += 1
    
    return total, invalid_count

if __name__ == "__main__":
    answer, count = solve_gift_shop_part2("day2_input1.txt")
    print(f"Total invalid IDs found: {count}")
    print(f"Sum of all invalid IDs (Part 2): {answer}")
