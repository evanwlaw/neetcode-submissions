import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        minheap -> [dist, idx]

        """

        minHeap = [[0,0]]
        visited = set()
        output = 0

        while minHeap:
            dist, node = heapq.heappop(minHeap)
            if node not in visited:
                visited.add(node) # forgot to add this in my first run before i read solution

                x1, y1 = points[node]
                output += dist

                for node2, [x2, y2] in enumerate(points):
                    if node2 not in visited:
                        distance = abs(x1 - x2) + abs(y1 - y2)
                        heapq.heappush(minHeap, [distance, node2])
        return output

            