from heapq import heapify, heappop, heappush
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]

sol = KthLargest(3,[4, 5, 8, 2])  
print(sol.add(3))   # return 3
print(sol.add(5))   # return 3
print(sol.add(10))   # return 3
print(sol.add(9))   # return 5
print(sol.add(4))   # return 6


arr = [1,2,3,4,5,6,7]
print(arr[-3])