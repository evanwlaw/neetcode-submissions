class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mIdx = m - 1
        nIdx = n - 1
        r = len(nums1) - 1

        while nIdx >= 0:
            if mIdx >= 0 and nums1[mIdx] > nums2[nIdx]:
                nums1[r] = nums1[mIdx]
                mIdx -=1
            else:
                nums1[r] = nums2[nIdx]
                nIdx -= 1
            r -= 1
            