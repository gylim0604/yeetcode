class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        tDict = {}
        for i in range(0, len(t)):
            tDict[t[i]] = i

        for i in range(0, len(s)):
            res += abs(tDict[s[i]] - i)
        return res
s , t = 'abcde','edbac'
sol = Solution()
print(sol.findPermutationDifference(s,t))