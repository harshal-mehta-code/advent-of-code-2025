import sys

def solve():
    try:
        with open('day6_input.txt', 'r') as f:
            lines = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print("Error: day6_input.txt not found.")
        return

    if not lines:
        print("Error: day6_input.txt is empty.")
        return

    # Pad all lines to the maximum length to treat as a grid
    max_len = max(len(line) for line in lines)
    grid = [line.ljust(max_len) for line in lines]
    height = len(grid)
    width = max_len

    # Identify which columns are completely empty
    is_empty_col = []
    for c in range(width):
        col_chars = [grid[r][c] for r in range(height)]
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
    
    if in_problem:
        problems_ranges.append((start_col, width - 1))

    grand_total = 0

    for start_c, end_c in problems_ranges:
        numbers = []
        operator = None

        # Extract operator from the last row within this block range
        # We scan the last row in this column range for the operator
        last_row_slice = grid[height - 1][start_c : end_c + 1]
        stripped_slice = last_row_slice.strip()
        
        # In Part 1 we found the operator by checking every row. 
        # In Part 2, the description says "the symbol at the bottom of the problem is still the operator".
        # We can just look for + or * in the stripped last row slice.
        if '+' in stripped_slice:
            operator = '+'
        elif '*' in stripped_slice:
            operator = '*'
        
        # Now extract numbers from columns
        # "Cephalopod math is written right-to-left in columns."
        # "Each number is given in its own column, with the most significant digit at the top"
        # We iterate columns from right to left (end_c down to start_c).
        
        for c in range(end_c, start_c - 1, -1):
            # Build string from rows 0 to height-2 (excluding the operator row)
            col_str = ""
            for r in range(height - 1):
                col_str += grid[r][c]
            
            stripped_num = col_str.strip()
            if stripped_num:
                try:
                    num = int(stripped_num)
                    numbers.append(num)
                except ValueError:
                    # Might encounter spaces inside the column if not careful, 
                    # but strip() should handle surrounding spaces.
                    # If there are internal spaces, that might be an issue, but standard int() handles whitespace? 
                    # Actually int(' 1 2 ') is invalid. 
                    # Let's assume digits are contiguous or we should remove ALL spaces?
                    # "Each number is given in its own column... most significant digit at the top"
                    # It likely means the digits are potentially spaced out vertically?
                    # Re-reading: "The left/right alignment of numbers within each problem can be ignored." (Part 1)
                    # Part 2 says "Each number is given in its own column".
                    # Let's try removing all spaces just in case, or just strip. 
                    # Given the input provided earlier, digits seem contiguous vertically if they form a number.
                    # Let's stick to strip() first.
                    pass 

        if operator is None:
            print(f"Warning: No operator found for problem at cols {start_c}-{end_c}")
            continue
        
        if not numbers:
             print(f"Warning: No numbers found for problem at cols {start_c}-{end_c}")
             continue

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
