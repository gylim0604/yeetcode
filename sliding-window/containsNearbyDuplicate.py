class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False
        seen = set()
        l = 0
        for r in range(len(nums)):
            if r -l > k:
                seen.remove(nums[l])
                l+=1
            if nums[r] in seen:
                return True
            seen.add(nums[r])
        return False

sol = Solution()
print(sol.containsNearbyDuplicate([0,1,2,3,2,5],3))