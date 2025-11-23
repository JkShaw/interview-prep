"""
Product of Array Except Self
------------
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
------------
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
------------
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:
------------
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1] * len(nums)
        right_product = [1] * len(nums)

        curr_val = 1
        for idx in range(1, len(nums)):
            curr_val = curr_val * nums[idx - 1]
            left_product[idx] = curr_val

        curr_val = 1
        for idx in range(len(nums) - 2, -1, -1):
            curr_val = curr_val * nums[idx + 1]
            right_product[idx] = curr_val

        return [left_product[idx] * right_product[idx] for idx in range(len(nums))]
