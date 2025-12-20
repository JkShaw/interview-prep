"""
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.


Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}

        # update count_t based on target
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        have, need = 0, len(count_t)
        res, res_length = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            if ch in count_t and window[ch] == count_t[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < res_length:
                    res_length = r - l + 1
                    res = [l, r]

                # pop from left
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r + 1] if res_length != float('inf') else ""

