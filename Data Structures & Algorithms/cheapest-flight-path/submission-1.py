class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # djikstra's but need to include state of how many stops

        edge_adj = defaultdict(list) # u : (v,cost)
        for u,v,w in flights:
            edge_adj[u].append((v,w))
        
        min_heap = [(0,src,0)] # cost,city,numstops
        output_cost = 0

        while min_heap:
            cost, city, numStops = heapq.heappop(min_heap)
            
            if city == dst:
                return cost


            if numStops > k and city != dst:
                continue
            

            for city2, cost2 in edge_adj[city]:
                new_cost = cost2 + cost
                heapq.heappush(min_heap, (new_cost,city2, numStops + 1))
        return -1
