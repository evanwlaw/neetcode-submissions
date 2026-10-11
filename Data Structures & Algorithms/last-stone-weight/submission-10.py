import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Input: stones = [2,3,6,2,4]
        Output: 1

        -6  -4   -3  -2  -2

        use a maxheap to get largest two stones
        """

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1

            if x > y:
                heapq.heappush(stones, -(x - y))
        return -stones[0] if stones else 0