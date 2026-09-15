class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        dp[i] is the cost of getting to the ith step

        dp[0] = 0
        dp[1] = 1

        dp[i] = min(dp[i-1] + nums[i], dp[i-2])

        """

        dp = [0] * (len(cost) + 1)


        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        return dp[len(cost)]

