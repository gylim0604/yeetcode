class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        if len(nums) <=1:
            return True
        for i in range(len(nums)-1):
            if (nums[i] + nums[i+1])%2== 0:
                return False
        return True
sol = Solution()
print(sol.isArraySpecial([4,3,1,6]))
print(sol.isArraySpecial([1,2,3,4]))