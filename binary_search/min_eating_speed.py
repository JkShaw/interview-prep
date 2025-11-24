"""
Koko Eating Bananas
------------

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.


Example 1:
------------
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
------------
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
------------
Input: piles = [30,11,23,4,20], h = 6
Output: 23


Constraints:
------------
1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109

"""
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], hours_to_eat: int) -> int:
        max_pile_size = max(piles)
        left = 1
        right = max_pile_size

        while left < right:
            eating_speed = (left + right) // 2

            # Calculate how long it takes to eat all piles at this speed.
            total_time_to_eat = 0
            for pile_size in piles:
                total_time_to_eat += (pile_size + eating_speed - 1) // eating_speed

            # If it takes too long, the speed is too slow.
            if total_time_to_eat > hours_to_eat:
                left = eating_speed + 1

            # The speed is fast enough, try a slower speed.
            else:
                right = eating_speed

        # 'left' will be the minimum eating speed to finish in time.
        return left

"""
Time Complexity: 
O(n log m) – where 'm' represents the maximum number of bananas in any pile. 
             'n' piles of bananas
Space Complexity:
O(1)          
"""