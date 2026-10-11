class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        in a sorted array that is rotated, find the minimum val
        return min val

        needs to be log n time -> binary search

        Input: nums = [3,4,5,6,1,2]
        Output: 1
        

        0   1   2   3   4   5
        3   4   5   6   1   2
        l
                            r
                m
        
        if nums[l] < nums[r] -> normal sorted
        if nums[l] > nums[r] -> rotated

        if nums[m] > nums[r] -> we can throw away left side nums[l:m+1] (including nums[m]). those values are larger than nums[r] and pivot would be on right side

        0   1   2   3   4   5
        3   4   5   6   1   2
                    l
                            r
                        m
        
        if nums[m] < nums[r] -> possibly nums[m] is the smallest -> move r to m 

        Input: nums = [4,5,0,1,2,3]
        Output: 0

        0   1   2   3   4   5
        4   5   0   1   2   3
                l
                r
        solution is guarantteed in nums

        """

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
        