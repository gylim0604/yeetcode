from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0;
        for val in nums1:
            for divider in nums2:
                if(val%( divider * k) == 0):
                    res = res + 1
        return res

nums1 = [1,3,4]
nums2 = [1,3,4]
k = 1
sol = Solution()
print(sol.numberOfPairs(nums1, nums2,k))