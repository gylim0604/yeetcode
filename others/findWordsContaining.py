from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for idx, val in enumerate(words):
            if x in val:
                res.append(idx)
        return res
arr = ["leet","cod"]
x = 'e'
sol = Solution();
print(sol.findWordsContaining(arr,x))