"""
Apply Substitutions

You are given two strings s and t. In one step, you can choose any substring of s and replace it with the string t.
Return the maximum number of times you can perform the above operation.
A substring is a contiguous (non-empty) sequence of characters within a string.

Example 1:
Input: s = "abab", t = "ab"
Output: 2
Explanation:
We can make the following changes:
- Replace the substring s[0:2] with t. Now s = "abab".
- Replace the substring s[2:4] with t. Now s = "abab".
Hence, the maximum number of operations is 2.

Example 2:
Input: s = "ababab", t = "ab"
Output: 3
Explanation:
We can make the following changes:
- Replace the substring s[0:2] with t. Now s = "ababab".
- Replace the substring s[2:4] with t. Now s = "ababab".
- Replace the substring s[4:6] with t. Now s = "ababab".
Hence, the maximum number of operations is 3.

Example 3:
Input: s = "abcab", t = "abc"
Output: 1
Explanation:
We can make the following changes:
- Replace the substring s[0:3] with t. Now s = "abcab".
Hence, the maximum number of operations is 1.

Constraints:
1 <= s.length, t.length <= 105
s and t contain only lowercase English letters.
"""
def apply_substitutions(original_string, substitutions):
    len_s = len(substitutions)
    len_o = len(original_string)

    if len_s > len_o:
        return 0

    count = 0
    for idx in range(len_o - len_s + 1):
        print(original_string[idx:idx+len_s])
        if original_string[idx:idx+len_s] == substitutions:
            count += 1

    return count

if __name__ == '__main__':
    # s = "abcab"
    # t = "abc"
    # s = "abab"
    # t = "ab"
    s = "ababab"
    t = "ab"
    result = apply_substitutions(s, t)
    print(result)
    # Output: 1