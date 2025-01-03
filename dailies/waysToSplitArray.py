class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        res = 0
        left = 0
        totalSum = sum(nums)
        for _, val in enumerate(nums[:-1]):
            left += val
            right = totalSum - left
            if left >= right:
                res+=1
        return res
sol = Solution()
# print(sol.waysToSplitArray([10,4,-8,7]))
print(sol.waysToSplitArray([1,1]))