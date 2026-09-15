class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        Input: prices = [10,1,5,6,7,1]
        Output: 6

        buyAmt = 10
        maxProfit = 0

        prices[1] = 1
        buyAmt = min(prices[1], 10) -> 1
        if prices[i] > buyAmt: -> no


        prices[2] = 
            profit = prices[i] - buyAmt
            maxProfit = max(maxProfit, profit)

        """
        buyAmt = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            buyAmt = min(prices[i], buyAmt)

            maxProfit = max(maxProfit, prices[i] - buyAmt)
        return maxProfit