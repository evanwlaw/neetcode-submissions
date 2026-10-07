class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        input is sorted by rotated

        output is the valu of the smallest/min value in the array

        Input: nums = [3,4,5,6,1,2]
        Output: 1

        Need to find in O(log N) -> binary search with ptrs l and r at each end.
        Goal is to find where l crosses r to find the min. We are guaranteed to find solution. 
        0   1   2   3   4   5
        3   4   5   6   1   2
                    l  
                        r
                        
                
        m = l + (r-l) // 2 (aka (l + r) // 2)

        on 1st run:
        l, r = 0, 5
        m = 2

        we know m is on right side of the array if nums[m] > nums[r]
            move l = m + 1 = 3

        on 2nd run:
        l, r = 3, 5
        m = 4

        we know since nums[m] < nums[r]:
            we can move r to m = 4

        on 3rd run:
        l, r = 3, 4
        m = 3
        since nums[m] > nums[r]
            move l = m + 1 = 5
        
        since l > r, terminate. return l or r
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]