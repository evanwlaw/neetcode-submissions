import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        return kth largest
        2   3   1   5   4 -> return 2
        
        minHeap of size k
        2   3
        Time: O(n log k) - better than sort O(nlogn)
        Space: O(k)
        """

        minHeap = []

        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
