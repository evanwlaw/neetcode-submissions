import heapq

class MedianFinder:
    def __init__(self):
        self.lower = [] # max heap
        self.higher = [] # min heap


    def addNum(self, num):
        # insert to lower
        heapq.heappush(self.lower, -1 * num)
        # check if nums are in right heap
        if (self.lower and self.higher and (-1 * self.lower[0]) > self.higher[0]):
            temp = heapq.heappop(self.lower) * -1
            heapq.heappush(self.higher, temp)

        # balance heaps. can have either heap +1 of the other
        # but only move if at least +2 otherwise number will go back and forth
        if len(self.lower) > len(self.higher) + 1:
            temp = heapq.heappop(self.lower) * -1
            heapq.heappush(self.higher, temp)
        if len(self.lower) + 1 < len(self.higher):
            temp = heapq.heappop(self.higher) * -1
            heapq.heappush(self.lower, temp)


    def findMedian(self):
        if len(self.lower) > len(self.higher):
            return self.lower[0] * -1
        elif len(self.lower) < len(self.higher):
            return self.higher[0]
        else:
            return (-1 * self.lower[0] + self.higher[0]) / 2
