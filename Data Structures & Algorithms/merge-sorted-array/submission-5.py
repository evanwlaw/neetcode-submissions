class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        10      20     20     40    0   0       m = 4
        1   2       n = 2

        fill from back use 3 ptrs
        """

        m, n = m - 1, n - 1
        z = len(nums1) - 1

        while n >= 0:

            if m >= 0 and nums1[m] > nums2[n]:
                nums1[z] = nums1[m]
                m -= 1
            else:
                nums1[z] = nums2[n]
                n -= 1
            z -= 1
        
        
        


        
        