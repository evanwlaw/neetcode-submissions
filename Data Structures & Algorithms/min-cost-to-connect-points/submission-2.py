import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        use minheap from node to closest other point via manhattan dist


        """

        minHeap = [[0,0]] # [cost, pt idx]
        output = 0
        visited = set()

        while minHeap:
            d1, p1Idx = heapq.heappop(minHeap)

            if p1Idx not in visited:
                visited.add(p1Idx)
                x1, y1 = points[p1Idx]
                output += d1

                for i, (x2, y2) in enumerate(points):
                    if i not in visited:
                        dist = abs(x1 - x2) + abs(y1 - y2)
                        heapq.heappush(minHeap, [dist, i])
        return output 

