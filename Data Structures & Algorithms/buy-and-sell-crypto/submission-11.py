class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Input: prices = [10,1,5,6,7,1]
        Output: 6 buy at prices[1] and sell at prices[6]


        output -> variable that holds the max profit up to the ith

        currBuyDay = prices[0]

        iterate through prices:
            if currBuyDay > prices[i]:
                update currbuyday
            else:
                check if it's the maxProfit so far
                -> maxProfit = max(maxProfit, prices[i] - currBuyDay)
        
        i = 1
        currBuyDay = 1
        maxProfit = 0

        """
        if not prices or len(prices) < 2:
            return 0

        currBuyDay = prices[0]
        max_profit = 0

        for p in prices:
            currBuyDay = min(currBuyDay, p)
            max_profit = max(max_profit, p - currBuyDay)
        return max_profit
