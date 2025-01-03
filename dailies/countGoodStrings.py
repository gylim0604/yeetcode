class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        return self.tabulation(low, high, zero, one)

    def tabulation(self, low:int, high:int, zero: int, one: int)-> int:
        dp = [1] + [0]*(high)
        mod = 10**9+7
        
        for end in range(1, high+ 1):
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >=one:
                dp[end]+= dp[end-one]
            dp[end]%=mod
        return sum(dp[low:high+1])%mod
            
    def dpBackTrack(self, low:int, high: int, zero: int, one:int)-> int:
        mod = 10**9+7
        dp = {}
        def backtrack(length):
            if length >high:
                return 0
            if length in dp:
                return dp[length]
            dp[length] = 1 if length >= low else 0

            dp[length] += backtrack(length + zero) + backtrack(length+ one)
            return dp[length]%mod
        
        return backtrack(0)
sol = Solution()
print(sol.countGoodStrings(3,3,1,1))