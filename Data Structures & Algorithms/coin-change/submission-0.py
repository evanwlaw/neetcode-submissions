class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sum = [float("inf")] * (amount + 1)
        sum[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                check = i - c
                # make sure we check valid sums
                if check >= 0:
                    sum[i] = min(sum[i-c] + 1, sum[i])

        return sum[amount] if sum[amount] != float("inf") else -1