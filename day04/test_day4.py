#!/usr/bin/env python3
"""
Test Day 4 solution with the example
"""

def count_accessible_rolls(grid_lines):
    """Count rolls that have fewer than 4 adjacent rolls."""
    grid = [line.strip() for line in grid_lines if line.strip()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    accessible_count = 0
    accessible_positions = []
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                adjacent_rolls = 0
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        adjacent_rolls += 1
                
                if adjacent_rolls < 4:
                    accessible_count += 1
                    accessible_positions.append((r, c))
    
    return accessible_count, accessible_positions

# Test with the example
example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

lines = example.split('\n')
count, positions = count_accessible_rolls(lines)

print(f"Accessible rolls: {count}")
print(f"Expected: 13")
print(f"\nPositions: {positions}")
