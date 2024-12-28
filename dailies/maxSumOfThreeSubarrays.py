class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        sums = []
        currSum = sum(nums[:k])
        sums.append(currSum)
        for i in range(1, len(nums)-k + 1):
            currSum = currSum - nums[i-1] + nums[i + k - 1]
            sums.append(currSum)
        left = [0]*len(sums)
        maxSum = sums[0]
        left[0] = 0
        for i in range(1, len(sums)):
            if sums[i]> maxSum:
                maxSum = sums[i]
                left[i] = i
            else:
                left[i] = left[i-1]
        right = [0]*len(sums)
        maxSum = sums[-1]
        right[-1] = len(sums) - 1

        for i in range(len(sums) - 2, -1,-1):
            if sums[i] >= maxSum:
                maxSum = sums[i]
                right[i] = i
            else: 
                right[i] = right[i + 1]
        max_total = 0
        result = []
        for mid in range(k, len(sums) -k):
            l = left[mid-k]
            r = right[mid+k]
            total = sums[l] + sums[mid] + sums[r]
            if total > max_total:
                max_total = total
                result = [l,mid, r]
        print(left, right)
        return result
            
sol = Solution()
# print(sol.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1],2))
print(sol.maxSumOfThreeSubarrays([7,13,20,19,19,2,10,1,1,19],3))