class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        so get the lowest

        1   3   5   4   2 -> 14235

        1. walk backwards until nums[i] <= nums[i+1] -> that's pivot

        2. walkbackwards until nums[swap] > nums[i] -> swap

        1   3   5   4   2
            i       s
        
        1   4   5   3   2 ->swap pivot
            i       s

        however, we can sort from [i+1:] from least to greatest to get smallest permuation
        1   4   2   3   5

        3. if no pivot found, swap ends
        """
        if len(nums) == 1:
            return nums
        
        i = len(nums) - 2 # compare i with i + 1
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            swap = len(nums) - 1
            while nums[swap] <= nums[i]:
                swap -= 1
            nums[i], nums[swap] = nums[swap], nums[i]

        # reverse from i+1 to end
        i, n = i + 1, len(nums) - 1
        while i < n:
            nums[i], nums[n] = nums[n], nums[i]
            i += 1
            n -= 1



