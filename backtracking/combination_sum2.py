"""
Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.


Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def helper(idx, path, val):
            if val == target:
                result.append(list(path))
                return

            for j in range(idx, len(candidates)):
                # remove duplicate path
                if j > idx and candidates[j] == candidates[j - 1]:
                    continue

                # remove impossible candidates
                if (val + candidates[j]) > target:
                    break

                path.append(candidates[j])
                helper(j + 1, path, val + candidates[j])
                path.pop()

        helper(0, [], 0)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(s.combinationSum2([2, 5], 5))
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))