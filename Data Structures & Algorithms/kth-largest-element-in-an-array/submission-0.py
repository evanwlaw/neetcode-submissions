class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Use min heap. Maintain k elements in heap.
        Heap[0] is the kth
        TC: O(n log k)
        SC: O(n)

        """
        heap = []

        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]