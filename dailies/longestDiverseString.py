import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        heap = [(-a,'a'),(-b,'b'),(-c,'c')]
        heapq.heapify(heap)
        curr = heapq.heappop(heap)
        while curr[0] < 0:
            val, char = curr
            for i in range(0,2):
                if(val == 0):
                    break
                res = res + char
                val +=1
            if not heap: 
                break
            curr = heapq.heappop(heap)
            if val < 0:
                heapq.heappush(heap,(val, char))
        return res
        

a ,b,c= 1,1,7
sol = Solution()
print(sol.longestDiverseString(a,b,c))
print(sol.longestDiverseString(7,1,0))