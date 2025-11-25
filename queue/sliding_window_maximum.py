"""
Sliding Window Maximum
-----------
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1:
-----------
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
-----------
Input: nums = [1], k = 1
Output: [1]


Constraints:
-----------
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        res = []

        # create deque to store max values
        dq = deque()

        # Process first k (or first window) elements of array
        for i in range(0, k):
            # For every element, the previous smaller elements
            # are useless so remove them from dq
            while dq and arr[i] > arr[dq[-1]]:
                # Remove from rear
                dq.pop()

            # Add new element at rear of queue
            dq.append(i)

        # Process rest of the elements, i.e., from arr[k] to arr[n-1]
        for i in range(k, len(arr)):
            # The element at the front of the queue is the largest
            # element of previous window, so store it
            res.append(arr[dq[0]])

            # Remove the elements which are out of this window
            while dq and dq[0] <= i - k:
                # Remove from front of queue
                dq.popleft()

            # Remove all elements smaller than the currently being
            # added element (remove useless elements)
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()

            # Add current element at the rear of dq
            dq.append(i)

        # store the maximum element of last window
        res.append(arr[dq[0]])
        return res


if __name__ == '__main__':
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    output = [3, 3, 5, 5, 6, 7]

    res = Solution().maxSlidingWindow(arr, k)
    print(output, res)