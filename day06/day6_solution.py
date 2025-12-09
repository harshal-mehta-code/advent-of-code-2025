import sys

def solve():
    try:
        with open('day6_input.txt', 'r') as f:
            lines = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print("Error: input.txt not found.")
        return

    if not lines:
        print("Error: input.txt is empty.")
        return

    # Pad all lines to the maximum length to treat as a grid
    max_len = max(len(line) for line in lines)
    grid = [line.ljust(max_len) for line in lines]
    height = len(grid)
    width = max_len

    # Identify which columns are completely empty
    # A column is empty if grid[row][col] is ' ' for all rows
    is_empty_col = []
    for c in range(width):
        col_chars = [grid[r][c] for r in range(height)]
        # Check if all spaces
        if all(char == ' ' for char in col_chars):
            is_empty_col.append(True)
        else:
            is_empty_col.append(False)

    # Find ranges of non-empty columns (problems)
    problems_ranges = []
    in_problem = False
    start_col = -1

    for c in range(width):
        is_empty = is_empty_col[c]
        if not is_empty:
            if not in_problem:
                in_problem = True
                start_col = c
        else:
            if in_problem:
                in_problem = False
                problems_ranges.append((start_col, c - 1))
    
    # Handle the case where the last problem goes to the edge of the grid
    if in_problem:
        problems_ranges.append((start_col, width - 1))

    grand_total = 0

    for start_c, end_c in problems_ranges:
        numbers = []
        operator = None

        # Process each row within this column range
        for r in range(height):
            # Extract the slice for this row
            row_slice = grid[r][start_c : end_c + 1]
            stripped = row_slice.strip()

            if not stripped:
                continue
            
            # Check if it's the operator
            if stripped in ('+', '*'):
                operator = stripped
            else:
                try:
                    num = int(stripped)
                    numbers.append(num)
                except ValueError:
                    # Should not happen based on description, but good to debug
                    print(f"Warning: Unexpected content '{stripped}' in problem at cols {start_c}-{end_c}")

        if operator is None:
            print(f"Warning: No operator found for problem at cols {start_c}-{end_c}")
            continue
        
        if not numbers:
             print(f"Warning: No numbers found for problem at cols {start_c}-{end_c}")
             continue

        # Calculate result for this problem
        # "each problem has a group of numbers that need to be either added (+) or multiplied (*) together."
        
        if operator == '+':
            result = sum(numbers)
        elif operator == '*':
            result = 1
            for n in numbers:
                result *= n
        
        grand_total += result

    print(f"Grand Total: {grand_total}")

if __name__ == "__main__":
    solve()
