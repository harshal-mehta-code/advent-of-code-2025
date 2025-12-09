import sys
sys.setrecursionlimit(10000)

def solve(input_file='day7_input.txt'):
    try:
        with open(input_file, 'r') as f:
            lines = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return 0

    if not lines:
        print(f"Error: {input_file} is empty.")
        return 0

    max_len = max(len(line) for line in lines)
    grid = [line.ljust(max_len, '.') for line in lines]
    height = len(grid)
    width = max_len

    start_pos = None
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 'S':
                start_pos = (r, c)
                break
        if start_pos:
            break
    
    if not start_pos:
        print("Error: Start position 'S' not found.")
        return 0

    memo = {}

    def count_timelines(r, c):
        # r, c is the position of the beam HEAD.
        # It is about to move downwards.
        if (r, c) in memo:
            return memo[(r, c)]
        
        count = 0
        curr_r = r
        
        # Determine if this beam path hits a splitter or exits
        hit_splitter = False
        splitter_pos = None

        while curr_r < height:
            if c < 0 or c >= width:
                # Out of bounds horizontally? effectively just stops or treated as empty/done?
                # "Tachyon beams pass freely through empty space"
                # If it goes off side, it probably just continues down or disappears?
                # Assume standard grid bounds. If valid index, check it.
                pass
            
            # Check cell
            if 0 <= c < width:
                cell = grid[curr_r][c]
                if cell == '^':
                    hit_splitter = True
                    splitter_pos = (curr_r, c)
                    break
            
            curr_r += 1
        
        if hit_splitter:
            sr, sc = splitter_pos
            # Beam splits into left and right
            left_count = count_timelines(sr, sc - 1)
            right_count = count_timelines(sr, sc + 1)
            count = left_count + right_count
        else:
            # Beam reached bottom without hitting a splitter
            # "until all of the tachyon beams reach a splitter or exit the manifold"
            # Exiting the manifold means valid completion of a timeline journey.
            count = 1
        
        memo[(r, c)] = count
        return count

    # Start just below S
    result = count_timelines(start_pos[0] + 1, start_pos[1])
    return result

if __name__ == "__main__":
    result = solve()
    print(f"Timeline Count: {result}")
