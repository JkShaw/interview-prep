"""
Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def explore_island(row, col):
            # Check boundaries and if the cell is land
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
                return

            # Mark the current cell as visited by turning it into water
            grid[row][col] = '0'

            # Recursively explore adjacent land cells
            explore_island(row + 1, col)
            explore_island(row - 1, col)
            explore_island(row, col + 1)
            explore_island(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    # Found a new island
                    island_count += 1

                    # Explore and mark the entire island
                    explore_island(row, col)

        return island_count


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = Solution().numIslands(grid)
    print(result)
