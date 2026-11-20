from collections import deque, defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        """
        return the cost goign from src to dst within k stops (k + 1 flights)

        go through airports bfs to get the lowest price
        
        
        """
        prices = [float("inf")] * n
        # 1. adjlist
        adjList = defaultdict(list) # airport : [[n1, cost], [n2, cost]]
        for u, v, cost in flights:
            adjList[u].append(([v, cost]))

        # 2. queue from src
        queue = deque([[src, 0, 0]]) #airport, cost, numStops
        prices[src] = 0

        # 3. bfs
        while queue:
            airport, currCost, numStops = queue.popleft()
            if numStops > k: # pass airports that exceed our num of stops
                continue

            # find if going through a specific airport's is cheaper or not
            for neighborAiport, neighborCost in adjList[airport]:
                newCost = currCost + neighborCost
                if newCost < prices[neighborAiport]:
                    queue.append([neighborAiport, newCost, numStops + 1])
                    prices[neighborAiport] = newCost

        return prices[dst] if prices[dst] != float("inf") else -1