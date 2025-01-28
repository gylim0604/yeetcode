class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # O(nlogn)
        sorted_arr = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and sorted_arr[i]== sorted_arr[i-1]:
                continue
            # fix first val to sorted_arr[i]
            curr = sorted_arr[i]
            # since we sorted the array, once we get to positive values it can no longer sum to 0
            if curr > 0:
                break
            l,r = i+1, n-1
            while l <r:
                currSum = sorted_arr[l] + sorted_arr[r] + curr
                # if l + r = 0
                if currSum == 0:
                    res.append([curr, sorted_arr[l], sorted_arr[r]])
                    # skip duplicates
                    while l < r and sorted_arr[l] == sorted_arr[l+1]:
                        l+=1
                    while l < r and sorted_arr[r] == sorted_arr[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif currSum < 0: 
                    l+=1
                else:
                    r-=1
        return res



sol = Solution()
# print(sol.threeSum([1,2,-2,-1]))
# print(sol.threeSum([-1,0,1,0]))
print(sol.threeSum([1,-1,-1,0]))