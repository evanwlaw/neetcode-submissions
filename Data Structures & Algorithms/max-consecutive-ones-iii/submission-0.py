class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        Output: 6


        1   1   1   0   0   0   1   1   1   1   0
                        l
                                            r
        maxWindLen = 6
        zeros = 2

        sliding window
        - when to increase
            when num of 0s < k
                r += 1
                maxWindLen = max(maxWindLen, r - l + 1)

        - when to decrease
            while num of 0s > k:
                l += 1

        """
        if len(nums) == 1:
            return 1

        zeros = 0
        maxWindLen = 0
        l, r = 0, 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            maxWindLen = max(maxWindLen, r - l + 1)
            r += 1
        return maxWindLen





        