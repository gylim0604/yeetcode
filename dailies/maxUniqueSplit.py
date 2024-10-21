from typing import List


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.backtrack(s,0, set())
        
    def backtrack(self, s:str, start: int, usedSubstring: List[str]):
        if start == len(s):
            return len(usedSubstring)
        maxSplit = 0
        for i in range(start,len(s)):
            substr = s[start:i+1]
            if substr not in usedSubstring:
                usedSubstring.add(substr)
                maxSplit = max(maxSplit,self.backtrack(s, i+1, usedSubstring))
                usedSubstring.remove(substr)
        return maxSplit
    
sol = Solution()
print(sol.maxUniqueSplit("wwwzfvwfvww"))