class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # edge adjacency list
        edge_adj = defaultdict(list) # u : (v,w)
        for u, v, w in times:
            edge_adj[u].append((v,w))

        # minheap (weight, node)
        min_heap = [(0,k)]
        # djikstra's on minheap
        visited = set()
        t = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(w1,t)

            for n2, w2 in edge_adj[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1+w2, n2))            
        return t if len(visited) == n else -1