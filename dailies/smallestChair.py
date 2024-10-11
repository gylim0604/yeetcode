import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [(a,i,l) for i,(a,l) in enumerate(times)]
        times.sort()
        availChairs = list(range(len(times))) # idx
        heapq.heapify(availChairs) 
        usedChairs = [] # leaving, idx
        print(times, availChairs)

        for a, i, l in times:
            while usedChairs and usedChairs[0][0] <= a:
                # free up all used chairs where leaving time <= a
                _, idx = heapq.heappop(usedChairs)
                heapq.heappush(availChairs, idx)    
            curr = heapq.heappop(availChairs)
            if i == targetFriend:
                return curr
            heapq.heappush(usedChairs, (l, curr))
        return -1
    
chairs = [[1,4],[2,3],[4,6]]
target = 1
sol = Solution()
print(sol.smallestChair(chairs, 1))