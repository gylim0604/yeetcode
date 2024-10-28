import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for el in nums:
            if el in count:
                count[el] +=1
            else:
                count[el] = 1
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num],num))
            if len(heap)> k:
                heapq.heappop(heap)
        print(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
sol= Solution()
print(sol.topKFrequent( [1,2,2,3,3,3],2))