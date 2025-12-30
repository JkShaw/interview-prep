"""
Number of Connected Components in an Undirected Graph

There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.
Return the total number of connected components in that graph.

Example 1:
Input:
n=3
edges=[[0,1], [0,2]]
Output:1

Example 2:
Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]
Output:2

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""
from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        visited = set()
        num_components = 0

        # Build graph
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(node):
            visited.add(node)

            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        # traverse node from 0 to (n-1) and count componenets
        for node in range(n):
            if node not in visited:
                num_components += 1
                dfs(node)

        return num_components

if __name__ == "__main__":
    s = Solution()
    n = 3
    edges = [[0, 1], [0, 2]]
    expected = 1
    print(s.countComponents(n, edges))

    n = 6
    edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
    expected = 2
    print(s.countComponents(n, edges))