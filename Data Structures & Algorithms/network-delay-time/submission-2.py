import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edge_adj = defaultdict(list) # u : [(v, w),..]
        min_heap = [(0,k)] # w,n
        visited = set()
        time = 0

        # populate adj list
        for u, v, w in times:
            edge_adj[u].append((v,w))

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = w1

            for n2,w2  in edge_adj[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1+w2, n2))
        return time if len(visited) == n else -1

        
