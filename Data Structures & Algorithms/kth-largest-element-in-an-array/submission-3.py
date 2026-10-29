import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        we want to get k th largest -> heap

        min or max?

        Input: nums = [2,3,1,5,4], k = 2
        1   2   3   4   5 -> return 4

        we want to keep the largest -> min heap

        min heap len 2:
        2, 3 -> insert 1 ->  1 2 3 -> pop 1 since len > 2: 2 3
        2, 3 -> insert 5 ->  2 3 5 -> pop 2 since len > 2: 3 5
        3, 5 -> insert 4 ->  3 4 5  -> pop 3 since len> 2: 4 5
        return heap[-1]

        so mmin heap

        """
        minHeap = []
        for n in nums:
            heapq.heappush(minHeap, n)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]