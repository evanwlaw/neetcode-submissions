# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Input: head = [1,2,3,4], n = 3
        Output: [1,2,4]

        1   >   2   >   3   >   4
        s   
                                f

        two prts -> have the distance between them as n

        1. fast ptr gets to n distance
        2. then increment both until fast hits end
        3. delete node
            slow.next = slow.next.next

        Use a dummy node in case if first node is the one needing to be deleted

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

        
