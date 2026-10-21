import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        adjlist -> node : [cost, neighbor1]

        adjlist[u] -> [t, v]

        minheap -> cost, node

        bfs -> neighbor to push to heap is time of previous node + neighbor node (v)
        """

        adjList = defaultdict(list)

        for u, v, t in times:
            adjList[u].append([t, v])
        
        queue = [[0, k]] # push start into queue. cost to start is 0
        output = 0 # this is time
        visited = set()

        while queue:
            t1, u = heapq.heappop(queue)
            if u not in visited:
                visited.add(u)
                output = t1

                for t2, nei in adjList[u]:
                    if nei not in visited:
                        heapq.heappush(queue, [t1 + t2, nei])
        return output if len(visited) == n else -1
