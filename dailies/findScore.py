import heapq


class Solution:
    def findScore(self, nums: list[int]) -> int:
        score = 0
        heap = []
        marked = set()
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i],i))
        while heap:
            val, idx = heapq.heappop(heap)
            if not idx in marked:
                score+= val
                marked.add(idx+1)
                marked.add(idx-1)
        return score
sol = Solution()
print(sol.findScore([2,1,3,4,5,2]))