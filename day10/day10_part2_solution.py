import sys
import re
from fractions import Fraction
import itertools

def parse_line(line):
    # line format: [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    
    # Extract target joltage values
    target_match = re.search(r'\{([\d,]+)\}', line)
    if not target_match:
        return None, None
    target_str = target_match.group(1)
    b = [int(x) for x in target_str.split(',')]
    num_counters = len(b)
    
    # Extract buttons
    button_matches = re.findall(r'\(([\d,]+)\)', line)
    matrix_cols = []
    
    for btn_str in button_matches:
        indices = [int(x) for x in btn_str.split(',')]
        col = [0] * num_counters
        for idx in indices:
            if 0 <= idx < num_counters:
                col[idx] = 1
        matrix_cols.append(col)
        
    # A is a list of columns.
    num_vars = len(matrix_cols)
    A = []
    for r in range(num_counters):
        row = []
        for c in range(num_vars):
            row.append(matrix_cols[c][r])
        A.append(row)
        
    return A, b, matrix_cols

def solve_system(A, b, matrix_cols):
    rows = len(A)
    cols = len(A[0])
    
    # Calculate Upper Bounds for each variable
    # Since A[r][c] is 0 or 1, and x >= 0,
    # if button c increments counter r (A[r][c] == 1), then x[c] <= b[r].
    # We take the tightest bound across all counters it affects.
    upper_bounds = []
    for c in range(cols):
        possible_bounds = [b[r] for r in range(rows) if A[r][c] == 1]
        if not possible_bounds:
            # Button affects no counters, minimizing sum means press it 0 times
            upper_bounds.append(0)
        else:
            upper_bounds.append(min(possible_bounds))
            
    # Gaussian Elimination
    # Use Fraction for exact arithmetic
    matrix = [[Fraction(x) for x in row] + [Fraction(b[r])] for r, row in enumerate(A)]
    
    pivot_row = 0
    pivot_cols = []
    pivot_map = {} # col -> row
    
    for col in range(cols):
        if pivot_row >= rows:
            break
            
        pivot_candidate = -1
        for r in range(pivot_row, rows):
            if matrix[r][col] != 0:
                pivot_candidate = r
                break
        
        if pivot_candidate == -1:
            continue
            
        # Swap
        matrix[pivot_row], matrix[pivot_candidate] = matrix[pivot_candidate], matrix[pivot_row]
        
        # Scale
        pivot_val = matrix[pivot_row][col]
        for c in range(col, cols + 1):
            matrix[pivot_row][c] /= pivot_val
            
        # Eliminate
        for r in range(rows):
            if r != pivot_row and matrix[r][col] != 0:
                factor = matrix[r][col]
                for c in range(col, cols + 1):
                    matrix[r][c] -= factor * matrix[pivot_row][c]
                    
        pivot_cols.append(col)
        pivot_map[col] = pivot_row
        pivot_row += 1
        
    # Consistency check
    for r in range(rows):
        all_zeros = True
        for c in range(cols):
            if matrix[r][c] != 0:
                all_zeros = False
                break
        if all_zeros and matrix[r][cols] != 0:
            return None 

    free_vars = [c for c in range(cols) if c not in pivot_map]
    
    # Determine search ranges for free variables
    # We simply use the calculated upper bounds.
    # Note: RREF dependencies might impose tighter bounds, but this is safe.
    
    search_ranges = []
    for fv in free_vars:
        search_ranges.append(range(upper_bounds[fv] + 1))

    # To optimize, we should prioritize smaller values, but itertools.product 
    # with 'ranges' will iterate in order (0,0,0), (0,0,1)... etc.
    # This is good for finding min sum.
    
    min_sum = float('inf')
    found_any = False
    
    # Heuristic: limit total combinations if it's too large?
    # AoC usually keeps it tractable. But if we have 5 free vars with range 200, that's bad.
    # Machine 30 had 2 free vars.
    
    import itertools
    
    # Precompute RREF dependency structure to move it out of inner loop
    # Equation for pivot c: x[c] = constant - sum(coeff * x[free])
    pivot_dependencies = []
    for c in pivot_cols:
        r = pivot_map[c]
        constant = matrix[r][cols]
        coeffs = []
        for fv in free_vars:
            if matrix[r][fv] != 0:
                coeffs.append((fv, matrix[r][fv]))
        pivot_dependencies.append((c, constant, coeffs))

    for free_vals in itertools.product(*search_ranges):
        # Quick check: Construct candidate solution
        current_x = {}
        for i, val in enumerate(free_vals):
            current_x[free_vars[i]] = Fraction(val)
            
        # Compute pivots
        valid = True
        for c, constant, coeffs in pivot_dependencies:
            val = constant
            for fv, coeff in coeffs:
                val -= coeff * current_x[fv]
            
            # Check integer and bounds
            if val.denominator != 1 or val < 0 or val > upper_bounds[c]:
                valid = False
                break
            current_x[c] = val
        
        if valid:
            current_sum = sum(int(current_x[i]) for i in range(cols))
            if current_sum < min_sum:
                min_sum = current_sum
                found_any = True
                
    if found_any:
        return min_sum
    return None

def solve(input_file='input.txt'):
    try:
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return 0
        
    total_presses = 0
    
    for i, line in enumerate(lines):
        A, b, cols = parse_line(line)
        if A is None:
            continue
            
        min_p = solve_system(A, b, cols)
        
        if min_p is None:
            print(f"Machine {i+1}: No solution found!")
        else:
            total_presses += min_p
            
    return total_presses

if __name__ == "__main__":
    result = solve()
    print(f"Total Presses: {result}")
