# Day 11: Reactor

## Part 1
The problem asks us to count the number of paths from a starting node `you` to an ending node `out` in a directed acyclic graph (DAG). The graph is defined by a list of devices and their connections.

**Solution Approach**:
The graph is parsed into an adjacency list. Since it's a DAG, we can use Depth-First Search (DFS) with memoization to count the number of distinct paths.

- **Start Node**: `you`
- **End Node**: `out`
- **Algorithm**: `count_paths(node) = sum(count_paths(neighbor) for neighbor in adj[node])`

**Result**: `636`

## Part 2
We are asked to count paths from `svr` (server rack) to `out` that visit *both* `dac` (digital-to-analog converter) and `fft` (fast Fourier transform).

**Solution Approach**:
Since the graph is a DAG, a path cannot visit nodes in an arbitrary order (e.g., `dac` -> `fft` -> `dac` is impossible). We only need to consider the two possible linear orderings of the required nodes:
1. `svr` -> ... -> `dac` -> ... -> `fft` -> ... -> `out`
2. `svr` -> ... -> `fft` -> ... -> `dac` -> ... -> `out`

We can calculate the number of paths for each segment independently and multiply them:
- path1_count = `paths(svr, dac)` * `paths(dac, fft)` * `paths(fft, out)`
- path2_count = `paths(svr, fft)` * `paths(fft, dac)` * `paths(dac, out)`

The total count is the sum of these two values.

**Result**: `509312913844956`
