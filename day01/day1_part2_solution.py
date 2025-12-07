#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 1 Part 2: Secret Entrance
Count how many times the dial passes through 0 during any rotation.
"""

def solve_safe_puzzle_part2(input_file):
    """
    Count how many times the dial points at 0 during any rotation.
    
    The dial:
    - Has numbers 0-99 in a circle
    - Starts at position 50
    - L means rotate left (toward lower numbers)
    - R means rotate right (toward higher numbers)
    - We count EVERY time the dial passes through 0, not just when it ends on 0
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
            # Rotating left (decreasing position)
            # Count how many times we pass through or land on 0
            
            # Calculate how many complete loops we make (each loop passes 0 once)
            complete_loops = distance // 100
            zero_count += complete_loops
            
            # Check if we pass through or land on 0 in the partial rotation
            remaining = distance % 100
            new_position = (position - remaining) % 100
            
            # We pass through/land on 0 if:
            # - We land exactly on 0 (new_position == 0), OR
            # - We wrap around (remaining > position and position != 0)
            if new_position == 0:
                zero_count += 1
            elif remaining > position and position != 0:
                zero_count += 1
            
            position = new_position
            
        else:  # direction == 'R'
            # Rotating right (increasing position)
            # Calculate how many complete loops we make
            complete_loops = distance // 100
            zero_count += complete_loops
            
            # Check if we pass through or land on 0 in the partial rotation
            remaining = distance % 100
            new_position = (position + remaining) % 100
            
            # We pass through/land on 0 if:
            # - We land exactly on 0 (new_position == 0), OR  
            # - We wrap around (position + remaining >= 100 and new_position != 0)
            if new_position == 0:
                zero_count += 1
            elif position + remaining >= 100 and new_position != 0:
                zero_count += 1
            
            position = new_position
    
    return zero_count

if __name__ == "__main__":
    answer = solve_safe_puzzle_part2("day1_input.txt")
    print(f"The password (Part 2) is: {answer}")
