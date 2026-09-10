class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Input: nums = [2,9,8,3,6]
        Output: 16
        Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.


        figure which is the max of current house ->
        1. Rob this one + the value of two houses ago
        2. the value of previous house

        each dp[i] is the max value that we can steal up to that house.
        return value 5th house
        """
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for house in range(2, n):
            dp[house] = max(dp[house - 1], dp[house-2] + nums[house])
        return dp[len(nums)-1]

