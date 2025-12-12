
import sys
import collections

def solve():
    """
    Solves Day 11 Part 1: Counting paths from 'you' to 'out'.
    """
    
    # Read input
    try:
        with open('day11/input.txt', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        # Fallback for running from within day11 directory or for testing
        try:
             with open('input.txt', 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("Error: input.txt not found.")
            return

    adjacency_list = collections.defaultdict(list)

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(':')
        source = parts[0].strip()
        if len(parts) > 1 and parts[1].strip():
            targets = parts[1].strip().split()
            adjacency_list[source].extend(targets)
        else:
             # It seems some nodes might just be 'node: ' which implies no outgoing connections? 
             # Or maybe just 'out' is a sink.
             pass

    # Memoization cache
    memo = {}

    def count_paths(node):
        if node == 'out':
            return 1
        
        if node in memo:
            return memo[node]
        
        total_paths = 0
        if node in adjacency_list:
            for neighbor in adjacency_list[node]:
                total_paths += count_paths(neighbor)
        
        memo[node] = total_paths
        return total_paths

    # Calculate paths starting from 'you'
    result = count_paths('you')
    print(f"Total paths from 'you' to 'out': {result}")

def test_example():
    print("Running Example Test...")
    example_input = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
    """
    
    # Mocking reading from input for the example
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

    memo = {}
    def count_paths(node):
        if node == 'out': return 1
        if node in memo: return memo[node]
        total = 0
        for neighbor in adjacency_list.get(node, []):
            total += count_paths(neighbor)
        memo[node] = total
        return total

    result = count_paths('you')
    print(f"Example Result: {result}")
    assert result == 5, f"Expected 5, got {result}"
    print("Example Test Passed!")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        test_example()
    else:
        solve()
