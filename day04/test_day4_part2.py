#!/usr/bin/env python3
"""
Test Day 4 Part 2 solution with the example
"""

def count_removable_rolls(grid_lines):
    """Repeatedly remove accessible rolls until none remain."""
    grid = [list(line.strip()) for line in grid_lines if line.strip()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    total_removed = 0
    iteration = 0
    
    while True:
        accessible = []
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    adjacent_rolls = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                            adjacent_rolls += 1
                    
                    if adjacent_rolls < 4:
                        accessible.append((r, c))
        
        if not accessible:
            break
        
        for r, c in accessible:
            grid[r][c] = '.'
        
        iteration += 1
        total_removed += len(accessible)
        print(f"Iteration {iteration}: Removed {len(accessible)} rolls (total: {total_removed})")
    
    return total_removed

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
total = count_removable_rolls(lines)

print(f"\nTotal rolls removed: {total}")
print(f"Expected: 43")
