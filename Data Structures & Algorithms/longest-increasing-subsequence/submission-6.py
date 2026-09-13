class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''            0 1 2 3 4 5 6
        Input: nums = [9,1,4,2,3,3,7]
        Output: 4

        dp[i] -> longest subsequence up to this i point
        dp[0] -> 0
        dp[1] -> 1

        loop from 2, len(nums)
            i = 2
            is nums[2], 4 > nums[i-1=1], 1? yes so dp[2] longest -> 2
                dp[2-1] = dp[1] + 1 = 2
        
            i = 3
            is nums[3], 2 > nums[2], 4? no.
                dp[3-1] = dp[2] = 2
            
            i = 4
            is nums[4], 3 > nums[3], 2? yes.
                dp[4-1] = dp[3] + 1 = 3

            i = 5
            is nums[5], 3 > nums[4], 3? no.
                dp[5-1] = dp[4] = 3
            
            i = 6
            is nums[6], 7 > nums[5], 3? yes.
                dp[6-1] = dp[5] + 1 = 4

            check if nums[i] > nums[i-1] -> if yes, then dp[i-1] = dp[i-2] + 1 else, dp[i-2]
        '''
        if not nums:
            return 0

        dp = [1] * (len(nums))


        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            
        return max(dp)