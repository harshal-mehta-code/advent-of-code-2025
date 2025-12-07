#!/usr/bin/env python3
"""
Test the Part 2 solution with the example
"""

def solve_safe_puzzle_part2_test():
    """
    Test with the example:
    L68 L30 R48 L5 R60 L55 L1 L99 R14 L82
    Expected: 6
    """
    rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    
    position = 50
    zero_count = 0
    
    print(f"Starting position: {position}")
    
    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])
        old_position = position
        
        if direction == 'L':
            complete_loops = distance // 100
            zero_count += complete_loops
            
            remaining = distance % 100
            new_position = (position - remaining) % 100
            
            passed = False
            if new_position == 0:
                zero_count += 1
                passed = True
            elif remaining > position and position != 0:
                zero_count += 1
                passed = True
            
            if passed:
                print(f"{rotation}: {old_position} -> {new_position} (passed through 0)")
            else:
                print(f"{rotation}: {old_position} -> {new_position}")
            
            position = new_position
            
        else:  # R
            complete_loops = distance // 100
            zero_count += complete_loops
            
            remaining = distance % 100
            new_position = (position + remaining) % 100
            
            passed = False
            if new_position == 0:
                zero_count += 1
                passed = True
            elif position + remaining >= 100 and new_position != 0:
                zero_count += 1
                passed = True
            
            if passed:
                print(f"{rotation}: {old_position} -> {new_position} (passed through 0)")
            else:
                print(f"{rotation}: {old_position} -> {new_position}")
            
            position = new_position
    
    print(f"\nTotal zero count: {zero_count}")
    print(f"Expected: 6")
    return zero_count

if __name__ == "__main__":
    solve_safe_puzzle_part2_test()
