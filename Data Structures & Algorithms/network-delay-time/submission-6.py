class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        weights wont be negative

        we need to return the min it takes for n nodes to receive signal (aka traversed).

        input -> list of [ui, vi, ti]
            - u is source node
            - v is target node
            - t is time/weight -> could be 0
        
        n = nodes
        k = starting node

        track the min time to get to node -> array size n + 1-> i is the node val is the time
        start with inf
        0       1       2       3       4
        inf     inf     inf     inf     inf

        Input: times = [[1,2,1],[2,3,1],[1,4,4],[3,4,1]], n = 4, k = 1

        addList Map {node : [neighbor, weight]}
        1 : [2, 1], [4, 4]
        2 : [3, 1]
        3 : [4, 1]
        
        bfs traverse from starting node
        priority queue = [startingnode, weight of 0]

        visited = set()

        while queue
            for each neighbor of popped ndoe:
                if neighbor weight < trackWeight[1] -> update trackWeight[1]
                    append neighbor to queue

        
        0       1       2       3       4
        inf     0       1     inf     inf
        
        """
        adjList = defaultdict(list) # u : [v, t]
        for u, v, t in times:
            adjList[u].append([v, t])
        
        # trackWeight = [float("inf") for _ in range(n + 1)]

        queue = [[0, k]]
        visited = set()
        time = 0

        while queue:
            t, node = heapq.heappop(queue)
            if node not in visited:
                visited.add(node)
                time = t

                for nei, t2 in adjList[node]:
                    if nei not in visited:
                        heapq.heappush(queue, [t+t2, nei])
        return time if len(visited) == n else -1
