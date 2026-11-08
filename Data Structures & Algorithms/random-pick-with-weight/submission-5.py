import random
class Solution:
    """
    1   3   2   4   -> 10

    randint from 1:10 -> binary search to get idx

    buckets
    0       1       2       3
    1       4       6       10
    (1:1]   (1:4]   (4:6]   (6:10]
    """
    def __init__(self, w: List[int]):
        self.buckets = []
        runningSum = 0
        for i in w:
            runningSum += i
            self.buckets.append(runningSum)

    def pickIndex(self) -> int:
        l, r = 0, len(self.buckets) - 1
        target = random.randint(1, self.buckets[-1])
        
        while l < r:
            m = l + (r - l) // 2

            if target > self.buckets[m]:
                l = m + 1
            else:
                r = m
        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()