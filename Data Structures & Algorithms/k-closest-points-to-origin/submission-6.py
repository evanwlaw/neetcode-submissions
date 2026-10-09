import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        return the k closest to origin

        distance is sqrt((x1 - x2)^2 + (y1 - y2)^2))

        since x2, y2 are 0,0 -> sqrt(x1**2 + y1**2)

        we want to keep k of the shortest -> reject longer distances. So we can use a maxHeap to hold k len of the smallest distances. if we go over k len, then we pop the largest distance.
        
        """
        maxHeap = []
        for x, y in points:
            distance = -(x**2 + y**2)
            
            heapq.heappush(maxHeap, [distance, x,y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [[x, y] for dist, x,y in maxHeap]

