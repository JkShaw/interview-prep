"""
Reorganize String
------------
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Example 1:
------------
Input: s = "aab"
Output: "aba"

Example 2:
------------
Input: s = "aaab"
Output: ""

Constraints:
------------
1 <= s.length <= 500
s consists of lowercase English letters.
"""
class Solution:
    def reorganizeString(self, input_string: str) -> str:
        character_counts = {}
        for char in input_string:
            character_counts[char] = character_counts.get(char, 0) + 1

        # Early check: if any character appears too many times, return ""
        if max(character_counts.values()) > (len(input_string) + 1) // 2:
            return ""

        sorted_characters = sorted(character_counts.items(), key=lambda item: item[1], reverse=True)

        reorganized_string = [''] * len(input_string)
        index = 0

        # Distribute most frequent characters first
        for char, count in sorted_characters:
            for _ in range(count):
                # When we exceed the array, wrap to index 1 to fill odd positions
                if index >= len(input_string):
                    index = 1

                reorganized_string[index] = char
                index += 2

        return ''.join(reorganized_string)