class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        0   1   4   0   3   0   4   2
                        l 
                        r

        """

        l, r = 0, len(nums)

        while l < r:
            if nums[l] == val:
                r -= 1
                nums[l] = nums[r]
            else:
                l += 1
        
        return l