"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution:
    def lengthOfLongestSubstring(self, input_string: str) -> int:
        characters_in_window = dict()
        left_pointer = 0
        max_length = 0

        for right_pointer in range(len(input_string)):
            current_character = input_string[right_pointer]

            # If a character repeats, we must shrink the window from the 
            # left until the duplicate is removed.
            # print(right_pointer, current_character, characters_in_window)
            if current_character in characters_in_window and characters_in_window[current_character] >= left_pointer:
                left_pointer = characters_in_window[current_character] + 1
                characters_in_window[current_character] = right_pointer
            else:
                # Add the new character to the window, effectively expanding it.
                characters_in_window[current_character] = right_pointer

                # After each valid expansion, check if we have a new longest substring.
                current_window_size = right_pointer - left_pointer + 1
                max_length = max(max_length, current_window_size)
        return max_length
