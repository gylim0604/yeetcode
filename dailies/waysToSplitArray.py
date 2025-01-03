class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        res = 0
        prefixSum = [0] * (len(nums) + 1)
        suffixSum = [0] * (len(nums) + 1)
        for i in range(1, len(prefixSum)):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]
        for i in range(len(prefixSum) - 2, -1, -1):
            suffixSum[i] = suffixSum[i+1] + nums[i]
        for i in range(1, len(prefixSum) -1):
            left, right = prefixSum[i], suffixSum[i]
            if left >= right:
                res+=1
        return res
sol = Solution()
# print(sol.waysToSplitArray([10,4,-8,7]))
print(sol.waysToSplitArray([1,1]))