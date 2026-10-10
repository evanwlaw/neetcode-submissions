class Solution:
    def climbStairs(self, n: int) -> int:
        """
        given in, return number of distinct ways to top of stairs
        steps can be 1 or 2

        if n = 3 -> 3
        1   1   1
        1   2
        2   1

        if n = 4 -> 5
        1   1   1   1
        1   2   1
        2   1   1
        1   1   2
        2   2

        to get to the  step -> it's the number of steps to get from i - 1 and i - 2

        because we can get to i from minus 1 or minus 2 steps

        dp[1] = 1
        dp[2] = 2 -> dp[i-1] + dp[i-2] -> dp[1] + dp[0]

        """

        # if n == 1:
        #     return 1
        
        # dp = [1] * (n+1)
        
        # for i in range(2, len(dp)):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        """
        more optimized in space
        """
        prev1, prev2 = 1, 1

        for i in range(n-1):
            temp = prev1 + prev2
            prev1 = prev2
            prev2 = temp
        return prev2