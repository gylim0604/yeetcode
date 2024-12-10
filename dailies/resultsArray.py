class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        if k == 1:
            return nums
        length = len(nums)
        res = [-1]*(length - k + 1)
        counter = 1

        for i in range(length - 1):
            if nums[i] + 1 ==nums[i + 1]:
                counter+=1
            else: 
                counter = 1
            if counter >= k:
                res[i-k + 2] = nums[i + 1]
        
        return res
    
sol = Solution()
print(sol.resultsArray([1,2,3,4,3,2,5],3))