class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        s = set(days)
        maxDay = days[-1]
        dp = [0] * (maxDay + 1)

        for i in range(1,len(dp)):
            # is a travel day
            if i in s:
                cost_1 = dp[i - 1] + costs[0]
                cost_7 = dp[max(0,i-7)] + costs[1]
                cost_30 = dp[max(0,i-30)] + costs[2] 
                print(cost_1, cost_7,cost_30)
                dp[i] = min(cost_1, cost_7, cost_30)
            # not a travel day
            else:
                dp[i] = dp[i-1]
        return dp[maxDay]

sol = Solution()
print(sol.mincostTickets([1,4,6,7,8,20],[2,7,15]))