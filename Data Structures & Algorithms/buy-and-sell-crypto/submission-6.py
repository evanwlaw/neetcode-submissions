class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # window increases if [l] < [r]
        # reset when [l] > [r]


        """

        10  1   5   6   7   1
            l
                    r
        """

        l, r = 0, 1
        res = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                potential_profit = prices[r] - prices[l]
                res = max(res, potential_profit)
            else:
                l = r
            r += 1
        return res