class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        tDict = {}
        sDict = {}
        for i in range(0, len(s)):
            tDict[t[i]] = i
            sDict[s[i]] = i

        for el in sDict:
            res += abs(tDict[el] - sDict[el])
        
        return res
s , t = 'abcde','edbac'
sol = Solution()
print(sol.findPermutationDifference(s,t))