class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            next_idx = (i+k)%n
            arr[next_idx] = nums[i]
        nums = arr
        print(arr)

    def bruteForce(self, nums: list[int], k: int) -> None:
        # Brute force, O(k^n)
        temp = 0
        n = len(nums)
        while k > 0:
            temp = nums[-1]
            for i in range(n-1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = temp
            k-=1
        print(nums)
        
sol = Solution()
# [2, 3, 4, 1]
print(sol.rotate([1,2,3,4],3))
print(sol.rotate([1,2,3,4,5,6,7],3))