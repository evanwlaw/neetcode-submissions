# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        We could have a function that merges 2 lists at a time and iterate through the list -> O(M*N) time where M is number of lists and N is number of nodes. Repetitive work to compare.

        Use heap to efficient add once to output linked list

        Initially, add the first node in each list (each one is already sorted). 

        While heap is not none, keep poping from heap and add to output linked list
            Push the popped node's neighbor to heap

        Push/Pop op of heap is O(logN) time.


        """

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node)) # i is tiebreaker

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            
            # add to output LL
            curr.next = node
            curr = curr.next
            node = node.next

            # push to heap if neighbor exists
            if node:
                heapq.heappush(heap, (node.val, i, node))
        return dummy.next




