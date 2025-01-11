from typing import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        s_l = len(s)
        if s_l < k:
            return False
        if s_l == k:
            return True
        freq = Counter(s)
        odd_count = sum(v & 1 for v in freq.values())
        return odd_count < k


sol = Solution()
print(sol.canConstruct("annabelle",2))
print(sol.canConstruct("leetcode",3))
print(sol.canConstruct("true",4))