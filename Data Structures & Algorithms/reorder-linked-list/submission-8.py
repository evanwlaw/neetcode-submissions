# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        cut in halves.

        reverse second half

        zip to first half
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow rn is just one node before half so copy slow.next as start of second half
        second = slow.next
        # cut first off
        slow.next = None

        prev = None
        #reverse second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # prev is now the new second
        second = prev
        first = head

        """
        2   4
        6   8
        """

        while first and second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
