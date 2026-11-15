import random
class Solution:
    """
    1      3       2       4       -> 10
    1     (1,4]   (4,6]    (6,10]
    binary search buckets
    """
    def __init__(self, w: List[int]):
        self.buckets = []
        runningSum = 0
        for i in range(len(w)):
            runningSum += w[i]
            self.buckets.append(runningSum)
    def pickIndex(self) -> int:
        l, r = 0, len(self.buckets)
        target = random.randint(1, self.buckets[-1])

        while l < r:
            middle = l + (r - l) // 2

            if self.buckets[middle] < target:
                l = l + 1
            else:
                r = middle
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()