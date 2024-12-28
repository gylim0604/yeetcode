class Solution:
    def finalPricesBruteForce(self, prices: list[int]) -> list[int]:
        for i in range(len(prices) -1):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i]-= prices[j]
                    break    
        return prices
    
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []
        for idx in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[idx]:
                prices[stack.pop()]-= prices[idx]
            stack.append(idx)
        return prices

sol = Solution()
print(sol.finalPrices([8,4,6,2,3]))
print(sol.finalPrices([10,1,1,6]))