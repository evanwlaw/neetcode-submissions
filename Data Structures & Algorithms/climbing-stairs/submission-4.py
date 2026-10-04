class Solution:
    def climbStairs (self, n: int) -> int:
        """
        need to reach top of stairs.
        Either 1 or 2 steps at a time
        Output is the # of distinct ways to climb to top

        n = 2
        output = 2
        1 + 1
        2

        n = 3
        output = 3
        1 + 1 + 1
        2 + 1
        1 + 2

        use dp -> dp[i] = the number of ways to get to that point
        dp[0] = 0 to get step 0
        dp[1] = 1 way (1 step)
        dp[2] = 2 way (dp[1] + 1(2))
        dp[3] = # of ways to get to dp[1] + dp[2]
        dp[4]

        n = 4
        1 + 1 + 1 + 1
        1 + 2 + 1
        1 + 1 + 2
        2 + 1 + 1

        """
        # if n <= 2:
        #     return n
        # dp = [0] * (n+1)
        # dp[0] = 1
        # dp[1] = 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i - 1] + dp[i-2]
        # return dp[n]

        if n <= 2:
            return n
        dp1 = 1
        dp2 = 1

        for i in range(n-1):
            # temp = dp1
            temp = dp2 + dp1
            dp1 = dp2
            dp2 = temp
        return dp2