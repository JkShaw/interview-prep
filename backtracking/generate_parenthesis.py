"""
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]


Constraints:
1 <= n <= 8
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(left, right, partial):
            if left == n and right == n:
                result.append("".join(partial))
                return

            if left < n:
                partial.append("(")
                backtrack(left + 1, right, partial)
                partial.pop()

            if right < left:
                partial.append(")")
                backtrack(left, right + 1, partial)
                partial.pop()

        backtrack(0, 0, [])

        return result

"""
Time & Space Complexity
Time complexity:  O(4^n/sqrt(n))
Space complexity: O(n)
"""

