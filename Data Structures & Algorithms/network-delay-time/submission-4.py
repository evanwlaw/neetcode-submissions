class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        dijkstra's with minheap

        process each node based on the weight so far via minheap
        """

        # adj list node : (vi, ti)
        adj_list = defaultdict(list)
        # time[i] = ui, vi, ti
        for ui, vi, ti in times:
            adj_list[ui].append((vi,ti))

        # seed heap with (weight=0,k)
        minHeap = [(0, k)]

        time = 0
        visited = set()

        # dijkstra's
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 not in visited:
                visited.add(n1)
                time = w1

                # go through neighbors
                for n2, w2 in adj_list[n1]:
                    if n2 not in visited:
                        heapq.heappush(minHeap, (w2 + w1, n2))
        return time if len(visited) == n else -1

