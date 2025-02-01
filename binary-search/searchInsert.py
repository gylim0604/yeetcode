class Solution:
    def searchInsertBinary(self, nums: list[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        low, high = 0, len(nums)-1
        mid = 0
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target: 
                return mid
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        return low
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

sol = Solution()
print(sol.searchInsert([1,3],2))