class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
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



