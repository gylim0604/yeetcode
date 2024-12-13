import heapq


class Solution:
    # Solution using heap and set
    def findScore1(self, nums: list[int]) -> int:
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
    def findScore(self, nums: list[int]) -> int:
        score = 0
        i =0
        while i < len(nums):
            start  = i
            while i + 1 < len(nums) and nums[i+1] < nums[i]:
                i+=1
            for j in range(i, start -1, -2):
                score+=nums[j]
            i+=2

        return score

sol = Solution()
print(sol.findScore([2,1,3,4,5,2]))