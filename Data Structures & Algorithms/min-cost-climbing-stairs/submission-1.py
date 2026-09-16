class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        can choose either the first or second step.
        return cost of what it takes to get to len(cost) + 1

        Input: cost = [1,2,1,2,1,1,1]
        Output: 4

        use dp to hold the cost it takes to get to dp[i]

        dp[0] and dp[1] are base case of 0 cost as these are free

        dp[2] = min(dp[2-1],dp[2-2])
        dp[3] = min(dp[3-1] + nums[3-1],dp[3-1] + nums[3-2])

        """

        dp = [0] * (len(cost)+1)

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        return dp[len(cost)]