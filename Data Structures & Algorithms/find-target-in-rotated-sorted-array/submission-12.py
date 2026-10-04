class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Input: nums = [3,4,5,6,1,2], target = 1
        Output: 4


        Input: nums = [3,5,6,0,1,2], target = 4
        Output: -1


        binary search -> need to figure out if target is in left or right side of the sorted position

    target: 1 (on right side of smallest)
    i   0   1   2   3   4   5
    v   3   4   5   6   1   2
        l
                            r

                m

        1st iteration:
            find m: l + (r-l) / 2 -> 0 + 5 / 2 -> m = 2.5
            
            if left side is sorted to m is sorted:
                find if target is on left side
            else m throughright is sorted 

        """
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
