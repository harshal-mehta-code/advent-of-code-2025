import sys
import re

def parse_line(line):
    # line format: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    
    # Extract target pattern
    target_match = re.search(r'\[([.#]+)\]', line)
    if not target_match:
        return None, None
    target_str = target_match.group(1)
    # Convert to vector: . -> 0, # -> 1
    # Note: Light 0 is the first character
    b = [1 if c == '#' else 0 for c in target_str]
    num_lights = len(b)
    
    # Extract buttons
    # Buttons are in (x,y,z) format
    button_matches = re.findall(r'\(([\d,]+)\)', line)
    matrix_cols = []
    
    for btn_str in button_matches:
        # Each button affects specific lights
        indices = [int(x) for x in btn_str.split(',')]
        col = [0] * num_lights
        for idx in indices:
            if 0 <= idx < num_lights:
                col[idx] = 1
        matrix_cols.append(col)
        
    # A is a list of columns. Transpose to get rows if needed, but for now we work with columns.
    # Actually, for Ax=b, A's columns are the button effects.
    # Let's construct A as a list of lists where A[row][col] is the effect of button 'col' on light 'row'.
    num_vars = len(matrix_cols)
    A = []
    for r in range(num_lights):
        row = []
        for c in range(num_vars):
            row.append(matrix_cols[c][r])
        A.append(row)
        
    return A, b

def solve_system(A, b):
    # Solve Ax = b over GF(2)
    rows = len(A)
    cols = len(A[0])
    
    # Augmented matrix [A | b]
    matrix = [A[row][:] + [b[row]] for row in range(rows)]
    
    # Gaussian elimination
    pivot_row = 0
    pivot_cols = [] # List of columns that have pivots
    pivot_map = {}  # Map from col -> row where pivot exists
    
    for col in range(cols):
        if pivot_row >= rows:
            break
            
        # Find a row with a 1 in this column, starting from pivot_row
        pivot_candidate = -1
        for r in range(pivot_row, rows):
            if matrix[r][col] == 1:
                pivot_candidate = r
                break
        
        if pivot_candidate == -1:
            continue # No pivot in this column, it's a free variable
            
        # Swap rows
        matrix[pivot_row], matrix[pivot_candidate] = matrix[pivot_candidate], matrix[pivot_row]
        
        # Eliminate other rows
        for r in range(rows):
            if r != pivot_row and matrix[r][col] == 1:
                # Row XOR
                for c in range(col, cols + 1):
                    matrix[r][c] ^= matrix[pivot_row][c]
        
        pivot_cols.append(col)
        pivot_map[col] = pivot_row
        pivot_row += 1

    # Check for consistency
    # If any row is all zeros except the last column (b), implies 0 = 1 -> No solution
    for r in range(rows):
        all_zeros = True
        for c in range(cols):
            if matrix[r][c] != 0:
                all_zeros = False
                break
        if all_zeros and matrix[r][cols] == 1:
            return None # No solution

    # Identify free variables
    free_vars = []
    for c in range(cols):
        if c not in pivot_map:
            free_vars.append(c)
            
    # Function to extract solution given values for free variables
    def get_solution(free_vals):
        x = [0] * cols
        # Set free variables
        for i, fv_idx in enumerate(free_vars):
            x[fv_idx] = free_vals[i]
            
        # Solve for pivot variables (back substitution effectively done by RREF)
        # In RREF, pivot row for col c has 1 at c and 0 at other pivot cols.
        # So val(c) + sum(val(free_vars) * coeff) = val(b_row)
        # val(c) = val(b_row) - sum(...)  (modulo 2: + and - are same)
        
        # Iterate backwards to fill dependencies correctly? 
        # Actually with full elimination (both above and below pivot), 
        # the equation for pivot col c at row r is:
        # x[c] + sum(x[free] * matrix[r][free]) = matrix[r][end]
        # x[c] = matrix[r][end] ^ sum(x[free] * matrix[r][free])
        
        for c in pivot_cols:
            r = pivot_map[c]
            val = matrix[r][cols]
            for fv in free_vars:
                if matrix[r][fv] == 1:
                    val ^= x[fv]
            x[c] = val
        return x

    # We need to find the solution with minimum weight (sum of x)
    # If there are free variables, we iterate all 2^{num_free} combinations.
    # Assuming standard AOC constraints, num_free shouldn't be huge.
    
    min_presses = float('inf')
    
    import itertools
    for free_vals in itertools.product([0, 1], repeat=len(free_vars)):
        x = get_solution(free_vals)
        weight = sum(x)
        if weight < min_presses:
            min_presses = weight
            
    return min_presses

def solve(input_file='input.txt'):
    try:
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return 0
        
    total_presses = 0
    
    for i, line in enumerate(lines):
        A, b = parse_line(line)
        if A is None:
            continue
            
        min_p = solve_system(A, b)
        
        if min_p is None:
            print(f"Machine {i+1}: No solution found!")
        else:
            # print(f"Machine {i+1}: {min_p} presses")
            total_presses += min_p
            
    return total_presses

if __name__ == "__main__":
    result = solve()
    print(f"Total Presses: {result}")
