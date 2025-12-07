"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_price_so_far = float('inf')

        best_profit_so_far = 0

        for current_price in prices:
            # Calculate profit if we sell today, using the cheapest buy price found before today.
            potential_profit = current_price - cheapest_price_so_far

            # If today's potential profit is the best we've seen, we update our maximum profit.
            if potential_profit > best_profit_so_far:
                best_profit_so_far = potential_profit

            # Check if the current day's price is a new low, to find better future buy opportunities.
            if current_price < cheapest_price_so_far:
                cheapest_price_so_far = current_price

        return best_profit_so_far
