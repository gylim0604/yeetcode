import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ['']
        heap = []
        if a > 0:
            heap.append((-a, 'a'))
        if b > 0:
            heap.append((-b, 'b'))
        if c > 0:
            heap.append((-c, 'c'))
        heapq.heapify(heap)

        while heap:
            # Add first character
            currVal, currChar = heapq.heappop(heap)
            # if there has been 2 consecutive characters
            if len(res) >= 2 and res[-1] == currChar and res[-2] == currChar:
                if not heap:
                    break
                nextVal,nextChar = heapq.heappop(heap)
                res = res + nextChar
                nextVal+=1
                # if next is still valid, add back to heap
                if nextVal < 0:
                    heapq.heappush(heap,(nextVal, nextChar))
                heapq.heappush(heap,(currVal, currChar))
            else:
                # append curr to result
                res = res + currChar
                currVal +=1
                # if curr is still valid, add back to heap
                if currVal < 0:
                    heapq.heappush(heap,(currVal, currChar))
        return res
        

a ,b,c= 1,1,7
sol = Solution()
# print(sol.longestDiverseString(a,b,c))
# print(sol.longestDiverseString(7,1,0))

print(sol.longestDiverseString(0,8,11))