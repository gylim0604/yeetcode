class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
            for i in range(0, len(sentence)):
                if sentence[i] == ' ' and sentence[i-1] != sentence[i+1]:
                    return False
            return sentence[0] == sentence[-1]

sol = Solution()
print(sol.isCircularSentence("leetcode exercises sound delightful"))
print(sol.isCircularSentence("eetcode"))
print(sol.isCircularSentence("Leetcode is cool"))
print(sol.isCircularSentence("MuFoevIXCZzrpXeRmTssj lYSW U jM"))