"""
Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output: true

Example 2:
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output: false

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Constraints:
1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        queue = deque([(0, -1)]) # (current node, parent node)
        visited.add(0)

        while queue:
            node, parent = queue.popleft()
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                queue.append((nei, node))

        return len(visited) == n

if __name__ == '__main__':
    solution = Solution()
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    print(solution.validTree(5, edges))

    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(solution.validTree(5, edges))

    # assert solution.validTree([[0, 1], [0, 2], [0, 3], [1, 4]]) == -1