import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        input is a list of points [xi, yi]

        need to return a list of len k of the points closest to 0, 0 origin
        
        distance = ((x**2) + (y**2))

        We can run through the given points list
            calc distance
            put into heap [(distance, x, y)]
            if heap > k,
                pop from heap

        build output list from heap

        return output

        python heap is minheap.
        so we can use a maxheap by marking distances as negative when calculating

        Time Complexity: O(N log N) - popping/pushing into heap will take at most O(N log N time) + the O(N) time to build the output
        Space Complexity: O(k) - heap will be at most k items.
        """
        
        if len(points) <= 1:
            return points
        
        maxHeap = []
        for x, y in points:
            distance = -((x**2) + (y**2))
            heapq.heappush(maxHeap, [distance, x, y])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        output = []

        for d, x, y in maxHeap:
            output.append([x,y])
        return output


 
