class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        for ui, vi, wi in times:
            adjList[ui].append((wi, vi))


        # minheap
        minHeap = [[0, k]]
        visited = set()

        weight = 0 
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 not in visited:
                visited.add(n1)
                weight = w1 
                for w2, n2 in adjList[n1]:
                    if n2 not in visited:
                        heapq.heappush(minHeap, (w1+w2, n2))
        return weight if len(visited) == n else -1