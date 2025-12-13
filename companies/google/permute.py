"""
Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]


Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]

        for idx in range(len(nums)):
            item = nums.pop(0)

            # get permutations of rest of the items in array
            perms = self.permute(nums)

            # add item to the perms
            for perm in perms:
                perm.append(item)

            result.extend(perms)

            # Add the popped item again
            nums.append(item)

        return result