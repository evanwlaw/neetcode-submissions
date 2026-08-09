import heapq
class MedianFinder:
    """
    1. Need to have a sorted list. Use two heaps for all inputs. use maxheap on lower half. Use minheap on upper half. Need to get middle value(s).
    2. A list can get median in O(1) but takes O(N) to insert. Heaps is O(logN) insert and O(1) to get median.
    3. I would not be able to get the rebalancing of lists and the max heap implementation myself
    """
    def __init__(self):
        self.lower, self.higher = [], []
        

    def addNum(self, num: int) -> None:
        # add num to lower half/max heap
        heapq.heappush(self.lower, -1 * num)

        # make sure num is smaller than in higher
        if (self.lower and self.higher and (-1 * self.lower[0]) > self.higher[0]):
            temp = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.higher, temp)
        
        # balance heaps
        if len(self.lower) > len(self.higher):
            temp = -1 * heapq.heappop(self.lower)
            heapq.heappush(self.higher, temp)

        if len(self.lower) < len(self.higher):
            temp = -1 * heapq.heappop(self.higher)
            heapq.heappush(self.lower, temp)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.higher):
            return -1 * self.lower[0]
        elif len(self.lower) < len(self.higher):
            return self.higher[0]
        else:
            return ((-1 * self.lower[0]) + self.higher[0]) / 2
        