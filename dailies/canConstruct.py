class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        # O(1) space
        freq = [0]*26
        for c in s:
            freq[ord(c)-ord('a')]+=1 
        oddCount = 0
        for count in freq:
            if count%2 != 0:
                oddCount+=1
        return oddCount <= k

sol = Solution()
print(sol.canConstruct("annabelle",2))
print(sol.canConstruct("leetcode",3))
print(sol.canConstruct("true",4))