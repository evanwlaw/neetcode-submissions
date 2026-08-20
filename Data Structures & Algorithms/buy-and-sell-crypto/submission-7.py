class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minPrice = prices[0]
        maxPrice = 0

        for p in prices:
            minPrice = min(minPrice, p)
            maxPrice = max(maxPrice, (p - minPrice))
        return maxPrice