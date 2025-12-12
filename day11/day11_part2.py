
import sys
import collections

def solve():
    """
    Solves Day 11 Part 2: Counting paths from 'svr' to 'out' passing through both 'dac' and 'fft'.
    """
    
    # Read input
    try:
        with open('day11/input.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        # Fallback
        try:
             with open('input.txt', 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("Error: input.txt not found.")
            return

    adjacency_list = collections.defaultdict(list)

    for line in lines:
        line = line.strip()
        if not line: continue
        parts = line.split(':')
        source = parts[0].strip()
        if len(parts) > 1 and parts[1].strip():
            targets = parts[1].strip().split()
            adjacency_list[source].extend(targets)

    # Generalized count_paths with memoization for a specific target
    def count_paths(start_node, end_node):
        memo = {}

        def _dfs(node):
            if node == end_node:
                return 1
            if node in memo:
                return memo[node]
            
            total = 0
            if node in adjacency_list:
                for neighbor in adjacency_list[node]:
                    total += _dfs(neighbor)
            
            memo[node] = total
            return total

        return _dfs(start_node)

    # Verify if counts are 0, it means that direction is impossible in DAG
    # Path 1: svr -> dac -> fft -> out
    p1_segment1 = count_paths('svr', 'dac')
    p1_segment2 = count_paths('dac', 'fft')
    p1_segment3 = count_paths('fft', 'out')
    path1_total = p1_segment1 * p1_segment2 * p1_segment3

    # Path 2: svr -> fft -> dac -> out
    p2_segment1 = count_paths('svr', 'fft')
    p2_segment2 = count_paths('fft', 'dac')
    p2_segment3 = count_paths('dac', 'out')
    path2_total = p2_segment1 * p2_segment2 * p2_segment3

    total_paths = path1_total + path2_total
    
    print(f"Path 1 (svr->dac->fft->out): {p1_segment1} * {p1_segment2} * {p1_segment3} = {path1_total}")
    print(f"Path 2 (svr->fft->dac->out): {p2_segment1} * {p2_segment2} * {p2_segment3} = {path2_total}")
    print(f"Total paths visiting both dac and fft: {total_paths}")

def test_example():
    print("Running Part 2 Example Test...")
    example_input = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
    """
    
    lines = example_input.strip().split('\n')
    adjacency_list = collections.defaultdict(list)
    for line in lines:
        line = line.strip()
        if not line: continue
        parts = line.split(':')
        source = parts[0].strip()
        if len(parts) > 1 and parts[1].strip():
            targets = parts[1].strip().split()
            adjacency_list[source].extend(targets)

    def count_paths(start_node, end_node):
        memo = {}
        def _dfs(node):
            if node == end_node: return 1
            if node in memo: return memo[node]
            total = 0
            for neighbor in adjacency_list.get(node, []):
                total += _dfs(neighbor)
            memo[node] = total
            return total
        return _dfs(start_node)

    # Path 1: svr -> dac -> fft -> out
    p1 = count_paths('svr', 'dac') * count_paths('dac', 'fft') * count_paths('fft', 'out')
    # Path 2: svr -> fft -> dac -> out
    p2 = count_paths('svr', 'fft') * count_paths('fft', 'dac') * count_paths('dac', 'out')
    
    result = p1 + p2
    print(f"Example Result: {result}")
    assert result == 2, f"Expected 2, got {result}"
    print("Example Test Passed!")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        test_example()
    else:
        solve()
