class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        10  1   5   6   7   1 ->output 6 from prices[1] sell on prices[4]

        """
        maxProfit = 0
        buyDayPrice = prices[0]

        for p in prices:
            buyDayPrice = min(buyDayPrice, p)
            maxProfit = max(maxProfit, p - buyDayPrice)
        return maxProfit