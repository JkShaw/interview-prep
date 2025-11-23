"""
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
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten_oranges_queue = deque()
        fresh_oranges_count = 0
        time_elapsed = 0

        # fetch rotten oranges and count fresh ones.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten_oranges_queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_oranges_count += 1

        # adjacent cells: up, down, left, right.
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Process rotten oranges layer by layer (BFS).
        while rotten_oranges_queue:
            current_row, current_column, current_time = rotten_oranges_queue.popleft()
            time_elapsed = max(time_elapsed, current_time)

            # Explore adjacent cells.
            for dr, dc in directions:
                neighbor_row = current_row + dr
                neighbor_col = current_column + dc

                # Check if the neighbor is within grid bounds and is a fresh orange.
                if 0 <= neighbor_row < rows and 0 <= neighbor_row < cols and grid[neighbor_row][neighbor_col] == 1:
                    grid[neighbor_row][neighbor_col] = 2 # marking it as rotten
                    fresh_oranges_count -= 1
                    rotten_oranges_queue.append((neighbor_row, neighbor_row, current_time + 1))

        # If there are still fresh oranges, they are unreachable.
        if fresh_oranges_count > 0:
            return -1

        return time_elapsed

"""
Time Complexity:
O(M * N) – Where M and N is number of rows and columns in the grid representing the oranges

Space Complexity:
O(rows*cols) 
"""