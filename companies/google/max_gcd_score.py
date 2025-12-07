"""
Maximize Subarray GCD Score
------------
You are given an array of positive integers nums and an integer k.
You may perform at most k operations. In each operation, you can choose one element in the array and double its value. Each element can be doubled at most once.
The score of a contiguous subarray is defined as the product of its length and the greatest common divisor (GCD) of all its elements.
Your task is to return the maximum score that can be achieved by selecting a contiguous subarray from the modified array.

Note:
The greatest common divisor (GCD) of an array is the largest integer that evenly divides all the array elements.

Example 1:
------------
Input: nums = [2,4], k = 1
Output: 8
Explanation:
Double nums[0] to 4 using one operation. The modified array becomes [4, 4].
The GCD of the subarray [4, 4] is 4, and the length is 2.
Thus, the maximum possible score is 2 × 4 = 8.

Example 2:
------------
Input: nums = [3,5,7], k = 2
Output: 14
Explanation:
Double nums[2] to 14 using one operation. The modified array becomes [3, 5, 14].
The GCD of the subarray [14] is 14, and the length is 1.
Thus, the maximum possible score is 1 × 14 = 14.

Example 3:
------------
Input: nums = [5,5,5], k = 1
Output: 15
Explanation:
The subarray [5, 5, 5] has a GCD of 5, and its length is 3.
Since doubling any element doesn't improve the score, the maximum score is 3 × 5 = 15.


Constraints:
------------
1 <= n == nums.length <= 1500
1 <= nums[i] <= 109
1 <= k <= n
"""
from typing import List


def gcd(first_number, second_number):
    while second_number:
        first_number, second_number = second_number, first_number % second_number
    return first_number


class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # count number of factors of 2 in each number
        factors_of_2 = [0] * n
        for idx, num in enumerate(nums):
            while num % 2 == 0:
                factors_of_2[idx] += 1
                num //= 2

        max_score = 0

        # Try all possible subarrays starting from index left
        for left in range(n):
            current_gcd = 0
            min_factor_count = float('inf') # number having minimum 2**factor, for [3, 5, 7] its 0, for [2, 4] its 1
            elements_with_min_factors = 0

            # Extend the subarray to index right
            for right in range(left, n):
                # Update GCD of current subarray
                current_gcd = gcd(current_gcd, nums[right])

                # Track minimum factor of 2 count and how many elements have it
                if factors_of_2[right] < min_factor_count:
                    min_factor_count = factors_of_2[right]
                    elements_with_min_factors = 1
                elif factors_of_2[right] == min_factor_count:
                    elements_with_min_factors += 1

                # Calculate score: double GCD if elements with minimum factors exceed k
                subarray_length = right - left + 1
                if elements_with_min_factors > k:
                    score = current_gcd * subarray_length
                else:
                    score = current_gcd * 2 * subarray_length

                max_score = max(max_score, score)

        return max_score

if __name__ == '__main__':
    sol = Solution()
    nums = [3, 5, 7]
    k = 2
    result = sol.maxGCDScore(nums, k)
    print(result)


"""
Time Complexity: O(n² * log(max(arr)))
Space Complexity: O(n)
"""