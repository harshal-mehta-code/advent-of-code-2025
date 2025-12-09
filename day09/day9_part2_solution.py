import sys

def solve(input_file='day9_input.txt'):
    try:
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return 0

    points = []
    for line in lines:
        try:
            x, y = map(int, line.split(','))
            points.append((x, y))
        except ValueError:
            continue
    
    n = len(points)
    if n < 4:
        return 0 # Need at least 4 points for a loop

    # Build Polygon Edges
    poly_edges = []
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        poly_edges.append((p1, p2))

    # Generate candidates: (area, x1, x2, y1, y2)
    candidates = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            # Form rectangle boundaries
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            
            width = max_x - min_x + 1
            height = max_y - min_y + 1
            area = width * height
            
            # Store necessary info
            candidates.append((area, min_x, max_x, min_y, max_y))
    
    # Sort descending by area
    candidates.sort(key=lambda x: x[0], reverse=True)
    
    # Validation loop
    for area, r_min_x, r_max_x, r_min_y, r_max_y in candidates:
        
        # 1. Center Point Check (Ray Casting)
        center_x = (r_min_x + r_max_x) / 2.0
        center_y = (r_min_y + r_max_y) / 2.0
        
        inside = False
        for i in range(n):
            p1x, p1y = points[i]
            p2x, p2y = points[(i + 1) % n]
            
            # Vertical edge check for ray casting (ray to +X)
            # Edge must straddle the y coordinate of the point
            if (p1y > center_y) != (p2y > center_y):
                # Calculate x-coordinate of intersection
                intersect_x = (p2x - p1x) * (center_y - p1y) / (p2y - p1y) + p1x
                if center_x < intersect_x:
                    inside = not inside
        
        if not inside:
            continue

        # If center is inside, we verify no invalid intersections
        valid = True
        
        # 2. Check if any polygon vertex is strictly inside rectangle
        # Strictly inside: min_x < vx < max_x AND min_y < vy < max_y
        for px, py in points:
            if r_min_x < px < r_max_x and r_min_y < py < r_max_y:
                valid = False
                break
        if not valid:
            continue
            
        # 3. Check if any polygon edge strictly intersects rectangle interior
        # Strictly intersects means passing through the rectangle, not just touching boundary
        for (p1x, p1y), (p2x, p2y) in poly_edges:
            # Determine if horizontal or vertical
            if p1x == p2x: # Vertical Edge
                vx = p1x
                vy_start = min(p1y, p2y)
                vy_end = max(p1y, p2y)
                
                # Check intersection with rectangle interior
                # Must be strictly between rect x bounds
                # And y intervals must overlapping strictly
                if r_min_x < vx < r_max_x:
                     if max(r_min_y, vy_start) < min(r_max_y, vy_end):
                         valid = False
                         break
                         
            else: # Horizontal Edge
                hy = p1y
                hx_start = min(p1x, p2x)
                hx_end = max(p1x, p2x)
                
                # Check intersection with rectangle interior
                if r_min_y < hy < r_max_y:
                    if max(r_min_x, hx_start) < min(r_max_x, hx_end):
                        valid = False
                        break
        
        if valid:
            return area

    return 0

if __name__ == "__main__":
    result = solve()
    print(f"Max Area: {result}")
