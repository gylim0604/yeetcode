class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        
        dp = [0] * len(days)
        dp[0] = costs[0]
        for i in range(len(days)):
            cost_1 = (dp[i-1] + costs[0]) if i > 0 else costs[0]
            j = i
            while j >= 0 and days[j] >= days[i] - 6:
                j-=1
            cost_7 = dp[j]+ costs[1] if j >= 0 else costs[1]
            j = i
            while j >= 0 and days[j] >= days[i] - 29:
                j-=1
            cost_30 = dp[j]+ costs[2] if j >= 0 else costs[2]
            
            dp[i] = min(cost_1, cost_7, cost_30)

        return dp[-1]

sol = Solution()
print(sol.mincostTickets([2,33],[2,7,15]))