class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        minheap
        """
        adjList = defaultdict(list) # node : (cost, node2)

        for u, v, t in times:
            adjList[u].append((t, v))

        minHeap = [[0, k]] # cost, node
        visited = set()
        output = 0

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 not in visited:
                visited.add(n1)

                output = t1

                for t2, n2 in adjList[n1]:
                    if n2 not in visited:
                        heapq.heappush(minHeap, (t1+t2, n2))
        return output if len(visited) == n else -1
