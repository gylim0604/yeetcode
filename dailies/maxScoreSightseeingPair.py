class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        maxPrefixScore = values[0]
        maxScore = maxPrefixScore
        for idx,val in enumerate(values):
            if idx == 0:
                continue
            maxScore = max(maxScore, (maxPrefixScore + val -idx))
            maxPrefixScore = max(maxPrefixScore, (idx+val))
        return maxScore
sol = Solution()
print(sol.maxScoreSightseeingPair([8,1,5,2,6]))