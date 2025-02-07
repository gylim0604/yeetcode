from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        res = 0
        prod_map = defaultdict()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                prod = nums[i] * nums[j]
                prod_map.setdefault(prod,0)
                prod_map[prod]+=1
        print(prod_map)
        for _, val in prod_map.items():
            if val >1:
                res += (val * (val-1)//2)*8
        return res

sol = Solution()
print(sol.tupleSameProduct([2,3,4,6]))
print(sol.tupleSameProduct([1,2,4,5,10]))
print(sol.tupleSameProduct([2,3,4,6,8,12]))