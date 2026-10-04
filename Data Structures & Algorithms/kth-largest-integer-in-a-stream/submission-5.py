import heapq
class KthLargest:
    """
    use a minheap where we keep k number of values
    the top is the kth.

    add() ->
        push val to minheap
        if len of minheap > k:
            pop the top to keep k num
        return top of minheap
    
    ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

    beginning has heap of k len:
    [2,3,3]
    
    add 3:
    [2,3,3,3] -> pop top -> [3,3,3]. return top = 3
    
    add 5
    [3,3,3,5] -> popt top -> [3,3,5]. return top = 3
    add 6
    [3,3,5,6]. pop top -> [3,5,6] reutnr top = 3

    add 7
    [3,5,6,7]. pop top -> [5,6,7] return top = 7

    add 8
    [5,6,7,8]. pop top -> [6,7,8] return top = 6


    """
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]