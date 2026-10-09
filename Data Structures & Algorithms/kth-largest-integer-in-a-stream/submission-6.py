import heapq
class KthLargest:
    """
    find the kth largest int in stream

    use a minheap of len k. we can peek at the end (kth) in constant space

    we want to pop the smallest items leaving kth largest
    
    """
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
