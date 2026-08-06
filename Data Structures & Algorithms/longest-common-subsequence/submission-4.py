class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        i cat
            -
        j crabt
              -
        dp[i][j] = lcs length of the first i chars + j chars

            j
        i   0   2   3   4   
        0   1   1   1   1
        1   1   1   2   1
        2   1   1   1   3
        
        if char at i and j are the same:
            move both forward
        else:
            dp[i][j] = max(move )

        '''
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[m][n]
                    
            


