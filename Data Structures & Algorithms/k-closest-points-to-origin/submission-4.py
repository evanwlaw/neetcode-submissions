import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_heap = []

        for x, y in points:
            dist = -((x**2) + (y**2))
            heapq.heappush(dist_heap, [dist, [x,y]])
            if len(dist_heap) > k:
                heapq.heappop(dist_heap)

            
        return [point for _, point in dist_heap]