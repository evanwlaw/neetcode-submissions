class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Input: nums = [3,4,5,6,1,2]
        Output: 1


        3   4   5   6   1   2
        l
                            r
                    m
        6   1   2   3   4   5
        l
                            r
                    m
        use binary search to find the smallest val
        basecase if rotated 6 times: if nums[l] < nums[m] nums[r]  -> [l:rm] is sorted correctly -> nums[l] smallest

        if nums[l] < nums[m] and nums[m] > nums[r]:
            left side [l:m] is sorted correctly, 
            right side is not. target is on right side
            l = middle + 1
        
        if nums[l] > nums[m] and nums[m] < nums[r]:
            right side [m:r] is sorted correctly,
            left side is not. target is on the left side
            r = middle - 1
        

        
        """
        output = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                output = min(output, nums[l])
                return output
            m = (r + l) // 2
            output = min(output, nums[m])

            if nums[l] <= nums[m] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return output
