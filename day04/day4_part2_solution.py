#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 4 Part 2: Printing Department
Iteratively remove accessible rolls until none remain.
"""

def count_removable_rolls(input_file):
    """
    Repeatedly remove accessible rolls (< 4 adjacent rolls) until none remain.
    Returns the total number of rolls removed.
    """
    # Read the grid into a mutable structure
    with open(input_file, 'r') as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Directions for 8 adjacent cells
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    total_removed = 0
    
    # Keep removing accessible rolls until no more can be removed
    while True:
        # Find all accessible rolls in this iteration
        accessible = []
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    # Count adjacent rolls
                    adjacent_rolls = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                            adjacent_rolls += 1
                    
                    # Accessible if fewer than 4 adjacent rolls
                    if adjacent_rolls < 4:
                        accessible.append((r, c))
        
        # If no accessible rolls found, we're done
        if not accessible:
            break
        
        # Remove all accessible rolls
        for r, c in accessible:
            grid[r][c] = '.'
        
        total_removed += len(accessible)
    
    return total_removed

if __name__ == "__main__":
    answer = count_removable_rolls("day4_input1.txt")
    print(f"Total rolls removed: {answer}")
