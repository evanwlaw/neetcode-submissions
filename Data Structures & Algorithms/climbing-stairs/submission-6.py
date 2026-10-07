class Solution:
    def climbStairs(self, n: int) -> int:
        """

        1 or 2 steps

        step 1 -> 1 way
        step 2 -> 2 ways
        step 3 -> step1 + step2 -> 3
        step 4 -> step 3 + step 2 ->  5 way
        step 5 -> step 4 + step 3 ->

        1

        1 1
        2

        1 1 1 
        1 2
        2 1

        1 1 1 1
        1 1 2
        1 2 1
        2 1 1
        2 2


        1 1 1 1 1
        1 1 1 2
        1 1 2 1
        1 2 1 1
        2 1 1 1
        2 2 1
        2 1 2
        1 2 2

        to get to step[i] it's step[i-1] + step[i-2]
        base is first step is 1 way, second step is 2
        """
        if n <= 2:
            return n
        dp = [1] * (n)
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

