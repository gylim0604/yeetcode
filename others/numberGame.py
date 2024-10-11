from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range(0,len(nums),2):
            print(nums[i], nums[i+1])
            nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums

arr = [5,4,2,3]
sol = Solution()
print(sol.numberGame(arr))