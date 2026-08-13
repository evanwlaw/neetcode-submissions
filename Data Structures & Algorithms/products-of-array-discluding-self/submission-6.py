class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1       2       4       6

        2,4,6   1,4,6   1,2,6   1,2,4

        prefix * postfix

        res
        1       1       2       8
                        12      8

        48      24      12      8
        """

        prefix = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]  

        return res