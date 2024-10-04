from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 0, len(skill) - 1
        target = skill[left]+ skill[right]
        res = 0;
        while left <= right:
            curr = skill[left] + skill[right]
            if(target != curr):
                return -1
            res += (skill[left] * skill[right])
            left+= 1
            right -=1
        return res

skill = [3,4]
sol = Solution()
print(sol.dividePlayers(skill))