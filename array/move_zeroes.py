"""
Move Zeroes
-----------
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:
-----------
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
-----------
Input: nums = [0]
Output: [0]


Constraints:
-----------
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr_idx = len(nums) - 1
        non_zero_idx = len(nums) - 1

        # Insert all the non-zers in the last
        while curr_idx >= 0:
            if nums[curr_idx] != 0:
                nums[non_zero_idx] = nums[curr_idx]
                non_zero_idx -= 1
            curr_idx -= 1

        # insert into first
        curr_idx = 0
        for idx in range(non_zero_idx + 1, len(nums)):
            nums[curr_idx] = nums[idx]
            curr_idx += 1

        while curr_idx < len(nums):
            nums[curr_idx] = 0
            curr_idx += 1


