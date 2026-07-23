class Solution:
    def countBits(self, n: int) -> List[int]:
        '''


        0 --> 0
        1 --> 1
        2 --> 10   -> dp[0] + 2 % 2 -> 0 + 1
        3 --> 11   -> dp[1] + 3 % 2 -> 1 + 1
        4 --> 100  -> dp[2] + 4 % 2 -> 1 + 0
        5 --> 101  -> dp[2] + 5 % 2 -> 1 + 1
        '''
        dp = [0] * (n+1)

        for i in range(1,n + 1):
            dp[i] = dp[i // 2] + (i%2)
        return dp