"""
Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.


Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]


Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partial = []

        def dfs(i):
            if i >= len(s):
                result.append(partial[:])
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partial.append(s[i:j + 1])
                    dfs(j + 1)
                    partial.pop()

        dfs(0)
        return result

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
