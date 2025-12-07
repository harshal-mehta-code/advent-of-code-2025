#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 5: Cafeteria
Determine which available ingredient IDs are fresh.
"""

def count_fresh_ingredients(input_file):
    """
    Count how many available ingredient IDs fall within fresh ranges.
    Ranges are inclusive and can overlap.
    """
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f]
    
    # Find the blank line that separates ranges from IDs
    blank_idx = lines.index('')
    
    # Parse fresh ID ranges
    ranges = []
    for i in range(blank_idx):
        if lines[i]:
            parts = lines[i].split('-')
            start = int(parts[0])
            end = int(parts[1])
            ranges.append((start, end))
    
    # Parse available ingredient IDs
    available_ids = []
    for i in range(blank_idx + 1, len(lines)):
        if lines[i]:
            available_ids.append(int(lines[i]))
    
    # Count how many available IDs are fresh
    fresh_count = 0
    
    for ingredient_id in available_ids:
        # Check if this ID falls in any range
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        
        if is_fresh:
            fresh_count += 1
    
    return fresh_count

if __name__ == "__main__":
    answer = count_fresh_ingredients("input.txt")
    print(f"Fresh ingredients: {answer}")
