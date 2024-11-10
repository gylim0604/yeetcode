class Solution:
    def minimumSubarrayLength(self, nums: list[int], k: int) -> int:
        minLength = float('inf')
        windowStart =  windowEnd = 0
        bitCounts = [0]*32

        while windowEnd < len(nums):
            self.updateBitCounts(bitCounts, nums[windowEnd], 1)
            while (windowStart <= windowEnd and self.convertBitToNum(bitCounts) >=k):
                minLength = min(minLength, windowEnd - windowStart + 1)
                self.updateBitCounts(bitCounts, nums[windowStart],-1)
                windowStart +=1
            windowEnd +=1
        return -1 if minLength == float('inf') else minLength

    def updateBitCounts(self,bitCounts:list[int], number: int, delta: int)-> None:
        for pos in range(32):
            if number & (1<<pos):
                bitCounts[pos] += delta
    def convertBitToNum(self, bitCounts: list[int])-> int:
        result = 0
        for pos in range(32):
            if bitCounts[pos]:
                result |= 1 << pos
        return result

sol  = Solution()
print(sol.minimumSubarrayLength([2,1,8],10))