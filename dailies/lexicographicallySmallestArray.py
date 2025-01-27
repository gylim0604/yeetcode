from collections import deque
import heapq


class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        groups = [] # list of queues
        num_to_group = {} # nums[i] -> groups index
        
        # form groups
        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())

            groups[-1].append(n)
            num_to_group[n] = len(groups)-1

        res = []
        for n in nums:
            j = num_to_group[n]
            res.append(groups[j].popleft()) 
        return res

sol = Solution()
print(sol.lexicographicallySmallestArray([1,5,3,9,8],2))
print(sol.lexicographicallySmallestArray([1,7,6,18,2,1],3))
print(sol.lexicographicallySmallestArray([1,7,28,19,10],3))
# print(sol.lexicographicallySmallestArray([8, 2, 4, 1],3))