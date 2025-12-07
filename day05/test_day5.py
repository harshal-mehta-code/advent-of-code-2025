#!/usr/bin/env python3
"""
Test Day 5 solution with the example
"""

def count_fresh_ingredients(lines):
    """Count how many available ingredient IDs are fresh."""
    # Find the blank line
    blank_idx = lines.index('')
    
    # Parse ranges
    ranges = []
    for i in range(blank_idx):
        if lines[i]:
            parts = lines[i].split('-')
            start = int(parts[0])
            end = int(parts[1])
            ranges.append((start, end))
    
    # Parse available IDs
    available_ids = []
    for i in range(blank_idx + 1, len(lines)):
        if lines[i]:
            available_ids.append(int(lines[i]))
    
    # Count fresh
    fresh_count = 0
    fresh_ids = []
    
    for ingredient_id in available_ids:
        is_fresh = False
        for start, end in ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        
        if is_fresh:
            fresh_count += 1
            fresh_ids.append(ingredient_id)
    
    return fresh_count, fresh_ids

# Test with the example
example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

lines = example.strip().split('\n')
count, fresh = count_fresh_ingredients(lines)

print(f"Fresh ingredients: {count}")
print(f"Fresh IDs: {fresh}")
print(f"Expected: 3 (IDs: 5, 11, 17)")
