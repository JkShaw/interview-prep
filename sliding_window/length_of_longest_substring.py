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
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left_pointer = 0
        visited = dict()

        for i, ch in enumerate(s):
            if ch in visited and visited[ch] >= left_pointer:
                left_pointer = visited[ch] + 1
                visited[ch] = i
            else:
                visited[ch] = i
                max_length = max(max_length, i - left_pointer + 1)

            print(f"left_pointer: {left_pointer}, ch: {ch}, i: {i}, visited: {visited}, max_length: {max_length}")
        return max_length

if __name__ == '__main__':
    s = Solution()
    # print(s.lengthOfLongestSubstring("abcabcbb"))
    # print(s.lengthOfLongestSubstring("bbbbb"))
    # print(s.lengthOfLongestSubstring("pwwkew"))
    # print(s.lengthOfLongestSubstring("abba"))
    print(s.lengthOfLongestSubstring("tmmzuxt"))
