class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        bellman ford - we dont want to use bfs because not looking for shortest path
        looking for path that goes through k+1 edges/flights
        flights : [src,dst,price]
        
        n = 4

        prices
        0       1       2       3
        inf
        '''

        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):

            tempPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue

                new_edge_cost = prices[s] + p
                if new_edge_cost < tempPrices[d]:
                    tempPrices[d] = new_edge_cost
            prices = tempPrices
        return -1 if prices[dst] == float("inf") else prices[dst]

