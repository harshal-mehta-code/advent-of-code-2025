import sys
from collections import deque

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

    # Padded grid
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

    # Queue of beam heads: (row, col)
    # The beam head is where the beam *starts* its downward journey segment
    queue = deque()
    
    # Initial beam starts below S
    initial_beam_start = (start_pos[0] + 1, start_pos[1])
    if initial_beam_start[0] < height:
        queue.append(initial_beam_start)

    visited_starts = set()
    visited_splitters = set()

    while queue:
        r, c = queue.popleft()

        if (r, c) in visited_starts:
            continue
        visited_starts.add((r, c))

        # Trace beam downwards
        curr_r = r
        while curr_r < height:
            if c < 0 or c >= width:
                break # Out of bounds horizontally (shouldn't happen with padding but good safety)
            
            cell = grid[curr_r][c]
            
            if cell == '^':
                # Splitter hit!
                if (curr_r, c) not in visited_splitters:
                    visited_splitters.add((curr_r, c))
                
                # Create new beams: left and right from the splitter
                # Left new beam starts at curr_r, c-1? No, "a new tachyon beam continues from the immediate left and from the immediate right of the splitter."
                # The beam moves *downward*. So the new beams start at (curr_r, c-1) and (curr_r, c+1) and then proceed DOWN?
                # Description: "At that point, the original beam stops, and two new beams are emitted from the splitter:"
                # Example visual:
                # ......|^|......
                # ......|.|......
                # So the new beams are effectively starting at (curr_r, c-1) and (curr_r, c+1) but they move DOWN IMMEDIATELY?
                # No, they seem to simply exist at left/right and then move down.
                # Actually, standard interpretation: reset "downward" movement from those new positions.
                # So next step for left beam is (curr_r + 1, c - 1) ??
                # Let's look closely at the diagram.
                # 141: ......|^|......
                # 160: ......|.|......
                # The beams are at (141, left_of_caret) and (141, right_of_caret).
                # Then in next step they are at (142, left) and (142, right).
                # So yes, they start at same row, adjacent cols, then proceed down.
                # EXCEPT: if there is something else there? 
                # "Tachyon beams pass freely through empty space (.)"
                # "if a tachyon beam encounters a splitter (^), the beam is stopped"
                
                # So we queue up (curr_r, c - 1) and (curr_r, c + 1) as new HEADS of beams that will travel down.
                # But wait, if we queue (curr_r, c-1), the loop will start at `curr_r`.
                # We need to make sure we don't process the row `curr_r` again if it's meant to be "one step down".
                # Look at 141 -> 160.
                # The beam exists at 141. Then moves to 160.
                # So it IS travelling down. 
                # The "start" of the new beam is indeed (curr_r, c-1). And it will flow down from there.
                
                queue.append((curr_r, c - 1))
                queue.append((curr_r, c + 1))
                break # Original beam stops
            
            # S is just a visual start, treat as empty if encountered (though usually at top)
            # . is empty space
            
            curr_r += 1

    return len(visited_splitters)

if __name__ == "__main__":
    result = solve()
    print(f"Splitter Count: {result}")
