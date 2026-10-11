class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        find target val in a sorted array that is rotated
        return the idx of target if found or -1 if not

        - no guarantee solution is input
        - algorithm needs to be O(log N) time -> binary search

        Input: nums = [3,4,5,6,1,2], target = 1
        Output: 4

        0   1   2   3   4   5
        3   4   5   6   1   2
        l  
                            r
                m
        
        is target left or right of m?

        in normal binary search with array sorted properly, nums[l] <= nums[r]

        we can find if target is left or right of the pivot of where the array splits.

        first find where the pivot is (left or right) from m.
        in example, we see that pivot is right of nums[m] -> nums[l] <= nums[m]

            if nums[l] <=  nums[m] -> pivot is to the right of nums[m].
                then chekc to see if target is in left nums[l:m] -> move pointers accordingly.
            else: pivot is left of nums[m]

        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            # find where pivot is first
            if nums[l] <= nums[m]: # pivot is on right side
                # see if target is on left or right of pivot
                if nums[l] <= target <= nums[m]: # on left side
                    r = m - 1
                else: # else right side
                    l = m + 1
            else: # pivot is on left side
                if nums[m] <= target <= nums[r]: # target is on right side
                    l = m + 1
                else:
                    r = m - 1
        return -1 # if pointers cross and didnt find target, -1
                    

