import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        use min heap of len k
        [4  5]
        '''

        min_heap = []

        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)

            elif n > min_heap[0]:
                heapq.heappushpop(min_heap, n)
        return min_heap[0]