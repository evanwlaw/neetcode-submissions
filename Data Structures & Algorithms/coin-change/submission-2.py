class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Input: coins = [1,5,10], amount = 12
        Output: 3

        12 -> 2x 1 coins and 1x 10 coin
        - 12 - 10 -> 2 find how many coins make up 2

        find the number of coins it takes per sum up to amount. DP approach where dp[i] = minimum number of coins to make the amount

        Base number of coins for all sums is coins of 1 value up to the given amount (if amount is 20, then 20x 1 coins is the largest amount it takes).


        dp[0] -> 0 coins needed to make 0 sum. this is base case. 
        dp[1] -> 1 coin (1) -> 5, 10 too larget (i - coinvalue == 0 + 1 coin)
        dp[2] -> 2 coin -> dp[i - coinvalue] + 1 -> dp[1] + 1
        ..
        ..
        dp[5] -> 1 coin -> dp[i - 5] + 1 (1) vs dp[i - 1] + 1 (5)

        iterate range(amount) ->
            iterate through coinvalues:
                if coinvalue - i >= 0, then this is valid sum 

        """
        print()
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1

