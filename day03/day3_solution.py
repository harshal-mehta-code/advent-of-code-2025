#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 3: Lobby
Find the maximum joltage from each battery bank.
"""

def find_max_joltage(bank):
    """
    Find the maximum joltage possible from a bank of batteries.
    We need to select exactly 2 batteries (in order) to maximize the 2-digit number.
    """
    max_joltage = 0
    
    # Try all pairs of positions (i, j) where i < j
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            # Form the 2-digit number from batteries at positions i and j
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    
    return max_joltage

def solve_lobby(input_file):
    """
    Find the total output joltage from all battery banks.
    """
    total_joltage = 0
    
    with open(input_file, 'r') as f:
        for line in f:
            bank = line.strip()
            if bank:  # Skip empty lines
                max_joltage = find_max_joltage(bank)
                total_joltage += max_joltage
    
    return total_joltage

if __name__ == "__main__":
    answer = solve_lobby("day3_input1.txt")
    print(f"Total output joltage: {answer}")
