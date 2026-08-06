class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m = rows, n = cols
        dp = [[1] * n for _ in range(m)]
        # dp[0][0] = 1 # seed, there is one way to go start. thus 1 way to right/down

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]