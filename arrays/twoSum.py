from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0,len(nums)):
            remain = target - nums[i]
            if remain in map:
                return [map[remain],i]
            else:
                map[nums[i]] = i

sol = Solution()
print(sol.twoSum([2,7,11,15],9))