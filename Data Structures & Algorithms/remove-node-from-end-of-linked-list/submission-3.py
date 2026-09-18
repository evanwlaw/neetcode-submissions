# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Input: head = [1,2,3,4], n = 2
        Output: [1,2,4]

        1   2   3   4
            s
                        f

        Use two ptrs -> slow and fast
        get fast ptr to be n nodes away from s.
        then increment both together until fast reaches end.
        Slow ptr should be at the node in front of the nth node
        Delete the nth node
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy.next

        while n > 0:
            n -= 1
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next
