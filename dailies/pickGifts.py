import heapq
import math


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        res= 0
        heap = []
        for el in gifts:
            heapq.heappush(heap, -el)
        
        for i in range(k):
            val = heapq.heappop(heap)
            heapq.heappush(heap, -math.isqrt(-val))
        while heap:
            res += heapq.heappop(heap)
        return -res

sol = Solution()
print(sol.pickGifts([25,64,9,4,100],4))