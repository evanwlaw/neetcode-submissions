import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Input: points = [[0,2],[2,0],[2,2]], k = 2
        Output: [[0,2],[2,0]]

        We need to keep track of the distance between the points to 0,0.
        and we also need to map the distance to the point itself so we can return it.

        I think a heap is a good data structure.
        Heap -> [(dist, pointcoord)]

        Iterate through points:
            calc distance from point to 0,0
            push to heap
        Iterate k times:
            pop from heap -> put into output list

        return output

        Time: O(O(NLOGN)) - It takes O(N) to go through all the points. And may need to rebalance heap. O(NLOGN)
        Space: O(N) - Heap is needed to hold all points and distance pairs
        """ 

        dist_heap = []

        for x, y in points:
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(dist_heap, [dist, [x,y]])
        
        output = []
        for i in range(k):
            output.append(heapq.heappop(dist_heap)[1])
        return output
