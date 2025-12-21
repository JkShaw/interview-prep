"""
Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        nums = matrix

        def find_row():
            l, r = 0, ROWS - 1
            mid = r
            while l <= r:
                mid = l + ((r - l) >> 1)

                if nums[mid][0] > target:
                    r = mid - 1
                elif nums[mid][0] <= target <= nums[mid][-1]:
                    return mid
                else:
                    l = mid + 1
            return mid

        def find_col(row):
            l, r = 0, COLS - 1
            while l <= r:
                mid = l + ((r - l) >> 1)
                if nums[row][mid] == target:
                    return True
                elif nums[row][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return False

        row = find_row()
        return find_col(row)

    def searchMatrixOld(self, matrix: List[List[int]], target: int) -> bool:
        final_row = -1

        for row in range(len(matrix)):
            if matrix[row][0] <= target <= matrix[row][-1]:
                final_row = row
                break

        if final_row == -1:
            return False

        left, right = 0, len(matrix[final_row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[final_row][mid] == target:
                return True
            elif target > matrix[final_row][mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False