"""
Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.



Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
from collections import deque
from typing import List



class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        dq = deque()
        l = 0
        result = []
        len_arr = len(arr)

        for i in range(k):
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            dq.append(i)


        for i in range(k, len_arr):
            result.append(arr[dq[0]])

            while dq and (dq[0] <= (i - k)):
                dq.popleft()

            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

        result.append(arr[dq[0]])
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
