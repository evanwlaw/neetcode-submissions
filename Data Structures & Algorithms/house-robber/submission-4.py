class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Input: nums = [2,9,8,3,6]
        Output: 16
        Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.


        dp(5) = max(dp(4), dp(3) + nums[i])
        dp(i) = max(dp(i - 1), dp(i-2) + nums[i])
        '''
        dp2, dp1 = 0,0

        for i in nums:
            temp = max(i + dp2, dp1)
            dp2 = dp1
            dp1 = temp
        return dp1