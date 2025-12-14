"""
Target Sum

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.


Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1


Constraints:
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

"""
from collections import defaultdict
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(idx, curr_sum):
            if idx == len(nums):
                return 1 if curr_sum == target else 0

            return (
                backtrack(idx + 1, curr_sum + nums[idx]) +
                backtrack(idx + 1, curr_sum - nums[idx])
            )

        ways = backtrack(0, 0)
        return ways

    def findTargetSumWaysDP1(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1

        for i in range(len(nums)):
            for curr_sum, count in dp[i].items():
                dp[i + 1][curr_sum + nums[i]] += count
                dp[i + 1][curr_sum - nums[i]] += count

        return dp[len(nums)][target]

    def findTargetSumWaysDP2(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            next_dp = defaultdict(int)

            for curr_sum, count in dp.items():
                next_dp[curr_sum + nums[i]] += count
                next_dp[curr_sum - nums[i]] += count

            dp = next_dp

        return dp[target]
if __name__ == '__main__':
    s = Solution()
    print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
