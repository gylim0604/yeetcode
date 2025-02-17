class Solution:
    def find_partition(self, start_idx, curr_sum , string_num, target, memo): 
        if start_idx == len(string_num):
            return curr_sum == target
        
        if curr_sum > target:
            return False
        
        if memo[start_idx][curr_sum] != -1:
            return memo[start_idx][curr_sum] == 1
        
        partition_found = False
        for curr_idx in range(start_idx, len(string_num)):
            curr_str = string_num[start_idx: curr_idx + 1]
            addend = int(curr_str)
    def punishmentNumber(self, n: int) -> int:
        for i in range(1,n+1):
            print(i*i,i)

sol = Solution()
print(sol.punishmentNumber(10))