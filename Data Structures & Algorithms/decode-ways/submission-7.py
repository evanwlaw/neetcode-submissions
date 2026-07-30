class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        1012 -> JAB, JL
        2

        12 -> AB or L
        2

        '''
        if not s or s[0] == '0':
            return 0
        n = len(s) + 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n):

            # single
            digit = int(s[i-1])

            if digit != 0:
                dp[i] += dp[i - 1]

            # double
            digit = int(s[i-2:i])

            if 10 <= digit <= 26:
                dp[i] += dp[i - 2]
        return dp[n-1]