class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        need to find the peak -> can be any peak

        binary search -> if nums[middle] < nums[middle + 1], we know we can move to right as we're slooping upwards
        """

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m
        return l