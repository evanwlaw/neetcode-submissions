class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n = 1
        1 + 0

        n = 2
        1 + 1
        0 + 2

        n = 3
        1 + 1 + 1
        1 + 2
        2 + 1

        n = 4
        1 + 1 + 1 + 1
        1 + 1 + 2
        1 + 2 + 1
        2 + 1 + 1
        2 + 2

        dp(1) = 1
        dp(2) = 2
        dp(3) = dp(2) + dp(3)
        '''
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]