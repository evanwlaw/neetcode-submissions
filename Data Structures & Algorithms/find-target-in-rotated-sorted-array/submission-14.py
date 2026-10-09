class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        search for target in rotated array

        binary search.
        need to figure out if target is in left or right side of pivot

        Input: nums = [3,4,5,6,1,2], target = 1
        Output: 4

        0   1   2   3   4   5
        3   4   5   6   1   2
                    l 
                            r
                        m
        
        if nums[l] < nums[r] -> sorted properly
        1st run
            l, r, m = 0, 5, 2
            target is right side of pivot -> nums[m] > target
            need to move l to m + 1 = 3
        2nd run
            l, r, m = 3, 5, 4
        
        nums[l] <= target <= nums[m]
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]: # pivot is on right side of m
                # find out if target is on left or right of pivot
                if nums[l] <= target <= nums[m]: # pivot is on left side
                    r = m - 1
                else:
                    l = m + 1
            else: # pivot left side
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
