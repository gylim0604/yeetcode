class Solution:
    def check(self, nums: list[int]) -> bool:
        skip = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if skip:
                    return False
                else:
                    skip = True
        if skip and nums[-1] > nums[0]:
            return False
        return True 
        
sol = Solution()
print(sol.check([3,4,5,1,2]))
print(sol.check([2,1,3,4]))
print(sol.check([1,2,3]))