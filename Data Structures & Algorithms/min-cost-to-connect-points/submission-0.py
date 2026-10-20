class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        minheap -> [cost to node, node]

        cost is the manhattan distance

        """
        # adjList = defaultdict(list) # u : [v, t]
        # for u, v, t in times:
        #     adjList[u].append([v, t])
        

        queue = [[0, 0]] # cost to node, node
        visited = set()
        total_cost = 0

        while len(visited) < len(points):
            cost, node = heapq.heappop(queue)
            if node not in visited:
                visited.add(node)
                total_cost += cost

                x1, y1 = points[node]

                for nei, (x2, y2) in enumerate(points):
                    if nei not in visited and node != nei:
                        nei_cost = abs(x1-x2) + abs(y1-y2)
                        heapq.heappush(queue, [nei_cost, nei])
        return total_cost
