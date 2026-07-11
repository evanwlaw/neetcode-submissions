class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        bellman ford - we don't want to get the shortest path
        we want the path that stops k times

        prices
        0       1       2       3
        0       inf     inf     inf

        '''

        prices = [float("inf")] * n

        prices[src] = 0

        for i in range(k + 1):
            tempPrices = prices.copy()

            for s, d, p in flights: # s=src airport, d=dest airport, p=price
                if prices[s] == float("inf"):
                    continue
                check_new = prices[s] + p
                if check_new < tempPrices[d]:
                    tempPrices[d] = check_new
            prices = tempPrices
        return -1 if prices[dst] == float("inf") else prices[dst]