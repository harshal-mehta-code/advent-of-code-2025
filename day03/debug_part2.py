#!/usr/bin/env python3
"""
Debug the greedy algorithm for Part 2
"""

def find_max_joltage_debug(bank):
    """Find the maximum joltage by selecting exactly 12 batteries - with debug output."""
    n = len(bank)
    result = []
    available_positions = list(range(n))
    
    print(f"Bank: {bank} (length {n})")
    
    for digit_position in range(12):
        remaining_needed = 12 - digit_position - 1
        max_digit = '0'
        best_pos = -1
        
        print(f"  Position {digit_position}: need {remaining_needed} more after this")
        
        for i, pos in enumerate(available_positions):
            positions_after = len(available_positions) - i - 1
            if positions_after >= remaining_needed:
                print(f"    Can choose pos {pos} ('{bank[pos]}'), {positions_after} positions after")
                if bank[pos] > max_digit:
                    max_digit = bank[pos]
                    best_pos = i
        
        print(f"  Chose '{max_digit}' at index {best_pos} (actual pos {available_positions[best_pos]})")
        result.append(max_digit)
        available_positions.pop(best_pos)
    
    return ''.join(result)

# Test with the problematic example
bank = "234234234234278"
result = find_max_joltage_debug(bank)
print(f"\nResult: {result}")
print(f"Expected: 434234234278")
