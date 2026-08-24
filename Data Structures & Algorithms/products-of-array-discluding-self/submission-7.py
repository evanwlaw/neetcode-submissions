class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1,2,4,6]
        Output: [48,24,12,8]

        iterate through nums[0]
        we know our current nums is 1
        we lose the current nums by iterating next and won't be able to use for subsequent nums product.

        iterate through nums[1]
        we know our current nums 2.
        we lose the current nums by iterating next and won't be able to use for subsequent nums product.

        iterate through nums[2]
        we know our current nums 4
        we lose the current nums by iterating next and won't be able to use for subsequent nums product.


        iterate through nums[3]
        we know our current nums 6
        we lose the current nums by iterating next and won't be able to use for subsequent nums product.

        running through nums, we need variable that holds nums[:i]  multiplied.

        and we can do the same working backwards to get the output array

        prefix = 8
        nums
        1   2   4   6

        output
        1   1   2   8
        postfix = 1
        """
        prefix = 1
        output = [1] * len(nums)

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output



