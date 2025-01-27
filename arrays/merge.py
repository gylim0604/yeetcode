class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = m-1,n-1
        c = len(nums1)-1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[c] = nums1[i]
                i-=1
            else:
                nums1[c] = nums2[j]
                j-=1
            c-=1

        

sol = Solution()
print(sol.merge([1,3,5,0,0,0],3,[2,4,6],3))
print(sol.merge([1],1,[],0))
print(sol.merge([0],0,[1],1))