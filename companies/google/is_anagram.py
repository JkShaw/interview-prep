"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_frequency = dict()

        # Create character count for source
        for ch in s:
            if ch not in char_frequency:
                char_frequency[ch] = 1
            else:
                char_frequency[ch] += 1

        # Traverse target and match with character count map, if it becomes empty it mean anagram
        for ch in t:
            if ch not in char_frequency:
                return False
            else:
                char_frequency[ch] -= 1
                if char_frequency[ch] == 0:
                    del char_frequency[ch]

        return not char_frequency

