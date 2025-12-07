#!/usr/bin/env python3
"""
Test Day 5 Part 2 solution with the example
"""

def count_total_fresh_ids(lines):
    """Count total unique IDs covered by all fresh ranges."""
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
    
    # Sort and merge
    ranges.sort()
    
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    # Count total
    total = 0
    for start, end in merged:
        total += (end - start + 1)
    
    print(f"Original ranges: {sorted([(s, e) for s, e in ranges])}")
    print(f"Merged ranges: {merged}")
    
    return total

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
total = count_total_fresh_ids(lines)

print(f"\nTotal fresh IDs: {total}")
print(f"Expected: 14")
print(f"(IDs: 3,4,5,10,11,12,13,14,15,16,17,18,19,20)")
