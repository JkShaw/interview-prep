"""
N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]


Constraints:
1 <= n <= 9
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        positive_diagonals = set()
        negative_diagonals = set()
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in board]
                res.append(copy)

            for col in range(n):
                if col in cols or (row - col) in negative_diagonals or (row + col) in positive_diagonals:
                    continue

                cols.add(col)
                positive_diagonals.add(row + col)
                negative_diagonals.add(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)
                cols.remove(col)
                positive_diagonals.remove(row + col)
                negative_diagonals.remove(row - col)
                board[row][col] = '.'

        backtrack(0)
        return res