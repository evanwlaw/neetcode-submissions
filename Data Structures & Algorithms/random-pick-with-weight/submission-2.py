import random
class Solution:
    """
    return random idx of weight probability
    w = [1,3]
    0   1
    1   3   4
    .25 .75 1

    0   1   2   3
    1   3   2   4   10
    .2  .3  .2  .4  1

    We can find a number from 1-10. and then use the weights[i] as buckets of where the number ranges are.

    0       1       2       3
    1       3       2       4   10
    
    idx 0: [1]
    idx 1: (1:4]
    idx 2: (4:6]
    idx 3: (6:10]

    """
    def __init__(self, w: List[int]):
        self.buckets = []
        runningSum = 0
        for i in w:
            runningSum += i
            self.buckets.append(runningSum)


    def pickIndex(self) -> int:
        target = random.randint(1, self.buckets[-1])
        l, r = 0, len(self.buckets) - 1

        while l < r:
            m = l + (r-l) // 2
            if target > self.buckets[m]:
                l = m + 1
            else:
                r = m
        return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()