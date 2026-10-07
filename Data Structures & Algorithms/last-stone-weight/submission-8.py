import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Input: stones = [2,3,6,2,4]
        Output: 1

        we want to get the top two largest stones -> get difference if not equal and put it back into our pile

        max heap can be used to get the top two stones. each value in heap represents the stones

        after heapify via python (need to negate):
        -6  -4  -3  -2  -2

        smash first time: 6 - 4 = 2
        -3  -2  -2  -2

        smash second time: 3 - 2 = 1
        -2  -2  -1

        smash third time: -2 == -2 -> nothing
        -1

        since len of heap is == 1 -> return 1
        """
        if not stones:
            return 0
        
        if len(stones) == 1:
            return stones[0]

        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones) * -1
            y = heapq.heappop(stones) * -1
            if x > y:
                heapq.heappush(stones, -(x-y))
            
        return 0 if not stones else stones[0] * -1




