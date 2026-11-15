from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        find cheapest flight from src to dst

        bfs with priority queue
        """

        # adjList = defaultdict(list) # node : [(cost, neighbor), ()]

        # for u, v, cost in flights:
        #     adjList[u].append((cost, v))

        # queue = [(0,src)]
        # visited = set()
        # visited.add(src)
        
        # while queue:
        #     cost, node = heapq.heappop(queue)
        #     if node == dst:
        #         return cost
            
        #     for nei in adjList[node]:
        #         if nei not in visited:
        #             visited.add(nei)
        #             heapq.heappush(queue, (cost + nei[0], nei))
        # return -1

        adjList = defaultdict(list) # node : [(cost, neighbor), ()]
        prices = [float("inf")] * n
        prices[src] = 0

        for u, v, cost in flights:
            adjList[u].append((cost, v))

        queue = deque([(0,src, 0)]) # cost, node, numstops
        # visited = set()
        # visited.add(src)
        
        while queue:
            cost, node, numStops = queue.popleft()
            # if node == dst:
            #     return cost
            
            if numStops > k and node != dst: # current visitng airport stops is high, find a diff route
                continue
            
            for cost2, nei in adjList[node]:
                nextCost = cost + cost2
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    queue.append((nextCost, nei, numStops + 1))
        return prices[dst] if prices[dst] != float("inf") else -1
