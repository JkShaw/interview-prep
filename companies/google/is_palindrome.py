"""
Palindrome Number
------------

Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:
------------
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
------------
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
------------
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-2**31 <= x <= 2**31 - 1
"""


class Solution:
    def isPalindrome(self, num: int) -> bool:
        # If num < 0 then its not a palindrome
        if num < 0:
            return False

        current = num
        reverse = 0

        while current:
            remainder = current % 10
            reverse = reverse * 10 + remainder
            current = current // 10

        return num == reverse


if __name__ == '__main__':
    sol = Solution()
    x1 = 1232
    result = sol.isPalindrome(x1)
    print(result)
