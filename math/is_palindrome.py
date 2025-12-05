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
    def isPalindrome(self, input_number: int) -> bool:
        # Negative numbers cannot be palindromes. Also, if a number ends in 0 (and is not 0 itself),
        # its reverse would start with 0, so it can't be a palindrome.
        if input_number < 0 or (input_number % 10 == 0 and input_number != 0):
            return False

        reverted_second_half = 0
        remaining_first_half = input_number

        # We only need to reverse half the number to avoid potential integer overflow and improve performance.
        while remaining_first_half > reverted_second_half:
            last_digit = remaining_first_half % 10
            reverted_second_half = reverted_second_half * 10 + last_digit
            remaining_first_half //= 10

        # For numbers with an odd number of digits, the middle digit will be the last digit of the
        # reverted half. We can remove it by integer division as it doesn't affect the palindrome check.
        return remaining_first_half == reverted_second_half or remaining_first_half == reverted_second_half // 10

"""
Time Complexity: O(log10(n)
Space Complexity: O(1)
"""