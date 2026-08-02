class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Bottom up
        dp = []
        for _ in range(m):
            dp.append([0] * n)

        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r == c == 0:
                    continue

                value = 0
                if r > 0:
                    value += dp[r-1][c]
                if c > 0:
                    value += dp[r][c-1]
                dp[r][c] = value
        return dp[m-1][n-1]

