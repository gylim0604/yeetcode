from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for el in nums:
            if freq.get(el):
                return True
            freq[el] = 1 
        return False

arr = [1,2,3,4]
sol = Solution()
print(sol.hasDuplicate(arr))