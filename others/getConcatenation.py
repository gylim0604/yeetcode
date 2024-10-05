from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [None]*(size*2)
        for i in range(0,(2*size)):
            res[i] = nums[i%size]
        return res

arr = [1,2,1]
sol = Solution()
print(sol.getConcatenation(arr))