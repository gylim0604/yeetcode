class Solution:
	def scoreOfString(self, s: str) -> int:
		score = 0
		for i in range(1, len(s)):
			score = score + abs(ord(s[i-1]) - ord(s[i]))
		return score

s = 'hello'
sol = Solution()
print(sol.scoreOfString(s))