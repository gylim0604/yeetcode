class Solution:
    def minSwaps(self, s: str) -> int:
        close, maxClose = 0,0
        for el in s:
            if el == '[':
                close-=1
            else:
                close+=1
            maxClose = max(close, maxClose)
        return( maxClose+1) //2
    
s = '][]['
sol = Solution()
print(sol.minSwaps(s))