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
    max_area = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            width = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height
            
            if area > max_area:
                max_area = area

    return max_area

if __name__ == "__main__":
    result = solve()
    print(f"Max Area: {result}")
