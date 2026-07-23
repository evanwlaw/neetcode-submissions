class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Input: nums = [2,9,8,3,6]

        Output: 16
        2, 8, 6 -> 16

        i = 4 -> take 6 + 2 + 8 or 9+3?
        i = 3 -> take 9 + 3 or 2 + 3?

        max(dp[i-2] + nums[i], dp[i-1])


        '''
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n - 1]
