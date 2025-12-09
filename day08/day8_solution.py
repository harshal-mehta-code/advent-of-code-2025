import sys
import math

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by size
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False

def solve(input_file='day8_input.txt', num_connections=1000):
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

    # Take top K connections
    pairs_to_connect = edges[:num_connections]

    uf = UnionFind(n)
    for _, i, j in pairs_to_connect:
        uf.union(i, j)

    # Calculate component sizes
    # We can use uf.size for roots, but let's be safe and iterate
    # component_sizes = {}
    # for i in range(n):
    #     root = uf.find(i)
    #     component_sizes[root] = component_sizes.get(root, 0) + 1
    
    # Actually, uf.size[root] is maintained correctly
    unique_roots = set()
    for i in range(n):
        unique_roots.add(uf.find(i))
    
    sizes = []
    for root in unique_roots:
        sizes.append(uf.size[root])
    
    sizes.sort(reverse=True)
    
    if len(sizes) < 3:
        # Handling less than 3 circuits edge case, though unlikely for problem
        product = 1
        for s in sizes:
            product *= s
        return product
    
    return sizes[0] * sizes[1] * sizes[2]

if __name__ == "__main__":
    # Default behavior for the actual puzzle
    result = solve()
    print(f"Result: {result}")
