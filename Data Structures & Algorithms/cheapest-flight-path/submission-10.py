from collections import deque, defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n

        adjList = defaultdict(list) # airport : (neighbor, cost)

        for u, v, cost in flights:
            adjList[u].append((v,cost))
        
        queue = deque([[src,0, 0]]) # airport,pathCost, numStops
        prices[src] = 0
        
        while queue:
            airport, pathCost, numStops = queue.popleft()
            if numStops > k and airport != dst:
                continue
            
            for neighbor, cost in adjList[airport]:
                newCost =  cost + pathCost
                if newCost < prices[neighbor]:
                    prices[neighbor] = newCost
                    queue.append([neighbor, newCost, numStops + 1])

        return prices[dst] if prices[dst] != float('inf') else -1
