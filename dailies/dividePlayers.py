from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        totalSkill = sum(skill)
        skillFreq = [0]*1001

        for el in skill:
            skillFreq[el] += 1
        if totalSkill% (n//2) != 0:
            return -1
        targetSkill = totalSkill // (n//2)
        res = 0;
        for playerSkill in skill:
            partnerSkill = targetSkill - playerSkill
            if skillFreq[partnerSkill] == 0:
                return -1
            res += playerSkill * partnerSkill
            skillFreq[partnerSkill] -=1
        return res //2

skill = [1,2,3,4]
sol = Solution()
print(sol.dividePlayers(skill))