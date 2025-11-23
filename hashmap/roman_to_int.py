"""
Roman to Integer
----------------
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.



Example 1:
----------------
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
----------------
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
----------------
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:
----------------
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


class Solution:
    def romanToInt(self, roman_numeral_string: str) -> int:
        roman_value_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total_integer_value = 0
        previous_symbol_value = 0

        # Iterate through the Roman numeral string from right to left.
        for current_character in reversed(roman_numeral_string):
            current_symbol_value = roman_value_map[current_character]

            # If the current symbol's value is less than the previous one, subtract it.
            if current_symbol_value < previous_symbol_value:
                total_integer_value -= current_symbol_value
            else:
                # Otherwise, add the current symbol's value to the total.
                total_integer_value += current_symbol_value

            # Update the previous symbol's value for the next iteration.
            previous_symbol_value = current_symbol_value

        return total_integer_value

if __name__ == '__main__':
    s = "MCMXCIV"
    print(Solution().romanToInt(s))

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""