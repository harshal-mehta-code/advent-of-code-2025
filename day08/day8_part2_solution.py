import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.num_components = n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            self.num_components -= 1
            return True
        return False

def solve(input_file='day8_input.txt'):
    try:
        with open(input_file, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return 0

    points = []
    for line in lines:
        parts = line.split(',')
        if len(parts) == 3:
            points.append(tuple(map(int, parts)))
    
    n = len(points)
    if n == 0:
        return 0
    if n == 1:
        return 0 

    # Calculate all pairwise squared distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            edges.append((dist_sq, i, j))
    
    # Sort by distance
    edges.sort(key=lambda x: x[0])

    uf = UnionFind(n)
    
    for _, i, j in edges:
        if uf.union(i, j):
            # If this connection reduced components to 1, it's the final one needed
            if uf.num_components == 1:
                p1 = points[i]
                p2 = points[j]
                return p1[0] * p2[0]

    return 0

if __name__ == "__main__":
    result = solve()
    print(f"Result: {result}")
