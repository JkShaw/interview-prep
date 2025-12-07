from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        a, b, c, d = 0, 1, 2, 3

        while a < len(nums) - 3:
            while b < len(nums) - 2:
                c = b + 1
                d = len(nums) - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])

                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1

                    elif total > target:
                        d -= 1
                    else:
                        c += 1
                b += 1
            a += 1
            b = a + 1

        return result

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    Output =  [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    result = Solution().fourSum(nums, target)
    print(result)