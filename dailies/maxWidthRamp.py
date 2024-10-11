from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices = [i for i in range(n)]
        # sorted indices based of the values
        indices.sort(key=lambda i: (nums[i],i))
        
        minIndex = n
        maxWidth = 0

        for i in indices:
            maxWidth = max(maxWidth, i - minIndex)
            minIndex = min(i, minIndex)
        return maxWidth
nums =[6, 0, 8, 2, 1, 5]
sol = Solution()
print(sol.maxWidthRamp(nums))