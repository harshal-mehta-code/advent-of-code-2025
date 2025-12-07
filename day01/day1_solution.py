#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 1: Secret Entrance
Solve the safe dial puzzle by counting how many times the dial points at 0.
"""

def solve_safe_puzzle(input_file):
    """
    Count how many times the dial points at 0 after each rotation.
    
    The dial:
    - Has numbers 0-99 in a circle
    - Starts at position 50
    - L means rotate left (toward lower numbers)
    - R means rotate right (toward higher numbers)
    - Wraps around (0 -> 99 when going left, 99 -> 0 when going right)
    """
    # Read all rotations
    with open(input_file, 'r') as f:
        rotations = [line.strip() for line in f if line.strip()]
    
    # Start at position 50
    position = 50
    zero_count = 0
    
    # Process each rotation
    for rotation in rotations:
        direction = rotation[0]  # 'L' or 'R'
        distance = int(rotation[1:])  # The number after L or R
        
        if direction == 'L':
            # Rotate left (subtract, wrapping around)
            position = (position - distance) % 100
        else:  # direction == 'R'
            # Rotate right (add, wrapping around)
            position = (position + distance) % 100
        
        # Check if we landed on 0
        if position == 0:
            zero_count += 1
    
    return zero_count

if __name__ == "__main__":
    answer = solve_safe_puzzle("day1_input.txt")
    print(f"The password is: {answer}")
