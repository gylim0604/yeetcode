from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times = [start for start, _ in intervals ]
        end_times = [ end for _, end in intervals]
        start_times.sort()
        end_times.sort()
        maxIntervals, activeIntervals = 0,0
        i,j = 0,0
        n = len(intervals)
        while i < n and j < n:
            if start_times[i] <= end_times[j]:
                activeIntervals+=1
                i+= 1
            else:
                activeIntervals-=1
                j+=1
            maxIntervals = max(maxIntervals,activeIntervals)
        return maxIntervals

arr = [[1,3],[5,6],[8,10],[11,13]]
sol = Solution()
print(sol.minGroups(arr))