"""
Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([])
        next_level = deque([])

        def makeRotten(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] in (0, 2):
                return

            grid[r][c] = 2
            next_level.append((r, c))
            visited.add((r, c))

        # find the rotten fruits locations
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))

        # Traverse and mark adjancent fruit as rotten
        minutes = 0
        while queue:

            r, c = queue.popleft()
            visited.add((r, c))

            makeRotten(r, c + 1)
            makeRotten(r, c - 1)
            makeRotten(r + 1, c)
            makeRotten(r - 1, c)

            if not queue and next_level:
                minutes += 1
                queue = next_level
                next_level = deque([])

        # if some fresh is still available, return -1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return minutes