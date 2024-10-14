import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        # set freq table
        freq = {}
        for el in hand:
            freq[el]= 1 + freq.get(el,0)
        # set heap
        minHeap = list(freq.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(first, first +  groupSize):
                if i not in freq:
                    return False
                freq[i]-=1
                if freq[i] == 0:
                    if i!= minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True

hand = [1,2,4,2,3,5,3,4]
groupSize = 4
sol = Solution()
print(sol.isNStraightHand(hand,groupSize))