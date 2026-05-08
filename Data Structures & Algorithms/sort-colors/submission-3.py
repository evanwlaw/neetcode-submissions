class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        2   1   1   0
        l
                    r
        i

        l:i -> i:r -> r
        0      1      2

        """

        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1

            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1 # no need to increment i as what if it's replaced to a 0 for example

            else: # else increment i if nums[i] == 1
                i += 1
