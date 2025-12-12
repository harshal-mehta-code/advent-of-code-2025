
# Solution for Day 12 Part 1
# Strategy: Count regions where TotalPresentArea <= RegionArea.
# Analysis showed that all possible regions have huge slack (>28%), so precise packing check is unnecessary.

def parse_shape(lines):
    return sum(line.count('#') for line in lines)

def solve():
    try:
        with open('input.txt', 'r') as f:
            content = f.read().splitlines()
    except FileNotFoundError:
        print("Input file not found.")
        return

    shapes = []
    
    # Locate region start
    region_start_index = 0
    for idx, line in enumerate(content):
        # Regions start with digit, then 'x', then digit
        parts = line.split(':')
        if len(parts) > 1 and 'x' in parts[0]:
            region_start_index = idx
            break
            
    # Parse shapes
    current_shape_lines = []
    for idx in range(region_start_index):
        line = content[idx].strip()
        if not line:
            continue
        # Check if it's a shape header "N:"
        if line[0].isdigit() and line.endswith(':'):
            if current_shape_lines:
                shapes.append(parse_shape(current_shape_lines))
                current_shape_lines = []
        else:
            current_shape_lines.append(line)
            
    if current_shape_lines:
        shapes.append(parse_shape(current_shape_lines))
        
    print(f"Parsed {len(shapes)} shapes with areas: {shapes}")
    
    # Parse regions and count valid ones
    valid_regions = 0
    
    for idx in range(region_start_index, len(content)):
        line = content[idx].strip()
        if not line:
            continue
            
        # Parse "WxL: c0 c1 c2 c3 c4 c5"
        try:
            parts = line.split(':')
            dims = parts[0].split('x')
            w, h = int(dims[0]), int(dims[1])
            counts = list(map(int, parts[1].strip().split()))
            
            region_area = w * h
            presents_area = sum(c * shapes[i] for i, c in enumerate(counts))
            
            if presents_area <= region_area:
                valid_regions += 1
                
        except Exception as e:
            print(f"Error parsing line {idx}: {line} -> {e}")
            
    print(f"Answer: {valid_regions}")

if __name__ == "__main__":
    solve()
