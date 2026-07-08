import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # djikstra's

        # min_heap -> (weight, node) pop/process min time
        # (3,4) will be processed before (4,4)
        # if in visited, skip
        # in each neighbor edge, it's curr weight plus prev weight

        # 1st - adj list
        edge_adj = defaultdict(list)

        for u,v,w in times: # u : [(v,w),(v,w),...]
            edge_adj[u].append((v,w))
        
        min_heap = [(0,k)]
        time = 0
        visited = set()

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = w1

            for n2, w2 in edge_adj[n1]:
                if n2 in visited:
                    continue
                heapq.heappush(min_heap, (w1 + w2, n2))
        return time if len(visited) == n else -1

