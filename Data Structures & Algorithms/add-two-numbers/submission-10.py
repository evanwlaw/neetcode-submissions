# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1   2   3
        4   5   6
        5   7   9
     
            1
        7   2   3   0   0
        8   9   9   1   1
        5
        return linkedlist
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        res = []

        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0

            value = l1Val + l2Val + carry
            
            carry = value // 10
            curr.next = ListNode(value % 10) # we just want digit

            # update ptrs and carry after using it
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        
        return dummy.next


