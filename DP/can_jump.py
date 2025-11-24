"""
Jump Game
------------
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.


Example 1:
------------
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
------------
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:
------------
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        destination_idx = len(nums) - 1

        for idx in range(len(nums) - 2, -1, -1):
            # Check if we can reach the current destination from this position
            if idx + nums[idx] >= destination_idx:
                # If we can, update the destination to the current position.
                destination_idx = idx

        # If first position is the destination, we can reach the end.
        return destination_idx == 0


"""
Time Complexity: O(n)
Space Complexity: O(1)          
"""