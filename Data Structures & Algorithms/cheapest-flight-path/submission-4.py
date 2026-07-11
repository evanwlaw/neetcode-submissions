class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Bellman ford - we don't want to get the shortest path (don't use BFS). 
        We want the path that stops k times -> We need to travel k + 1 flights/edges.

        Use a temp array to compare previous iteration results.

        prices
        0       1       2       3
        0       inf     inf     inf

        if prices[source airport] + price of current flight < tempArray[curr dest cost]
            update tempArray[curr dest cost] to new cheaper cost via current flight
        
        
        '''
        prices = [float("inf")] * n
        prices[src] = 0
        

        for i in range(k + 1):
            tempPrices = prices.copy()

            # iterate through flights/edges
            for s, d, p in flights: # s=source, d=dst, p=prices
                if prices[s] == float("inf"):
                    continue
                # relax edge
                if prices[s] + p < tempPrices[d]:
                    tempPrices[d] = prices[s] + p
            prices = tempPrices
        return -1 if prices[dst] == float("inf") else prices[dst]

