class Solution:
    def maxScore(self, s: str) -> int:
        sLen = len(s)
        prefix = [0] * (sLen + 1)
        for i in range(1, sLen + 1):
            prefix[i] = prefix[i-1]+ (1 if s[i - 1] == '1' else 0)
        print(prefix)
        maxScore = 0
        currScore = 0
        for i in range(sLen - 1):
            if s[i] == '0':
                currScore +=1
            # prefix[sLen] - prefix[i+1] = total 1s - 1s available at point i, means will get # of 1s to the right of i
            maxScore = max(maxScore, currScore + (prefix[sLen] - prefix[i+1]))
        return maxScore
sol = Solution()
# print(sol.maxScore("011101"))
# print(sol.maxScore("00111"))
print(sol.maxScore("1111"))
print(sol.maxScore("000"))

# 011101
# 0 11101 = 1 + 4
# 01 1101 = 1 + 3
# 011 101 = 1 + 2
# 0111 01 = 1 + 1
# 01110 1 = 2 + 1

# 1111  = 4
# 1 111 = 3
# 11 11 = 2
# 111 1 =