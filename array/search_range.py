"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


Example 1:
---------
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
---------
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
---------
Input: nums = [], target = 0
Output: [-1,-1]


Constraints:
-----------
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first_location = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    first_location = mid
                    right = mid - 1
            return first_location

        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last_location = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    last_location = mid
                    left = mid + 1
            return last_location

        first_location = find_first(nums, target)
        last_location = find_last(nums, target)
        return [first_location, last_location]