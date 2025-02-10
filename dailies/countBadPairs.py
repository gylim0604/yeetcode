class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        diff_map = {}

        for i in range(n):
            diff = i - nums[i]  
            good_pair = diff_map.get(diff,0)
            res += i - good_pair 
            diff_map[diff] = good_pair + 1

        return res
sol = Solution()
print(sol.countBadPairs([4,1,3,3]))
print(sol.countBadPairs([1,2,3,4,5]))