
def parse_shape(lines):
    # Determine width and height
    if not lines:
        return 0
    return sum(line.count('#') for line in lines)

def solve():
    with open('input.txt', 'r') as f:
        content = f.read().splitlines()

    shapes = []
    current_shape = []
    reading_shapes = True
    
    regions = []

    i = 0
    # First, find where regions start
    # Regions start with "WxL:"
    region_start_index = 0
    for idx, line in enumerate(content):
        if 'x' in line.split(':')[0] and line[0].isdigit():
            region_start_index = idx
            break
            
    # Parse shapes (everything before region_start_index)
    # But shape 5 ends before line 31.
    
    current_shape_lines = []
    for idx in range(region_start_index):
        line = content[idx].strip()
        if not line:
            continue
        if line[0].isdigit() and line.endswith(':'):
            if current_shape_lines:
                shapes.append(parse_shape(current_shape_lines))
                current_shape_lines = []
        else:
            current_shape_lines.append(line)
            
    if current_shape_lines:
        shapes.append(parse_shape(current_shape_lines))
        
    # Check if we have 6 shapes
    # If the file format separates sections clearly
    
    # Parse regions
    for idx in range(region_start_index, len(content)):
        line = content[idx].strip()
        if not line:
            continue
        parts = line.split(':')
        dims = parts[0].split('x')
        w, h = int(dims[0]), int(dims[1])
        counts = list(map(int, parts[1].strip().split()))
        regions.append({'w': w, 'h': h, 'counts': counts})
    
    # Analyze
    possible_by_area = 0
    impossible_by_area = 0
    slacks = []

    print(f"Found {len(shapes)} shapes with areas: {shapes}")
    
    for r in regions:
        region_area = r['w'] * r['h']
        needed_area = sum(c * shapes[idx] for idx, c in enumerate(r['counts']))
        
        if needed_area <= region_area:
            possible_by_area += 1
            slacks.append(region_area - needed_area)
        else:
            impossible_by_area += 1

    print(f"Total Regions: {len(regions)}")
    print(f"Impossible by Area: {impossible_by_area}")
    print(f"Possible by Area: {possible_by_area}")
    
    widths = [r['w'] for r in regions]
    heights = [r['h'] for r in regions]
    print(f"Min Width: {min(widths)}, Max Width: {max(widths)}")
    print(f"Min Height: {min(heights)}, Max Height: {max(heights)}")

    if slacks:
        print(f"Max Slack: {max(slacks)}")
        print(f"Min Slack: {min(slacks)}")
        print(f"Avg Slack: {sum(slacks)/len(slacks)}")
    
    # Check if exact match is required?
    exact_matches = slacks.count(0)
    print(f"Exact Area Matches: {exact_matches}")

solve()
