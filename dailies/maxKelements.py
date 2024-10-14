import heapq
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        nums = [-el for el in nums]
        heapq.heapify(nums)
        for i in range(k):
            curr = heapq.heappop(nums)
            res+= abs(curr)
            temp = ceil(curr//3)
            heapq.heappush(nums,temp)

        return res
arr = [1,10,3,3,3]
k = 3
sol = Solution()
print(sol.maxKelements(arr,k))