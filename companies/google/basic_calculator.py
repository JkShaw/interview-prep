"""
Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().


Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:
1 <= s.length <= 3 * 10**5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""


class Solution:
    def calculate(self, expression: str) -> int:
        current_number = 0
        operation_stack = []
        result = 0
        sign = 1

        for character in expression:
            if character.isdigit():
                current_number = current_number * 10 + int(character)
            elif character == '+':
                result += sign * current_number
                current_number = 0
                sign = 1
            elif character == '-':
                result += sign * current_number
                current_number = 0
                sign = -1
            elif character == '(':  # Store result and sign for later
                operation_stack.append(result)
                operation_stack.append(sign)
                result = 0
                sign = 1
            elif character == ')':  # Finish current calculation
                result += sign * current_number
                current_number = 0
                result *= operation_stack.pop()
                result += operation_stack.pop()
            else:
                pass

        if current_number != 0:  # Add the last number
            result += sign * current_number

        return result

