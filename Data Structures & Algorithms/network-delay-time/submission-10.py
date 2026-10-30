from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        need to figure time it takes from n to propagate to all nodes

        Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

        form node 1 to node 3 -> is time of 2
        from node 1 to node 4 -> is time of 3 via 2 and 3
        from node 1 to node 4 -> is time of 4 via 1

        use a minheap -> [cost, node]

        1. build adjlist[u] = [[t,v]]
        2. enqueue [0, k] k is start
        3. bfs through minheap
        """

        adjList = defaultdict(list) # adjList[u] = [[t,v]]
        for u, v, t in times:
            adjList[u].append((t,v))
        
        minHeap = [(0,k)]
        visited = set()
        time = 0
        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 not in visited:
                time = t1 # t1 is the time spanning from k to current
                visited.add(n1)

                for t2, n2 in adjList[n1]:
                    if n2 not in visited:
                        heapq.heappush(minHeap, (t2 + t1, n2))
        return time if len(visited) == n else -1

