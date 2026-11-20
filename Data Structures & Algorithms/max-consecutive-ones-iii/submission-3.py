class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        1   1   1   0   0   0   1   1   1   1   0
        ------------------


        """

        # maxZeros = 0
        # l = 0
        # output = 0

        # for r in range(len(nums)):
        #     if nums[r] == 0:
        #         maxZeros += 1
                
        #     while l < r and maxZeros > k:
        #         if nums[l] == 0:
        #             maxZeros -= 1
        #         l += 1

        #     output = max(output, r - l + 1)
        # return output

        zeros = 0
        l, r = 0,0
        output = 0
        if len(nums) == 1:
            return 1
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            output = max(output, r - l + 1)
            r += 1
        return output
            