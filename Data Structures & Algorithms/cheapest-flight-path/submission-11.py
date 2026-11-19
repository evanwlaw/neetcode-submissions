from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list) # city : [[city,cost]]
        prices = [float('inf')] * n
        for u, v, cost in flights:
            adjList[u].append([v, cost])
        
        queue = deque([[src, 0, 0]]) # city, cost, numStops

        while queue:
            city1, cost1, numStops = queue.popleft()

            if numStops > k:
                continue
            
            for city2, cost2 in adjList[city1]:
                newCost = cost1 + cost2
                if newCost < prices[city2]:
                    prices[city2] = newCost
                    queue.append([city2, newCost, numStops + 1])
        return prices[dst] if prices[dst] != float('inf') else -1
