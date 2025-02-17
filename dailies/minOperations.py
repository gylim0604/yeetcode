import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        res = 0
        heapq.heapify(nums)
        while nums  and nums[0] <k:
            val1, val2 = heapq.heappop(nums), heapq.heappop(nums) 
            new = min(val1,val2)*2 + max(val1,val2)
            heapq.heappush(nums,new)
            res+=1
        return res

sol = Solution()
print(sol.minOperations([2,11,10,1,3],10))
print(sol.minOperations([1,1,2,4,9],20))
print(sol.minOperations([999999999,999999999,999999999],1000000000))