class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        """
        1   2   3   0   0   3   4
                l
                            r

        two ptrs - l at beginnging, r at the first non-zero
        swap l with r if nums[l] == 0
        increment r until nonzero
        """

        l, r = 0, 0


        while r < len(nums):
            if nums[r] == 0:
                r += 1
            
            else:
                if nums[l] == 0:
                    nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
        