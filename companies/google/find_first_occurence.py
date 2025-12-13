"""
Find the Index of the First Occurrence in a String
Attempted
Easy
Topics
premium lock icon
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        text_length = len(haystack)
        pattern_length = len(needle)

        if pattern_length == 0:
            return 0

        # Create potential starting point map.
        potential_starts = []
        for i in range(text_length - pattern_length + 1):
            potential_starts.append(i)

        # Only compare pattern at possible start positions.
        for start_index in potential_starts:
            if haystack[start_index:start_index + pattern_length] == needle:
                return start_index

        # Pattern isn't in text.
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr("mississippi", "issip"))
    # print(s.strStr("leetcode", "leeto"))