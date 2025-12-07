#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 4: Printing Department
Count rolls of paper accessible by forklifts.
"""

def count_accessible_rolls(input_file):
    """
    Count rolls that have fewer than 4 adjacent rolls.
    A roll is accessible if it has < 4 rolls in the 8 adjacent positions.
    """
    # Read the grid
    with open(input_file, 'r') as f:
        grid = [line.strip() for line in f if line.strip()]
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Directions for 8 adjacent cells (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # top-left, top, top-right
        (0, -1),           (0, 1),    # left, right
        (1, -1),  (1, 0),  (1, 1)     # bottom-left, bottom, bottom-right
    ]
    
    accessible_count = 0
    
    # Check each cell
    for r in range(rows):
        for c in range(cols):
            # Only check if this cell is a roll
            if grid[r][c] == '@':
                # Count adjacent rolls
                adjacent_rolls = 0
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check if neighbor is within bounds and is a roll
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        adjacent_rolls += 1
                
                # Accessible if fewer than 4 adjacent rolls
                if adjacent_rolls < 4:
                    accessible_count += 1
    
    return accessible_count

if __name__ == "__main__":
    answer = count_accessible_rolls("day4_input1.txt")
    print(f"Accessible rolls: {answer}")
