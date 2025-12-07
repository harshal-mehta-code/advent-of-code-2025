#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 3 Part 2: Lobby
Find the maximum joltage from each battery bank using 12 batteries.
"""

from itertools import combinations

def find_max_joltage_part2(bank):
    """
    Find the maximum joltage possible from a bank by selecting exactly 12 batteries.
    We use a greedy algorithm to find the lexicographically largest subsequence of length 12.
    """
    n = len(bank)
    k = 12  # number of batteries to select
    
    # Greedy algorithm: build the result digit by digit
    # For each position, choose the largest digit such that we can still select enough digits after it
    result = []
    start_pos = 0
    
    for i in range(k):
        # How many more digits do we need after this one?
        remaining = k - i - 1
        
        # Find the largest digit in the range where we can still pick 'remaining' digits after it
        # We need at least 'remaining' positions after our choice
        max_digit = '0'
        best_pos = start_pos
        
        # We can choose from start_pos to (n - remaining - 1)
        for pos in range(start_pos, n - remaining):
            if bank[pos] > max_digit:
                max_digit = bank[pos]
                best_pos = pos
        
        result.append(max_digit)
        start_pos = best_pos + 1
    
    return int(''.join(result))

def solve_lobby_part2(input_file):
    """
    Find the total output joltage from all battery banks (Part 2).
    """
    total_joltage = 0
    
    with open(input_file, 'r') as f:
        for line in f:
            bank = line.strip()
            if bank:  # Skip empty lines
                max_joltage = find_max_joltage_part2(bank)
                total_joltage += max_joltage
    
    return total_joltage

if __name__ == "__main__":
    answer = solve_lobby_part2("day3_input1.txt")
    print(f"Total output joltage (Part 2): {answer}")
