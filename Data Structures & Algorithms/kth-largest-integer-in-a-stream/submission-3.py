class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap,val)
        elif val > self.minheap[0]:
            heapq.heappop(self.minheap)
            heapq.heappush(self.minheap, val)
        return self.minheap[0]
        
