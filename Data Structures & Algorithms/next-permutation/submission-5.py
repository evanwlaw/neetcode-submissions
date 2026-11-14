class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1   3   5   4   2 -> 14235
        """
        i = len(nums) - 2
        # find where num "drops"
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0: # means there exists something to swap
            swap = len(nums) - 1
            while nums[swap] <= nums[i]:
                swap -= 1
            nums[i], nums[swap] = nums[swap], nums[i]
        
        # reverse i + 1 : end
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1