#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 5 Part 2: Cafeteria
Count total unique ingredient IDs considered fresh across all ranges.
"""

def count_total_fresh_ids(input_file):
    """
    Count total unique IDs covered by all fresh ranges.
    Uses interval merging to handle overlapping ranges efficiently.
    """
    with open(input_file, 'r') as f:
        lines = [line.strip() for line in f]
    
    # Find the blank line
    blank_idx = lines.index('')
    
    # Parse fresh ID ranges
    ranges = []
    for i in range(blank_idx):
        if lines[i]:
            parts = lines[i].split('-')
            start = int(parts[0])
            end = int(parts[1])
            ranges.append((start, end))
    
    # Sort ranges by start position
    ranges.sort()
    
    # Merge overlapping ranges
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            # Overlapping or adjacent - merge with previous range
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            # Non-overlapping - add as new range
            merged.append((start, end))
    
    # Count total IDs in merged ranges
    total = 0
    for start, end in merged:
        # Range is inclusive, so count is (end - start + 1)
        total += (end - start + 1)
    
    return total

if __name__ == "__main__":
    answer = count_total_fresh_ids("input.txt")
    print(f"Total fresh ingredient IDs: {answer}")
