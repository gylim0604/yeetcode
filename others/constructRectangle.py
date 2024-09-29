from math import  isqrt
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for width in range(isqrt(area), 0, -1):
            print(width)
            if(area% width == 0 ):
                length = area//width;
                return [length, width]


area = 4
sol = Solution()
print(sol.constructRectangle(area))