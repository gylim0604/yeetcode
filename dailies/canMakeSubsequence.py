class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        i,j = 0,0
        while i < len(str1) and j < len(str2):
            val1 = ord(str1[i])
            val2 = ord(str2[j])
            if val1 == val2 or self.increment_char(val1) == val2:
                j+=1
            i+=1
        return j == len(str2)
    def increment_char(self, val: int)-> int:
        return (val - ord('a') + 1)%26 + ord('a')
sol = Solution()
print(sol.canMakeSubsequence("abc","ad"))
print(sol.canMakeSubsequence("zc","ad"))
print(sol.canMakeSubsequence("ab","d"))