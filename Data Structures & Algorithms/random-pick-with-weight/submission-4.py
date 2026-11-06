import random
class Solution:
    """
    1   3   2   4 -> 10
    """
    def __init__(self, w: List[int]):
        self.rangeBuckets = [w[0]]
        for i in range(1, len(w)):
            self.rangeBuckets.append(self.rangeBuckets[i-1] + w[i])


    def pickIndex(self) -> int:
        target = random.randint(1, self.rangeBuckets[-1])
        l, r = 0, len(self.rangeBuckets) - 1

        while l < r:
            m = l + (r-l) // 2

            if target > self.rangeBuckets[m]:
                l = m + 1
            else:
                r = m
        return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()