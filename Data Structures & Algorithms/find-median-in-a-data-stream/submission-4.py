import heapq
class MedianFinder:
    def __init__(self):
        self.lower, self.upper = [], []

    def addNum(self, num):
        if self.upper and num > self.upper[0]: # push to upper
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num) # push to lower by default

        # balance heaps
        if len(self.lower) > len(self.upper) + 1:
            temp = heapq.heappop(self.lower)
            heapq.heappush(self.upper, -temp)

        if len(self.lower) + 1 < len(self.upper):
            temp = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -temp)

    def findMedian(self):

        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        elif len(self.lower) < len(self.upper):
            return self.upper[0]
        else:
            return ((-1 * self.lower[0]) + self.upper[0]) / 2