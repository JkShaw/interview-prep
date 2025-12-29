"""
Islands and Treasure

You are given a m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

Example 2:
Input: [
  [0,-1],
  [2147483647,2147483647]
]
Output: [
  [0,-1],
  [1,2]
]

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
"""
from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([])
        next_level = deque([])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def addRoom(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == -1:
                return
            visited.add((r, c))
            next_level.append((r, c))

        # Add all treasure chest ie 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # Traverse start from treasure and if land found set it as distance from treasure
        # marking it as visited
        distance = 0
        while queue:
            r, c = queue.popleft()
            # Mark grid at r, c at distance far away from treasure
            grid[r][c] = distance
            visited.add((r, c))

            addRoom(r + 1, c)
            addRoom(r - 1, c)
            addRoom(r, c + 1)
            addRoom(r, c - 1)

            if not queue:
                queue = next_level
                next_level = deque([])
                distance += 1


if __name__ == '__main__':
    grid = [
      [2147483647,-1,0,2147483647],
      [2147483647,2147483647,2147483647,-1],
      [2147483647,-1,2147483647,-1],
      [0,-1,2147483647,2147483647]
    ]
    expected = [
      [3,-1,0,1],
      [2,2,1,-1],
      [1,-1,2,-1],
      [0,-1,3,4]
    ]
    Solution().islandsAndTreasure(grid)
    print(grid)

    grid = [
      [0,-1],
      [2147483647,2147483647]
    ]
    expected = [
      [0,-1],
      [1,2]
    ]
    Solution().islandsAndTreasure(grid)
    print(grid)
