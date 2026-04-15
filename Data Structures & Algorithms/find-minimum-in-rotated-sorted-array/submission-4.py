class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        3   4   5   6   1   2
        l
                            r
        if nums[l] < [r] -> sorted
        
        nums[l] <= nums[m] -> m is on the left side. move l
        """

        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return res