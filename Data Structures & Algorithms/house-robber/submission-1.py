class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Input: nums = [2,9,8,3,6]
        Output: 16
        Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.


        dp(5) = max(dp(4), dp(3) + nums[i])
        dp(i) = max(dp(i - 1), dp(i-2) + nums[i])
        '''
        memo = {}
        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return nums[0]
            if i in memo:
                return memo[i]
            
            memo[i] = max(dp(i-1), dp(i-2) + nums[i - 1])

            return memo[i]
        return dp(len(nums))