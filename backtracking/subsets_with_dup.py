"""
Subsets II

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]


Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def helper(idx, partial):
            if idx == len(nums):
                result.append(list(partial))
                return

            partial.append(nums[idx])
            helper(idx + 1, partial)
            partial.pop()

            while ((idx + 1) < len(nums)) and (nums[idx + 1] == nums[idx]):
                idx += 1

            helper(idx + 1, partial)

        helper(0, [])
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    nums = [1, 2, 2]
    sol = Solution()
    result = sol.subsetsWithDup(nums)
    print(result)
