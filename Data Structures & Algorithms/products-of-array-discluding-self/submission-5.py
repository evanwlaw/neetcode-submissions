class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

        1       2       4       6
first pass (prefix = 1):
    res[i] = prefix
    prefix = nums[i] * prefix
        1       1       2       8

second pass (postfix = 1)
for i in range(len(nums) - 1, -1, -1)
    res[i] *= postfix
    postfix = nums[i] * postfix
                        2      8

        """
        prefix = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] =  prefix
            prefix *= nums[i]
        
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
