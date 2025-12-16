from typing import List
import heapq

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        curr = 0

        for num, count in counter.items():
            if curr < k:
                heapq.heappush(heap, (count, num))
                curr += 1
            else:
                heapq.heappushpop(heap, (count, num))

        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1,2,3,4,5,6,7], 2))
    print(s.topKFrequent([7,7], 1))
    print(s.topKFrequent([1, 1, 1, 1, 2, 2, 3, 4, 4, 4], 2))
